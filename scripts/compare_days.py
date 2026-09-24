"""Two models from two result groups compared on the BA-days both scored, overall and by season.

    python scripts/compare_days.py --candidate humid:final3_hw --reference phase_g_final:final3
    python scripts/compare_days.py --candidate humid:h_boosting humid:w_boosting --reference phase_g_final:final3_boosting
                                   --runs ~/ba-load-forecast-runs/phase_e --doc docs/phase_h_by_season.md

Reads the per-BA parquet files of each group (``<runs>/<group>_<BA>.parquet``), keeps the days on which every
model asked for and the reference were scored, and writes the demand-weighted MAPE and peak under-forecast per
BA and per season (winter December to February, summer June to September, the rest), with the gap to the
reference and the count of BAs better and worse. A group name may be given as ``group@folder`` when its files
live in another folder.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from ba_load_forecast.report import markdown_table

ROOT = Path(__file__).resolve().parents[1]
BAS = ["PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL"]
SEASONS = {"winter": (12, 1, 2), "summer": (6, 7, 8, 9)}


def season_of(day) -> str:
    m = pd.Timestamp(day).month
    for name, months in SEASONS.items():
        if m in months:
            return name
    return "shoulder"


def load_model(runs: Path, spec: str, ba: str) -> pd.DataFrame | None:
    """``group:model`` (or ``group@folder:model``) -> the scored rows of that model for the BA, indexed by day."""
    group, model = spec.rsplit(":", 1)
    folder = runs
    if "@" in group:
        group, sub = group.split("@")
        folder = Path(sub).expanduser()
    f = folder / f"{group}_{ba}.parquet"
    if not f.exists():
        return None
    d = pd.read_parquet(f)
    d = d[(d["model"] == model) & ~d["skipped"].astype(bool) & d["error"].isna()]
    return d.set_index("day")[["mape", "peak_under_pct", "actual_mean"]]


def compare(runs: Path, candidates: list[str], reference: str, bas: list[str]) -> pd.DataFrame:
    rows = []
    for ba in bas:
        ref = load_model(runs, reference, ba)
        cands = {c: load_model(runs, c, ba) for c in candidates}
        if ref is None or any(v is None for v in cands.values()):
            continue
        common = ref.index
        for v in cands.values():
            common = common.intersection(v.index)
        if len(common) == 0:
            continue
        seasons = pd.Series([season_of(d) for d in common], index=common)
        for season in ["all", "winter", "summer", "shoulder"]:
            days = common if season == "all" else common[seasons.to_numpy() == season]
            if len(days) == 0:
                continue
            row = {"ba": ba, "season": season, "days": len(days), "demand_mw": float(ref.loc[days, "actual_mean"].mean()),
                   "ref_mape": float(ref.loc[days, "mape"].mean()), "ref_peak_under": float(ref.loc[days, "peak_under_pct"].mean())}
            for c, v in cands.items():
                name = c.rsplit(":", 1)[1]
                row[f"{name}_mape"] = float(v.loc[days, "mape"].mean())
                row[f"{name}_peak_under"] = float(v.loc[days, "peak_under_pct"].mean())
            rows.append(row)
    return pd.DataFrame(rows)


def summary(t: pd.DataFrame, candidates: list[str]) -> pd.DataFrame:
    out = []
    for season, g in t.groupby("season", sort=False):
        w = g["demand_mw"].to_numpy()
        row = {"season": season, "bas": len(g), "days": int(g["days"].sum()), "ref_mape": float(np.average(g["ref_mape"], weights=w))}
        for c in candidates:
            name = c.rsplit(":", 1)[1]
            gap = g[f"{name}_mape"] - g["ref_mape"]
            row[f"{name}_mape"] = float(np.average(g[f"{name}_mape"], weights=w))
            row[f"{name}_gap"] = float(np.average(gap, weights=w))
            row[f"{name}_better"] = int((gap < -0.005).sum())
            row[f"{name}_worse"] = int((gap > 0.005).sum())
            row[f"{name}_peak_gap"] = float(np.average(g[f"{name}_peak_under"] - g["ref_peak_under"], weights=w))
        out.append(row)
    order = {"all": 0, "winter": 1, "summer": 2, "shoulder": 3}
    return pd.DataFrame(out).sort_values("season", key=lambda s: s.map(order)).set_index("season")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--candidate", nargs="+", required=True, help="group:model, one or more")
    ap.add_argument("--reference", required=True, help="group:model")
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--bas", nargs="+", default=BAS)
    ap.add_argument("--doc", type=Path, default=None)
    a = ap.parse_args(argv)
    t = compare(a.runs, a.candidate, a.reference, a.bas)
    if t.empty:
        print("no BA has both the candidates and the reference")
        return 1
    s = summary(t, a.candidate)
    lines = [f"# {', '.join(a.candidate)} against {a.reference}, on the days both scored", "",
             "Demand-weighted mean of the per-BA MAPE (percent) and of the peak under-forecast (percent of the actual peak); "
             "gap < 0 is better than the reference; winter is December to February, summer June to September.", "",
             "## Summary", "", markdown_table(s, 3), "", "## By BA and season", "",
             markdown_table(t.set_index(["ba", "season"]), 3), ""]
    text = "\n".join(lines)
    print("\n".join(lines[:7]))
    if a.doc:
        a.doc.write_text(text, encoding="utf-8")
        print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
