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
    # Pensacola is in the list because the former Gulf Power load (north-west Florida) joins the FPL series
    # in July 2022, a step of about 10 % that is visible against the other Florida BAs.
    "FPL": ("KMIA", "KPBI", "KMLB", "KRSW", "KSRQ", "KPNS"),
}

# Phase U (ideas A28 and A32): a candidate table for twelve BAs evaluated so far on one station, the ones where the recipe
# trails the published forecast or under-forecasts the daily peak most often, and those whose footprint one airport
# describes badly. The BA's own station comes first; the others are the main airports of its other load centres.
# Used only with ``Loader(stations="extra")`` until a run on the development period decides.
BA_STATIONS_EXTRA: dict[str, tuple[str, ...]] = {
    "LDWP": ("KBUR", "KVNY"),                    # the San Fernando Valley, inland of the coastal KLAX (KCQT, downtown: ISD hours missing outside 2021)
    "WALC": ("KNYL", "KIGM", "KBLH"),            # Yuma, Kingman, Blythe
    "NEVP": ("KVGT", "KHND"),                    # North Las Vegas, Henderson
    "PSCO": ("KCOS", "KGJT", "KPUB"),            # Colorado Springs, Grand Junction, Pueblo (KBJC, Broomfield: half the ISD hours missing)
    "WACM": ("KCYS", "KCPR", "KGXY"),            # Cheyenne, Casper, Greeley
    "PACE": ("KOGD", "KPVU", "KIDA", "KRKS"),    # Ogden, Provo, Idaho Falls, Rock Springs
    "NWMT": ("KGTF", "KMSO", "KHLN", "KBZN"),    # Great Falls, Missoula, Helena, Bozeman
    "AECI": ("KCOU", "KJLN", "KIRK", "KPOF"),    # Columbia, Joplin, Kirksville, Poplar Bluff
    "SOCO": ("KBHM", "KMOB", "KSAV", "KMCN", "KMGM"),  # Birmingham, Mobile, Savannah, Macon, Montgomery
    "PGE": ("KSLE", "KHIO"),                     # Salem, Hillsboro
    "BANC": ("KSAC", "KRDD"),                    # Sacramento Executive, Redding
    "TPWR": ("KTIW", "KTCM"),                    # Tacoma Narrows, McChord
}


def extra_icaos() -> list[str]:
    """The stations of ``BA_STATIONS_EXTRA`` that no other table has, in order and without repeats."""
    known = set(all_icaos()) | set(BA_STATION.values())
    out: list[str] = []
    for icaos in BA_STATIONS_EXTRA.values():
        for icao in icaos:
            if icao not in known and icao not in out:
                out.append(icao)
    return out


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
