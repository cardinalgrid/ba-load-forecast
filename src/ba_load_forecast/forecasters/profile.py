"""The expected daily profile of Cardinal Grid Note 2, promoted to a forecaster.

Note 2 describes a day by its shape (the 24 hourly values divided by the day's mean) and its level (the
mean). The forecast for a target day is the median shape of its analogue days times the level of the
most recent ones. Analogues share the day type (workday, Saturday-like, Sunday-like, holidays mapped
by ``calendar_us``) and the temperature regime (heating below 59 F, cooling above 72 F, mild between,
by the daily mean); the regime of the target day comes from the forecast temperature, the regime of
past days from the observed temperature. Nothing after the cut-off is used: candidates are fully
known days from D-2 back, plus the same weeks of the previous year.
"""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import day_types

from ..information_set import InformationSet
from .base import ForecastError
from .naive import day_values

HEATING, MILD, COOLING = 0, 1, 2


def regime(mean_temp_f: float, heating_f: float = 59.0, cooling_f: float = 72.0) -> int | None:
    if np.isnan(mean_temp_f):
        return None
    if mean_temp_f < heating_f:
        return HEATING
    if mean_temp_f > cooling_f:
        return COOLING
    return MILD


class ProfileForecaster:
    def __init__(self, weeks: int = 4, analog_days: int = 21, level_days: int = 5, min_days: int = 3,
                 heating_f: float = 59.0, cooling_f: float = 72.0):
        self.weeks = weeks
        self.analog_days = analog_days
        self.level_days = level_days
        self.min_days = min_days
        self.heating_f = heating_f
        self.cooling_f = cooling_f
        self.name = "profile"

    def candidates(self, info: InformationSet) -> list[tuple[pd.Timestamp, np.ndarray, int | None, bool]]:
        """(day, 24 values, regime, recent) for every fully known day of the same type in the two windows."""
        recent = [info.day - timedelta(days=k) for k in range(2, 2 + 7 * self.weeks)]
        last_year = info.day - timedelta(days=365)
        previous = [last_year + timedelta(days=k) for k in range(-self.analog_days, self.analog_days + 1)]
        out = []
        for days, is_recent in ((recent, True), (previous, False)):
            types = day_types(np.array(days, dtype="datetime64[D]"))
            for d, t in zip(days, types, strict=True):
                if t != info.day_type:
                    continue
                v = day_values(info.load_history, d)
                if np.isnan(v).any() or v.mean() <= 0:
                    continue
                temp = day_values(info.temp_history_f, d)
                r = regime(float(np.nanmean(temp)) if np.isfinite(temp).sum() >= 18 else np.nan, self.heating_f, self.cooling_f)
                out.append((pd.Timestamp(d), v, r, is_recent))
        return out

    def predict(self, info: InformationSet) -> np.ndarray:
        target = regime(float(np.nanmean(info.temp_forecast_f)) if np.isfinite(info.temp_forecast_f).sum() >= 18 else np.nan,
                        self.heating_f, self.cooling_f)
        cands = self.candidates(info)
        pool = [c for c in cands if target is not None and c[2] == target]
        if len(pool) < self.min_days:
            pool = cands                       # fallback: ignore the regime
        if len(pool) < self.min_days:
            raise ForecastError(f"only {len(pool)} analogue days for {info.day}")
        shapes = np.vstack([v / v.mean() for _, v, _, _ in pool])
        shape = np.median(shapes, axis=0)
        recent = sorted((c for c in pool if c[3]), key=lambda c: c[0], reverse=True)[: self.level_days]
        if not recent:
            recent = sorted(pool, key=lambda c: c[0], reverse=True)[: self.level_days]
        level = float(np.median([v.mean() for _, v, _, _ in recent]))
        return shape * level
