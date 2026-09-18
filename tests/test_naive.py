from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError, blind_copy
from ba_load_forecast.forecasters.naive import LastKnownDay, SameTypeMean, SameWeekdayLastWeek
from ba_load_forecast.information_set import Loader
from tests.conftest import demand_value


def expected_day(day: str) -> np.ndarray:
    return np.array([demand_value(t) for t in pd.date_range(day, periods=24, freq="h")])


@pytest.fixture
def info(public_data):
    tidy, isd, hrrr = public_data
    return blind_copy(Loader(tidy, isd, hrrr, history_days=45).information_set("PJM", date(2024, 1, 16)))


def test_last_known_day_uses_the_hours_before_the_cutoff(info):
    f = LastKnownDay().predict(info)
    exp = np.concatenate([expected_day("2024-01-15")[:9], expected_day("2024-01-14")[9:]])
    np.testing.assert_array_equal(f, exp)


def test_same_weekday_last_week(info):
    np.testing.assert_array_equal(SameWeekdayLastWeek().predict(info), expected_day("2024-01-09"))


def test_same_type_mean_uses_only_complete_days_of_the_same_type(info):
    # 2024-01-16 is a Tuesday: the workdays from 2024-01-02 to 2024-01-14 excluding the weekends and D-1
    f = SameTypeMean(weeks=2).predict(info)
    days = [d for d in pd.date_range("2024-01-02", "2024-01-14") if d.weekday() < 5 and d != pd.Timestamp("2024-01-01")]
    exp = np.mean([expected_day(str(d.date())) for d in days], axis=0)
    np.testing.assert_allclose(f, exp)
    with pytest.raises(ForecastError):
        SameTypeMean(weeks=0).predict(info)
