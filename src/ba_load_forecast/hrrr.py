"""Point reads of 2 m temperature from the public HRRR Zarr archive, and a resumable extraction.

Archive layout (``s3://hrrrzarr``): ``sfc/YYYYMMDD/YYYYMMDD_HHz_fcst.zarr`` holds one forecast run; inside
it, ``2m_above_ground/TMP/2m_above_ground/TMP`` is the array of 2 m temperature in kelvin with shape
``(lead, y, x)``, lead 1 h first. Runs at 00, 06, 12 and 18 UTC reach 48 h since 2 December 2020 (36 h
before that, back to August 2018); the other runs reach 18 h. Chunks are ``(lead, 150, 150)`` and are read
whole, so one download serves every station in the same chunk.

The extraction writes one parquet per run (``runs/YYYYMMDD_HHz.parquet``) with the columns
``icao, init_utc, lead_h, valid_utc, temp_f``; a run that the archive does not have leaves an empty file so
that a resumed extraction does not ask for it again. ``consolidate`` gathers the run files into one parquet
per station.
"""

from __future__ import annotations

import json
import time
from collections.abc import Callable, Iterable
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .hrrr_grid import BUCKET, CHUNK, GridPoint

VARIABLE = "2m_above_ground/TMP"
COLUMNS = ["icao", "init_utc", "lead_h", "valid_utc", "temp_f"]
RETRY_WAITS_S = (5, 15, 45, 120, 300, 600)


def with_retries(call: Callable[[], object], what: str, log: Callable[[str], None] = print,
                 waits: tuple[float, ...] | None = None):
    """Run ``call``; on any error other than a missing object, wait and try again, then give up.

    Network errors (DNS, connection resets, throttling) are transient on a job that runs for hours;
    ``FileNotFoundError`` is how the archive reports an object that does not exist and is not retried.
    """
    waits = RETRY_WAITS_S if waits is None else waits
    for i, wait in enumerate((*waits, None)):
        try:
            return call()
        except FileNotFoundError:
            raise
        except Exception as e:
            if wait is None:
                raise
            log(f"{what}: {type(e).__name__}: {str(e)[:120]}; retry {i + 1}/{len(waits)} in {wait} s")
            time.sleep(wait)
    return None  # pragma: no cover


def kelvin_to_f(k):
    return (np.asarray(k, dtype=float) - 273.15) * 9.0 / 5.0 + 32.0


def run_root(day: date, init_hour: int, bucket: str = BUCKET) -> str:
    d = day.strftime("%Y%m%d")
    return f"{bucket}/sfc/{d}/{d}_{init_hour:02d}z_fcst.zarr/{VARIABLE}/{VARIABLE}"


def run_meta(fs, root: str, log: Callable[[str], None] = print) -> dict | None:
    """The Zarr array metadata of a run (shape, chunks, dtype, compressor), or None when the run is absent."""
    try:
        return json.loads(with_retries(lambda: fs.cat(f"{root}/.zarray"), f"{root}/.zarray", log))
    except FileNotFoundError:
        return None


def decode_chunk(raw: bytes, meta: dict) -> np.ndarray:
    """One compressed chunk to a float32 array ``(lead, CHUNK, CHUNK)``; the fill value becomes NaN."""
    import numcodecs

    codec = numcodecs.get_codec(meta["compressor"])
    buf = codec.decode(raw)
    for f in meta.get("filters") or []:
        buf = numcodecs.get_codec(f).decode(buf)
    n_lead = meta["chunks"][0]
    a = np.frombuffer(buf, dtype=np.dtype(meta["dtype"])).reshape(n_lead, meta["chunks"][1], meta["chunks"][2])
    out = a.astype(np.float32)
    fill = meta.get("fill_value")
    if fill is not None:
        out[a == np.asarray(fill, dtype=a.dtype)] = np.nan
    return out


def read_run(fs, day: date, init_hour: int, points: dict[str, GridPoint], bucket: str = BUCKET,
             log: Callable[[str], None] = print) -> dict[str, np.ndarray] | None:
    """Temperature in Fahrenheit per lead (index 0 = lead 1 h) for every station, or None if the run is absent.

    Every chunk needed is fetched in one concurrent request; a chunk the archive lacks gives NaN for its
    stations, a chunk that fails for any other reason is fetched again (``with_retries``).
    """
    root = run_root(day, init_hour, bucket)
    meta = run_meta(fs, root, log)
    if meta is None:
        return None
    if tuple(meta["chunks"][1:]) != (CHUNK, CHUNK):
        raise ValueError(f"unexpected chunking {meta['chunks']} in {root}")
    n_lead = meta["shape"][0]
    keys = sorted({p.chunk_key for p in points.values()})
    paths = [f"{root}/0.{k}" for k in keys]

    def fetch():
        got = fs.cat(paths, on_error="return")
        bad = [q for q, r in got.items() if isinstance(r, Exception) and not isinstance(r, FileNotFoundError)]
        if bad:
            raise OSError(f"{len(bad)} chunk reads failed, e.g. {bad[0]}: {got[bad[0]]}")
        return got

    raw = with_retries(fetch, f"{root} chunks", log)
    blocks: dict[str, np.ndarray | None] = {}
    for k in keys:
        r = raw.get(f"{root}/0.{k}")
        blocks[k] = None if r is None or isinstance(r, Exception) else decode_chunk(r, meta)[:n_lead]
    out = {}
    for icao, p in points.items():
        b = blocks[p.chunk_key]
        out[icao] = np.full(n_lead, np.nan) if b is None else kelvin_to_f(b[:, p.in_chunk_y, p.in_chunk_x])
    return out


def run_frame(fs, day: date, init_hour: int, points: dict[str, GridPoint], bucket: str = BUCKET,
              log: Callable[[str], None] = print):
    """The tidy rows of one run (``COLUMNS``), or None when the run is absent."""
    temps = read_run(fs, day, init_hour, points, bucket, log)
    if temps is None:
        return None
    init = datetime(day.year, day.month, day.day, init_hour)
    parts = []
    for icao, t in temps.items():
        lead = np.arange(1, len(t) + 1)
        parts.append(pd.DataFrame({"icao": icao, "init_utc": init, "lead_h": lead.astype("int16"),
                                   "valid_utc": init + pd.to_timedelta(lead, unit="h"), "temp_f": t.astype("float32")}))
    return pd.concat(parts, ignore_index=True)[COLUMNS]


def run_file(out_dir: Path, day: date, init_hour: int) -> Path:
    return Path(out_dir) / "runs" / f"{day.strftime('%Y%m%d')}_{init_hour:02d}z.parquet"


def days_between(start: date, end: date) -> Iterable[date]:
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def extract(points: dict[str, GridPoint], start: date, end: date, out_dir: Path, init_hours: tuple[int, ...] = (12, 6),
            fs=None, resume: bool = True, log: Callable[[str], None] = print, bucket: str = BUCKET) -> int:
    """Write one run file per day and initialisation hour in ``[start, end]``; returns the number of runs fetched.

    With ``resume`` a run whose file exists is skipped, so an interrupted extraction continues where it stopped.
    """
    if fs is None:
        import s3fs

        fs = s3fs.S3FileSystem(anon=True)
    out_dir = Path(out_dir)
    (out_dir / "runs").mkdir(parents=True, exist_ok=True)
    fetched = 0
    for day in days_between(start, end):
        for h in init_hours:
            f = run_file(out_dir, day, h)
            if resume and f.exists():
                continue
            frame = run_frame(fs, day, h, points, bucket, log)
            if frame is None:
                frame = pd.DataFrame({c: pd.Series(dtype=t) for c, t in
                                      zip(COLUMNS, ["object", "datetime64[ns]", "int16", "datetime64[ns]", "float32"], strict=True)})
                log(f"{day} {h:02d}Z: run not in the archive")
            tmp = f.with_suffix(".tmp")
            frame.to_parquet(tmp, index=False)
            tmp.replace(f)
            fetched += 1
            if fetched % 20 == 0:
                log(f"{day} {h:02d}Z: {fetched} runs fetched")
    return fetched


def consolidate(out_dir: Path, log: Callable[[str], None] = print) -> dict[str, int]:
    """Gather ``runs/*.parquet`` into ``<ICAO>.parquet`` per station, sorted by initialisation and lead.

    Returns the number of rows written per station.
    """
    out_dir = Path(out_dir)
    files = sorted((out_dir / "runs").glob("*.parquet"))
    frames = [pd.read_parquet(f) for f in files]
    frames = [f for f in frames if len(f)]
    if not frames:
        return {}
    allrows = pd.concat(frames, ignore_index=True)
    counts = {}
    for icao, grp in allrows.groupby("icao", sort=True):
        g = grp.sort_values(["init_utc", "lead_h"]).reset_index(drop=True)
        g.to_parquet(out_dir / f"{icao}.parquet", index=False)
        counts[icao] = len(g)
    log(f"consolidated {len(files)} run files into {len(counts)} station files")
    return counts


def load_station(out_dir: Path, icao: str):
    """The consolidated rows of one station (``COLUMNS``), or an empty frame."""
    f = Path(out_dir) / f"{icao}.parquet"
    if not f.exists():
        return pd.DataFrame(columns=COLUMNS)
    return pd.read_parquet(f)
