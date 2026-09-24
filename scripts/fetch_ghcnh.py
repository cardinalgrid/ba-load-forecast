"""Download the GHCNh temperature of every station used here for the years the ISD archive does not cover.

    python scripts/fetch_ghcnh.py [--years 2025] [--out data/ghcnh] [--stations KPHL KORD] [--skip-existing]

One CSV per station (``<ICAO>.csv``, ``valid_utc,temp_f``), the same format as ``scripts/fetch_asos.py``; the
loader fills the hours the ISD series lacks from whichever folder it is given. The station list is cached next
to the files (``ghcnh-station-list.csv``). About 12 MB is downloaded per station-year and reduced to ~100 kB.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from grid_sentinel.stations import BA_STATION

from ba_load_forecast.ghcnh import fetch_ghcnh, station_ids
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
    ap.add_argument("--years", type=int, nargs="+", default=[2025])
    ap.add_argument("--out", type=Path, default=DATA / "ghcnh")
    ap.add_argument("--stations", nargs="*", default=None)
    ap.add_argument("--skip-existing", action="store_true")
    a = ap.parse_args(argv)
    stations = a.stations or all_stations()
    ids = station_ids(stations, a.out / "ghcnh-station-list.csv")
    missing = [s for s in stations if s not in ids]
    if missing:
        log(f"not in the GHCNh station list: {missing}")
    for year in a.years:
        out = a.out if len(a.years) == 1 else a.out / str(year)
        for icao in stations:
            if icao not in ids:
                continue
            if a.skip_existing and (out / f"{icao}.csv").exists():
                continue
            p = fetch_ghcnh(icao, ids[icao], year, out)
            if p is None:
                log(f"{icao} {year}: no file at NOAA")
                continue
            n = sum(1 for _ in open(p, encoding="utf-8")) - 1
            log(f"{icao} {year}: {n} reports ({ids[icao]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
