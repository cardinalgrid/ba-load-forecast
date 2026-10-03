"""Typical daily load curve of every BA, with the spread of the days around it, as one HTML page.

    python scripts/load_profiles.py --runs <folder with b4_<BA>_hourly.parquet>

From the hourly actuals of the 43-BA run (2023 to 2025, each BA in its local time), on the days the run scored:
for each BA, season (all, winter = Dec-Feb, summer = Jun-Aug, shoulder = the rest) and day type (weekday, Saturday,
Sunday, holiday), the 10th, 25th, 50th, 75th and 90th percentiles of the load at each hour over the days of the group,
plus the number of days and the mean load. Writes ``results/b4_2023_2025/profiles.json`` and fills
``scripts/load_profiles_template.html`` into ``docs/load_profiles_43_bas.html``.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HOURS = [f"h{i:02d}" for i in range(24)]
QS = (0.10, 0.25, 0.50, 0.75, 0.90)
SEASONS = {"all": None, "winter": (12, 1, 2), "summer": (6, 7, 8), "shoulder": (3, 4, 5, 9, 10, 11)}
DAY_TYPES = ("weekday", "saturday", "sunday", "holiday")
NOT_COMPARABLE = ("AVA", "FPC", "LGEE", "PSEI", "TEPC")
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")
NAMES = {
    "AECI": "Associated Electric Cooperative", "AVA": "Avista", "AZPS": "Arizona Public Service", "BANC": "Balancing Authority of Northern California",
    "BPAT": "Bonneville Power Administration", "CISO": "California ISO", "CPLE": "Duke Energy Progress East", "CPLW": "Duke Energy Progress West",
    "DUK": "Duke Energy Carolinas", "EPE": "El Paso Electric", "ERCO": "ERCOT", "FMPP": "Florida Municipal Power Pool", "FPC": "Duke Energy Florida",
    "FPL": "Florida Power & Light", "GCPD": "Grant County PUD", "IPCO": "Idaho Power", "ISNE": "ISO New England", "JEA": "JEA (Jacksonville)",
    "LDWP": "Los Angeles Department of Water and Power", "LGEE": "Louisville Gas & Electric and Kentucky Utilities", "MISO": "Midcontinent ISO",
    "NEVP": "Nevada Power", "NWMT": "NorthWestern Energy (Montana)", "NYIS": "New York ISO", "PACE": "PacifiCorp East", "PACW": "PacifiCorp West",
    "PGE": "Portland General Electric", "PJM": "PJM Interconnection", "PNM": "Public Service Company of New Mexico", "PSCO": "Public Service Company of Colorado",
    "PSEI": "Puget Sound Energy", "SC": "South Carolina Public Service Authority", "SCEG": "Dominion Energy South Carolina", "SCL": "Seattle City Light",
    "SOCO": "Southern Company", "SRP": "Salt River Project", "SWPP": "Southwest Power Pool", "TEC": "Tampa Electric", "TEPC": "Tucson Electric Power",
    "TPWR": "Tacoma Power", "TVA": "Tennessee Valley Authority", "WACM": "WAPA Rocky Mountain", "WALC": "WAPA Desert Southwest",
}


def day_groups(rows: pd.DataFrame, ba: str) -> pd.DataFrame:
    """One row per scored day of ``ba``: day, month, day type."""
    r = rows[(rows["ba"] == ba) & (~rows["skipped"].astype(bool))]
    r = r.drop_duplicates("day")[["day", "day_type", "special_day"]].copy()
    r["day"] = r["day"].astype(str)
    r["month"] = pd.to_datetime(r["day"]).dt.month
    # special_day holds the day type the special day behaves like (1 Saturday-like, 2 Sunday-like); any value marks it
    holiday = r["special_day"].notna()
    r["kind"] = np.select([holiday, r["day_type"] == 1, r["day_type"] == 2], ["holiday", "saturday", "sunday"], "weekday")
    return r[["day", "month", "kind"]]


def profiles(path: Path, rows: pd.DataFrame) -> dict:
    t = pd.read_parquet(path)
    t["day"] = t["day"].astype(str)
    ba = t["ba"].iloc[0]
    act = t[t["model"] == "actual"].set_index("day")[HOURS]
    groups = day_groups(rows, ba)
    act = act.loc[act.index.intersection(groups["day"])]
    groups = groups.set_index("day").loc[act.index]
    a = act.to_numpy(dtype=float)
    ok = np.isfinite(a).all(axis=1) & (a > 0).all(axis=1)
    a, groups = a[ok], groups[ok]
    out = {"ba": ba, "name": NAMES.get(ba, ba), "set": "development" if ba in DEV_BAS else "new",
           "comparable": ba not in NOT_COMPARABLE, "mean_mw": float(a.mean()), "days": len(a), "groups": {}}
    for season, months in SEASONS.items():
        in_season = np.ones(len(a), dtype=bool) if months is None else groups["month"].isin(months).to_numpy()
        for kind in DAY_TYPES:
            sel = in_season & (groups["kind"] == kind).to_numpy()
            if sel.sum() < 3:
                continue
            q = np.quantile(a[sel], QS, axis=0)
            out["groups"][f"{season}|{kind}"] = {"n": int(sel.sum()), "mean": float(a[sel].mean()),
                                                 "q": [[round(float(v), 1) for v in row] for row in q]}
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e_ghcnh")
    ap.add_argument("--group", default="b4")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "b4_2023_2025")
    ap.add_argument("--template", type=Path, default=ROOT / "scripts" / "load_profiles_template.html")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "load_profiles_43_bas.html")
    a = ap.parse_args(argv)
    rows = pd.read_parquet(a.results / "rows.parquet")
    files = sorted(glob.glob(str(a.runs / f"{a.group}_*_hourly.parquet")))
    data = [profiles(Path(f), rows) for f in files]
    data.sort(key=lambda d: -d["mean_mw"])
    payload = {"period": "2023-01-01 to 2025-12-31", "quantiles": list(QS), "seasons": list(SEASONS), "day_types": list(DAY_TYPES), "bas": data}
    (a.results / "profiles.json").write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
    html = a.template.read_text(encoding="utf-8").replace("/*PROFILES_JSON*/null", json.dumps(payload, separators=(",", ":")))
    a.out.write_text(html, encoding="utf-8")
    print(len(data), "BAs;", sum(len(d["groups"]) for d in data), "groups; wrote", a.out, f"({a.out.stat().st_size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
