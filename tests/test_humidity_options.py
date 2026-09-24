"""Phase H options: the humidity and wind blocks of the boosting and the apparent temperature of the additive."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.features import apparent_series, rows_for_days
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.weather_extra import HUMIDITY_COLUMNS, WIND_COLUMNS
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def weather_for(temp: pd.Series, dew_below: float = 10.0, wind: float = 4.0) -> pd.DataFrame:
    """A weather frame on the temperature's hours: dew point a fixed distance below, constant wind."""
    return pd.DataFrame({"dewpoint_f": temp.to_numpy() - dew_below, "wind_ms": wind}, index=temp.index)


def test_rows_carry_the_weather_columns_and_apparent_series_moves_only_where_it_should():
    load, temp = world(days=60)
    day = date(2022, 2, 20)
    w = weather_for(temp)
    rows = rows_for_days(load, temp, [day], weather=w)
    assert set(HUMIDITY_COLUMNS + WIND_COLUMNS) <= set(rows.columns)
    np.testing.assert_allclose(rows["dpd"].to_numpy(), 10.0)
    assert (rows["rh"] > 0).all()
    plain = rows_for_days(load, temp, [day])
    assert "dewpoint" not in plain.columns
    hot = pd.Series([95.0, 40.0, 70.0], index=temp.index[:3])
    a = apparent_series(hot, pd.DataFrame({"dewpoint_f": [80.0, 30.0, 50.0], "wind_ms": [1.0, 8.0, 2.0]}, index=hot.index))
    assert a.iloc[0] > 95.0                                                   # humid heat
    assert a.iloc[1] < 40.0                                                   # wind chill
    assert a.iloc[2] == 70.0                                                  # neither
    assert apparent_series(hot, None).equals(hot)


def test_models_use_the_weather_frame_and_refuse_without_it():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    with pytest.raises(ForecastError, match="humidity"):
        Boosting(train_days=300, max_iter=30, extra=("humidity",)).predict(info)
    with pytest.raises(ForecastError, match="apparent"):
        AdditiveModel(train_days=300, apparent=True).predict(info)
    info.weather = weather_for(temp)
    b = Boosting(train_days=300, max_iter=30, extra=("humidity", "wind"))
    p = b.predict(info)
    assert p.shape == (24,)
    assert set(HUMIDITY_COLUMNS + WIND_COLUMNS) <= set(b.columns)
    a = AdditiveModel(train_days=300, apparent=True)
    q = a.predict(info)
    assert q.shape == (24,)
    assert np.isfinite(q).all()
    plain = AdditiveModel(train_days=300).predict(info)
    assert not np.allclose(q, plain)                                          # the apparent temperature changes the fit
    lin = AdditiveModel(train_days=300, extra=("humidity",))
    r = lin.predict(info)
    assert r.shape == (24,)
    assert np.isfinite(r).all()
    assert not np.allclose(r, plain)                                          # the linear humidity terms change the fit
    with pytest.raises(ForecastError, match="humidity"):
        AdditiveModel(train_days=300, extra=("humidity",)).predict(perfect_weather_info(load, temp, date(2023, 1, 20)))
