"""Per-BA errors by part of the day for the recipe and the BA's own forecast (``DF``), from the hourly outputs.

    python scripts/daypart_43.py --runs <folder with b4_<BA>_hourly.parquet> --doc docs/daypart_43_bas.md

Parts of the day in the BA's local time: night 00-05, morning 06-10, midday 11-15, evening 16-21, late 22-23.
For each BA and model, on the days both the recipe and ``DF`` scored: the MAPE of the hours of each part (mean of the
absolute hourly error in percent of the actual, over all hours of the part and all days); the signed error at the hour
of the actual daily peak (percent of the peak; negative is under); the share of days under-forecast at the peak; and
the mean absolute error of the peak hour's timing (hours). Writes ``results/b4_2023_2025/daypart.csv`` and a document.
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
PARTS = {"night": range(0, 6), "morning": range(6, 11), "midday": range(11, 16), "evening": range(16, 22), "late": range(22, 24)}
NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")


def scored_days(rows: pd.DataFrame, ba: str, model: str) -> pd.Index:
    """The days of ``ba`` on which both ``model`` and ``DF`` were scored (not skipped, with a MAPE)."""
    r = rows[(rows["ba"] == ba) & (~rows["skipped"].astype(bool)) & rows["mape"].notna()]
    a = set(r[r["model"] == model]["day"])
    b = set(r[r["model"] == "DF"]["day"])
    return pd.Index(sorted(a & b))


def ba_table(path: Path, model: str, rows: pd.DataFrame) -> dict:
    t = pd.read_parquet(path)
    t["day"] = t["day"].astype(str)
    ba = t["ba"].iloc[0]
    wide = {m: t[t["model"] == m].set_index("day")[HOURS] for m in ("actual", model, "DF")}
    days = wide["actual"].index.intersection(wide[model].index).intersection(wide["DF"].index)
    days = days.intersection(scored_days(rows, ba, model))
    a = wide["actual"].loc[days].to_numpy(dtype=float)
    ok = np.isfinite(a).all(axis=1) & (a > 0).all(axis=1)
    out = {"ba": ba, "days": int(ok.sum())}
    for m in (model, "DF"):
        f = wide[m].loc[days].to_numpy(dtype=float)
        good = ok & np.isfinite(f).all(axis=1)
        aa, ff = a[good], f[good]
        err = (ff - aa) / aa * 100
        tag = "recipe" if m == model else "df"
        for part, hrs in PARTS.items():
            out[f"{part}_{tag}"] = float(np.abs(err[:, list(hrs)]).mean())
        ph = aa.argmax(axis=1)
        peak_err = (ff[np.arange(len(ff)), ph] - aa.max(axis=1)) / aa.max(axis=1) * 100
        out[f"peak_err_{tag}"] = float(peak_err.mean())
        out[f"peak_under_share_{tag}"] = float((peak_err < 0).mean())
        out[f"peak_hour_mae_{tag}"] = float(np.abs(ff.argmax(axis=1) - ph).mean())
        out[f"days_{tag}"] = int(good.sum())
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e_ghcnh")
    ap.add_argument("--group", default="b4")
    ap.add_argument("--model", default="final10s")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "b4_2023_2025" / "daypart.csv")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "daypart_43_bas.md")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "b4_2023_2025",
                    help="folder with rows.parquet of the same run: only the days it scored are used")
    a = ap.parse_args(argv)
    files = sorted(glob.glob(str(a.runs / f"{a.group}_*_hourly.parquet")))
    scored = pd.read_parquet(a.results / "rows.parquet")
    scored["day"] = scored["day"].astype(str)
    t = pd.DataFrame([ba_table(Path(f), a.model, scored) for f in files])
    t["set"] = np.where(t["ba"].isin(DEV_BAS), "development", "new")
    t["comparable"] = ~t["ba"].isin(NOT_COMPARABLE)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    t.to_csv(a.out, index=False, float_format="%.3f")

    def pair(r, key, fmt="{:.2f}"):
        return f"{fmt.format(r[key + '_recipe'])} / {fmt.format(r[key + '_df'])}"

    lines = ["# Errors by part of the day, per BA, 2023 to 2025: the recipe / the BA's forecast", "",
             f"From the hourly outputs of the 43-BA run (`{a.group}`, model `{a.model}`), on the days both scored. Each cell is "
             "recipe / `DF`. MAPE of a part of the day: mean absolute hourly error in percent of the actual over the hours of the "
             "part (local time: night 00-05, morning 06-10, midday 11-15, evening 16-21, late 22-23). Peak: signed error at the "
             "hour of the actual daily peak in percent of the peak (negative is under), the share of days under-forecast at the "
             "peak, and the mean absolute error of the forecast peak hour in hours. (a) marks the five BAs whose `DF` the EIA "
             "lists as not comparable with their demand.", "",
             "| BA | set | days | night | morning | midday | evening | late | peak error | days under at peak | peak hour error (h) |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for _, r in t.sort_values("ba").iterrows():
        label = r["ba"] + ("" if r["comparable"] else " (a)")
        lines.append(f"| {label} | {r['set']} | {r['days']} | {pair(r, 'night')} | {pair(r, 'morning')} | {pair(r, 'midday')} | "
                     f"{pair(r, 'evening')} | {pair(r, 'late')} | {pair(r, 'peak_err', '{:+.2f}')} | "
                     f"{pair(r, 'peak_under_share', '{:.0%}')} | {pair(r, 'peak_hour_mae', '{:.2f}')} |")
    comp = t[t["comparable"]]
    lines += ["", "## Means over the 38 comparable BAs (each BA counted once)", "",
              "| part | recipe | DF | BAs where the recipe is better |", "| --- | --- | --- | --- |"]
    for part in [*PARTS, "peak_err", "peak_hour_mae"]:
        rc, dc = comp[f"{part}_recipe"], comp[f"{part}_df"]
        better = int((rc.abs() < dc.abs()).sum())
        lines.append(f"| {part} | {rc.mean():.2f} | {dc.mean():.2f} | {better} of {len(comp)} |")
    a.doc.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[-9:]))
    print("wrote", a.doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
