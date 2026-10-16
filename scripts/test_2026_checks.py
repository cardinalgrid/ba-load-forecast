"""Descriptive checks on the test of January to September 2026, written after the run (``docs/test_2026_checks.md``).

    python scripts/test_2026_checks.py --runs <folder of the t2026 run>

Not part of the test. ``docs/test_2026_protocol.md`` fixes the headline and forbids removing BA-days by hand; nothing
here replaces it. The checks look at what the headline compares against: the BA's own day-ahead forecast (``DF``) as
published on Form EIA-930.

1. The published ``DF`` against the published demand, month by month, January to September of 2024, 2025 and 2026,
   for every comparable BA (raw EIA-930, all hours, before protocol v2): the median ratio ``DF / D`` and the hourly
   MAPE. A BA is marked as having a level change when its monthly median ratio in 2026 moved by more than 5 % (in log)
   from the same month of 2024 in at least six of the nine months. The rule was written after the run, on these data.
2. The ``DF`` of CISO as the run saw it (protocol v2 applied), shifted by one and two hours, month by month in 2025
   and 2026: a change of hour labels shows as a shift that lowers the error.
3. The headline aggregates of ``scoreboard_43.py`` recomputed without the marked BAs, and without CISO as well.
4. Coverage, Winkler score and width of the band by month (the NBM moved to version 5.0 in May 2026; protocol addendum).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ba_load_forecast.paths import TIDY  # noqa: E402

MODEL = "recipe2026"
H = [f"h{i:02d}" for i in range(24)]
MONTHS = range(1, 10)


def md(df: pd.DataFrame, fmt: str = "{:.2f}") -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(map(str, cols)) + " |", "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in df.iterrows():
        cells = [fmt.format(v) if isinstance(v, (float, np.floating)) and np.isfinite(v) else ("" if isinstance(v, float) else str(v))
                 for v in r]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def df_by_month(bas: list[str]) -> pd.DataFrame:
    parts = [pd.read_parquet(f, columns=["ba", "date", "forecast", "demand"]) for y in (2024, 2025, 2026)
             for f in sorted(TIDY.glob(f"{y}H*.parquet"))]
    t = pd.concat(parts, ignore_index=True)
    t = t[t["ba"].isin(bas) & (t["demand"] > 0) & (t["forecast"] > 0)]
    day = pd.to_datetime(t["date"])
    t = t.assign(year=day.dt.year, month=day.dt.month)
    t = t[t["month"].isin(MONTHS)]
    t["ratio"] = t["forecast"] / t["demand"]
    t["ape"] = (t["forecast"] - t["demand"]).abs() / t["demand"] * 100
    return t.groupby(["ba", "year", "month"]).agg(ratio=("ratio", "median"), mape=("ape", "mean")).reset_index()


def level_changes(m: pd.DataFrame) -> pd.Series:
    p = m.pivot_table(index=["ba", "month"], columns="year", values="ratio")
    moved = (np.log(p[2026] / p[2024]).abs() > 0.05).groupby("ba").sum()
    return moved.astype(int)


def shifted(runs: Path, ba: str) -> pd.DataFrame:
    h = pd.read_parquet(runs / f"t2026_{ba}_hourly.parquet")
    get = {k: h[h["model"] == k].set_index("day")[H].sort_index() for k in ("actual", "DF", MODEL)}
    idx = get["actual"].index.intersection(get["DF"].index).intersection(get[MODEL].index)
    a, d, r = (get[k].loc[idx].to_numpy().ravel() for k in ("actual", "DF", MODEL))
    month = np.repeat(pd.to_datetime(pd.Index(idx)).strftime("%Y-%m"), 24)
    rows = []
    for mo in sorted(set(month)):
        k = np.flatnonzero(month == mo)
        row = {"month": mo, "days": len(k) // 24, "MAPE recipe": np.nanmean(np.abs(r[k] - a[k]) / a[k] * 100)}
        for s in (0, -2, -1, 1, 2):
            kk = k[(k + s >= 0) & (k + s < len(d))]
            row["MAPE DF" if s == 0 else f"DF shifted {s:+d} h"] = np.nanmean(np.abs(d[kk + s] - a[kk]) / a[kk] * 100)
        rows.append(row)
    return pd.DataFrame(rows)


def band_by_month(rows: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    r = rows[(rows["model"] == MODEL) & rows["coverage_90"].notna()].copy()
    r["month"] = pd.to_datetime(r["day"]).dt.month

    def summ(d: pd.DataFrame) -> pd.Series:
        return pd.Series({"BA-days": len(d), "coverage 90": d["coverage_90"].mean(),
                          "Winkler 90, weighted": np.average(d["winkler_90"], weights=d["actual_mean"]),
                          "width 90, weighted": np.average(d["width_90"], weights=d["actual_mean"])})

    by_month = r.groupby("month")[["coverage_90", "winkler_90", "width_90", "actual_mean"]].apply(summ).reset_index()
    by_month["BA-days"] = by_month["BA-days"].astype(int).astype(str)
    by_month["month"] = pd.to_datetime(by_month["month"].astype(int).astype(str) + "-2026", format="%m-%Y").dt.strftime("%B")
    r["NBM"] = np.where(r["month"] <= 4, "January to April (version 4.3)", "May to September (version 5.0)")
    halves = r.groupby("NBM")[["coverage_90", "winkler_90", "width_90", "actual_mean"]].apply(summ).reset_index()
    halves["BA-days"] = halves["BA-days"].astype(int).astype(str)
    return by_month, halves


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, required=True)
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "test_2026")
    ap.add_argument("--reference", type=Path, default=ROOT / "results" / "b4_2023_2025" / "scoreboard.csv")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "test_2026_checks.md")
    a = ap.parse_args(argv)

    sb = pd.read_csv(a.results / "scoreboard.csv")
    ref = pd.read_csv(a.reference).set_index("ba")
    comparable = sb.loc[sb["comparable"], "ba"].tolist()
    m = df_by_month(comparable)
    moved = level_changes(m)
    marked = sorted(moved[moved >= 6].index)

    per = sb[sb["comparable"]].set_index("ba")[["mape_df", "mape"]].rename(columns={"mape_df": "MAPE DF 2026", "mape": "MAPE recipe 2026"})
    per.insert(0, "MAPE DF 2023-2025", ref["mape_df"].reindex(per.index))
    per.insert(0, "months moved > 5 %", moved.reindex(per.index).fillna(0).astype(int))
    per = per.sort_values(["months moved > 5 %", "MAPE DF 2026"], ascending=False).reset_index().rename(columns={"ba": "BA"})
    shown = per[(per["months moved > 5 %"] >= 2) | (per["MAPE DF 2026"] > 1.5 * per["MAPE DF 2023-2025"])]

    detail = []
    for ba in [*marked, "CISO"]:
        w = m[m["ba"] == ba].pivot_table(index="month", columns="year", values=["ratio", "mape"])
        w.columns = [f"{'DF / D' if k == 'ratio' else 'MAPE DF'} {y}" for k, y in w.columns]
        w = w[[c for c in w.columns if c.startswith("DF / D")] + [c for c in w.columns if c.startswith("MAPE")]].reset_index()
        detail.append(f"**{ba}**\n\n{md(w, '{:.3g}')}\n")

    ciso = shifted(a.runs, "CISO")
    t = sb.copy()
    sets = [("38 comparable BAs (the headline)", []), (f"without the BAs with a level change ({', '.join(marked)})", marked),
            ("without those and CISO", [*marked, "CISO"])]
    agg = []
    for name, drop in sets:
        d = t[t["comparable"] & ~t["ba"].isin(drop)]
        w = d["demand_mw"]
        agg.append({"set": name, "BAs": len(d), "MAPE recipe, weighted": np.average(d["mape"], weights=w),
                    "MAPE DF, weighted": np.average(d["mape_df"], weights=w), "MAPE recipe, median": d["mape"].median(),
                    "MAPE DF, median": d["mape_df"].median(), "BAs better": int((d["gap"] < 0).sum()),
                    "BAs worse": int((d["gap"] > 0).sum()), "better, p < 0.05": int(((d["gap"] < 0) & (d["dm_p"] < 0.05)).sum()),
                    "worse, p < 0.05": int(((d["gap"] > 0) & (d["dm_p"] < 0.05)).sum())})
    agg = pd.DataFrame(agg)
    for c in ("BAs", "BAs better", "BAs worse", "better, p < 0.05", "worse, p < 0.05"):
        agg[c] = agg[c].astype(int).astype(str)
    worse = ", ".join(sb[sb["comparable"] & (sb["gap"] > 0)].sort_values("gap", ascending=False)["ba"])

    by_month, halves = band_by_month(pd.read_parquet(a.results / "rows.parquet"))
    lowest = by_month.loc[by_month["coverage 90"].idxmin()]

    text = f"""# The test on January to September 2026: descriptive checks after the run

Written on 16 October 2026, after the run and the reports of `docs/test_2026_protocol.md`, by
`scripts/test_2026_checks.py`. None of this is the test: the headline of the protocol stands as reported in
`docs/test_2026_scoreboard.md`, and no BA-day was removed from it. These checks describe what the headline compares
against, the BA's own day-ahead forecast (`DF`) as published on Form EIA-930, and the band after the NBM moved to
version 5.0.

## 1. The published DF changed at several BAs

The headline compares the recipe with `DF` as published. At several BAs the published `DF` moved away from the
published demand in 2026 by far more than in earlier years. The table lists the comparable BAs with a level change
(below) or whose `DF` MAPE in 2026 is more than 1.5 times their 2023 to 2025 value. "Months moved" counts the months
of January to September 2026 in which the median hourly ratio `DF / D` moved by more than 5 % (in log) from the same
month of 2024 (raw EIA-930, all hours). A BA is marked as having a level change when that count is six or more; the
rule was written after the run, on these data, and marks {len(marked)}: {', '.join(marked)}.

{md(shown)}

Month by month (raw EIA-930, all hours, January to September of each year; hourly MAPE, so larger than the daily MAPE
of the scoreboard):

{chr(10).join(detail)}
SWPP and LDWP had already moved in 2025 (SWPP from May 2025), so part of their change is also in the 2023 to 2025
evaluation. CISO is not marked by the level rule (its ratio stays between 0.95 and 0.98 in the three years), but its
`DF` error rose from {ref.loc['CISO', 'mape_df']:.2f} % over 2023 to 2025 to {sb.set_index('ba').loc['CISO', 'mape_df']:.2f} % in
2026. The `DF` as the run saw it (protocol v2 applied), shifted by whole hours, points to a change of hour labels in the
published series: from December 2025 on, a shift of one hour (+1 h) lowers its error in every month:

{md(ciso)}

## 2. The headline without those BAs

The aggregates of the scoreboard recomputed on the comparable BAs left after removing the marked BAs, and CISO as
well. Same per-BA numbers as `docs/test_2026_scoreboard.md`; only the set changes.

{md(agg)}

Without the published series that changed, the recipe stays ahead on the demand-weighted MAPE, by a much smaller
margin than in the headline, and the medians of the two are close: the gain is concentrated in the largest BAs and in
the BAs whose `DF` is weak. Removing those BAs removes only BAs where the recipe was ahead; the {(sb['comparable'] & (sb['gap'] > 0)).sum()}
comparable BAs where `DF` is ahead are the same in every row: {worse}.

## 3. The band by month

Coverage of the 90 % band (mean over BA-days) and Winkler score and width (weighted by mean demand), 43 BAs. The NBM
moved to version 5.0 in May 2026, with a spread about 0.9 times that of version 4.3 on the one day both versions hold
(protocol addendum).

{md(by_month, '{:.3f}')}

{md(halves, '{:.3f}')}

Coverage is within one point of 90 % in every month except {lowest['month']} ({lowest['coverage 90']:.3f}). The
width narrows from January to September, and already from January to April under version 4.3, so this table does not
separate the effect of version 5.0 from that of the season.
"""
    a.doc.parent.mkdir(parents=True, exist_ok=True)
    a.doc.write_text(text, encoding="utf-8")
    print(agg.to_string(index=False))
    print("wrote", a.doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
