"""Several weather stations per balancing authority.

One airport per BA (``grid_sentinel.stations.BA_STATION``) is what Note 2 and phase B used; a system the
size of CAISO or PJM is not one city. This table adds, for the development BAs, the main airports of
the largest load centres in each footprint. Station identifiers and coordinates come from the public
ISD history file, like the single-station table. Weights are equal; a population weighting is an
alternative that was not tested (see ``docs/methods.md``).
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import requests
from grid_sentinel.stations import BA_STATION, HISTORY_URL

BA_STATIONS_MULTI: dict[str, tuple[str, ...]] = {
    "PJM": ("KPHL", "KORD", "KDCA", "KPIT", "KCLE"),
    "MISO": ("KIND", "KMSP", "KDTW", "KSTL", "KMSY"),
    "ERCO": ("KDFW", "KIAH", "KSAT", "KAUS"),
    "CISO": ("KLAX", "KSFO", "KSMF", "KSAN", "KFAT"),
    "SWPP": ("KOKC", "KMCI", "KTUL", "KOMA"),
    "NYIS": ("KJFK", "KALB", "KBUF", "KSYR"),
    "ISNE": ("KBOS", "KBDL", "KPVD", "KPWM"),
    "TVA": ("KBNA", "KMEM", "KTYS", "KHSV"),
    "DUK": ("KCLT", "KRDU", "KGSO", "KGSP"),
    "BPAT": ("KPDX", "KSEA", "KGEG", "KBOI"),
}


def all_icaos() -> list[str]:
    """Every station in the multi-station table, the single-station ones included, without repeats."""
    out: list[str] = []
    for ba, icaos in BA_STATIONS_MULTI.items():
        for icao in (BA_STATION[ba], *icaos):
            if icao not in out:
                out.append(icao)
    return out


def station_table_for(icaos: list[str], isd_dir: Path, begin: int = 20150701, end: int = 20250101) -> pd.DataFrame:
    """``icao, usaf, wban, name, state, lat, lon`` for the stations asked, from the ISD history file.

    For an ICAO with several records, the one that spans ``begin`` to ``end`` and started earliest.
    """
    isd_dir = Path(isd_dir)
    hist = isd_dir / "isd-history.csv"
    if not hist.exists():
        isd_dir.mkdir(parents=True, exist_ok=True)
        r = requests.get(HISTORY_URL, timeout=120)
        r.raise_for_status()
        hist.write_bytes(r.content)
    h = pd.read_csv(hist, dtype=str)
    h = h[(h["CTRY"] == "US") & h["ICAO"].isin(set(icaos)) & (h["USAF"] != "999999")].copy()
    h["BEGIN"] = h["BEGIN"].astype(int)
    h["END"] = h["END"].astype(int)
    h = h[(h["BEGIN"] <= begin) & (h["END"] >= end)].sort_values("BEGIN").groupby("ICAO").head(1)
    out = h.rename(columns={"ICAO": "icao", "USAF": "usaf", "WBAN": "wban", "STATION NAME": "name", "STATE": "state",
                            "LAT": "lat", "LON": "lon"})[["icao", "usaf", "wban", "name", "state", "lat", "lon"]].copy()
    out["lat"] = out["lat"].astype(float)
    out["lon"] = out["lon"].astype(float)
    missing = sorted(set(icaos) - set(out["icao"]))
    if missing:
        raise ValueError(f"no usable ISD record for {missing}")
    return out.set_index("icao").loc[icaos].reset_index()
