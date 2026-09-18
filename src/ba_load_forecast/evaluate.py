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
from .metrics import FIELDS, day_metrics

BA_MODEL = "DF"
COLUMNS = ["ba", "day", "model", *FIELDS, "day_type", "special_day", "run_init", "error"]


def score_day(info: InformationSet, forecasters: Sequence[Forecaster]) -> list[dict]:
    """The rows of one BA-day: one per forecaster plus the BA's own forecast."""
    blind = blind_copy(info)
    common = {"ba": info.ba, "day": info.day, "day_type": info.day_type, "special_day": info.special_day,
              "run_init": None if info.run is None else f"{info.run[0]}T{info.run[1]:02d}"}
    rows = []
    actual = info.actual if info.actual_plausible else np.full(24, np.nan)   # a gross fault in the outcome: no one is scored
    note = None if info.actual_plausible else "implausible actual"
    for fc in forecasters:
        error = note
        try:
            forecast = np.asarray(fc.predict(blind), dtype=float)
        except ForecastError as e:
            forecast, error = np.full(24, np.nan), str(e)
        rows.append({**common, "model": fc.name, **day_metrics(forecast, actual), "error": error})
    rows.append({**common, "model": BA_MODEL, **day_metrics(info.ba_forecast, actual), "error": note})
    return rows


def evaluate(loader: Loader, forecasters: Sequence[Forecaster], bas: Iterable[str], start: date, end: date,
             log: Callable[[str], None] | None = None) -> pd.DataFrame:
    """One row per BA-day-model for every day in ``[start, end]`` (``COLUMNS``)."""
    rows = []
    for ba in bas:
        n = 0
        for day in days_between(start, end):
            rows.extend(score_day(loader.information_set(ba, day), forecasters))
            n += 1
        if log:
            log(f"{ba}: {n} days scored")
    return pd.DataFrame(rows, columns=COLUMNS)
