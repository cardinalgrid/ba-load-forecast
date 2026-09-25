"""Candidate recipes against a reference on the days all scored, with the strata that matter for extreme events.

    python scripts/compare_events.py --candidate events:final4r events:final4w events:final4p --reference events:final4
                                     --doc docs/phase_i_events_strata.md

Beyond the year and the three seasons of ``compare_days.py``, the comparison is made on the winter-event days
(the event windows of ``grid_sentinel.events``), on the coldest mornings of each BA (the ``--cold`` days with the
lowest observed minimum temperature) and on the days of largest actual peak of each BA (``--peaks``). For each
stratum and model: demand-weighted MAPE, peak under-forecast, CRPS, Winkler score and coverage of the 90 %
band, plus the gap to the reference and the count of BAs better and worse. Gap < 0 is better.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.events import EVENTS

from ba_load_forecast.report import markdown_table
from compare_days import BAS, season_of

METRICS = ["mape", "peak_under_pct", "peak_err_pct", "crps", "winkler_90", "coverage_90"]
STRATA = ["all", "winter", "summer", "shoulder", "events", "cold_mornings", "top_peaks"]


def load_model(runs: Path, spec: str, ba: str) -> pd.DataFrame | None:
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
    cols = [c for c in METRICS + ["actual_mean", "actual_peak", "temp_min_f"] if c in d.columns]
    return d.set_index("day")[cols]


def strata_masks(days: pd.Index, ref: pd.DataFrame, cold: int, peaks: int) -> dict[str, np.ndarray]:
    day = pd.to_datetime(pd.Index(days))
    seasons = np.array([season_of(d) for d in days])
    in_event = np.zeros(len(days), dtype=bool)
    for ev in EVENTS:
        in_event |= np.asarray((day >= pd.Timestamp(ev["start"])) & (day <= pd.Timestamp(ev["end"])))
    coldest = ref.loc[days].nsmallest(cold, "temp_min_f").index
    top = ref.loc[days].nlargest(peaks, "actual_peak").index
    return {"all": np.ones(len(days), dtype=bool), "winter": seasons == "winter", "summer": seasons == "summer",
            "shoulder": seasons == "shoulder", "events": in_event, "cold_mornings": pd.Index(days).isin(coldest),
            "top_peaks": pd.Index(days).isin(top)}


def compare(runs: Path, candidates: list[str], reference: str, bas: list[str], cold: int, peaks: int) -> pd.DataFrame:
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
        masks = strata_masks(common, ref, cold, peaks)
        for stratum in STRATA:
            days = common[masks[stratum]]
            if len(days) == 0:
                continue
            row = {"ba": ba, "stratum": stratum, "days": len(days), "demand_mw": float(ref.loc[days, "actual_mean"].mean())}
            for name, frame in [("ref", ref)] + [(c.rsplit(":", 1)[1], v) for c, v in cands.items()]:
                for m in METRICS:
                    row[f"{name}_{m}"] = float(frame.loc[days, m].mean()) if m in frame.columns else np.nan
            rows.append(row)
    return pd.DataFrame(rows)


def summary(t: pd.DataFrame, candidates: list[str]) -> pd.DataFrame:
    out = []
    names = [c.rsplit(":", 1)[1] for c in candidates]
    for stratum in STRATA:
        g = t[t["stratum"] == stratum]
        if g.empty:
            continue
        w = g["demand_mw"].to_numpy()
        for name in ["ref"] + names:
            row = {"stratum": stratum, "model": name, "bas": len(g), "days": int(g["days"].sum())}
            for m in METRICS:
                col = g[f"{name}_{m}"]
                row[m] = float(np.average(col, weights=w)) if col.notna().all() else np.nan
                if name != "ref":
                    gap = col - g[f"ref_{m}"]
                    row[f"{m}_gap"] = float(np.average(gap, weights=w)) if gap.notna().all() else np.nan
                    if m in ("mape", "crps"):
                        row[f"{m}_better"] = int((gap < -0.005).sum())
                        row[f"{m}_worse"] = int((gap > 0.005).sum())
            out.append(row)
    s = pd.DataFrame(out).set_index(["stratum", "model"])
    for c in [c for c in s.columns if c.endswith("_better") or c.endswith("_worse")]:
        s[c] = s[c].map(lambda v: "" if pd.isna(v) else str(int(v)))                # counts, blank on the reference rows
    return s


def per_event(runs: Path, candidates: list[str], reference: str, bas: list[str]) -> pd.DataFrame:
    """Each event separately: MAPE and peak under-forecast per model, demand-weighted over the BAs in the window."""
    rows = []
    specs = [("ref", reference)] + [(c.rsplit(":", 1)[1], c) for c in candidates]
    for ev in EVENTS:
        for ba in bas:
            frames = {name: load_model(runs, spec, ba) for name, spec in specs}
            if any(v is None for v in frames.values()):
                continue
            common = None
            for v in frames.values():
                common = v.index if common is None else common.intersection(v.index)
            day = pd.to_datetime(pd.Index(common))
            days = common[np.asarray((day >= pd.Timestamp(ev["start"])) & (day <= pd.Timestamp(ev["end"])))]
            if len(days) == 0:
                continue
            row = {"event": ev["name"], "ba": ba, "days": len(days), "demand_mw": float(frames["ref"].loc[days, "actual_mean"].mean())}
            for name, v in frames.items():
                row[f"{name}_mape"] = float(v.loc[days, "mape"].mean())
                row[f"{name}_peak_under"] = float(v.loc[days, "peak_under_pct"].mean())
                row[f"{name}_worst_peak_under"] = float(v.loc[days, "peak_under_pct"].min())
            rows.append(row)
    t = pd.DataFrame(rows)
    if t.empty:
        return t
    out = []
    for ev, g in t.groupby("event", sort=False):
        w = g["demand_mw"].to_numpy()
        row = {"event": ev, "bas": len(g), "days": int(g["days"].sum())}
        for name, _ in specs:
            row[f"{name}_mape"] = float(np.average(g[f"{name}_mape"], weights=w))
            row[f"{name}_peak_under"] = float(np.average(g[f"{name}_peak_under"], weights=w))
            row[f"{name}_worst"] = float(g[f"{name}_worst_peak_under"].min())
        out.append(row)
    return pd.DataFrame(out).set_index("event")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--candidate", nargs="+", required=True, help="group:model, one or more")
    ap.add_argument("--reference", required=True, help="group:model")
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--bas", nargs="+", default=BAS)
    ap.add_argument("--cold", type=int, default=30, help="coldest mornings per BA")
    ap.add_argument("--peaks", type=int, default=30, help="days of largest actual peak per BA")
    ap.add_argument("--doc", type=Path, default=None)
    a = ap.parse_args(argv)
    t = compare(a.runs, a.candidate, a.reference, a.bas, a.cold, a.peaks)
    if t.empty:
        print("no BA has both the candidates and the reference")
        return 1
    s = summary(t, a.candidate)
    e = per_event(a.runs, a.candidate, a.reference, a.bas)
    lines = [f"# {', '.join(a.candidate)} against {a.reference}, by stratum", "",
             "Demand-weighted means over the BAs on the days every model scored. MAPE, CRPS and Winkler in percent of the "
             "actual; peak under-forecast and peak error in percent of the actual peak; coverage of the 90 % band. "
             f"Strata: the year, winter (December to February), summer (June to September), the rest, the winter-event days, "
             f"the {a.cold} coldest mornings of each BA (observed minimum) and the {a.peaks} days of largest actual peak of "
             "each BA. Gap < 0 is better than the reference.", "",
             "## Summary", "", markdown_table(s, 3), ""]
    if not e.empty:
        lines += ["## Each event (peak under-forecast: mean over the event days, worst single BA-day)", "", markdown_table(e, 2), ""]
    lines += ["## By BA and stratum", "", markdown_table(t.set_index(["ba", "stratum"]), 3), ""]
    text = "\n".join(lines)
    print("\n".join(lines[:7]))
    if a.doc:
        a.doc.write_text(text, encoding="utf-8")
        print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
