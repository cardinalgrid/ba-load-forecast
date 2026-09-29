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
from grid_sentinel.consistency import day_is_plausible, forecast_is_plausible, neighbour_spikes
from grid_sentinel.data import load_series_local, tidy_frame, utc_offset
from grid_sentinel.stations import BA_STATION
from grid_sentinel.weather import fetch_isd_lite, hourly_temperature_f, read_isd_lite

from .asos import read_asos, supplement_path
from .cleaning import sentinel_clean
from .cutoff import (
    DEFAULT_INIT_HOURS,
    PATH_HOURS,
    blend_paths,
    forecast_path,
    last_load_hour,
    mean_paths,
    path_timestamps,
    previous_run,
    run_for_day,
)
from .hrrr import load_station
from .nbm import daily_at_cutoff, load_daily, nbm_path
from .sky import all_days, forecast_as_seen, pv_capacity, run_table, sky_frame
from .stations_multi import BA_STATIONS_MULTI, station_table_for
from .weather_extra import read_isd_lite_field


def station_temperature_f(usaf: str, wban: str, ba: str, year: int, tidy_dir: Path, isd_dir: Path,
                          supplement_file: Path | list[Path] | None = None) -> pd.Series:
    """Temperature in Fahrenheit at one ISD station, indexed like the BA's load (local hour beginning).

    With ``supplement_file`` (``scripts/fetch_ghcnh.py`` or ``scripts/fetch_asos.py`` output for the station, one file
    or a list applied in order), the hours the ISD file does not cover are filled from it: the ISD archive stops on
    27 August 2025 (``asos.FIRST_MISSING_ISD``). A later file only fills what the earlier ones left missing."""
    s = load_series_local(tidy_dir, ba, year)
    if s.empty:                                   # no load for the year: no observation is fetched either
        return pd.Series(dtype=float)
    p = fetch_isd_lite(usaf, wban, year, isd_dir)
    files = [] if supplement_file is None else ([supplement_file] if isinstance(supplement_file, Path) else list(supplement_file))
    if p is None and not files:
        return pd.Series(dtype=float)
    off = utc_offset(tidy_dir, ba, year).reindex(s.index)
    off = off.fillna(off.median())
    utc = pd.DatetimeIndex(s.index + pd.to_timedelta(off.to_numpy(), unit="h")).tz_localize("UTC")
    out = np.full(len(s), np.nan)
    if p is not None:
        obs = read_isd_lite(p).drop_duplicates("utc").set_index("utc")["temp_c"].sort_index()
        out = obs.reindex(utc).to_numpy(dtype=float) * 9.0 / 5.0 + 32.0
    for f in files:
        sup = read_asos(f).reindex(utc).to_numpy(dtype=float)
        gap = np.isnan(out)
        out[gap] = sup[gap]
    return pd.Series(out, index=s.index)


def station_field(usaf: str, wban: str, ba: str, year: int, tidy_dir: Path, isd_dir: Path, field: str,
                  supplement_file: Path | list[Path] | None = None) -> pd.Series:
    """One observed field (``weather_extra.ISD_LITE_FIELDS``: ``temp_f``, ``dewpoint_f``, ``wind_ms``) at one ISD
    station, indexed like the BA's load; the hours the ISD file lacks are filled from the supplements in order,
    exactly as ``station_temperature_f`` does for the temperature."""
    s = load_series_local(tidy_dir, ba, year)
    if s.empty:
        return pd.Series(dtype=float)
    p = fetch_isd_lite(usaf, wban, year, isd_dir)
    files = [] if supplement_file is None else ([supplement_file] if isinstance(supplement_file, Path) else list(supplement_file))
    if p is None and not files:
        return pd.Series(dtype=float)
    off = utc_offset(tidy_dir, ba, year).reindex(s.index)
    off = off.fillna(off.median())
    utc = pd.DatetimeIndex(s.index + pd.to_timedelta(off.to_numpy(), unit="h")).tz_localize("UTC")
    out = np.full(len(s), np.nan)
    if p is not None:
        obs = read_isd_lite_field(p, field)
        out = obs[~obs.index.duplicated()].reindex(utc).to_numpy(dtype=float)
    for f in files:
        sup = read_asos(f, field).reindex(utc).to_numpy(dtype=float)
        gap = np.isnan(out)
        out[gap] = sup[gap]
    return pd.Series(out, index=s.index)


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
    benchmark_plausible: bool = True                            # the published forecast is free of reporting faults
    stations: list[str] = field(default_factory=list)
    temp_history_stations_f: pd.DataFrame | None = None       # one column per station, aligned with load_history
    temp_forecast_path_stations_f: pd.DataFrame | None = None  # one column per station, indexed by path_timestamps
    sky: pd.DataFrame | None = None                            # sky.SKY_COLUMNS for the history and the target day
    weather: pd.DataFrame | None = None                        # dewpoint_f, wind_ms: observed over the history, the HRRR path after
    run_second: tuple[date, int] | None = None                 # with Loader(second_run=True): the older run blended into the paths
    nbm_daily: dict[str, float] | None = None                  # with Loader(nbm_daily_dir): the NBM daily products of the day, BA mean

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


JUMP = 0.4              # an hour more than this far from the mean of its two neighbours is a reporting fault, not load
FORECAST_FAULT = 0.5    # a published forecast more than this far from the outcome at any hour is a reporting fault
LABEL_OFFSETS = Path(__file__).resolve().parents[2] / "docs" / "hour_label_offsets.csv"


def jumps(actual: np.ndarray, limit: float = JUMP) -> np.ndarray:
    """The Sentinel's spike mask (``grid_sentinel.consistency.neighbour_spikes``): an hour far both from its
    neighbours and from the day's level. Kept under this name for the callers of the first protocol."""
    return neighbour_spikes(actual, limit)


def plausible(actual: np.ndarray, reference: float, jump: float | None = JUMP) -> bool:
    """False when any hour of the day that occurred is a gross fault against the recent median, or (with
    ``jump``) a spike against its neighbours and the day's level."""
    a = np.asarray(actual, dtype=float)
    if jump is not None and not day_is_plausible(a, jump):
        return False
    if np.isnan(reference) or reference <= 0:
        return True
    ok = a[~np.isnan(a)]
    return bool(np.all((ok >= GROSS_LOW * reference) & (ok <= GROSS_HIGH * reference)))


def forecast_plausible(forecast: np.ndarray, actual: np.ndarray, limit: float = FORECAST_FAULT) -> bool:
    """The Sentinel's verdict on a published forecast (``grid_sentinel.consistency.forecast_is_plausible``):
    False when it is missing, non-positive or more than ``limit`` (relative) away from the outcome at any
    hour where both exist. A reporting fault of the benchmark, on which no model is scored."""
    f = np.asarray(forecast, dtype=float)
    if f.shape != (24,):
        return False
    return forecast_is_plausible(f, np.asarray(actual, dtype=float), limit, n_hours=24)


def hourly_bias_table(observed: pd.Series, seen: pd.Series) -> pd.DataFrame:
    """Days in rows, local hours in columns: observed minus forecast-as-seen-at-the-cut-off, in degrees."""
    e = (observed.asfreq("h") - seen.reindex(observed.asfreq("h").index)).dropna()
    if e.empty:
        return pd.DataFrame(columns=range(24))
    return pd.DataFrame({"day": e.index.normalize(), "hour": e.index.hour, "e": e.to_numpy()}).pivot(
        index="day", columns="hour", values="e").reindex(columns=range(24))


def rolling_hour_bias(table: pd.DataFrame, day: date, window_days: int, min_days: int = 10) -> np.ndarray:
    """The median error of the forecast per local hour over the ``window_days`` days ending two days before
    ``day`` (the last day fully known at the cut-off); zero where fewer than ``min_days`` errors exist."""
    if table.empty:
        return np.zeros(24)
    last = pd.Timestamp(day) - pd.Timedelta(days=2)
    rows = table.loc[last - pd.Timedelta(days=window_days - 1): last]
    med = rows.median(axis=0, skipna=True).where(rows.count(axis=0) >= min_days, 0.0)
    return med.reindex(range(24)).fillna(0.0).to_numpy(dtype=float)


NBM_FIELD_COLUMNS = {"dewpoint_f": ("nbm_dewpoint_f", 1.0), "wind_ms": ("nbm_wind_mph", 0.44704)}   # field -> (NBM column, unit factor)


def cold_bias_from_table(table: pd.DataFrame, day: date, window_days: int, threshold_f: float, min_hours: int = 48) -> float:
    """Median of observed minus forecast on the hours forecast below ``threshold_f`` within the ``window_days`` days
    ending two days before ``day``; zero with fewer than ``min_hours`` such hours."""
    if table.empty:
        return 0.0
    last = pd.Timestamp(day) - pd.Timedelta(days=2) + pd.Timedelta(hours=23)
    rows = table.loc[last - pd.Timedelta(days=window_days): last]
    cold = rows[rows["seen"] < threshold_f]
    if len(cold) < min_hours:
        return 0.0
    return float(cold["e"].median())


def apply_cold_bias(path: np.ndarray, bias: float, threshold_f: float) -> np.ndarray:
    """Add ``bias`` (observed minus forecast) to the hours of a path forecast below the threshold."""
    p = np.asarray(path, dtype=float).copy()
    cold = np.isfinite(p) & (p < threshold_f)
    p[cold] += bias
    return p


def apply_hour_bias(path: np.ndarray, path_ts: pd.DatetimeIndex, bias: np.ndarray) -> np.ndarray:
    """Add the local-hour bias to a temperature path (observed minus forecast: the forecast is moved toward
    what has been observed at that hour lately)."""
    hours = pd.DatetimeIndex(path_ts).hour.to_numpy()
    return np.asarray(path, dtype=float) + np.asarray(bias, dtype=float)[hours]


def label_offsets(path: Path | None = None) -> pd.DataFrame:
    """The documented hour-label offsets of the published series (``docs/hour_label_offsets.csv``)."""
    p = Path(path) if path else LABEL_OFFSETS
    if not p.exists():
        return pd.DataFrame(columns=["ba", "column", "start", "end", "shift_hours"])
    t = pd.read_csv(p)
    t["start"] = pd.to_datetime(t["start"])
    t["end"] = pd.to_datetime(t["end"])
    return t


def apply_label_offsets(s: pd.Series, ba: str, column: str, offsets: pd.DataFrame) -> pd.Series:
    """Move the timestamps of ``s`` (local hour beginning) by the documented offset of ``ba``/``column`` inside
    each offset period, so that every value carries the hour it belongs to. Values that land on an hour
    already occupied keep the moved one; the hour left empty at a switch stays missing."""
    if s.empty or offsets.empty:
        return s
    rows = offsets[(offsets["ba"] == ba) & (offsets["column"] == column)]
    if rows.empty:
        return s
    idx = pd.DatetimeIndex(s.index)
    new_index = idx.to_numpy().copy()
    moved = np.zeros(len(idx), dtype=bool)
    for r in rows.itertuples(index=False):
        mask = idx >= r.start
        if pd.notna(r.end):
            mask &= idx <= r.end
        new_index[mask] = (idx[mask] + pd.Timedelta(hours=int(r.shift_hours))).to_numpy()
        moved |= mask
    out = pd.Series(s.to_numpy(), index=pd.DatetimeIndex(new_index), name=s.name)
    keep = pd.Series(moved, index=out.index)
    out = out[~out.index.duplicated(keep="last") | keep.to_numpy()]
    out = out[~out.index.duplicated(keep="last")]
    return out.sort_index()


class Loader:
    """Reads and caches the public data of every BA-year touched, then builds information sets."""

    def __init__(self, tidy_dir: Path, isd_dir: Path, hrrr_dir: Path, history_days: int = 730,
                 init_hours: tuple[int, ...] = DEFAULT_INIT_HOURS, gross_guard: bool = True,
                 stations: str = "single", hrrr_dirs: list[Path] | None = None, cleaning: str = "gross",
                 sky: bool = False, cloud_dir: Path | None = None, pv: bool = False, irradiance: bool = False,
                 dswrf_dir: Path | None = None, align_labels: bool = True, temp_bias_days: int = 0,
                 supplement_dir: Path | list[Path] | None = None, fields: tuple[str, ...] = (),
                 field_dirs: dict[str, Path] | None = None, field_bias_days: int = 0, second_run: bool = False,
                 nbm_dir: Path | None = None, nbm_mode: str | None = None, nbm_daily_dir: Path | None = None,
                 nbm_weight: float = 0.5, nbm_cold_bias_days: int = 0, nbm_cold_threshold_f: float = 25.0,
                 nbm_field_dirs: dict[str, Path] | None = None, nbm_dswrf_dir: Path | None = None,
                 gfs_dir: Path | None = None, gfs_lag_h: float = 5.0):
        """``stations="multi"`` uses every station of ``BA_STATIONS_MULTI`` for the BA: the temperature fields
        become the equal-weight mean across stations and the per-station series are attached; HRRR rows are
        looked up in ``hrrr_dirs`` (default: ``hrrr_dir`` and its sibling ``hrrr_multi``). ``cleaning="sentinel"``
        repairs the load history with grid-data-sentinel (``cleaning.sentinel_clean``, one year at a time, warmed
        up on the year before) before the gross-fault guard; the outcome is never cleaned."""
        self.cleaning = cleaning
        # second_run=True: every forecast path (temperature and extra fields) is the mean of the cut-off run and the
        # extracted run up to 6 h older where that run covers the hour (a lagged ensemble of two runs)
        self.second_run = second_run
        # nbm_dir + nbm_mode: the NBM hourly temperature at the stations (nbm.extract) enters the temperature path,
        # "replace" (NBM where it has the hour, HRRR elsewhere) or "blend" (the mean of the two where both have it)
        self.nbm_dir = Path(nbm_dir) if nbm_dir else None
        self.nbm_mode = nbm_mode
        # nbm_weight: the weight of the NBM in the blend (0.5 = plain mean); nbm_cold_bias_days > 0: the NBM path is moved,
        # on hours forecast below nbm_cold_threshold_f, by the median of its own error on such hours over that many known
        # days (the NBM is too warm in the cold: docs/nbm_verification.md)
        self.nbm_weight = float(nbm_weight)
        self.nbm_cold_bias_days = int(nbm_cold_bias_days)
        self.nbm_cold_threshold_f = float(nbm_cold_threshold_f)
        self._nbm_cold_tables: dict[tuple[str, str], pd.DataFrame] = {}
        # nbm_field_dirs: field -> folder of the NBM extraction of that field (dewpoint_f -> nbm_dewpoint, wind_ms -> nbm_wind);
        # the NBM path of the field is blended with the HRRR path with nbm_weight, like the temperature
        self.nbm_field_dirs = {k: Path(v) for k, v in (nbm_field_dirs or {}).items()}
        self._nbm_fields: dict[tuple[str, str], pd.DataFrame] = {}
        # nbm_dswrf_dir: the NBM surface short-wave flux replaces the HRRR one as the irradiance seen at the cut-off
        self.nbm_dswrf_dir = Path(nbm_dswrf_dir) if nbm_dswrf_dir else None
        self._nbm_dswrf: dict[str, pd.Series | None] = {}
        # gfs_dir: the GFS 0.25 degree 2 m temperature at the stations (gfs.extract); its path from the run available at the
        # cut-off with gfs_lag_h of availability lag joins the temperature mean with equal weight (three-hourly gaps interpolated)
        self.gfs_dir = Path(gfs_dir) if gfs_dir else None
        self.gfs_lag_h = float(gfs_lag_h)
        self._gfs: dict[str, pd.DataFrame] = {}
        # nbm_daily_dir: the NBM daily products (nbm.extract_daily) of the target day, averaged over the BA's stations
        self.nbm_daily_dir = Path(nbm_daily_dir) if nbm_daily_dir else None
        self._nbm: dict[str, pd.DataFrame] = {}
        self._nbm_daily: dict[str, pd.DataFrame] = {}
        # fields beyond the temperature ("dewpoint_f", "wind_ms"): observed like the temperature, forecast from the
        # HRRR extraction in field_dirs (default: siblings of hrrr_dir named after the field)
        self.fields = tuple(fields)
        self.field_dirs = {k: Path(v) for k, v in (field_dirs or {}).items()}
        # field_bias_days > 0: the HRRR path of every extra field is corrected by the median of its own error per
        # local hour over that many known days, exactly as temp_bias_days does for the temperature
        self.field_bias_days = field_bias_days
        # temp_bias_days > 0: the HRRR temperature path of the target day is corrected by the median of the forecast's
        # own error per local hour over that many known days (forecast as seen at the cut-off against the observation)
        self.temp_bias_days = temp_bias_days
        dirs = [] if supplement_dir is None else ([supplement_dir] if isinstance(supplement_dir, (str, Path)) else list(supplement_dir))
        self.supplement_dirs = [Path(d) for d in dirs]
        self._bias_tables: dict[tuple[str, str], pd.DataFrame] = {}
        # align_labels applies the documented hour-label offsets of the published series (docs/hour_label_offsets.csv)
        self.offsets = label_offsets() if align_labels else pd.DataFrame(columns=["ba", "column", "start", "end", "shift_hours"])
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
        """Forecast surface short-wave flux (W/m2) as seen at the cut-off, mean over the BA's stations; from the NBM
        extraction when ``nbm_dswrf_dir`` is set (its three-hourly tail interpolated over gaps of up to 2 h)."""
        if self.nbm_dswrf_dir is not None:
            s = self.as_seen_series(ba, self._nbm_dswrf, self.nbm_dswrf_dir, "nbm_dswrf_wm2")
            return None if s is None else s.interpolate(limit=2, limit_area="inside")
        return self.as_seen_series(ba, self._dswrf, self.dswrf_dir, "dswrf_wm2")

    def nbm_field_rows(self, field: str, icao: str) -> pd.DataFrame:
        key = (field, icao)
        if key not in self._nbm_fields:
            folder = self.nbm_field_dirs.get(field)
            self._nbm_fields[key] = load_station(folder, icao) if folder else pd.DataFrame()
        return self._nbm_fields[key]

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

    def temp_seen_series(self, ba: str, icao: str) -> pd.Series | None:
        """The 2 m temperature forecast for every local hour by the run available at that day's cut-off, one station."""
        cache: dict = self.__dict__.setdefault("_temp_seen", {})
        key = (ba, icao)
        if key not in cache:
            table = run_table(self.hrrr(icao), "temp_f")
            if not table[0]:
                cache[key] = None
            else:
                inits = sorted(table[0])
                first, last = inits[0].date(), (inits[-1] + pd.Timedelta(days=2)).date()

                def offset_of_day(d):
                    off = self.offset(ba, d.year)
                    if off.empty:
                        return np.nan
                    v = off.get(pd.Timestamp(d) + pd.Timedelta(hours=12), np.nan)
                    return float(off.median()) if np.isnan(v) else float(v)

                cache[key] = forecast_as_seen([table], all_days(first, last), offset_of_day, self.init_hours)
        return cache[key]

    def field_seen_series(self, ba: str, icao: str, field: str) -> pd.Series | None:
        """The forecast of ``field`` for every local hour by the run available at that day's cut-off, one station."""
        cache: dict = self.__dict__.setdefault("_field_seen", {})
        key = (ba, icao, field)
        if key not in cache:
            table = run_table(self.field_rows(field, icao), field)
            if not table[0]:
                cache[key] = None
            else:
                inits = sorted(table[0])
                first, last = inits[0].date(), (inits[-1] + pd.Timedelta(days=2)).date()

                def offset_of_day(d):
                    off = self.offset(ba, d.year)
                    if off.empty:
                        return np.nan
                    v = off.get(pd.Timestamp(d) + pd.Timedelta(hours=12), np.nan)
                    return float(off.median()) if np.isnan(v) else float(v)

                cache[key] = forecast_as_seen([table], all_days(first, last), offset_of_day, self.init_hours)
        return cache[key]

    def field_hour_bias(self, ba: str, icao: str, field: str, day: date) -> np.ndarray:
        """The recent bias of the forecast of ``field`` per local hour at one station, known at the cut-off."""
        key = (ba, icao, field)
        if key not in self._bias_tables:
            seen = self.field_seen_series(ba, icao, field)
            if seen is None:
                self._bias_tables[key] = pd.DataFrame(columns=range(24))
            else:
                years = [y for y in range(seen.index.min().year, seen.index.max().year + 1)]
                observed = pd.concat([self.station_field_series(icao, ba, y, field) for y in years])
                observed = observed[~observed.index.duplicated()].sort_index()
                self._bias_tables[key] = hourly_bias_table(observed, seen)
        return rolling_hour_bias(self._bias_tables[key], day, self.field_bias_days)

    def hour_bias(self, ba: str, icao: str, day: date) -> np.ndarray:
        """The forecast's recent bias per local hour at one station, known at the cut-off of ``day``."""
        key = (ba, icao)
        if key not in self._bias_tables:
            seen = self.temp_seen_series(ba, icao)
            if seen is None:
                self._bias_tables[key] = pd.DataFrame(columns=range(24))
            else:
                years = range(seen.index.min().year, seen.index.max().year + 1)
                observed = pd.concat([self.station_temperature(icao, ba, y) for y in years])
                observed = observed[~observed.index.duplicated()].sort_index()
                self._bias_tables[key] = hourly_bias_table(observed, seen)
        return rolling_hour_bias(self._bias_tables[key], day, self.temp_bias_days)

    def stations_of(self, ba: str) -> list[str]:
        if self.stations == "multi" and ba in BA_STATIONS_MULTI:
            return list(BA_STATIONS_MULTI[ba])
        return [BA_STATION[ba]]

    def field_dir(self, field: str) -> Path:
        return self.field_dirs.get(field, self.hrrr_dir.parent / {"dewpoint_f": "dewpoint", "wind_ms": "wind"}.get(field, field))

    def field_rows(self, field: str, icao: str) -> pd.DataFrame:
        return self._cached(("frows", field, icao), lambda: load_station(self.field_dir(field), icao))

    def station_field_series(self, icao: str, ba: str, year: int, field: str) -> pd.Series:
        def read():
            if self._station_table is None:
                self._station_table = station_table_for(sorted({i for v in BA_STATIONS_MULTI.values() for i in v}),
                                                        self.isd_dir).set_index("icao")
            st = self._station_table.loc[icao]
            return station_field(st["usaf"], st["wban"], ba, year, self.tidy_dir, self.isd_dir, field,
                                 supplement_file=[f for f in (supplement_path(icao, d) for d in self.supplement_dirs) if f])

        return self._cached(("sfield", field, icao, ba, year), read)

    def weather_frame(self, ba: str, start: date, day: date, history_index: pd.DatetimeIndex, path_ts: pd.DatetimeIndex,
                      off_path: np.ndarray, run, run2=None) -> pd.DataFrame | None:
        """One column per field in ``self.fields``: the mean over the BA's stations of the observation over the
        history and of the HRRR path from 09:00 of D-1 (NaN without a run)."""
        if not self.fields:
            return None
        stations = self.stations_of(ba)
        index = history_index.union(path_ts)
        out = pd.DataFrame(index=index)
        for fld in self.fields:
            hist = pd.concat([self._years(ba, start, day, lambda b, y, i=icao, f=fld: self.station_field_series(i, b, y, f))
                              .reindex(history_index) for icao in stations], axis=1).mean(axis=1, skipna=False)
            paths = {}
            for icao in stations:
                rows = self.field_rows(fld, icao)
                paths[icao] = (forecast_path(rows, day, off_path, run, column=fld) if run is not None and len(rows)
                               else np.full(PATH_HOURS, np.nan))
                if run2 is not None and len(rows):
                    paths[icao] = blend_paths(paths[icao], forecast_path(rows, day, off_path, run2, column=fld))
                if fld in self.nbm_field_dirs and run is not None:
                    nrows = self.nbm_field_rows(fld, icao)
                    if len(nrows):
                        col, scale = NBM_FIELD_COLUMNS[fld]
                        paths[icao] = blend_paths(paths[icao], nbm_path(nrows, day, off_path, run, column=col) * scale, self.nbm_weight)
                if self.field_bias_days and run is not None and len(rows):
                    paths[icao] = apply_hour_bias(paths[icao], path_ts, self.field_hour_bias(ba, icao, fld, day))
            path = pd.DataFrame(paths, index=path_ts).mean(axis=1, skipna=False)
            out[fld] = pd.concat([hist, path]).reindex(index).to_numpy(dtype=float)
        return out

    def station_temperature(self, icao: str, ba: str, year: int) -> pd.Series:
        def read():
            if self._station_table is None:
                self._station_table = station_table_for(sorted({i for v in BA_STATIONS_MULTI.values() for i in v}),
                                                        self.isd_dir).set_index("icao")
            st = self._station_table.loc[icao]
            return station_temperature_f(st["usaf"], st["wban"], ba, year, self.tidy_dir, self.isd_dir,
                                         supplement_file=[f for f in (supplement_path(icao, d) for d in self.supplement_dirs) if f])

        return self._cached(("stemp", icao, ba, year), read)

    # ---- cached readers -------------------------------------------------------------------------------
    def raw_load(self, ba: str, year: int) -> pd.Series:
        return self._cached(("raw", ba, year), lambda: apply_label_offsets(load_series_local(self.tidy_dir, ba, year), ba, "demand", self.offsets))

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
            return apply_label_offsets(s, ba, "forecast", self.offsets)

        return self._cached(("forecast", ba, year), read)

    def offset(self, ba: str, year: int) -> pd.Series:
        return self._cached(("offset", ba, year), lambda: utc_offset(self.tidy_dir, ba, year))

    def temperature(self, ba: str, year: int) -> pd.Series:
        def read():
            s = hourly_temperature_f(ba, year, self.tidy_dir, self.isd_dir)
            files = [f for f in (supplement_path(BA_STATION[ba], d) for d in self.supplement_dirs) if f] if ba in BA_STATION else []
            if not files or s.empty or not s.isna().any():
                return s
            off = utc_offset(self.tidy_dir, ba, year).reindex(s.index)
            off = off.fillna(off.median())
            utc = pd.DatetimeIndex(s.index + pd.to_timedelta(off.to_numpy(), unit="h")).tz_localize("UTC")
            v = s.to_numpy(dtype=float).copy()
            for f in files:
                sup = read_asos(f).reindex(utc).to_numpy(dtype=float)
                gap = np.isnan(v)
                v[gap] = sup[gap]
            return pd.Series(v, index=s.index)

        return self._cached(("temp", ba, year), read)

    def nbm_seen_series(self, ba: str, icao: str) -> pd.Series | None:
        """The NBM 2 m temperature for every local hour by the run available at that day's cut-off, one station."""
        cache: dict = self.__dict__.setdefault("_nbm_seen", {})
        key = (ba, icao)
        if key not in cache:
            rows = self.nbm(icao)
            table = run_table(rows, "nbm_temp_f") if len(rows) else ({}, np.zeros((0, 0)))
            if not table[0]:
                cache[key] = None
            else:
                inits = sorted(table[0])
                first, last = inits[0].date(), (inits[-1] + pd.Timedelta(days=2)).date()

                def offset_of_day(d):
                    off = self.offset(ba, d.year)
                    if off.empty:
                        return np.nan
                    v = off.get(pd.Timestamp(d) + pd.Timedelta(hours=12), np.nan)
                    return float(off.median()) if np.isnan(v) else float(v)

                cache[key] = forecast_as_seen([table], all_days(first, last), offset_of_day, self.init_hours)
        return cache[key]

    def nbm_cold_bias(self, ba: str, icao: str, day: date) -> float:
        """The median of observed minus NBM-as-seen on the hours the NBM forecast below the cold threshold, over the
        last ``nbm_cold_bias_days`` known days at one station; zero with fewer than 48 such hours."""
        key = (ba, icao)
        if key not in self._nbm_cold_tables:
            seen = self.nbm_seen_series(ba, icao)
            if seen is None:
                self._nbm_cold_tables[key] = pd.DataFrame(columns=["seen", "e"])
            else:
                years = range(seen.index.min().year, seen.index.max().year + 1)
                observed = pd.concat([self.station_temperature(icao, ba, y) for y in years])
                observed = observed[~observed.index.duplicated()].sort_index().asfreq("h")
                s = seen.reindex(observed.index)
                t = pd.DataFrame({"seen": s, "e": observed - s}).dropna()
                self._nbm_cold_tables[key] = t
        return cold_bias_from_table(self._nbm_cold_tables[key], day, self.nbm_cold_bias_days, self.nbm_cold_threshold_f)

    def gfs(self, icao: str) -> pd.DataFrame:
        if icao not in self._gfs:
            self._gfs[icao] = load_station(self.gfs_dir, icao) if self.gfs_dir else pd.DataFrame()
        return self._gfs[icao]

    def nbm(self, icao: str) -> pd.DataFrame:
        if icao not in self._nbm:
            self._nbm[icao] = load_station(self.nbm_dir, icao) if self.nbm_dir else pd.DataFrame()
        return self._nbm[icao]

    def nbm_daily_rows(self, icao: str) -> pd.DataFrame:
        if icao not in self._nbm_daily:
            self._nbm_daily[icao] = load_daily(self.nbm_daily_dir, icao)
        return self._nbm_daily[icao]

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
        run2 = previous_run(run, self.init_hours) if (self.second_run and run is not None) else None
        paths = {}
        for icao in stations:
            rows = self.hrrr(icao)
            paths[icao] = forecast_path(rows, day, off_path, run) if run is not None and len(rows) else np.full(PATH_HOURS, np.nan)
            if run2 is not None and len(rows):
                paths[icao] = blend_paths(paths[icao], forecast_path(rows, day, off_path, run2))
            sources = [paths[icao]]                                    # the models that enter the temperature mean
            if self.nbm_mode and run is not None:
                nrows = self.nbm(icao)
                if len(nrows):
                    npath = nbm_path(nrows, day, off_path, run)
                    if self.nbm_cold_bias_days:
                        npath = apply_cold_bias(npath, self.nbm_cold_bias(ba, icao, day), self.nbm_cold_threshold_f)
                    if self.nbm_mode == "blend":
                        if self.gfs_dir is None:
                            paths[icao] = blend_paths(paths[icao], npath, self.nbm_weight)
                        sources.append(npath)
                    else:                                              # replace: NBM where known, HRRR elsewhere
                        paths[icao] = np.where(np.isfinite(npath), npath, paths[icao])
            if self.gfs_dir is not None and not np.isnan(off_cutoff):
                grows = self.gfs(icao)
                if len(grows):
                    grun = run_for_day(day, float(off_cutoff), (12, 6), lag_h=self.gfs_lag_h)
                    sources.append(nbm_path(grows, day, off_path, grun, column="gfs_temp_f"))
                    paths[icao] = np.where(np.isfinite(mean_paths(sources)), mean_paths(sources), paths[icao])
            if self.temp_bias_days and run is not None and len(rows):
                paths[icao] = apply_hour_bias(paths[icao], path_ts, self.hour_bias(ba, icao, day))
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

        weather = self.weather_frame(ba, start, day, history_index, path_ts, off_path, run, run2)

        nbm_daily = None
        if self.nbm_daily_dir is not None and run is not None:
            per_station = [daily_at_cutoff(self.nbm_daily_rows(icao), run) for icao in stations]
            per_station = [d for d in per_station if d]
            if per_station:
                keys = set().union(*per_station)
                nbm_daily = {k: float(np.nanmean([d[k] for d in per_station if k in d])) for k in keys}

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
            benchmark_plausible=forecast_plausible(fcst.reindex(hours).to_numpy(dtype=float), outcome.reindex(hours).to_numpy(dtype=float)),
            sky=sky, stations=stations, temp_history_stations_f=stations_hist,
            temp_forecast_path_stations_f=path_frame if len(stations) > 1 else None, weather=weather, run_second=run2,
            nbm_daily=nbm_daily,
        )
