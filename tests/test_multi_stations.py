from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast import information_set as mod
from tests.conftest import write_hrrr, write_isd

HISTORY_TWO = (
    "USAF,WBAN,STATION NAME,CTRY,STATE,ICAO,LAT,LON,ELEV(M),BEGIN,END\n"
    "724080,13739,PHILADELPHIA INTL,US,PA,KPHL,39.873,-75.227,2.0,19410101,20261231\n"
    "725000,00001,TEST FIELD,US,PA,KTST,40.000,-76.000,10.0,19410101,20261231\n"
)


def test_multi_station_loader_averages_and_attaches_stations(public_data, monkeypatch):
    tidy, isd, hrrr = public_data
    (isd / "isd-history.csv").write_text(HISTORY_TWO)
    write_isd(isd, "725000", "00001", "2023-11-30 00:00", "2024-01-22 00:00")     # same synthetic temperature
    (isd / "isd-history.csv").write_text(HISTORY_TWO)                             # write_isd overwrote it
    write_hrrr(hrrr.parent / "hrrr_multi", "KTST", "2024-01-15 12:00", n_lead=48)
    monkeypatch.setattr(mod, "BA_STATIONS_MULTI", {"PJM": ("KPHL", "KTST")})
    loader = mod.Loader(tidy, isd, hrrr, history_days=30, stations="multi")
    info = loader.information_set("PJM", date(2024, 1, 16))
    assert info.stations == ["KPHL", "KTST"]
    assert list(info.temp_history_stations_f.columns) == ["KPHL", "KTST"]
    assert info.temp_history_stations_f.index.equals(info.load_history.index)
    pd.testing.assert_series_equal(info.temp_history_f, info.temp_history_stations_f.mean(axis=1), check_names=False)
    assert list(info.temp_forecast_path_stations_f.columns) == ["KPHL", "KTST"]
    np.testing.assert_array_equal(info.temp_forecast_f, 100.0 + np.arange(17, 41))    # both stations carry the same path
    single = mod.Loader(tidy, isd, hrrr, history_days=30).information_set("PJM", date(2024, 1, 16))
    assert single.stations == ["KPHL"]
    assert single.temp_history_stations_f is None


def test_oracle_temperature_replaces_the_path_by_the_observed_temperature(public_data, monkeypatch):
    """A29: with oracle_temperature the target day's temperature 'forecast' is the observed temperature."""
    tidy, isd, hrrr = public_data
    (isd / "isd-history.csv").write_text(HISTORY_TWO)
    write_isd(isd, "725000", "00001", "2023-11-30 00:00", "2024-01-22 00:00")
    (isd / "isd-history.csv").write_text(HISTORY_TWO)
    write_hrrr(hrrr.parent / "hrrr_multi", "KTST", "2024-01-15 12:00", n_lead=48)
    monkeypatch.setattr(mod, "BA_STATIONS_MULTI", {"PJM": ("KPHL", "KTST")})
    plain = mod.Loader(tidy, isd, hrrr, history_days=30, stations="multi").information_set("PJM", date(2024, 1, 16))
    oracle = mod.Loader(tidy, isd, hrrr, history_days=30, stations="multi", oracle_temperature=True).information_set("PJM", date(2024, 1, 16))
    ok = np.isfinite(oracle.temp_observed_f)
    assert ok.sum() >= 20
    np.testing.assert_allclose(oracle.temp_forecast_f[ok], oracle.temp_observed_f[ok])
    assert not np.allclose(plain.temp_forecast_f[ok], plain.temp_observed_f[ok])      # the synthetic forecast differs
    np.testing.assert_array_equal(oracle.load_history.to_numpy(), plain.load_history.to_numpy())   # nothing else changes
