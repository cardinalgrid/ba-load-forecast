"""Ensembles: the mean of several forecasters, simple or weighted by their recent error.

The members are called on the same blind information set; a member that cannot forecast a day is left
out of that day's mean. With ``weighting="recent"`` each member's weight is the inverse of its MAPE over
the last ``window_days`` days whose load is already known at the cut-off (day D-2 and before), measured
on the forecasts the ensemble itself stored for those days; a member without such a record gets the
mean weight of the others. Nothing of the target day is used.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from ..information_set import InformationSet
from .base import Forecaster, ForecastError


class Ensemble:
    def __init__(self, members: list[Forecaster], weighting: str = "mean", window_days: int = 30,
                 min_days: int = 5, name: str | None = None):
        if weighting not in ("mean", "recent"):
            raise ValueError("weighting must be 'mean' or 'recent'")
        self.members = list(members)
        self.weighting = weighting
        self.window_days = window_days
        self.min_days = min_days
        self.name = name or f"ens_{weighting}_" + "+".join(m.name for m in members)
        self._stored: dict[date, dict[str, np.ndarray]] = {}
        self.last_weights: dict[str, float] = {}

    def recent_mape(self, info: InformationSet) -> dict[str, float]:
        """MAPE of each member over the stored forecasts of the last ``window_days`` known days."""
        first = info.day - timedelta(days=self.window_days + 2)
        errors: dict[str, list[float]] = {m.name: [] for m in self.members}
        for d, preds in self._stored.items():
            if d < first or d > info.day - timedelta(days=2):
                continue
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            ok = ~np.isnan(actual) & (actual > 0)
            if ok.sum() < 20:
                continue
            for name, p in preds.items():
                if name in errors:
                    errors[name].append(float(np.mean(np.abs(p[ok] - actual[ok]) / actual[ok])))
        return {n: float(np.mean(e)) for n, e in errors.items() if len(e) >= self.min_days}

    def weights(self, info: InformationSet, available: list[str]) -> dict[str, float]:
        if self.weighting == "mean" or len(available) == 1:
            return {n: 1.0 / len(available) for n in available}
        mape = self.recent_mape(info)
        raw = {n: 1.0 / mape[n] for n in available if n in mape and mape[n] > 0}
        if not raw:
            return {n: 1.0 / len(available) for n in available}
        fill = float(np.mean(list(raw.values())))
        w = {n: raw.get(n, fill) for n in available}
        total = sum(w.values())
        return {n: v / total for n, v in w.items()}

    def predict(self, info: InformationSet) -> np.ndarray:
        preds: dict[str, np.ndarray] = {}
        for m in self.members:
            try:
                preds[m.name] = np.asarray(m.predict(info), dtype=float)
            except ForecastError:
                continue
        if not preds:
            raise ForecastError("no member could forecast")
        self._stored[info.day] = preds
        cutoff = info.day - timedelta(days=self.window_days + 40)
        for d in [d for d in self._stored if d < cutoff]:
            del self._stored[d]
        w = self.weights(info, list(preds))
        self.last_weights = w
        return sum(w[n] * p for n, p in preds.items())
