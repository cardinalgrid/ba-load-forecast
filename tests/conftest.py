"""Synthetic public data in the layouts the loaders expect: tidy EIA-930, ISD-Lite and the HRRR extraction."""

import gzip

import numpy as np
import pandas as pd
import pytest

HISTORY = (
    "USAF,WBAN,STATION NAME,CTRY,STATE,ICAO,LAT,LON,ELEV(M),BEGIN,END\n"
    "724080,13739,PHILADELPHIA INTL,US,PA,KPHL,39.873,-75.227,2.0,19410101,20261231\n"
)


def demand_value(ts: pd.Timestamp) -> float:
    """A load that identifies its hour: day-of-year in the hundreds, hour in the units."""
    return 10_000.0 + 100.0 * ts.dayofyear + ts.hour


def observed_temp_c(utc: pd.Timestamp) -> float:
    """A temperature, exact in tenths of a degree, that identifies its UTC day and hour."""
    return float(10 * utc.day + utc.hour / 10.0)


def write_tidy(tidy_dir, ba, start, end, offset_h=5, drop=()):
    """Hourly rows from ``start`` to ``end`` (local hour beginning) into the half-year parquet files."""
    tidy_dir.mkdir(parents=True, exist_ok=True)
    hours = pd.date_range(start, end, freq="h")
    hours = hours[~hours.isin([pd.Timestamp(d) for d in drop])]
    local_end = hours + pd.Timedelta(hours=1)
    df = pd.DataFrame({
        "ba": ba, "region": "MIDA", "date": local_end.normalize(), "hour": local_end.hour, "local_end": local_end,
        "utc_end": (local_end + pd.Timedelta(hours=offset_h)).tz_localize("UTC"),
        "forecast": [demand_value(h) + 10.0 for h in hours], "demand": [demand_value(h) for h in hours],
        "demand_adjusted": 0.0, "demand_imputed": False,
    })
    for (year, half), part in df.groupby([df["local_end"].dt.year, np.where(df["local_end"].dt.month <= 6, "H1", "H2")]):
        f = tidy_dir / f"{year}{half}.parquet"
        rows = pd.concat([pd.read_parquet(f), part]) if f.exists() else part
        rows.to_parquet(f, index=False)


def write_isd(isd_dir, usaf, wban, start_utc, end_utc):
    isd_dir.mkdir(parents=True, exist_ok=True)
    (isd_dir / "isd-history.csv").write_text(HISTORY)
    hours = pd.date_range(start_utc, end_utc, freq="h")
    for year, part in hours.groupby(hours.year).items():
        lines = [f"{t.year} {t.month:02d} {t.day:02d} {t.hour:02d} {round(observed_temp_c(t) * 10):6d} -9999 -9999 -9999 -9999 -9999 -9999 -9999"
                 for t in part]
        with gzip.open(isd_dir / f"{usaf}-{wban}-{year}.gz", "wt") as fh:
            fh.write("\n".join(lines) + "\n")


def write_hrrr(hrrr_dir, icao, init, n_lead=48):
    hrrr_dir.mkdir(parents=True, exist_ok=True)
    init = pd.Timestamp(init)
    lead = np.arange(1, n_lead + 1)
    pd.DataFrame({"icao": icao, "init_utc": init, "lead_h": lead.astype("int16"),
                  "valid_utc": init + pd.to_timedelta(lead, unit="h"),
                  "temp_f": (100.0 + lead).astype("float32")}).to_parquet(hrrr_dir / f"{icao}.parquet", index=False)


@pytest.fixture
def public_data(tmp_path):
    """PJM/KPHL from 2023-12-01 to 2024-01-20 (Eastern standard time), 05:00 of 2024-01-16 missing,
    and one HRRR run (2024-01-15 12Z, temp_f = 100 + lead)."""
    tidy = tmp_path / "tidy"
    isd = tmp_path / "isd"
    hrrr = tmp_path / "hrrr"
    write_tidy(tidy, "PJM", "2023-12-01 00:00", "2024-01-20 23:00", offset_h=5, drop=["2024-01-16 05:00"])
    write_isd(isd, "724080", "13739", "2023-11-30 00:00", "2024-01-22 00:00")
    write_hrrr(hrrr, "KPHL", "2024-01-15 12:00")
    return tidy, isd, hrrr
