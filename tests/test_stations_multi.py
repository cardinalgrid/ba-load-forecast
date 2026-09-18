import pytest
from grid_sentinel.stations import BA_STATION

from ba_load_forecast.stations_multi import BA_STATIONS_MULTI, all_icaos, station_table_for

HISTORY = (
    "USAF,WBAN,STATION NAME,CTRY,STATE,ICAO,LAT,LON,ELEV(M),BEGIN,END\n"
    "724080,13739,PHILADELPHIA INTL,US,PA,KPHL,39.873,-75.227,2.0,19410101,20261231\n"
    "725300,94846,CHICAGO OHARE INTL,US,IL,KORD,41.995,-87.934,201.8,19461001,20261231\n"
    "999999,00001,CHICAGO OHARE (OLD),US,IL,KORD,41.995,-87.934,201.8,19300101,19460930\n"
    "725300,00002,CHICAGO OHARE (SHORT),US,IL,KORD,41.995,-87.934,201.8,20200101,20261231\n"
)


def test_every_ba_keeps_its_single_station_first():
    for ba, icaos in BA_STATIONS_MULTI.items():
        assert icaos[0] == BA_STATION[ba]
        assert len(icaos) == len(set(icaos))
    icaos = all_icaos()
    assert len(icaos) == len(set(icaos))
    assert icaos[0] == "KPHL"


def test_station_table_for_picks_the_long_record(tmp_path):
    (tmp_path / "isd-history.csv").write_text(HISTORY)
    t = station_table_for(["KORD", "KPHL"], tmp_path)
    assert list(t["icao"]) == ["KORD", "KPHL"]
    assert t.loc[0, "wban"] == "94846"
    with pytest.raises(ValueError, match="KXXX"):
        station_table_for(["KXXX"], tmp_path)
