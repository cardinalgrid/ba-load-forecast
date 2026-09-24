"""Humidity and wind: readers and the apparent-temperature formulas."""
import gzip

import numpy as np
import pandas as pd

from ba_load_forecast.weather_extra import (
    apparent_temperature_f,
    heat_index_f,
    read_isd_lite_field,
    relative_humidity,
    weather_columns,
    wind_chill_f,
)


def test_isd_lite_fields_are_read_in_the_right_units(tmp_path):
    p = tmp_path / "724080-13739-2024.gz"
    with gzip.open(p, "wt") as fh:
        fh.write("2024 01 01 00   61  -39 10165   0    0  4 -9999 -9999\n")     # 6.1 C, dew -3.9 C, calm
        fh.write("2024 01 01 01   56 -9999 10164 180   21 -9999 0 -9999\n")     # dew point missing, wind 2.1 m/s
    t = read_isd_lite_field(p, "temp_f")
    d = read_isd_lite_field(p, "dewpoint_f")
    w = read_isd_lite_field(p, "wind_ms")
    assert abs(t.iloc[0] - (6.1 * 9 / 5 + 32)) < 1e-9
    assert len(d) == 1
    assert abs(d.iloc[0] - (-3.9 * 9 / 5 + 32)) < 1e-9
    assert w.tolist() == [0.0, 2.1]
    assert t.index.tz is not None


def test_relative_humidity_and_heat_index_match_nws_examples():
    assert abs(relative_humidity(70.0, 70.0) - 100.0) < 1e-6
    rh = relative_humidity(90.0, 70.0)
    assert 50 < rh < 55                                                      # 32.2 C / 21.1 C: about 52 %
    assert abs(heat_index_f(90.0, 50.0) - 95.0) < 1.5                         # NWS chart: 90 F at 50 % is 95 F
    assert heat_index_f(75.0, 90.0) == 75.0                                   # below 80 F the index is the temperature
    assert abs(heat_index_f(100.0, 10.0) - 96.0) < 2.0                        # the low-humidity adjustment
    assert abs(heat_index_f(84.0, 90.0) - 98.0) < 2.0                         # NWS chart: 84 F at 90 % is 98 F


def test_wind_chill_matches_the_nws_chart_and_stops_at_its_limits():
    assert abs(wind_chill_f(0.0, 15.0 / 2.23694) - (-19.0)) < 1.0            # 0 F at 15 mph: -19 F
    assert wind_chill_f(30.0, 1.0 / 2.23694) == 30.0                          # under 3 mph: no chill
    assert wind_chill_f(55.0, 10.0) == 55.0                                   # above 50 F: no chill


def test_apparent_temperature_blends_and_tolerates_missing_inputs():
    t = np.array([95.0, 20.0, 70.0, 95.0])
    td = np.array([75.0, 10.0, 50.0, np.nan])
    w = np.array([2.0, 8.0, 3.0, np.nan])
    a = apparent_temperature_f(t, td, w)
    assert a[0] > 95.0                                                        # hot and humid: above the temperature
    assert a[1] < 20.0                                                        # cold and windy: below
    assert a[2] == 70.0                                                       # mild: unchanged
    assert a[3] == 95.0                                                       # nothing known: unchanged
    cols = weather_columns(t, td, w)
    assert set(cols) == {"dewpoint", "dpd", "rh", "heat_index", "wind", "wind_chill"}
    assert np.isnan(cols["rh"][3])
    assert cols["heat_index"][3] == 95.0
    assert cols["wind_chill"][3] == 95.0
    assert pd.Series(cols["dpd"]).iloc[0] == 20.0
