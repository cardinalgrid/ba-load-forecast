"""Download the NOAA ISD-Lite files of every station in the multi-station table, 2015 to 2025.

    python scripts/fetch_isd.py [--isd-dir DIR] [--years 2015 2025]

Files that already exist are skipped; the whole list is retried until every file is there (or reported
absent by NOAA), so a flaky network only delays the run.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from grid_sentinel.weather import fetch_isd_lite

from ba_load_forecast.stations_multi import all_icaos, station_table_for

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--isd-dir", type=Path, default=ROOT.parent / "notes" / "03-daily-load-profiles" / "data" / "isd")
    ap.add_argument("--years", type=int, nargs=2, default=[2015, 2025])
    ap.add_argument("--rounds", type=int, default=30)
    a = ap.parse_args(argv)
    table = station_table_for(all_icaos(), a.isd_dir)
    years = range(a.years[0], a.years[1] + 1)
    absent: set[tuple[str, int]] = set()
    for round_ in range(1, a.rounds + 1):
        missing = [(r.icao, r.usaf, r.wban, y) for r in table.itertuples() for y in years
                   if not (a.isd_dir / f"{r.usaf}-{r.wban}-{y}.gz").exists() and (r.icao, y) not in absent]
        if not missing:
            log(f"all files present; {len(absent)} reported absent by NOAA: {sorted(absent)}")
            return 0
        log(f"round {round_}: {len(missing)} files to fetch")
        for icao, usaf, wban, y in missing:
            try:
                p = fetch_isd_lite(usaf, wban, y, a.isd_dir)
            except Exception as e:  # noqa: BLE001
                log(f"{icao} {y}: {type(e).__name__}: {str(e)[:100]}")
                continue
            if p is None:
                absent.add((icao, y))
                log(f"{icao} {y}: not on the NOAA server")
        time.sleep(30)
    log("gave up with files still missing")
    return 1


if __name__ == "__main__":
    sys.exit(main())
