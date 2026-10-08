"""Peak error on the named winter events, the recipe against each BA's own forecast, one point per BA and event.

    python scripts/figure_events.py --runs <folder with n4_b43_<BA>.parquet> --out docs/figures/events_peak

From the rows of the 43-BA run (group ``n4_b43`` or ``b4``), the event windows of ``grid_sentinel.events`` that fall in
the run, and the 38 BAs whose ``DF`` the EIA treats as comparable: for each BA and event, the mean signed error at the
hour of the actual daily peak (percent of the peak) over the event days both scored, for ``final10s`` and ``DF``.
Points below the diagonal are BA-events where the recipe under-forecasts the peak more than the BA's forecast.
Writes ``<out>.csv`` and a figure (3.5 in, PDF and PNG).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
import pandas as pd
from grid_sentinel.events import EVENTS

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
LABELS = {"uri": "Uri (Feb 2021)", "elliott": "Elliott (Dec 2022)", "gerri_heather": "Gerri and Heather (Jan 2024)",
          "january_2025": "cold wave of Jan 2025"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, required=True)
    ap.add_argument("--group", default="n4_b43")
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "docs" / "figures" / "events_peak")
    a = ap.parse_args(argv)
    rows = []
    for f in sorted(a.runs.glob(f"{a.group}_*.parquet")):
        if f.name.endswith("_hourly.parquet"):
            continue
        d = pd.read_parquet(f)
        d = d[~d["skipped"].astype(bool) & d["error"].isna() & d["model"].isin(["final10s", "DF"])]
        if d.empty or d["ba"].iloc[0] in NOT_COMPARABLE:
            continue
        d["day"] = pd.to_datetime(d["day"])
        for ev in EVENTS:
            w = d[(d["day"] >= pd.Timestamp(ev["start"])) & (d["day"] <= pd.Timestamp(ev["end"]))]
            p = w.pivot_table(index="day", columns="model", values="peak_err_pct").dropna()
            if len(p) and {"final10s", "DF"} <= set(p.columns):
                rows.append({"ba": d["ba"].iloc[0], "event": ev["name"], "days": len(p),
                             "recipe": p["final10s"].mean(), "df": p["DF"].mean()})
    t = pd.DataFrame(rows)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    t.to_csv(a.out.with_suffix(".csv"), index=False)
    for ev, g in t.groupby("event"):
        print(f"{ev}: {len(g)} BAs, recipe {g['recipe'].mean():.2f}, DF {g['df'].mean():.2f}, "
              f"recipe lower at the peak in {(g['recipe'] < g['df']).sum()}")
    fig, ax = plt.subplots(figsize=(3.5, 3.3))
    lim = [min(t["recipe"].min(), t["df"].min()) - 1, max(t["recipe"].max(), t["df"].max()) + 1]
    ax.plot(lim, lim, color="0.6", lw=0.8, ls="--")
    ax.axhline(0, color="0.85", lw=0.6)
    ax.axvline(0, color="0.85", lw=0.6)
    markers = {0: ("o", "C0"), 1: ("s", "C1"), 2: ("^", "C2"), 3: ("D", "C3")}
    for i, (ev, g) in enumerate(t.groupby("event", sort=False)):
        m, c = markers[i % 4]
        ax.scatter(g["df"], g["recipe"], s=12, marker=m, color=c, label=LABELS.get(ev, ev), lw=0)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_xlabel("BA's own forecast: error at the peak (%)", fontsize=8)
    ax.set_ylabel("recipe: error at the peak (%)", fontsize=8)
    ax.tick_params(labelsize=7)
    ax.legend(frameon=False, fontsize=6.5, loc="upper left")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(a.out.with_suffix(f".{ext}"), dpi=200)
    print("wrote", a.out.with_suffix(".pdf"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
