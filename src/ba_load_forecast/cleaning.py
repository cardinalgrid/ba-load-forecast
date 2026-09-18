"""The training history cleaned by grid-data-sentinel: flagged readings repaired, genuine extremes kept.

The control cleaning of the study removes gross faults only (``information_set.gross_guard``). This
option runs the Sentinel composite (TEDA on levels and differences, stuck values, calendar-aware profile,
cross-checks against the temperature) on one year of load, warmed up on the year before, and repairs the
flagged hours with the Sentinel's equivalent-days method. Detection never modifies the series; the
repair is a separate step and every repaired hour is listed in the audit.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from grid_sentinel import Repairer, Sentinel
from grid_sentinel.pandas import context_from, from_series, regularize, to_series


def sentinel_clean(load: pd.Series, temp: pd.Series | None = None, warm: pd.Series | None = None,
                   warm_temp: pd.Series | None = None) -> tuple[pd.Series, pd.DataFrame]:
    """``load`` with the hours the Sentinel flags repaired; the audit lists them (timestamp, reason, original).

    ``warm`` (and its temperature) is earlier history used only to warm the detector's state.
    """
    if load.dropna().empty:
        return load, pd.DataFrame(columns=["timestamp", "reason", "original", "repaired"])
    s = regularize(load.astype(float))
    det = Sentinel()
    if warm is not None and not warm.dropna().empty:
        w = regularize(warm.astype(float))
        wv, wt = from_series(w)
        wctx = context_from(temperature_f=warm_temp.reindex(w.index)) if warm_temp is not None else None
        det.fit(wv, wt, wctx)
    values, ts = from_series(s)
    ctx = context_from(temperature_f=temp.reindex(s.index)) if temp is not None else None
    res = det.predict(values, ts, ctx)
    flags = np.asarray(res.is_anomaly, dtype=bool) & ~np.isnan(values)
    fixed, _ = Repairer(method="equivalent_days").transform(values, ts, flags)
    cleaned = to_series(fixed, ts).reindex(load.index)
    reasons = np.asarray(res.reason)
    audit = pd.DataFrame({"timestamp": ts[flags], "reason": reasons[flags], "original": values[flags], "repaired": fixed[flags]})
    return cleaned, audit
