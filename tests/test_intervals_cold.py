"""Nearest-temperature pool and exponential tail: wider bands on the coldest days, unchanged on the mild ones."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from tests.conftest import make_info
from tests.test_intervals import Flat


def cold_world(seed=3, days=420):
    """Errors grow with the cold: sigma 1 % at 65 F, 6 % at 0 F, linearly; one day in three is cold."""
    rng = np.random.default_rng(seed)
    hours = pd.date_range("2023-01-01", periods=24 * days, freq="h")
    day_index = (hours.normalize() - hours[0].normalize()).days.to_numpy()
    temps = np.where(day_index % 3 == 0, 40.0 - 40.0 * ((day_index // 3) % 4) / 3.0, 65.0)   # cold days at 40, 27, 13, 0 F
    sigma = 0.01 + 0.05 * np.clip((65.0 - temps) / 65.0, 0, 1)
    load = pd.Series(1000.0 * (1 + rng.normal(0, 1, len(hours)) * sigma), index=hours)
    temp_of_day = {pd.Timestamp(h).date(): float(t) for h, t in zip(hours[::24], temps[::24], strict=True)}
    return load, temp_of_day


def bands(model, load, temp_of_day, days, score_from=None):
    """Run the model day by day; keep coverage and width from ``score_from`` on (the pool needs time to fill)."""
    out = {}
    for d in days:
        info = make_info(d, load, pd.Series(50.0, index=load.index), np.full(24, temp_of_day[d]))
        try:
            q = model.predict_quantiles(info)
        except Exception:
            continue
        if score_from is not None and d < score_from:
            continue
        actual = load.reindex(info.timestamps).to_numpy()
        out[d] = (float(np.mean((actual >= q[0]) & (actual <= q[2]))), float(np.mean(q[2] - q[0])) / 1000.0)
    return pd.DataFrame(out, index=["cover", "width"]).T


def test_nearest_pool_widens_the_coldest_days_and_not_the_mild_ones():
    load, temp_of_day = cold_world()
    days = [date(2023, 1, 5) + timedelta(days=k) for k in range(400)]
    fixed = dict(by_regime=True, window_days=365, gamma=0.0)              # no level adaptation: the pool alone is compared
    base = bands(AdaptiveIntervals(Flat(), **fixed), load, temp_of_day, days, score_from=days[200])
    nn = bands(AdaptiveIntervals(Flat(), **fixed, nearest=40), load, temp_of_day, days, score_from=days[200])
    coldest = [d for d in base.index if temp_of_day[d] < 5.0]
    mild = [d for d in base.index if temp_of_day[d] == 65.0]
    assert nn.loc[coldest, "width"].mean() > base.loc[coldest, "width"].mean() * 1.1   # the pool of the coldest days is wider
    assert nn.loc[coldest, "cover"].mean() > base.loc[coldest, "cover"].mean()
    assert abs(nn.loc[mild, "width"].mean() - base.loc[mild, "width"].mean()) < base.loc[mild, "width"].mean() * 0.15


def test_exponential_tail_gives_a_defined_level_below_the_observed_minimum():
    rng = np.random.default_rng(0)
    e = rng.normal(0, 0.02, size=(60, 24))
    model = AdaptiveIntervals(Flat(), tail=True)
    p = np.full(24, 1000.0)
    five = AdaptiveIntervals(Flat()).band(p, e, (0.05, 0.5, 0.95))
    tail = model.band(p, e, (0.01, 0.5, 0.99))
    assert (tail[0] < five[0]).all()                                       # the 1 % level lies beyond the empirical 5 %
    assert (tail[2] > five[2]).all()
    assert np.isfinite(tail).all()
