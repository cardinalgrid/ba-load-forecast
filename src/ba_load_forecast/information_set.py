"""Everything a forecaster had for one BA and one target day at the cut-off, and nothing else.

``Loader.information_set(ba, day)`` gathers, for the 24 local hours of ``day``:

* ``load_history``: the BA's hourly load (EIA-930 ``D``) up to the hour beginning 08:00 of the day before;
* ``temp_history_f``: the observed temperature at the BA's station for the same hours (training only);
* ``temp_forecast_f``: the HRRR 2 m temperature from the run available at the cut-off (what a model may use);
* ``temp_persistence_f``: the last observed temperature at the same hour (a floor for the weather input);
* ``temp_observed_f``: the temperature that actually occurred (a ceiling, never a model input);
* ``ba_forecast``: the BA's own day-ahead forecast (EIA-930 ``DF``), the comparison;
* ``actual``: the load that occurred (EIA-930 ``D``), for scoring only.

Load and forecast come from the tidy EIA-930 files of ba-forecast-scorecard, temperature from the
NOAA ISD-Lite cache and the HRRR extraction of this package; both are read through the helpers of
grid_sentinel so that every study of the initiative uses the same conventions (local hour beginning,
offsets in hours behind UTC).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types, special_days
from grid_sentinel.data import load_series_local, tidy_frame, utc_offset
from grid_sentinel.stations import BA_STATION
from grid_sentinel.weather import hourly_temperature_f

from .cutoff import DEFAULT_INIT_HOURS, PATH_HOURS, forecast_path, last_load_hour, path_timestamps, run_for_day
from .hrrr import load_station


@dataclass
class InformationSet:
    ba: str
    day: date
    timestamps: pd.DatetimeIndex
    offset_h: np.ndarray
    run: tuple[date, int] | None
    load_history: pd.Series
    temp_history_f: pd.Series
    temp_forecast_f: np.ndarray
    temp_forecast_path_f: np.ndarray
    path_timestamps: pd.DatetimeIndex
    temp_persistence_f: np.ndarray
    temp_observed_f: np.ndarray
    ba_forecast: np.ndarray
    actual: np.ndarray
    day_type: int
    special_day: int | None
    actual_plausible: bool = True

    @property
    def cutoff(self) -> datetime:
        return last_load_hour(self.day)


GROSS_LOW, GROSS_HIGH, GROSS_WINDOW_H = 0.2, 5.0, 24 * 28


def gross_guard(load: pd.Series) -> pd.Series:
    """The series with gross faults set to NaN: readings below ``GROSS_LOW`` or above ``GROSS_HIGH`` times
    the median of the previous four weeks (the hard gross-ratio rule of grid-data-sentinel).

    This is the control cleaning of the study: it removes only what no load could be (an overflow, a
    dropped digit), and leaves every other fault in the history.
    """
    if load.empty:
        return load
    ref = load.rolling(GROSS_WINDOW_H, min_periods=24 * 7).median().shift(1)
    ratio = load / ref
    bad = ratio.notna() & ((ratio < GROSS_LOW) | (ratio > GROSS_HIGH))
    return load.mask(bad)


def plausible(actual: np.ndarray, reference: float) -> bool:
    """False when any hour of the day that occurred is a gross fault against the recent median."""
    a = np.asarray(actual, dtype=float)
    if np.isnan(reference) or reference <= 0:
        return True
    ok = a[~np.isnan(a)]
    return bool(np.all((ok >= GROSS_LOW * reference) & (ok <= GROSS_HIGH * reference)))


class Loader:
    """Reads and caches the public data of every BA-year touched, then builds information sets."""

    def __init__(self, tidy_dir: Path, isd_dir: Path, hrrr_dir: Path, history_days: int = 730,
                 init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS, gross_guard: bool = True):
        self.tidy_dir = Path(tidy_dir)
        self.isd_dir = Path(isd_dir)
        self.hrrr_dir = Path(hrrr_dir)
        self.history_days = history_days
        self.init_hours = init_hours
        self.gross_guard = gross_guard
        self._series: dict[tuple, pd.Series] = {}
        self._hrrr: dict[str, pd.DataFrame] = {}

    # ---- cached readers -------------------------------------------------------------------------------
    def load(self, ba: str, year: int) -> pd.Series:
        return self._cached(("load", ba, year), lambda: load_series_local(self.tidy_dir, ba, year))

    def forecast(self, ba: str, year: int) -> pd.Series:
        def read():
            d = tidy_frame(self.tidy_dir, ba, year, ("local_end", "forecast"))
            if d.empty:
                return pd.Series(dtype=float)
            s = d.set_index("local_end")["forecast"].astype(float)
            s.index = pd.DatetimeIndex(s.index) - pd.Timedelta(hours=1)
            return s

        return self._cached(("forecast", ba, year), read)

    def offset(self, ba: str, year: int) -> pd.Series:
        return self._cached(("offset", ba, year), lambda: utc_offset(self.tidy_dir, ba, year))

    def temperature(self, ba: str, year: int) -> pd.Series:
        return self._cached(("temp", ba, year), lambda: hourly_temperature_f(ba, year, self.tidy_dir, self.isd_dir))

    def hrrr(self, icao: str) -> pd.DataFrame:
        if icao not in self._hrrr:
            self._hrrr[icao] = load_station(self.hrrr_dir, icao)
        return self._hrrr[icao]

    def _cached(self, key, read):
        if key not in self._series:
            self._series[key] = read()
        return self._series[key]

    def _years(self, ba: str, first: date, last: date, reader) -> pd.Series:
        parts = [reader(ba, y) for y in range(first.year, last.year + 1)]
        parts = [p for p in parts if not p.empty]
        if not parts:
            return pd.Series(dtype=float)
        s = pd.concat(parts)
        return s[~s.index.duplicated()].sort_index()

    # ---- the information set --------------------------------------------------------------------------
    def information_set(self, ba: str, day: date) -> InformationSet:
        start = day - timedelta(days=self.history_days)
        cutoff = last_load_hour(day)
        hours = pd.date_range(datetime(day.year, day.month, day.day), periods=24, freq="h")

        load = self._years(ba, start, day, self.load)
        fcst = self._years(ba, start, day, self.forecast)
        off = self._years(ba, start, day, self.offset)
        temp = self._years(ba, start, day, self.temperature)

        history_index = load.loc[pd.Timestamp(start):pd.Timestamp(cutoff)].index
        load_history = load.reindex(history_index)
        if self.gross_guard:
            load_history = gross_guard(load_history)
        temp_history = temp.reindex(history_index)
        reference = float(load_history.iloc[-GROSS_WINDOW_H:].median()) if len(load_history) else np.nan

        off_day = off.reindex(hours).to_numpy(dtype=float)
        fallback = float(off.median()) if len(off) else np.nan
        off_day = np.where(np.isnan(off_day), fallback, off_day)
        off_cutoff = off.get(pd.Timestamp(cutoff), fallback)

        run = None
        temp_fc = np.full(24, np.nan)
        path_ts = path_timestamps(day)
        temp_path = np.full(PATH_HOURS, np.nan)
        rows = self.hrrr(BA_STATION[ba])
        if not np.isnan(off_cutoff):
            run = run_for_day(day, float(off_cutoff), self.init_hours)
            if len(rows):
                off_path = off.reindex(path_ts).to_numpy(dtype=float)
                off_path = np.where(np.isnan(off_path), fallback, off_path)
                temp_path = forecast_path(rows, day, off_path, run)
                temp_fc = temp_path[-24:]

        persist = np.full(24, np.nan)
        for h in range(24):
            back = 1 if h <= cutoff.hour else 2
            persist[h] = temp.get(hours[h] - pd.Timedelta(days=back), np.nan)

        d64 = np.array([np.datetime64(day)])
        kinds = special_days(day.year)
        return InformationSet(
            ba=ba, day=day, timestamps=hours, offset_h=off_day, run=run,
            load_history=load_history, temp_history_f=temp_history,
            temp_forecast_f=temp_fc, temp_forecast_path_f=temp_path, path_timestamps=path_ts,
            temp_persistence_f=persist,
            temp_observed_f=temp.reindex(hours).to_numpy(dtype=float),
            ba_forecast=fcst.reindex(hours).to_numpy(dtype=float),
            actual=load.reindex(hours).to_numpy(dtype=float),
            day_type=int(day_types(d64)[0]), special_day=kinds.get(day),
            actual_plausible=plausible(load.reindex(hours).to_numpy(dtype=float), reference),
        )
