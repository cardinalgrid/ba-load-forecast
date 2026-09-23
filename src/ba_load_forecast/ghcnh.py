"""Observed airport temperature from NOAA's GHCNh (Global Historical Climatology Network hourly), the product
NOAA names as the successor of the Integrated Surface Database (ISD) whose files stop on 27 August 2025.

GHCNh carries the same METAR reports (``temperature_Report_Type`` FM15 routine and FM16 special, with the ISD
source and quality codes) and, for 2025, runs to 31 December. One file per station and year
(``.../hourly/access/by-year/<year>/psv/GHCNh_<GHCN_ID>_<year>.psv``, about 12 MB); the station list
(``ghcnh-station-list.csv``) maps the ICAO code to the GHCN id (``USW000`` + WBAN for the ASOS airports).

``fetch_ghcnh`` downloads one station-year, keeps the METAR temperature reports that passed quality control,
and writes the same ``<ICAO>.csv`` (``valid_utc,temp_f``) as ``asos.fetch_asos``, so the loader reads either
supplement with ``asos.read_asos`` and the nearest-hour convention of ISD-Lite.
"""

from __future__ import annotations

import io
import time
from pathlib import Path

import pandas as pd
import requests

GHCNH_BASE = "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly"
GHCNH_YEAR_URL = GHCNH_BASE + "/access/by-year/{year}/psv/GHCNh_{station}_{year}.psv"
GHCNH_STATIONS_URL = GHCNH_BASE + "/doc/ghcnh-station-list.csv"
METAR_REPORTS = ("FM15", "FM16")
FAILED_QC = {"2", "3", "6", "7"}            # ISD quality codes: suspect or erroneous, own or other source
COLUMNS = ["STATION", "DATE", "temperature", "temperature_Quality_Code", "temperature_Report_Type"]


def station_ids(icaos: list[str], cache: Path) -> dict[str, str]:
    """``{ICAO: GHCN_ID}`` from the station list (downloaded once into ``cache``)."""
    cache = Path(cache)
    if not cache.exists():
        r = requests.get(GHCNH_STATIONS_URL, timeout=180)
        r.raise_for_status()
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(r.content)
    t = pd.read_csv(cache, dtype=str)
    t = t[t["ICAO"].isin(set(icaos)) & (t["ISO_CODE"] == "US")]
    t = t[t["GHCN_ID"].str.startswith("USW")].drop_duplicates("ICAO")
    return dict(zip(t["ICAO"], t["GHCN_ID"], strict=True))


def parse_ghcnh(text: str) -> pd.DataFrame:
    """``valid_utc, temp_f`` from a GHCNh psv file: METAR reports (FM15, FM16) with a temperature (degrees Celsius
    in the file) that did not fail quality control."""
    df = pd.read_csv(io.StringIO(text), sep="|", usecols=COLUMNS, dtype=str, low_memory=False)
    ok = df["temperature_Report_Type"].isin(METAR_REPORTS) & df["temperature"].notna()
    ok &= ~df["temperature_Quality_Code"].fillna("").isin(FAILED_QC)
    df = df[ok]
    temp_c = pd.to_numeric(df["temperature"], errors="coerce")
    out = pd.DataFrame({"valid_utc": pd.to_datetime(df["DATE"], utc=True), "temp_f": temp_c * 9.0 / 5.0 + 32.0})
    return out[out["temp_f"].notna()].sort_values("valid_utc").reset_index(drop=True)


def fetch_ghcnh(icao: str, station: str, year: int, out_dir: Path, attempts: int = 3) -> Path | None:
    """Download one station-year and write ``out_dir/<ICAO>.csv``; ``None`` when NOAA has no file."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    url = GHCNH_YEAR_URL.format(year=year, station=station)
    for attempt in range(attempts):
        try:
            r = requests.get(url, timeout=600)
        except requests.RequestException:
            time.sleep(10 * (attempt + 1))
            continue
        if r.status_code == 404:
            return None
        if r.status_code == 200:
            dest = out_dir / f"{icao}.csv"
            parse_ghcnh(r.text).to_csv(dest, index=False)
            return dest
        time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"GHCNh: could not fetch {icao} ({station}) {year}")


__all__ = ["FAILED_QC", "GHCNH_STATIONS_URL", "GHCNH_YEAR_URL", "METAR_REPORTS", "fetch_ghcnh", "parse_ghcnh", "station_ids"]
