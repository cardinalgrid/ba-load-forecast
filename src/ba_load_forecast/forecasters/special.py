"""The three treatments of special days, and the data-driven day labels.

* Substitution (treatment iii) is what every model does by default: ``calendar_us`` maps a holiday to the
  day type it resembles (Saturday-like or Sunday-like) and the model sees that type.
* Indicators (treatment i) are the ``special_days=True`` option of the additive model and of the boosting,
  which add the special-day kind as a regressor on top of the substituted type.
* A separate model (treatment ii) is ``SeparateSpecialModel``: one instance of the base model fitted as
  usual and a second one fitted on the "special pool" (special days and weekends) that answers on special
  days only. When the pool is too small the usual model answers.

``ShapeLabels`` turns the clusters of ``scripts/day_clusters.py`` into a day label a model can use in
place of the calendar day type: the label of a past day is its cluster, the label of the target day is
what the calendar-and-regime classifier predicts.
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from ..clusters import LabelClassifier
from ..information_set import InformationSet
from .base import Forecaster, ForecastError
from .profile import regime


class SeparateSpecialModel:
    """Treatment (ii): a second copy of the base model, fitted on special days and weekends, for special days."""

    def __init__(self, factory: Callable[[], Forecaster], min_pool_days: int = 30):
        self.factory = factory
        self.min_pool_days = min_pool_days
        self.usual = factory()
        self.special = factory()
        self.name = f"{self.usual.name}_separate"

    def predict(self, info: InformationSet) -> np.ndarray:
        if info.special_day is None:
            return self.usual.predict(info)
        pooled = self._pool(info)
        if pooled is None:
            return self.usual.predict(info)
        try:
            return self.special.predict(pooled)
        except ForecastError:
            return self.usual.predict(info)

    def _pool(self, info: InformationSet) -> InformationSet | None:
        """The information set with the load of ordinary workdays removed, so that the base model fits on the
        special pool; None when the pool is smaller than ``min_pool_days``."""
        from dataclasses import replace

        from grid_sentinel.calendar_us import day_types

        hist = info.load_history
        if hist.empty:
            return None
        types = day_types(pd.DatetimeIndex(hist.index).to_numpy())
        keep = types != 0
        if keep.sum() < 24 * self.min_pool_days:
            return None
        return replace(info, load_history=hist.where(keep))


class ShapeLabels:
    """Day labels from the shape clusters: ``labels`` for past days, ``predict`` for the target day."""

    def __init__(self, results_dir: Path):
        self.results_dir = Path(results_dir)
        self._labels: dict[str, dict[date, int]] = {}
        self._clf: dict[str, LabelClassifier] = {}

    def _load(self, ba: str) -> None:
        f = self.results_dir / f"{ba}_days.csv"
        if not f.exists():
            raise ForecastError(f"no shape clusters for {ba} in {self.results_dir}")
        t = pd.read_csv(f)
        t["day"] = pd.to_datetime(t["day"]).dt.date
        self._labels[ba] = dict(zip(t["day"], t["cluster"].astype(int), strict=True))
        ok = t["regime"] >= 0
        self._clf[ba] = LabelClassifier().fit(t.loc[ok, "cluster"].to_numpy(), t.loc[ok, "day_type"].to_numpy(),
                                              t.loc[ok, "regime"].to_numpy())

    def labels(self, ba: str) -> dict[date, int]:
        if ba not in self._labels:
            self._load(ba)
        return self._labels[ba]

    def predict(self, info: InformationSet) -> int:
        if info.ba not in self._clf:
            self._load(info.ba)
        r = regime(float(np.nanmean(info.temp_forecast_f))) if np.isfinite(info.temp_forecast_f).sum() >= 18 else None
        return self._clf[info.ba].predict(info.day_type, r)
