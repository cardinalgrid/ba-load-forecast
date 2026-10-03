"""Phase Q: the second stage for the daily peak (``PeakStage``), on synthetic days."""

from __future__ import annotations

from datetime import date, timedelta
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.peak import PeakStage

H = np.arange(24)
CURVE = 1000.0 + 400.0 * np.exp(-0.5 * ((H - 17) / 3.0) ** 2)      # peak at 17 h


class FakeBand:
    """Issues [0.95, 1, 1.05] x a fixed curve; keeps ``_issued`` like AdaptiveIntervals."""

    def __init__(self):
        self.base = object()
        self.name = "band"
        self.extra_levels = ()
        self.last_extra = None
        self._issued = {}

    def predict(self, info):
        return CURVE.copy()

    def predict_quantiles(self, info):
        q = np.vstack([0.95 * CURVE, CURVE, 1.05 * CURVE])
        self._issued[info.day] = (q[0], q[-1])
        return q


class FakeMember:
    def __init__(self, shift_h, scale):
        self.name = f"m{shift_h}"
        self.curve = 1000.0 + scale * 400.0 * np.exp(-0.5 * ((H - 17 - shift_h) / 3.0) ** 2)

    def predict(self, info):
        return self.curve.copy()


def info_for(day: date, actual_scale: float = 1.0, tmax: float = 80.0, start: date = date(2020, 1, 1)):
    """Load known up to the end of D-2, each day's actual = actual_scale x CURVE; temperatures mild."""
    days = pd.date_range(pd.Timestamp(start), pd.Timestamp(day - timedelta(days=2)), freq="D")
    idx = pd.date_range(days[0], periods=24 * len(days), freq="h")
    load = pd.Series(np.tile(CURVE * actual_scale, len(days)), index=idx)
    temp = pd.Series(np.tile(60.0 + 15.0 * np.sin(H / 24 * 2 * np.pi), len(days)), index=idx)
    tf = np.full(24, 60.0)
    tf[15] = tmax
    return SimpleNamespace(ba="X", day=day, load_history=load, temp_history_f=temp, temp_forecast_f=tf,
                           nbm_spread_f=2.0, day_type=0, special_day=None)


def test_bump_scales_the_maximum_and_leaves_far_hours():
    st = PeakStage(FakeBand(), mode="members", sigma_h=2.5)
    f = st.bump(CURVE, 1.10)
    assert f[17] == pytest.approx(1.10)
    assert f[5] == pytest.approx(1.0, abs=1e-6)
    assert (CURVE * f).max() == pytest.approx(1.10 * CURVE.max())


def test_members_mode_lifts_by_the_mean_of_the_members_maxima_and_never_lowers():
    band = FakeBand()
    st = PeakStage(band, members=[FakeMember(-2, 1.1), FakeMember(2, 1.1)], mode="members")
    q = st.predict_quantiles(info_for(date(2021, 1, 10)))
    expected = np.mean([m.curve.max() for m in st.members]) / CURVE.max()
    assert st.last_ratio == pytest.approx(expected)
    assert q[1].max() == pytest.approx(expected * CURVE.max())
    low = PeakStage(FakeBand(), members=[FakeMember(0, 0.5)], mode="members")
    low.predict_quantiles(info_for(date(2021, 1, 10)))
    assert low.last_ratio == 1.0


def test_learned_mode_waits_for_min_days_then_learns_a_constant_peak_bias():
    st = PeakStage(FakeBand(), members=[FakeMember(0, 1.0)], mode="learned", min_days=30)
    start = date(2021, 1, 1)
    ratios = []
    for k in range(60):
        d = start + timedelta(days=k)
        st.predict_quantiles(info_for(d, actual_scale=1.04, start=date(2020, 12, 1)))
        ratios.append(st.last_ratio)
    assert ratios[0] == 1.0                                   # nothing known yet
    assert ratios[-1] == pytest.approx(1.04, abs=0.005)       # actual max is 4 % above the issued max every day


def test_the_stage_never_reads_the_target_day():
    st = PeakStage(FakeBand(), mode="learned", min_days=5)
    d = date(2021, 3, 1)
    info = info_for(d, start=date(2021, 1, 1))
    assert info.load_history.index.max() < pd.Timestamp(d - timedelta(days=1))
    st.predict_quantiles(info)
    assert all(k <= d - timedelta(days=2) for k in st.known_targets(info))


def test_learned_extreme_is_one_on_mild_days_and_the_band_issued_follows_the_stage():
    band = FakeBand()
    st = PeakStage(band, mode="learned_extreme", min_days=5)
    d = date(2021, 3, 1)
    q = st.predict_quantiles(info_for(d, tmax=70.0, start=date(2020, 9, 1)))
    assert st.last_ratio == 1.0
    _lo, hi = st.band._issued[d]
    assert np.allclose(hi, q[-1])
    assert st.band is not band                                # its own copy of the band
    assert st.band.base is band.base                          # sharing the base forecaster


def test_is_extreme_on_a_record_hot_forecast():
    st = PeakStage(FakeBand(), mode="learned_extreme")
    assert st.is_extreme(info_for(date(2021, 3, 1), tmax=110.0, start=date(2020, 9, 1)))
    assert not st.is_extreme(info_for(date(2021, 3, 1), tmax=70.0, start=date(2020, 9, 1)))
