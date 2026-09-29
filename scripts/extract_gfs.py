"""Extract the GFS 0.25 degree 2 m temperature at the stations, one parquet per run (resumable).

    python scripts/extract_gfs.py --start 2021-01-01 --end 2025-12-31 --out <folder>
    python scripts/extract_gfs.py --consolidate --out <folder>

Stations: every row of ``docs/stations_grid.csv`` and ``docs/stations_grid_multi.csv``. Runs: 06 and 12 UTC, with
the leads of a 39-hour path at a 9 a.m. cut-off (8 to 49 h and 2 to 43 h).
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.gfs import extract, station_cells
from ba_load_forecast.hrrr import consolidate
from ba_load_forecast.paths import DATA

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def stations() -> pd.DataFrame:
    frames = [pd.read_csv(ROOT / "docs" / f) for f in ("stations_grid.csv", "stations_grid_multi.csv")]
    return pd.concat(frames, ignore_index=True).drop_duplicates("icao")[["icao", "lat", "lon"]]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", type=date.fromisoformat, default=date(2021, 1, 1))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    ap.add_argument("--out", type=Path, default=DATA / "gfs")
    ap.add_argument("--init-hours", type=int, nargs="+", default=[6, 12])
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--consolidate", action="store_true")
    a = ap.parse_args(argv)
    if a.consolidate:
        counts = consolidate(a.out, log=log)
        log(f"{len(counts)} stations, {sum(counts.values())} rows")
        return 0
    cells = station_cells(stations())
    log(f"{len(cells)} stations; {a.start} to {a.end}, runs {a.init_hours}")
    n = extract(cells, a.start, a.end, a.out, init_hours=tuple(a.init_hours), workers=a.workers, log=log)
    log(f"ALL_DONE {n} runs written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
