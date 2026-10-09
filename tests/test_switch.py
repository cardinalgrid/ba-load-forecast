"""Phase V: the cold trigger and the switch between a base band and a candidate band."""

from datetime import date, timedelta
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.switch import Memo, TriggerSwitch, cold_trigger

DAY = date(2022, 1, 20)


def info_with(fc_min: float, last_min: float = 30.0, day: date = DAY):
    """400 known days whose minima run from 20 to 59 F, the last known day (D-2) at ``last_min``; the day before (D-1)
    only up to the cut-off."""
    hours = pd.date_range(pd.Timestamp(day - timedelta(days=401)), pd.Timestamp(day - timedelta(days=1)) + pd.Timedelta(hours=8), freq="h")
    k = (np.arange(len(hours)) // 24) % 40
    t = pd.Series(20.0 + k + 10 * np.sin(np.arange(len(hours)) * np.pi / 12) ** 2, index=hours)
    d2 = (hours >= pd.Timestamp(day - timedelta(days=2))) & (hours < pd.Timestamp(day - timedelta(days=1)))
    t[d2] = last_min + 5 * np.sin(np.arange(d2.sum()) * np.pi / 12) ** 2
    fc = np.full(24, fc_min + 8.0)
    fc[5] = fc_min
    return SimpleNamespace(day=day, temp_forecast_f=fc, temp_history_f=t)


def test_cold_trigger_fires_on_extreme_cold_and_on_a_front_only():
    assert cold_trigger(info_with(fc_min=10.0))                        # below every known minimum
    assert not cold_trigger(info_with(fc_min=40.0))                    # an ordinary day
    assert cold_trigger(info_with(fc_min=29.0, last_min=50.0))         # 21 F below the last known day: a front
    assert not cold_trigger(info_with(fc_min=40.0, last_min=50.0))     # 10 F below it: not enough


class Band:
    """A fake band: fixed quantiles, counts its calls (the adaptive state advances once per call)."""

    def __init__(self, name, q, extra=None, levels=()):
        self.name, self.q, self.extra, self.extra_levels, self.calls, self.last_extra = name, np.asarray(q, float), extra, levels, 0, None

    def predict_quantiles(self, info):
        self.calls += 1
        if self.extra is not None:
            self.last_extra = (info.day, np.asarray(self.extra, float))
        return self.q

    def predict(self, info):
        return self.q[1]


def bands():
    levels = (0.01, 0.25, 0.75, 0.99)
    b = Band("base", np.tile([[90.0], [100.0], [110.0]], (1, 24)), np.tile([[80.0], [95.0], [105.0], [120.0]], (1, 24)), levels)
    c = Band("cand", np.tile([[96.0], [106.0], [116.0]], (1, 24)), np.tile([[86.0], [101.0], [111.0], [126.0]], (1, 24)), levels)
    return Memo(b), Memo(c), b, c


def test_switch_keeps_the_base_off_trigger_and_the_lower_tail_on_trigger():
    base, cand, b, c = bands()
    off = TriggerSwitch(base, cand, trigger=lambda i: False)
    on = TriggerSwitch(base, cand, trigger=lambda i: True)
    sym = TriggerSwitch(base, cand, trigger=lambda i: True, asymmetric=False)
    info = SimpleNamespace(day=DAY)
    assert np.allclose(base.predict_quantiles(info), b.q)
    assert np.allclose(off.predict_quantiles(info), b.q)
    q = on.predict_quantiles(info)
    assert np.allclose(q[:, 0], [90.0, 106.0, 116.0])                 # lower level from the base, median and upper from the candidate
    assert np.allclose(on.last_extra[1][:, 0], [80.0, 95.0, 111.0, 126.0])
    assert np.allclose(sym.predict_quantiles(info), c.q)
    assert b.calls == 1 and c.calls == 1                               # each band called once per day, whoever reads it


def test_switch_sorts_the_levels_when_the_mix_crosses():
    levels = (0.25, 0.75)
    b = Band("base", np.tile([[90.0], [100.0], [110.0]], (1, 24)), np.tile([[98.0], [104.0]], (1, 24)), levels)
    c = Band("cand", np.tile([[80.0], [92.0], [101.0]], (1, 24)), np.tile([[86.0], [96.0]], (1, 24)), levels)
    sw = TriggerSwitch(Memo(b), Memo(c), trigger=lambda i: True)
    q = sw.predict_quantiles(SimpleNamespace(day=DAY))
    allq = np.vstack([sw.last_extra[1], q])[np.argsort([0.25, 0.75, 0.05, 0.5, 0.95])]
    assert (np.diff(allq, axis=0) >= 0).all()


def test_memo_remembers_a_forecast_error():
    class Failing(Band):
        def predict_quantiles(self, info):
            self.calls += 1
            raise ForecastError("not enough history")

    f = Failing("base", np.zeros((3, 24)))
    m = Memo(f)
    info = SimpleNamespace(day=DAY)
    for _ in range(2):
        with pytest.raises(ForecastError):
            m.predict_quantiles(info)
    assert f.calls == 1
