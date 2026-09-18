from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.features import FEATURE_COLUMNS, rows_for_days, target_temperature, training_days
from tests.conftest import make_info


def series(days=40, start="2024-01-01"):
    hours = pd.date_range(start, periods=24 * days, freq="h")
    load = pd.Series(1000.0 + np.arange(len(hours)), index=hours)          # identifies the hour
    temp = pd.Series(50.0 + np.arange(len(hours)) % 24, index=hours)       # hour of the day, in F
    return load, temp


def test_rows_are_causal_and_aligned():
    load, temp = series()
    d = date(2024, 1, 20)
    rows = rows_for_days(load, temp, [d])
    assert list(rows.columns) == [*FEATURE_COLUMNS, "y"]
    assert len(rows) == 24
    r = rows.iloc[5]                                  # 2024-01-20 05:00
    assert r["y"] == load["2024-01-20 05:00"]
    assert r["l_last_known"] == load["2024-01-19 05:00"]   # before the cut-off: yesterday is known
    r = rows.iloc[12]
    assert r["l_last_known"] == load["2024-01-18 12:00"]   # after it: the day before yesterday
    assert r["l_d7"] == load["2024-01-13 12:00"]
    assert r["l_mean24"] == load["2024-01-18 09:00":"2024-01-19 08:00"].mean()
    assert r["t"] == 62.0
    assert r["t_lag1"] == 61.0
    assert r["t_ma6"] == np.mean([56, 57, 58, 59, 60, 61])
    assert r["t_day_max"] == 73.0
    assert r["day_type"] == 1                          # a Saturday
    assert r["hour"] == 12


def test_special_kind_and_training_days_and_station_columns():
    load, temp = series()
    rows = rows_for_days(load, temp, [date(2024, 1, 1)])
    assert (rows["special_kind"] == 3).all()           # New Year's Day resembles a Sunday (kind 2 + 1)
    assert training_days(date(2024, 1, 10), 3) == [date(2024, 1, 8), date(2024, 1, 9), date(2024, 1, 10)]
    st = pd.DataFrame({"KAAA": temp + 1, "KBBB": temp - 1})
    rows = rows_for_days(load, temp, [date(2024, 1, 20)], stations=st)
    assert rows["t_KAAA"].iloc[0] == rows["t"].iloc[0] + 1
    assert rows["t_KBBB"].iloc[0] == rows["t"].iloc[0] - 1


def test_target_temperature_joins_observed_and_path():
    load, temp = series()
    path = np.arange(39, dtype=float) + 100
    info = make_info(date(2024, 1, 20), load, temp, path)
    t = target_temperature(info)
    assert t["2024-01-19 08:00"] == temp["2024-01-19 08:00"]
    assert t["2024-01-19 09:00"] == 100.0
    assert t["2024-01-20 23:00"] == 138.0
    rows = rows_for_days(info.load_history, t, [date(2024, 1, 20)])
    assert rows["t"].iloc[0] == 115.0
    assert np.isnan(rows["y"]).all()
