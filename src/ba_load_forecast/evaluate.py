"""The evaluation harness: every forecaster, every BA, every day, scored like the BA's own forecast.

For each BA and target day the harness builds the information set once, hands a blind copy to every
forecaster, scores each forecast against the load that occurred, and scores the BA's own day-ahead
forecast (``DF``) with the same function under the model name ``DF``. The result is one row per
BA-day-model; nothing is aggregated here (see ``report``).
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from datetime import date

import numpy as np
import pandas as pd

from .forecasters.base import Forecaster, ForecastError, blind_copy
from .hrrr import days_between
from .information_set import InformationSet, Loader
from .metrics import FIELDS, QUANTILE_FIELDS, crps_from_quantiles, day_metrics, quantile_metrics

BA_MODEL = "DF"
COLUMNS = ["ba", "day", "model", *FIELDS, *QUANTILE_FIELDS, "temp_min_f", "day_type", "special_day", "run_init", "error"]


HOURS = [f"h{h:02d}" for h in range(24)]
HOURLY_COLUMNS = ["ba", "day", "model", *HOURS]
ACTUAL = "actual"


def hourly_row(info: InformationSet, model: str, values) -> dict:
    v = np.asarray(values, dtype=float)
    v = v if v.shape == (24,) else np.full(24, np.nan)
    return {"ba": info.ba, "day": info.day, "model": model, **dict(zip(HOURS, v, strict=True))}


def score_day(info: InformationSet, forecasters: Sequence[Forecaster], hourly: list | None = None) -> list[dict]:
    """The rows of one BA-day: one per forecaster plus the BA's own forecast.

    With ``hourly`` (a list), the 24 forecast values of every model, of ``DF`` and the outcome (model
    ``actual``) are appended to it, and the 5th and 95th percentiles of quantile forecasters as
    ``<name>_q05`` and ``<name>_q95``. A quantile forecaster that cannot give an interval yet (not enough
    known errors) is asked for its point forecast instead.
    """
    blind = blind_copy(info)
    temp_min = float(np.nanmin(info.temp_observed_f)) if np.isfinite(info.temp_observed_f).any() else np.nan
    common = {"ba": info.ba, "day": info.day, "day_type": info.day_type, "special_day": info.special_day,
              "run_init": None if info.run is None else f"{info.run[0]}T{info.run[1]:02d}", "temp_min_f": temp_min}
    empty_q = {k: np.nan for k in QUANTILE_FIELDS}
    rows = []
    scorable = info.actual_plausible and info.benchmark_plausible     # a fault in the outcome or in the published forecast: no one is scored
    actual = info.actual if scorable else np.full(24, np.nan)
    note = None if scorable else ("implausible actual" if not info.actual_plausible else "implausible DF")
    for fc in forecasters:
        error = note
        qm = empty_q
        q = None
        try:
            if hasattr(fc, "predict_quantiles"):
                try:
                    q = np.asarray(fc.predict_quantiles(blind), dtype=float)
                    forecast = q[q.shape[0] // 2]
                    qm = quantile_metrics(q, actual)
                    extra = getattr(fc, "last_extra", None)
                    if extra is not None and extra[0] == info.day:
                        levels = [*fc.extra_levels, 0.05, 0.5, 0.95]
                        allq = np.vstack([extra[1], q])
                        order = np.argsort(levels)
                        qm["crps"] = crps_from_quantiles(allq[order], np.asarray(levels)[order], actual)
                except ForecastError:
                    q = None
                    forecast = np.asarray(fc.predict(blind), dtype=float)
            else:
                forecast = np.asarray(fc.predict(blind), dtype=float)
        except ForecastError as e:
            forecast, error = np.full(24, np.nan), str(e)
        rows.append({**common, "model": fc.name, **day_metrics(forecast, actual), **qm, "error": error})
        if hourly is not None:
            hourly.append(hourly_row(info, fc.name, forecast))
            if q is not None:
                hourly.append(hourly_row(info, f"{fc.name}_q05", q[0]))
                hourly.append(hourly_row(info, f"{fc.name}_q95", q[-1]))
                extra = getattr(fc, "last_extra", None)
                if extra is not None and extra[0] == info.day:
                    for level, row in zip(fc.extra_levels, extra[1], strict=True):
                        hourly.append(hourly_row(info, f"{fc.name}_q{round(level * 100):02d}", row))
    rows.append({**common, "model": BA_MODEL, **day_metrics(info.ba_forecast, actual), **empty_q, "error": note})
    if hourly is not None:
        hourly.append(hourly_row(info, BA_MODEL, info.ba_forecast))
        hourly.append(hourly_row(info, ACTUAL, info.actual))
    return rows


def evaluate(loader: Loader, forecasters: Sequence[Forecaster], bas: Iterable[str], start: date, end: date,
             log: Callable[[str], None] | None = None, hourly: bool = False):
    """One row per BA-day-model for every day in ``[start, end]`` (``COLUMNS``).

    With ``hourly=True`` returns ``(rows, hourly_frame)``; the second frame has ``HOURLY_COLUMNS``.
    """
    rows = []
    store: list | None = [] if hourly else None
    for ba in bas:
        n = 0
        for day in days_between(start, end):
            rows.extend(score_day(loader.information_set(ba, day), forecasters, store))
            n += 1
        if log:
            log(f"{ba}: {n} days scored")
    frame = pd.DataFrame(rows, columns=COLUMNS)
    if hourly:
        return frame, pd.DataFrame(store, columns=HOURLY_COLUMNS)
    return frame
