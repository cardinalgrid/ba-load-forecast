"""One table across the reports of several groups: every model's demand-weighted MAPE, its gap to a reference
model, and the per-BA gaps, so that a decision on what enters the recipe reads from one place.

    python scripts/compare_groups.py --groups phase_g_features phase_g_parameters --reference final_boosting
    python scripts/compare_groups.py --groups phase_g_ensemble --reference final2 --metric peak_under_pct

Reads ``results/<group>/by_model_ba.csv`` (per model and BA, with ``demand_mw`` and ``n_days``) and writes
``days`` and ``days_ref``, the scored BA-days of the model and of the reference over the same BAs: a model that
scored fewer days than the reference is not compared on the same footing, and the table says so. It also writes
``results/<group>/compare_<reference>.csv`` for each group plus a Markdown block on stdout. Only BAs present for
both the model and the reference count; the weighted mean uses the BA's mean demand as weight.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from ba_load_forecast.report import markdown_table

ROOT = Path(__file__).resolve().parents[1]


def compare(by_ba: pd.DataFrame, reference: str, metric: str) -> pd.DataFrame:
    ref = by_ba[by_ba["model"] == reference].set_index("ba")[[metric, "demand_mw", "n_days"]]
    rows = []
    for model, rows_of in by_ba.groupby("model"):
        g = rows_of.set_index("ba").join(ref, rsuffix="_ref", how="inner")
        if g.empty:
            continue
        w = g["demand_mw"].to_numpy(dtype=float)
        gap = g[metric] - g[f"{metric}_ref"]
        row = {"model": model, "n_bas": len(g), "days": int(g["n_days"].sum()), "days_ref": int(g["n_days_ref"].sum()),
               f"{metric}_weighted": float(np.average(g[metric], weights=w)),
               "gap_weighted": float(np.average(gap, weights=w)), "bas_better": int((gap < -0.005).sum()),
               "bas_worse": int((gap > 0.005).sum())}
        row.update({f"gap_{ba}": float(v) for ba, v in gap.items()})
        rows.append(row)
    if not rows:
        raise ValueError(f"reference model {reference!r} is not in the report")
    return pd.DataFrame(rows).set_index("model").sort_values("gap_weighted")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--groups", nargs="+", required=True, help="result folders under results/")
    ap.add_argument("--reference", required=True)
    ap.add_argument("--metric", default="mape")
    a = ap.parse_args(argv)
    for group in a.groups:
        f = ROOT / "results" / group / "by_model_ba.csv"
        if not f.exists():
            print(f"## {group}: no report yet\n")
            continue
        t = compare(pd.read_csv(f), a.reference, a.metric)
        t.round(3).to_csv(ROOT / "results" / group / f"compare_{a.reference}_{a.metric}.csv")
        summary = t[[c for c in t.columns if not c.startswith("gap_") or c == "gap_weighted"]]
        print(f"## {group}: {a.metric} against `{a.reference}` (demand-weighted; gap < 0 is better)\n")
        print(markdown_table(summary, 3))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
