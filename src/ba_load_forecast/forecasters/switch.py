"""A forecast for the ordinary days and another for the days a trigger fires (phase V).

The recipe's adoption rules joined two things in one: the error of the ordinary day and the peak of the extreme days.
Corrections that lift the peak of the storms (the linear recalibration of phase S, the severity-scaled move of phase O)
were refused because they also moved the ordinary days. ``TriggerSwitch`` issues the base band on every day the trigger
does not fire and the candidate's on the days it does, so the candidate's cost on ordinary days becomes the cost of its
false alarms only.

* ``cold_trigger``: from what is known at the cut-off only. It fires when the target day's forecast minimum is below the
  ``quantile`` of the observed daily minima over the last 365 known days (full days up to D-2), below the lowest minimum
  of the whole history window, or ``drop_f`` degrees or more below the minimum of the last known day (a front).
* ``asymmetric=True``: on a trigger day the median and the upper levels come from the candidate and the lower levels stay
  with the base, so that the lower tail does not rise with the point on the cold days that turn out ordinary (the
  reason the move of phase O raised the CRPS on every cold stratum); the levels are sorted hour by hour afterwards.
* ``window``: when given, the candidate moves only the hours whose base median is within this fraction of the day's
  forecast maximum (and half-way at their neighbours), the same window the recipe's peak quantile uses; the other hours
  keep the base. ``None`` moves the whole day (phase V, V4c); the peak is one hour, so V4d moves only those around it.
* ``Memo``: the bands keep adaptive state that advances once per call, so the switch must not call them a second time.
  Each band is wrapped in a ``Memo`` that is scored under its own name and remembers the day's quantiles.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np

from ..information_set import InformationSet
from .base import ForecastError


def cold_trigger(info: InformationSet, quantile: float = 0.03, drop_f: float = 15.0, min_days: int = 200) -> bool:
    fc = np.asarray(info.temp_forecast_f, dtype=float)
    if not np.isfinite(fc).any():
        return False
    fc_min = float(np.nanmin(fc))
    h = info.temp_history_f.dropna()
    if h.empty:
        return False
    idx = h.index.tz_localize(None) if getattr(h.index, "tz", None) is not None else h.index
    daily = h.groupby(idx.date).agg(["min", "count"])
    last_known = info.day - timedelta(days=2)
    daily = daily[(daily["count"] >= 20) & (daily.index <= last_known)]
    if daily.empty:
        return False
    recent = daily[daily.index > info.day - timedelta(days=367)]["min"]
    if len(recent) >= min_days and fc_min < float(np.quantile(recent, quantile)):
        return True
    if len(daily) >= min_days and fc_min < float(daily["min"].min()):
        return True
    return bool(daily.index[-1] == last_known and float(daily["min"].iloc[-1]) - fc_min >= drop_f)


class Memo:
    """A band scored under its own name whose quantiles of the day can be read again without advancing its state."""

    def __init__(self, band):
        self.band = band
        self.name = band.name
        self.extra_levels = tuple(getattr(band, "extra_levels", ()))
        self.last_extra = None
        self._day: date | None = None
        self._q = None

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        if self._day != info.day:
            self._day, self._q, self.last_extra = info.day, None, None
            try:
                self._q = np.asarray(self.band.predict_quantiles(info), dtype=float)
            except ForecastError as e:            # remembered too, so that a second reader does not call the band again
                self._q = e
            extra = getattr(self.band, "last_extra", None)
            self.last_extra = extra if extra is not None and extra[0] == info.day else None
        if isinstance(self._q, ForecastError):
            raise self._q
        return self._q

    def predict(self, info: InformationSet) -> np.ndarray:
        if self._day == info.day and not isinstance(self._q, ForecastError):
            return self._q[self._q.shape[0] // 2]
        return self.band.predict(info)


class TriggerSwitch:
    def __init__(self, base: Memo, candidate: Memo, trigger=cold_trigger, asymmetric: bool = True, name: str | None = None,
                 window: float | None = None):
        self.base = base
        self.candidate = candidate
        self.trigger = trigger
        self.asymmetric = asymmetric
        self.window = window
        self.name = name or f"switch_{candidate.name}"
        self.extra_levels = base.extra_levels
        self.last_extra = None
        self.fired: dict[date, bool] = {}

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        qb = self.base.predict_quantiles(info)
        xb = self.base.last_extra
        on = bool(self.trigger(info))
        self.fired[info.day] = on
        if not on:
            self.last_extra = xb
            return qb
        qc = self.candidate.predict_quantiles(info)
        xc = self.candidate.last_extra
        if not self.asymmetric and self.window is None:
            self.last_extra = xc
            return qc
        levels = np.array([*self.extra_levels, 0.05, 0.5, 0.95]) if xb is not None and xc is not None else np.array([0.05, 0.5, 0.95])
        moved = levels >= 0.5 if self.asymmetric else np.ones(len(levels), bool)
        b = np.vstack([xb[1], qb]) if len(levels) > 3 else qb
        c = np.vstack([xc[1], qc]) if len(levels) > 3 else qc
        w = self.hours(qb[qb.shape[0] // 2])
        mix = np.where(moved[:, None], b + w[None, :] * (c - b), b)
        order = np.argsort(levels)
        mix[order] = np.sort(mix[order], axis=0)
        n = len(levels) - 3
        self.last_extra = (info.day, mix[:n]) if n > 0 else None
        return mix[n:]

    def hours(self, median: np.ndarray) -> np.ndarray:
        """Weight of the candidate at each hour: 1 everywhere without a window; with one, 1 at the hours within it, 0.5 at
        their neighbours, 0 elsewhere (as ``AdaptiveBand.peak_adjust``)."""
        if self.window is None:
            return np.ones(len(median))
        inside = median >= self.window * np.nanmax(median)
        w = inside.astype(float)
        w[1:] = np.maximum(w[1:], 0.5 * inside[:-1])
        w[:-1] = np.maximum(w[:-1], 0.5 * inside[1:])
        return w

    def predict(self, info: InformationSet) -> np.ndarray:
        try:
            q = self.predict_quantiles(info)
        except ForecastError:
            return self.base.predict(info)
        return q[q.shape[0] // 2]
