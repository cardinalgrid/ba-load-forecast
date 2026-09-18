from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.recency import RecencyRegression, design
from tests.conftest import make_info

SHAPE = 100.0 * (1.0 + 0.4 * np.sin(2 * np.pi * (np.arange(24) - 6) / 24))


def world(start="2022-01-01", days=500, seed=0):
    """Temperature with a yearly and a daily cycle; load = base + hour shape + a U-shaped response to the
    temperature of the hour and of the previous 24 h mean, plus small noise."""
    rng = np.random.default_rng(seed)
    hours = pd.date_range(start, periods=24 * days, freq="h")
    doy = hours.dayofyear.to_numpy()
    h = hours.hour.to_numpy()
    temp = 60 + 20 * np.sin(2 * np.pi * (doy - 100) / 365) + 8 * np.sin(2 * np.pi * (h - 15) / 24) + rng.normal(0, 2, len(hours))
    t = pd.Series(temp, index=hours)
    ma24 = t.rolling(24, min_periods=24).mean().shift(1, freq="h").reindex(hours).to_numpy()
    load = 1000.0 + SHAPE[h] + 3.0 * ((temp - 65) / 10) ** 2 * 10 + 4.0 * ((ma24 - 65) / 10) ** 2 * 10 + rng.normal(0, 3, len(hours))
    return pd.Series(load, index=hours), t


def test_design_shape_and_lag_alignment():
    _, temp = world(days=40)
    ts = pd.date_range("2022-02-01", periods=24, freq="h")
    x = design(ts, temp, np.zeros(24, dtype=int), (1,), (6,), 3)
    assert x.shape == (24, 1 + 1 + 12 + 72 + 3 + 72 + 36 + 3 + 3)
    lag_col = 1 + 1 + 12 + 72 + 3 + 72 + 36
    assert x[5, lag_col] == pytest.approx(temp["2022-02-01 04:00"] / 100.0)
    assert x[5, lag_col + 3] == pytest.approx(temp["2022-01-31 23:00":"2022-02-01 04:00"].mean() / 100.0)


def test_recency_regression_recovers_the_world_and_refits_weekly():
    load, temp = world()
    model = RecencyRegression(train_days=365, refit_days=7)
    days = [date(2023, 4, 10) + timedelta(days=k) for k in range(10)]
    mapes, fits = [], []
    for d in days:
        path_idx = pd.date_range(pd.Timestamp(d) - pd.Timedelta(hours=15), periods=39, freq="h")
        info = make_info(d, load, temp, temp.reindex(path_idx).to_numpy())      # perfect weather
        f = model.predict(info)
        actual = load.reindex(info.timestamps).to_numpy()
        mapes.append(np.mean(np.abs(f - actual) / actual) * 100)
        fits.append(model.fitted_on)
    assert max(mapes) < 1.0
    assert fits[0] == days[0]
    assert fits[6] == days[0]
    assert fits[7] == days[7]


def test_recency_regression_refuses_without_weather_or_history():
    load, temp = world(days=60)
    info = make_info(date(2022, 2, 20), load, temp, np.full(24, np.nan))
    with pytest.raises(ForecastError, match="weather"):
        RecencyRegression().predict(info)
    info = make_info(date(2022, 2, 20), load, temp, np.full(24, 50.0))
    with pytest.raises(ForecastError, match="history"):
        RecencyRegression().predict(info)
