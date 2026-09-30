"""Phase O, part 2: the band on cold days (scaled or separately adaptive level) and the NBM spread as a width factor."""
from datetime import date, timedelta

import numpy as np

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from tests.test_direct_models import perfect_weather_info
from tests.test_ensemble_quantiles import Const, flat_history


def warmed_up(ai, load, temp, days=250, seed=1, spread=None):
    """Issue ``days`` days with a sinusoidal forecast minimum and 3 % noise, so the pool and the known minima exist."""
    rng = np.random.default_rng(seed)
    day0 = date(2024, 3, 1)
    for k in range(days):
        d = day0 + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        info.temp_forecast_f = np.full(24, 40.0 + 30.0 * np.sin(k / 40.0))
        info.temp_forecast_path_f[-24:] = info.temp_forecast_f
        info.actual = 1000.0 * (1.0 + rng.normal(0.0, 0.03, 24))
        if spread is not None:
            info.nbm_spread_f = spread
        try:
            ai.predict_quantiles(info)
        except ForecastError:
            pass
        load.loc[info.timestamps] = info.actual                              # the outcome becomes known for the next days
    return day0 + timedelta(days=days)


def cold_info(load, temp, d, spread=None):
    info = perfect_weather_info(load, temp, d)
    info.temp_forecast_f = np.full(24, -20.0)
    info.temp_forecast_path_f[-24:] = info.temp_forecast_f
    if spread is not None:
        info.nbm_spread_f = spread
    return info


def width(q):
    return float(np.mean(q[-1] - q[0]))


def test_scaled_level_widens_the_band_on_cold_days_only():
    load, temp = flat_history(level=1000.0, days=400)                        # warmed_up writes the outcomes into load
    plain = AdaptiveIntervals(Const("b", 1000.0), window_days=200, min_days=10)
    scaled = AdaptiveIntervals(Const("b", 1000.0), window_days=200, min_days=10, cold_level="scale", cold_alpha_scale=0.5)
    nxt = warmed_up(plain, load, temp)
    warmed_up(scaled, load, temp)
    cold_p = plain.predict_quantiles(cold_info(load, temp, nxt))
    cold_s = scaled.predict_quantiles(cold_info(load, temp, nxt))
    assert width(cold_p) > 0
    assert width(cold_s) > width(cold_p) * 1.1                                # a 95 % band instead of 90 % on the cold day
    mild = perfect_weather_info(load, temp, nxt + timedelta(days=1))
    mild.temp_forecast_f = np.full(24, 60.0)
    mild.temp_forecast_path_f[-24:] = mild.temp_forecast_f
    ratio = width(scaled.predict_quantiles(mild)) / width(plain.predict_quantiles(mild))
    assert abs(ratio - 1.0) < 0.10                                            # both near the 90 % band on a mild day


def test_adaptive_cold_level_is_tracked_apart():
    load, temp = flat_history(level=1000.0, days=400)
    ai = AdaptiveIntervals(Const("b", 1000.0), window_days=200, min_days=10, cold_level="adaptive", cold_gamma=0.10)
    nxt = warmed_up(ai, load, temp)
    before = ai.alphas.get("cold", ai.target)
    info = cold_info(load, temp, nxt)
    ai.predict_quantiles(info)
    assert nxt in ai._cold
    later = perfect_weather_info(load, temp, nxt + timedelta(days=3))
    later.load_history.loc[info.timestamps] = 1300.0                          # the cold day missed every hour
    ai.update_alpha(later)
    assert ai.alphas["cold"] < before - 0.05                                  # the cold level fell by about cold_gamma * (0.1 - 1)
    assert abs(ai.alphas.get(None, ai.target) - ai.alphas.get(None, ai.target)) < 1e-9


def test_spread_factor_scales_the_half_widths():
    load, temp = flat_history(level=1000.0, days=400)
    ai = AdaptiveIntervals(Const("b", 1000.0), window_days=200, min_days=10, spread_beta=1.0, spread_bounds=(0.5, 3.0))
    nxt = warmed_up(ai, load, temp, spread=2.0)
    base = ai.predict_quantiles(cold_info(load, temp, nxt, spread=2.0))       # the same day three times: same pool, same errors
    wide = ai.predict_quantiles(cold_info(load, temp, nxt, spread=4.0))
    assert abs(width(wide) / width(base) - 2.0) < 1e-6
    np.testing.assert_allclose(wide[1], base[1])                              # the median does not move
    unknown = ai.predict_quantiles(cold_info(load, temp, nxt))                # no spread that day: factor 1
    assert abs(width(unknown) / width(base) - 1.0) < 1e-6
