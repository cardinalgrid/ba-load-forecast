"""Phase T (A35): training weights on the highest-peak days and an asymmetric boosting loss."""
from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.features import peak_weights
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.boosting import Boosting
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def test_peak_weights_raise_the_highest_days_and_only_near_their_peak():
    hours = pd.date_range("2023-01-01", periods=24 * 10, freq="h")
    base = 100 + 10 * np.sin((hours.hour.to_numpy() - 12) / 24 * 2 * np.pi)       # peak at 18 h
    scale = np.repeat([1.0] * 9 + [1.2], 24)                                       # the last day is 20 % higher
    load = pd.Series(base * scale, index=hours)
    w = peak_weights(hours, load, alpha=1.0, quantile=0.8)
    assert np.all(w[:24 * 9] == 1.0)
    assert np.all(w[24 * 9:] > 4.0)                                                 # ~ 1 + 0.2 / 0.05
    wh = peak_weights(hours, load, alpha=1.0, quantile=0.8, hours=3)
    last = wh[24 * 9:]
    assert last[18] > 4.0 and last[15] > 4.0 and last[21] > 4.0
    assert last[14] == 1.0 and last[3] == 1.0


def test_members_accept_peak_weights_and_the_quantile_loss():
    load, temp = world(days=400)
    info = perfect_weather_info(load, temp, date(2023, 1, 20))
    plain = Boosting(train_days=300, max_iter=40).predict(info)
    weighted = Boosting(train_days=300, max_iter=40, peak_weight=1.0).predict(info)
    q = Boosting(train_days=300, max_iter=40, loss="quantile", loss_quantile=0.7).predict(info)
    assert weighted.shape == q.shape == (24,)
    assert not np.allclose(plain, weighted)
    assert q.mean() > plain.mean()                                                  # leans upward
    a = AdditiveModel(train_days=300, peak_weight=1.0, peak_weight_hours=3).predict(info)
    assert np.isfinite(a).all()
