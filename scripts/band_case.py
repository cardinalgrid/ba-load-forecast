"""Hour-by-hour case of two bands on one BA over a few days, from the hourly outputs of two run groups.

    python scripts/band_case.py --ref frozen8@<folder>:final8q --band frozen10sa@<folder>:final10s \
        --ba SWPP --start 2024-01-13 --end 2024-01-16 --out docs/band_case_SWPP_2024-01-13_2024-01-16.csv

Writes one row per hour: the actual load, the point forecast (the same in both groups when only the band differs),
the 5th and 95th percentiles of each band, and whether the hour fell inside each. Prints the hours covered per day.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

HOURS = [f"h{i:02d}" for i in range(24)]


def parse_spec(spec: str) -> tuple[str, Path, str]:
    """``group@folder:model`` -> (group, folder, model)."""
    group, rest = spec.split("@", 1)
    folder, model = rest.rsplit(":", 1)
    return group, Path(folder), model


def hourly(spec: str, ba: str, start: str, end: str) -> pd.DataFrame:
    group, folder, model = parse_spec(spec)
    t = pd.read_parquet(folder / f"{group}_{ba}_hourly.parquet")
    t = t[(t["day"].astype(str) >= start) & (t["day"].astype(str) <= end)]
    rows = {}
    for day, g in t.groupby("day"):
        x = g.set_index("model")[HOURS]
        for h in HOURS:
            key = (str(day), int(h[1:]))
            rows[key] = {"actual": x.at["actual", h], "point": x.at[model, h],
                         "q05": x.at[f"{model}_q05", h], "q95": x.at[f"{model}_q95", h]}
    out = pd.DataFrame.from_dict(rows, orient="index")
    out.index = pd.MultiIndex.from_tuples(out.index, names=["day", "hour"])
    return out


def case_table(ref: str, band: str, ba: str, start: str, end: str) -> pd.DataFrame:
    a = hourly(ref, ba, start, end)
    b = hourly(band, ba, start, end)
    t = pd.DataFrame({"actual": a["actual"], "point": a["point"],
                      "ref_q05": a["q05"], "ref_q95": a["q95"], "band_q05": b["q05"], "band_q95": b["q95"]})
    t["in_ref"] = (t["actual"] >= t["ref_q05"]) & (t["actual"] <= t["ref_q95"])
    t["in_band"] = (t["actual"] >= t["band_q05"]) & (t["actual"] <= t["band_q95"])
    return t.reset_index()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", required=True, help="group@folder:model of the reference band")
    ap.add_argument("--band", required=True, help="group@folder:model of the band under study")
    ap.add_argument("--ba", required=True)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args(argv)
    t = case_table(a.ref, a.band, a.ba, a.start, a.end)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    t.to_csv(a.out, index=False, float_format="%.1f")
    per_day = t.groupby("day")[["in_ref", "in_band"]].sum()
    print(per_day.to_string())
    print("wrote", a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
