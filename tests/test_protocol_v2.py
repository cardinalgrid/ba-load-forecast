"""Protocol v2: spikes in the outcome, reporting faults in the published forecast, hour-label offsets."""
import numpy as np
import pandas as pd

from ba_load_forecast.information_set import apply_label_offsets, forecast_plausible, jumps, plausible


def test_a_spike_against_its_neighbours_is_a_fault_and_a_ramp_is_not():
    day = 1000.0 + 200.0 * np.sin(np.linspace(0, np.pi, 24))
    assert not jumps(day).any()
    assert plausible(day, 1000.0)
    spiked = day.copy()
    spiked[22] = 4500.0                                                 # four and a half times the level, within 5x
    assert jumps(spiked)[22]
    assert not plausible(spiked, 1000.0)
    ramp = np.linspace(1000.0, 1800.0, 24)                              # 3.5 % per hour, legitimate
    assert plausible(ramp, 1300.0)
    edge = day.copy()
    edge[23] = day[22] * 1.6                                            # last hour, judged against its single neighbour
    assert jumps(edge)[23]


def test_published_forecast_faults_make_the_day_unscorable():
    actual = np.full(24, 1000.0)
    assert forecast_plausible(np.full(24, 1030.0), actual)
    zeros = np.full(24, 1030.0)
    zeros[1:6] = 0.0                                                    # the NYISO case: zeros in the published forecast
    assert not forecast_plausible(zeros, actual)
    off = np.full(24, 1030.0)
    off[5] = 1600.0                                                     # 60 % away at one hour
    assert not forecast_plausible(off, actual)
    assert not forecast_plausible(np.full(23, 1000.0), actual)
    partial_actual = actual.copy()
    partial_actual[3] = np.nan                                          # a missing outcome hour is not a forecast fault
    assert forecast_plausible(np.full(24, 1030.0), partial_actual)


def test_label_offsets_move_only_the_documented_period_and_column():
    hours = pd.date_range("2019-01-30", periods=24 * 4, freq="h")
    s = pd.Series(np.arange(len(hours), dtype=float), index=hours)
    offsets = pd.DataFrame({"ba": ["PJM"], "column": ["forecast"], "start": [pd.Timestamp("2019-02-01")],
                            "end": [pd.NaT], "shift_hours": [1]})
    moved = apply_label_offsets(s, "PJM", "forecast", offsets)
    assert moved.loc["2019-01-31 23:00"] == s.loc["2019-01-31 23:00"]  # before the switch: untouched
    assert "2019-02-01 00:00" not in moved.index.astype(str)          # the hour left empty at the switch stays missing
    assert moved.loc["2019-02-01 01:00"] == s.loc["2019-02-01 00:00"]  # after: every value carries the next hour
    assert len(moved) == len(s)
    same = apply_label_offsets(s, "PJM", "demand", offsets)              # other column: untouched
    pd.testing.assert_series_equal(same, s)
    other = apply_label_offsets(s, "MISO", "forecast", offsets)
    pd.testing.assert_series_equal(other, s)
    back = pd.DataFrame({"ba": ["CISO"], "column": ["demand"], "start": [pd.Timestamp("2019-02-01")],
                         "end": [pd.Timestamp("2019-02-01 23:00")], "shift_hours": [-1]})
    b = apply_label_offsets(s, "CISO", "demand", back)
    assert b.loc["2019-01-31 23:00"] == s.loc["2019-02-01 00:00"]      # a moved value wins over the one it lands on
    assert b.loc["2019-02-02 00:00"] == s.loc["2019-02-02 00:00"]      # the period end is respected
