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

## How good is the weather input? (December 2020 to 2025)

`docs/hrrr_verification.md` compares the HRRR 2 m temperature at each station's grid cell with the
ISD-Lite observation for the same hour, over the leads a 9 a.m. forecast uses (17 to 45 h), from
2 December 2020 to the end of 2025: 3.5 million pairs at 35 stations.

- Overall the forecast runs slightly cool: bias −1.2 °F, MAE 3.1 °F, RMSE 4.0 °F. The MAE grows from
  about 3.0 °F at the shortest leads to about 3.5 °F at 45 h.
- The sign flips with temperature. Below 20 °F the forecast is warm on average (+1.4 °F, MAE 3.8 °F),
  between 20 and 32 °F +0.5 °F, and above 32 °F cool by 1.0 to 1.5 °F.
- On the 30 coldest mornings of each station (hours 04:00 to 09:00 local), the sign depends on the place:
  warm at Columbia SC (+5.7 °F), Moses Lake (+3.6 °F), Portland (+3.0 °F) and Spokane (+2.8 °F); cold at
  Miami (−5.1 °F), Phoenix (−5.0 °F) and Tampa (−4.0 °F), whose "coldest mornings" are mild in absolute
  terms.
- In the four winter storms (all hours of the event days), the pooled bias is between −0.5 °F (Uri) and
  −1.6 °F (January 2025), with MAE 3.3 to 3.7 °F. The largest warm errors are in the Pacific Northwest
  during Elliott (Portland +7.5 °F, Spokane +4.9 °F) and at Denver during Uri (+4.0 °F); during Elliott the
  forecast was cold in the Southeast (Louisville −4.9 °F, Nashville −4.5 °F, Atlanta −3.2 °F).

A forecast that runs warm on a cold morning pushes a temperature-driven load forecast down, which is the
direction of the errors the storm reviews describe. Whether that is what happened at any BA is a question
for the forecasting phases, not for this table: at the Southeast stations, where the largest Elliott
under-forecast was reported, the public weather forecast erred cold, not warm.

## Results so far: phase B (floors, profile, recency regression)

`docs/phase_b.md` scores the simplest families against the BA's own forecast on the ten development
BAs (PJM, MISO, ERCOT, CAISO, SPP, NYISO, ISO-NE, TVA, Duke, BPA) from 2 December 2020 to the end of
2022, under the 9 a.m. cut-off, with the HRRR temperature as the only weather input and one station per
BA. Mean over BA-days, weighted by each BA's demand:

| Model | MAPE (%) | Median MAPE (%) | Under-forecast at the peak (%) | Days with lower MAPE than `DF` |
|---|---|---|---|---|
| The BA's own forecast (`DF`) | 3.00 | 2.70 | −1.12 | |
| Recency-effect regression (Hong) | 4.28 | 3.64 | −2.49 | 33 % |
| Profile (Note 2) | 6.87 | 5.29 | −4.34 | 21 % |
| Last known day | 6.95 | 5.82 | −4.24 | 19 % |
| Mean of the same day type, 2 weeks | 7.12 | 5.43 | −4.40 | 20 % |
| Same weekday last week | 8.66 | 6.73 | −5.26 | 15 % |

The vanilla regression does not beat the operators: the difference is significant at every BA except
SPP, where the two tie (3.88 % against 3.86 %, Diebold-Mariano p = 0.91, the model ahead on 49 % of
days). It also under-forecasts the daily peak more than the BAs do, and does worse than they do inside
Winter Storms Uri and Elliott at most BAs. CAISO is the clearest case of what one station costs: the
regression (5.7 %) is behind the two-week floor there (5.3 %). Two caveats: the training history was
cleaned only of gross faults (readings outside 0.2 to 5 times the four-week median); and on the days
when a BA shed firm load (ERCOT, SPP and MISO South in Uri; TVA and Duke in Elliott, among others) the
"load that occurred" is the load served, not the demand, so those BA-days are listed in
`docs/load_shed_days.csv` with their source and left out of every table (10 of 7473 BA-days here).

The next phases add the semi-parametric additive model, gradient boosting, several stations per BA,
the three treatments of special days and the ensembles, on the same harness.

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
