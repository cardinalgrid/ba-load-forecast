"""The ASOS supplement for the hours the ISD archive does not cover."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.asos import hourly_from_observations, iem_request, parse_iem, read_asos

IEM_TEXT = """station,valid,tmpf
PHL,2025-09-01 00:54,70.00
PHL,2025-09-01 01:54,70.00
PHL,2025-09-01 02:20,68.00
PHL,2025-09-01 02:54,69.00
PHL,2025-09-01 03:54,M
PHL,2025-09-01 04:54,66.00
"""


def test_parse_and_nearest_hour_convention():
    obs = parse_iem(IEM_TEXT)
    assert len(obs) == 5                                                       # the M row is dropped
    s = hourly_from_observations(obs)
    assert s.index.tz is not None
    assert s[pd.Timestamp("2025-09-01 01:00", tz="UTC")] == 70.0               # 00:54 is the 01:00 value
    assert s[pd.Timestamp("2025-09-01 03:00", tz="UTC")] == 69.0               # 02:54 wins over 02:20
    assert pd.Timestamp("2025-09-01 04:00", tz="UTC") not in s.index           # 03:54 was missing
    assert s[pd.Timestamp("2025-09-01 05:00", tz="UTC")] == 66.0
    with pytest.raises(ValueError, match="not an IEM"):
        parse_iem("Too many requests from your IP address")


def test_read_asos_round_trip(tmp_path):
    p = tmp_path / "KPHL.csv"
    parse_iem(IEM_TEXT).to_csv(p, index=False)
    s = read_asos(p)
    assert len(s) == 4
    assert np.isfinite(s.to_numpy()).all()


def test_iem_request_drops_the_k_and_asks_for_routine_hourly_utc():
    q = iem_request("KPHL", date(2025, 8, 1), date(2026, 1, 1))
    assert q["station"] == "PHL"
    assert iem_request(["KPHL", "KORD"], date(2025, 8, 1), date(2026, 1, 1))["station"] == ["PHL", "ORD"]
    assert iem_request("KPBI", date(2025, 8, 1), date(2026, 1, 1))["station"] == "DJT"
    assert q["tz"] == "Etc/UTC"
    assert q["report_type"] == "2"
    assert (q["year1"], q["month1"], q["day1"], q["year2"], q["month2"], q["day2"]) == (2025, 8, 1, 2026, 1, 1)


def test_station_temperature_fills_only_the_gap(tmp_path, monkeypatch):
    """A station whose ISD file is missing entirely is read from the supplement; the fill never overwrites."""
    from ba_load_forecast import information_set as m

    hours_local = pd.date_range("2025-09-01", periods=48, freq="h")
    load = pd.Series(1000.0, index=hours_local)
    monkeypatch.setattr(m, "fetch_isd_lite", lambda *a, **k: None)
    monkeypatch.setattr(m, "load_series_local", lambda *a, **k: load)
    monkeypatch.setattr(m, "utc_offset", lambda *a, **k: pd.Series(4.0, index=hours_local))
    utc = pd.date_range("2025-09-01 04:00", periods=48, freq="h", tz="UTC")
    obs = pd.DataFrame({"valid_utc": utc - pd.Timedelta(minutes=6), "temp_f": np.arange(48, dtype=float)})
    f = tmp_path / "KPHL.csv"
    obs.to_csv(f, index=False)
    s = m.station_temperature_f("724080", "13739", "PJM", 2025, tmp_path, tmp_path, supplement_file=f)
    assert len(s) == 48
    np.testing.assert_allclose(s.to_numpy(), np.arange(48, dtype=float))
    assert m.station_temperature_f("724080", "13739", "PJM", 2025, tmp_path, tmp_path).empty
