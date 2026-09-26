"""Extract the NBM 2 m temperature at the stations from the public archive, one parquet per run (resumable).

    python scripts/extract_nbm.py --start 2020-12-02 --end 2025-12-31 --out <folder>
    python scripts/extract_nbm.py --consolidate --out <folder>

    python scripts/extract_nbm.py --daily --start 2020-12-02 --end 2025-12-31 --out <folder>

Stations: every row of ``docs/stations_grid.csv`` and ``docs/stations_grid_multi.csv`` (the HRRR station tables;
only ``icao, lat, lon`` are used). Runs: 12 and 06 UTC, leads 1 to 45 (hourly to 36 h, then 39, 42 and 45 h).
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.hrrr import consolidate
from ba_load_forecast.nbm import DAILY_ELEMENTS, extract, extract_daily, station_cells
from ba_load_forecast.paths import DATA

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def stations() -> pd.DataFrame:
    frames = [pd.read_csv(ROOT / "docs" / f) for f in ("stations_grid.csv", "stations_grid_multi.csv")]
    return pd.concat(frames, ignore_index=True).drop_duplicates("icao")[["icao", "lat", "lon"]]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    ap.add_argument("--out", type=Path, default=DATA / "nbm")
    ap.add_argument("--init-hours", type=int, nargs="+", default=[12, 6])
    ap.add_argument("--max-lead", type=int, default=45)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--consolidate", action="store_true", help="gather runs/*.parquet into <ICAO>.parquet and stop")
    ap.add_argument("--daily", action="store_true", help="the daily products (18-h min and max percentiles, extreme-temperature "
                    f"probabilities) of the target day instead of the hourly temperature: {', '.join(DAILY_ELEMENTS)}")
    a = ap.parse_args(argv)
    if a.consolidate:
        counts = consolidate(a.out, log=log)
        log(f"{len(counts)} stations, {sum(counts.values())} rows")
        return 0
    cells = station_cells(stations())
    log(f"{len(cells)} stations on the grid; {a.start} to {a.end}, runs {a.init_hours}, leads to {a.max_lead}")
    if a.daily:
        n = extract_daily(cells, a.start, a.end, a.out, init_hours=tuple(a.init_hours), workers=a.workers, log=log)
    else:
        n = extract(cells, a.start, a.end, a.out, init_hours=tuple(a.init_hours), max_lead=a.max_lead, workers=a.workers, log=log)
    log(f"ALL_DONE {n} runs written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
