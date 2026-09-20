from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals, EmpiricalIntervals
from tests.conftest import make_info


class Flat:
    name = "flat"

    def predict(self, info):
        return np.full(24, 1000.0)


def coverage(model, load, temp_of_day, days):
    """Share of hours inside the 5-95 band for each day (NaN while the model cannot give a band)."""
    out = {}
    for d in days:
        info = make_info(d, load, pd.Series(50.0, index=load.index), np.full(24, temp_of_day(d)))
        try:
            q = model.predict_quantiles(info)
        except ForecastError:
            out[d] = np.nan
            continue
        actual = load.reindex(info.timestamps).to_numpy()
        out[d] = float(np.mean((actual >= q[0]) & (actual <= q[2])))
    return pd.Series(out)


def test_intervals_by_regime_cover_the_cold_days_that_simple_intervals_miss():
    rng = np.random.default_rng(0)
    hours = pd.date_range("2023-01-01", periods=24 * 420, freq="h")
    day_index = (hours.normalize() - hours[0].normalize()).days.to_numpy()
    cold_day = day_index % 4 == 0                                   # one day in four is a heating day
    sigma = np.where(cold_day, 0.05, 0.01)                          # and its errors are five times larger
    load = pd.Series(1000.0 * (1 + rng.normal(0, 1, len(hours)) * sigma), index=hours)

    def temp_of_day(d):
        return 30.0 if (pd.Timestamp(d) - hours[0].normalize()).days % 4 == 0 else 65.0

    days = [date(2023, 1, 5) + timedelta(days=k) for k in range(400)]
    late = days[150:]
    cold = [d for d in late if temp_of_day(d) == 30.0]
    simple = coverage(EmpiricalIntervals(Flat(), window_days=120), load, temp_of_day, days)
    regime = coverage(EmpiricalIntervals(Flat(), window_days=365, by_regime=True), load, temp_of_day, days)
    assert simple[cold].mean() < 0.80                               # too narrow on the cold days
    assert 0.84 < regime[cold].mean() < 0.96
    mild = [d for d in late if temp_of_day(d) == 65.0]
    assert 0.84 < regime[mild].mean() < 0.96


def test_adaptive_intervals_recover_coverage_after_the_errors_grow():
    rng = np.random.default_rng(1)
    hours = pd.date_range("2023-01-01", periods=24 * 420, freq="h")
    day_index = (hours.normalize() - hours[0].normalize()).days.to_numpy()
    sigma = np.where(day_index < 200, 0.01, 0.03)                   # the errors triple on day 200
    load = pd.Series(1000.0 * (1 + rng.normal(0, 1, len(hours)) * sigma), index=hours)
    days = [date(2023, 1, 5) + timedelta(days=k) for k in range(400)]
    after = [d for d in days if date(2023, 7, 22) <= d <= date(2023, 9, 30)]     # the 70 days after the change
    simple = coverage(EmpiricalIntervals(Flat(), window_days=120), load, lambda d: 65.0, days)
    model = AdaptiveIntervals(Flat(), window_days=120)
    adaptive = coverage(model, load, lambda d: 65.0, days)
    assert adaptive[after].mean() > simple[after].mean()
    assert adaptive.iloc[-60:].mean() > 0.85
    assert 0.005 <= model.alpha <= 0.5


def test_regime_pool_with_adaptive_level_covers_cold_days_when_their_errors_grow():
    rng = np.random.default_rng(2)
    hours = pd.date_range("2023-01-01", periods=24 * 420, freq="h")
    day_index = (hours.normalize() - hours[0].normalize()).days.to_numpy()
    cold_day = day_index % 4 == 0
    sigma = np.where(cold_day, np.where(day_index < 250, 0.03, 0.06), 0.01)   # cold-day errors double on day 250
    load = pd.Series(1000.0 * (1 + rng.normal(0, 1, len(hours)) * sigma), index=hours)

    def temp_of_day(d):
        return 30.0 if (pd.Timestamp(d) - hours[0].normalize()).days % 4 == 0 else 65.0

    days = [date(2023, 1, 5) + timedelta(days=k) for k in range(400)]
    tail = days[300:]
    cold = [d for d in tail if temp_of_day(d) == 30.0]
    mild = [d for d in tail if temp_of_day(d) == 65.0]
    regime = coverage(EmpiricalIntervals(Flat(), window_days=365, by_regime=True), load, temp_of_day, days)
    model = AdaptiveIntervals(Flat(), window_days=365, by_regime=True, alpha_by_regime=True)
    both = coverage(model, load, temp_of_day, days)
    assert both[cold].mean() > regime[cold].mean()                    # the adaptive level reacts to the change
    assert 0.80 < both[mild].mean() < 0.97                            # without breaking the mild days
    assert set(model.alphas) <= {0, 1, 2, None}
    assert len(model.alphas) >= 2                                     # one level per regime seen
