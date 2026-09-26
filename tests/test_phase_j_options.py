"""Phase J options: the run 6 h older blended into the path, the hot and cold-by-maximum peak rule, and the
cold-day training weights."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.cutoff import blend_paths, forecast_path, previous_run
from ba_load_forecast.features import cold_weights
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from tests.test_direct_models import perfect_weather_info
from tests.test_ensemble_quantiles import Const, flat_history
from tests.test_recency import world


def test_previous_run_only_within_six_hours():
    assert previous_run((date(2024, 1, 10), 12)) == (date(2024, 1, 10), 6)
    assert previous_run((date(2024, 1, 10), 6)) is None                      # 00 UTC is not extracted
    assert previous_run((date(2024, 1, 10), 6), init_hours=(12, 6, 0)) == (date(2024, 1, 10), 0)
    assert previous_run((date(2024, 1, 10), 12), max_gap_h=3) is None


def test_blend_paths_averages_where_both_are_known():
    a = np.array([10.0, 20.0, 30.0, np.nan])
    b = np.array([12.0, np.nan, 34.0, 40.0])
    out = blend_paths(a, b)
    assert np.allclose(out[:3], [11.0, 20.0, 32.0])
    assert np.isnan(out[3])                                                    # the first path is the reference
    assert blend_paths(a, None) is a


def test_two_runs_blended_through_forecast_path():
    day = date(2024, 1, 10)
    rows = []
    for init_h, offset in ((12, 0.0), (6, 2.0)):
        init = pd.Timestamp(2024, 1, 9, init_h)
        for lead in range(1, 49):
            rows.append({"init_utc": init, "lead_h": lead, "valid_utc": init + pd.Timedelta(hours=lead), "temp_f": 30.0 + offset})
    rows = pd.DataFrame(rows)
    run = (date(2024, 1, 9), 12)
    first = forecast_path(rows, day, 5.0, run)
    second = forecast_path(rows, day, 5.0, previous_run(run))
    out = blend_paths(first, second)
    both = np.isfinite(first) & np.isfinite(second)
    assert both.sum() > 24
    assert np.allclose(out[both], 31.0)
    assert np.allclose(out[np.isfinite(first) & ~np.isfinite(second)], 30.0)   # beyond the older run's reach


def test_hot_and_cold_by_maximum_rules():
    load, temp = flat_history(level=1000.0, days=400)
    base = Const("b", 1000.0)
    ai = AdaptiveIntervals(base, window_days=200, min_days=10, peak="quantile", peak_quantile=0.60,
                           peak_quantile_cold=0.70, peak_quantile_hot=0.75, cold_by_max=True)
    rng = np.random.default_rng(2)
    day0 = date(2024, 3, 1)
    for k in range(250):
        d = day0 + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        centre = 50.0 + 30.0 * np.sin(k / 40.0)
        info.temp_forecast_f = centre + 10.0 * np.sin(np.arange(24) / 24.0 * 2 * np.pi)   # daily range of 20 F
        info.temp_forecast_path_f[-24:] = info.temp_forecast_f
        info.actual = 1000.0 * (1.0 + rng.normal(0.0, 0.03, 24))
        try:
            ai.predict_quantiles(info)
        except ForecastError:
            pass
    def day_with(centre, spread):
        info = perfect_weather_info(load, temp, day0 + timedelta(days=260))
        info.temp_forecast_f = centre + spread * np.sin(np.arange(24) / 24.0 * 2 * np.pi)
        info.temp_forecast_path_f[-24:] = info.temp_forecast_f
        return info
    assert ai.is_hot_day(day_with(95.0, 10.0))
    assert ai.peak_level(day_with(95.0, 10.0)) == 0.75
    assert not ai.is_cold_day(day_with(60.0, 10.0)) and ai.peak_level(day_with(60.0, 10.0)) == 0.60
    cold_all_day = day_with(30.0, 1.0)                    # minimum above the coldest minima, maximum far below the coldest maxima
    assert ai.is_cold_day(cold_all_day) and ai.peak_level(cold_all_day) == 0.70
    ai.cold_by_max = False
    assert not ai.is_cold_day(cold_all_day)


def test_cold_weights_grow_below_the_cold_decile():
    idx = pd.date_range("2024-01-01", periods=24 * 100, freq="h")
    temp = pd.Series(50.0 + 20.0 * np.sin(np.arange(len(idx)) / (24 * 100) * 2 * np.pi), index=idx)
    temp.iloc[24 * 10: 24 * 11] = 0.0                    # one day far below every other minimum
    w = cold_weights(idx, temp, alpha=2.0)
    assert w.shape == (len(idx),)
    assert np.isclose(w.max(), w[24 * 10]) and w[24 * 10] > 3.0
    assert (w >= 1.0).all() and (w[: 24 * 10] == 1.0).all()
    assert (cold_weights(idx, temp, alpha=0.0) == 1.0).all()


def test_weighted_members_fit_and_differ():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    plain = Boosting(train_days=300, max_iter=30).predict(info)
    weighted = Boosting(train_days=300, max_iter=30, cold_weight=2.0).predict(info)
    assert weighted.shape == (24,) and np.isfinite(weighted).all()
    assert not np.allclose(plain, weighted)
    a_plain = AdditiveModel(train_days=300).predict(info)
    a_weighted = AdditiveModel(train_days=300, cold_weight=2.0).predict(info)
    assert np.isfinite(a_weighted).all() and not np.allclose(a_plain, a_weighted)
    x = np.column_stack([np.ones(50), np.linspace(-1, 1, 50)])
    y = x[:, 1] * 2.0
    y[:5] += 10.0
    w = np.ones(50)
    w[:5] = 100.0
    b_plain = AdditiveModel._ridge(x, y, 0.0)
    b_weighted = AdditiveModel._ridge(x, y, 0.0, w)
    assert abs((x[:5] @ b_weighted - y[:5]).mean()) < abs((x[:5] @ b_plain - y[:5]).mean())   # weighted rows fit closer
