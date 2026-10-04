"""Phase S (A30): what "nearest" means for the pool of known days of the interval forecaster."""

from __future__ import annotations

from datetime import date, timedelta

import pytest

from ba_load_forecast.forecasters import quantiles as q
from ba_load_forecast.forecasters.profile import COOLING, HEATING, MILD


class Base:
    name = "base"

    def predict(self, info):
        raise AssertionError("not called")


def filled(nearest_by: str) -> tuple[q.AdaptiveIntervals, list[date]]:
    ai = q.AdaptiveIntervals(Base(), nearest=2, nearest_by=nearest_by)
    days = [date(2024, 7, 1) + timedelta(days=k) for k in range(6)]
    # day 5 is the target; days 0-4 are known
    for k, d in enumerate(days):
        ai._tmin[d] = [70, 60, 75, 50, 72, 71][k]
        ai._tmax_f[d] = [90, 100, 85, 104, 95, 103][k]
        ai._tmean_f[d] = [80, 80, 80, 80, 80, 80][k]
        ai._pmax[d] = [1000, 1200, 900, 1300, 1050, 1250][k]
        ai._regime[d] = COOLING
    return ai, days


@pytest.mark.parametrize(("nearest_by", "expected"), [
    ("tmin", {0, 4}),        # minima 70 and 72 are closest to 71
    ("regime", {1, 3}),      # cooling day: maxima 100 and 104 are closest to 103
    ("peak", {1, 3}),        # base forecast maxima 1200 and 1300 are closest to 1250 (relative)
])
def test_nearest_by_picks_the_days_closest_on_its_measure(nearest_by, expected, monkeypatch):
    ai, days = filled(nearest_by)
    monkeypatch.setattr(q.EmpiricalIntervals, "pool_days", lambda self, info: days[:5])
    info = type("I", (), {"day": days[5]})()
    picked = ai.pool_days(info)
    assert {days.index(d) for d in picked} == expected


def test_regime_uses_the_minimum_on_heating_days_and_the_mean_on_mild_days():
    ai, days = filled("regime")
    ai._regime[days[5]] = HEATING
    assert ai.nearest_key(days[5]) is ai._tmin
    ai._regime[days[5]] = MILD
    assert ai.nearest_key(days[5]) is ai._tmean_f


def test_unknown_nearest_by_is_refused():
    with pytest.raises(ValueError, match="nearest_by"):
        q.AdaptiveIntervals(Base(), nearest_by="tmax")
