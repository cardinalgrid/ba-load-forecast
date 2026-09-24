"""Verify the extracted HRRR 2 m temperature against the NOAA ISD-Lite observations at every station.

Forecast minus observed, hour by hour, for the leads a day-ahead forecaster uses (17 to 45 h), by station,
lead, month, temperature bin and, separately, on the coldest mornings of each station. Writes CSV tables
and figures to ``results/hrrr_verification`` and a summary to ``docs/hrrr_verification.md``.

    python scripts/verify_hrrr.py --hrrr data/hrrr --years 2024
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from grid_sentinel.events import EVENTS
from grid_sentinel.stations import station_table
from grid_sentinel.weather import fetch_isd_lite, read_isd_lite

from ba_load_forecast.hrrr import COLUMNS
from ba_load_forecast.paths import DATA, ISD

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
LEADS = (17, 45)
BINS = [-np.inf, 20, 32, 59, 72, np.inf]
BIN_LABELS = ["below 20 F", "20 to 32 F", "32 to 59 F", "59 to 72 F", "above 72 F"]
COLD_MORNINGS = 30


def hrrr_rows(hrrr_dir: Path, icao: str, years: list[int]) -> pd.DataFrame:
    """Rows of one station from the consolidated file or, before consolidation, from the run files."""
    f = hrrr_dir / f"{icao}.parquet"
    if f.exists():
        d = pd.read_parquet(f)
    else:
        files = [p for p in sorted((hrrr_dir / "runs").glob("*.parquet")) if int(p.name[:4]) in years]
        parts = [pd.read_parquet(p, filters=[("icao", "==", icao)]) for p in files]
        parts = [p for p in parts if len(p)]
        d = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=COLUMNS)
    d = d[d["init_utc"].dt.year.isin(years)]
    return d[(d["lead_h"] >= LEADS[0]) & (d["lead_h"] <= LEADS[1])].copy()


def observed(st: pd.Series, years: list[int], isd_dir: Path) -> pd.Series:
    parts = []
    for y in years:
        p = fetch_isd_lite(st["usaf"], st["wban"], y, isd_dir)
        if p is not None:
            parts.append(read_isd_lite(p))
    if not parts:
        return pd.Series(dtype=float)
    o = pd.concat(parts, ignore_index=True).drop_duplicates("utc").set_index("utc")["temp_c"].sort_index()
    o.index = pd.DatetimeIndex(o.index).tz_localize(None)
    return o * 9.0 / 5.0 + 32.0


def markdown_table(t: pd.DataFrame) -> str:
    """A GitHub-flavoured markdown table of a frame with a named index, without extra dependencies."""
    t = t.reset_index()
    cols = [str(c) for c in t.columns]
    rows = [" | ".join(cols), " | ".join("---" for _ in cols)]
    for r in t.itertuples(index=False):
        cells = []
        for v in r:
            if isinstance(v, float):
                cells.append(str(int(v)) if v.is_integer() else f"{v:.2f}")
            else:
                cells.append(str(v))
        rows.append(" | ".join(cells))
    return "\n".join(f"| {r} |" for r in rows)


def summarize(g: pd.DataFrame) -> pd.Series:
    e = g["error"]
    return pd.Series({"n": len(e), "bias_f": e.mean(), "mae_f": e.abs().mean(), "rmse_f": np.sqrt((e**2).mean())})


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hrrr", type=Path, default=DATA / "hrrr")
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--stations", type=Path, default=ROOT / "docs" / "stations_grid.csv")
    ap.add_argument("--years", type=int, nargs="+", default=[2024])
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "hrrr_verification")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "hrrr_verification.md")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    figures = a.doc.parent / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    grid = pd.read_csv(a.stations)
    table = station_table(a.isd_dir).set_index("icao")
    joined = []
    for icao in grid["icao"]:
        fc = hrrr_rows(a.hrrr, icao, a.years)
        if fc.empty:
            print(f"{icao}: no forecast rows", flush=True)
            continue
        obs = observed(table.loc[icao], a.years, a.isd_dir)
        fc["observed_f"] = obs.reindex(pd.DatetimeIndex(fc["valid_utc"])).to_numpy()
        fc = fc.dropna(subset=["temp_f", "observed_f"])
        fc["error"] = fc["temp_f"].astype(float) - fc["observed_f"]
        fc["local_hour"] = (fc["valid_utc"].dt.hour + round(float(grid.loc[grid["icao"] == icao, "lon"].iloc[0]) / 15.0)) % 24
        fc["local_day"] = (fc["valid_utc"] - pd.to_timedelta(fc["local_hour"], unit="h")).dt.normalize()
        joined.append(fc)
        print(f"{icao}: {len(fc)} pairs, bias {fc['error'].mean():+.2f} F, MAE {fc['error'].abs().mean():.2f} F", flush=True)
    if not joined:
        print("nothing to verify")
        return 1
    d = pd.concat(joined, ignore_index=True)
    d["init_hour"] = d["init_utc"].dt.hour
    d["month"] = d["valid_utc"].dt.month
    d["bin"] = pd.cut(d["observed_f"], BINS, labels=BIN_LABELS)

    by_station = d.groupby("icao").apply(summarize).round(2)
    by_lead = d.groupby(["init_hour", "lead_h"]).apply(summarize).round(2)
    by_month = d.groupby("month").apply(summarize).round(2)
    by_bin = d.groupby("bin", observed=True).apply(summarize).round(2)
    by_hour = d.groupby("local_hour").apply(summarize).round(2)

    # the coldest mornings: per station, the COLD_MORNINGS local days with the lowest observed minimum in 04-09 local
    morning = d[(d["local_hour"] >= 4) & (d["local_hour"] <= 9)]
    daily_min = morning.groupby(["icao", "local_day"])["observed_f"].min().reset_index()
    coldest = daily_min.sort_values(["icao", "observed_f"]).groupby("icao").head(COLD_MORNINGS)
    cold = morning.merge(coldest[["icao", "local_day"]], on=["icao", "local_day"])
    cold_by_station = cold.groupby("icao").apply(summarize).round(2)
    cold_by_station["min_observed_f"] = coldest.groupby("icao")["observed_f"].min().round(1)
    cold_all = summarize(cold).round(2)

    # the four winter events: every hour of the local calendar days of each event, all leads
    ev_parts = []
    for ev in EVENTS:
        w = d[(d["local_day"] >= pd.Timestamp(ev["start"])) & (d["local_day"] <= pd.Timestamp(ev["end"]))]
        if w.empty:
            continue
        s = w.groupby("icao").apply(summarize).round(2)
        s.insert(0, "event", ev["name"])
        s["min_observed_f"] = w.groupby("icao")["observed_f"].min().round(1)
        total = summarize(w).round(2)
        total["event"] = ev["name"]
        total["min_observed_f"] = round(float(w["observed_f"].min()), 1)
        s.loc["ALL"] = total
        ev_parts.append(s)
    events_by_station = pd.concat(ev_parts) if ev_parts else pd.DataFrame()

    for name, t in [("by_station", by_station), ("by_lead", by_lead), ("by_month", by_month), ("by_bin", by_bin),
                    ("by_local_hour", by_hour), ("cold_mornings_by_station", cold_by_station),
                    ("events_by_station", events_by_station)]:
        t.to_csv(a.out / f"{name}.csv")

    # figures
    fig, ax = plt.subplots(figsize=(3.5, 2.4))
    for h, g in by_lead.reset_index().groupby("init_hour"):
        ax.plot(g["lead_h"], g["mae_f"], label=f"{h:02d} UTC runs", lw=1.2)
    ax.set_xlabel("lead (h)")
    ax.set_ylabel("MAE (°F)")
    ax.legend(fontsize=7, frameon=False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(figures / f"hrrr_mae_by_lead.{ext}", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.16, 2.6))
    cb = cold_by_station.sort_values("bias_f")
    ax.bar(cb.index, cb["bias_f"], color=np.where(cb["bias_f"] > 0, "#c0392b", "#2c3e50"))
    ax.axhline(0, color="k", lw=0.6)
    ax.set_ylabel("bias on cold mornings (°F)")
    ax.tick_params(axis="x", labelrotation=90, labelsize=7)
    ax.tick_params(axis="y", labelsize=8)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(figures / f"hrrr_cold_morning_bias.{ext}", dpi=200)
    plt.close(fig)

    years = ", ".join(str(y) for y in a.years)
    allsum = summarize(d).round(2)
    lines = [
        "# HRRR 2 m temperature against ISD-Lite observations",
        "",
        f"Forecast minus observed at the nearest HRRR grid cell of each station, {years}, leads {LEADS[0]} to {LEADS[1]} h "
        f"of the 12 and 06 UTC runs (the leads a day-ahead forecast issued at 9 a.m. local time uses). "
        f"{int(allsum['n'])} forecast-observation pairs at {d['icao'].nunique()} stations. Observations are hourly "
        "ISD-Lite readings; a station reports to the nearest tenth of a degree Celsius.",
        "",
        f"Overall: bias {allsum['bias_f']:+.2f} °F, MAE {allsum['mae_f']:.2f} °F, RMSE {allsum['rmse_f']:.2f} °F.",
        "",
        f"On the {COLD_MORNINGS} coldest mornings of each station (lowest observed minimum between 04:00 and 09:00 local "
        f"time), hours 04:00 to 09:00: bias {cold_all['bias_f']:+.2f} °F, MAE {cold_all['mae_f']:.2f} °F, "
        f"{int(cold_all['n'])} pairs. A positive bias means the forecast was warmer than what occurred.",
        "",
        "![MAE by lead](figures/hrrr_mae_by_lead.png)",
        "",
        "![Bias on cold mornings by station](figures/hrrr_cold_morning_bias.png)",
        "",
        "## By observed temperature",
        "",
        markdown_table(by_bin),
        "",
        "## By month",
        "",
        markdown_table(by_month),
        "",
        "## By station",
        "",
        markdown_table(by_station),
        "",
        "## Cold mornings by station",
        "",
        markdown_table(cold_by_station),
        "",
        "## The four winter events",
        "",
        "All hours of the local calendar days of each event (the dates of `grid_sentinel.events`), every lead "
        "from 17 to 45 h; the last row of each event pools every station.",
        "",
        markdown_table(events_by_station) if len(events_by_station) else "(no event inside the years verified)",
        "",
        "Tables as CSV, including the error by lead and by local hour, are in `results/hrrr_verification/`.",
        "",
    ]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print(f"written {a.doc}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
