"""Hourly feature rows for the direct day-ahead models (additive, boosting), built the same way for the
training days and for the target day, and causal by construction.

For a day ``d`` and hour ``h`` the row holds what a forecaster had at 9 a.m. of ``d-1``:

* calendar: hour, day type (workday, Saturday-like, Sunday-like), special-day kind, day of the year, trend;
* temperature at ``(d, h)`` and its recent past (lags 1 to 3 h, moving averages 6, 12, 24 h), the day's
  mean, minimum and maximum; for the training days these come from the observed series, for the target
  day from the observed series up to the cut-off followed by the HRRR path;
* load: the value at the same hour of the last fully known day (``d-1`` for hours up to 08:00, ``d-2``
  after), at the same hour of ``d-7``, and the mean of the 24 hours before the cut-off.

``rows_for_days`` returns one row per (day, hour) with the target ``y`` where the load is known.
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date, timedelta

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types, special_days

from .cutoff import CUTOFF_LOCAL_HOUR

EPOCH = pd.Timestamp("2015-01-01")
LAGS = (1, 2, 3)
MOVING_AVGS = (6, 12, 24)
TEMP_COLUMNS = ["t", *[f"t_lag{k}" for k in LAGS], *[f"t_ma{m}" for m in MOVING_AVGS], "t_day_mean", "t_day_min", "t_day_max"]
LOAD_COLUMNS = ["l_last_known", "l_d7", "l_mean24"]
CALENDAR_COLUMNS = ["hour", "day_type", "special_kind", "doy_sin", "doy_cos", "trend"]
FEATURE_COLUMNS = [*CALENDAR_COLUMNS, *TEMP_COLUMNS, *LOAD_COLUMNS]


def hourly_index(days: list[date]) -> pd.DatetimeIndex:
    return pd.DatetimeIndex([pd.Timestamp(d) + pd.Timedelta(hours=h) for d in days for h in range(24)])


def temperature_features(temp: pd.Series, ts: pd.DatetimeIndex) -> pd.DataFrame:
    """The temperature columns for the hours ``ts`` from an hourly series covering them and the day before."""
    t = temp.asfreq("h") if not temp.empty else temp
    out = pd.DataFrame(index=ts)
    out["t"] = t.reindex(ts).to_numpy()
    for k in LAGS:
        out[f"t_lag{k}"] = t.shift(k, freq="h").reindex(ts).to_numpy()
    for m in MOVING_AVGS:
        out[f"t_ma{m}"] = t.rolling(m, min_periods=m).mean().shift(1, freq="h").reindex(ts).to_numpy()
    days = ts.normalize()
    daily = pd.DataFrame({"day": days, "t": out["t"].to_numpy()}).groupby("day")["t"]
    out["t_day_mean"] = daily.transform("mean").to_numpy()
    out["t_day_min"] = daily.transform("min").to_numpy()
    out["t_day_max"] = daily.transform("max").to_numpy()
    return out


def load_features(load: pd.Series, ts: pd.DatetimeIndex) -> pd.DataFrame:
    """The load columns for the hours ``ts`` (only values known at 9 a.m. of the day before)."""
    lo = load.asfreq("h") if not load.empty else load
    out = pd.DataFrame(index=ts)
    hours = ts.hour
    back = np.where(hours <= CUTOFF_LOCAL_HOUR - 1, 24, 48)
    out["l_last_known"] = lo.reindex(ts - pd.to_timedelta(back, unit="h")).to_numpy()
    out["l_d7"] = lo.reindex(ts - pd.Timedelta(days=7)).to_numpy()
    cutoffs = ts.normalize() - pd.Timedelta(days=1) + pd.Timedelta(hours=CUTOFF_LOCAL_HOUR - 1)
    mean24 = lo.rolling(24, min_periods=20).mean()
    out["l_mean24"] = mean24.reindex(cutoffs).to_numpy()
    return out


def calendar_features(ts: pd.DatetimeIndex) -> pd.DataFrame:
    out = pd.DataFrame(index=ts)
    out["hour"] = ts.hour
    out["day_type"] = day_types(ts.to_numpy())
    kinds: dict = {}
    for y in range(ts.min().year, ts.max().year + 1):
        kinds.update(special_days(y))
    days = ts.date
    out["special_kind"] = [0 if kinds.get(d) is None else int(kinds[d]) + 1 for d in days]
    doy = ts.dayofyear.to_numpy()
    out["doy_sin"] = np.sin(2 * np.pi * doy / 365.25)
    out["doy_cos"] = np.cos(2 * np.pi * doy / 365.25)
    out["trend"] = ((ts - EPOCH) / pd.Timedelta(days=365.25)).to_numpy()
    return out


def rows_for_days(load: pd.Series, temp: pd.Series, days: list[date], stations: pd.DataFrame | None = None,
                  labels: Mapping[date, int] | None = None) -> pd.DataFrame:
    """Feature rows for every hour of ``days`` with the target ``y`` (NaN where the load is unknown).

    ``stations``, when given, is an hourly frame with one temperature column per station; each becomes a
    column ``t_<name>`` (the target-day values must already be the forecast path). ``labels`` maps days to
    a data-driven day label (the shape cluster) and adds the column ``cluster`` (-1 where unknown).
    """
    ts = hourly_index(days)
    out = pd.concat([calendar_features(ts), temperature_features(temp, ts), load_features(load, ts)], axis=1)
    if stations is not None and len(stations.columns):
        st = stations.asfreq("h") if not stations.empty else stations
        for c in st.columns:
            out[f"t_{c}"] = st[c].reindex(ts).to_numpy()
    if labels is not None:
        out["cluster"] = [labels.get(d, -1) for d in ts.date]
    out["y"] = load.reindex(ts).to_numpy() if not load.empty else np.nan
    return out


def training_days(last: date, n_days: int) -> list[date]:
    """The ``n_days`` days ending at ``last`` (inclusive), oldest first."""
    return [last - timedelta(days=k) for k in range(n_days - 1, -1, -1)]


def target_temperature(info) -> pd.Series:
    """Observed temperature up to the cut-off followed by the HRRR path: the series the target day is built on."""
    observed = info.temp_history_f.asfreq("h") if len(info.temp_history_f) else info.temp_history_f
    path = pd.Series(info.temp_forecast_path_f, index=info.path_timestamps)
    return pd.concat([observed.loc[: path.index[0] - pd.Timedelta(hours=1)], path]).interpolate(limit=6, limit_area="inside")
