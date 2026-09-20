from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.sky import SKY_COLUMNS, cos_zenith, forecast_as_seen, run_table, sky_frame


def test_cos_zenith_follows_the_sun():
    # Boston, 21 June 2024: solar noon is about 16:45 UTC; night around 05:00 UTC
    utc = pd.date_range("2024-06-21 00:00", periods=24, freq="h")
    c = cos_zenith(utc, 42.36, -71.01)
    assert int(np.argmax(c)) == 16
    assert c.max() == pytest.approx(np.cos(np.radians(42.36 - 23.44)), abs=0.02)      # zenith = latitude - declination
    assert c[5] == 0.0
    winter = cos_zenith(pd.date_range("2024-12-21 00:00", periods=24, freq="h"), 42.36, -71.01)
    assert winter.max() < 0.5 * c.max()
    assert (c >= 0).all()


def test_forecast_as_seen_uses_the_run_of_each_day_and_averages_stations():
    def rows(scale):
        parts = []
        for init in pd.date_range("2024-01-14 12:00", periods=3, freq="D"):
            lead = np.arange(1, 49)
            parts.append(pd.DataFrame({"init_utc": init, "lead_h": lead, "cloud_pct": scale * (init.day * 100 + lead)}))
        return pd.concat(parts, ignore_index=True)

    tables = [run_table(rows(1.0), "cloud_pct"), run_table(rows(3.0), "cloud_pct")]
    s = forecast_as_seen(tables, [date(2024, 1, 16), date(2024, 1, 17)], lambda d: 5.0, (12, 6))
    assert len(s) == 48
    # 16 January, local hour 0 (EST) = lead 17 of the run of the 15th at 12 UTC; mean of the two stations = 2 x
    assert s["2024-01-16 00:00"] == pytest.approx(2.0 * (15 * 100 + 17))
    assert s["2024-01-17 23:00"] == pytest.approx(2.0 * (16 * 100 + 40))
    missing = forecast_as_seen(tables, [date(2024, 1, 20)], lambda d: 5.0, (12, 6))
    assert missing.isna().all()


def test_sky_frame_columns():
    hours = pd.date_range("2024-06-21 00:00", periods=24, freq="h")
    off = pd.Series(4.0, index=hours)
    cloud = pd.Series(50.0, index=hours)
    f = sky_frame(hours, off, 42.36, -71.01, cloud)
    assert list(f.columns) == SKY_COLUMNS
    assert int(f["sun"].to_numpy().argmax()) == 12                     # solar noon near 12:45 EDT
    np.testing.assert_allclose(f["sun_clear"], f["sun"] * 0.5)
    g = sky_frame(hours, off, 42.36, -71.01, None)
    assert g["cloud"].isna().all()
    assert g["sun"].notna().all()
