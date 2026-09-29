"""The information cut-off: what a day-ahead forecaster had at 9 a.m. local time the day before.

For a target day ``D`` of a balancing authority:

* load is known through the hour beginning 08:00 local of ``D-1`` (the last complete hour before 9 a.m.);
* the weather forecast is the latest HRRR run whose initialisation time plus an availability lag
  (2 h, the time the model takes to finish its 48 h) is not after 09:00 local of ``D-1``. Only the runs
  that reach 48 h (00, 06, 12 and 18 UTC) qualify, and by default only 12 and 06 UTC are extracted:
  12 UTC is the latest that qualifies everywhere in standard time and in the Central, Mountain and
  Pacific zones in daylight time; 06 UTC is the one that qualifies in the Eastern zone in daylight time
  (12 UTC + 2 h = 14 UTC is after 09:00 EDT = 13 UTC).

Offsets follow the EIA-930 convention: hours behind UTC, positive in the United States (5 for Eastern
standard time, 4 for Eastern daylight time).
"""

from __future__ import annotations

from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd

CUTOFF_LOCAL_HOUR = 9
AVAILABILITY_LAG_H = 2
DEFAULT_INIT_HOURS = (12, 6)
HOURS = np.arange(24)


def cutoff_utc(day: date, offset_h: float, cutoff_hour: int = CUTOFF_LOCAL_HOUR) -> datetime:
    """The cut-off instant for target day ``day``: ``cutoff_hour`` local of the day before, in UTC."""
    local = datetime(day.year, day.month, day.day, cutoff_hour) - timedelta(days=1)
    return local + timedelta(hours=float(offset_h))


def last_load_hour(day: date) -> datetime:
    """The last local hour (hour beginning) of load a forecaster may use for target day ``day``: 08:00 of D-1."""
    return datetime(day.year, day.month, day.day, CUTOFF_LOCAL_HOUR - 1) - timedelta(days=1)


def run_for_day(day: date, offset_h: float, init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS,
                lag_h: float = AVAILABILITY_LAG_H, cutoff_hour: int = CUTOFF_LOCAL_HOUR) -> tuple[date, int]:
    """The latest HRRR run (initialisation date and UTC hour) available at the cut-off for target day ``day``."""
    limit = cutoff_utc(day, offset_h, cutoff_hour)
    candidates = []
    for back in (1, 2):
        d = day - timedelta(days=back)
        for h in init_hours:
            init = datetime(d.year, d.month, d.day, h)
            if init + timedelta(hours=lag_h) <= limit:
                candidates.append((init, d, h))
    if not candidates:
        raise ValueError(f"no run in {init_hours} is available at {limit} for {day}")
    _, d, h = max(candidates)
    return d, h


def previous_run(init: tuple[date, int], init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS,
                 max_gap_h: int = 6) -> tuple[date, int] | None:
    """The extracted run initialised at most ``max_gap_h`` hours before ``init`` (None when there is none:
    with the 12 and 06 UTC extraction, the 06 UTC run has no predecessor)."""
    d, h = init
    this = datetime(d.year, d.month, d.day, h)
    best = None
    for back in (0, 1):
        dd = d - timedelta(days=back)
        for hh in init_hours:
            cand = datetime(dd.year, dd.month, dd.day, hh)
            if cand < this and (this - cand) <= timedelta(hours=max_gap_h) and (best is None or cand > best[0]):
                best = (cand, dd, hh)
    return None if best is None else (best[1], best[2])


def blend_paths(first: np.ndarray, second: np.ndarray | None, weight: float = 0.5) -> np.ndarray:
    """The weighted mean of two forecast paths where both are known (``weight`` on the second), the first alone
    elsewhere (a lagged ensemble of two runs, or two weather models; the second may not reach every hour)."""
    if second is None:
        return first
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    both = np.isfinite(a) & np.isfinite(b)
    out = a.copy()
    out[both] = (1.0 - weight) * a[both] + weight * b[both]
    return out


def weighted_paths(paths: list[np.ndarray], weights: list[float]) -> np.ndarray:
    """Hour by hour, the weighted mean of the paths that have the hour, the weights renormalised over those
    (NaN where none has it); equal weights give ``mean_paths``."""
    stack = np.vstack([np.asarray(p, dtype=float) for p in paths])
    w = np.asarray(weights, dtype=float)[:, None] * np.isfinite(stack)
    total = np.nansum(stack * w, axis=0)
    norm = w.sum(axis=0)
    return np.where(norm > 0, total / np.where(norm > 0, norm, 1.0), np.nan)


def mean_paths(paths: list[np.ndarray]) -> np.ndarray:
    """Hour by hour, the mean of the paths that have the hour (NaN where none has it): several weather models
    with equal weight, each covering what it covers."""
    stack = np.vstack([np.asarray(p, dtype=float) for p in paths])
    n = np.isfinite(stack).sum(axis=0)
    total = np.nansum(stack, axis=0)
    return np.where(n > 0, total / np.maximum(n, 1), np.nan)


def valid_utc_for_day(day: date, offset_h) -> np.ndarray:
    """UTC instants (hour beginning) of the 24 local hours of ``day``; ``offset_h`` is a scalar or one per hour."""
    off = np.broadcast_to(np.asarray(offset_h, dtype=float), (24,))
    base = np.datetime64(datetime(day.year, day.month, day.day), "ns")
    return base + ((HOURS + off) * 3600.0 * 1e9).astype("timedelta64[ns]")


def lead_hours(day: date, offset_h, init: tuple[date, int]) -> np.ndarray:
    """Forecast lead, in hours, of each of the 24 local hours of ``day`` in the run ``init``."""
    d, h = init
    init_utc = np.datetime64(datetime(d.year, d.month, d.day, h), "ns")
    return ((valid_utc_for_day(day, offset_h) - init_utc) / np.timedelta64(1, "h")).astype(int)


PATH_HOURS = 24 - CUTOFF_LOCAL_HOUR + 24   # from 09:00 of D-1 to 23:00 of D: 39 hours


def path_timestamps(day: date) -> pd.DatetimeIndex:
    """Local hours (hour beginning) from the cut-off hour of D-1 to 23:00 of ``day``."""
    start = datetime(day.year, day.month, day.day, CUTOFF_LOCAL_HOUR) - timedelta(days=1)
    return pd.date_range(start, periods=PATH_HOURS, freq="h")


def forecast_path(rows: pd.DataFrame, day: date, offset_h, init: tuple[date, int], column: str = "temp_f") -> np.ndarray:
    """Temperature in Fahrenheit from the run ``init`` for every local hour from 09:00 of D-1 to 23:00 of D.

    The hours before the target day are what the same run said about the rest of D-1, which a forecaster
    running at 9 a.m. also had; ``offset_h`` is a scalar or one value per hour of the path. Hours the run
    does not cover are NaN.
    """
    off = np.broadcast_to(np.asarray(offset_h, dtype=float), (PATH_HOURS,))
    local = path_timestamps(day)
    valid = pd.DatetimeIndex(local.to_numpy() + (off * 3600.0 * 1e9).astype("timedelta64[ns]"))
    d, h = init
    init_ts = pd.Timestamp(datetime(d.year, d.month, d.day, h))
    run = rows[rows["init_utc"] == init_ts]
    s = pd.Series(run[column].to_numpy(dtype=float), index=pd.DatetimeIndex(run["valid_utc"]))
    s = s[~s.index.duplicated()]
    return s.reindex(valid).to_numpy(dtype=float)


def forecast_temperature(rows: pd.DataFrame, day: date, offset_h, init: tuple[date, int] | None = None,
                         init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS) -> np.ndarray:
    """Temperature in Fahrenheit forecast for the 24 local hours of ``day`` from the run available at the cut-off.

    ``rows`` are the extracted rows of one station (``init_utc, lead_h, valid_utc, temp_f``). Hours the run
    does not cover, or that the archive lacks, are NaN. ``offset_h`` is a scalar or one value per hour;
    the scalar (or the first value) is the offset at the cut-off.
    """
    off = np.broadcast_to(np.asarray(offset_h, dtype=float), (24,))
    if init is None:
        init = run_for_day(day, float(off[0]), init_hours)
    d, h = init
    init_ts = pd.Timestamp(datetime(d.year, d.month, d.day, h))
    run = rows[rows["init_utc"] == init_ts]
    valid = pd.DatetimeIndex(valid_utc_for_day(day, off))
    s = pd.Series(run["temp_f"].to_numpy(dtype=float), index=pd.DatetimeIndex(run["valid_utc"]))
    s = s[~s.index.duplicated()]
    return s.reindex(valid).to_numpy(dtype=float)
