"""A semi-parametric additive model, one regression per hour of the day (after Hyndman and Fan 2010).

For each hour the load is a sum of smooth functions of the temperature of that hour, of the mean of
the previous 24 hours and of the day's maximum and minimum (cubic B-spline bases with a linear term, so
that the response extrapolates linearly beyond the training range), plus the load at the same hour of
the last known day and of the same day a week before, the mean of the last 24 known hours, the day
type and a trend. Ridge regression on standardised columns; the penalty is chosen on the last
``val_days`` of the training window and the model is refitted every ``refit_days``.

With ``pv=True`` (needs ``Loader(sky=True, pv=True)``) two linear terms per hour describe the solar generation
netted from the load: ``pv_clear``, the installed PV capacity times the sun's elevation, and ``pv_cloud``, the
same times the forecast cloud fraction (zero where no cloud forecast exists). A linear term extrapolates as
the capacity grows, which trees cannot do; this is the simplest form of load reconstitution.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy.interpolate import BSpline

from ..features import EXTREME_COLUMNS, rows_for_days, target_temperature, training_days
from ..information_set import InformationSet
from ..sky import PV_COLUMNS, SKY_COLUMNS
from .base import ForecastError

SMOOTH = ("t", "t_ma24", "t_day_max", "t_day_min")
LINEAR = ("l_last_known", "l_d7", "l_mean24", "trend")
PV_LINEAR = ("pv_clear", "pv_cloud")


class SplineBasis:
    """Cubic B-spline basis with knots at quantiles of the training values; inputs are clipped to the range."""

    def __init__(self, x: np.ndarray, n_knots: int = 6):
        x = x[np.isfinite(x)]
        self.lo, self.hi = float(x.min()), float(x.max())
        inner = np.quantile(x, np.linspace(0, 1, n_knots + 2)[1:-1])
        self.t = np.concatenate([[self.lo] * 4, inner, [self.hi] * 4])

    def __call__(self, x: np.ndarray) -> np.ndarray:
        xc = np.clip(np.asarray(x, dtype=float), self.lo, self.hi)
        return BSpline.design_matrix(xc, self.t, 3).toarray()


class AdditiveModel:
    def __init__(self, train_days: int = 730, refit_days: int = 7, n_knots: int = 6,
                 lambdas: tuple[float, ...] = (0.01, 0.1, 1.0, 10.0, 100.0), val_days: int = 60,
                 min_train_days: int = 120, special_days: bool = False, label_column: str = "day_type",
                 labels=None, name: str | None = None, extremes: bool = False, pv: bool = False):
        self.pv = pv                          # linear PV terms (PV_LINEAR) from the sky frame; needs Loader(sky=True, pv=True)
        self.extremes = extremes              # explicit cold and heat terms (features.EXTREME_COLUMNS) as linear regressors
        self.train_days = train_days
        self.refit_days = refit_days
        self.n_knots = n_knots
        self.lambdas = lambdas
        self.val_days = val_days
        self.min_train_days = min_train_days
        self.special_days = special_days
        self.label_column = label_column
        self.labels = labels                    # a ShapeLabels, when label_column == "cluster"
        self.name = name or ("additive" + ("_special" if special_days else "") + ("_cluster" if label_column == "cluster" else ""))
        self.fitted_on: date | None = None
        self.fitted_ba: str | None = None
        self.bases: dict[str, SplineBasis] = {}
        self.label_values: list[int] = []
        self.coef: dict[int, np.ndarray] = {}
        self.mean: np.ndarray | None = None
        self.std: np.ndarray | None = None
        self.lam: float = 1.0

    # ---- design --------------------------------------------------------------------------------------
    def design(self, rows: pd.DataFrame) -> np.ndarray:
        cols = [np.ones(len(rows))]
        for lab in self.label_values:
            cols.append((rows[self.label_column].to_numpy() == lab).astype(float))
        if self.special_days:
            for kind in (1, 2):
                cols.append((rows["special_kind"].to_numpy() == kind).astype(float))
        for c in SMOOTH:
            cols.append(self.bases[c](rows[c].to_numpy()))
            cols.append(rows[c].to_numpy(dtype=float))
        for c in LINEAR:
            cols.append(rows[c].to_numpy(dtype=float))
        if self.extremes:
            for c in EXTREME_COLUMNS:
                cols.append(rows[c].to_numpy(dtype=float))
        if self.pv:
            for c in PV_LINEAR:
                cols.append(rows[c].to_numpy(dtype=float))
        return np.column_stack([c if c.ndim == 2 else c[:, None] for c in cols])

    def _standardise(self, x: np.ndarray, fit: bool) -> np.ndarray:
        if fit:
            self.mean = x.mean(axis=0)
            self.std = x.std(axis=0)
            self.mean[0], self.std[0] = 0.0, 1.0            # the intercept stays
            self.std[self.std == 0] = 1.0
        return (x - self.mean) / self.std

    @staticmethod
    def _ridge(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
        p = x.shape[1]
        pen = lam * np.eye(p)
        pen[0, 0] = 0.0
        return np.linalg.solve(x.T @ x + pen, x.T @ y)

    def _rows(self, info: InformationSet, temp: pd.Series, days: list[date], target: bool) -> pd.DataFrame:
        rows = rows_for_days(info.load_history, temp, days, labels=self.day_labels(info, target=target),
                             sky=info.sky if self.pv else None)
        if self.pv:
            if "pv_clear" not in rows.columns:
                raise ForecastError("pv=True needs Loader(sky=True, pv=True) and a capacity table for the BA")
            rows["pv_cloud"] = rows["pv_clear"] * rows["cloud"].fillna(0.0) / 100.0
            rows = rows.drop(columns=[c for c in SKY_COLUMNS + PV_COLUMNS if c in rows.columns and c != "pv_clear"])
        return rows

    # ---- fit / predict -------------------------------------------------------------------------------
    def needs_fit(self, info: InformationSet) -> bool:
        return (self.fitted_on is None or self.fitted_ba != info.ba or (info.day - self.fitted_on).days >= self.refit_days)

    def day_labels(self, info: InformationSet, target: bool = False):
        if self.labels is None:
            return None
        labels = dict(self.labels.labels(info.ba))
        if target:
            labels[info.day] = self.labels.predict(info)
        return labels

    def fit(self, info: InformationSet) -> None:
        days = training_days(info.day - timedelta(days=2), self.train_days)
        rows = self._rows(info, info.temp_history_f, days, target=False)
        rows = rows.dropna()
        if self.label_column == "cluster":
            rows = rows[rows["cluster"] >= 0]
        if rows["y"].gt(0).sum() < 24 * self.min_train_days:
            raise ForecastError(f"only {len(rows) // 24} complete days of history to fit on")
        rows = rows[rows["y"] > 0]
        self.label_values = sorted(rows[self.label_column].unique().tolist())[1:]      # first label is the reference
        self.bases = {c: SplineBasis(rows[c].to_numpy(), self.n_knots) for c in SMOOTH}
        x_all = self._standardise(self.design(rows), fit=True)
        y_all = rows["y"].to_numpy(dtype=float)
        hours = rows["hour"].to_numpy()
        day_of = pd.DatetimeIndex(rows.index).normalize()
        cut = day_of.max() - pd.Timedelta(days=self.val_days)
        train, val = np.asarray(day_of <= cut), np.asarray(day_of > cut)
        best = None
        for lam in self.lambdas:
            err = 0.0
            for h in range(24):
                m = (hours == h)
                b = self._ridge(x_all[m & train], y_all[m & train], lam)
                pred = x_all[m & val] @ b
                err += np.mean(np.abs(pred - y_all[m & val]) / y_all[m & val])
            if best is None or err < best[1]:
                best = (lam, err)
        self.lam = best[0]
        self.coef = {h: self._ridge(x_all[hours == h], y_all[hours == h], self.lam) for h in range(24)}
        self.fitted_on = info.day
        self.fitted_ba = info.ba

    def predict(self, info: InformationSet) -> np.ndarray:
        if np.isnan(info.temp_forecast_f).any():
            raise ForecastError("no weather forecast for the day")
        if self.needs_fit(info):
            self.fit(info)
        rows = self._rows(info, target_temperature(info), [info.day], target=True)
        feats = rows.drop(columns=["y"])
        if feats.isna().any().any():
            raise ForecastError("missing input for the target day: " + ", ".join(feats.columns[feats.isna().any()]))
        x = self._standardise(self.design(rows), fit=False)
        return np.array([x[h] @ self.coef[h] for h in range(24)])
