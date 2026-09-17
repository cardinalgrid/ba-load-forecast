from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.information_set import Loader
from tests.conftest import demand_value, observed_temp_c


def f_of(utc: str) -> float:
    return observed_temp_c(pd.Timestamp(utc)) * 9.0 / 5.0 + 32.0


def test_information_set_ends_at_the_cutoff_and_carries_the_day(public_data):
    tidy, isd, hrrr = public_data
    info = Loader(tidy, isd, hrrr).information_set("PJM", date(2024, 1, 16))

    assert info.load_history.index[0] == pd.Timestamp("2023-12-01 00:00")
    assert info.load_history.index[-1] == pd.Timestamp("2024-01-15 08:00")
    assert info.load_history.iloc[-1] == demand_value(pd.Timestamp("2024-01-15 08:00"))
    assert info.temp_history_f.index.equals(info.load_history.index)
    assert info.temp_history_f.iloc[-1] == pytest.approx(f_of("2024-01-15 13:00"))   # 08:00 EST = 13 UTC

    assert info.run == (date(2024, 1, 15), 12)
    np.testing.assert_array_equal(info.temp_forecast_f, 100.0 + np.arange(17, 41))
    assert info.temp_observed_f[0] == pytest.approx(f_of("2024-01-16 05:00"))
    assert info.temp_observed_f[23] == pytest.approx(f_of("2024-01-17 04:00"))
    # persistence: same hour of D-1 up to the cut-off hour, of D-2 after it
    assert info.temp_persistence_f[8] == pytest.approx(f_of("2024-01-15 13:00"))
    assert info.temp_persistence_f[9] == pytest.approx(f_of("2024-01-14 14:00"))

    expected = np.array([demand_value(t) for t in info.timestamps])
    expected[5] = np.nan
    np.testing.assert_array_equal(info.actual, expected)
    np.testing.assert_array_equal(info.ba_forecast, expected + 10.0)
    np.testing.assert_array_equal(info.offset_h, 5.0)
    assert info.day_type == 0
    assert info.special_day is None
    assert info.cutoff == pd.Timestamp("2024-01-15 08:00")


def test_special_day_and_history_window(public_data):
    tidy, isd, hrrr = public_data
    loader = Loader(tidy, isd, hrrr, history_days=7)
    info = loader.information_set("PJM", date(2024, 1, 1))
    assert (info.day_type, info.special_day) == (2, 2)          # New Year's Day resembles a Sunday
    assert info.load_history.index[0] == pd.Timestamp("2023-12-25 00:00")
    assert info.run == (date(2023, 12, 31), 12)
    assert np.isnan(info.temp_forecast_f).all()                 # that run is not in the extraction
    assert loader.information_set("PJM", date(2024, 1, 1)) is not info
    assert len(loader._series) == 8                              # two years of four series, read once
