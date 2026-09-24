"""Download the ASOS/METAR temperature archive of the Iowa Environmental Mesonet for every station used here,
for the period the NOAA ISD archive does not cover (from 27 August 2025).

    python scripts/fetch_asos.py [--start 2025-08-01] [--end 2026-01-01] [--out data/asos] [--stations KPHL KORD]

One CSV per station (``<ICAO>.csv``, ``valid_utc,temp_f``), from a single request for all stations (the service
limits the request rate; a refusal is retried after a pause). Stations: the multi-station table of ``stations_multi`` and the
single station of every BA in ``grid_sentinel.stations``.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

from grid_sentinel.stations import BA_STATION

from ba_load_forecast.asos import fetch_asos
from ba_load_forecast.paths import DATA
from ba_load_forecast.stations_multi import BA_STATIONS_MULTI

ROOT = Path(__file__).resolve().parents[1]


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def all_stations() -> list[str]:
    multi = {i for v in BA_STATIONS_MULTI.values() for i in v}
    return sorted(multi | set(BA_STATION.values()))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", type=date.fromisoformat, default=date(2025, 8, 1))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2026, 1, 1))
    ap.add_argument("--out", type=Path, default=DATA / "asos")
    ap.add_argument("--stations", nargs="*", default=None)
    ap.add_argument("--skip-existing", action="store_true")
    a = ap.parse_args(argv)
    stations = a.stations or all_stations()
    if a.skip_existing:
        stations = [i for i in stations if not (a.out / f"{i}.csv").exists()]
    if not stations:
        return 0
    written = fetch_asos(stations, a.start, a.end, a.out)
    for icao in stations:
        if icao in written:
            n = sum(1 for _ in open(written[icao], encoding="utf-8")) - 1
            log(f"{icao}: {n} observations")
        else:
            log(f"{icao}: nothing returned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
