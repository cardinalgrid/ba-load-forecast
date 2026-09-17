from datetime import date, datetime

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.cutoff import (
    cutoff_utc,
    forecast_temperature,
    last_load_hour,
    lead_hours,
    run_for_day,
    valid_utc_for_day,
)


def test_cutoff_and_last_load_hour_eastern_standard_time():
    assert cutoff_utc(date(2024, 1, 17), 5) == datetime(2024, 1, 16, 14)
    assert last_load_hour(date(2024, 1, 17)) == datetime(2024, 1, 16, 8)


@pytest.mark.parametrize(
    ("day", "offset", "expected_run", "expected_leads"),
    [
        (date(2024, 1, 17), 5, (date(2024, 1, 16), 12), (17, 40)),   # EST: 12Z + 2 h = 14Z = 09:00 EST
        (date(2024, 7, 17), 4, (date(2024, 7, 16), 6), (22, 45)),    # EDT: 12Z would only be ready at 10:00 EDT
        (date(2024, 7, 17), 5, (date(2024, 7, 16), 12), (17, 40)),   # CDT: 14Z = 09:00 CDT, on the limit
        (date(2024, 1, 17), 8, (date(2024, 1, 16), 12), (20, 43)),   # PST: 12Z ready at 06:00 PST
        (date(2024, 7, 17), 7, (date(2024, 7, 16), 12), (19, 42)),   # PDT
    ],
)
def test_run_for_day_and_leads(day, offset, expected_run, expected_leads):
    run = run_for_day(day, offset)
    assert run == expected_run
    leads = lead_hours(day, offset, run)
    assert (leads[0], leads[-1]) == expected_leads
    assert np.all(np.diff(leads) == 1)


def test_run_for_day_falls_back_to_the_day_before_when_only_12z_is_extracted():
    assert run_for_day(date(2024, 7, 17), 4, init_hours=(12,)) == (date(2024, 7, 15), 12)


def test_valid_utc_accepts_one_offset_per_hour():
    off = np.array([5.0] * 2 + [4.0] * 22)  # a spring-forward day, schematically
    v = valid_utc_for_day(date(2024, 3, 10), off)
    assert v[0] == np.datetime64("2024-03-10T05:00", "ns")
    assert v[2] == np.datetime64("2024-03-10T06:00", "ns")


def test_forecast_temperature_picks_the_run_and_the_hours():
    init = pd.Timestamp("2024-01-16 12:00")
    rows = pd.DataFrame({
        "icao": "KPHL", "init_utc": init, "lead_h": np.arange(1, 49),
        "valid_utc": init + pd.to_timedelta(np.arange(1, 49), unit="h"), "temp_f": np.arange(1, 49, dtype=float),
    })
    other = rows.copy()
    other["init_utc"] = pd.Timestamp("2024-01-16 06:00")
    other["valid_utc"] = other["init_utc"] + pd.to_timedelta(other["lead_h"], unit="h")
    other["temp_f"] = -other["temp_f"]
    t = forecast_temperature(pd.concat([other, rows]), date(2024, 1, 17), 5)
    np.testing.assert_array_equal(t, np.arange(17, 41, dtype=float))
    # a run the archive does not have gives NaN everywhere
    t = forecast_temperature(rows, date(2024, 1, 18), 5)
    assert np.isnan(t).all()
    # a 36 h run covers only part of the day
    t = forecast_temperature(rows[rows["lead_h"] <= 36], date(2024, 1, 17), 5)
    assert np.isnan(t).sum() == 4
