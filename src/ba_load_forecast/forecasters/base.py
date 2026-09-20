"""What a forecaster is, and what it is allowed to see.

A forecaster receives an ``InformationSet`` and returns 24 values for the local hours of the target
day. The harness hands it a *blind* copy of the information set: the load that occurred and the
temperature that occurred on the target day are replaced by NaN, so a forecaster cannot use them
even by mistake. Everything else in the information set was known at 9 a.m. the day before.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Protocol, runtime_checkable

import numpy as np

from ..information_set import InformationSet


class ForecastError(RuntimeError):
    """Raised by a forecaster that cannot produce a forecast for this day (not enough history, no weather)."""


@runtime_checkable
class Forecaster(Protocol):
    name: str

    def predict(self, info: InformationSet) -> np.ndarray:
        """Twenty-four values, one per local hour of ``info.day``, in the units of the load."""
        ...


class Cached:
    """A forecaster that answers a repeated question from memory.

    Wrapping a model lets the same fitted instance be scored on its own and serve as a member of one or
    more ensembles without being fitted and run once for each; the wrapper keeps the forecast of the last
    BA-day and takes the name of the model it wraps.
    """

    def __init__(self, forecaster: Forecaster):
        self.forecaster = forecaster
        self.name = forecaster.name
        self._key: tuple | None = None
        self._value: np.ndarray | None = None
        self._error: ForecastError | None = None

    def predict(self, info: InformationSet) -> np.ndarray:
        key = (info.ba, info.day)
        if key != self._key:
            self._key, self._value, self._error = key, None, None
            try:
                self._value = np.asarray(self.forecaster.predict(info), dtype=float)
            except ForecastError as e:
                self._error = e
        if self._error is not None:
            raise self._error
        return self._value


def blind_copy(info: InformationSet) -> InformationSet:
    """The information set without anything that was not known at the cut-off."""
    return replace(info, actual=np.full(24, np.nan), temp_observed_f=np.full(24, np.nan))
