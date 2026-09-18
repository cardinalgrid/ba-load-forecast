"""Metrics of one day-ahead forecast against the load that occurred, for one BA and one day.

All errors are forecast minus actual. The peak metrics look at the hour of the actual peak: a
forecast that puts its own peak elsewhere is not rewarded for the height of that other peak.
"""

from __future__ import annotations

import numpy as np

MAX_MISSING_HOURS = 2

FIELDS = ("mape", "peak_err_pct", "peak_under_pct", "peak_hour_err", "actual_peak", "actual_mean", "n_missing", "skipped")


def day_metrics(forecast, actual) -> dict:
    """Metrics of a 24-hour forecast; ``skipped`` when the day cannot be scored.

    ``mape`` is the mean absolute percentage error over the hours with a positive actual;
    ``peak_err_pct`` is the forecast error at the hour of the actual peak, in percent of that peak;
    ``peak_under_pct`` is the negative part of it (0 when the forecast was not below the peak);
    ``peak_hour_err`` is the hour of the forecast peak minus the hour of the actual peak.
    A day is skipped when more than ``MAX_MISSING_HOURS`` actual hours are missing, when any forecast
    hour is missing, or when the arrays do not have 24 values.
    """
    f = np.asarray(forecast, dtype=float)
    a = np.asarray(actual, dtype=float)
    n_missing = int(np.isnan(a).sum()) if a.shape == (24,) else 24
    out = {k: np.nan for k in FIELDS}
    out["n_missing"] = n_missing
    out["skipped"] = True
    if f.shape != (24,) or a.shape != (24,) or n_missing > MAX_MISSING_HOURS or np.isnan(f).any():
        return out
    ok = ~np.isnan(a) & (a > 0)
    if not ok.any():
        return out
    peak_hour = int(np.nanargmax(a))
    peak = float(a[peak_hour])
    out["mape"] = float(np.mean(np.abs(f[ok] - a[ok]) / a[ok]) * 100.0)
    out["peak_err_pct"] = float((f[peak_hour] - peak) / peak * 100.0)
    out["peak_under_pct"] = float(min(0.0, out["peak_err_pct"]))
    out["peak_hour_err"] = int(np.argmax(f)) - peak_hour
    out["actual_peak"] = peak
    out["actual_mean"] = float(np.nanmean(a))
    out["skipped"] = False
    return out
