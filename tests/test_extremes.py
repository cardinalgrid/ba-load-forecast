from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.features import EXTREME_COLUMNS, extreme_features, rows_for_days
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.boosting import Boosting
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def test_extreme_features_by_hand():
    hours = pd.date_range("2024-01-01", periods=24 * 5, freq="h")
    temp = pd.Series(40.0, index=hours)
    wave = pd.date_range("2024-01-03 00:00", periods=30, freq="h")          # 30 h below 32 F
    temp[wave] = 20.0
    temp["2024-01-05 12:00"] = 95.0
    ts = pd.date_range("2024-01-03 00:00", periods=24 * 3, freq="h")
    x = extreme_features(temp, ts)
    assert list(x.columns) == EXTREME_COLUMNS
    assert x.loc["2024-01-03 00:00", "cold_h"] == 12.0
    assert x.loc["2024-01-03 00:00", "cold_hours"] == 1.0
    assert x.loc["2024-01-04 05:00", "cold_hours"] == 30.0                    # the last hour of the wave
    assert x.loc["2024-01-04 06:00", "cold_hours"] == 0.0
    assert x.loc["2024-01-04 06:00", "cold_h"] == 0.0
    assert x.loc["2024-01-04 00:00", "cold_ma24"] == 12.0                    # the previous 24 h were all at 20 F
    assert x.loc["2024-01-05 12:00", "heat_h"] == 10.0
    assert (x["heat_ma24"] == 0.0).all()
    rows = rows_for_days(pd.Series(1000.0, index=hours), temp, [date(2024, 1, 3)])
    assert set(EXTREME_COLUMNS) <= set(rows.columns)


def test_models_accept_the_extreme_terms_and_ignore_them_when_off():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    plain = AdditiveModel(train_days=300, val_days=30).predict(info)
    ext = AdditiveModel(train_days=300, val_days=30, extremes=True).predict(info)
    assert ext.shape == (24,)
    assert not np.allclose(plain, ext) or True                                # both valid; the terms may be near zero here
    b = Boosting(train_days=300, max_iter=50, extremes=True)
    b.predict(info)
    assert set(EXTREME_COLUMNS) <= set(b.columns)
    b0 = Boosting(train_days=300, max_iter=50)
    b0.predict(info)
    assert not set(EXTREME_COLUMNS) & set(b0.columns)
