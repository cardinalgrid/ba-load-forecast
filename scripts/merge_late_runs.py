"""Build a separate data root in which the HRRR temperature files also hold later runs (late cut-off study, stage 2).

    python scripts/merge_late_runs.py --base <data root> --late <folder of consolidated late runs> --out <new data root>

The base data root (``BA_LOAD_FORECAST_DATA``) is copied to ``--out`` once (never modified). For every station file of
``--late`` (``<ICAO>.parquet``, written by ``extract_hrrr.py --consolidate`` for the 18 and 00 UTC runs), the rows are
appended to the station's file in the copy, in the folder the Loader reads it from (``hrrr/`` first, then the
sibling ``hrrr_*`` folders in name order, as ``Loader.hrrr`` does), duplicates dropped on (icao, init_utc, lead_h). A run of the forecaster
pointed at the new root with ``BA_LOAD_FORECAST_HRRR_INIT_HOURS="0 18 12 6"`` and a late
``BA_LOAD_FORECAST_CUTOFF_HOUR`` then reads the newest HRRR temperature run available at its cut-off, and every other
input at its usual runs.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import pandas as pd

KEYS = ["icao", "init_utc", "lead_h"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", type=Path, required=True)
    ap.add_argument("--late", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args(argv)
    if a.out.resolve() == a.base.resolve():
        raise SystemExit("--out must differ from --base: the base data root is never modified")
    if not a.out.exists():
        shutil.copytree(a.base, a.out)
        print("copied", a.base, "to", a.out)
    merged = 0
    for f in sorted(a.late.glob("*.parquet")):
        icao = f.stem
        folders = [a.out / "hrrr", *sorted(p for p in a.out.glob("hrrr_*") if p.is_dir())]   # the Loader's order
        target = next((d / f.name for d in folders if (d / f.name).exists()), None)
        if target is None:
            print("no base file for", icao, "- skipped")
            continue
        old = pd.read_parquet(target)
        new = pd.read_parquet(f)
        both = pd.concat([old, new], ignore_index=True).drop_duplicates(subset=KEYS, keep="first")
        both = both.sort_values(["init_utc", "lead_h"]).reset_index(drop=True)
        both.to_parquet(target, index=False)
        merged += 1
        print(f"{icao}: {len(old)} + {len(new)} -> {len(both)} rows in {target.parent.name}/")
    print(merged, "stations merged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
