"""The error profile of the BAs' own day-ahead forecast (EIA-930 ``DF``) by hour of the day.

    python scripts/df_profile.py

Uses the tidy EIA-930 files only (no model run). Per BA, on the development period: the mean signed error
and the mean absolute percentage error of ``DF`` by local hour, the same by year, the hours at which
``DF`` is off by more than half of the demand (reporting faults rather than forecast errors), and the MAPE
``DF`` would have if its own recent median error at each hour (trailing ``--window`` days, known before the
day) were removed. A large fall under that correction means a systematic offset between what ``DF`` and
``D`` measure, or a forecast that is not revised by hour; it is a diagnostic of the benchmark, not a model.
A second table looks for a time misalignment: the MAPE of ``DF`` moved one hour either way, year by year
over the whole archive; where the moved series is closer to ``D`` by a wide margin, ``DF`` and ``D`` are
stamped on different hour conventions in the published data.
Tables go to ``results/df_profile/`` and a summary to ``docs/df_hourly_bias.md``.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from ba_load_forecast.information_set import Loader
from ba_load_forecast.paths import TIDY
from ba_load_forecast.report import load_shed_days, markdown_table

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")
FAULT = 0.5          # |DF / D - 1| above this marks the hour as a reporting fault


def day_matrix(s: pd.Series, start: date, end: date) -> pd.DataFrame:
    """Days in rows, local hours 0 to 23 (hour beginning) in columns."""
    s = s[~s.index.duplicated()].loc[pd.Timestamp(start): pd.Timestamp(end) + pd.Timedelta(hours=23)]
    return pd.DataFrame({"day": s.index.normalize(), "hour": s.index.hour, "v": s.to_numpy()}).pivot(
        index="day", columns="hour", values="v").reindex(columns=range(24))


SHIFTS = (-1, 0, 1)


def shifted_mape(load: pd.Series, fcst: pd.Series, shift: int) -> float:
    """MAPE of DF against D when the DF value stamped ``shift`` hours away is compared with D (-1: the hour before)."""
    moved = fcst.copy()
    moved.index = moved.index - pd.Timedelta(hours=shift)
    rel = ((moved.reindex(load.index) - load) / load).dropna()
    rel = rel[rel.abs() <= FAULT]
    return float(rel.abs().mean() * 100) if len(rel) else float("nan")


def alignment_by_year(ld: Loader, ba: str, years) -> pd.DataFrame:
    rows = []
    for y in years:
        load, fcst = ld.raw_load(ba, y), ld.forecast(ba, y)
        if load.empty or fcst.empty:
            continue
        load, fcst = load[~load.index.duplicated()], fcst[~fcst.index.duplicated()]
        load = load[load > 0]
        row = {"ba": ba, "year": y} | {f"mape_shift_{k:+d}h": shifted_mape(load, fcst, k) for k in SHIFTS}
        if not np.isnan(list(row.values())[2:]).all():
            row["best_shift_h"] = min(SHIFTS, key=lambda k: row[f"mape_shift_{k:+d}h"])
            rows.append(row)
    return pd.DataFrame(rows)


def trailing_median(rel: pd.DataFrame, window: int, min_days: int = 20) -> pd.DataFrame:
    """Median relative error by hour over the previous ``window`` days, the day itself left out."""
    return rel.shift(1).rolling(window, min_periods=min_days).median()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--window", type=int, default=60)
    ap.add_argument("--first-year", type=int, default=2016)
    ap.add_argument("--last-year", type=int, default=2025)
    ap.add_argument("--tidy", type=Path, default=TIDY)
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--group", default="intervals")
    ap.add_argument("--model", default="ens_bc_regime")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "df_profile")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "df_hourly_bias.md")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)

    ld = Loader(a.tidy, a.tidy, a.tidy)          # only the load and forecast readers are used
    shed = load_shed_days()
    shed_key = set(zip(shed["ba"], pd.to_datetime(shed["date"]), strict=True)) if len(shed) else set()
    years = range(a.start.year, a.end.year + 1)
    summary, bias_rows, mape_rows, align = [], {}, {}, []
    for ba in a.bas:
        align.append(alignment_by_year(ld, ba, range(a.first_year, a.last_year + 1)))
        load = pd.concat([ld.raw_load(ba, y) for y in years])
        fcst = pd.concat([ld.forecast(ba, y) for y in years])
        d, f = day_matrix(load, a.start, a.end), day_matrix(fcst, a.start, a.end)
        days = d.dropna().index.intersection(f.dropna().index)
        days = pd.DatetimeIndex([x for x in days if (ba, x) not in shed_key])
        d, f = d.loc[days], f.loc[days]
        d = d.where(d > 0)
        rel = (f - d) / d
        fault = rel.abs() > FAULT
        clean = ~fault.any(axis=1)
        rel_c = rel[clean]
        by_hour = pd.DataFrame({"bias_pct": rel_c.mean() * 100, "mape_pct": rel_c.abs().mean() * 100,
                                "sd_pct": rel_c.std() * 100})
        by_hour.round(3).to_csv(a.out / f"{ba}_by_hour.csv")
        by_year = (rel_c * 100).groupby(rel_c.index.year).mean().round(2)
        by_year.to_csv(a.out / f"{ba}_bias_by_year_hour.csv")
        med = trailing_median(rel_c, a.window)
        ok = med.notna().all(axis=1)
        corrected = f.loc[rel_c.index][ok] / (1.0 + med[ok])
        mape_corr = ((corrected - d.loc[corrected.index]).abs() / d.loc[corrected.index]).mean(axis=1) * 100
        mape_same = rel_c[ok].abs().mean(axis=1) * 100
        model_mape, model_days = np.nan, 0
        stored = a.runs / f"{a.group}_{ba}_hourly.parquet"
        if stored.exists():
            h = pd.read_parquet(stored)
            m = h[h["model"] == a.model].assign(day=lambda x: pd.to_datetime(x["day"])).set_index("day")
            m = m[[f"h{i:02d}" for i in range(24)]].dropna()
            m.columns = range(24)
            both = m.index.intersection(corrected.index)
            model_days = len(both)
            if model_days:
                model_mape = ((m.loc[both] - d.loc[both]).abs() / d.loc[both]).mean(axis=1).mean() * 100
                mape_same, mape_corr = mape_same.loc[both], mape_corr.loc[both]
        bias_rows[ba] = by_hour["bias_pct"]
        mape_rows[ba] = by_hour["mape_pct"]
        summary.append({
            "ba": ba, "days": len(days), "fault_hours": int(fault.to_numpy().sum()), "fault_days": int((~clean).sum()),
            "mape": rel.abs().mean(axis=1).mean() * 100, "mape_no_fault_days": rel_c.abs().mean(axis=1).mean() * 100,
            "bias_min": by_hour["bias_pct"].min(), "hour_of_min": int(by_hour["bias_pct"].idxmin()),
            "bias_max": by_hour["bias_pct"].max(), "hour_of_max": int(by_hour["bias_pct"].idxmax()),
            "bias_range": by_hour["bias_pct"].max() - by_hour["bias_pct"].min(),
            "mape_same_days": mape_same.mean(), "mape_bias_removed": mape_corr.mean(),
            "model_mape": model_mape, "model_days": model_days, "demand_mw": float(np.nanmean(d[clean].to_numpy())),
        })

    s = pd.DataFrame(summary).set_index("ba").sort_values("bias_range", ascending=False)
    s.round(3).to_csv(a.out / "summary.csv")
    w = s.dropna(subset=["model_mape"])
    weighted = {c: float(np.average(w[c], weights=w["demand_mw"])) for c in ("mape_same_days", "mape_bias_removed", "model_mape")} if len(w) else {}
    al = pd.concat(align, ignore_index=True)
    al.round(3).to_csv(a.out / "alignment_by_year.csv", index=False)
    moved = al[al["best_shift_h"] != 0].copy()
    moved["gain"] = moved["mape_shift_+0h"] - moved[[f"mape_shift_{k:+d}h" for k in SHIFTS]].min(axis=1)
    moved = moved[moved["gain"] >= 0.3].set_index(["ba", "year"]).drop(columns="gain")
    bias = pd.DataFrame(bias_rows).T.loc[s.index]
    mape = pd.DataFrame(mape_rows).T.loc[s.index]
    bias.round(3).to_csv(a.out / "bias_by_hour.csv")
    mape.round(3).to_csv(a.out / "mape_by_hour.csv")
    for t in (bias, mape):
        t.columns = [f"{h:02d}" for h in t.columns]

    lines = [
        "# The BAs' own forecast by hour of the day", "",
        f"EIA-930 day-ahead demand forecast (`DF`) against demand (`D`), {a.start} to {a.end}, local hours (hour "
        "beginning), documented load-shed days left out. Days on which `DF` is off by more than "
        f"{FAULT:.0%} of the demand at any hour are counted apart as reporting faults and left out of the hourly tables.", "",
        "## Summary", "",
        "`bias_range` is the distance between the most negative and the most positive mean signed error over the 24 "
        "hours. `mape_bias_removed` is the MAPE of `DF` after dividing it by one plus its own median relative error "
        f"at the same hour over the previous {a.window} days (the day itself left out), next to `mape_same_days`, "
        "the plain MAPE on the days where that correction exists.", "",
        markdown_table(s, 2), "",
        f"`model_mape` is the MAPE of `{a.model}` (stored hourly forecasts of the `{a.group}` group) on the days it shares "
        "with the corrected `DF`; the two `DF` columns are on those same days. Weighted by mean demand over the BAs: "
        + (f"`DF` {weighted['mape_same_days']:.2f} %, `DF` with its hourly bias removed {weighted['mape_bias_removed']:.2f} %, "
           f"`{a.model}` {weighted['model_mape']:.2f} %." if weighted else "no stored model forecasts found."), "",
        "## Mean signed error by hour (%, negative is under-forecast)", "", markdown_table(bias, 1), "",
        "## MAPE by hour (%)", "", markdown_table(mape, 1), "",
        "## Time alignment of `DF` and `D`, year by year", "",
        "MAPE of `DF` as published (`+0h`) and with the value stamped one hour earlier (`-1h`) or later (`+1h`) compared "
        "with the same `D`. Only the BA-years in which a moved series beats the published one by 0.3 points or more are "
        "listed; the full table is `results/df_profile/alignment_by_year.csv`.", "",
        markdown_table(moved, 2) if len(moved) else "No BA-year shows a misalignment.", "",
        "## Reading", "",
        "A forecast issued once, a day ahead, by a model without a systematic fault has a signed error near zero at "
        "every hour. Where the signed error swings by several points between the night and the morning, and the swing "
        "is stable from year to year (`results/df_profile/<BA>_bias_by_year_hour.csv`), the published `DF` and `D` are "
        "unlikely to measure the same quantity at those hours, or `DF` is not the forecast the operator used for the "
        "night. The EIA-930 instructions ask for \"the day-ahead demand forecast generated in the normal course of "
        "business\" and fix neither the hour of issue nor the treatment of pumping load or of behind-the-meter "
        "generation, so the cause cannot be settled from the data alone. Two consequences for a comparison against "
        "`DF`: a model that learns the demand series directly gains at those hours for a reason that is not forecasting "
        "skill, and the fair reading of a win or a loss looks at the hours as well as at the daily mean.", "",
    ]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print(s.round(2).to_string())
    print(weighted)
    print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
