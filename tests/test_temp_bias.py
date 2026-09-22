"""Correction of the temperature forecast by its own recent bias per local hour."""
from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.information_set import apply_hour_bias, hourly_bias_table, rolling_hour_bias


def test_bias_table_and_rolling_median_recover_a_known_hourly_bias():
    hours = pd.date_range("2024-01-01", periods=24 * 60, freq="h")
    observed = pd.Series(50.0 + 10.0 * np.sin(2 * np.pi * hours.hour / 24), index=hours)
    bias = np.where(hours.hour < 12, 2.0, -1.0)                      # the forecast runs 2 F cold in the morning, 1 F warm later
    seen = observed - bias + np.random.default_rng(0).normal(0, 0.3, len(hours))
    table = hourly_bias_table(observed, seen)
    assert table.shape == (60, 24)
    b = rolling_hour_bias(table, date(2024, 2, 20), window_days=30)
    assert abs(b[3] - 2.0) < 0.3
    assert abs(b[15] + 1.0) < 0.3
    early = rolling_hour_bias(table, date(2024, 1, 5), window_days=30)  # only three known days: no correction
    assert (early == 0.0).all()
    assert (rolling_hour_bias(pd.DataFrame(columns=range(24)), date(2024, 2, 20), 30) == 0.0).all()


def test_apply_hour_bias_moves_each_path_hour_by_its_local_hour():
    path_ts = pd.date_range("2024-02-19 09:00", periods=39, freq="h")
    path = np.zeros(39)
    bias = np.arange(24, dtype=float)
    out = apply_hour_bias(path, path_ts, bias)
    assert out[0] == 9.0 and out[-1] == 23.0
    assert out[15] == 0.0                                                # 00:00 of the target day
