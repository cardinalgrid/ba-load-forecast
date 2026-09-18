"""Forecasters: every one implements ``predict(info) -> np.ndarray[24]`` and sees only the blind information set."""

from .base import Forecaster, ForecastError, blind_copy

__all__ = ["ForecastError", "Forecaster", "blind_copy"]
