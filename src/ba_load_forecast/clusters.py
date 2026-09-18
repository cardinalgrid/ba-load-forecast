"""Daily load shapes grouped by similarity, and what the groups say about special days.

A day is described by its shape: the 24 hourly values divided by the day's mean, so that two days
with the same profile and different levels are the same point. k-means groups the shapes of one BA;
the number of groups is the one with the best silhouette. The groups are then crossed with the
calendar (workday, Saturday, Sunday, the special days of ``grid_sentinel.calendar_us``) and with the
temperature regime, which gives (a) a data-driven version of the special-day table of Cardinal Grid
Note 2, (b) a distance to the nearest centroid that flags atypical days, and (c) a label that a
forecaster can use instead of the calendar day type, predicted for the target day from the calendar
and the forecast regime.

k-means and the silhouette are implemented here in numpy (a few thousand points in 24 dimensions):
no dependency, and the same result on every machine.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

import numpy as np
import pandas as pd


def daily_shapes(load: pd.Series) -> tuple[pd.DatetimeIndex, np.ndarray]:
    """Complete days (24 finite values, positive mean) of an hourly series as normalised shapes."""
    if load.empty:
        return pd.DatetimeIndex([]), np.empty((0, 24))
    s = load.copy()
    s.index = pd.DatetimeIndex(s.index)
    frame = pd.DataFrame({"day": s.index.normalize(), "hour": s.index.hour, "v": s.to_numpy(dtype=float)})
    wide = frame.pivot_table(index="day", columns="hour", values="v", aggfunc="first").reindex(columns=range(24))
    ok = wide.notna().all(axis=1) & (wide.mean(axis=1) > 0)
    wide = wide[ok]
    shapes = wide.to_numpy(dtype=float)
    shapes = shapes / shapes.mean(axis=1, keepdims=True)
    return pd.DatetimeIndex(wide.index), shapes


def _pairwise(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.sqrt(np.maximum(((a[:, None, :] - b[None, :, :]) ** 2).sum(axis=2), 0.0))


def kmeans(x: np.ndarray, k: int, n_init: int = 20, max_iter: int = 300, seed: int = 0) -> tuple[np.ndarray, np.ndarray, float]:
    """Lloyd's k-means with k-means++ seeding; the best of ``n_init`` runs by inertia.

    Returns (centroids, labels, inertia).
    """
    rng = np.random.default_rng(seed)
    n = len(x)
    best = None
    for _ in range(n_init):
        centers = np.empty((k, x.shape[1]))
        centers[0] = x[rng.integers(n)]
        for j in range(1, k):                                   # k-means++: far points are likelier seeds
            d2 = _pairwise(x, centers[:j]).min(axis=1) ** 2
            p = d2 / d2.sum() if d2.sum() > 0 else np.full(n, 1.0 / n)
            centers[j] = x[rng.choice(n, p=p)]
        labels = np.zeros(n, dtype=int)
        for _ in range(max_iter):
            new_labels = _pairwise(x, centers).argmin(axis=1)
            if np.array_equal(new_labels, labels) and _ > 0:
                break
            labels = new_labels
            for j in range(k):
                members = x[labels == j]
                centers[j] = members.mean(axis=0) if len(members) else x[rng.integers(n)]
        inertia = float((_pairwise(x, centers).min(axis=1) ** 2).sum())
        if best is None or inertia < best[2]:
            best = (centers.copy(), labels.copy(), inertia)
    return best


def silhouette(x: np.ndarray, labels: np.ndarray) -> float:
    """Mean silhouette coefficient over all points (NaN when there is only one cluster)."""
    ks = np.unique(labels)
    if len(ks) < 2:
        return float("nan")
    d = _pairwise(x, x)
    n = len(x)
    a = np.zeros(n)
    b = np.full(n, np.inf)
    for kk in ks:
        m = labels == kk
        size = m.sum()
        within = d[:, m].sum(axis=1)
        a[m] = within[m] / max(size - 1, 1)
        other = within / size
        b[~m] = np.minimum(b[~m], other[~m])
    s = np.where(a < b, 1 - a / b, b / a - 1)
    s[np.isnan(s)] = 0.0
    return float(s.mean())


@dataclass
class ClusterModel:
    centroids: np.ndarray
    silhouette: float
    labels_: np.ndarray = field(default_factory=lambda: np.empty(0, dtype=int))

    @property
    def k(self) -> int:
        return len(self.centroids)

    def distances(self, shapes: np.ndarray) -> np.ndarray:
        """Euclidean distance of every shape to every centroid, ``(n, k)``."""
        return _pairwise(np.atleast_2d(np.asarray(shapes, dtype=float)), self.centroids)

    def label(self, shapes: np.ndarray) -> np.ndarray:
        return self.distances(shapes).argmin(axis=1)

    def distance(self, shapes: np.ndarray) -> np.ndarray:
        """Distance to the nearest centroid: the atypicality of a day."""
        return self.distances(shapes).min(axis=1)


def fit_clusters(shapes: np.ndarray, k_range: Iterable[int] = range(3, 9), seed: int = 0, n_init: int = 20) -> ClusterModel:
    """k-means on the shapes for every ``k`` in ``k_range``; keeps the ``k`` with the best silhouette."""
    shapes = np.asarray(shapes, dtype=float)
    if len(shapes) < 10:
        raise ValueError("too few days to cluster")
    best = None
    for k in k_range:
        if k >= len(shapes):
            continue
        centers, labels, _ = kmeans(shapes, k, n_init=n_init, seed=seed)
        sil = silhouette(shapes, labels)
        if best is None or sil > best.silhouette:
            best = ClusterModel(centroids=centers, silhouette=sil, labels_=labels)
    if best is None:
        raise ValueError("no k in the range fits the number of days")
    return best


def crosstab(labels: np.ndarray, day_type: np.ndarray, regime: np.ndarray) -> pd.DataFrame:
    """Counts of days by cluster (rows) and day type x regime (columns)."""
    df = pd.DataFrame({"cluster": labels, "day_type": day_type, "regime": regime})
    return pd.crosstab(df["cluster"], [df["day_type"], df["regime"]])


class LabelClassifier:
    """The cluster a day is expected to fall in, from its calendar day type and its temperature regime.

    Fitted as the most frequent cluster in each (day type, regime) cell of the history; a cell never seen
    falls back to the most frequent cluster of the day type, then of everything.
    """

    def __init__(self):
        self.by_cell: dict[tuple[int, int], int] = {}
        self.by_type: dict[int, int] = {}
        self.default: int = 0

    def fit(self, labels: np.ndarray, day_type: np.ndarray, regime: np.ndarray) -> LabelClassifier:
        df = pd.DataFrame({"c": labels, "t": day_type, "r": regime})
        self.default = int(df["c"].mode().iloc[0])
        self.by_type = {int(t): int(g["c"].mode().iloc[0]) for t, g in df.groupby("t")}
        self.by_cell = {(int(t), int(r)): int(g["c"].mode().iloc[0]) for (t, r), g in df.groupby(["t", "r"])}
        return self

    def predict(self, day_type: int, regime: int | None) -> int:
        if regime is not None and (int(day_type), int(regime)) in self.by_cell:
            return self.by_cell[(int(day_type), int(regime))]
        return self.by_type.get(int(day_type), self.default)
