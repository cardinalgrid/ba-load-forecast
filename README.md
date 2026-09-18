# ba-load-forecast

Day-ahead load forecasting for US balancing authorities (BAs) with public data only, scored against each
BA's own day-ahead forecast. Part of [Cardinal Grid](https://cardinalgrid.com), an independent open
initiative.

> Status: **0.1.0, data layer.** The information cut-off, the archived weather forecasts and the
> loaders exist and are tested; no forecasting model yet.

## The question

Every BA reports to the EIA, every hour, the demand that occurred (`D`) and the forecast it made the day
before (`DF`). Cardinal Grid Note 1 measured that forecast across 42 BAs: a weighted MAPE of 3.6 %,
under-forecasts at the daily peak on 59 % of days, and, in the winter storms of 2021 to 2025, peak
under-forecasts of 9 to 14 % at some BAs, early in the storms as the weather worsened (FERC/NERC 2025).
Can an open system, with public load, public weather forecasts and explicit handling of special days,
beat that operational forecast, on ordinary days and on the cold mornings?

## The rules the data layer enforces

**Cut-off.** The forecast for day `D` uses load through the hour beginning 08:00 local time of `D-1`
(everything a forecaster running at 9 a.m. would have) and the latest HRRR run whose initialisation plus
2 h of processing is not after 09:00 local of `D-1`. With the UTC offsets the EIA files carry, that is
the 12 UTC run in standard time everywhere, and the 06 UTC run in the Eastern zone in daylight time.
Forecast leads are 17 to 45 h.

**Weather.** Temperature forecasts come from the HRRR archive on AWS Open Data (`s3://hrrrzarr`), read at
the grid cell nearest each BA's representative station (35 stations, none more than 2 km from its cell).
Runs reach 48 h from 2 December 2020, which sets the start of the evaluation period. Observed temperature
(NOAA ISD-Lite) is used for training and for two reference runs only: perfect weather (a ceiling) and
persistence (the last observed temperature at the same hour, a floor). It never enters a forecast.

**Comparison.** Every forecast is scored against `DF` for the same BA and day, under the same cut-off.

## How good is the weather input? (2024)

`docs/hrrr_verification.md` compares the HRRR 2 m temperature at each station's grid cell with the
ISD-Lite observation for the same hour, over the leads a 9 a.m. forecast uses (17 to 45 h), for 2024:
738 101 pairs at 35 stations.

- Overall the forecast runs slightly cool: bias −1.4 °F, MAE 3.1 °F, RMSE 4.0 °F. The MAE grows from
  about 2.7 °F at the shortest leads to about 3.7 °F at 45 h.
- The sign flips with temperature. Below 20 °F the forecast is warm on average (+0.7 °F), between 20 and
  32 °F +0.5 °F, and above 32 °F cool by 1.2 to 1.7 °F.
- On the 30 coldest mornings of each station (hours 04:00 to 09:00 local), bias is −0.4 °F and MAE 3.0 °F
  overall, but the sign depends on the place: the forecast is warm at the northern and inland stations
  (Columbia SC +3.3 °F, Spokane +2.8 °F, Boise +2.6 °F) and cold at the southern ones (Phoenix −5.2 °F,
  Miami −4.5 °F, Tampa −4.1 °F), whose "coldest mornings" are mild in absolute terms.

A forecast that runs warm on a cold morning pushes a temperature-driven load forecast down, which is the
direction of the errors the storm reviews describe. Whether that is what happened at any BA is a question
for the forecasting phases, not for this table.

## Layout

| Module | Responsibility |
|---|---|
| `hrrr_grid.py` | Nearest HRRR grid cell and Zarr chunk for each station |
| `hrrr.py` | Point reads from the public archive; resumable extraction to parquet; consolidation per station |
| `cutoff.py` | The 9 a.m. rule: the run available for each BA-day, leads, the forecast temperature of a day |
| `information_set.py` | `Loader.information_set(ba, day)`: load history to the cut-off, forecast and observed temperature, the BA's `DF`, the outcome |
| `scripts/extract_hrrr.py` | Extraction command line (`scripts/run_extract.cmd` runs it detached, year by year) |
| `scripts/verify_hrrr.py` | HRRR against ISD-Lite: error by station, lead, month, temperature and on the coldest mornings |

## Install and use

```bash
pip install -e ".[hrrr,dev]"          # needs grid-data-sentinel[pandas] for the public-data helpers
python scripts/extract_hrrr.py --start 2020-12-02 --end 2025-12-31 --init-hours 12 6
python scripts/extract_hrrr.py --consolidate
python scripts/verify_hrrr.py --years 2024
```

```python
from datetime import date
from ba_load_forecast.information_set import Loader

loader = Loader(tidy_dir="../ba-forecast-scorecard/data/tidy", isd_dir="data/isd", hrrr_dir="data/hrrr")
info = loader.information_set("PJM", date(2024, 1, 17))
info.load_history          # hourly load, local hour beginning, ends 2024-01-16 08:00
info.run                   # (2024-01-16, 12): the HRRR run available at the cut-off
info.temp_forecast_f       # 24 values for 2024-01-17 from that run
info.ba_forecast, info.actual   # the BA's DF and what occurred, for scoring
```

Tests: `pytest -q` (synthetic data; the tests that touch the archives are marked `network` and skipped by
default).

## Data sources

EIA-930 hourly demand and day-ahead forecast (tidy files from
[ba-forecast-scorecard](https://github.com/cardinalgrid/ba-forecast-scorecard)); NOAA ISD-Lite hourly
observations; HRRR forecasts from the [AWS Open Data archive](https://registry.opendata.aws/noaa-hrrr-pds/)
in Zarr (`hrrrzarr`, maintained by the University of Utah). The station assignment per BA is the one of
Cardinal Grid Note 2 and of [grid-data-sentinel](https://github.com/cardinalgrid/grid-data-sentinel).

## Limitations

One station per BA. The 9 a.m. cut-off is an assumption about when BAs run their forecasts. The HRRR is a
weather model with its own error, not the forecast any BA used, and the 2 h availability lag is a
convention. Nothing here describes the internal process of any operator.

## License

Apache-2.0. Ricardo Guerra, Cardinal Grid (independent open initiative).
