"""The National Blend of Models (NBM) at the stations, from the public archive on AWS (``noaa-nbm-pds``).

The archive keeps one GeoTIFF per element and forecast hour under
``blendv<version>/conus/<YYYY>/<MM>/<DD>/<HHMM>/<element>/blendv<version>_conus_<element>_<init>_<valid>.tif``
(versions 3.2, 4.0, 4.1, 4.2 and 4.3 in separate trees, each covering its own months). The CONUS grid is a
Lambert conformal conic on a sphere (radius 6 371 200 m, standard parallel and origin at 25 N, central
meridian 95 W), 2345 by 1597 cells of 2 539.703 m, stored as tiled, LZW-compressed 16-bit integers with
-9999 as no data; the ``temp`` element is the 2 m temperature in whole degrees Fahrenheit. Forecast hours are
hourly to 36 h and three-hourly beyond, so the last hours of a 9 a.m. cut-off path (leads 37 to 45) come from
the 39, 42 and 45 h files and are interpolated when the path is built.

The grid parameters below were read from the GeoTIFF keys of the archive's own files (``ProjCoordTrans``
LambertConfConic_2SP, ``ModelTiepoint``, ``ModelPixelScale``) and checked against the HRRR at the same
stations and hour (mean difference 0.25 F, mean absolute difference 1.9 F between the two models).

Output layout is that of ``hrrr.extract``: one ``runs/<YYYYMMDD>_<HH>z.parquet`` per run with the columns
``icao, init_utc, lead_h, valid_utc, nbm_temp_f``; ``hrrr.consolidate`` gathers them per station.
"""

from __future__ import annotations

import io
import re
import urllib.error
import urllib.request
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .hrrr import days_between, run_file, with_retries

BASE = "https://noaa-nbm-pds.s3.amazonaws.com/"
VERSIONS = ("4.3", "4.2", "4.1", "4.0", "3.2")          # newest first: the first tree that has the run wins
ELEMENTS = {"nbm_temp_f": "temp", "nbm_dewpoint_f": "dewpoint", "nbm_wind_mph": "windspd"}
NODATA = -9999

# Lambert conformal conic of the CONUS grid, from the GeoTIFF keys
RADIUS_M = 6371200.0
LAT_1 = 25.0
LAT_0 = 25.0
LON_0 = 265.0
X_0 = -3272421.457337171                                 # easting of the centre of cell (0, 0)... see cell_of
Y_0 = 3790842.1060354356
CELL_M = 2539.703
NY, NX = 1597, 2345


def lcc_xy(lat, lon) -> tuple[np.ndarray, np.ndarray]:
    """Easting and northing (m) of latitude and longitude (degrees) on the archive's projection."""
    lat = np.radians(np.asarray(lat, dtype=float))
    lon = np.radians(np.asarray(lon, dtype=float))
    p1, p0, l0 = np.radians(LAT_1), np.radians(LAT_0), np.radians(LON_0)
    n = np.sin(p1)                                        # one standard parallel
    f = np.cos(p1) * np.tan(np.pi / 4 + p1 / 2) ** n / n
    rho = RADIUS_M * f / np.tan(np.pi / 4 + lat / 2) ** n
    rho0 = RADIUS_M * f / np.tan(np.pi / 4 + p0 / 2) ** n
    theta = n * ((lon - l0 + np.pi) % (2 * np.pi) - np.pi)
    return rho * np.sin(theta), rho0 - rho * np.cos(theta)


def cell_of(lat, lon) -> tuple[np.ndarray, np.ndarray]:
    """Row and column of the grid cell containing each point (the tie point is the outer corner of cell 0, 0)."""
    x, y = lcc_xy(lat, lon)
    col = np.floor((x - X_0) / CELL_M).astype(int)
    row = np.floor((Y_0 - y) / CELL_M).astype(int)
    return row, col


def station_cells(table: pd.DataFrame) -> dict[str, tuple[int, int]]:
    """``icao -> (row, col)`` from a table with ``icao, lat, lon``; points off the grid are dropped."""
    row, col = cell_of(table["lat"].to_numpy(), table["lon"].to_numpy())
    out = {}
    for icao, r, c in zip(table["icao"], row, col, strict=True):
        if 0 <= r < NY and 0 <= c < NX:
            out[str(icao)] = (int(r), int(c))
    return out


def _get(url: str, timeout: int = 120) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise FileNotFoundError(url) from e
        raise


def list_run(day: date, init_hour: int, element: str, versions: tuple[str, ...] = VERSIONS) -> tuple[str, list[str]] | None:
    """The version tree holding the run and the keys of its files for one element (None when no tree has it)."""
    for v in versions:
        prefix = f"blendv{v}/conus/{day:%Y/%m/%d}/{init_hour:02d}00/{element}/"
        url = f"{BASE}?list-type=2&prefix={prefix}&max-keys=400"
        text = with_retries(lambda u=url: _get(u), f"list {prefix}", log=lambda m: None).decode()
        keys = re.findall(r"<Key>([^<]+)</Key>", text)
        if keys:
            return v, keys
    return None


def lead_of(key: str) -> int | None:
    """Forecast lead (h) from the file name ``..._<init>_<valid>.tif``."""
    m = re.search(r"_(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})_(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})\.tif$", key)
    if not m:
        return None
    init, valid = (datetime.strptime(s, "%Y-%m-%dT%H:%M") for s in m.groups())
    return int((valid - init).total_seconds() // 3600)


def read_cells(data: bytes, cells: dict[str, tuple[int, int]]) -> dict[str, float]:
    import tifffile

    grid = tifffile.imread(io.BytesIO(data))
    out = {}
    for icao, (r, c) in cells.items():
        v = float(grid[r, c])
        out[icao] = np.nan if v == NODATA else v
    return out


def run_frame(day: date, init_hour: int, cells: dict[str, tuple[int, int]], column: str = "nbm_temp_f",
              max_lead: int = 45, workers: int = 16, log: Callable[[str], None] = print) -> pd.DataFrame:
    """Every forecast hour of the run up to ``max_lead`` at the stations, downloaded in parallel."""
    listed = list_run(day, init_hour, ELEMENTS[column])
    if listed is None:
        raise FileNotFoundError(f"no NBM tree has {day} {init_hour:02d}Z")
    version, keys = listed
    wanted = [(lead_of(k), k) for k in keys]
    wanted = sorted((lead, k) for lead, k in wanted if lead is not None and 1 <= lead <= max_lead)
    init_ts = pd.Timestamp(datetime(day.year, day.month, day.day, init_hour))

    def fetch(item):
        lead, key = item
        data = with_retries(lambda: _get(BASE + urllib.request.quote(key)), key, log=log)
        return lead, read_cells(data, cells)

    rows = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for lead, values in pool.map(fetch, wanted):
            for icao, v in values.items():
                rows.append({"icao": icao, "init_utc": init_ts, "lead_h": lead,
                             "valid_utc": init_ts + pd.Timedelta(hours=lead), column: v})
    frame = pd.DataFrame(rows, columns=["icao", "init_utc", "lead_h", "valid_utc", column])
    frame.attrs["version"] = version
    return frame


def extract(cells: dict[str, tuple[int, int]], start: date, end: date, out_dir: Path, init_hours: tuple[int, ...] = (12, 6),
            column: str = "nbm_temp_f", max_lead: int = 45, workers: int = 16, log: Callable[[str], None] = print) -> int:
    """Resumable: one parquet per run under ``out_dir/runs``; runs whose file exists are skipped. Returns the
    number of runs written; a run absent from every tree writes an empty file so that it is not retried."""
    out_dir = Path(out_dir)
    (out_dir / "runs").mkdir(parents=True, exist_ok=True)
    written = 0
    for day in days_between(start, end):
        for h in init_hours:
            f = run_file(out_dir, day, h)
            if f.exists():
                continue
            try:
                frame = run_frame(day, h, cells, column=column, max_lead=max_lead, workers=workers, log=log)
            except FileNotFoundError as e:
                log(f"{day} {h:02d}Z absent ({e})")
                frame = pd.DataFrame(columns=["icao", "init_utc", "lead_h", "valid_utc", column])
            frame.to_parquet(f, index=False)
            written += 1
            log(f"{day} {h:02d}Z v{frame.attrs.get('version', '?')}: {len(frame)} rows, leads "
                f"{int(frame['lead_h'].min()) if len(frame) else '-'}-{int(frame['lead_h'].max()) if len(frame) else '-'}")
    return written


# Daily products of the target day D (the run is initialised on D-1): the overnight minimum is the 18-h period ending
# 18 UTC of D ("mint18"), the daytime maximum the 18-h period ending 06 UTC of D+1 ("maxt18"); percentiles and the
# mean and spread of the NBM distribution, and the probabilities of the extreme thresholds (whole degrees Fahrenheit,
# probabilities in percent).
DAILY_ELEMENTS = ("mint18p05", "mint18p50", "mint18p95", "mint18pmean", "mint18stddev",
                  "maxt18p05", "maxt18p50", "maxt18p95", "maxt18pmean", "maxt18stddev",
                  "probmint18lt000", "probmint18lt010", "probmint18lt032",
                  "probmaxt18gt090", "probmaxt18gt100", "probmaxt18gt110")


def daily_valid(day_init: date, element: str) -> datetime:
    """The valid time of the file that describes the target day D = ``day_init`` + 1 for a daily element."""
    target = day_init + timedelta(days=1)
    if element.startswith("mint18") or element.startswith("probmint18"):
        return datetime(target.year, target.month, target.day, 18)
    after = target + timedelta(days=1)
    return datetime(after.year, after.month, after.day, 6)


def valid_of(key: str) -> datetime | None:
    m = re.search(r"_(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})\.tif$", key)
    return datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M") if m else None


def daily_frame(day: date, init_hour: int, cells: dict[str, tuple[int, int]], elements: tuple[str, ...] = DAILY_ELEMENTS,
                workers: int = 8, log: Callable[[str], None] = print) -> pd.DataFrame:
    """One value per station and element for the target day (long format: ``icao, init_utc, element, valid_utc,
    lead_h, value``); elements or files the archive lacks are simply missing from the frame."""
    init_ts = pd.Timestamp(datetime(day.year, day.month, day.day, init_hour))
    wanted = []
    version = None                                        # found once, then the other elements are listed in that tree only
    for element in elements:
        listed = list_run(day, init_hour, element, versions=VERSIONS if version is None else (version,))
        if listed is None:
            continue
        version, keys = listed
        want = daily_valid(day, element)
        for k in keys:
            if valid_of(k) == want:
                wanted.append((element, k, want))
                break

    def fetch(item):
        element, key, valid = item
        data = with_retries(lambda: _get(BASE + urllib.request.quote(key)), key, log=log)
        return element, valid, read_cells(data, cells)

    rows = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for element, valid, values in pool.map(fetch, wanted):
            lead = int((valid - init_ts.to_pydatetime()).total_seconds() // 3600)
            for icao, v in values.items():
                rows.append({"icao": icao, "init_utc": init_ts, "element": element, "valid_utc": pd.Timestamp(valid),
                             "lead_h": lead, "value": v})
    frame = pd.DataFrame(rows, columns=["icao", "init_utc", "element", "valid_utc", "lead_h", "value"])
    frame.attrs["version"] = version or "?"
    return frame


def extract_daily(cells: dict[str, tuple[int, int]], start: date, end: date, out_dir: Path, init_hours: tuple[int, ...] = (12, 6),
                  elements: tuple[str, ...] = DAILY_ELEMENTS, workers: int = 8, log: Callable[[str], None] = print) -> int:
    """Resumable like ``extract``: one parquet per run under ``out_dir/runs`` with the daily products."""
    out_dir = Path(out_dir)
    (out_dir / "runs").mkdir(parents=True, exist_ok=True)
    written = 0
    for day in days_between(start, end):
        for h in init_hours:
            f = run_file(out_dir, day, h)
            if f.exists():
                continue
            frame = daily_frame(day, h, cells, elements=elements, workers=workers, log=log)
            frame.to_parquet(f, index=False)
            written += 1
            log(f"{day} {h:02d}Z v{frame.attrs.get('version', '?')}: {frame['element'].nunique()} elements, {len(frame)} rows")
    return written


def nbm_path(rows: pd.DataFrame, day: date, offset_h, init: tuple[date, int], column: str = "nbm_temp_f",
             max_gap_h: int = 3) -> np.ndarray:
    """The 39-hour path (09:00 of D-1 to 23:00 of D) of an NBM element from the run ``init``: the hourly files
    to 36 h, and the three-hourly files beyond linearly interpolated between neighbours no more than ``max_gap_h``
    apart (the interpolation runs over the whole run, so the last hours of the path sit between the 39, 42 and
    45 h files); hours the run does not reach stay NaN."""
    from .cutoff import PATH_HOURS, path_timestamps

    d, h = init
    init_ts = pd.Timestamp(datetime(d.year, d.month, d.day, h))
    run = rows[rows["init_utc"] == init_ts]
    if run.empty:
        return np.full(PATH_HOURS, np.nan)
    s = pd.Series(run[column].to_numpy(dtype=float), index=pd.DatetimeIndex(run["valid_utc"]))
    s = s[~s.index.duplicated()].sort_index()
    hourly = s.reindex(pd.date_range(s.index.min(), s.index.max(), freq="h"))
    hourly = hourly.interpolate(limit=max_gap_h - 1, limit_area="inside")
    off = np.broadcast_to(np.asarray(offset_h, dtype=float), (PATH_HOURS,))
    local = path_timestamps(day)
    valid = pd.DatetimeIndex(local.to_numpy() + (off * 3600.0 * 1e9).astype("timedelta64[ns]"))
    return hourly.reindex(valid).to_numpy(dtype=float)


def daily_at_cutoff(daily: pd.DataFrame, init: tuple[date, int]) -> dict[str, float]:
    """``element -> value`` of one station's daily products for the target day, from the run ``init``."""
    d, h = init
    init_ts = pd.Timestamp(datetime(d.year, d.month, d.day, h))
    sub = daily[daily["init_utc"] == init_ts]
    return {str(e): float(v) for e, v in zip(sub["element"], sub["value"], strict=True)}


def load_daily(out_dir: Path, icao: str) -> pd.DataFrame:
    """The consolidated daily products of one station (``icao, init_utc, element, valid_utc, lead_h, value``)."""
    f = Path(out_dir) / f"{icao}.parquet"
    if not f.exists():
        return pd.DataFrame(columns=["icao", "init_utc", "element", "valid_utc", "lead_h", "value"])
    return pd.read_parquet(f)


def leads_for_path(day: date, offset_h: float, init: tuple[date, int]) -> np.ndarray:
    """Convenience for callers: the leads of the 39 path hours (09:00 D-1 to 23:00 D) in the run ``init``."""
    d, h = init
    init_utc = datetime(d.year, d.month, d.day, h)
    first = datetime(day.year, day.month, day.day, 9) - timedelta(days=1) + timedelta(hours=offset_h)
    return np.array([(first + timedelta(hours=k) - init_utc).total_seconds() / 3600.0 for k in range(39)])
