"""Gradient boosting on hourly rows (histogram-based trees, scikit-learn).

One model per BA on the rows of ``features.rows_for_days``: calendar, the temperature of the hour and
its recent past, the day's extremes, the known load lags, and, when the information set carries several
stations, one temperature column per station. Trees capture the interactions the regression writes by
hand (temperature by hour, by day type, by season) and whatever else the rows contain. Trained on the
last ``train_days``, early stopping on a random tenth of the rows, refitted every ``refit_days``.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

from ..features import (
    EXTRA_LOAD_COLUMNS,
    EXTRA_TEMP_COLUMNS,
    EXTREME_COLUMNS,
    FEATURE_COLUMNS,
    rows_for_days,
    target_temperature,
    training_days,
)
from ..information_set import InformationSet
from ..sky import IRRADIANCE_COLUMNS, PV_COLUMNS, SKY_COLUMNS
from .base import ForecastError


class Boosting:
    def __init__(self, train_days: int = 730, refit_days: int = 7, max_iter: int = 400, learning_rate: float = 0.05,
                 max_leaf_nodes: int = 31, min_train_days: int = 120, seed: int = 0, stations: bool = True,
                 special_days: bool = True, label_column: str = "day_type", labels=None, name: str | None = None,
                 extremes: bool = False, sky: bool = False, extra: tuple[str, ...] = (), min_samples_leaf: int = 20,
                 l2: float = 0.0, target: str = "level"):
        self.extra = tuple(extra)             # optional feature blocks: "load" (EXTRA_LOAD_COLUMNS), "temp" (EXTRA_TEMP_COLUMNS)
        self.min_samples_leaf = min_samples_leaf
        self.l2 = l2
        self.target = target                  # "level": the load in MW; "ratio": the load divided by the last known 24 h mean
        self.extremes = extremes              # explicit cold and heat terms (features.EXTREME_COLUMNS)
        self.sky = sky                        # sun, cloud cover and, with Loader(pv=True), the PV capacity terms; needs Loader(sky=True)
        self.train_days = train_days
        self.refit_days = refit_days
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.max_leaf_nodes = max_leaf_nodes
        self.min_train_days = min_train_days
        self.seed = seed
        self.stations = stations
        self.special_days = special_days
        self.label_column = label_column
        self.labels = labels                    # a ShapeLabels, when label_column == "cluster"
        self.name = name or ("boosting" + ("" if special_days else "_nospecial") + ("_cluster" if label_column == "cluster" else ""))
        self.model: HistGradientBoostingRegressor | None = None
        self.columns: list[str] = []
        self.fitted_on: date | None = None
        self.fitted_ba: str | None = None

    def _station_frames(self, info: InformationSet, target: bool) -> pd.DataFrame | None:
        if not self.stations or info.temp_history_stations_f is None:
            return None
        hist = info.temp_history_stations_f
        if not target:
            return hist
        path = info.temp_forecast_path_stations_f
        return pd.concat([hist.loc[: path.index[0] - pd.Timedelta(hours=1)], path]).interpolate(limit=6, limit_area="inside")

    def _columns(self, rows: pd.DataFrame) -> list[str]:
        cols = [c for c in FEATURE_COLUMNS if c != "day_type" or self.label_column == "day_type"]
        if self.label_column != "day_type":
            cols.append(self.label_column)
        if not self.special_days:
            cols = [c for c in cols if c != "special_kind"]
        cols += [c for c in rows.columns if c.startswith("t_K")]
        if self.extremes:
            cols += EXTREME_COLUMNS
        if "load" in self.extra:
            cols += EXTRA_LOAD_COLUMNS
        if "temp" in self.extra:
            cols += EXTRA_TEMP_COLUMNS
        if self.sky and "sun" in rows.columns:
            cols += [c for c in SKY_COLUMNS + PV_COLUMNS + IRRADIANCE_COLUMNS if c in rows.columns]
        return cols

    def needs_fit(self, info: InformationSet) -> bool:
        return (self.model is None or self.fitted_ba != info.ba or self.fitted_on is None
                or (info.day - self.fitted_on).days >= self.refit_days)

    def day_labels(self, info: InformationSet, target: bool = False):
        if self.labels is None:
            return None
        labels = dict(self.labels.labels(info.ba))
        if target:
            labels[info.day] = self.labels.predict(info)
        return labels

    def fit(self, info: InformationSet) -> None:
        days = training_days(info.day - timedelta(days=2), self.train_days)
        rows = rows_for_days(info.load_history, info.temp_history_f, days, self._station_frames(info, target=False),
                             labels=self.day_labels(info), sky=info.sky if self.sky else None)
        rows = rows[rows["y"] > 0].dropna(subset=["y"])
        if self.label_column == "cluster":
            rows = rows[rows["cluster"] >= 0]
        if len(rows) < 24 * self.min_train_days:
            raise ForecastError(f"only {len(rows) // 24} days of history to fit on")
        self.columns = self._columns(rows)
        y = rows["y"].to_numpy(dtype=float)
        if self.target == "ratio":
            base = rows["l_mean24"].to_numpy(dtype=float)
            keep = np.isfinite(base) & (base > 0)
            rows, y = rows[keep], y[keep] / base[keep]
        self.model = HistGradientBoostingRegressor(
            max_iter=self.max_iter, learning_rate=self.learning_rate, max_leaf_nodes=self.max_leaf_nodes,
            min_samples_leaf=self.min_samples_leaf, l2_regularization=self.l2,
            early_stopping=True, validation_fraction=0.1, n_iter_no_change=20, random_state=self.seed,
        ).fit(rows[self.columns].to_numpy(dtype=float), y)
        self.fitted_on = info.day
        self.fitted_ba = info.ba

    def predict(self, info: InformationSet) -> np.ndarray:
        if np.isnan(info.temp_forecast_f).any():
            raise ForecastError("no weather forecast for the day")
        if self.needs_fit(info):
            self.fit(info)
        rows = rows_for_days(info.load_history, target_temperature(info), [info.day], self._station_frames(info, target=True),
                             labels=self.day_labels(info, target=True), sky=info.sky if self.sky else None)
        x = rows[self.columns].to_numpy(dtype=float)
        pred = self.model.predict(x)
        if self.target == "ratio":
            base = rows["l_mean24"].to_numpy(dtype=float)
            if not np.isfinite(base).all() or (base <= 0).any():
                raise ForecastError("no known 24 h mean to scale the ratio target")
            pred = pred * base
        return pred
