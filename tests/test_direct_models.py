from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.additive import AdditiveModel, SplineBasis
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.boosting import Boosting
from tests.conftest import make_info
from tests.test_recency import world


def perfect_weather_info(load, temp, d):
    path_idx = pd.date_range(pd.Timestamp(d) - pd.Timedelta(hours=15), periods=39, freq="h")
    return make_info(d, load, temp, temp.reindex(path_idx).to_numpy())


def run_days(model, load, temp, first: date, n: int):
    mapes, fits = [], []
    for k in range(n):
        d = first + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        f = model.predict(info)
        actual = load.reindex(info.timestamps).to_numpy()
        mapes.append(np.mean(np.abs(f - actual) / actual) * 100)
        fits.append(model.fitted_on)
    return mapes, fits


def test_spline_basis_clips_and_sums_to_one():
    b = SplineBasis(np.linspace(0, 100, 500), n_knots=4)
    x = np.array([-10, 0, 50, 100, 120])
    m = b(x)
    assert m.shape == (5, 4 + 4)
    np.testing.assert_allclose(m.sum(axis=1), 1.0)
    np.testing.assert_allclose(m[0], m[1])            # clipped below
    np.testing.assert_allclose(m[3], m[4])            # clipped above


def test_additive_model_recovers_the_world_and_refits_weekly():
    load, temp = world()
    model = AdditiveModel(train_days=365, refit_days=7, val_days=30)
    mapes, fits = run_days(model, load, temp, date(2023, 4, 10), 9)
    assert max(mapes) < 1.5
    assert fits[0] == date(2023, 4, 10)
    assert fits[6] == date(2023, 4, 10)
    assert fits[7] == date(2023, 4, 17)
    assert model.lam in model.lambdas


def test_boosting_recovers_the_world():
    load, temp = world()
    model = Boosting(train_days=365, refit_days=30, max_iter=200)
    mapes, _ = run_days(model, load, temp, date(2023, 4, 10), 3)
    assert max(mapes) < 3.0
    assert "special_kind" in model.columns
    assert not any(c.startswith("t_K") for c in model.columns)


def test_direct_models_refuse_without_weather_or_history():
    load, temp = world(days=60)
    info = make_info(date(2022, 2, 20), load, temp, np.full(24, np.nan))
    for model in (AdditiveModel(), Boosting()):
        with pytest.raises(ForecastError, match="weather"):
            model.predict(info)
    info = perfect_weather_info(load, temp, date(2022, 2, 20))
    for model in (AdditiveModel(), Boosting()):
        with pytest.raises(ForecastError, match="history"):
            model.predict(info)
