"""Verify the extracted HRRR 2 m dew point against the airport observations at every station of the multi-station
table, the way ``verify_hrrr.py`` verifies the temperature.

Forecast minus observed, hour by hour, for the leads a day-ahead forecaster uses (17 to 45 h), by station,
lead, month, observed dew-point bin and local hour, and separately on the most humid afternoons of each station.
Observations: ISD-Lite (dew point column) until the archive stops, then the GHCNh and IEM supplements. Writes CSV
tables and figures to ``results/hrrr_dewpoint_verification`` and a summary to ``docs/hrrr_dewpoint_verification.md``.

    python scripts/verify_dewpoint.py --hrrr data/dewpoint --years 2021 2022 2023 2024 2025
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from grid_sentinel.weather import fetch_isd_lite

from ba_load_forecast.asos import read_asos
from ba_load_forecast.hrrr import COLUMNS
from ba_load_forecast.paths import DATA, ISD
from ba_load_forecast.stations_multi import station_table_for
from ba_load_forecast.weather_extra import read_isd_lite_field

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIELD = "dewpoint_f"
LEADS = (17, 45)
BINS = [-np.inf, 20, 40, 55, 65, np.inf]
BIN_LABELS = ["below 20 F", "20 to 40 F", "40 to 55 F", "55 to 65 F", "above 65 F"]
HUMID_AFTERNOONS = 30


def hrrr_rows(hrrr_dir: Path, icao: str, years: list[int]) -> pd.DataFrame:
    f = hrrr_dir / f"{icao}.parquet"
    d = pd.read_parquet(f) if f.exists() else pd.DataFrame(columns=COLUMNS)
    if d.empty:
        return d
    d = d[d["init_utc"].dt.year.isin(years)]
    return d[(d["lead_h"] >= LEADS[0]) & (d["lead_h"] <= LEADS[1])].copy()


def observed(st: pd.Series, icao: str, years: list[int], isd_dir: Path, supplements: list[Path]) -> pd.Series:
    """Observed dew point in Fahrenheit indexed by naive UTC hour: ISD-Lite, then the supplements where it is missing."""
    parts = []
    for y in years:
        p = fetch_isd_lite(st["usaf"], st["wban"], y, isd_dir)
        if p is not None:
            parts.append(read_isd_lite_field(p, FIELD))
    o = pd.concat(parts).sort_index() if parts else pd.Series(dtype=float, index=pd.DatetimeIndex([], tz="UTC"))
    o = o[~o.index.duplicated()]
    for folder in supplements:
        f = folder / f"{icao}.csv"
        if not f.exists():
            continue
        s = read_asos(f, FIELD)
        s = s[~s.index.isin(o.index)]
        o = pd.concat([o, s]).sort_index()
    o.index = pd.DatetimeIndex(o.index).tz_localize(None)
    return o


def markdown_table(t: pd.DataFrame) -> str:
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
    ap.add_argument("--hrrr", type=Path, default=DATA / "dewpoint")
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--supplements", type=Path, nargs="*", default=[DATA / "ghcnh", DATA / "asos"])
    ap.add_argument("--stations", type=Path, default=ROOT / "docs" / "stations_grid_multi.csv")
    ap.add_argument("--years", type=int, nargs="+", default=[2021, 2022, 2023, 2024, 2025])
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "hrrr_dewpoint_verification")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "hrrr_dewpoint_verification.md")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    figures = a.doc.parent / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    grid = pd.read_csv(a.stations)
    table = station_table_for(sorted(grid["icao"]), a.isd_dir).set_index("icao")
    joined = []
    for icao in grid["icao"]:
        fc = hrrr_rows(a.hrrr, icao, a.years)
        if fc.empty:
            print(f"{icao}: no forecast rows", flush=True)
            continue
        obs = observed(table.loc[icao], icao, a.years, a.isd_dir, a.supplements)
        fc["observed_f"] = obs.reindex(pd.DatetimeIndex(fc["valid_utc"])).to_numpy()
        fc = fc.dropna(subset=[FIELD, "observed_f"])
        fc["error"] = fc[FIELD].astype(float) - fc["observed_f"]
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

    # the most humid afternoons: per station, the days with the highest observed dew point between 12:00 and 18:00 local
    afternoon = d[(d["local_hour"] >= 12) & (d["local_hour"] <= 18)]
    daily_max = afternoon.groupby(["icao", "local_day"])["observed_f"].max().reset_index()
    humid = daily_max.sort_values(["icao", "observed_f"], ascending=[True, False]).groupby("icao").head(HUMID_AFTERNOONS)
    hum = afternoon.merge(humid[["icao", "local_day"]], on=["icao", "local_day"])
    humid_by_station = hum.groupby("icao").apply(summarize).round(2)
    humid_by_station["max_observed_f"] = humid.groupby("icao")["observed_f"].max().round(1)
    humid_all = summarize(hum).round(2)

    for name, t in [("by_station", by_station), ("by_lead", by_lead), ("by_month", by_month), ("by_bin", by_bin),
                    ("by_local_hour", by_hour), ("humid_afternoons_by_station", humid_by_station)]:
        t.to_csv(a.out / f"{name}.csv")

    fig, ax = plt.subplots(figsize=(3.5, 2.4))
    for h, g in by_lead.reset_index().groupby("init_hour"):
        ax.plot(g["lead_h"], g["mae_f"], label=f"{h:02d} UTC runs", lw=1.2)
    ax.set_xlabel("lead (h)")
    ax.set_ylabel("dew point MAE (°F)")
    ax.legend(fontsize=7, frameon=False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(figures / f"hrrr_dewpoint_mae_by_lead.{ext}", dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.16, 2.6))
    hb = humid_by_station.sort_values("bias_f")
    ax.bar(hb.index, hb["bias_f"], color=np.where(hb["bias_f"] > 0, "#c0392b", "#2c3e50"))
    ax.axhline(0, color="k", lw=0.6)
    ax.set_ylabel("dew point bias, humid afternoons (°F)")
    ax.tick_params(axis="x", labelrotation=90, labelsize=7)
    ax.tick_params(axis="y", labelsize=8)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(figures / f"hrrr_dewpoint_humid_bias.{ext}", dpi=200)
    plt.close(fig)

    years = ", ".join(str(y) for y in a.years)
    allsum = summarize(d).round(2)
    lines = [
        "# HRRR 2 m dew point against the airport observations",
        "",
        f"Forecast minus observed at the nearest HRRR grid cell of each station, {years}, leads {LEADS[0]} to {LEADS[1]} h "
        f"of the 12 and 06 UTC runs (the leads a day-ahead forecast issued at 9 a.m. local time uses). "
        f"{int(allsum['n'])} forecast-observation pairs at {d['icao'].nunique()} stations of the multi-station table. "
        "Observations are the hourly ISD-Lite dew point (tenths of a degree Celsius) and, after the ISD archive stops on "
        "27 August 2025, the GHCNh and IEM supplements at the same airports.",
        "",
        f"Overall: bias {allsum['bias_f']:+.2f} °F, MAE {allsum['mae_f']:.2f} °F, RMSE {allsum['rmse_f']:.2f} °F. "
        "For comparison, the 2 m temperature of the same runs and stations: bias -1.23 °F, MAE 3.12 °F "
        "(`docs/hrrr_verification.md`).",
        "",
        f"On the {HUMID_AFTERNOONS} most humid afternoons of each station (highest observed dew point between 12:00 and 18:00 "
        f"local time), hours 12:00 to 18:00: bias {humid_all['bias_f']:+.2f} °F, MAE {humid_all['mae_f']:.2f} °F, "
        f"{int(humid_all['n'])} pairs. A positive bias means the forecast was more humid than what occurred.",
        "",
        "![Dew point MAE by lead](figures/hrrr_dewpoint_mae_by_lead.png)",
        "",
        "![Dew point bias on humid afternoons by station](figures/hrrr_dewpoint_humid_bias.png)",
        "",
        "## By observed dew point",
        "",
        markdown_table(by_bin),
        "",
        "## By month",
        "",
        markdown_table(by_month),
        "",
        "## By local hour",
        "",
        markdown_table(by_hour),
        "",
        "## By station",
        "",
        markdown_table(by_station),
        "",
        "## Humid afternoons by station",
        "",
        markdown_table(humid_by_station),
        "",
        "Tables as CSV, including the error by lead, are in `results/hrrr_dewpoint_verification/`.",
        "",
    ]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print(f"written {a.doc}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
