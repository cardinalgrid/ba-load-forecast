"""Calibration of the issued quantiles, by stratum: the share of hours whose actual load fell at or below each quantile.

    python scripts/calibration_curve.py --models frozen8@<runs>:final8q frozen10@<runs>:final10a2t --doc docs/calibration_curves.md

A well-calibrated quantile at level q holds the actual load q of the time. For every model (``group@folder:model``,
as in ``compare_events.py``) the hourly table of the run holds the 23 issued quantiles next to the actual load; this
script reads them on the BA-days every model scored, pools the hours of each stratum (year, winter, summer, shoulder,
the event days, the 30 coldest mornings and the 30 largest peaks of each BA) and reports, per stratum and level, the
empirical frequency, the mean absolute calibration error over the levels, and one figure per stratum (nominal on the
x axis, empirical on the y axis, one line per model).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compare_days import BAS
from compare_events import STRATA, load_model, strata_masks

from ba_load_forecast.report import markdown_table

ROOT = Path(__file__).resolve().parents[1]
HOURS = [f"h{h:02d}" for h in range(24)]


def hourly_table(runs: Path, spec: str, ba: str) -> pd.DataFrame | None:
    group, model = spec.rsplit(":", 1)
    folder = runs
    if "@" in group:
        group, sub = group.split("@")
        folder = Path(sub).expanduser()
    f = folder / f"{group}_{ba}_hourly.parquet"
    if not f.exists():
        return None
    d = pd.read_parquet(f)
    keep = d["model"].eq("actual") | d["model"].eq(model) | d["model"].str.startswith(f"{model}_q")
    return d[keep]


def levels_of(table: pd.DataFrame, model: str) -> dict[str, float]:
    """``model name -> nominal level`` for the quantile rows (the point itself is the median)."""
    out = {model: 0.5}
    for name in table["model"].unique():
        if name.startswith(f"{model}_q") and name[len(model) + 2:].isdigit():
            out[name] = int(name[len(model) + 2:]) / 100.0
    return dict(sorted(out.items(), key=lambda kv: kv[1]))


def empirical(table: pd.DataFrame, days: pd.Index, levels: dict[str, float]) -> pd.Series:
    """Share of the hours of ``days`` whose actual load is at or below each quantile."""
    sub = table[table["day"].isin(days)]
    actual = sub[sub["model"] == "actual"].set_index("day")[HOURS]
    out = {}
    for name, q in levels.items():
        pred = sub[sub["model"] == name].set_index("day")[HOURS].reindex(actual.index)
        a, p = actual.to_numpy(dtype=float), pred.to_numpy(dtype=float)
        ok = np.isfinite(a) & np.isfinite(p) & (a > 0)
        out[q] = float((a[ok] <= p[ok]).mean()) if ok.sum() else np.nan
    return pd.Series(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", required=True, help="group[@folder]:model, one or more")
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--bas", nargs="+", default=BAS)
    ap.add_argument("--cold", type=int, default=30)
    ap.add_argument("--peaks", type=int, default=30)
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "calibration")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "calibration_curves.md")
    ap.add_argument("--tag", default="calibration", help="file name stem of the figures")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    figures = a.doc.parent / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    names = [m.rsplit(":", 1)[1] for m in a.models]
    pooled: dict[tuple[str, str], list[tuple[pd.Series, int]]] = {}       # (stratum, model) -> [(curve, n_hours)]
    used = []
    for ba in a.bas:
        daily = {m: load_model(a.runs, m, ba) for m in a.models}
        hourly = {m: hourly_table(a.runs, m, ba) for m in a.models}
        if any(v is None for v in daily.values()) or any(v is None for v in hourly.values()):
            continue
        common = None
        for v in daily.values():
            common = v.index if common is None else common.intersection(v.index)
        if common is None or len(common) == 0:
            continue
        used.append(ba)
        masks = strata_masks(common, daily[a.models[0]], a.cold, a.peaks)
        for stratum in STRATA:
            days = common[masks[stratum]]
            if len(days) == 0:
                continue
            for m, name in zip(a.models, names, strict=True):
                lv = levels_of(hourly[m], name)
                pooled.setdefault((stratum, name), []).append((empirical(hourly[m], days, lv), 24 * len(days)))

    rows = []
    for (stratum, name), parts in pooled.items():
        w = np.array([n for _, n in parts], dtype=float)
        curve = sum(c * n for c, n in parts) / w.sum()
        for q, e in curve.items():
            rows.append({"stratum": stratum, "model": name, "nominal": q, "empirical": round(float(e), 4), "hours": int(w.sum())})
    table = pd.DataFrame(rows)
    table.to_csv(a.out / "calibration.csv", index=False)
    summary = (table.assign(abs_err=(table["empirical"] - table["nominal"]).abs())
               .groupby(["stratum", "model"], sort=False)
               .agg(levels=("nominal", "size"), hours=("hours", "first"), mean_abs_calibration_error=("abs_err", "mean"),
                    worst_level_error=("abs_err", "max"))
               .reset_index())
    summary["mean_abs_calibration_error"] = summary["mean_abs_calibration_error"].round(4)
    summary["worst_level_error"] = summary["worst_level_error"].round(4)
    summary.to_csv(a.out / "calibration_summary.csv", index=False)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    for stratum in STRATA:
        sub = table[table["stratum"] == stratum]
        if sub.empty:
            continue
        fig, ax = plt.subplots(figsize=(3.5, 3.0))
        ax.plot([0, 1], [0, 1], color="0.6", lw=0.8, ls="--")
        for name in names:
            s = sub[sub["model"] == name].sort_values("nominal")
            ax.plot(s["nominal"], s["empirical"], marker="o", ms=2.5, lw=1.0, label=name)
        ax.set_xlabel("nominal level")
        ax.set_ylabel("share of hours at or below the quantile")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.tick_params(labelsize=8)
        ax.legend(fontsize=7, frameon=False)
        fig.tight_layout()
        for ext in ("pdf", "png"):
            fig.savefig(figures / f"{a.tag}_{stratum}.{ext}", dpi=200)
        plt.close(fig)

    lines = ["# Calibration of the issued quantiles, by stratum", "",
             f"Models: {', '.join(a.models)}. BAs: {', '.join(used)}; the days every model scored, pooled over the BAs "
             f"(hours weighted equally). A quantile at nominal level q is calibrated when the actual load falls at or below it a "
             f"share q of the hours; the mean absolute calibration error averages |empirical - nominal| over the issued levels.", "",
             "## Summary", "", markdown_table(summary), ""]
    for stratum in STRATA:
        sub = table[table["stratum"] == stratum]
        if sub.empty:
            continue
        wide = sub.pivot(index="nominal", columns="model", values="empirical")[names].reset_index()   # in the order given
        lines += [f"## {stratum}", "", f"![{stratum}](figures/{a.tag}_{stratum}.png)", "", markdown_table(wide), ""]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print("written", a.doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
