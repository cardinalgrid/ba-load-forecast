"""Fields the HRRR Zarr archive lacks, read from the GRIB2 archive on AWS (``noaa-hrrr-bdp-pds``, public).

The surface downward short-wave flux (``DSWRF``, W/m²) is present only as metadata in the Zarr archive before
2025, but every GRIB2 run file carries it, and the ``.idx`` file next to each run gives the byte range of every
message. So one message (about 2.5 MB by day, a few hundred bytes at night, when the field is zero) is
downloaded per forecast hour and decoded with ecCodes; the values at the stations' grid points are kept. The
grid is the same 1059 by 1799 Lambert grid as the Zarr archive, in the same row-major order (checked against
the stored 2 m temperatures), so the Zarr grid indices apply unchanged.

Output layout is that of ``hrrr.extract``: one ``runs/<YYYYMMDD>_<HH>z.parquet`` per run with the columns
``icao, init_utc, lead_h, valid_utc, <field>``; ``hrrr.consolidate`` gathers them per station.
"""

from __future__ import annotations

import urllib.error
import urllib.request
from collections.abc import Callable
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .hrrr import KEYS, days_between, run_file, with_retries
from .hrrr_grid import GridPoint

GRIB_BASE = "https://noaa-hrrr-bdp-pds.s3.amazonaws.com"
NY, NX = 1059, 1799
GRIB_FIELDS = {"dswrf_wm2": ":DSWRF:surface:"}     # output column -> key in the .idx line
ZERO_MESSAGE_BYTES = 5000                            # a constant (night) field packs into a few hundred bytes
CUTOFF_LEADS = tuple(range(17, 46))                  # the leads a 9 a.m. cut-off uses (cutoff.lead_hours)


def grib_url(day: date, init_hour: int, lead: int) -> str:
    return f"{GRIB_BASE}/hrrr.{day.strftime('%Y%m%d')}/conus/hrrr.t{init_hour:02d}z.wrfsfcf{lead:02d}.grib2"


def _get(url: str, headers: dict | None = None, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code in (403, 404):
            raise FileNotFoundError(url) from e
        raise


def message_range(index_text: str, key: str) -> tuple[int, int | None]:
    """Byte range of the message whose .idx line contains ``key`` (end None for the last message)."""
    lines = index_text.splitlines()
    for i, line in enumerate(lines):
        if key in line:
            start = int(line.split(":")[1])
            end = int(lines[i + 1].split(":")[1]) - 1 if i + 1 < len(lines) else None
            return start, end
    raise KeyError(key)


def decode(message: bytes) -> np.ndarray:
    import eccodes

    gid = eccodes.codes_new_from_message(message)
    try:
        return eccodes.codes_get_values(gid).reshape(NY, NX)
    finally:
        eccodes.codes_release(gid)


def field_at_points(day: date, init_hour: int, lead: int, points: dict[str, GridPoint], key: str) -> dict[str, float]:
    """The field's value at each station's grid point for one forecast hour; zeros when the message is constant."""
    url = grib_url(day, init_hour, lead)
    start, end = message_range(_get(url + ".idx").decode(), key)
    if end is not None and end - start + 1 < ZERO_MESSAGE_BYTES:
        return {icao: 0.0 for icao in points}
    grid = decode(_get(url, {"Range": f"bytes={start}-{end if end is not None else ''}"}))
    return {icao: float(grid[p.y, p.x]) for icao, p in points.items()}


def run_frame(day: date, init_hour: int, points: dict[str, GridPoint], field: str = "dswrf_wm2",
              leads=CUTOFF_LEADS, log: Callable[[str], None] = print) -> pd.DataFrame | None:
    """Rows for one run and the given leads; None when the run is not in the archive."""
    key = GRIB_FIELDS[field]
    init = datetime(day.year, day.month, day.day, init_hour)
    rows = []
    for lead in leads:
        try:
            vals = with_retries(lambda lead=lead: field_at_points(day, init_hour, lead, points, key), f"{day} {init_hour:02d}Z f{lead:02d}", log)
        except FileNotFoundError:
            if lead == leads[0]:
                return None
            continue
        for icao, v in vals.items():
            rows.append((icao, init, lead, init + timedelta(hours=lead), v))
    return pd.DataFrame(rows, columns=[*KEYS, field]).astype({"lead_h": "int16", field: "float32"})


def extract(points: dict[str, GridPoint], start: date, end: date, out_dir: Path, init_hours: tuple[int, ...] = (12, 6),
            field: str = "dswrf_wm2", leads=CUTOFF_LEADS, resume: bool = True, log: Callable[[str], None] = print) -> int:
    """One run file per day and initialisation hour, as ``hrrr.extract``; resumable."""
    out_dir = Path(out_dir)
    (out_dir / "runs").mkdir(parents=True, exist_ok=True)
    fetched = 0
    for day in days_between(start, end):
        for h in init_hours:
            f = run_file(out_dir, day, h)
            if resume and f.exists():
                continue
            frame = run_frame(day, h, points, field, leads, log)
            if frame is None:
                frame = pd.DataFrame({c: pd.Series(dtype=t) for c, t in
                                      zip([*KEYS, field], ["object", "datetime64[ns]", "int16", "datetime64[ns]", "float32"], strict=True)})
                log(f"{day} {h:02d}Z: run not in the archive")
            tmp = f.with_suffix(".tmp")
            frame.to_parquet(tmp, index=False)
            tmp.replace(f)
            fetched += 1
            if fetched % 10 == 0:
                log(f"{day} {h:02d}Z: {fetched} runs fetched")
    return fetched
