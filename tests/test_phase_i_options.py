"""Phase I options: extra quantile levels with CRPS and Winkler, the cold-day peak quantile, the robust boosting
loss and the apparent temperature without wind."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.evaluate import score_day
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from ba_load_forecast.metrics import QUANTILE_FIELDS, crps_from_quantiles, quantile_metrics
from tests.test_direct_models import perfect_weather_info
from tests.test_ensemble_quantiles import Const, flat_history
from tests.test_humidity_options import weather_for
from tests.test_recency import world


def test_crps_and_winkler_by_hand():
    a = np.full(24, 100.0)
    q = np.vstack([np.full(24, 90.0), np.full(24, 100.0), np.full(24, 110.0)])
    m = quantile_metrics(q, a)
    assert set(QUANTILE_FIELDS) <= set(m)
    assert abs(m["winkler_90"] - 20.0) < 1e-9                                 # width 20 % of the actual, no exceedance
    q2 = np.vstack([np.full(24, 102.0), np.full(24, 105.0), np.full(24, 110.0)])   # the actual is 2 under the lower bound
    m2 = quantile_metrics(q2, a)
    assert abs(m2["winkler_90"] - (8.0 + 20.0 * 2.0)) < 1e-9                  # width 8 plus the penalty 2/alpha times 2
    levels = np.array([0.05, 0.5, 0.95])
    c = crps_from_quantiles(q, levels, a)
    assert abs(c - 2.0 * np.mean([0.05 * 10, 0.0, 0.05 * 10]) / 100.0 * 100.0) < 1e-9   # twice the mean pinball, in percent
    assert np.isnan(crps_from_quantiles(q, levels, np.full(24, np.nan)))


def test_extra_levels_are_issued_and_scored():
    load, temp = flat_history(level=1000.0, days=120)
    noisy = Const("n", 1000.0)
    ai = AdaptiveIntervals(noisy, window_days=60, min_days=10, extra_levels=(0.01, 0.10, 0.90, 0.99), peak="quantile", peak_quantile=0.60)
    day0 = date(2024, 2, 1)
    hourly = []
    rows = None
    for k in range(40):
        d = day0 + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        info.actual = load.reindex(info.timestamps).to_numpy() * (1.0 + 0.02 * np.sin(np.arange(24) + k))
        rows = score_day(info, [ai], hourly)
    assert ai.last_extra is not None
    assert ai.last_extra[1].shape == (4, 24)
    assert (np.diff(ai.last_extra[1], axis=0) >= -1e-9).all()               # levels in order
    names = {r["model"] for r in hourly}
    assert {f"{ai.name}_q01", f"{ai.name}_q10", f"{ai.name}_q90", f"{ai.name}_q99", f"{ai.name}_q05", f"{ai.name}_q95"} <= names
    last = next(r for r in rows if r["model"] == ai.name)
    assert np.isfinite(last["crps"])
    assert np.isfinite(last["winkler_90"])


def test_cold_day_peak_quantile_lifts_the_point_only_on_the_coldest_days():
    load, temp = flat_history(level=1000.0, days=400)
    base = Const("b", 1000.0)
    ai = AdaptiveIntervals(base, window_days=200, min_days=10, peak="quantile", peak_quantile=0.60, peak_quantile_cold=0.90)
    rng = np.random.default_rng(1)
    day0 = date(2024, 3, 1)
    for k in range(250):                                                      # build the known minima and errors
        d = day0 + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        info.temp_forecast_f = np.full(24, 40.0 + 30.0 * np.sin(k / 40.0))
        info.temp_forecast_path_f[-24:] = info.temp_forecast_f
        info.actual = 1000.0 * (1.0 + rng.normal(0.0, 0.03, 24))
        try:
            ai.predict_quantiles(info)
        except ForecastError:                                                 # the first days have no known errors yet
            pass
    cold = perfect_weather_info(load, temp, day0 + timedelta(days=250))
    cold.temp_forecast_f = np.full(24, -20.0)
    cold.temp_forecast_path_f[-24:] = cold.temp_forecast_f
    assert ai.is_cold_day(cold)
    assert ai.peak_level(cold) == 0.90
    mild = perfect_weather_info(load, temp, day0 + timedelta(days=251))
    mild.temp_forecast_f = np.full(24, 60.0)
    mild.temp_forecast_path_f[-24:] = mild.temp_forecast_f
    assert not ai.is_cold_day(mild)
    assert ai.peak_level(mild) == 0.60


def test_robust_loss_and_apparent_without_wind():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    b = Boosting(train_days=300, max_iter=30, loss="absolute_error")
    p = b.predict(info)
    assert p.shape == (24,)
    assert b.model.loss == "absolute_error"
    info.weather = pd.DataFrame({"dewpoint_f": temp.to_numpy() - 10.0, "wind_ms": 12.0}, index=temp.index)
    with_wind = AdditiveModel(train_days=300, apparent=True).predict(info)
    without = AdditiveModel(train_days=300, apparent=True, apparent_wind=False).predict(info)
    assert not np.allclose(with_wind, without)                                # a strong wind changes the wind chill
    plain = weather_for(temp)                                                 # the helper from the phase H tests still works
    assert set(plain.columns) == {"dewpoint_f", "wind_ms"}
