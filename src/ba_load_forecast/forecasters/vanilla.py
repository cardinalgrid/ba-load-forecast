"""The vanilla benchmark of load forecasting: one linear regression on calendar and temperature (Hong 2010).

The model of the GEFCom2012 benchmark (Hong, Pinson and Fan 2014): for every hour

    load = b0 + b1 trend + month + weekday x hour + hour x (T, T^2, T^3) + month x (T, T^2, T^3)

with T the temperature of that hour, fitted by ordinary least squares on the last ``train_days`` fully known days
and refitted every ``refit_days``. On the target day T is the observed temperature up to the cut-off followed by
the forecast path, the same series every other model sees. It knows nothing of the recent load, holidays or the
weather models' errors: it is the floor a temperature-driven model must clear.
"""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from ..features import target_temperature, training_days
from ..information_set import InformationSet
from .base import ForecastError


def vanilla_design(index: pd.DatetimeIndex, temp_f: np.ndarray, origin: pd.Timestamp) -> np.ndarray:
    """The design matrix of the vanilla model for hourly timestamps ``index`` and temperatures ``temp_f`` (deg F)."""
    n = len(index)
    t = (np.asarray(temp_f, dtype=float) - 50.0) / 30.0           # scaled, so the cubes stay well conditioned
    hour = index.hour.to_numpy()
    month = index.month.to_numpy() - 1
    wday = index.dayofweek.to_numpy()
    trend = ((index - origin) / pd.Timedelta(days=365)).to_numpy(dtype=float)
    cols = [np.ones(n), trend]
    cols += [(month == m).astype(float) for m in range(1, 12)]
    cols += [((wday == w) & (hour == h)).astype(float) for w in range(7) for h in range(24) if (w, h) != (0, 0)]
    for p in (1, 2, 3):
        cols += [(hour == h) * t**p for h in range(24)]
        cols += [(month == m) * t**p for m in range(12)]
    return np.column_stack(cols)


class VanillaBenchmark:
    """Hong's vanilla regression, refitted every ``refit_days`` on ``train_days`` of known history."""

    def __init__(self, train_days: int = 1095, refit_days: int = 30, min_train_days: int = 365, name: str = "vanilla"):
        self.train_days = train_days
        self.refit_days = refit_days
        self.min_train_days = min_train_days
        self.name = name
        self.coef: np.ndarray | None = None
        self.fitted_on = None
        self.fitted_ba = None
        self.origin = pd.Timestamp("2015-01-01")

    def fit(self, info: InformationSet) -> None:
        days = training_days(info.day - timedelta(days=2), self.train_days)
        hours = pd.date_range(pd.Timestamp(days[0]), pd.Timestamp(days[-1]) + pd.Timedelta(hours=23), freq="h")
        y = info.load_history.reindex(hours).to_numpy(dtype=float)
        t = info.temp_history_f.reindex(hours).to_numpy(dtype=float)
        keep = np.isfinite(y) & np.isfinite(t) & (y > 0)
        if keep.sum() < 24 * self.min_train_days:
            raise ForecastError(f"only {int(keep.sum()) // 24} days of history to fit on")
        x = vanilla_design(hours[keep], t[keep], self.origin)
        self.coef = np.linalg.lstsq(x, y[keep], rcond=None)[0]
        self.fitted_on = info.day
        self.fitted_ba = info.ba

    def predict(self, info: InformationSet) -> np.ndarray:
        if np.isnan(info.temp_forecast_f).any():
            raise ForecastError("no weather forecast for the day")
        if self.coef is None or self.fitted_ba != info.ba or (info.day - self.fitted_on).days >= self.refit_days:
            self.fit(info)
        hours = pd.date_range(pd.Timestamp(info.day), periods=24, freq="h")
        t = target_temperature(info).reindex(hours).to_numpy(dtype=float)
        if np.isnan(t).any():
            raise ForecastError("temperature path incomplete for the day")
        return vanilla_design(hours, t, self.origin) @ self.coef
