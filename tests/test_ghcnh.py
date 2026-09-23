"""GHCNh: the NOAA successor of ISD as the supplement source."""
import numpy as np
import pandas as pd

from ba_load_forecast.asos import hourly_from_observations
from ba_load_forecast.ghcnh import parse_ghcnh, station_ids

HEADER = "STATION|Station_name|DATE|Year|Month|Day|Hour|Minute|LATITUDE|LONGITUDE|ELEVATION|temperature|temperature_Measurement_Code|temperature_Quality_Code|temperature_Report_Type|temperature_Source_Code|temperature_Source_Station_ID|dew_point_temperature"
ROWS = [
    "USW00013739|PHILA INTL AP|2025-09-01T00:54:00|2025|09|01|00|54|39.87|-75.23|2.1|20.0||1|FM15|223|ICAO-KPHL|10.0",
    "USW00013739|PHILA INTL AP|2025-09-01T01:54:00|2025|09|01|01|54|39.87|-75.23|2.1|21.1||5|FM15|343|ICAO-KPHL|10.0",
    "USW00013739|PHILA INTL AP|2025-09-01T02:20:00|2025|09|01|02|20|39.87|-75.23|2.1|19.0||1|FM16|223|ICAO-KPHL|10.0",
    "USW00013739|PHILA INTL AP|2025-09-01T03:00:00|2025|09|01|03|00|39.87|-75.23|2.1|30.0||1|FM12|223|ICAO-KPHL|10.0",
    "USW00013739|PHILA INTL AP|2025-09-01T03:54:00|2025|09|01|03|54|39.87|-75.23|2.1|99.0||3|FM15|223|ICAO-KPHL|10.0",
    "USW00013739|PHILA INTL AP|2025-09-01T04:54:00|2025|09|01|04|54|39.87|-75.23|2.1|||1|FM15|223|ICAO-KPHL|10.0",
]


def test_parse_keeps_metar_reports_that_passed_qc_and_converts_to_fahrenheit():
    obs = parse_ghcnh("\n".join([HEADER, *ROWS]) + "\n")
    assert len(obs) == 3                                                       # synop, failed QC and empty rows dropped
    assert obs["temp_f"].iloc[0] == 68.0
    assert abs(obs["temp_f"].iloc[1] - 69.98) < 0.01
    s = hourly_from_observations(obs)
    assert s[pd.Timestamp("2025-09-01 01:00", tz="UTC")] == 68.0             # 00:54 is the 01:00 value
    assert abs(s[pd.Timestamp("2025-09-01 02:00", tz="UTC")] - 69.98) < 0.01    # 01:54 is nearer to 02:00 than 02:20
    assert pd.Timestamp("2025-09-01 03:00", tz="UTC") not in s.index           # 02:20 belongs to 02:00; nothing is left for 03:00
    assert np.isfinite(s.to_numpy()).all()


def test_station_ids_maps_icao_to_ghcn_id(tmp_path):
    cache = tmp_path / "list.csv"
    cache.write_text(
        "GHCN_ID,LATITUDE,LONGITUDE,ELEVATION,STATE,NAME,GSN,(US)HCN_(US)CRN,WMO_ID,ICAO,ISO_CODE\n"
        "USW00013739,39.8733,-75.2269,2.1,PA,PHILA INTL AP,,,72408,KPHL,US\n"
        "USC00013739,39.8,-75.2,2.1,PA,SOMETHING ELSE,,,,KPHL,US\n"
        "CA000000001,45.0,-75.0,1.0,,OTTAWA,,,,KPHL,CA\n"
        "USW00094789,40.6392,-73.7639,2.7,NY,JFK INTL AP,,,74486,KJFK,US\n",
        encoding="utf-8",
    )
    ids = station_ids(["KPHL", "KJFK", "KXXX"], cache)
    assert ids == {"KPHL": "USW00013739", "KJFK": "USW00094789"}
