"""The sky as a day-ahead forecaster sees it: where the sun is, and how much cloud the HRRR run expects.

Behind-the-meter solar generation lowers the net load that EIA-930 reports, by an amount that follows the
sun's elevation and the cloud cover of the day. Neither is in the temperature. Two public inputs describe
it at the 9 a.m. cut-off:

* the cosine of the solar zenith angle at the BA's main station for each hour (pure geometry: latitude,
  longitude, day of the year, time), available for every hour of the history;
* the total cloud cover forecast by the HRRR run available at the cut-off (``cloud_pct`` of
  ``hrrr.FIELDS``), averaged over the BA's stations, available from 2 December 2020. For past days the
  value kept is the one that was forecast for them at their own cut-off, so that the model is trained on
  the same kind of input it will be given.

``sun_clear = sun * (1 - cloud / 100)`` is their product: a crude clear-sky index, left to the model to use.

The size of the effect grows with the installed PV capacity, which a forecaster knows: ``pv_capacity``
reads the monthly capacity behind each BA's load (``docs/pv_capacity_monthly.csv``, built by
``scripts/pv_capacity.py`` from Forms EIA-861M and EIA-860M) and ``PV_COLUMNS`` scale the geometry by it:
``pv_cap`` (MW), ``pv_clear = pv_cap * sun`` (a clear-sky output proxy, available for the whole history) and
``pv_est = pv_clear * (1 - cloud / 100)`` (missing where the cloud cover is).
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from .cutoff import lead_hours, run_for_day

SKY_COLUMNS = ["sun", "cloud", "sun_clear"]
PV_COLUMNS = ["pv_cap", "pv_clear", "pv_est"]
PV_TABLE = Path(__file__).resolve().parents[2] / "docs" / "pv_capacity_monthly.csv"


def pv_capacity(path: Path | None = None) -> dict[str, pd.Series]:
    """``{ba: monthly total PV capacity in MW}`` from the table written by ``scripts/pv_capacity.py``."""
    t = pd.read_csv(path or PV_TABLE)
    t["month"] = pd.to_datetime(t["month"])
    return {ba: g.set_index("month")["total_mw"].sort_index() for ba, g in t.groupby("ba")}


def cos_zenith(utc, lat: float, lon: float) -> np.ndarray:
    """Cosine of the solar zenith angle (0 at night) for UTC instants (hour beginning; evaluated at mid-hour)."""
    t = pd.DatetimeIndex(utc) + pd.Timedelta(minutes=30)
    n = t.dayofyear.to_numpy(dtype=float)
    decl = np.radians(23.44) * np.sin(2 * np.pi * (284 + n) / 365.0)
    b = 2 * np.pi * (n - 81) / 364.0
    eot_min = 9.87 * np.sin(2 * b) - 7.53 * np.cos(b) - 1.5 * np.sin(b)             # equation of time
    solar_h = t.hour.to_numpy() + t.minute.to_numpy() / 60.0 + lon / 15.0 + eot_min / 60.0
    omega = np.radians(15.0 * (solar_h - 12.0))
    phi = np.radians(lat)
    return np.maximum(0.0, np.sin(phi) * np.sin(decl) + np.cos(phi) * np.cos(decl) * np.cos(omega))


def run_table(rows: pd.DataFrame, field: str) -> tuple[dict, np.ndarray]:
    """``{init timestamp: row}`` and the ``(n_runs, 48)`` array of a station's forecasts by lead (1 h first)."""
    if rows.empty:
        return {}, np.empty((0, 48))
    wide = rows.pivot_table(index="init_utc", columns="lead_h", values=field, aggfunc="first").reindex(columns=range(1, 49))
    return {pd.Timestamp(i): k for k, i in enumerate(wide.index)}, wide.to_numpy(dtype=float)


def forecast_as_seen(tables: list[tuple[dict, np.ndarray]], days: list[date], offset_of_day, init_hours) -> pd.Series:
    """For every local hour of ``days``, the value forecast by the run available at that day's cut-off, averaged
    over the stations (``tables``). ``offset_of_day(day)`` gives the UTC offset (hours behind UTC)."""
    index, values = [], []
    for d in days:
        off = offset_of_day(d)
        hours = pd.date_range(datetime(d.year, d.month, d.day), periods=24, freq="h")
        index.extend(hours)
        if np.isnan(off):
            values.extend([np.nan] * 24)
            continue
        run = run_for_day(d, float(off), init_hours)
        init = pd.Timestamp(datetime(run[0].year, run[0].month, run[0].day, run[1]))
        leads = lead_hours(d, float(off), run)
        per_station = []
        for by_init, arr in tables:
            k = by_init.get(init)
            if k is None:
                continue
            ok = (leads >= 1) & (leads <= arr.shape[1])
            v = np.full(24, np.nan)
            v[ok] = arr[k, leads[ok] - 1]
            per_station.append(v)
        values.extend(np.nanmean(np.vstack(per_station), axis=0) if per_station else [np.nan] * 24)
    return pd.Series(values, index=pd.DatetimeIndex(index), dtype=float)


def sky_frame(local_hours: pd.DatetimeIndex, offsets: pd.Series, lat: float, lon: float, cloud: pd.Series | None,
              pv: pd.Series | None = None) -> pd.DataFrame:
    """``SKY_COLUMNS`` for the local hours given (``offsets``: hours behind UTC per local hour), plus ``PV_COLUMNS``
    when ``pv`` (monthly installed capacity, MW) is given: the month's value is held through the month."""
    off = offsets.reindex(local_hours)
    off = off.fillna(off.median() if off.notna().any() else 0.0).to_numpy(dtype=float)
    utc = local_hours.to_numpy() + (off * 3600.0 * 1e9).astype("timedelta64[ns]")
    sun = cos_zenith(utc, lat, lon)
    out = pd.DataFrame({"sun": sun}, index=local_hours)
    out["cloud"] = cloud.reindex(local_hours).to_numpy(dtype=float) if cloud is not None else np.nan
    out["sun_clear"] = out["sun"] * (1.0 - out["cloud"] / 100.0)
    if pv is not None:
        months = local_hours.to_period("M").to_timestamp()
        cap = pv.reindex(pv.index.union(pd.DatetimeIndex(months.unique()))).ffill().bfill()
        out["pv_cap"] = cap.reindex(months).to_numpy(dtype=float)
        out["pv_clear"] = out["pv_cap"] * out["sun"]
        out["pv_est"] = out["pv_clear"] * (1.0 - out["cloud"] / 100.0)
    return out


def all_days(first: date, last: date) -> list[date]:
    return [first + timedelta(days=k) for k in range((last - first).days + 1)]
