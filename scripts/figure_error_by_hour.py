"""Error by hour of the day of the recipe, its ensemble before the correction and the BAs' own forecasts, 43 BAs.

    python scripts/figure_error_by_hour.py --runs <folder with n4_b43_<BA>_hourly.parquet and n4_b43_<BA>.parquet>
                                           --out docs/figures/error_by_hour

From the hourly outputs of the 43-BA run (group ``n4_b43`` or ``b4``), on the BA-days on which the recipe and ``DF`` were
both scored, for the 38 BAs whose ``DF`` the EIA treats as comparable with their demand. For each hour of the day (the
BA's local time): the absolute and the signed error in percent of the actual, averaged over the BA's days and then over
the BAs weighted by mean demand. Writes ``<out>.csv`` and a two-panel figure (3.5 in, PDF and PNG).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HOURS = [f"h{i:02d}" for i in range(24)]
NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
MODELS = {"final10s": "recipe", "final10s_ensemble": "ensemble, before the correction", "DF": "BA's own forecast"}


def ba_hours(hourly: Path, rows: Path, group: str) -> pd.DataFrame | None:
    t = pd.read_parquet(hourly)
    t["day"] = t["day"].astype(str)
    ba = t["ba"].iloc[0]
    if ba in NOT_COMPARABLE:
        return None
    r = pd.read_parquet(rows)
    r["day"] = r["day"].astype(str)
    r = r[~r["skipped"].astype(bool) & r["mape"].notna()]
    days = set(r[r["model"] == "final10s"]["day"]) & set(r[r["model"] == "DF"]["day"])
    wide = {m: t[t["model"] == m].set_index("day")[HOURS] for m in ("actual", *MODELS)}
    common = pd.Index(sorted(days))
    for w in wide.values():
        common = common.intersection(w.index)
    a = wide["actual"].loc[common].to_numpy(dtype=float)
    ok = np.isfinite(a).all(axis=1) & (a > 0).all(axis=1)
    out = []
    for m in MODELS:
        f = wide[m].loc[common].to_numpy(dtype=float)
        good = ok & np.isfinite(f).all(axis=1)
        err = (f[good] - a[good]) / a[good] * 100
        for h in range(24):
            out.append({"ba": ba, "model": m, "hour": h, "abs": float(np.abs(err[:, h]).mean()),
                        "signed": float(err[:, h].mean()), "days": int(good.sum()), "demand": float(a[good].mean())})
    return pd.DataFrame(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, required=True)
    ap.add_argument("--group", default="n4_b43")
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "docs" / "figures" / "error_by_hour")
    a = ap.parse_args(argv)
    parts = []
    for hourly in sorted(a.runs.glob(f"{a.group}_*_hourly.parquet")):
        rows = hourly.with_name(hourly.name.replace("_hourly", ""))
        if rows.exists():
            p = ba_hours(hourly, rows, a.group)
            if p is not None:
                parts.append(p)
    t = pd.concat(parts, ignore_index=True)
    g = t.groupby(["model", "hour"]).apply(
        lambda x: pd.Series({"abs": np.average(x["abs"], weights=x["demand"]), "signed": np.average(x["signed"], weights=x["demand"])}),
        include_groups=False).reset_index()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    g.to_csv(a.out.with_suffix(".csv"), index=False)
    print(f"{t['ba'].nunique()} BAs")
    print(g.pivot(index="hour", columns="model", values="abs").round(2).to_string())

    fig, axes = plt.subplots(2, 1, figsize=(3.5, 3.6), sharex=True)
    styles = {"final10s": dict(color="C0", lw=1.3), "final10s_ensemble": dict(color="C0", lw=0.9, ls="--"),
              "DF": dict(color="0.25", lw=1.3)}
    for m, label in MODELS.items():
        s = g[g["model"] == m].sort_values("hour")
        axes[0].plot(s["hour"], s["abs"], label=label, **styles[m])
        axes[1].plot(s["hour"], s["signed"], **styles[m])
    axes[1].axhline(0, color="0.6", lw=0.6)
    axes[0].set_ylabel("absolute error (%)", fontsize=8)
    axes[1].set_ylabel("signed error (%)", fontsize=8)
    axes[1].set_xlabel("hour of the day, local time", fontsize=8)
    axes[1].set_xticks(range(0, 24, 3))
    for ax in axes:
        ax.tick_params(labelsize=7)
    axes[0].legend(frameon=False, fontsize=6.5)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(a.out.with_suffix(f".{ext}"), dpi=200)
    print("wrote", a.out.with_suffix(".pdf"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
