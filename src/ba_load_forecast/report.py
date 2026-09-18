"""Aggregation of the harness rows: model by BA, demand-weighted overall, the winter events, and a test.

Only BA-days scored for every model (the BA's own forecast included) enter the tables, so that every
model is measured on the same days. Winning a day means a lower MAPE than the BA's forecast, or a
smaller under-forecast at the peak (a less negative ``peak_under_pct``).
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.events import EVENTS

from .evaluate import BA_MODEL

METRICS = ["mape", "peak_err_pct", "peak_under_pct", "peak_hour_err"]


def complete_cases(rows: pd.DataFrame) -> pd.DataFrame:
    """The rows of the BA-days on which every model was scored."""
    scored = rows[~rows["skipped"].astype(bool)]
    n_models = rows["model"].nunique()
    counts = scored.groupby(["ba", "day"])["model"].nunique()
    full = counts[counts == n_models].index
    return scored.set_index(["ba", "day"]).loc[full].reset_index()


def paired_with_ba(rows: pd.DataFrame) -> pd.DataFrame:
    """Every model row joined with the BA's own row for the same BA-day (columns suffixed ``_ba``)."""
    ba = rows[rows["model"] == BA_MODEL].set_index(["ba", "day"])[METRICS].add_suffix("_ba")
    return rows.join(ba, on=["ba", "day"])


def by_model_ba(rows: pd.DataFrame) -> pd.DataFrame:
    p = paired_with_ba(rows)
    p["abs_peak_hour_err"] = p["peak_hour_err"].abs()
    p["win_mape"] = p["mape"] < p["mape_ba"]
    p["win_peak_under"] = p["peak_under_pct"] > p["peak_under_pct_ba"]
    g = p.groupby(["model", "ba"])
    out = g[["mape", "peak_err_pct", "peak_under_pct", "abs_peak_hour_err"]].mean()
    out.insert(1, "mape_median", g["mape"].median())
    out["worst_peak_under_pct"] = g["peak_under_pct"].min()
    out["win_mape"] = g["win_mape"].mean()
    out["win_peak_under"] = g["win_peak_under"].mean()
    out["n_days"] = g.size()
    out["demand_mw"] = g["actual_mean"].mean()
    out.loc[out.index.get_level_values("model") == BA_MODEL, ["win_mape", "win_peak_under"]] = np.nan
    return out


def overall(table: pd.DataFrame) -> pd.DataFrame:
    """The by-model-BA table averaged over BAs, weighted by each BA's mean demand."""
    t = table.reset_index()
    out = {}
    for model, g in t.groupby("model"):
        w = g["demand_mw"] / g["demand_mw"].sum()
        row = {c: float((g[c] * w).sum()) for c in ["mape", "mape_median", "peak_err_pct", "peak_under_pct",
                                                     "abs_peak_hour_err", "win_mape", "win_peak_under"]}
        row["worst_peak_under_pct"] = float(g["worst_peak_under_pct"].min())
        row["n_days"] = int(g["n_days"].sum())
        row["n_bas"] = len(g)
        out[model] = row
    return pd.DataFrame(out).T.sort_values("mape")


def events_table(rows: pd.DataFrame, events=EVENTS) -> pd.DataFrame:
    """Per event, model and BA: mean and worst under-forecast at the peak over the event's calendar days."""
    parts = []
    day = pd.to_datetime(rows["day"])
    for ev in events:
        w = rows[(day >= pd.Timestamp(ev["start"])) & (day <= pd.Timestamp(ev["end"]))]
        if w.empty:
            continue
        g = w.groupby(["model", "ba"])
        t = g[["mape", "peak_err_pct", "peak_under_pct"]].mean()
        t["worst_peak_under_pct"] = g["peak_under_pct"].min()
        t["n_days"] = g.size()
        t.insert(0, "event", ev["name"])
        parts.append(t.reset_index())
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def dm_test(errors_a, errors_b, power: int = 1) -> tuple[float, float]:
    """Diebold-Mariano statistic and two-sided p-value for one-step-ahead forecasts.

    Loss is ``|e|**power``; the differential is loss_a minus loss_b, so a negative statistic favours
    ``a``. Uses the Harvey, Leybourne and Newbold small-sample correction and the normal
    approximation for the p-value (reference marked for verification in the study notes).
    """
    a = np.asarray(errors_a, dtype=float)
    b = np.asarray(errors_b, dtype=float)
    ok = ~np.isnan(a) & ~np.isnan(b)
    d = np.abs(a[ok]) ** power - np.abs(b[ok]) ** power
    n = len(d)
    if n < 3:
        return float("nan"), float("nan")
    var = d.var(ddof=1)
    if var == 0.0:
        return 0.0, 1.0
    stat = d.mean() / math.sqrt(var / n)
    stat *= math.sqrt((n + 1 - 2 + 0) / n)
    p = math.erfc(abs(stat) / math.sqrt(2.0))
    return float(stat), float(p)


def dm_against_ba(rows: pd.DataFrame, metric: str = "mape") -> pd.DataFrame:
    """Diebold-Mariano of every model against the BA's forecast, per BA, on the daily ``metric``."""
    p = paired_with_ba(rows)
    out = []
    for (model, ba), g in p.groupby(["model", "ba"]):
        if model == BA_MODEL:
            continue
        stat, pv = dm_test(g[metric].to_numpy(), g[f"{metric}_ba"].to_numpy())
        out.append({"model": model, "ba": ba, "metric": metric, "dm_stat": stat, "p_value": pv, "n_days": len(g)})
    return pd.DataFrame(out)


def load_shed_days(path=None) -> pd.DataFrame:
    """The documented firm-load-shed days (``docs/load_shed_days.csv``: ba, date, ...), or an empty frame."""
    p = Path(path) if path else Path(__file__).resolve().parents[2] / "docs" / "load_shed_days.csv"
    if not p.exists():
        return pd.DataFrame(columns=["ba", "date"])
    d = pd.read_csv(p)
    d["date"] = pd.to_datetime(d["date"]).dt.date
    return d


def split_shed(rows: pd.DataFrame, shed: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """The rows outside and inside the documented load-shed BA-days."""
    if shed.empty:
        return rows, rows.iloc[0:0]
    key = set(zip(shed["ba"], shed["date"], strict=True))
    mask = np.array([(b, d) in key for b, d in zip(rows["ba"], rows["day"], strict=True)])
    return rows[~mask], rows[mask]


def summarise(rows: pd.DataFrame, events=EVENTS, shed: pd.DataFrame | None = None) -> dict[str, pd.DataFrame]:
    """Tables on the complete cases; documented load-shed BA-days are left out of every metric and reported apart.

    On a load-shed day the load that occurred is the load served, not the demand, so no forecast can be
    scored against it. ``shed`` defaults to the list in ``docs/load_shed_days.csv``.
    """
    cc = complete_cases(rows)
    shed = load_shed_days() if shed is None else shed
    cc, shed_rows = split_shed(cc, shed)
    table = by_model_ba(cc)
    out = {
        "by_model_ba": table,
        "overall": overall(table),
        "events": events_table(cc, events),
        "dm_mape": dm_against_ba(cc, "mape"),
        "dm_peak": dm_against_ba(cc, "peak_err_pct"),
        "coverage": rows.groupby("model")["skipped"].apply(lambda s: 1.0 - s.astype(bool).mean()).to_frame("scored_fraction"),
    }
    if len(shed_rows):
        out["shed_days"] = shed_rows[["ba", "day", "model", "mape", "peak_err_pct", "peak_under_pct"]].sort_values(["ba", "day", "model"])
    return out


def markdown_table(t: pd.DataFrame, digits: int = 2) -> str:
    t = t.reset_index() if not isinstance(t.index, pd.RangeIndex) else t
    cols = [str(c) for c in t.columns]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join("---" for _ in cols) + " |"]
    for r in t.itertuples(index=False):
        cells = []
        for v in r:
            if isinstance(v, float):
                cells.append("" if np.isnan(v) else (str(int(v)) if v.is_integer() and abs(v) > 50 else f"{v:.{digits}f}"))
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_report(tables: dict[str, pd.DataFrame], path, title: str, intro: str) -> None:
    ov = tables["overall"]
    lines = [f"# {title}", "", intro, "",
             "## All BAs, weighted by mean demand", "",
             "Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the "
             "negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst "
             "under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at "
             "the peak, than the BA's own forecast (`DF`).", "",
             markdown_table(ov), "",
             "## By BA", "", markdown_table(tables["by_model_ba"]), ""]
    if len(tables["events"]):
        lines += ["## The winter events (calendar days of each event)", "", markdown_table(tables["events"]), ""]
    if "shed_days" in tables:
        lines += ["## Documented load-shed days (left out of every table above)", "",
                  "On these BA-days the load that occurred is the load served under firm load shed, not the demand "
                  "(`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the "
                  "metrics are shown for the record.", "",
                  markdown_table(tables["shed_days"]), ""]
    lines += ["## Diebold-Mariano against the BA's forecast (daily MAPE)", "",
              "Negative statistics favour the model; p-values from the normal approximation.", "",
              markdown_table(tables["dm_mape"], 3), "",
              "## Coverage", "", "Fraction of BA-days each model produced a scorable forecast for.", "",
              markdown_table(tables["coverage"], 3), ""]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
