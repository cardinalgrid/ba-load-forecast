"""Where does a model lose to the BA's own forecast? Errors by hour of the day and by month.

    python scripts/diagnose.py --group recipe --model ens_recent_bc

Reads the hourly forecasts stored by the phase E run (``<group>_<BA>_hourly.parquet``: 24 values per BA, day
and model, with ``DF`` and ``actual``) and writes, per BA: the mean absolute percentage error of the model
and of ``DF`` by hour of the day and by month, their difference, the mean signed error by hour and month (a
midday surplus that grows from one year to the next is what behind-the-meter solar looks like), and the
same split by day type and by year. Tables go to ``results/diagnostics/``, figures to ``docs/figures/`` and a
summary to ``docs/diagnostics.md``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
import pandas as pd

from ba_load_forecast.evaluate import ACTUAL, BA_MODEL, HOURS
from ba_load_forecast.report import load_shed_days, markdown_table

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def long_errors(hourly: pd.DataFrame, model: str) -> pd.DataFrame:
    """One row per BA, day and hour with the percentage errors of the model and of DF."""
    def wide(name):
        w = hourly[hourly["model"] == name].set_index(["ba", "day"])[HOURS]
        w.columns = range(24)
        return w.stack(future_stack=True).rename(name)

    d = pd.concat([wide(model), wide(BA_MODEL), wide(ACTUAL)], axis=1).dropna()
    d = d[d[ACTUAL] > 0].reset_index().rename(columns={"level_2": "hour"})
    d["err_model"] = (d[model] - d[ACTUAL]) / d[ACTUAL] * 100.0
    d["err_df"] = (d[BA_MODEL] - d[ACTUAL]) / d[ACTUAL] * 100.0
    d["day"] = pd.to_datetime(d["day"])
    d["month"] = d["day"].dt.month
    d["year"] = d["day"].dt.year
    d["weekend"] = d["day"].dt.weekday >= 5
    return d


def by(d: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    g = d.groupby(keys)
    out = pd.DataFrame({
        "mape_model": g["err_model"].apply(lambda s: s.abs().mean()),
        "mape_df": g["err_df"].apply(lambda s: s.abs().mean()),
        "bias_model": g["err_model"].mean(),
        "bias_df": g["err_df"].mean(),
        "n": g.size(),
    })
    out["mape_gap"] = out["mape_model"] - out["mape_df"]
    return out.round(3)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--group", default="recipe")
    ap.add_argument("--model", default="ens_recent_bc")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "diagnostics")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "diagnostics.md")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    figures = a.doc.parent / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    files = sorted(a.runs.glob(f"{a.group}_*_hourly.parquet"))
    if not files:
        print("no hourly forecasts found")
        return 1
    hourly = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
    shed = load_shed_days()
    if len(shed):
        key = set(zip(shed["ba"], shed["date"], strict=True))
        hourly = hourly[[(b, d) not in key for b, d in zip(hourly["ba"], hourly["day"], strict=True)]]
    d = long_errors(hourly, a.model)

    lines = ["# Where the model loses to the BA's forecast", "",
             f"Hourly percentage errors of `{a.model}` and of the BA's own forecast (`DF`) on the development period, "
             "documented load-shed days left out. `mape_gap` is the model's MAPE minus the BA's: positive where the BA "
             "is better. `bias` is the mean signed error: negative means under-forecast.", ""]
    summary = by(d, ["ba"]).sort_values("mape_gap")
    summary.to_csv(a.out / "by_ba.csv")
    lines += ["## By BA", "", markdown_table(summary, 2), ""]

    bas = list(summary.index)
    fig, axes = plt.subplots(len(bas), 2, figsize=(7.16, 1.35 * len(bas)), sharex="col")
    for i, ba in enumerate(bas):
        sub = d[d["ba"] == ba]
        h = by(sub, ["hour"])
        m = by(sub, ["month"])
        y = by(sub, ["year", "hour"])
        for t, name in ((h, "hour"), (m, "month"), (y, "year_hour"), (by(sub, ["weekend", "hour"]), "weekend_hour")):
            t.to_csv(a.out / f"{ba}_by_{name}.csv")
        for ax, t, xlabel in ((axes[i, 0], h, "hour of the day"), (axes[i, 1], m, "month")):
            ax.plot(t.index, t["mape_model"], color="#c0392b", lw=1.1, label="model")
            ax.plot(t.index, t["mape_df"], color="#2c3e50", lw=1.1, label="DF")
            ax.set_ylabel(ba, fontsize=8)
            ax.tick_params(labelsize=7)
            if i == len(bas) - 1:
                ax.set_xlabel(xlabel, fontsize=8)
        worst_hours = h.sort_values("mape_gap", ascending=False).head(4)
        worst_months = m.sort_values("mape_gap", ascending=False).head(3)
        midday = h.loc[10:15, "bias_model"].mean() - h.loc[[0, 1, 2, 3, 4, 20, 21, 22, 23], "bias_model"].mean()
        by_year_midday = y.loc[(slice(None), slice(10, 15)), "bias_model"].groupby(level=0).mean().round(2).to_dict()
        lines += [f"## {ba}", "",
                  f"MAPE {summary.loc[ba, 'mape_model']:.2f} % against {summary.loc[ba, 'mape_df']:.2f} % for `DF`. "
                  f"Largest gaps by hour: {', '.join(f'{int(k)}h (+{v:.2f})' for k, v in worst_hours['mape_gap'].items())}; "
                  f"by month: {', '.join(f'{int(k)} (+{v:.2f})' for k, v in worst_months['mape_gap'].items())}. "
                  f"Model bias from 10h to 15h minus its bias at night: {midday:+.2f} points; midday bias by year: {by_year_midday}.", ""]
    axes[0, 0].legend(fontsize=7, frameon=False)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(figures / f"{a.doc.stem}_mape_by_hour_month.{ext}", dpi=200)
    plt.close(fig)
    lines += [f"![MAPE by hour and by month, model against DF](figures/{a.doc.stem}_mape_by_hour_month.png)", ""]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print(summary.to_string())
    print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
