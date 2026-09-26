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
        self._tmin: dict[date, float] = {}

    @staticmethod
    def regime_of(info: InformationSet) -> int | None:
        t = info.temp_forecast_f
        return regime(float(np.nanmean(t))) if np.isfinite(t).sum() >= 18 else None

    def predict(self, info: InformationSet) -> np.ndarray:
        p = np.asarray(self.base.predict(info), dtype=float)
        self._stored[info.day] = p
        self._regime[info.day] = self.regime_of(info)
        self._tmin[info.day] = float(np.nanmin(info.temp_forecast_f)) if np.isfinite(info.temp_forecast_f).any() else np.nan
        for d in [d for d in self._stored if d < info.day - timedelta(days=self.window_days + 40)]:
            del self._stored[d]
            self._regime.pop(d, None)
            self._tmin.pop(d, None)
        return p

    def known_days(self, info: InformationSet, only_regime: int | None = None) -> list[date]:
        first = info.day - timedelta(days=self.window_days + 2)
        return [d for d in self._stored if first <= d <= info.day - timedelta(days=2)
                and (only_regime is None or self._regime.get(d) == only_regime)]

    def errors_of(self, info: InformationSet, days: list[date]) -> np.ndarray:
        """(n_days, 24) relative errors (actual - forecast) / forecast on the given known days."""
        rows = []
        for d in days:
            p = self._stored[d]
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            rows.append((actual - p) / p)
        return np.array(rows) if rows else np.empty((0, 24))

    def relative_errors(self, info: InformationSet, only_regime: int | None = None) -> np.ndarray:
        """(n_days, 24) relative errors on the known days of the window (of one regime when asked)."""
        return self.errors_of(info, self.known_days(info, only_regime))

    def pool_days(self, info: InformationSet) -> list[date]:
        """The known days whose errors describe the target day: those of its regime when enough, else all."""
        if self.by_regime:
            r = self.regime_of(info)
            if r is not None:
                same = self.known_days(info, only_regime=r)
                if len(same) >= self.min_days:
                    return same
        return self.known_days(info)

    def error_pool(self, info: InformationSet) -> np.ndarray:
        return self.errors_of(info, self.pool_days(info))

    def peak_errors(self, info: InformationSet, days: list[date]) -> np.ndarray:
        """The relative error at the hour of the actual peak, one value per known day."""
        out = []
        for d in days:
            p = self._stored[d]
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            if np.isfinite(actual).sum() < 20:
                continue
            h = int(np.nanargmax(actual))
            out.append((actual[h] - p[h]) / p[h])
        return np.array(out)

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

    Two refinements for the coldest days, where the regime pool still mixes a -15 C day with a +5 C one:
    ``nearest=k`` keeps, of the pool, only the ``k`` known days closest to the target day in forecast daily
    minimum temperature (the regime pool is used when fewer than ``min_days`` qualify); ``tail=True`` reads the
    outer quantiles from an exponential fitted to the errors beyond the pool 10th and 90th percentiles instead
    of from the empirical distribution, so that a level below the smallest observed error is still defined.
    """

    def __init__(self, base: Forecaster, target: float = 0.10, gamma: float = 0.02, window_days: int = 120,
                 min_days: int = 20, name: str | None = None, by_regime: bool = False, alpha_by_regime: bool = False,
                 nearest: int | None = None, tail: bool = False, peak: str | None = None, peak_window: float = 0.97,
                 peak_quantile: float = 0.55, peak_quantile_cold: float | None = None, cold_decile: float = 0.10,
                 extra_levels: tuple[float, ...] = (), peak_quantile_hot: float | None = None, hot_decile: float = 0.90,
                 cold_by_max: bool = False, cold_source: str = "path"):
        super().__init__(base, window_days=window_days, min_days=min_days, name=name or f"aci_{base.name}",
                         by_regime=by_regime)
        self.target = target
        self.gamma = gamma
        self.alpha_by_regime = alpha_by_regime
        self.nearest = nearest
        self.tail = tail
        self.peak = peak                      # None, "lift" or "quantile" (see peak_adjust)
        self.peak_window = peak_window        # hours whose forecast is within this fraction of the forecast maximum
        self.peak_quantile = peak_quantile
        self.peak_quantile_cold = peak_quantile_cold   # the peak quantile on the coldest days (forecast minimum in the bottom decile)
        self.cold_decile = cold_decile
        self.peak_quantile_hot = peak_quantile_hot     # the peak quantile on the hottest days (forecast maximum in the top decile)
        self.hot_decile = hot_decile
        self.cold_by_max = cold_by_max                 # a day is also cold when its forecast maximum is in the coldest decile of maxima
        # where the day's forecast minimum comes from: "path" (the temperature path) or an NBM daily element such as
        # "mint18p50" / "mint18p05" (info.nbm_daily; falls back to the path when the day has no NBM products)
        self.cold_source = cold_source
        self._tmin_src: dict[date, float] = {}
        self._tmax: dict[date, float] = {}
        self.extra_levels = tuple(sorted(extra_levels))   # further quantiles issued next to the band (CRPS, tail analysis)
        self.last_extra: tuple[date, np.ndarray] | None = None
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

    def pool_days(self, info: InformationSet) -> list[date]:
        days = super().pool_days(info)
        if self.nearest is None:
            return days
        tmin = self._tmin.get(info.day, np.nan)
        if np.isfinite(tmin) and len(days) > self.nearest:
            def distance(d):
                t = self._tmin.get(d, np.nan)
                return abs(t - tmin) if np.isfinite(t) else np.inf
            days = sorted(days, key=distance)[: self.nearest]
        return days

    def band(self, p: np.ndarray, e: np.ndarray, levels: tuple[float, ...]) -> np.ndarray:
        q = super().band(p, e, levels)
        if not self.tail:
            return q
        lo_level, hi_level = levels[0], levels[-1]
        for h in range(24):
            eh = e[:, h]
            eh = eh[np.isfinite(eh)]
            q10, q90 = np.quantile(eh, 0.10), np.quantile(eh, 0.90)
            low = q10 - eh[eh < q10]
            high = eh[eh > q90] - q90
            if lo_level < 0.10 and len(low) >= 3:
                q[0, h] = p[h] * (1.0 + q10 - low.mean() * np.log(0.10 / lo_level))
            if hi_level > 0.90 and len(high) >= 3:
                q[-1, h] = p[h] * (1.0 + q90 + high.mean() * np.log(0.10 / (1.0 - hi_level)))
        return np.sort(q, axis=0)

    def source_min(self, info: InformationSet) -> float:
        """The day's forecast minimum by ``cold_source``: the path, or an NBM daily element when the day has it."""
        t = np.asarray(info.temp_forecast_f, dtype=float)
        path_min = float(np.nanmin(t)) if np.isfinite(t).any() else np.nan
        if self.cold_source != "path" and info.nbm_daily and np.isfinite(info.nbm_daily.get(self.cold_source, np.nan)):
            return float(info.nbm_daily[self.cold_source])
        return path_min

    def _known_extremes(self, info: InformationSet) -> tuple[float, float, np.ndarray, np.ndarray]:
        t = np.asarray(info.temp_forecast_f, dtype=float)
        tmin = self.source_min(info)
        tmax = float(np.nanmax(t)) if np.isfinite(t).any() else np.nan
        self._tmax.setdefault(info.day, tmax)
        self._tmin_src.setdefault(info.day, tmin)
        source = self._tmin if self.cold_source == "path" else self._tmin_src
        known_min = np.array([v for d, v in source.items() if d < info.day and np.isfinite(v)])
        known_max = np.array([v for d, v in self._tmax.items() if d < info.day and np.isfinite(v)])
        return tmin, tmax, known_min, known_max

    def is_cold_day(self, info: InformationSet) -> bool:
        """The target day's forecast minimum is in the coldest ``cold_decile`` of the known days' minima (or, with
        ``cold_by_max``, its forecast maximum in the coldest decile of the known maxima: a day cold all through)."""
        tmin, tmax, known_min, known_max = self._known_extremes(info)
        if not np.isfinite(tmin) or len(known_min) < 100:
            return False
        if tmin <= np.quantile(known_min, self.cold_decile):
            return True
        return bool(self.cold_by_max and len(known_max) >= 100 and tmax <= np.quantile(known_max, self.cold_decile))

    def is_hot_day(self, info: InformationSet) -> bool:
        """The target day's forecast maximum is in the hottest ``1 - hot_decile`` of the known days' maxima."""
        _, tmax, _, known_max = self._known_extremes(info)
        if not np.isfinite(tmax) or len(known_max) < 100:
            return False
        return bool(tmax >= np.quantile(known_max, self.hot_decile))

    def peak_level(self, info: InformationSet) -> float:
        if self.peak_quantile_cold is not None and self.is_cold_day(info):
            return self.peak_quantile_cold
        if self.peak_quantile_hot is not None and self.is_hot_day(info):
            return self.peak_quantile_hot
        return self.peak_quantile

    def peak_adjust(self, info: InformationSet, p: np.ndarray, e: np.ndarray, q: np.ndarray, days: list[date]) -> np.ndarray:
        """Shift the band upward around the forecast peak.

        The corrected point is a median per hour of the day; the actual peak is a maximum over noisy hours and the
        error measured at it is biased downward even for an unbiased forecast. ``"lift"`` replaces, at the hours
        within ``peak_window`` of the forecast maximum, the hourly median correction by the median of the errors
        measured at the actual peak hour of the pool days (half of the difference at the neighbouring hours);
        ``"quantile"`` reads the point at ``peak_quantile`` instead of the median at those hours (and at the
        mid-point between the two at the neighbours). The whole band moves with the point.
        """
        window = p >= self.peak_window * np.nanmax(p)
        weight = window.astype(float)
        weight[1:] = np.maximum(weight[1:], 0.5 * window[:-1])
        weight[:-1] = np.maximum(weight[:-1], 0.5 * window[1:])
        shift = np.zeros(24)
        if self.peak == "lift":
            pe = self.peak_errors(info, days)
            if len(pe) < self.min_days:
                return q
            m_peak = float(np.median(pe))
            for h in range(24):
                eh = e[:, h]
                eh = eh[np.isfinite(eh)]
                shift[h] = weight[h] * p[h] * (m_peak - float(np.median(eh)))
        elif self.peak == "quantile":
            peak_q = self.peak_level(info)
            for h in range(24):
                eh = e[:, h]
                eh = eh[np.isfinite(eh)]
                level = 0.5 + weight[h] * (peak_q - 0.5)
                shift[h] = p[h] * (float(np.quantile(eh, level)) - float(np.median(eh)))
        return q + np.maximum(shift, 0.0)[None, :]

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        p = self.predict(info)
        self.update_alpha(info)
        alpha = self.alphas.get(self.level_key(info.day), self.target)
        days = self.pool_days(info)
        e = self.errors_of(info, days)
        q = self.band(p, e, (alpha / 2.0, 0.5, 1.0 - alpha / 2.0))
        if self.peak:
            q = self.peak_adjust(info, p, e, q, days)
        self._issued[info.day] = (q[0], q[-1])
        if self.extra_levels:
            qx = self.band(p, e, self.extra_levels)
            if self.peak:
                qx = qx + (q[1] - self.band(p, e, (0.5,))[0])[None, :]     # the same peak shift as the band
            self.last_extra = (info.day, qx)
        return q
