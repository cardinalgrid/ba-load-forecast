"""Extract 2 m temperature forecasts from the public HRRR archive for the stations of every BA.

Examples::

    python scripts/extract_hrrr.py --start 2020-12-02 --end 2025-12-31 --init-hours 12 6 --out data/hrrr
    python scripts/extract_hrrr.py --consolidate --out data/hrrr

The station table (``docs/stations_grid.csv``) is written on the first call from the NOAA station history
and the HRRR grid index, and reused afterwards.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.hrrr import consolidate, extract
from ba_load_forecast.hrrr_grid import load_grid, points_from_table, station_grid_points

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def station_points(isd_dir: Path, grid_cache: Path, table_csv: Path):
    if table_csv.exists():
        return points_from_table(pd.read_csv(table_csv))
    from grid_sentinel.stations import station_table

    lat, lon = load_grid(grid_cache)
    t = station_grid_points(station_table(isd_dir), lat, lon)
    table_csv.parent.mkdir(parents=True, exist_ok=True)
    t.to_csv(table_csv, index=False, float_format="%.5f")
    log(f"station table written: {len(t)} stations, {t.groupby(['chunk_y', 'chunk_x']).ngroups} chunks, "
        f"max distance {t['distance_km'].max():.2f} km")
    return points_from_table(t)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", type=date.fromisoformat)
    ap.add_argument("--end", type=date.fromisoformat)
    ap.add_argument("--init-hours", type=int, nargs="+", default=[12, 6])
    ap.add_argument("--out", type=Path, default=ROOT / "data" / "hrrr")
    ap.add_argument("--isd-dir", type=Path, default=ROOT.parent / "notes" / "03-daily-load-profiles" / "data" / "isd")
    ap.add_argument("--stations", type=Path, default=ROOT / "docs" / "stations_grid.csv")
    ap.add_argument("--consolidate", action="store_true", help="gather the run files into one parquet per station")
    ap.add_argument("--no-resume", action="store_true")
    ap.add_argument("--field", default="temp_f", choices=["temp_f", "cloud_pct", "dewpoint_f", "wind_ms"],
                    help="what to extract: 2 m temperature (F) or total cloud cover (percent)")
    a = ap.parse_args(argv)

    if a.start and a.end:
        points = station_points(a.isd_dir, a.out / "HRRR_grid.npz", a.stations)
        log(f"extracting {a.start} to {a.end}, runs {a.init_hours}, {len(points)} stations")
        t0 = time.time()
        n = extract(points, a.start, a.end, a.out, tuple(a.init_hours), resume=not a.no_resume, log=log, field=a.field)
        log(f"done: {n} runs fetched in {(time.time() - t0) / 60:.1f} min")
    if a.consolidate:
        counts = consolidate(a.out, log=log)
        log(f"rows per station: min {min(counts.values()) if counts else 0}, max {max(counts.values()) if counts else 0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
