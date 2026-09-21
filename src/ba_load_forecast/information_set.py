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

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types, special_days
from grid_sentinel.data import load_series_local, tidy_frame, utc_offset
from grid_sentinel.stations import BA_STATION
from grid_sentinel.weather import fetch_isd_lite, hourly_temperature_f, read_isd_lite

from .cleaning import sentinel_clean
from .cutoff import DEFAULT_INIT_HOURS, PATH_HOURS, forecast_path, last_load_hour, path_timestamps, run_for_day
from .hrrr import load_station
from .sky import all_days, forecast_as_seen, pv_capacity, run_table, sky_frame
from .stations_multi import BA_STATIONS_MULTI, station_table_for


def station_temperature_f(usaf: str, wban: str, ba: str, year: int, tidy_dir: Path, isd_dir: Path) -> pd.Series:
    """Temperature in Fahrenheit at one ISD station, indexed like the BA's load (local hour beginning)."""
    p = fetch_isd_lite(usaf, wban, year, isd_dir)
    s = load_series_local(tidy_dir, ba, year)
    if p is None or s.empty:
        return pd.Series(dtype=float)
    obs = read_isd_lite(p).drop_duplicates("utc").set_index("utc")["temp_c"].sort_index()
    off = utc_offset(tidy_dir, ba, year).reindex(s.index)
    off = off.fillna(off.median())
    utc = pd.DatetimeIndex(s.index + pd.to_timedelta(off.to_numpy(), unit="h")).tz_localize("UTC")
    return pd.Series(obs.reindex(utc).to_numpy(dtype=float) * 9.0 / 5.0 + 32.0, index=s.index)


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
    stations: list[str] = field(default_factory=list)
    temp_history_stations_f: pd.DataFrame | None = None       # one column per station, aligned with load_history
    temp_forecast_path_stations_f: pd.DataFrame | None = None  # one column per station, indexed by path_timestamps
    sky: pd.DataFrame | None = None                            # sky.SKY_COLUMNS for the history and the target day

    @property
    def cutoff(self) -> datetime:
        return last_load_hour(self.day)


GROSS_LOW, GROSS_HIGH, GROSS_WINDOW_H = 0.2, 5.0, 24 * 28
FIRST_DAY = date(2015, 7, 1)


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
                 init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS, gross_guard: bool = True,
                 stations: str = "single", hrrr_dirs: list[Path] | None = None, cleaning: str = "gross",
                 sky: bool = False, cloud_dir: Path | None = None, pv: bool = False, irradiance: bool = False,
                 dswrf_dir: Path | None = None):
        """``stations="multi"`` uses every station of ``BA_STATIONS_MULTI`` for the BA: the temperature fields
        become the equal-weight mean across stations and the per-station series are attached; HRRR rows are
        looked up in ``hrrr_dirs`` (default: ``hrrr_dir`` and its sibling ``hrrr_multi``). ``cleaning="sentinel"``
        repairs the load history with grid-data-sentinel (``cleaning.sentinel_clean``, one year at a time, warmed
        up on the year before) before the gross-fault guard; the outcome is never cleaned."""
        self.cleaning = cleaning
        self.tidy_dir = Path(tidy_dir)
        self.isd_dir = Path(isd_dir)
        self.hrrr_dir = Path(hrrr_dir)
        # by default every sibling folder whose name starts like the main one (hrrr, hrrr_multi, hrrr_fpl, ...)
        self.hrrr_dirs = ([Path(d) for d in hrrr_dirs] if hrrr_dirs
                          else [self.hrrr_dir, *sorted(p for p in self.hrrr_dir.parent.glob(f"{self.hrrr_dir.name}_*") if p.is_dir())])
        self.history_days = history_days
        self.init_hours = init_hours
        self.gross_guard = gross_guard
        self.stations = stations
        self._series: dict[tuple, pd.Series] = {}
        self._hrrr: dict[str, pd.DataFrame] = {}
        self._station_table: pd.DataFrame | None = None
        # sky=True attaches the sun's elevation and the HRRR cloud cover as seen at each day's cut-off
        self.sky = sky
        self.pv = pv                          # with sky=True: scale the sun by the installed PV capacity (sky.PV_COLUMNS)
        self._pv: dict[str, pd.Series] | None = None
        self.cloud_dir = Path(cloud_dir) if cloud_dir else self.hrrr_dir.parent / "cloud"
        self._cloud: dict[str, pd.Series | None] = {}
        # irradiance=True attaches the forecast surface short-wave flux as seen at the cut-off (hrrr_grib extraction)
        self.irradiance = irradiance
        self.dswrf_dir = Path(dswrf_dir) if dswrf_dir else self.hrrr_dir.parent / "dswrf"
        self._dswrf: dict[str, pd.Series | None] = {}
        self._latlon: dict[str, tuple[float, float]] = {}

    def latlon(self, ba: str) -> tuple[float, float]:
        if ba not in self._latlon:
            t = station_table_for([BA_STATION[ba]], self.isd_dir).iloc[0]
            self._latlon[ba] = (float(t["lat"]), float(t["lon"]))
        return self._latlon[ba]

    def cloud_series(self, ba: str) -> pd.Series | None:
        """Cloud cover (percent) forecast for every local hour by the run available at that day's cut-off,
        mean over the BA's stations; None when no station has a cloud extraction."""
        return self.as_seen_series(ba, self._cloud, self.cloud_dir, "cloud_pct")

    def dswrf_series(self, ba: str) -> pd.Series | None:
        """Forecast surface short-wave flux (W/m2) as seen at the cut-off, mean over the BA's stations."""
        return self.as_seen_series(ba, self._dswrf, self.dswrf_dir, "dswrf_wm2")

    def as_seen_series(self, ba: str, cache: dict, folder: Path, field: str) -> pd.Series | None:
        if ba not in cache:
            tables = [run_table(load_station(folder, icao), field) for icao in self.stations_of(ba)]
            tables = [t for t in tables if t[0]]
            if not tables:
                cache[ba] = None
            else:
                inits = sorted(i for t in tables for i in t[0])
                first, last = inits[0].date(), (inits[-1] + pd.Timedelta(days=2)).date()

                def offset_of_day(d):
                    off = self.offset(ba, d.year)
                    if off.empty:
                        return np.nan
                    v = off.get(pd.Timestamp(d) + pd.Timedelta(hours=12), np.nan)
                    return float(off.median()) if np.isnan(v) else float(v)

                cache[ba] = forecast_as_seen(tables, all_days(first, last), offset_of_day, self.init_hours)
        return cache[ba]

    def stations_of(self, ba: str) -> list[str]:
        if self.stations == "multi" and ba in BA_STATIONS_MULTI:
            return list(BA_STATIONS_MULTI[ba])
        return [BA_STATION[ba]]

    def station_temperature(self, icao: str, ba: str, year: int) -> pd.Series:
        def read():
            if self._station_table is None:
                self._station_table = station_table_for(sorted({i for v in BA_STATIONS_MULTI.values() for i in v}),
                                                        self.isd_dir).set_index("icao")
            st = self._station_table.loc[icao]
            return station_temperature_f(st["usaf"], st["wban"], ba, year, self.tidy_dir, self.isd_dir)

        return self._cached(("stemp", icao, ba, year), read)

    # ---- cached readers -------------------------------------------------------------------------------
    def raw_load(self, ba: str, year: int) -> pd.Series:
        return self._cached(("raw", ba, year), lambda: load_series_local(self.tidy_dir, ba, year))

    def load(self, ba: str, year: int) -> pd.Series:
        """The load series used as history: raw, or repaired by the Sentinel when ``cleaning="sentinel"``."""
        if self.cleaning != "sentinel":
            return self.raw_load(ba, year)

        def clean():
            raw = self.raw_load(ba, year)
            if raw.empty:
                return raw
            prev = self.raw_load(ba, year - 1)
            temp = self.temperature(ba, year)
            temp_prev = self.temperature(ba, year - 1) if not prev.empty else None
            cleaned, _ = sentinel_clean(raw, temp if not temp.empty else None, warm=prev if not prev.empty else None,
                                        warm_temp=temp_prev if temp_prev is not None and not temp_prev.empty else None)
            return cleaned

        return self._cached(("load", ba, year), clean)

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
            rows = load_station(self.hrrr_dir, icao)
            for d in self.hrrr_dirs:
                if len(rows):
                    break
                rows = load_station(d, icao)
            self._hrrr[icao] = rows
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
        start = max(day - timedelta(days=self.history_days), FIRST_DAY)   # EIA-930 starts in July 2015
        cutoff = last_load_hour(day)
        hours = pd.date_range(datetime(day.year, day.month, day.day), periods=24, freq="h")

        load = self._years(ba, start, day, self.load)
        outcome = load if self.cleaning != "sentinel" else self._years(ba, start, day, self.raw_load)
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
        path_ts = path_timestamps(day)
        stations = self.stations_of(ba)
        off_path = off.reindex(path_ts).to_numpy(dtype=float)
        off_path = np.where(np.isnan(off_path), fallback, off_path)
        if not np.isnan(off_cutoff):
            run = run_for_day(day, float(off_cutoff), self.init_hours)
        paths = {}
        for icao in stations:
            rows = self.hrrr(icao)
            paths[icao] = forecast_path(rows, day, off_path, run) if run is not None and len(rows) else np.full(PATH_HOURS, np.nan)
        path_frame = pd.DataFrame(paths, index=path_ts)
        temp_path = path_frame.mean(axis=1, skipna=False).to_numpy() if len(stations) > 1 else path_frame.iloc[:, 0].to_numpy()
        temp_fc = temp_path[-24:]
        stations_hist = None
        if len(stations) > 1:
            cols = {icao: self._years(ba, start, day, lambda b, y, i=icao: self.station_temperature(i, b, y)).reindex(history_index)
                    for icao in stations}
            stations_hist = pd.DataFrame(cols, index=history_index)
            temp_history = stations_hist.mean(axis=1)
            temp = pd.concat([self._years(ba, start, day, lambda b, y, i=icao: self.station_temperature(i, b, y)) for icao in stations],
                             axis=1).mean(axis=1)

        sky = None
        if self.sky:
            lat, lon = self.latlon(ba)
            pv = None
            if self.pv:
                if self._pv is None:
                    self._pv = pv_capacity()
                pv = self._pv.get(ba)
            sky = sky_frame(history_index.union(hours), off, lat, lon, self.cloud_series(ba), pv=pv,
                            dswrf=self.dswrf_series(ba) if self.irradiance else None)

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
            actual=outcome.reindex(hours).to_numpy(dtype=float),
            day_type=int(day_types(d64)[0]), special_day=kinds.get(day),
            actual_plausible=plausible(outcome.reindex(hours).to_numpy(dtype=float), reference),
            sky=sky, stations=stations, temp_history_stations_f=stations_hist,
            temp_forecast_path_stations_f=path_frame if len(stations) > 1 else None,
        )
