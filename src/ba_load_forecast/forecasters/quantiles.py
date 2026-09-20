"""Quantile forecasts, minimal version: a 90% prediction interval around the day-ahead forecast.

Two ways to get the 5th, 50th and 95th percentiles of the load at each hour:

* ``QuantileBoosting``: three gradient-boosting models with the pinball loss, one per quantile, on the same
  rows as the point boosting. The 50th percentile is the point forecast.
* ``EmpiricalIntervals``: the point forecast of any base model, widened by the empirical quantiles of the
  base model's relative errors on the last ``window_days`` days whose load is known at the cut-off, per
  hour of the day. Cheap, and usually well calibrated on ordinary days; the study measures how it does on
  the cold mornings.

Both expose ``predict_quantiles(info) -> (3, 24)`` in the order of ``QUANTILES`` next to ``predict``.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

from ..features import rows_for_days, target_temperature, training_days
from ..information_set import InformationSet
from .base import Forecaster, ForecastError
from .boosting import Boosting
from .profile import regime

QUANTILES = (0.05, 0.5, 0.95)


class QuantileBoosting(Boosting):
    """Three boosted models with the pinball loss; ``predict`` is the median."""

    def __init__(self, *args, quantiles: tuple[float, ...] = QUANTILES, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantiles = quantiles
        self.models: dict[float, HistGradientBoostingRegressor] = {}
        if kwargs.get("name") is None:
            self.name = "qboost"

    def fit(self, info: InformationSet) -> None:
        days = training_days(info.day - timedelta(days=2), self.train_days)
        rows = rows_for_days(info.load_history, info.temp_history_f, days, self._station_frames(info, target=False),
                             labels=self.day_labels(info))
        rows = rows[rows["y"] > 0].dropna(subset=["y"])
        if len(rows) < 24 * self.min_train_days:
            raise ForecastError(f"only {len(rows) // 24} days of history to fit on")
        self.columns = self._columns(rows)
        x = rows[self.columns].to_numpy(dtype=float)
        y = rows["y"].to_numpy(dtype=float)
        self.models = {}
        for q in self.quantiles:
            self.models[q] = HistGradientBoostingRegressor(
                loss="quantile", quantile=q, max_iter=self.max_iter, learning_rate=self.learning_rate,
                max_leaf_nodes=self.max_leaf_nodes, early_stopping=True, validation_fraction=0.1, n_iter_no_change=20,
                random_state=self.seed,
            ).fit(x, y)
        self.model = self.models[0.5]
        self.fitted_on = info.day
        self.fitted_ba = info.ba

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        if np.isnan(info.temp_forecast_f).any():
            raise ForecastError("no weather forecast for the day")
        if self.needs_fit(info):
            self.fit(info)
        rows = rows_for_days(info.load_history, target_temperature(info), [info.day], self._station_frames(info, target=True),
                             labels=self.day_labels(info, target=True))
        x = rows[self.columns].to_numpy(dtype=float)
        q = np.vstack([self.models[qq].predict(x) for qq in self.quantiles])
        return np.sort(q, axis=0)                       # quantile crossing removed by sorting

    def predict(self, info: InformationSet) -> np.ndarray:
        return self.predict_quantiles(info)[list(self.quantiles).index(0.5)]


class EmpiricalIntervals:
    """The base model's forecast widened by the empirical quantiles of its recent relative errors, per hour."""

    def __init__(self, base: Forecaster, window_days: int = 60, min_days: int = 20,
                 quantiles: tuple[float, ...] = QUANTILES, name: str | None = None, by_regime: bool = False):
        """With ``by_regime`` the errors come from the known days of the window that had the same temperature
        regime as the target day (heating, mild, cooling by the forecast daily mean); with fewer than
        ``min_days`` such days, from every known day of the window. A cold morning is then judged by the
        errors of cold days, which are larger."""
        self.base = base
        self.window_days = window_days
        self.min_days = min_days
        self.quantiles = quantiles
        self.by_regime = by_regime
        self.name = name or f"emp_{base.name}"
        self._stored: dict[date, np.ndarray] = {}
        self._regime: dict[date, int | None] = {}

    @staticmethod
    def regime_of(info: InformationSet) -> int | None:
        t = info.temp_forecast_f
        return regime(float(np.nanmean(t))) if np.isfinite(t).sum() >= 18 else None

    def predict(self, info: InformationSet) -> np.ndarray:
        p = np.asarray(self.base.predict(info), dtype=float)
        self._stored[info.day] = p
        self._regime[info.day] = self.regime_of(info)
        for d in [d for d in self._stored if d < info.day - timedelta(days=self.window_days + 40)]:
            del self._stored[d]
            self._regime.pop(d, None)
        return p

    def relative_errors(self, info: InformationSet, only_regime: int | None = None) -> np.ndarray:
        """(n_days, 24) relative errors (actual - forecast) / forecast on the known days of the window."""
        first = info.day - timedelta(days=self.window_days + 2)
        rows = []
        for d, p in self._stored.items():
            if d < first or d > info.day - timedelta(days=2):
                continue
            if only_regime is not None and self._regime.get(d) != only_regime:
                continue
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            rows.append((actual - p) / p)
        return np.array(rows) if rows else np.empty((0, 24))

    def error_pool(self, info: InformationSet) -> np.ndarray:
        if self.by_regime:
            r = self.regime_of(info)
            if r is not None:
                e = self.relative_errors(info, only_regime=r)
                if len(e) >= self.min_days:
                    return e
        return self.relative_errors(info)

    def band(self, p: np.ndarray, e: np.ndarray, levels: tuple[float, ...]) -> np.ndarray:
        if len(e) < self.min_days:
            raise ForecastError(f"only {len(e)} known days of errors for the interval")
        out = np.empty((len(levels), 24))
        for h in range(24):
            eh = e[:, h]
            eh = eh[np.isfinite(eh)]
            if len(eh) < self.min_days:
                raise ForecastError(f"only {len(eh)} known errors at hour {h}")
            for i, q in enumerate(levels):
                out[i, h] = p[h] * (1.0 + np.quantile(eh, q))
        return np.sort(out, axis=0)

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        p = self.predict(info)
        return self.band(p, self.error_pool(info), self.quantiles)


class AdaptiveIntervals(EmpiricalIntervals):
    """Empirical intervals whose nominal level adapts to the coverage actually achieved.

    Adaptive conformal inference (Gibbs and Candes 2021, arXiv:2106.00170): the miscoverage level used to
    read the error quantiles is updated once for every day whose outcome becomes known,
    ``alpha <- alpha + gamma * (target - miss)``, where ``miss`` is the share of that day's hours that fell
    outside the interval issued for it. When the intervals have been too narrow (cold spell, storm) alpha
    falls and the next intervals widen; long-run coverage converges to ``1 - target`` without assuming that
    errors are exchangeable. The median is read at 0.5 as before.

    With ``by_regime`` the error pool is the regime-conditional one of ``EmpiricalIntervals`` (a longer window
    is then advisable), and with ``alpha_by_regime`` one level is tracked per temperature regime, so that the
    misses of a cold spell widen the next cold days and not the mild ones.
    """

    def __init__(self, base: Forecaster, target: float = 0.10, gamma: float = 0.02, window_days: int = 120,
                 min_days: int = 20, name: str | None = None, by_regime: bool = False, alpha_by_regime: bool = False):
        super().__init__(base, window_days=window_days, min_days=min_days, name=name or f"aci_{base.name}",
                         by_regime=by_regime)
        self.target = target
        self.gamma = gamma
        self.alpha_by_regime = alpha_by_regime
        self.alphas: dict[int | None, float] = {}          # level per regime (key None: the single level)
        self._issued: dict[date, tuple[np.ndarray, np.ndarray]] = {}
        self._scored: set[date] = set()

    @property
    def alpha(self) -> float:
        return self.alphas.get(None, self.target)

    def level_key(self, d: date) -> int | None:
        return self._regime.get(d) if self.alpha_by_regime else None

    def update_alpha(self, info: InformationSet) -> None:
        for d in sorted(self._issued):
            if d in self._scored or d > info.day - timedelta(days=2):
                continue
            lo, hi = self._issued[d]
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            ok = np.isfinite(actual)
            self._scored.add(d)
            if ok.sum() < 20:
                continue
            miss = float(((actual[ok] < lo[ok]) | (actual[ok] > hi[ok])).mean())
            key = self.level_key(d)
            self.alphas[key] = float(np.clip(self.alphas.get(key, self.target) + self.gamma * (self.target - miss), 0.005, 0.5))
        for d in [d for d in self._issued if d < info.day - timedelta(days=self.window_days + 40)]:
            del self._issued[d]
            self._scored.discard(d)

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        p = self.predict(info)
        self.update_alpha(info)
        alpha = self.alphas.get(self.level_key(info.day), self.target)
        q = self.band(p, self.error_pool(info), (alpha / 2.0, 0.5, 1.0 - alpha / 2.0))
        self._issued[info.day] = (q[0], q[-1])
        return q
