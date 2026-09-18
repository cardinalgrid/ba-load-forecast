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


def blind_copy(info: InformationSet) -> InformationSet:
    """The information set without anything that was not known at the cut-off."""
    return replace(info, actual=np.full(24, np.nan), temp_observed_f=np.full(24, np.nan))
