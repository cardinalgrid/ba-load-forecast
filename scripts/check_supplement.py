"""Cross-check of the observed-temperature supplements: GHCNh (NOAA, the successor of ISD) against the Iowa
Environmental Mesonet ASOS archive over the period both cover, and each against ISD-Lite over the days the ISD
archive still has (up to 27 August 2025).

    python scripts/check_supplement.py [--ghcnh data/ghcnh] [--asos data/asos] [--isd ../notes/03-daily-load-profiles/data/isd]
                                       [--start 2025-08-27] [--end 2025-12-31] [--doc docs/supplement_check.md]

Per station: hours in each source, hours in common, mean and maximum absolute difference in Fahrenheit, and the
number of hours that differ by more than 1 F. The METAR temperature is reported in whole degrees Celsius by
some sources and in tenths by others, so differences up to 0.1 F are rounding.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from ba_load_forecast.asos import read_asos
from ba_load_forecast.paths import DATA, ISD
from ba_load_forecast.report import markdown_table
from ba_load_forecast.stations_multi import BA_STATIONS_MULTI, station_table_for

ROOT = Path(__file__).resolve().parents[1]


def isd_lite_hourly(path: Path) -> pd.Series:
    from grid_sentinel.weather import read_isd_lite

    if not path.exists():
        return pd.Series(dtype=float)
    obs = read_isd_lite(path).drop_duplicates("utc").set_index("utc")["temp_c"].sort_index()
    return obs * 9.0 / 5.0 + 32.0


def compare(a: pd.Series, b: pd.Series, start, end) -> dict:
    j = pd.concat([a.rename("a"), b.rename("b")], axis=1).loc[start:end].dropna()
    d = (j["a"] - j["b"]).abs()
    return {"hours_a": int(a.loc[start:end].notna().sum()), "hours_b": int(b.loc[start:end].notna().sum()), "common": len(j),
            "mean_abs_diff_f": float(d.mean()) if len(j) else np.nan, "max_abs_diff_f": float(d.max()) if len(j) else np.nan,
            "hours_over_1f": int((d > 1.0).sum())}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ghcnh", type=Path, default=DATA / "ghcnh")
    ap.add_argument("--asos", type=Path, default=DATA / "asos")
    ap.add_argument("--isd", type=Path, default=ISD)
    ap.add_argument("--start", default="2025-08-27")
    ap.add_argument("--end", default="2025-12-31")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "supplement_check.md")
    a = ap.parse_args(argv)
    icaos = sorted({i for v in BA_STATIONS_MULTI.values() for i in v})
    table = station_table_for(icaos, a.isd).set_index("icao")
    start, end = pd.Timestamp(a.start, tz="UTC"), pd.Timestamp(a.end, tz="UTC") + pd.Timedelta(hours=23)
    rows_gi, rows_isd = [], []
    for icao in icaos:
        g = read_asos(a.ghcnh / f"{icao}.csv") if (a.ghcnh / f"{icao}.csv").exists() else pd.Series(dtype=float)
        m = read_asos(a.asos / f"{icao}.csv") if (a.asos / f"{icao}.csv").exists() else pd.Series(dtype=float)
        if len(g) and len(m):
            rows_gi.append({"station": icao, **compare(g, m, start, end)})
        st = table.loc[icao]
        isd = isd_lite_hourly(a.isd / f"{st['usaf']}-{st['wban']}-2025.gz")
        if len(isd):
            e = isd.index.max()
            s0 = e - pd.Timedelta(days=30)
            r = {"station": icao, "isd_last": str(e)[:13]}
            if len(g):
                r.update({f"ghcnh_{k}": v for k, v in compare(isd, g, s0, e).items() if k in ("common", "mean_abs_diff_f", "max_abs_diff_f")})
            if len(m):
                r.update({f"asos_{k}": v for k, v in compare(isd, m, s0, e).items() if k in ("common", "mean_abs_diff_f", "max_abs_diff_f")})
            rows_isd.append(r)
    t1 = pd.DataFrame(rows_gi).set_index("station")
    t2 = pd.DataFrame(rows_isd).set_index("station")
    lines = ["# Observed-temperature supplements: GHCNh against the IEM ASOS archive, and both against ISD-Lite", "",
             f"Period of the GHCNh-IEM comparison: {a.start} to {a.end} (UTC hours). Hourly values are the report nearest to the "
             "top of the hour, the ISD-Lite convention. Differences up to 0.1 F are rounding (whole degrees Celsius in one source, "
             "tenths in the other).", "", "## GHCNh against IEM ASOS", "", markdown_table(t1, 2), "",
             f"All stations: {len(t1)}; hours in common {int(t1['common'].sum())}; mean absolute difference "
             f"{float(np.average(t1['mean_abs_diff_f'], weights=t1['common'])):.3f} F; hours over 1 F {int(t1['hours_over_1f'].sum())}.",
             "", "## Each supplement against ISD-Lite over the last 30 days the ISD archive covers", "", markdown_table(t2, 2), ""]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[-6:-3]))
    print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
