"""Phase S (A30b): linear recalibration per hour of the day."""

from __future__ import annotations

from datetime import date, timedelta
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.recalibrate import LinearRecalibration

START = date(2023, 1, 1)
RNG = np.random.default_rng(0)
TRUTH = {START + timedelta(days=k): 1000 + 300 * RNG.standard_normal() + 200 * np.sin(np.arange(24) / 24 * 2 * np.pi)
         for k in range(200)}


class Shrunk:
    """A forecast that knows the truth but shrinks it toward 1000 by a factor of 0.8."""

    name = "shrunk"

    def predict(self, info):
        return 1000 + 0.8 * (TRUTH[info.day] - 1000)


def info_for(day: date):
    days = [d for d in TRUTH if d <= day - timedelta(days=2)]
    idx = pd.date_range(pd.Timestamp(START), periods=24 * len(days), freq="h")
    load = pd.Series(np.concatenate([TRUTH[d] for d in days]) if days else [], index=idx, dtype=float)
    return SimpleNamespace(day=day, load_history=load, temp_forecast_f=np.full(24, 50.0))


def test_identity_until_enough_days_then_the_shrinkage_is_undone():
    r = LinearRecalibration(Shrunk(), min_days=60, by_regime=False)
    out = {}
    for k in range(120):
        d = START + timedelta(days=k)
        out[d] = r.predict(info_for(d))
    first, last = START, START + timedelta(days=119)
    np.testing.assert_allclose(out[first], Shrunk().predict(SimpleNamespace(day=first)))
    np.testing.assert_allclose(out[last], TRUTH[last], rtol=1e-6)        # slope 1.25 recovered exactly
    _a, b = r.last_coefficients
    np.testing.assert_allclose(b, 1.25, rtol=1e-6)


def test_the_slope_is_clipped():
    r = LinearRecalibration(Shrunk(), min_days=60, by_regime=False, slope_bounds=(0.9, 1.1))
    for k in range(100):
        r.predict(info_for(START + timedelta(days=k)))
    _, b = r.last_coefficients
    assert np.all(b <= 1.1 + 1e-12)


def test_only_known_days_enter():
    r = LinearRecalibration(Shrunk(), min_days=5, by_regime=False)
    for k in range(10):
        r.predict(info_for(START + timedelta(days=k)))
    day = START + timedelta(days=10)
    assert all(d <= day - timedelta(days=2) for d in r.known(SimpleNamespace(day=day)))


def test_regime_falls_back_to_all_days():
    r = LinearRecalibration(Shrunk(), min_days=5, by_regime=True)
    for k in range(10):
        r.predict(info_for(START + timedelta(days=k)))
    r._regime[START + timedelta(days=10)] = 2          # no known day of that regime
    assert len(r.known(SimpleNamespace(day=START + timedelta(days=10)))) == 9


@pytest.mark.parametrize("k", [0, 59])
def test_returns_the_base_before_min_days(k):
    r = LinearRecalibration(Shrunk(), min_days=60, by_regime=False)
    for j in range(k + 1):
        p = r.predict(info_for(START + timedelta(days=j)))
    assert r.last_coefficients is None
    np.testing.assert_allclose(p, Shrunk().predict(SimpleNamespace(day=START + timedelta(days=k))))
