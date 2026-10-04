"""Linear recalibration of a forecast, per hour of the day: undo the shrinkage toward the mean (A30b).

The members of the recipe are fitted by least squares on six years; at the top of their training range they answer
with too little load (phase R: with the observed temperature, every member under-forecasts the 30 largest peaks of
each BA by 3 to 5 %). The recipe's correction, the median of the recent relative errors on comparable days, moves the
whole curve up or down but cannot stretch it. ``LinearRecalibration`` regresses, for each hour of the day, the load
that occurred on the base forecast over the known days (D-2 and before, at most ``window_days``), and issues
``a_h + b_h * forecast_h``: a slope above one stretches the high days up and the low days down.

* ``by_regime``: the regression uses the known days of the target day's temperature regime (heating, mild, cooling
  by the forecast daily mean) when at least ``min_days`` of them exist, otherwise every known day.
* The slope is clipped to ``slope_bounds`` and the regression is centred on the mean forecast of the sample, so that
  a clipped slope still passes through the centre of the data; with fewer than ``min_days`` known days the base
  forecast is returned unchanged.

Nothing of the target day is used.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from ..information_set import InformationSet
from .base import Forecaster
from .profile import regime


class LinearRecalibration:
    def __init__(self, base: Forecaster, window_days: int = 365, min_days: int = 60, by_regime: bool = True,
                 slope_bounds: tuple[float, float] = (0.8, 1.5), name: str | None = None):
        self.base = base
        self.window_days = window_days
        self.min_days = min_days
        self.by_regime = by_regime
        self.slope_bounds = slope_bounds
        self.name = name or f"recal_{base.name}"
        self._stored: dict[date, np.ndarray] = {}
        self._regime: dict[date, int | None] = {}
        self.last_coefficients: tuple[np.ndarray, np.ndarray] | None = None

    @staticmethod
    def regime_of(info: InformationSet) -> int | None:
        t = np.asarray(info.temp_forecast_f, dtype=float)
        return regime(float(np.nanmean(t))) if np.isfinite(t).sum() >= 18 else None

    def known(self, info: InformationSet) -> list[date]:
        first = info.day - timedelta(days=self.window_days + 2)
        days = [d for d in self._stored if first <= d <= info.day - timedelta(days=2)]
        if self.by_regime:
            r = self._regime.get(info.day)
            same = [d for d in days if self._regime.get(d) == r]
            if r is not None and len(same) >= self.min_days:
                return same
        return days

    def coefficients(self, info: InformationSet) -> tuple[np.ndarray, np.ndarray] | None:
        days = self.known(info)
        if len(days) < self.min_days:
            return None
        f = np.vstack([self._stored[d] for d in days])
        rows = []
        for d in days:
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            rows.append(info.load_history.reindex(hours).to_numpy(dtype=float))
        y = np.vstack(rows)
        a = np.zeros(24)
        b = np.ones(24)
        for h in range(24):
            ok = np.isfinite(f[:, h]) & np.isfinite(y[:, h]) & (y[:, h] > 0)
            if ok.sum() < self.min_days:
                continue
            x, z = f[ok, h], y[ok, h]
            xm, zm = x.mean(), z.mean()
            var = ((x - xm) ** 2).sum()
            if var <= 0:
                continue
            slope = float(np.clip(((x - xm) * (z - zm)).sum() / var, *self.slope_bounds))
            b[h] = slope
            a[h] = zm - slope * xm
        return a, b

    def predict(self, info: InformationSet) -> np.ndarray:
        p = np.asarray(self.base.predict(info), dtype=float)
        self._regime[info.day] = self.regime_of(info)
        coef = self.coefficients(info)
        self._stored[info.day] = p.copy()
        for d in [d for d in self._stored if d < info.day - timedelta(days=self.window_days + 40)]:
            del self._stored[d]
            self._regime.pop(d, None)
        if coef is None:
            self.last_coefficients = None
            return p
        a, b = coef
        self.last_coefficients = (a, b)
        return a + b * p
