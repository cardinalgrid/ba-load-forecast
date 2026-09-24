"""Forecast surface short-wave radiation (DSWRF) from the HRRR GRIB2 archive, at the stations of a table.

    python scripts/extract_dswrf.py --start 2020-12-02 --end 2022-12-31 --stations data\\cloud\\stations.csv --out data\\dswrf
    python scripts/extract_dswrf.py --consolidate --out data\\dswrf

Only the leads a 9 a.m. cut-off uses (17 to 45 h) and, by default, the 12Z and 06Z runs. Resumable; the
consolidation step writes one file per station, readable by ``hrrr.load_station``.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.hrrr import consolidate
from ba_load_forecast.hrrr_grib import extract
from ba_load_forecast.hrrr_grid import points_from_table
from ba_load_forecast.paths import DATA

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--init-hours", type=int, nargs="+", default=[12, 6])
    ap.add_argument("--stations", type=Path, default=DATA / "cloud" / "stations.csv")
    ap.add_argument("--out", type=Path, default=DATA / "dswrf")
    ap.add_argument("--consolidate", action="store_true")
    a = ap.parse_args(argv)
    if a.consolidate:
        counts = consolidate(a.out, log)
        log(f"rows per station: min {min(counts.values())}, max {max(counts.values())}" if counts else "nothing to consolidate")
        return 0
    points = points_from_table(pd.read_csv(a.stations))
    log(f"{len(points)} stations, {a.start} to {a.end}, runs {a.init_hours}")
    n = extract(points, a.start, a.end, a.out, tuple(a.init_hours), log=log)
    log(f"done: {n} runs fetched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
