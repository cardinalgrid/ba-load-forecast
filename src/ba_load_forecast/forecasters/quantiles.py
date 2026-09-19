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
                 quantiles: tuple[float, ...] = QUANTILES, name: str | None = None):
        self.base = base
        self.window_days = window_days
        self.min_days = min_days
        self.quantiles = quantiles
        self.name = name or f"emp_{base.name}"
        self._stored: dict[date, np.ndarray] = {}

    def predict(self, info: InformationSet) -> np.ndarray:
        p = np.asarray(self.base.predict(info), dtype=float)
        self._stored[info.day] = p
        for d in [d for d in self._stored if d < info.day - timedelta(days=self.window_days + 40)]:
            del self._stored[d]
        return p

    def relative_errors(self, info: InformationSet) -> np.ndarray:
        """(n_days, 24) relative errors (actual - forecast) / forecast on the known days of the window."""
        first = info.day - timedelta(days=self.window_days + 2)
        rows = []
        for d, p in self._stored.items():
            if d < first or d > info.day - timedelta(days=2):
                continue
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            rows.append((actual - p) / p)
        return np.array(rows) if rows else np.empty((0, 24))

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        p = self.predict(info)
        e = self.relative_errors(info)
        if len(e) < self.min_days:
            raise ForecastError(f"only {len(e)} known days of errors for the interval")
        out = np.empty((len(self.quantiles), 24))
        for h in range(24):
            eh = e[:, h]
            eh = eh[np.isfinite(eh)]
            if len(eh) < self.min_days:
                raise ForecastError(f"only {len(eh)} known errors at hour {h}")
            for i, q in enumerate(self.quantiles):
                out[i, h] = p[h] * (1.0 + np.quantile(eh, q))
        return np.sort(out, axis=0)
