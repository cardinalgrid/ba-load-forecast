from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.features import rows_for_days
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.special import SeparateSpecialModel, ShapeLabels
from tests.conftest import make_info


class Mean:
    """A base model that answers the mean of the known history: lets the test see which history it saw."""

    name = "mean"

    def predict(self, info):
        h = info.load_history.dropna()
        if len(h) < 24:
            raise ForecastError("no history")
        return np.full(24, h.mean())


def history():
    hours = pd.date_range("2023-11-01", periods=24 * 70, freq="h")
    wd = pd.DatetimeIndex(hours).weekday
    load = pd.Series(np.where(wd < 5, 1000.0, 500.0), index=hours)     # workdays 1000, weekends 500
    return load, pd.Series(50.0, index=hours)


def test_separate_model_uses_the_special_pool_on_special_days():
    load, temp = history()
    m = SeparateSpecialModel(Mean)
    assert m.name == "mean_separate"
    ordinary = make_info(date(2024, 1, 3), load, temp, np.full(24, 50.0))     # a Wednesday
    assert ordinary.special_day is None
    assert m.predict(ordinary)[0] == pytest.approx(load.loc[: ordinary.cutoff].mean())
    holiday = make_info(date(2024, 1, 1), load, temp, np.full(24, 50.0))
    assert holiday.special_day == 2
    from grid_sentinel.calendar_us import day_types

    hist = load.loc[: holiday.cutoff]
    pool_mean = hist[day_types(hist.index.to_numpy()) != 0].mean()          # weekends and the autumn holidays
    assert 500.0 < pool_mean < 700.0
    assert SeparateSpecialModel(Mean, min_pool_days=10).predict(holiday)[0] == pytest.approx(pool_mean)
    assert m.predict(holiday)[0] == pytest.approx(hist.mean())              # 70 days: the pool is under 30 days


def test_shape_labels_from_cluster_results(tmp_path):
    t = pd.DataFrame({"day": ["2024-01-01", "2024-01-02", "2024-01-06", "2024-01-07"], "cluster": [3, 1, 3, 3],
                      "day_type": [2, 0, 1, 2], "regime": [0, 0, 0, 0], "distance": 0.1})
    t.to_csv(tmp_path / "PJM_days.csv", index=False)
    labels = ShapeLabels(tmp_path)
    assert labels.labels("PJM")[date(2024, 1, 2)] == 1
    load, temp = history()
    info = make_info(date(2024, 1, 8), load, temp, np.full(24, 40.0))       # a heating-regime Monday
    assert labels.predict(info) == 1
    rows = rows_for_days(load, temp, [date(2024, 1, 2), date(2024, 1, 9)], labels=labels.labels("PJM"))
    assert rows["cluster"].iloc[0] == 1
    assert rows["cluster"].iloc[-1] == -1
    with pytest.raises(ForecastError, match="no shape clusters"):
        labels.labels("TVA")
