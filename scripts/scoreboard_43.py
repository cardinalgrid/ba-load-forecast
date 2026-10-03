"""Scoreboard of the recipe against each BA's own day-ahead forecast (``DF`` of Form EIA-930) on the 43 BAs.

    python scripts/scoreboard_43.py --results results/b4_2023_2025 --doc docs/scoreboard_43_bas.md

Reads the daily rows of the 43-BA evaluation (``rows.parquet`` of ``run_phase_e.py --groups b4``) and, on the days
both the recipe and ``DF`` scored, gives per BA the mean daily MAPE, the peak under-forecast, the coverage and the
Winkler score of the 90 % band, and the Diebold-Mariano test of the daily MAPE against ``DF``. Five BAs publish a
forecast that the EIA lists as not comparable with their demand (``NOT_COMPARABLE``): they stay in the evaluation
of the forecaster, their rows carry the caveat, and they are left out of the aggregates against ``DF``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ba_load_forecast.report import dm_test  # noqa: E402

# EIA-930, Hourly Electric Grid Monitor, "About the data": BAs whose day-ahead demand forecast is reported on a basis
# that differs from their demand (a subset of their system or a different definition), so that forecast and demand
# are not comparable. Kept in the forecaster's evaluation; out of the scoreboard against DF.
NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")


def common_days(rows: pd.DataFrame, model: str, ref: str = "DF") -> pd.DataFrame:
    ok = rows[(~rows["skipped"].astype(bool)) & rows["mape"].notna()]
    a = ok[ok["model"] == model].set_index(["ba", "day"])
    b = ok[ok["model"] == ref].set_index(["ba", "day"])
    idx = a.index.intersection(b.index)
    return a.loc[idx], b.loc[idx]


def per_ba(rows: pd.DataFrame, model: str, ref: str = "DF") -> pd.DataFrame:
    a, b = common_days(rows, model, ref)
    out = []
    for ba in sorted(a.index.get_level_values("ba").unique()):
        x, y = a.loc[ba], b.loc[ba]
        stat, p = dm_test(x["mape"].to_numpy(), y["mape"].to_numpy())
        out.append({
            "ba": ba, "set": "development" if ba in DEV_BAS else "new",
            "comparable": ba not in NOT_COMPARABLE, "days": len(x), "demand_mw": float(x["actual_mean"].mean()),
            "mape": float(x["mape"].mean()), "mape_df": float(y["mape"].mean()),
            "peak_under": float(x["peak_under_pct"].mean()), "peak_under_df": float(y["peak_under_pct"].mean()),
            "coverage_90": float(x["coverage_90"].mean()), "winkler_90": float(x["winkler_90"].mean()),
            "dm_stat": stat, "dm_p": p,
        })
    t = pd.DataFrame(out)
    t["gap"] = t["mape"] - t["mape_df"]
    return t


def aggregates(t: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for name, sub in [("all {n} BAs, forecaster only", t), ("{n} comparable BAs", t[t["comparable"]]),
                      ("{n} development BAs", t[t["set"] == "development"]),
                      ("{n} new comparable BAs", t[(t["set"] == "new") & t["comparable"]])]:
        if sub.empty:
            continue
        w = sub["demand_mw"] / sub["demand_mw"].sum()
        rows.append({
            "set": name.format(n=len(sub)), "bas": len(sub),
            "mape_weighted": float((sub["mape"] * w).sum()), "mape_df_weighted": float((sub["mape_df"] * w).sum()),
            "mape_median": float(sub["mape"].median()), "mape_df_median": float(sub["mape_df"].median()),
            "better": int((sub["gap"] < 0).sum()), "worse": int((sub["gap"] > 0).sum()),
            "better_p05": int(((sub["gap"] < 0) & (sub["dm_p"] < 0.05)).sum()),
            "worse_p05": int(((sub["gap"] > 0) & (sub["dm_p"] < 0.05)).sum()),
            "coverage_90": float((sub["coverage_90"] * w).sum()),
        })
    return pd.DataFrame(rows)


def figure(t: pd.DataFrame, out: Path) -> None:
    import matplotlib
    import matplotlib.ticker

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    s = t.sort_values("mape_df", ascending=True).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(3.5, 0.16 * len(s) + 0.8))
    y = np.arange(len(s))
    for i, r in s.iterrows():
        ax.plot([r["mape_df"], r["mape"]], [i, i], color="0.75", lw=0.8, zorder=1)
    comp = s["comparable"].to_numpy()
    ax.scatter(s["mape_df"][comp], y[comp], s=9, color="0.35", zorder=2, label="the BA's forecast (DF)")
    ax.scatter(s["mape_df"][~comp], y[~comp], s=9, facecolors="none", edgecolors="0.35", zorder=2, label="DF, not comparable")
    ax.scatter(s["mape"], y, s=9, color="C3", zorder=3, label="the recipe")
    ax.set_yticks(y)
    ax.set_yticklabels(s["ba"], fontsize=5.5)
    ax.set_ylim(-0.7, len(s) - 0.3)
    ax.set_xscale("log")
    ticks = [v for v in (1, 2, 3, 5, 10, 20, 30) if v <= 1.5 * max(s["mape"].max(), s["mape_df"].max())]
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(v) for v in ticks])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xlabel("mean daily MAPE, 2023 to 2025 (%)", fontsize=8)
    ax.tick_params(axis="x", labelsize=7)
    ax.grid(axis="x", lw=0.3, alpha=0.5)
    ax.legend(frameon=False, fontsize=6, loc="lower right")
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(out.with_suffix(f".{ext}"), dpi=200)
    plt.close(fig)


def md_table(t: pd.DataFrame, cols: list[tuple[str, str, str]]) -> str:
    head = "| " + " | ".join(h for _, h, _ in cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    lines = [head, sep]
    for _, r in t.iterrows():
        cells = []
        for key, _, fmt in cols:
            v = r[key]
            cells.append(fmt.format(v) if fmt else str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_doc(t: pd.DataFrame, agg: pd.DataFrame, doc: Path, model: str, fig_rel: str) -> None:
    t = t.copy()
    t["ba_label"] = t["ba"] + np.where(t["comparable"], "", " (a)")
    t["dm"] = t.apply(lambda r: f"{r['dm_stat']:.1f}" + ("*" if r["dm_p"] < 0.05 else ""), axis=1)
    per = md_table(t.sort_values("gap"), [
        ("ba_label", "BA", ""), ("set", "set", ""), ("demand_mw", "mean MW", "{:.0f}"), ("days", "days", "{}"),
        ("mape", "MAPE recipe", "{:.2f}"), ("mape_df", "MAPE DF", "{:.2f}"), ("gap", "gap", "{:+.2f}"), ("dm", "DM", ""),
        ("peak_under", "peak under recipe", "{:.2f}"), ("peak_under_df", "peak under DF", "{:.2f}"),
        ("coverage_90", "coverage 90", "{:.3f}"), ("winkler_90", "Winkler 90", "{:.2f}")])
    ag = md_table(agg, [
        ("set", "set", ""), ("bas", "BAs", "{}"), ("mape_weighted", "MAPE recipe, weighted", "{:.2f}"),
        ("mape_df_weighted", "MAPE DF, weighted", "{:.2f}"), ("mape_median", "MAPE recipe, median", "{:.2f}"),
        ("mape_df_median", "MAPE DF, median", "{:.2f}"), ("better", "BAs better", "{}"), ("worse", "BAs worse", "{}"),
        ("better_p05", "better, p < 0.05", "{}"), ("worse_p05", "worse, p < 0.05", "{}"), ("coverage_90", "coverage 90", "{:.3f}")])
    text = f"""# The recipe against each BA's own forecast on the 43 BAs, 2023 to 2025

Daily rows of the 43-BA evaluation (`run_phase_e.py --groups b4`, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, protocol v2),
on the days both `{model}` and `DF` scored. MAPE is the mean of the daily MAPE in percent of the actual; peak under-forecast
in percent of the actual peak (negative is under); coverage and Winkler score of the 90 % band of `{model}`. DM is the
Diebold-Mariano statistic of the daily MAPE of `{model}` against `DF` (negative: the recipe's errors are smaller; `*` for
p < 0.05, two-sided, normal approximation). Gap is MAPE of the recipe minus MAPE of `DF`; negative is better.

(a) The EIA lists the day-ahead forecast of these BAs as not comparable with their demand (a different basis or a subset of
the system): AVA, FPC, LGEE, PSEI, TEPC. They stay in the evaluation of the forecaster and are left out of the aggregates
against `DF`.

## Aggregates

Weighted means use each BA's mean demand on the days scored as the weight.

{ag}

## By BA, sorted by the gap

{per}

![The recipe against each BA's forecast]({fig_rel})
"""
    doc.parent.mkdir(parents=True, exist_ok=True)
    doc.write_text(text, encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "b4_2023_2025")
    ap.add_argument("--model", default="final10s")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "scoreboard_43_bas.md")
    ap.add_argument("--fig", type=Path, default=ROOT / "docs" / "figures" / "scoreboard_43_bas")
    a = ap.parse_args(argv)
    rows = pd.read_parquet(a.results / "rows.parquet")
    t = per_ba(rows, a.model)
    agg = aggregates(t)
    t.to_csv(a.results / "scoreboard.csv", index=False, float_format="%.4f")
    agg.to_csv(a.results / "scoreboard_aggregates.csv", index=False, float_format="%.4f")
    figure(t, a.fig)
    try:
        fig_rel = a.fig.with_suffix(".png").relative_to(a.doc.parent).as_posix()
    except ValueError:
        fig_rel = a.fig.with_suffix(".png").as_posix()
    write_doc(t, agg, a.doc, a.model, fig_rel)
    print(agg.to_string(index=False))
    print("wrote", a.doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
