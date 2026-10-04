"""When was each BA's published day-ahead forecast (``DF``) made? An indirect test from the error by hour of the day.

    python scripts/df_vintage_fingerprint.py --runs <folder with b4_<BA>_hourly.parquet> --doc docs/df_vintage_fingerprint.md

A forecast made at midnight before the target day is one to four hours ahead at the first hours of the day and
about a day ahead at its last hours, so its error grows through the day. A forecast made at 9 a.m. of the day before
is already 15 hours ahead at the first hour, and its error grows much less. The test compares, hour by hour, the error
of ``DF`` with the error of the open forecaster, whose cut-off is known (9 a.m. of the day before), so that what is
hard about each hour (the morning ramp, the evening peak) cancels:

    ratio(h) = MAE of DF at hour h / MAE of the open forecaster at hour h          (both in percent of the actual)
    fingerprint = mean ratio at hours 00-03 / mean ratio at hours 20-23

A ``DF`` made at about the same time as the open forecaster gives a fingerprint near 1; a ``DF`` made close to the
target day gives a fingerprint well below 1. ``DF`` is first divided by one plus its own median relative error at the
same hour over the previous 60 days (known before the day), so that a constant definitional offset at some hours (a
different perimeter or hour convention) does not pass for a lead-time effect. Two BAs with a known vintage calibrate
the scale in principle: CAISO's ``DF`` equals its day-ahead market forecast issued the morning before (12 of 12 sampled
days); MISO's equals the forecast in its daily report published at about 00:30 EST of the target day (10 of 12), but the
values for the target day change between consecutive reports, so they were updated at some hour of the day before, not
necessarily at midnight. The two calibration BAs come out close (CAISO 1.08, MISO 1.19, 3 October 2026), so the test does
not separate a morning ``DF`` from a midnight one with a known reference; it is reported as a signal only: a fingerprint
well below 1 means a ``DF`` relatively better at the first hours of the day than at the last, which a forecast made close
to the day would show. Writes ``results/df_vintage/fingerprint.csv`` and a document.
"""

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HOURS = [f"h{i:02d}" for i in range(24)]
NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")
KNOWN = {"CISO": "matched: CAISO day-ahead market forecast, morning of D-1",
         "MISO": "matched: forecast in MISO's report published about 00:30 EST of D, updated during D-1 (hour unknown)"}


def corrected(df: pd.DataFrame, actual: pd.DataFrame, window: int = 60) -> pd.DataFrame:
    """DF divided by one plus its own median relative error at the same hour over the previous ``window`` days."""
    rel = (df - actual) / actual
    med = rel.shift(2).rolling(window, min_periods=20).median()          # known before the day: up to D-2
    return df / (1.0 + med)


def ba_fingerprint(path: Path, model: str, start: str, end: str) -> dict | None:
    t = pd.read_parquet(path)
    t["day"] = pd.to_datetime(t["day"])
    ba = t["ba"].iloc[0]
    wide = {m: t[t["model"] == m].set_index("day")[HOURS].sort_index() for m in ("actual", model, "DF")}
    days = wide["actual"].index.intersection(wide[model].index).intersection(wide["DF"].index)
    a = wide["actual"].loc[days].astype(float)
    a = a.where(a > 0)
    dfc = corrected(wide["DF"].loc[days].astype(float), a)
    m = wide[model].loc[days].astype(float)
    keep = (days >= pd.Timestamp(start)) & (days <= pd.Timestamp(end))
    a, dfc, m = a[keep], dfc[keep], m[keep]
    ok = a.notna().all(axis=1) & dfc.notna().all(axis=1) & m.notna().all(axis=1)
    if ok.sum() < 200:
        return None
    a, dfc, m = a[ok], dfc[ok], m[ok]
    e_df = ((dfc - a).abs() / a * 100).mean()
    e_m = ((m - a).abs() / a * 100).mean()
    ratio = (e_df / e_m).to_numpy()
    if not np.all(np.isfinite(ratio)) or np.any(ratio <= 0):
        return None
    out = {"ba": ba, "days": int(ok.sum()),
           "fingerprint": float(ratio[0:4].mean() / ratio[20:24].mean()),
           "slope": float(np.polyfit(np.arange(24), np.log(ratio), 1)[0]),
           "mae_df_00_03": float(e_df.iloc[0:4].mean()), "mae_df_20_23": float(e_df.iloc[20:24].mean()),
           "mae_model_00_03": float(e_m.iloc[0:4].mean()), "mae_model_20_23": float(e_m.iloc[20:24].mean())}
    out.update({f"ratio_{h}": float(ratio[i]) for i, h in enumerate(HOURS)})
    return out


def signal(f: float) -> str:
    """What the fingerprint suggests, without a validated scale."""
    if not np.isfinite(f) or f <= 0:
        return "no answer"
    if f < 0.80:
        return "relatively better in the first hours: consistent with a DF made close to the day"
    if f > 1.20:
        return "relatively worse in the first hours: no sign of a late DF"
    return "no clear signal"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e_ghcnh")
    ap.add_argument("--group", default="b4")
    ap.add_argument("--model", default="final10s")
    ap.add_argument("--start", default="2023-01-01")
    ap.add_argument("--end", default="2025-12-31")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "df_vintage" / "fingerprint.csv")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "df_vintage_fingerprint.md")
    a = ap.parse_args(argv)
    rows = [r for f in sorted(glob.glob(str(a.runs / f"{a.group}_*_hourly.parquet")))
            if (r := ba_fingerprint(Path(f), a.model, a.start, a.end)) is not None]
    t = pd.DataFrame(rows)
    morning = float(t.loc[t.ba == "CISO", "fingerprint"].iloc[0])
    midnight = float(t.loc[t.ba == "MISO", "fingerprint"].iloc[0])
    t["class"] = [KNOWN.get(b, signal(f)) for b, f in zip(t["ba"], t["fingerprint"], strict=True)]
    t["set"] = np.where(t["ba"].isin(DEV_BAS), "development", "new")
    t["comparable"] = ~t["ba"].isin(NOT_COMPARABLE)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    t.to_csv(a.out, index=False, float_format="%.4f")
    s = t.sort_values("fingerprint")
    lines = ["# When is each BA's published forecast made? The error-by-hour fingerprint", "",
             f"Hourly outputs of the `{a.group}` run, {a.start} to {a.end}. Fingerprint = (MAE of `DF` / MAE of `{a.model}`) at hours "
             "00-03 divided by the same ratio at hours 20-23, local reporting clock, `DF` first corrected by its own trailing "
             "hourly bias. CAISO, whose `DF` is matched to the day-ahead market forecast of the morning before, gives "
             f"{morning:.2f}; MISO, whose `DF` is matched to a report published at about 00:30 EST of the target day but updated "
             f"at an unknown hour of the day before, gives {midnight:.2f}. The scale is not validated: the column is a signal, not "
             "a time. A BA with no row has a series the test cannot use (a ratio that is not positive at some hour).", "",
             "| BA | set | days | fingerprint | slope of log ratio per hour | MAE DF 00-03 | MAE DF 20-23 | signal |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for _, r in s.iterrows():
        lines.append(f"| {r['ba']}{'' if r['comparable'] else ' (a)'} | {r['set']} | {r['days']} | {r['fingerprint']:.2f} | "
                     f"{r['slope']:+.3f} | {r['mae_df_00_03']:.2f} | {r['mae_df_20_23']:.2f} | {r['class']} |")
    lines += ["", "(a) `DF` listed by the EIA as not comparable with demand."]
    a.doc.parent.mkdir(parents=True, exist_ok=True)
    a.doc.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(s[["ba", "set", "fingerprint", "slope", "class"]].to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
