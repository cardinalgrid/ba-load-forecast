"""Humidity and wind: the observed fields beyond temperature, and the apparent-temperature formulas.

Observed fields come from the same ISD-Lite files as the temperature (dew point in column 6, wind speed in
column 9, both in tenths of a unit) and, after the ISD archive stops, from the same supplements (GHCNh, then the
IEM archive; ``valid_utc,temp_f,dewpoint_f,wind_ms``). Forecast fields come from the HRRR archive (``hrrr.FIELDS``:
``dewpoint_f``, ``wind_ms``).

Derived quantities, all on the hourly rows of a day:

* relative humidity from temperature and dew point (Magnus formula, over water);
* heat index (NWS, Rothfusz 1990 regression with the NWS adjustments), used where the temperature is at least
  80 F; below that it equals the temperature;
* wind chill (NWS 2001 formula) where the temperature is at most 50 F and the wind at least 3 mph; otherwise it
  equals the temperature;
* apparent temperature: the heat index where it applies, the wind chill where it applies, the temperature elsewhere.
"""

from __future__ import annotations

import gzip
import io
from pathlib import Path

import numpy as np
import pandas as pd

# ISD-Lite columns (0-based): 0 year, 1 month, 2 day, 3 hour, 4 air temperature (tenths C), 5 dew point (tenths C),
# 6 sea-level pressure, 7 wind direction, 8 wind speed (tenths m/s), 9 sky, 10 precipitation 1 h, 11 precipitation 6 h
ISD_LITE_FIELDS = {"temp_f": (4, "c"), "dewpoint_f": (5, "c"), "wind_ms": (8, "ms")}
WEATHER_FIELDS = ("dewpoint_f", "wind_ms")
WEATHER_COLUMNS = ["dewpoint", "dpd", "rh", "heat_index", "wind", "wind_chill"]
HUMIDITY_COLUMNS = ["dewpoint", "dpd", "rh", "heat_index"]
HUMIDITY_LINEAR = ["heat_excess", "rh"]         # the additive model's linear humidity terms: heat index above the temperature, RH
WIND_COLUMNS = ["wind", "wind_chill"]
KNOT_MS = 0.514444


def read_isd_lite_field(path: Path, field: str) -> pd.Series:
    """One field of an ISD-Lite file as a series indexed by tz-aware UTC hour: Fahrenheit for the temperatures,
    m/s for the wind; missing values (-9999) dropped."""
    col, unit = ISD_LITE_FIELDS[field]
    with gzip.open(path, "rt") as fh:
        txt = fh.read()
    df = pd.read_csv(io.StringIO(txt), sep=r"\s+", header=None, usecols=[0, 1, 2, 3, col],
                     names=["y", "m", "d", "h", "v"], engine="python")
    df = df[df["v"] != -9999]
    utc = pd.to_datetime({"year": df["y"], "month": df["m"], "day": df["d"], "hour": df["h"]}, utc=True)
    v = df["v"].to_numpy(dtype=float) / 10.0
    if unit == "c":
        v = v * 9.0 / 5.0 + 32.0
    return pd.Series(v, index=pd.DatetimeIndex(utc)).sort_index()


def relative_humidity(temp_f, dewpoint_f) -> np.ndarray:
    """Relative humidity in percent from temperature and dew point (Magnus, over water), clipped to 0 to 100."""
    t = (np.asarray(temp_f, dtype=float) - 32.0) * 5.0 / 9.0
    td = (np.asarray(dewpoint_f, dtype=float) - 32.0) * 5.0 / 9.0
    a, b = 17.625, 243.04
    rh = 100.0 * np.exp(a * td / (b + td) - a * t / (b + t))
    return np.clip(rh, 0.0, 100.0)


def heat_index_f(temp_f, rh) -> np.ndarray:
    """NWS heat index in Fahrenheit (Rothfusz regression with the NWS low-humidity and high-humidity adjustments);
    equal to the temperature below 80 F."""
    t = np.asarray(temp_f, dtype=float)
    r = np.asarray(rh, dtype=float)
    hi = (-42.379 + 2.04901523 * t + 10.14333127 * r - 0.22475541 * t * r - 6.83783e-3 * t * t
          - 5.481717e-2 * r * r + 1.22874e-3 * t * t * r + 8.5282e-4 * t * r * r - 1.99e-6 * t * t * r * r)
    low = (r < 13) & (t >= 80) & (t <= 112)
    hi = np.where(low, hi - ((13 - r) / 4) * np.sqrt(np.clip((17 - np.abs(t - 95.0)) / 17, 0.0, None)), hi)
    high = (r > 85) & (t >= 80) & (t <= 87)
    hi = np.where(high, hi + ((r - 85) / 10) * ((87 - t) / 5), hi)
    return np.where(t >= 80.0, hi, t)


def wind_chill_f(temp_f, wind_ms) -> np.ndarray:
    """NWS wind chill in Fahrenheit where the temperature is at most 50 F and the wind at least 3 mph; the
    temperature elsewhere."""
    t = np.asarray(temp_f, dtype=float)
    v = np.asarray(wind_ms, dtype=float) * 2.23694                       # mph
    with np.errstate(invalid="ignore"):
        wc = 35.74 + 0.6215 * t - 35.75 * np.power(np.maximum(v, 0.0), 0.16) + 0.4275 * t * np.power(np.maximum(v, 0.0), 0.16)
    return np.where((t <= 50.0) & (v >= 3.0), wc, t)


def apparent_temperature_f(temp_f, dewpoint_f, wind_ms) -> np.ndarray:
    """Heat index where it applies, wind chill where it applies, the temperature elsewhere. A missing dew point
    or wind leaves the temperature unchanged at that hour."""
    t = np.asarray(temp_f, dtype=float)
    td = np.asarray(dewpoint_f, dtype=float)
    w = np.asarray(wind_ms, dtype=float)
    out = t.copy()
    ok = np.isfinite(td)
    out[ok] = heat_index_f(t[ok], relative_humidity(t[ok], td[ok]))
    okw = np.isfinite(w)
    out[okw] = np.where(t[okw] <= 50.0, wind_chill_f(t[okw], w[okw]), out[okw])
    return out


def weather_columns(temp_f: np.ndarray, dewpoint_f: np.ndarray, wind_ms: np.ndarray) -> dict[str, np.ndarray]:
    """``WEATHER_COLUMNS`` for hourly arrays of temperature, dew point and wind."""
    t = np.asarray(temp_f, dtype=float)
    rh = relative_humidity(t, dewpoint_f)
    hi = np.where(np.isfinite(rh), heat_index_f(t, np.nan_to_num(rh)), t)    # no dew point: the index is the temperature
    return {"dewpoint": np.asarray(dewpoint_f, dtype=float), "dpd": t - np.asarray(dewpoint_f, dtype=float),
            "rh": rh, "heat_index": hi, "wind": np.asarray(wind_ms, dtype=float), "wind_chill": wind_chill_f(t, wind_ms)}


__all__ = ["HUMIDITY_COLUMNS", "HUMIDITY_LINEAR", "ISD_LITE_FIELDS", "KNOT_MS", "WEATHER_COLUMNS", "WEATHER_FIELDS", "WIND_COLUMNS",
           "apparent_temperature_f", "heat_index_f", "read_isd_lite_field", "relative_humidity", "weather_columns",
           "wind_chill_f"]
