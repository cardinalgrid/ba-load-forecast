from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.profile import ProfileForecaster
from tests.conftest import make_info

MILD_SHAPE = 1.0 + 0.3 * np.sin(2 * np.pi * (np.arange(24) - 6) / 24)      # afternoon peak
COLD_SHAPE = 1.0 + 0.3 * np.cos(2 * np.pi * (np.arange(24) - 7) / 24)      # morning peak


def history(start="2023-10-01", days=120, cold_every=None):
    """Load with a known shape per regime and a level that grows 1 % a day; temperature 65 F, or 30 F on cold days."""
    hours = pd.date_range(start, periods=24 * days, freq="h")
    load = np.empty(len(hours))
    temp = np.empty(len(hours))
    for k in range(days):
        cold = cold_every is not None and k % cold_every == 0
        level = 1000.0 * (1.01**k)
        load[24 * k: 24 * k + 24] = (COLD_SHAPE if cold else MILD_SHAPE) * level
        temp[24 * k: 24 * k + 24] = 30.0 if cold else 65.0
    return pd.Series(load, index=hours), pd.Series(temp, index=hours)


def test_profile_reproduces_shape_and_recent_level():
    load, temp = history()
    day = date(2024, 1, 17)                                         # a Wednesday, 108 days into the history
    info = make_info(day, load, temp, np.full(24, 65.0))
    f = ProfileForecaster().predict(info)
    np.testing.assert_allclose(f / f.mean(), MILD_SHAPE, rtol=1e-6)
    # level: the median daily mean of the 5 most recent known workdays: day indices 106 (Mon 15), 103, 102, 101, 100
    expected_level = 1000.0 * (1.01**102)
    assert f.mean() == pytest.approx(expected_level, rel=1e-6)


def test_profile_uses_the_cold_shape_when_cold_is_forecast():
    load, temp = history(cold_every=4)                              # every fourth day is a heating day
    cold = ProfileForecaster().predict(make_info(date(2024, 1, 17), load, temp, np.full(24, 30.0)))
    np.testing.assert_allclose(cold / cold.mean(), COLD_SHAPE, rtol=1e-6)
    mild = ProfileForecaster().predict(make_info(date(2024, 1, 17), load, temp, np.full(24, 65.0)))
    np.testing.assert_allclose(mild / mild.mean(), MILD_SHAPE, rtol=1e-6)


def test_profile_without_weather_falls_back_and_short_history_refuses():
    load, temp = history()
    info = make_info(date(2024, 1, 17), load, temp, np.full(24, np.nan))
    f = ProfileForecaster().predict(info)
    np.testing.assert_allclose(f / f.mean(), MILD_SHAPE, rtol=1e-6)
    short_load, short_temp = history(start="2024-01-14", days=3)   # only Monday the 15th is a known workday
    with pytest.raises(ForecastError):
        ProfileForecaster().predict(make_info(date(2024, 1, 17), short_load, short_temp, np.full(24, 65.0)))
