"""Multiple linear regression with recency effect, the "vanilla benchmark" of the load-forecasting literature.

Hong's benchmark model explains hourly load with a trend, the month, the day type by hour, and a cubic
polynomial of temperature interacted with the hour and with the month; the recency effect adds the
temperature of the previous hours (lags) and its moving averages, so that the load responds to how long
it has been cold, not only to how cold it is now (Hong, Pinson and Fan 2014,
doi:10.1016/j.ijforecast.2013.07.001; Wang, Liu and Hong 2016, doi:10.1016/j.ijforecast.2015.09.006).

Training uses the observed temperature; forecasting uses the HRRR path, which also supplies the hours
of D-1 after the cut-off that the lags and moving averages need. The model is refitted every
``refit_days`` days on the last ``train_days`` days of history, by ordinary least squares.
"""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types

from ..information_set import InformationSet
from .base import ForecastError

EPOCH = pd.Timestamp("2015-01-01")
TEMP_SCALE = 100.0


def design(ts: pd.DatetimeIndex, temp: pd.Series, day_type: np.ndarray, lags: tuple[int, ...],
           moving_avgs: tuple[int, ...], degree: int) -> np.ndarray:
    """The regressors for the hours ``ts`` given the hourly temperature series (which must cover them and
    the hours before them that the lags and moving averages need)."""
    n = len(ts)
    hour = ts.hour.to_numpy()
    month = ts.month.to_numpy() - 1
    t = temp.reindex(ts).to_numpy(dtype=float) / TEMP_SCALE
    cols = [np.ones(n), ((ts - EPOCH) / pd.Timedelta(days=365.25)).to_numpy(dtype=float)]
    cols.append(np.eye(12)[month])                                           # month
    cols.append(np.eye(72)[np.asarray(day_type) * 24 + hour])                # day type x hour
    powers = np.stack([t**p for p in range(1, degree + 1)], axis=1)         # T, T^2, T^3
    cols.append(powers)
    cols.append((powers[:, :, None] * np.eye(24)[hour][:, None, :]).reshape(n, -1))    # T^p x hour
    cols.append((powers[:, :, None] * np.eye(12)[month][:, None, :]).reshape(n, -1))   # T^p x month
    for k in lags:
        v = temp.shift(k, freq="h").reindex(ts).to_numpy(dtype=float) / TEMP_SCALE
        cols.append(np.stack([v**p for p in range(1, degree + 1)], axis=1))
    for m in moving_avgs:
        ma = temp.rolling(m, min_periods=m).mean().shift(1, freq="h")
        v = ma.reindex(ts).to_numpy(dtype=float) / TEMP_SCALE
        cols.append(np.stack([v**p for p in range(1, degree + 1)], axis=1))
    return np.column_stack([c if c.ndim == 2 else c[:, None] for c in cols])


class RecencyRegression:
    def __init__(self, train_days: int = 730, refit_days: int = 7, lags: tuple[int, ...] = (1, 2, 3),
                 moving_avgs: tuple[int, ...] = (6, 12, 24), degree: int = 3, min_train_days: int = 120):
        self.train_days = train_days
        self.refit_days = refit_days
        self.lags = lags
        self.moving_avgs = moving_avgs
        self.degree = degree
        self.min_train_days = min_train_days
        self.name = "recency_regression"
        self.coef: np.ndarray | None = None
        self.fitted_on: date | None = None
        self.fitted_ba: str | None = None

    def needs_fit(self, info: InformationSet) -> bool:
        return (self.coef is None or self.fitted_ba != info.ba or self.fitted_on is None
                or (info.day - self.fitted_on).days >= self.refit_days)

    def fit(self, info: InformationSet) -> None:
        hist = info.load_history
        temp = info.temp_history_f.asfreq("h") if len(info.temp_history_f) else info.temp_history_f
        start = pd.Timestamp(info.cutoff) - pd.Timedelta(days=self.train_days)
        y_all = hist.loc[start:]
        ok = y_all.notna() & (y_all > 0)
        ts = pd.DatetimeIndex(y_all.index[ok])
        if len(ts) < 24 * self.min_train_days:
            raise ForecastError(f"only {len(ts) // 24} days of history to fit on")
        x = design(ts, temp, day_types(ts.to_numpy()), self.lags, self.moving_avgs, self.degree)
        y = y_all[ok].to_numpy(dtype=float)
        rows = ~np.isnan(x).any(axis=1)
        if rows.sum() < 24 * self.min_train_days:
            raise ForecastError(f"only {rows.sum() // 24} complete days of load and temperature to fit on")
        self.coef = np.linalg.lstsq(x[rows], y[rows], rcond=None)[0]
        self.fitted_on = info.day
        self.fitted_ba = info.ba

    def predict(self, info: InformationSet) -> np.ndarray:
        if np.isnan(info.temp_forecast_f).any():
            raise ForecastError("no weather forecast for the day")
        if self.needs_fit(info):
            self.fit(info)
        observed = info.temp_history_f.asfreq("h") if len(info.temp_history_f) else info.temp_history_f
        path = pd.Series(info.temp_forecast_path_f, index=info.path_timestamps)
        temp = pd.concat([observed.loc[: path.index[0] - pd.Timedelta(hours=1)], path])
        temp = temp.interpolate(limit=6, limit_area="inside")     # short gaps in the observations before the cut-off
        ts = pd.DatetimeIndex(info.timestamps)
        x = design(ts, temp, np.full(24, info.day_type), self.lags, self.moving_avgs, self.degree)
        if not np.isfinite(x).all():
            raise ForecastError("missing temperature in the hours before the day for the lags and moving averages")
        return x @ self.coef
