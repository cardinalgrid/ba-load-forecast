"""The vanilla benchmark (Hong 2010): a linear model on calendar and temperature polynomials."""
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.vanilla import VanillaBenchmark, vanilla_design
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def test_design_has_the_vanilla_columns_and_full_rank():
    idx = pd.date_range("2022-01-01", periods=24 * 400, freq="h")
    t = 50 + 30 * np.sin(np.arange(len(idx)) / 500)
    x = vanilla_design(idx, t, pd.Timestamp("2015-01-01"))
    assert x.shape == (len(idx), 2 + 11 + (7 * 24 - 1) + 3 * (24 + 12))
    assert np.linalg.matrix_rank(x) == x.shape[1] - 3        # hour x T^p and month x T^p share the T^p column


def test_vanilla_follows_a_temperature_driven_world():
    load, temp = world(days=800)
    model = VanillaBenchmark(train_days=600, refit_days=30)
    errors = []
    for k in range(5):
        d = date(2023, 6, 1) + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        p = model.predict(info)
        actual = load.reindex(info.timestamps).to_numpy()
        errors.append(np.mean(np.abs(p - actual) / actual))
    assert p.shape == (24,)
    assert np.mean(errors) < 0.06
    assert model.name == "vanilla"


def test_vanilla_refuses_short_history():
    load, temp = world(days=200)
    with pytest.raises(ForecastError, match="history"):
        VanillaBenchmark().predict(perfect_weather_info(load, temp, date(2022, 6, 1)))
