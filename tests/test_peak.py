"""The peak corrections lift the forecast around its peak and nowhere else."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from tests.conftest import make_info

SHAPE = 1000.0 + 200.0 * np.exp(-((np.arange(24) - 18) / 3.0) ** 2)     # an evening peak at 18h


class Shaped:
    name = "shaped"

    def predict(self, info):
        return SHAPE.copy()


def world(days=300, seed=4):
    """The shape plus noise, so that the actual peak is a maximum over noisy hours."""
    rng = np.random.default_rng(seed)
    hours = pd.date_range("2023-01-01", periods=24 * days, freq="h")
    load = pd.Series(np.tile(SHAPE, days) * (1 + rng.normal(0, 0.02, len(hours))), index=hours)
    return load


def run(model, load, days):
    points, peak_err = [], []
    for d in days:
        info = make_info(d, load, pd.Series(50.0, index=load.index), np.full(24, 60.0))
        try:
            q = model.predict_quantiles(info)
        except Exception:
            continue
        actual = load.reindex(info.timestamps).to_numpy()
        h = int(np.argmax(actual))
        points.append(q[1])
        peak_err.append((q[1][h] - actual[h]) / actual[h] * 100)
    return np.array(points), np.array(peak_err)


def test_lift_and_quantile_reduce_the_under_forecast_at_the_actual_peak():
    load = world()
    days = [date(2023, 1, 5) + timedelta(days=k) for k in range(280)]
    base_p, base_e = run(AdaptiveIntervals(Shaped(), by_regime=True, window_days=365), load, days)
    lift_p, lift_e = run(AdaptiveIntervals(Shaped(), by_regime=True, window_days=365, peak="lift"), load, days)
    q55_p, q55_e = run(AdaptiveIntervals(Shaped(), by_regime=True, window_days=365, peak="quantile"), load, days)
    assert base_e[100:].mean() < -1.0                                   # the maximum of noisy hours sits above the median forecast
    assert lift_e[100:].mean() > base_e[100:].mean() + 0.5
    assert q55_e[100:].mean() > base_e[100:].mean() + 0.15                # the 55th percentile of a 2 % noise is about 0.25 % up
    night = slice(0, 10)
    np.testing.assert_allclose(lift_p[100:, night], base_p[100:, night])   # untouched away from the peak
    np.testing.assert_allclose(q55_p[100:, night], base_p[100:, night])
    assert (lift_p[100:, 18] >= base_p[100:, 18]).all()
