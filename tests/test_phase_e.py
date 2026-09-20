from datetime import date

import numpy as np
import pytest

from ba_load_forecast.evaluate import ACTUAL, BA_MODEL, HOURS, evaluate
from ba_load_forecast.forecasters.base import Cached, ForecastError
from ba_load_forecast.forecasters.ensemble import Ensemble
from ba_load_forecast.forecasters.quantiles import EmpiricalIntervals
from ba_load_forecast.information_set import Loader


class Counting:
    name = "counting"

    def __init__(self, fail=False):
        self.calls = 0
        self.fail = fail

    def predict(self, info):
        self.calls += 1
        if self.fail:
            raise ForecastError("no")
        return np.full(24, 1000.0 + info.day.day)


def test_cached_runs_the_model_once_per_ba_day(public_data):
    tidy, isd, hrrr = public_data
    loader = Loader(tidy, isd, hrrr, history_days=30)
    a, b = loader.information_set("PJM", date(2024, 1, 15)), loader.information_set("PJM", date(2024, 1, 16))
    m = Counting()
    c = Cached(m)
    assert c.name == "counting"
    np.testing.assert_array_equal(c.predict(a), c.predict(a))
    assert m.calls == 1
    c.predict(b)
    assert m.calls == 2
    failing = Cached(Counting(fail=True))
    for _ in range(2):
        with pytest.raises(ForecastError):
            failing.predict(a)
    assert failing.forecaster.calls == 1


def test_shared_members_and_hourly_forecasts(public_data):
    tidy, isd, hrrr = public_data
    loader = Loader(tidy, isd, hrrr, history_days=30)
    member = Counting()
    shared = Cached(member)
    ens = Cached(Ensemble([shared], name="ens"))
    models = [shared, ens, EmpiricalIntervals(ens, name="ens_bc")]
    rows, hourly = evaluate(loader, models, ["PJM"], date(2024, 1, 15), date(2024, 1, 17), hourly=True)
    assert member.calls == 3                                   # once per day, although three models use it
    assert set(hourly["model"]) == {"counting", "ens", "ens_bc", BA_MODEL, ACTUAL}
    h = hourly[(hourly["model"] == "counting") & (hourly["day"] == date(2024, 1, 17))]
    np.testing.assert_array_equal(h[HOURS].to_numpy()[0], 1017.0)
    df = hourly[(hourly["model"] == BA_MODEL) & (hourly["day"] == date(2024, 1, 15))][HOURS].to_numpy()[0]
    ac = hourly[(hourly["model"] == ACTUAL) & (hourly["day"] == date(2024, 1, 15))][HOURS].to_numpy()[0]
    np.testing.assert_allclose(df - ac, 10.0)                  # the fixture's DF is demand + 10
    bc = rows[rows["model"] == "ens_bc"]
    assert not bc["skipped"].all()                             # no interval yet, but the point forecast is scored
    assert bc["pinball_50"].isna().all()
