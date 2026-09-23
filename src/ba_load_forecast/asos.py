"""Observed airport temperature after the ISD archive stops: the ASOS/METAR archive of the Iowa Environmental
Mesonet (Iowa State University), which mirrors the NWS observations of the same stations.

NOAA's ISD and ISD-Lite files for 2025 (``ncei.noaa.gov/pub/data/noaa``) end on 27 August 2025 for every station
used here and were last modified on 29 August 2025; the NCEI Access Data Service (``global-hourly``) ends on the
same day. From that day on the observed temperature comes from this archive, one routine hourly METAR per hour,
assigned to the nearest hour exactly as ISD-Lite does (an observation at 00:54 UTC is the 01:00 value). Over the
days both sources cover, the two agree to within 0.1 F (rounding of the METAR temperature). The supplement is only
used where the ISD series is missing; nothing before the cut of the archive changes.

``fetch_asos`` writes one CSV per station (``<ICAO>.csv``: ``valid_utc,temp_f``); ``read_asos`` returns the
hourly series in Fahrenheit indexed by tz-aware UTC hour.
"""

from __future__ import annotations

import time
from datetime import date
from pathlib import Path

import pandas as pd
import requests

IEM_URL = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
FIRST_MISSING_ISD = date(2025, 8, 27)      # first day the NOAA ISD archive does not cover


IEM_ALIASES = {"KPBI": "DJT"}     # West Palm Beach International (WBAN 12844) carries its 2025 identifier in IEM


def iem_id(icao: str) -> str:
    """IEM station ids drop the leading ``K`` of the ICAO code; a station whose identifier changed is mapped."""
    if icao in IEM_ALIASES:
        return IEM_ALIASES[icao]
    return icao[1:] if len(icao) == 4 and icao.startswith("K") else icao


def iem_request(icao: str | list[str], start: date, end: date) -> dict:
    """Query parameters of the IEM ASOS download service for one station or a list: routine hourly METARs, UTC,
    temperature in Fahrenheit, missing values as ``M``."""
    return {
        "station": [iem_id(i) for i in icao] if isinstance(icao, list) else iem_id(icao),
        "data": "tmpf", "tz": "Etc/UTC", "format": "onlycomma", "latlon": "no", "elev": "no",
        "missing": "M", "trace": "T", "direct": "no", "report_type": "2",
        "year1": start.year, "month1": start.month, "day1": start.day,
        "year2": end.year, "month2": end.month, "day2": end.day,
    }


def parse_iem(text: str) -> pd.DataFrame:
    """``station, valid_utc, temp_f`` from the IEM comma format; rows without a temperature are dropped."""
    from io import StringIO

    df = pd.read_csv(StringIO(text), dtype=str)
    if "valid" not in df.columns or "tmpf" not in df.columns:
        raise ValueError("not an IEM ASOS response: " + text[:80].replace("\n", " "))
    df = df[df["tmpf"].notna() & (df["tmpf"] != "M")]
    return pd.DataFrame({"station": df["station"].str.strip().to_numpy(), "valid_utc": pd.to_datetime(df["valid"], utc=True),
                         "temp_f": df["tmpf"].astype(float)})


def fetch_asos(icaos: list[str], start: date, end: date, out_dir: Path, attempts: int = 5) -> dict[str, Path]:
    """Download the stations in one request and write ``out_dir/<ICAO>.csv`` for each (overwriting). The service
    limits the request rate, so one request for all stations is used and a refusal is retried after a growing
    pause. Returns the file of every station the service returned rows for."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for attempt in range(attempts):
        r = requests.get(IEM_URL, params=iem_request(list(icaos), start, end), timeout=600)
        if r.status_code == 200 and "Too many requests" not in r.text[:200]:
            obs = parse_iem(r.text)
            written = {}
            for icao in icaos:
                part = obs[obs["station"] == iem_id(icao)]
                if part.empty:
                    continue
                dest = out_dir / f"{icao}.csv"
                part[["valid_utc", "temp_f"]].to_csv(dest, index=False)
                written[icao] = dest
            return written
        time.sleep(30.0 * (attempt + 1))
    raise RuntimeError(f"IEM refused the request {attempts} times")


def hourly_from_observations(obs: pd.DataFrame) -> pd.Series:
    """One value per UTC hour: the observation nearest to the top of the hour (ISD-Lite's convention), the last
    one when two are equally near."""
    if obs.empty:
        return pd.Series(dtype=float, index=pd.DatetimeIndex([], tz="UTC"))
    t = pd.to_datetime(obs["valid_utc"], utc=True)
    hour = t.dt.round("h")
    dist = (t - hour).abs()
    df = pd.DataFrame({"hour": hour, "dist": dist, "temp_f": obs["temp_f"].astype(float)})
    df = df.sort_values(["hour", "dist"], ascending=[True, False]).drop_duplicates("hour", keep="last")
    return pd.Series(df["temp_f"].to_numpy(), index=pd.DatetimeIndex(df["hour"]), name="temp_f").sort_index()


def read_asos(path: Path) -> pd.Series:
    """The hourly series of one station file written by ``fetch_asos``."""
    return hourly_from_observations(pd.read_csv(path, parse_dates=["valid_utc"]))


def asos_path(icao: str, asos_dir: Path | None) -> Path | None:
    if asos_dir is None:
        return None
    p = Path(asos_dir) / f"{icao}.csv"
    return p if p.exists() else None


__all__ = ["FIRST_MISSING_ISD", "IEM_URL", "asos_path", "fetch_asos", "hourly_from_observations", "iem_id", "iem_request",
           "parse_iem", "read_asos"]
