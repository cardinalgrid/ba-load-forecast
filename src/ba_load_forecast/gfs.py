"""The GFS 0.25 degree 2 m temperature at the stations, from the public archive on AWS (``noaa-gfs-bdp-pds``).

The archive holds one GRIB2 file per run and forecast hour (``gfs.YYYYMMDD/HH/atmos/gfs.tHHz.pgrb2.0p25.fFFF``;
the ``atmos`` folder exists from 23 March 2021, earlier runs sit one level up; the bucket starts on
1 January 2021), each with a ``.idx`` file giving the byte range of every message, so one message of about
0.9 MB is downloaded per forecast hour (``hrrr_grib`` does the same for the HRRR flux) and decoded with ecCodes.
The grid is the global 0.25 degree latitude-longitude grid, 721 rows from 90 N to 90 S and 1440 columns from
0 E eastward; a station takes the nearest grid point (at most 0.125 degree, about 14 km, away).

The GFS finishes its 0.25 degree run about four hours after the initialisation, so at a 9 a.m. cut-off the run
available is the 06 UTC one in the Eastern, Central and Mountain zones and the 12 UTC one in the Pacific zone in
standard time (``run_for_day`` with a 5 h lag): both are extracted, with the leads a 39-hour path needs.

Output layout is that of ``hrrr.extract``: one ``runs/<YYYYMMDD>_<HH>z.parquet`` per run with the columns
``icao, init_utc, lead_h, valid_utc, gfs_temp_f``; ``hrrr.consolidate`` gathers them per station.
"""

from __future__ import annotations

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .hrrr import KEYS, days_between, run_file, with_retries
from .hrrr_grib import _get, message_range

BASE = "https://noaa-gfs-bdp-pds.s3.amazonaws.com"
ATMOS_FROM = date(2021, 3, 23)
KEY = ":TMP:2 m above ground:"
NLAT, NLON = 721, 1440
STEP = 0.25
LAG_H = 5                                     # availability lag of the 0.25 degree run (cutoff.run_for_day)
LEADS = {6: tuple(range(8, 50)), 12: tuple(range(2, 44))}   # the 39-hour path of a 9 a.m. cut-off in every zone


def gfs_url(day: date, init_hour: int, lead: int) -> str:
    sub = "atmos/" if day >= ATMOS_FROM else ""
    return f"{BASE}/gfs.{day:%Y%m%d}/{init_hour:02d}/{sub}gfs.t{init_hour:02d}z.pgrb2.0p25.f{lead:03d}"


def grid_index(lat, lon) -> tuple[np.ndarray, np.ndarray]:
    """Row and column of the nearest 0.25 degree grid point."""
    row = np.rint((90.0 - np.asarray(lat, dtype=float)) / STEP).astype(int)
    col = np.rint((np.asarray(lon, dtype=float) % 360.0) / STEP).astype(int) % NLON
    return np.clip(row, 0, NLAT - 1), col


def station_cells(table: pd.DataFrame) -> dict[str, tuple[int, int]]:
    row, col = grid_index(table["lat"].to_numpy(), table["lon"].to_numpy())
    return {str(i): (int(r), int(c)) for i, r, c in zip(table["icao"], row, col, strict=True)}


def decode(message: bytes) -> np.ndarray:
    import eccodes

    gid = eccodes.codes_new_from_message(message)
    try:
        lat0 = eccodes.codes_get(gid, "latitudeOfFirstGridPointInDegrees")
        ni, nj = eccodes.codes_get(gid, "Ni"), eccodes.codes_get(gid, "Nj")
        grid = eccodes.codes_get_values(gid).reshape(nj, ni)
        if lat0 < 0:                          # scanning from the south: flip to 90 N first
            grid = grid[::-1]
        return grid
    finally:
        eccodes.codes_release(gid)


def message_bytes(day: date, init_hour: int, lead: int) -> bytes:
    """The 2 m temperature message of one forecast hour (a byte-range read guided by the .idx file)."""
    url = gfs_url(day, init_hour, lead)
    start, end = message_range(_get(url + ".idx").decode(), KEY)
    return _get(url, {"Range": f"bytes={start}-{end if end is not None else ''}"})


def field_at_points(day: date, init_hour: int, lead: int, cells: dict[str, tuple[int, int]]) -> dict[str, float]:
    grid = decode(message_bytes(day, init_hour, lead))
    return {icao: float((grid[r, c] - 273.15) * 9.0 / 5.0 + 32.0) for icao, (r, c) in cells.items()}


def run_exists(day: date, init_hour: int) -> bool:
    """The run is in the archive when its first hourly or first three-hourly file has an index (before 23 March
    2021 the archive keeps three-hourly files only)."""
    first = LEADS[init_hour][0]
    for lead in (first, first + (-first) % 3):
        try:
            _get(gfs_url(day, init_hour, lead) + ".idx")
            return True
        except FileNotFoundError:
            continue
    return False


def run_frame(day: date, init_hour: int, cells: dict[str, tuple[int, int]], workers: int = 8,
              log: Callable[[str], None] = print) -> pd.DataFrame | None:
    """Rows for one run and its leads (the hours the archive has: hourly, or three-hourly before 23 March 2021);
    None when the run is not in the archive. Downloads run in threads, decoding in the calling thread."""
    init = datetime(day.year, day.month, day.day, init_hour)
    if not run_exists(day, init_hour):
        return None
    leads = LEADS[init_hour] if day >= ATMOS_FROM else tuple(k for k in LEADS[init_hour] if k % 3 == 0)

    def fetch(lead):
        try:
            return lead, with_retries(lambda: message_bytes(day, init_hour, lead), f"{day} {init_hour:02d}Z f{lead:03d}", log)
        except FileNotFoundError:
            return lead, None

    rows = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for lead, data in pool.map(fetch, leads):
            if data is None:
                continue
            grid = with_retries(lambda data=data: decode(data), f"{day} {init_hour:02d}Z f{lead:03d} decode", log, waits=(1.0, 3.0))
            for icao, (r, c) in cells.items():
                rows.append((icao, init, lead, init + timedelta(hours=lead), float((grid[r, c] - 273.15) * 9.0 / 5.0 + 32.0)))
    return pd.DataFrame(rows, columns=[*KEYS, "gfs_temp_f"]).astype({"lead_h": "int16", "gfs_temp_f": "float32"})


def extract(cells: dict[str, tuple[int, int]], start: date, end: date, out_dir: Path, init_hours: tuple[int, ...] = (6, 12),
            workers: int = 8, log: Callable[[str], None] = print) -> int:
    """One run file per day and initialisation hour, as ``hrrr.extract``; resumable; an absent run leaves an empty file."""
    out_dir = Path(out_dir)
    (out_dir / "runs").mkdir(parents=True, exist_ok=True)
    fetched = 0
    for day in days_between(start, end):
        for h in init_hours:
            f = run_file(out_dir, day, h)
            if f.exists():
                continue
            frame = run_frame(day, h, cells, workers=workers, log=log)
            if frame is None:
                frame = pd.DataFrame(columns=[*KEYS, "gfs_temp_f"])
                log(f"{day} {h:02d}Z: run not in the archive")
            tmp = f.with_suffix(".tmp")
            frame.to_parquet(tmp, index=False)
            tmp.replace(f)
            fetched += 1
            log(f"{day} {h:02d}Z: {len(frame)} rows, leads {int(frame['lead_h'].min()) if len(frame) else '-'}-{int(frame['lead_h'].max()) if len(frame) else '-'}")
    return fetched
