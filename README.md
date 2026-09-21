# ba-load-forecast

Day-ahead load forecasting for US balancing authorities (BAs) with public data only, scored against each
BA's own day-ahead forecast. Part of [Cardinal Grid](https://cardinalgrid.com), an independent open
initiative.

> Status: **0.1.0, data layer.** The information cut-off, the archived weather forecasts and the
> loaders exist and are tested; no forecasting model yet.

Documentation: `docs/methods.md` (every rule, model and parameter, with the reason), `docs/reproduce.md`
(inputs and commands in order), and one report per phase (`docs/phase_b.md`, `docs/phase_c.md`,
`docs/phase_d.md`, `docs/hrrr_verification.md`, `docs/day_clusters.md`).

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

## Results of phases B to D

`docs/phase_b.md`, `docs/phase_c.md` and `docs/phase_d.md` score the model families against the BA's own
forecast on the ten development BAs (PJM, MISO, ERCOT, CAISO, SPP, NYISO, ISO-NE, TVA, Duke, BPA) from
2 December 2020 to the end of 2022, under the 9 a.m. cut-off, with the HRRR temperature as the only
weather input. Mean over the BA-days on which every model of phase D produced a forecast (7253), weighted
by each BA's demand; documented load-shed days (`docs/load_shed_days.csv`) left out:

| Model | Stations per BA | Training | MAPE (%) | Median MAPE (%) | Under-forecast at the peak (%) | Days with lower MAPE than `DF` |
|---|---|---|---|---|---|---|
| Ensemble of the additive model and the boosting, weighted by recent error | 4 to 5 | 6 years | 2.76 | 2.40 | −1.99 | 56 % |
| Additive model with an empirical bias correction | 4 to 5 | 6 years | 2.80 | 2.41 | −1.84 | 55 % |
| Gradient boosting | 4 to 5 | 6 years | 2.90 | 2.54 | −1.92 | 53 % |
| The BA's own forecast (`DF`) | | | 3.01 | 2.70 | −1.10 | |
| Additive model (per-hour splines) | 4 to 5 | 6 years | 3.03 | 2.66 | −2.28 | 51 % |
| Gradient boosting | 4 to 5 | 2 years | 3.08 | 2.66 | −2.05 | 50 % |
| Additive model | 1 | 6 years | 3.57 | 3.03 | −2.47 | 43 % |
| Recency-effect regression (Hong) | 4 to 5 | 6 years | 3.66 | 3.19 | −2.23 | 41 % |
| Recency-effect regression (Hong) | 1 | 2 years | 4.27 | 3.64 | −2.49 | 33 % |
| Profile of Note 2 | 1 | | 6.86 | 5.29 | −4.34 | 21 % |

## Phase E: the recipe, in one run (`docs/phase_e_final.md`)

Phase E adds FPL to the development set, settles the recipe and runs it once on the eleven BAs (8163 BA-days,
2 December 2020 to 31 December 2022). The recipe: the additive model with special-day indicators and the
boosting, each on four to six stations per BA and six years of history, combined by their recent error, with
a bias correction read from the errors of the known days in the same temperature regime over the last year;
at ISO-NE and CAISO the additive model carries two linear terms for the installed PV capacity and the boosting
carries the sun's elevation and the HRRR cloud cover as seen at the cut-off. The 90 % interval is read at a level
that adapts to the coverage achieved, one level per regime.

| | MAPE (%) | Median MAPE (%) | Under-forecast at the peak (%) | Days with lower MAPE than `DF` | Coverage of the 90 % interval: year / storms / coldest mornings |
|---|---|---|---|---|---|
| Recipe (`final`) | **2.56** | 2.23 | −1.85 | 61 % | 89.5 % / 76.9 % / 80.7 % |
| The BA's own forecast (`DF`) | 3.04 | 2.74 | −1.26 | | |
| `DF` with its own trailing hourly bias removed (`docs/df_hourly_bias.md`) | 2.17 | | | | |

By BA (MAPE, recipe against `DF`; the Diebold-Mariano test on daily MAPE is significant at 5 % everywhere except FPL):
ahead at PJM (2.34 against 3.65), SPP (2.42 against 3.85), MISO (2.09 against 2.65), NYISO (2.45 against 2.67) and
CAISO (2.64 against 2.80); even at FPL (3.91 against 3.92); behind at ERCOT (2.79 against 2.63), BPA (2.52 against
2.07), Duke (3.31 against 2.84), TVA (3.04 against 2.23) and ISO-NE (3.43 against 2.36). Against `DF` with its
hourly bias removed the recipe is ahead only at SPP.

What each step of phase E was worth, on the same days (`docs/phase_e.md`, `docs/phase_e_sky.md`, `docs/phase_e_pv.md`,
`docs/phase_e_pv2.md`, `docs/phase_e_intervals2.md`):

- **Bias correction by temperature regime** instead of the last 60 days: 2.66 % to 2.58 %; it is also what absorbs the
  Gulf Power step at FPL (July 2022, +11 %) within weeks.
- **Sky features in the boosting** (the short-wave flux is empty in the public HRRR Zarr archive until 2025, so the
  sun's elevation and the total cloud cover stand in): ISO-NE 3.74 % to 3.57 %, CAISO 2.76 % to 2.70 %, FPL unchanged.
- **Installed PV capacity** (Forms EIA-861M and EIA-860M) inside the boosting: nothing, because trees do not extrapolate a
  capacity that is always above its training range. As two linear terms of the additive model (the simplest load
  reconstitution): ISO-NE 3.58 % to 3.43 %, CAISO 2.71 % to 2.65 %. The midday gap to ISO-NE's own forecast narrows by
  0.3 to 0.4 point and remains (about 5 % against 2 % at 11:00): no public forecast irradiance exists at the cut-off
  for these years.
- **Intervals**: the regime-conditional errors read at an adaptive level per regime reach the nominal coverage over the
  year with bands 4 % narrower than adaptive conformal inference alone; inside the storms and on the coldest mornings
  every variant covers 77 to 81 % of the hours.
- **The benchmark itself** (`docs/df_hourly_bias.md`): PJM's published `DF` is stamped one hour earlier than its demand
  from February 2019 on (moved by one hour its MAPE is 2.3 to 2.5 %, not 3.4 to 3.9 %); NYISO's is 2.4 % low at every
  hour, MISO's and SPP's 1 to 4 % high, ISO-NE's 3 to 6 % low before dawn, FPL's 4 to 7 % low in the evening. The
  recipe beats the forecasts as published; it does not yet beat the forecasters.

What the tables say, so far:

- **Several weather stations per BA and six years of training are the two levers that matter.** With one
  airport and two years no model reaches the operators; with four or five stations and six years the
  boosting alone is below the BAs' aggregate, and the ensemble of the additive model and the boosting is
  0.25 point below it, ahead on 56 % of the days. The ensemble beats the BA's forecast at PJM (2.64 %
  against 3.65 %), SPP (2.53 % against 3.88 %), MISO (2.26 % against 2.64 %) and NYISO (2.51 % against
  2.66 %), and loses at ERCOT, CAISO, Duke, TVA, BPA and, by a wide margin, ISO-NE (3.87 % against 2.36 %).
- **A cheap bias correction helps:** the median of the model's relative errors over the last 60 known days,
  per hour of the day, applied to the forecast, takes the additive model from 3.03 % to 2.80 % and reduces
  its under-forecast at the peak more than anything else tried (−2.28 % to −1.84 %).
- **Explicit cold and heat terms** add nothing on top of the spline response with a linear tail.
  **Cleaning the history with grid-data-sentinel** instead of the gross-fault guard changes the annual mean
  by 0.01 point. **Data-driven day labels** from the shape clusters (`docs/day_clusters.md`) make every
  model worse: within a temperature regime the normalised shape barely depends on the calendar.
- **Special days:** on the special days themselves (247 BA-days) indicators take the additive model from
  3.92 % to 3.59 %, below the BA's 3.69 %; on the eves the BAs stay ahead (3.43 % against 3.55 % for the
  ensemble). A separate special-day model changes nothing.
- **At the daily peak the models still under-forecast more than the operators** (−1.8 to −2.0 % against
  −1.1 %). Inside the storms, the bias-corrected additive model matches or beats the BA at the peak in
  Winter Storm Elliott at seven of the ten BAs (PJM −1.2 % against −3.1 %, NYISO −0.5 % against −3.4 %),
  and in Uri at five; the boosting is the worst of the models at the peak outside its training range
  (ERCOT in Uri, −12.9 %).
- **Prediction intervals** (5th to 95th percentile) are too narrow where they matter: empirical intervals
  around the additive model cover 85 % of the hours over the year, 72 % inside the storms and 76 % on the
  30 coldest mornings of each BA; the quantile boosting covers less. Calibration by regime is open work.

Caveats: the training history is cleaned of gross faults only (readings outside 0.2 to 5 times the
four-week median); on the days when a BA shed firm load the "load that occurred" is the load served, so
those BA-days are left out of every table; the BAs' forecasters use weather vendors and internal
information that this study does not have.

## Phase F: three fixes where the recipe lost (`docs/phase_f_final.md`)

Phase F tried one change for each limitation of phase E and kept two. **Coldest days**: the median correction and the
band are read from the 40 known days of the target day's regime nearest in forecast minimum temperature
(`docs/phase_e_intervals3.md`): coverage on the coldest mornings 80.7 % to 84.3 %, band wider there only, and a
slightly better point (2.56 % to 2.53 %); an exponential tail beyond the pool's outer deciles changed nothing.
**Peak**: the point is read at the 60th percentile of the errors around the forecast peak (`docs/phase_e_peak.md`),
because the actual peak is a maximum over noisy hours and the error measured there is biased downward even for an
unbiased forecast: under-forecast at the peak −1.85 % to −1.44 % for 0.016 point of MAPE, better at all 22 event-BA
pairs. **Forecast irradiance** (`docs/phase_e_irradiance.md`): the HRRR surface short-wave flux, read from the GRIB2
archive by byte range because the Zarr archive lacks it before 2025, did not help at ISO-NE or CAISO and was not
adopted.

The recipe after phase F, in one run on the eleven BAs (8163 BA-days):

| | MAPE (%) | Median MAPE (%) | Error at the peak (%) | Under-forecast at the peak (%) | Days with lower MAPE than `DF` | Coverage of the 90 % interval: year / storms / coldest mornings |
|---|---|---|---|---|---|---|
| Recipe after phase F (`final2`) | **2.55** | 2.21 | +0.10 | **−1.37** | 61 % | 88.9 % / 79.0 % / 84.6 % |
| Recipe after phase E (`final`) | 2.56 | 2.23 | −0.79 | −1.85 | 61 % | 89.5 % / 76.9 % / 80.7 % |
| The BA's own forecast (`DF`) | 3.04 | 2.74 | +0.09 | −1.26 | | |
| `DF` with its own trailing hourly bias removed | 2.17 | | | | | |

By BA the picture of phase E holds (ahead at PJM, SPP, MISO, NYISO and CAISO, even at FPL, behind at ERCOT, BPA,
Duke, TVA and ISO-NE; Diebold-Mariano significant everywhere except FPL). Inside the storms the under-forecast at the
peak is now −2.64 % in Uri and −2.55 % in Elliott, against −2.00 % and −2.43 % for `DF`, and the daily MAPE is still
behind the BAs' (3.89 % against 3.62 % in Uri, 4.54 % against 4.49 % in Elliott). What remains open is written in the
limitations: the midday hours at ISO-NE, the storms, and the distance to the forecasters' own accuracy.

## Frozen evaluation: 2023 to 2025, nothing changed (`docs/frozen_evaluation.md`)

Every number above comes from the 25 months on which the recipe was chosen. The recipe was then frozen and run once
on the three following years, 1 January 2023 to 31 December 2025, on the same eleven BAs (10 470 BA-days), with the
models learning day by day from the six years before each day as they would in operation, and nothing changed
after these numbers were seen.

| | MAPE (%) | Median MAPE (%) | Error at the peak (%) | Under-forecast at the peak (%) | Days with lower MAPE than `DF` | Coverage of the 90 % interval: year / storms / coldest mornings |
|---|---|---|---|---|---|---|
| Recipe (`final2`) | **2.52** | 2.18 | +0.06 | −1.37 | 62 % | 89.1 % / 80.8 % / 84.5 % |
| The BA's own forecast (`DF`) | 3.22 | 2.90 | −0.08 | −1.31 | | |
| `DF` with its own trailing hourly bias removed (`docs/df_hourly_bias_2023_2025.md`) | 2.16 | | | | | |

By year: 2.74 % against 2.95 % in 2023, 2.83 % against 3.10 % in 2024, 3.13 % against 3.63 % in 2025. By BA the
picture of the development period holds: ahead at PJM (2.28 against 3.53), SPP (2.54 against 3.43), MISO (1.91 against
2.73) and CAISO; even at NYISO (2.87 against 2.94, the one BA where the Diebold-Mariano test is not significant);
behind at ERCOT, FPL, BPA, Duke, TVA and ISO-NE (3.85 against 2.55). CAISO needs a caveat: its published `DF` breaks
down over these years (5.5 %, 7.0 %, 8.1 %) and the hour-label test flags it as stamped one hour off from 2023 on, so
the 2.81 % against 6.73 % there is a win over the published data, not over the forecaster. Inside the two winter
events of the period the recipe is behind at the peak in January 2024 (−3.45 % against −2.45 %) and level in January
2025 (−2.61 % against −2.63 %), with the daily MAPE slightly behind in the first and ahead in the second. The
interval coverage is where the development left it: at the nominal level over the year, 81 % inside the storms.

Against `DF` with its own hourly bias removed the recipe is ahead at SPP only. The public data's forecasts
are beaten in three years the recipe never saw; the forecasters are not.

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

One to six stations per BA. The 9 a.m. cut-off is an assumption about when BAs run their forecasts. The HRRR is a
weather model with its own error, not the forecast any BA used, and the 2 h availability lag is a
convention. Nothing here describes the internal process of any operator.

## License

Apache-2.0. Ricardo Guerra, Cardinal Grid (independent open initiative).
