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
from .weather_extra import apparent_temperature_f, weather_columns

EPOCH = pd.Timestamp("2015-01-01")
LAGS = (1, 2, 3)
MOVING_AVGS = (6, 12, 24)
TEMP_COLUMNS = ["t", *[f"t_lag{k}" for k in LAGS], *[f"t_ma{m}" for m in MOVING_AVGS], "t_day_mean", "t_day_min", "t_day_max"]
LOAD_COLUMNS = ["l_last_known", "l_d7", "l_mean24"]
CALENDAR_COLUMNS = ["hour", "day_type", "special_kind", "doy_sin", "doy_cos", "trend"]
FEATURE_COLUMNS = [*CALENDAR_COLUMNS, *TEMP_COLUMNS, *LOAD_COLUMNS]
COLD_F, HEAT_F = 32.0, 85.0
EXTREME_COLUMNS = ["cold_h", "cold_ma24", "cold_hours", "heat_h", "heat_ma24"]
# optional blocks (phase G): more load memory, and the thermal history and shape of the day
EXTRA_LOAD_COLUMNS = ["l_d14", "l_d21", "l_d7_mean24"]
EXTRA_TEMP_COLUMNS = ["t_prev_max", "t_prev_min", "hdh72", "cdh72", "t_day_range", "t_h07", "t_h17"]
BALANCE_F = 65.0


def extra_load_features(load: pd.Series, ts: pd.DatetimeIndex) -> pd.DataFrame:
    """Load two and three weeks back at the same hour, and the mean of the same weekday last week."""
    lo = load.asfreq("h") if not load.empty else load
    out = pd.DataFrame(index=ts)
    out["l_d14"] = lo.reindex(ts - pd.Timedelta(days=14)).to_numpy()
    out["l_d21"] = lo.reindex(ts - pd.Timedelta(days=21)).to_numpy()
    day_mean = lo.groupby(lo.index.normalize()).mean() if len(lo) else pd.Series(dtype=float)
    out["l_d7_mean24"] = day_mean.reindex(ts.normalize() - pd.Timedelta(days=7)).to_numpy()
    return out


def extra_temp_features(temp: pd.Series, ts: pd.DatetimeIndex) -> pd.DataFrame:
    """Yesterday's extremes, heating and cooling degree-hours of the 72 hours before the day (thermal inertia of
    buildings), the day's range and its temperature at 07:00 and 17:00 (the ramps)."""
    t = temp.asfreq("h") if not temp.empty else temp
    out = pd.DataFrame(index=ts)
    days = ts.normalize()
    daily = t.groupby(t.index.normalize()) if len(t) else None
    dmax = daily.max() if daily is not None else pd.Series(dtype=float)
    dmin = daily.min() if daily is not None else pd.Series(dtype=float)
    out["t_prev_max"] = dmax.reindex(days - pd.Timedelta(days=1)).to_numpy()
    out["t_prev_min"] = dmin.reindex(days - pd.Timedelta(days=1)).to_numpy()
    hdh = (BALANCE_F - t).clip(lower=0).rolling(72, min_periods=60).sum()
    cdh = (t - BALANCE_F).clip(lower=0).rolling(72, min_periods=60).sum()
    out["hdh72"] = hdh.reindex(days - pd.Timedelta(hours=1)).to_numpy()      # the 72 hours ending at 23:00 of D-1
    out["cdh72"] = cdh.reindex(days - pd.Timedelta(hours=1)).to_numpy()
    tt = t.reindex(ts)
    grp = pd.DataFrame({"day": days, "t": tt.to_numpy()}).groupby("day")["t"]
    out["t_day_range"] = (grp.transform("max") - grp.transform("min")).to_numpy()
    out["t_h07"] = t.reindex(days + pd.Timedelta(hours=7)).to_numpy()
    out["t_h17"] = t.reindex(days + pd.Timedelta(hours=17)).to_numpy()
    return out


def extreme_features(temp: pd.Series, ts: pd.DatetimeIndex) -> pd.DataFrame:
    """Explicit extreme terms: degrees below ``COLD_F`` (hour and 24 h mean), consecutive hours below it up to
    and including the hour, and degrees above ``HEAT_F`` (hour and 24 h mean). What a smooth response does
    not extrapolate on its own into a cold wave."""
    t = temp.asfreq("h") if not temp.empty else temp
    out = pd.DataFrame(index=ts)
    th = t.reindex(ts).to_numpy(dtype=float)
    ma = t.rolling(24, min_periods=24).mean().shift(1, freq="h").reindex(ts).to_numpy(dtype=float)
    out["cold_h"] = np.maximum(0.0, COLD_F - th)
    out["cold_ma24"] = np.maximum(0.0, COLD_F - ma)
    below = (t < COLD_F).astype(int)                                  # NaN counts as not cold
    run = below.groupby((below == 0).cumsum()).cumsum()
    out["cold_hours"] = run.reindex(ts).to_numpy(dtype=float)
    out["heat_h"] = np.maximum(0.0, th - HEAT_F)
    out["heat_ma24"] = np.maximum(0.0, ma - HEAT_F)
    return out


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
                  labels: Mapping[date, int] | None = None, sky: pd.DataFrame | None = None,
                  weather: pd.DataFrame | None = None) -> pd.DataFrame:
    """Feature rows for every hour of ``days`` with the target ``y`` (NaN where the load is unknown).

    ``stations``, when given, is an hourly frame with one temperature column per station; each becomes a
    column ``t_<name>`` (the target-day values must already be the forecast path). ``labels`` maps days to
    a data-driven day label (the shape cluster) and adds the column ``cluster`` (-1 where unknown).
    """
    ts = hourly_index(days)
    out = pd.concat([calendar_features(ts), temperature_features(temp, ts), load_features(load, ts),
                     extreme_features(temp, ts), extra_load_features(load, ts), extra_temp_features(temp, ts)], axis=1)
    if stations is not None and len(stations.columns):
        st = stations.asfreq("h") if not stations.empty else stations
        for c in st.columns:
            out[f"t_{c}"] = st[c].reindex(ts).to_numpy()
    if sky is not None:
        for c in sky.columns:                                # sun, cloud, their product; PV capacity terms when present
            out[c] = sky[c].reindex(ts).to_numpy(dtype=float)
    if weather is not None:                                  # dew point and wind (observed, then the HRRR path) and what follows
        dew = weather["dewpoint_f"].reindex(ts).to_numpy(dtype=float) if "dewpoint_f" in weather.columns else np.full(len(ts), np.nan)
        wind = weather["wind_ms"].reindex(ts).to_numpy(dtype=float) if "wind_ms" in weather.columns else np.full(len(ts), np.nan)
        for c, v in weather_columns(out["t"].to_numpy(dtype=float), dew, wind).items():
            out[c] = v
    if labels is not None:
        out["cluster"] = [labels.get(d, -1) for d in ts.date]
    out["y"] = load.reindex(ts).to_numpy() if not load.empty else np.nan
    return out


def apparent_series(temp: pd.Series, weather: pd.DataFrame | None) -> pd.Series:
    """The temperature series replaced by the apparent temperature (heat index, wind chill) wherever the dew
    point or the wind is known at that hour; the temperature itself elsewhere."""
    if weather is None or temp.empty:
        return temp
    dew = weather["dewpoint_f"].reindex(temp.index).to_numpy(dtype=float) if "dewpoint_f" in weather.columns else np.full(len(temp), np.nan)
    wind = weather["wind_ms"].reindex(temp.index).to_numpy(dtype=float) if "wind_ms" in weather.columns else np.full(len(temp), np.nan)
    return pd.Series(apparent_temperature_f(temp.to_numpy(dtype=float), dew, wind), index=temp.index)


def cold_weights(rows_index: pd.DatetimeIndex, temp: pd.Series, alpha: float, decile: float = 0.10,
                 scale_f: float = 10.0) -> np.ndarray:
    """One weight per training row: 1 plus ``alpha`` for every ``scale_f`` degrees the row's day has its observed
    minimum below the ``decile`` quantile of the daily minima of the training days (1 on every other day). Days
    far into the cold tail count more, so that six years with few extreme days do not regress the fit to the
    mean; the temperature is the observed history, known when the model is fitted."""
    days = pd.DatetimeIndex(rows_index).normalize()
    tmin = temp.groupby(temp.index.normalize()).min()
    per_day = tmin.reindex(days.unique())
    threshold = float(np.nanquantile(per_day.to_numpy(dtype=float), decile)) if per_day.notna().sum() else np.nan
    row_tmin = per_day.reindex(days).to_numpy(dtype=float)
    if not np.isfinite(threshold):
        return np.ones(len(days))
    excess = np.where(np.isfinite(row_tmin), np.maximum(0.0, threshold - row_tmin), 0.0)
    return 1.0 + alpha * excess / scale_f


def training_days(last: date, n_days: int) -> list[date]:
    """The ``n_days`` days ending at ``last`` (inclusive), oldest first."""
    return [last - timedelta(days=k) for k in range(n_days - 1, -1, -1)]


def target_temperature(info) -> pd.Series:
    """Observed temperature up to the cut-off followed by the HRRR path: the series the target day is built on."""
    observed = info.temp_history_f.asfreq("h") if len(info.temp_history_f) else info.temp_history_f
    path = pd.Series(info.temp_forecast_path_f, index=info.path_timestamps)
    return pd.concat([observed.loc[: path.index[0] - pd.Timedelta(hours=1)], path]).interpolate(limit=6, limit_area="inside")
