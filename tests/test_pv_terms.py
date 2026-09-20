"""The linear PV terms of the additive model: a growing solar dent in the load is followed as the capacity grows."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.sky import sky_frame
from tests.conftest import make_info
from tests.test_recency import world


def solar_world(days=900):
    """The synthetic world minus a solar dent that grows linearly with an installed capacity."""
    load, temp = world(start="2021-01-01", days=days)
    hours = load.index
    off = pd.Series(5.0, index=hours)
    sky = sky_frame(hours, off, 42.36, -71.01, None)
    months = pd.date_range("2021-01-01", hours[-1], freq="MS")
    cap = pd.Series(np.linspace(100.0, 400.0, len(months)), index=months)     # capacity quadruples over the period
    sky = sky_frame(hours, off, 42.36, -71.01, None, pv=cap)
    net = load - 0.8 * sky["pv_clear"].to_numpy()                           # 80 % of capacity times the sun's elevation
    return net, temp, sky


def info_with_sky(load, temp, sky, d):
    path_idx = pd.date_range(pd.Timestamp(d) - pd.Timedelta(hours=15), periods=39, freq="h")
    info = make_info(d, load, temp, temp.reindex(path_idx).to_numpy())
    info.sky = sky
    return info


def midday_error(model, load, temp, sky, first: date, n: int) -> float:
    errs = []
    for k in range(n):
        d = first + pd.Timedelta(days=k)
        info = info_with_sky(load, temp, sky, d.date() if hasattr(d, "date") else d)
        f = model.predict(info)
        actual = load.reindex(info.timestamps).to_numpy()
        errs.append(np.mean((f - actual)[10:15]) / np.mean(actual[10:15]) * 100)      # signed midday error, %
    return float(np.mean(errs))


def test_pv_terms_remove_the_midday_bias_of_a_growing_solar_dent():
    load, temp, sky = solar_world()
    first = date(2023, 5, 1)
    plain = midday_error(AdditiveModel(train_days=700, val_days=30), load, temp, sky, first, 20)
    with_pv = midday_error(AdditiveModel(train_days=700, val_days=30, pv=True), load, temp, sky, first, 20)
    assert plain > 0.3                       # without the terms the model over-forecasts midday as the capacity grows
    assert abs(with_pv) < plain / 2


def test_pv_terms_need_the_capacity_table():
    load, temp = world(start="2021-01-01", days=400)
    info = info_with_sky(load, temp, None, date(2022, 1, 20))
    with pytest.raises(ForecastError, match="pv=True"):
        AdditiveModel(train_days=300, val_days=30, pv=True).predict(info)
