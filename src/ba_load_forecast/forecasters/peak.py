"""A second stage for the daily peak: predict the day's maximum on its own and reshape the curve around it.

The recipe's point is a weighted mean of members whose peaks fall at different hours, read at the hourly median of
its recent errors; a mean of curves with misaligned peaks has a lower maximum than its members, and a median per
hour is not a forecast of a maximum. ``PeakStage`` takes the band of an ``AdaptiveIntervals`` (its own instance, so
that its adaptive level follows the band this stage issues) and multiplies every issued quantile by a bump centred
on the hour of the forecast peak,

    q'(h) = q(h) * (1 + (r - 1) * w(h)),   w(h) = exp(-0.5 * ((h - h_peak) / sigma) ** 2),

so that the forecast maximum becomes ``r`` times what it was and hours far from the peak do not move. ``r`` comes
from one of three rules (``mode``):

* ``"members"``: the mean of the members' own daily maxima over the maximum of the issued point, never below 1.
  No fitting; it undoes the flattening of the mean and nothing else.
* ``"learned"``: ``exp(f(x))``, with ``f`` a ridge regression of log(actual / issued) at the hour of the actual peak on
  the known days (D-2 and before, at most ``window_days``, at least ``min_days``) against features known at the
  cut-off: the members' flattening and disagreement at the peak, how far the forecast maximum and minimum sit beyond
  the station's known extremes (95th percentile of the daily maxima, 5th of the minima), the NBM spread, the day type, a
  special-day flag, and the median of the target over the last 14 known days (which carries the season; the raw
  temperatures are left out because a linear fit extrapolates them across seasons). Refitted every day.
* ``"learned_extreme"``: the learned ratio only on days whose forecast maximum is above the 90th percentile, or
  forecast minimum below the 10th percentile, of the known days' observed daily extremes; ratio 1 otherwise.

The ratio is clipped to ``clip`` (log scale). Nothing of the target day is used.
"""

from __future__ import annotations

import copy
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ..information_set import InformationSet
from .base import ForecastError

FEATURES = ("flatten", "disagree", "hot_excess", "cold_excess", "spread", "weekend", "special", "recent")


class PeakStage:
    def __init__(self, band, members=(), mode: str = "learned", sigma_h: float = 2.5, window_days: int = 730,
                 min_days: int = 120, ridge: float = 1.0, clip: tuple[float, float] = (-0.08, 0.15),
                 extreme_quantile: float = 0.10, name: str | None = None):
        if mode not in ("members", "learned", "learned_extreme"):
            raise ValueError("mode must be 'members', 'learned' or 'learned_extreme'")
        # an own copy of the band: the same AdaptiveIntervals asked twice a day would see this stage's issued band
        # and its own; the copy shares the (cached) base forecaster so that nothing is fitted twice
        self.band = copy.deepcopy(band, memo={id(band.base): band.base})
        self.members = list(members)
        self.mode = mode
        self.sigma_h = sigma_h
        self.window_days = window_days
        self.min_days = min_days
        self.ridge = ridge
        self.clip = clip
        self.extreme_quantile = extreme_quantile
        self.name = name or f"{band.name}_peak_{mode}"
        self.extra_levels = getattr(self.band, "extra_levels", ())
        self.last_extra = None
        self.last_ratio = 1.0
        self._x: dict[date, np.ndarray] = {}      # features of the day, known at the cut-off
        self._point: dict[date, np.ndarray] = {}  # the issued point before this stage

    # ---- features -------------------------------------------------------------------------------------------------
    def _daily_extremes(self, info: InformationSet) -> tuple[np.ndarray, np.ndarray]:
        """Observed daily maxima and minima of the temperature history (days with 18 hours or more), cached per day."""
        key = (info.ba, info.day)
        if getattr(self, "_ext_key", None) == key:
            return self._ext
        s = info.temp_history_f.dropna() if info.temp_history_f is not None else pd.Series(dtype=float)
        if s.empty:
            self._ext = (np.array([]), np.array([]))
        else:
            g = s.groupby(s.index.normalize())
            n = g.count()
            self._ext = (g.max()[n >= 18].to_numpy(), g.min()[n >= 18].to_numpy())
        self._ext_key = key
        return self._ext

    def features(self, info: InformationSet, point: np.ndarray) -> np.ndarray:
        peak = float(np.nanmax(point))
        maxima = []
        for m in self.members:
            try:
                p = np.asarray(m.predict(info), dtype=float)
            except ForecastError:
                continue
            if p.shape == (24,) and np.isfinite(p).all():
                maxima.append(float(p.max()))
        flatten = np.log(np.mean(maxima) / peak) if maxima else 0.0
        disagree = (max(maxima) - min(maxima)) / peak if len(maxima) > 1 else 0.0
        tf = np.asarray(info.temp_forecast_f, dtype=float)
        tmax = float(np.nanmax(tf)) if np.isfinite(tf).any() else np.nan
        tmin = float(np.nanmin(tf)) if np.isfinite(tf).any() else np.nan
        hi, lo = self._daily_extremes(info)
        hot_excess = max(0.0, tmax - float(np.quantile(hi, 0.95))) if len(hi) >= 60 and np.isfinite(tmax) else 0.0
        cold_excess = max(0.0, float(np.quantile(lo, 0.05)) - tmin) if len(lo) >= 60 and np.isfinite(tmin) else 0.0
        spread = float(getattr(info, "nbm_spread_f", np.nan))
        weekend = float(info.day_type > 0)
        special = float(info.special_day is not None)
        recent = self.recent_target(info)
        return np.array([flatten, disagree, hot_excess, cold_excess, spread, weekend, special, recent], dtype=float)

    def is_extreme(self, info: InformationSet) -> bool:
        tf = np.asarray(info.temp_forecast_f, dtype=float)
        if not np.isfinite(tf).any():
            return False
        hi, lo = self._daily_extremes(info)
        if len(hi) < 60:
            return False
        q = self.extreme_quantile
        return float(np.nanmax(tf)) > float(np.quantile(hi, 1 - q)) or float(np.nanmin(tf)) < float(np.quantile(lo, q))

    # ---- the target on the known days --------------------------------------------------------------------------------
    def known_targets(self, info: InformationSet) -> dict[date, float]:
        first = info.day - timedelta(days=self.window_days + 2)
        out = {}
        for d, p in self._point.items():
            if d < first or d > info.day - timedelta(days=2):
                continue
            hours = pd.date_range(pd.Timestamp(d), periods=24, freq="h")
            actual = info.load_history.reindex(hours).to_numpy(dtype=float)
            if np.isfinite(actual).sum() < 20:
                continue
            h = int(np.nanargmax(actual))
            if not np.isfinite(p[h]) or p[h] <= 0:
                continue
            out[d] = float(np.log(actual[h] / p[h]))
        return out

    def recent_target(self, info: InformationSet) -> float:
        t = self.known_targets(info)
        recent = [v for d, v in sorted(t.items())[-14:]]
        return float(np.median(recent)) if len(recent) >= 5 else 0.0

    def learned_log_ratio(self, info: InformationSet, x: np.ndarray) -> float | None:
        t = self.known_targets(info)
        days = [d for d in t if d in self._x]
        if len(days) < self.min_days:
            return None
        X = np.vstack([self._x[d] for d in days])
        y = np.array([t[d] for d in days])
        med = np.nanmedian(X, axis=0)
        med = np.where(np.isfinite(med), med, 0.0)
        X = np.where(np.isfinite(X), X, med)
        xq = np.where(np.isfinite(x), x, med)
        mu, sd = X.mean(axis=0), X.std(axis=0)
        sd = np.where(sd > 1e-9, sd, 1.0)
        Z = (X - mu) / sd
        z = (xq - mu) / sd
        A = Z.T @ Z + self.ridge * len(y) * 0.1 * np.eye(Z.shape[1])
        beta = np.linalg.solve(A, Z.T @ (y - y.mean()))
        return float(y.mean() + z @ beta)

    # ---- the stage ---------------------------------------------------------------------------------------------------
    def ratio(self, info: InformationSet, point: np.ndarray, x: np.ndarray) -> float:
        if self.mode == "members":
            return max(1.0, float(np.exp(x[0])))
        if self.mode == "learned_extreme" and not self.is_extreme(info):
            return 1.0
        f = self.learned_log_ratio(info, x)
        if f is None:
            return 1.0
        return float(np.exp(np.clip(f, *self.clip)))

    def bump(self, point: np.ndarray, r: float) -> np.ndarray:
        h_peak = int(np.nanargmax(point))
        h = np.arange(24)
        w = np.exp(-0.5 * ((h - h_peak) / self.sigma_h) ** 2)
        return 1.0 + (r - 1.0) * w

    def _record(self, info: InformationSet, point: np.ndarray) -> np.ndarray:
        x = self.features(info, point)
        self._x[info.day] = x
        self._point[info.day] = np.asarray(point, dtype=float).copy()
        cutoff = info.day - timedelta(days=self.window_days + 40)
        for d in [d for d in self._point if d < cutoff]:
            self._point.pop(d, None)
            self._x.pop(d, None)
        return x

    def predict_quantiles(self, info: InformationSet) -> np.ndarray:
        q = np.asarray(self.band.predict_quantiles(info), dtype=float)
        point = q[q.shape[0] // 2]
        x = self._record(info, point)
        r = self.ratio(info, point, x)
        self.last_ratio = r
        f = self.bump(point, r)
        q = q * f[None, :]
        if hasattr(self.band, "_issued"):
            self.band._issued[info.day] = (q[0], q[-1])          # the adaptive level follows the band issued here
        extra = getattr(self.band, "last_extra", None)
        self.last_extra = (extra[0], extra[1] * f[None, :]) if extra is not None and extra[0] == info.day else None
        return q

    def predict(self, info: InformationSet) -> np.ndarray:
        """The base point unchanged: asked only while the band cannot be issued yet (warm-up), when nothing is learned."""
        self.last_ratio = 1.0
        return np.asarray(self.band.predict(info), dtype=float)
