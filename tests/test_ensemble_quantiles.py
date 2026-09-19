from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.ensemble import Ensemble
from ba_load_forecast.forecasters.quantiles import EmpiricalIntervals, QuantileBoosting
from ba_load_forecast.metrics import quantile_metrics
from tests.conftest import make_info
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


class Const:
    def __init__(self, name, value, fail_on=None):
        self.name, self.value, self.fail_on = name, value, fail_on

    def predict(self, info):
        if self.fail_on is not None and info.day == self.fail_on:
            raise ForecastError("off today")
        return np.full(24, float(self.value))


def flat_history(level=1000.0, days=60):
    hours = pd.date_range("2024-01-01", periods=24 * days, freq="h")
    return pd.Series(level, index=hours), pd.Series(50.0, index=hours)


def test_ensemble_mean_and_failing_member():
    load, temp = flat_history()
    d = date(2024, 2, 20)
    info = make_info(d, load, temp, np.full(24, 50.0))
    ens = Ensemble([Const("a", 100), Const("b", 200)])
    assert ens.name == "ens_mean_a+b"
    np.testing.assert_allclose(ens.predict(info), 150.0)
    ens = Ensemble([Const("a", 100), Const("b", 200, fail_on=d)])
    np.testing.assert_allclose(ens.predict(info), 100.0)
    with pytest.raises(ForecastError, match="no member"):
        Ensemble([Const("a", 100, fail_on=d)]).predict(info)


def test_ensemble_recent_weights_penalise_the_worse_member():
    load, temp = flat_history(level=1000.0)                     # the truth is 1000 every hour
    ens = Ensemble([Const("good", 1010), Const("bad", 1300)], weighting="recent", window_days=10, min_days=3)
    for k in range(12):
        d = date(2024, 2, 1) + timedelta(days=k)
        ens.predict(make_info(d, load, temp, np.full(24, 50.0)))
    w = ens.last_weights
    assert w["good"] > 0.9
    assert w["good"] + w["bad"] == pytest.approx(1.0)
    first = Ensemble([Const("good", 1010), Const("bad", 1300)], weighting="recent")
    first.predict(make_info(date(2024, 2, 1), load, temp, np.full(24, 50.0)))
    assert first.last_weights == {"good": 0.5, "bad": 0.5}        # no record yet: equal weights


def test_quantile_metrics_by_hand():
    a = 100.0 + np.arange(24)
    q = np.vstack([a * 0.9, a, a * 1.1])
    m = quantile_metrics(q, a)
    assert m["coverage_90"] == 1.0
    assert m["pinball_50"] == 0.0
    assert m["width_90"] == pytest.approx(20.0)
    assert m["peak_in_band"] == 1.0
    q2 = np.vstack([a * 1.05, a * 1.1, a * 1.2])                 # the band sits above the actual
    m2 = quantile_metrics(q2, a)
    assert m2["coverage_90"] == 0.0
    assert m2["pinball_50"] == pytest.approx(5.0)                # tau 0.5, error 10 % -> 5 % of actual
    assert np.isnan(quantile_metrics(q[:2], a)["coverage_90"])


def test_empirical_intervals_width_follows_the_errors():
    load, temp = flat_history(level=1000.0, days=120)
    rng = np.random.default_rng(0)
    noisy = load + rng.normal(0, 20, len(load))                  # a base model that is right on average, 2 % noise
    noisy_by_day = {d: noisy.loc[str(d)].to_numpy() for d in pd.date_range("2024-01-01", periods=120).date}

    class Noisy:
        name = "noisy"

        def predict(self, info):
            return noisy_by_day[info.day]

    emp = EmpiricalIntervals(Noisy(), window_days=60, min_days=20)
    for k in range(70):
        d = date(2024, 1, 10) + timedelta(days=k)
        info = make_info(d, load, temp, np.full(24, 50.0))
        if k < 21:                                                # fewer than 20 days with a known outcome (D-2 back)
            with pytest.raises(ForecastError):
                emp.predict_quantiles(info)
        else:
            q = emp.predict_quantiles(info)
    assert q.shape == (3, 24)
    width = (q[2] - q[0]) / q[1]
    assert 0.04 < width.mean() < 0.09                            # about 2 x 1.645 x 2 %


def test_quantile_boosting_covers_the_world():
    load, temp = world()
    model = QuantileBoosting(train_days=365, refit_days=30, max_iter=150)
    cov = []
    for k in range(3):
        d = date(2023, 4, 10) + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        q = model.predict_quantiles(info)
        actual = load.reindex(info.timestamps).to_numpy()
        cov.append(np.mean((actual >= q[0]) & (actual <= q[2])))
        assert np.all(q[0] <= q[1])
        assert np.all(q[1] <= q[2])
    assert np.mean(cov) > 0.7
    assert model.name == "qboost"
