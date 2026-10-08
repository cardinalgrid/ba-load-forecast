"""Map of the weather stations behind each BA of the 43-BA evaluation.

    python scripts/figure_station_map.py --states <cb_2023_us_state_20m.zip> --out docs/figures/station_map

The state outlines are the U.S. Census Bureau cartographic boundary file (2023, 1:20 million), read with pyshp. Each
dot is a weather station (coordinates from ``docs/stations_grid*.csv`` and ``docs/stations_b4.csv``): the eleven
development BAs use one to six stations each (``stations_multi.BA_STATIONS_MULTI``), the other 32 one station each
(``grid_sentinel.stations.BA_STATION``). Each BA's code is written at the mean position of its stations. Plain
longitude and latitude (equirectangular, latitude scaled by its cosine at 38 N). Writes PDF and PNG, 7.16 in wide.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import matplotlib
import numpy as np
import shapefile
from grid_sentinel.stations import BA_STATION

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ba_load_forecast.stations_multi import BA_STATIONS_MULTI  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BAS_43 = ("PJM MISO ERCO CISO SWPP NYIS ISNE TVA DUK BPAT FPL AECI AVA AZPS BANC CPLE CPLW EPE FMPP FPC GCPD IPCO JEA LDWP "
          "LGEE NEVP NWMT PACE PACW PGE PNM PSCO PSEI SC SCEG SCL SOCO SRP TEC TEPC TPWR WACM WALC").split()
DEV = set(BAS_43[:11])
SKIP_STATES = {"AK", "HI", "PR"}
LABEL_OFFSETS = {"PSEI/SCL/TPWR": (-3, 4, "right"), "GCPD": (-3, 4, "right"), "AVA": (3, 3, "left"), "TEC": (-3, 2, "right"),
                 "CPLE": (4, -2, "left"), "FMPP/FPC": (4, 3, "left")}


def stations() -> dict[str, tuple[float, float]]:
    out = {}
    for name in ("stations_grid.csv", "stations_grid_multi.csv", "stations_b4.csv"):
        for r in csv.DictReader(open(ROOT / "docs" / name)):
            out[r["icao"]] = (float(r["lon"]), float(r["lat"]))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--states", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "figures" / "station_map")
    a = ap.parse_args(argv)
    coords = stations()
    k = np.cos(np.radians(38.0))
    fig, ax = plt.subplots(figsize=(7.16, 4.0))
    sf = shapefile.Reader(str(a.states))
    fields = [f[0] for f in sf.fields[1:]]
    for rec, shp in zip(sf.records(), sf.shapes(), strict=True):
        if dict(zip(fields, rec, strict=True)).get("STUSPS") in SKIP_STATES:
            continue
        pts = np.asarray(shp.points)
        parts = list(shp.parts) + [len(pts)]
        for i in range(len(parts) - 1):
            p = pts[parts[i]:parts[i + 1]]
            ax.plot(p[:, 0] * k, p[:, 1], color="0.75", lw=0.4)
    missing = []
    shared: dict[str, list[str]] = {}                  # one-station BAs that share a station get one joint label
    for ba in BAS_43:
        icaos = BA_STATIONS_MULTI.get(ba) if ba in DEV else None
        icaos = list(icaos) if icaos else [BA_STATION[ba]]
        xy = [coords[i] for i in icaos if i in coords]
        missing += [i for i in icaos if i not in coords]
        if not xy:
            continue
        xy = np.asarray(xy)
        color = "C0" if ba in DEV else "0.35"
        ax.scatter(xy[:, 0] * k, xy[:, 1], s=9 if ba in DEV else 7, color=color, zorder=3, lw=0)
        if ba in DEV:
            ax.annotate(ba, (xy[:, 0].mean() * k, xy[:, 1].mean()), xytext=(2, 2), textcoords="offset points",
                        fontsize=5.5, color="C0", fontweight="bold")
        else:
            shared.setdefault(icaos[0], []).append(ba)
    for icao, bas in shared.items():
        x, y = coords[icao]
        label = "/".join(sorted(bas))
        dx, dy, ha = LABEL_OFFSETS.get(label, (2, 2, "left"))
        ax.annotate(label, (x * k, y), xytext=(dx, dy), textcoords="offset points", fontsize=5.5, color="0.15", ha=ha)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.scatter([], [], s=9, color="C0", label="development BAs (one to six stations)")
    ax.scatter([], [], s=7, color="0.35", label="other BAs (one station)")
    ax.legend(frameon=False, fontsize=6.5, loc="lower left")
    fig.tight_layout(pad=0.2)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(a.out.with_suffix(f".{ext}"), dpi=250)
    print("wrote", a.out.with_suffix(".pdf"), "| stations missing from the tables:", missing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
