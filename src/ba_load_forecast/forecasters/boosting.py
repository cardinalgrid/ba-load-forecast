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

from ..features import EXTREME_COLUMNS, FEATURE_COLUMNS, rows_for_days, target_temperature, training_days
from ..information_set import InformationSet
from ..sky import IRRADIANCE_COLUMNS, PV_COLUMNS, SKY_COLUMNS
from .base import ForecastError


class Boosting:
    def __init__(self, train_days: int = 730, refit_days: int = 7, max_iter: int = 400, learning_rate: float = 0.05,
                 max_leaf_nodes: int = 31, min_train_days: int = 120, seed: int = 0, stations: bool = True,
                 special_days: bool = True, label_column: str = "day_type", labels=None, name: str | None = None,
                 extremes: bool = False, sky: bool = False):
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
        self.model = HistGradientBoostingRegressor(
            max_iter=self.max_iter, learning_rate=self.learning_rate, max_leaf_nodes=self.max_leaf_nodes,
            early_stopping=True, validation_fraction=0.1, n_iter_no_change=20, random_state=self.seed,
        ).fit(rows[self.columns].to_numpy(dtype=float), rows["y"].to_numpy(dtype=float))
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
        return self.model.predict(x)
