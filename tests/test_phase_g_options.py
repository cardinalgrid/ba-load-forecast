"""Phase G options: the extra feature blocks, the ratio target of the boosting and the hourly ensemble weights."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.features import EXTRA_LOAD_COLUMNS, EXTRA_TEMP_COLUMNS, rows_for_days
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.ensemble import Ensemble
from tests.conftest import make_info
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def test_extra_feature_blocks_are_what_they_say():
    load, temp = world(days=60)
    day = date(2022, 2, 20)
    rows = rows_for_days(load, temp, [day])
    ts = rows.index
    assert set(EXTRA_LOAD_COLUMNS + EXTRA_TEMP_COLUMNS) <= set(rows.columns)
    assert rows.loc[ts[5], "l_d14"] == load[ts[5] - pd.Timedelta(days=14)]
    assert rows.loc[ts[5], "l_d21"] == load[ts[5] - pd.Timedelta(days=21)]
    prev = pd.Timestamp(day) - pd.Timedelta(days=1)
    assert rows.loc[ts[0], "t_prev_max"] == temp[prev: prev + pd.Timedelta(hours=23)].max()
    assert rows.loc[ts[0], "t_h07"] == temp[pd.Timestamp(day) + pd.Timedelta(hours=7)]
    assert rows.loc[ts[0], "t_day_range"] == temp[pd.Timestamp(day): pd.Timestamp(day) + pd.Timedelta(hours=23)].max() - \
        temp[pd.Timestamp(day): pd.Timestamp(day) + pd.Timedelta(hours=23)].min()
    hdh = (65.0 - temp).clip(lower=0)[pd.Timestamp(day) - pd.Timedelta(hours=72): pd.Timestamp(day) - pd.Timedelta(hours=1)].sum()
    assert abs(rows.loc[ts[0], "hdh72"] - hdh) < 1e-6


def test_models_accept_the_extra_blocks_and_the_ratio_target():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    b = Boosting(train_days=300, max_iter=50, extra=("load", "temp"))
    p = b.predict(info)
    assert p.shape == (24,)
    assert set(EXTRA_LOAD_COLUMNS + EXTRA_TEMP_COLUMNS) <= set(b.columns)
    r = Boosting(train_days=300, max_iter=50, target="ratio")
    q = r.predict(info)
    assert q.shape == (24,)
    assert 0.5 < q.mean() / p.mean() < 1.5                                # the ratio target comes back in MW
    a = AdditiveModel(train_days=300, val_days=30, extra=("load",))
    assert a.predict(info).shape == (24,)


class Fixed:
    def __init__(self, name, values):
        self.name, self.values = name, np.asarray(values, dtype=float)

    def predict(self, info):
        return self.values.copy()


def test_hourly_weights_favour_the_member_that_is_better_at_that_hour():
    hours = pd.date_range("2023-01-01", periods=24 * 80, freq="h")
    actual = pd.Series(np.tile(1000.0 + 100.0 * (np.arange(24) >= 12), 80), index=hours)   # 1000 at night, 1100 by day
    night_good = Fixed("night", np.r_[np.full(12, 1000.0), np.full(12, 1000.0)])                # right at night, low by day
    day_good = Fixed("day", np.r_[np.full(12, 1100.0), np.full(12, 1100.0)])                    # high at night, right by day
    ens = Ensemble([night_good, day_good], weighting="hourly", window_days=30)
    out = None
    for k in range(40):
        d = date(2023, 1, 5) + timedelta(days=k)
        info = make_info(d, actual, pd.Series(50.0, index=hours), np.full(24, 60.0))
        out = ens.predict(info)
    assert abs(out[:12].mean() - 1000.0) < 20.0                       # the night member dominates the night hours
    assert abs(out[12:].mean() - 1100.0) < 20.0                       # the day member dominates the day hours
