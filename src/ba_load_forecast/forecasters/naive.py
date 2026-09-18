"""Floors: forecasts that use the load history and nothing else.

They exist so that every other model can be measured against what costs nothing. All three respect
the cut-off: the last known hour is 08:00 of the day before the target day, so "yesterday" is not
fully known and the floors are built from the hours that are.
"""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types

from ..information_set import InformationSet
from .base import ForecastError


def day_values(history: pd.Series, day) -> np.ndarray:
    """The 24 hourly values of one local calendar day from the history (NaN where absent)."""
    hours = pd.date_range(pd.Timestamp(day), periods=24, freq="h")
    return history.reindex(hours).to_numpy(dtype=float)


class LastKnownDay:
    """The last 24 known hours (09:00 of D-2 to 08:00 of D-1), each placed at its own hour of the day."""

    name = "last_known_day"

    def predict(self, info: InformationSet) -> np.ndarray:
        cutoff = pd.Timestamp(info.cutoff)
        hours = pd.date_range(cutoff - pd.Timedelta(hours=23), cutoff, freq="h")
        values = info.load_history.reindex(hours)
        out = np.full(24, np.nan)
        for ts, v in values.items():
            out[ts.hour] = v
        return out


class SameWeekdayLastWeek:
    """The same weekday of the previous week (D-7), entirely known at the cut-off."""

    name = "same_weekday_last_week"

    def predict(self, info: InformationSet) -> np.ndarray:
        return day_values(info.load_history, info.day - timedelta(days=7))


class SameTypeMean:
    """Hour-by-hour mean of the fully known days of the same day type in the last ``weeks`` weeks (D-2 back)."""

    def __init__(self, weeks: int = 2):
        self.weeks = weeks
        self.name = f"same_type_mean_{weeks}w"

    def predict(self, info: InformationSet) -> np.ndarray:
        days = [info.day - timedelta(days=k) for k in range(2, 2 + 7 * self.weeks)]
        types = day_types(np.array(days, dtype="datetime64[D]"))
        stack = [day_values(info.load_history, d) for d, t in zip(days, types, strict=True) if t == info.day_type]
        stack = [v for v in stack if not np.isnan(v).any()]
        if not stack:
            raise ForecastError(f"no complete day of type {info.day_type} in the last {self.weeks} weeks")
        return np.mean(np.vstack(stack), axis=0)
