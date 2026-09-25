# Methods

This page states what every piece of the study does, with which parameters, and why that value. The
module docstrings say the same in fewer words; `docs/reproduce.md` lists the commands; the phase
reports (`docs/phase_b.md`, `docs/phase_c.md`, `docs/phase_d.md`) hold the numbers.

## 1. The question and the comparison

Every U.S. balancing authority (BA) reports to the EIA the hourly demand that occurred (`D`) and the
day-ahead forecast it made the day before (`DF`). The study asks whether an open system built from
public data only can match that operational forecast, on ordinary days and at the daily peak during
winter storms. Every model is therefore scored against `DF` for the same BA and day, under the same
information cut-off, and `DF` is scored by the same functions as the models.

The models are developed on ten BAs (PJM, MISO, ERCOT, CAISO, SPP, NYISO, ISO-NE, TVA, Duke Energy
Carolinas, BPA) from 2 December 2020 to 31 December 2022, a period that contains Winter Storms Uri
and Elliott. Winter Storms Gerri and Heather (January 2024) and the January 2025 Arctic events are
not used in any modelling decision.

## 2. Data and what a forecaster is allowed to see

| Item | Rule | Reason |
|---|---|---|
| Load | the raw `demand` column of EIA-930, local time, hour beginning | the column Cardinal Grid Note 1 scored; the EIA's adjusted column repairs some BAs and not others |
| Start of the history | never before 1 July 2015 | EIA-930 starts then |
| Cut-off | load through the hour beginning 08:00 local of the day before the target day | what a forecaster running at 9 a.m. has |
| Weather forecast | the latest HRRR run among 12 and 06 UTC whose initialisation plus 2 h is not after 09:00 local of the day before, with the UTC offset the EIA files carry for that day | 2 h is the time a 48 h run takes to finish; the rule gives 12 UTC everywhere except the Eastern zone in daylight time (06 UTC); leads are 17 to 45 h |
| Evaluation period | from 2 December 2020 | the public Zarr archive has 48 h runs only from that day; from August 2018 to then runs reach 36 h, and a 9 a.m. cut-off needs at least 39 h to cover the target day |
| Temperature path | 39 hours of the same run, from 09:00 of the day before to 23:00 of the target day | lags and moving averages of temperature need the rest of the day before; the forecaster had those hours too |
| Observed temperature | NOAA ISD-Lite; used to train, never to forecast | standard practice: train on observations, run on forecasts |
| Observed temperature after 27 August 2025 | NOAA's GHCNh (Global Historical Climatology Network hourly), the product NCEI names as the replacement of ISD: the METAR reports (FM15, FM16) of the same airports that passed quality control, assigned to the nearest hour as ISD-Lite does, used only where the ISD series is missing (`ghcnh.py`, `scripts/fetch_ghcnh.py`, `data/ghcnh/`); for the hours GHCNh lacks, the ASOS/METAR archive of the Iowa Environmental Mesonet, the NWS observations of the same airports (`asos.py`, `scripts/fetch_asos.py`, `data/asos/`), applied second | NOAA's ISD and ISD-Lite files for 2025 end on 27 August 2025 for every station used here (last modified 29 August 2025, checked on 23 September 2026; the NCEI Access Data Service ends the same day). GHCNh for 2025 runs to 31 December but every one of the 67 station files has the same hole of 90 hours from 30 August 00 UTC to 2 September 2025, plus a few shorter ones; the IEM archive covers them. Over the 143 613 station-hours both cover (49 stations, September to December 2025) the two agree to 0.045 F on average, 27 hours differ by more than 1 F; against ISD-Lite over its last 30 days GHCNh differs by 0.02 F and IEM by 0.07 F on average (`docs/supplement_check.md`). Without the supplement the additive model and the recency regression cannot run from that day on (their temperature lags need the observed hours before the target day) and the recipe is the boosting alone for the last four months of 2025 |
| Gaps in temperature | linear interpolation of up to 6 h, interior only | stations miss isolated hours |
| Gross-fault guard | a reading outside 0.2 to 5 times the median of the previous four weeks (672 h window, at least 168 h, shifted one hour) becomes missing, in the history only | the hard gross-ratio rule of grid-data-sentinel; it removes only what no load could be (the public PJM record contains a reading of 2 147 480 000 MW) |
| Implausible outcome | if any hour of the load that occurred is outside 0.2 to 5 times the median of the last 672 known hours, the day scores nobody, `DF` included | an error cannot be measured against a broken reading; 0.3 % of days |
| Blind copy | a forecaster receives the information set with the outcome and the observed temperature of the target day replaced by missing values | no model can use the result, by construction; a test with a cheating forecaster checks it |
| Absent HRRR run | 8 of 3712 runs are not in the archive; the model declines the day and the day counts in the coverage table | no weather forecast is invented |
| Documented load-shed days | the BA-days in `docs/load_shed_days.csv` (source, page and quote per row) are left out of every table and reported apart | on those days the load that occurred is the load served, not the demand |

## 3. Weather stations

One station per BA is the main airport of the largest load centre, the assignment of Cardinal Grid
Note 2. For the development BAs a second table (`stations_multi.py`, `docs/stations_grid_multi.csv`)
adds the airports of the largest cities in each footprint, four or five per BA. Stations are weighted
equally: the additive model and the regression use the mean, the boosting sees the mean and one column
per station. A population weighting was not tested. The HRRR cell is the nearest by great-circle
distance (at most 2.0 km); the ISD record is the one that spans July 2015 to January 2025.

## 4. Evaluation

Per BA and day (`metrics.py`): hourly MAPE over the hours with a positive outcome; error at the peak =
(forecast at the hour of the actual peak − actual peak) / actual peak, taken at the hour of the
**actual** peak so that a forecast peak at another hour is not rewarded; the negative part of that
error (under-forecast); the error in the hour of the peak. A day is skipped with more than two missing
outcome hours or any missing forecast hour.

Aggregation (`report.py`): only BA-days on which **every** model of a report produced a forecast enter
its tables, so that all models are measured on the same days; the number of days, and the value of `DF`,
therefore differ slightly from one report to another (3.00 to 3.03 %). Means are taken per BA and, across
BAs, weighted by each BA's mean demand, as in Note 1. A day is won when the model's MAPE is below the
BA's, or when its under-forecast at the peak is smaller. The Diebold-Mariano test [1] compares daily
MAPE (or peak error) series with absolute loss at horizon one, the small-sample correction of Harvey,
Leybourne and Newbold [2] and a normal p-value (700 to 750 days per BA); a negative statistic favours
the model. Winter events are the calendar days of `grid_sentinel.events`. Special days and their eves
have a table of their own. Quantile forecasts are scored with the pinball loss in percent of the
outcome at the 5th, 50th and 95th percentiles, the coverage and relative width of the 5-95 band and
whether the actual peak fell inside it, over all days, the event days and the 30 coldest days of each
BA by observed minimum temperature.

## 4b. Band and tail, apart

The 90 % band answers where the outcome falls on most hours; the tail answers how far it goes when it leaves the band, which the 40 nearest days cannot estimate on their own (two of them lie beyond the 95th percentile). `scripts/tail_analysis.py` (`docs/tail_analysis.md`) therefore judges the two apart on the scored hours of 2023 to 2025: the band by coverage, width and the exceedance rate per side; the tail by the mean excess beyond the bound in percent of the outcome, the worst case, and a generalized Pareto distribution fitted to the excesses of each side with all BAs and years pooled in relative units and then by temperature regime, from which the expected shortfall follows. The tail is also attributed to member disagreement (the top quarter of days by the relative spread of the three members). On 2023 to 2025 with `final4`: coverage 89.2 %, 5.8 % of the hours under the band and 5.0 % over it; mean excess 2.0 % of the outcome below and 1.7 % above, worst 41 % and 33 % (single days at Duke and FPL); Pareto shape 0.19 below and 0.15 above (a heavy but finite-mean tail); in the cold regime the outcome exceeds the upper bound on 7.6 % of the hours (the storm under-forecast) against 5.2 % under it. Days of member disagreement carry 29 % of the hours outside the band and 33 % of the excess, against a quarter by construction: the members signal the tail only weakly.

## 4a. The benchmark by hour of the day

`scripts/df_profile.py` (`docs/df_hourly_bias.md`) profiles the BAs' own forecast (`DF`) against demand (`D`) by local hour, from the EIA-930 files alone. Three things follow for any comparison against `DF`.

1. **At PJM the published `DF` is stamped one hour earlier than `D` from 2019 on.** Compared with the `D` of the following hour, its MAPE falls from 3.4 to 3.9 % to 2.3 to 2.5 % in every year from 2019 to 2025; in 2016 to 2018 the published alignment is the better one (2.3 to 2.4 %). The daily peaks of the two series sit one hour apart. The signed error of `DF` as published has the shape a time shift gives: negative while the load falls (−6 to −7 % from 22:00 to 01:00), positive while it rises (+3 % at 05:00 and 06:00). The same test points to a shift at CAISO in 2016 and from 2023 on, outside or at the edge of the development period, where the CAISO `DF` degrades for other reasons as well (5.5 to 8 %).
2. **Constant or hour-dependent offsets.** NYISO's `DF` is 2.2 to 2.6 % below `D` at every hour and in every year; MISO's is 1 to 3 % above, SPP's 2 to 4 % above; ISO-NE's is 3 to 6 % below between 01:00 and 05:00 and within 1 % for the rest of the day; FPL's is 4 to 7 % below from 18:00 to 01:00. TVA, BPA and Duke show no offset (within 1 % at every hour). The EIA-930 instructions ask for "the day-ahead demand forecast generated in the normal course of business" and fix neither the hour of issue nor what the forecast quantity includes, so `DF` and `D` need not measure the same quantity.
3. **What it is worth.** Dividing `DF` by one plus its own median relative error at the same hour over the previous 60 days (known before the day) takes the demand-weighted MAPE of the eleven BAs from 3.04 % to 2.17 %, below the 2.59 % of the corrected ensemble on the same days. By BA the ensemble stays ahead of that corrected `DF` only at SPP (2.35 % against 2.53 %) and is close at PJM (2.35 % against 2.24 %).

`DF` as published stays the headline benchmark, because it is what a user of the public data receives. The corrected `DF` is reported next to it as the harder benchmark: it is closer to what the operators' forecasters achieve. It is not a forecast available at the 9 a.m. cut-off unless the BA publishes `DF` for the next day before that hour, which EIA-930 does not record.

## 5. Models

All models are fitted per BA, on a rolling origin: the last training day is two days before the target
day (the day before is known only until 08:00), models are refitted every 7 days, and the training
window is 730 days in phases B and C and 2190 days in phase D.

| Model | Specification | Why |
|---|---|---|
| Floors (`naive.py`) | the last 24 known hours placed at their hour of the day; the same weekday of the previous week; the mean of the same day type over the two weeks ending two days before | only fully known days |
| Profile (`profile.py`) | shape = median of the normalised analogue days (same day type and temperature regime; last 4 weeks plus 21 days either side of the same date a year before); level = median of the daily means of the 5 most recent analogues; regimes split at 59 and 72 F by the daily mean; with fewer than 3 analogues the regime is ignored | the profile of Note 2 made causal |
| Recency-effect regression (`recency.py`) | ordinary least squares on 215 regressors: trend, month, day type by hour, a cubic in temperature, the cubic by hour and by month, and cubics in the temperature lags of 1 to 3 h and in its moving averages over 6, 12 and 24 h | the benchmark model of the load-forecasting literature [3] with the recency effect [4]; temperature is divided by 100 to condition the matrix |
| Additive model (`additive.py`) | 24 ridge regressions, one per hour, after [5]: cubic B-spline bases with 6 interior knots at the quantiles of the training values for the temperature of the hour, the mean of the previous 24 h and the day's maximum and minimum, **plus a linear term for each**, the spline input being clipped to the training range; the load at the same hour of the last known day and of the same day a week before, the mean of the 24 hours before the cut-off, the day type, a trend; standardised columns; the penalty chosen in {0.01, 0.1, 1, 10, 100} by MAPE on the last 60 days of the window, then a refit on all of it | the splines give the U-shaped response; beyond the training range the spline is constant and the linear term continues, which is what lets the model extrapolate into cold it has not seen |
| Gradient boosting (`boosting.py`) | histogram gradient boosting (scikit-learn 1.3 `HistGradientBoostingRegressor`): at most 400 iterations, learning rate 0.05, 31 leaves, early stopping on 10 % of the rows after 20 iterations without improvement, seed 0; hourly rows with the calendar, the temperatures and the known load; one temperature column per station when there are several | trees find interactions the regression writes by hand; they do not extrapolate beyond the training range |
| Features (`features.py`) | hour, day type, special-day kind, sine and cosine of the day of the year, trend; temperature, its lags of 1 to 3 h, moving averages over 6, 12 and 24 h, the day's mean, minimum and maximum; load at the same hour of the last known day (the day before up to 08:00, two days before after it), of the same day a week before, and the mean of the 24 hours before the cut-off | the same functions build the training rows (observed temperature) and the target rows (HRRR path), so there is no path for information to leak |
| Ensemble (`ensemble.py`) | the mean of the members; with recent weights, the inverse of each member's MAPE over the last 30 days whose outcome is known at the cut-off, measured on the forecasts the ensemble stored; equal weights until 5 such days exist; a member that declines a day is left out of that day | nothing of the target day enters the weights |
| Bias correction (`quantiles.EmpiricalIntervals`) | the median, per hour of the day, of the model's relative errors over the last 60 known days, applied to the forecast; at least 20 days | causal and cheap; found while building the intervals |
| Quantiles (`quantiles.py`) | boosting with the pinball loss at 5, 50 and 95 %, sorted to remove crossings; or the empirical quantiles of the same relative errors used by the bias correction | a minimal version of a 90 % prediction interval |

### Additions of phase E

The development set has eleven BAs from phase E on: the ten above and FPL (Florida Power & Light). The
FPL series contains a structural step inside the development period: the load of the former Gulf Power
area joins it in mid-July 2022 (about 11 %, measured against the other Florida BAs). The series is not
adjusted; a model has to absorb the step from the load lags, as it would in operation. FPL uses six
stations (Miami, West Palm Beach, Melbourne, Fort Myers, Sarasota, Pensacola).

| Piece | Specification | Why |
|---|---|---|
| Bias correction on the ensemble | the median relative error of the ensemble per hour of the day, from the known days **of the same temperature regime** as the target day over the last 365 days (all known days when fewer than 20 share the regime); before 20 known days exist the uncorrected forecast is used | the regime-conditional correction beats the 60-day one (2.58 % against 2.66 %); it is also what absorbs a structural step within weeks |
| Adaptive intervals (`quantiles.AdaptiveIntervals`) | adaptive conformal inference [8]: the miscoverage level used to read the error quantiles is updated once per newly known day, `alpha <- alpha + 0.02 (0.10 - miss)`, clipped to 0.005 to 0.5, errors from a 120-day window | reaches the nominal 90 % over the year without assuming exchangeable errors |
| Shared fitted members (`base.Cached`) | a wrapper that keeps the forecast of the last BA-day | the same fitted model is scored alone and inside ensembles at the cost of one fit |
| Sky features, boosting only (`sky.py`, `Boosting(sky=True)`) | the cosine of the solar zenith angle at the BA's main station (declination 23.44° sin(2π(284 + n)/365), equation of time, evaluated at the middle of the hour, zero at night); the HRRR total cloud cover (`entire_atmosphere/TCDC`, %) averaged over the BA's stations, kept **as seen at each day's cut-off** (for every past day, the value forecast for it by the run available at that day's 9 a.m. rule), so the model trains on the kind of input it receives; and their product `sun × (1 − cloud/100)`. Cloud cover exists from 2 December 2020; before that it is missing, which the boosting accepts | the downward short-wave flux (`surface/DSWRF`, `VBDSF`) is present only as metadata in the public HRRR Zarr archive until 2025, so it cannot be used; tested at ISO-NE, CAISO and FPL (`docs/phase_e_sky.md`): the corrected ensemble goes from 3.74 % to 3.57 % at ISO-NE and from 2.76 % to 2.70 % at CAISO and does not move at FPL; the gain grows with the length of the cloud history (boosting at ISO-NE: −0.08 point in December 2020, −0.23 in 2021, −0.33 in 2022) and closes little of the midday gap to ISO-NE's forecast |
| Installed PV capacity (`scripts/pv_capacity.py`, `sky.PV_COLUMNS`, `Loader(pv=True)`) | the month's installed PV capacity behind the BA's load, in MW: net-metered PV by state from Form EIA-861M (states summed per BA) plus utility-scale PV by balancing authority from the Form EIA-860M generator inventory (nameplate cumulated by operating month, retirements removed); as features, the capacity, the capacity times the sun's elevation (`pv_clear`, available for the whole history) and that times one minus the forecast cloud fraction (`pv_est`) | a forecaster knows the installed capacity at the cut-off, and it is what scales the solar effect from one year to the next; in the boosting the terms add nothing (trees do not extrapolate a capacity that is always above its training range: `docs/phase_e_pv.md`); as two linear terms per hour in the additive model (`AdditiveModel(pv=True)`: capacity times the sun, and times the forecast cloud fraction, the simplest form of load reconstitution) they take the additive model at ISO-NE from 4.22 % to 3.86 % and the corrected ensemble from 3.58 % to 3.43 %, and CAISO's from 2.71 % to 2.65 % (`docs/phase_e_pv2.md`); the midday gap to ISO-NE's own forecast narrows by 0.3 to 0.4 point and remains |
| Adaptive level on the regime-conditional errors (`AdaptiveIntervals(by_regime=True, alpha_by_regime=...)`) | the error pool of the regime-conditional intervals (365 days) read at the adaptive level; with `alpha_by_regime` one level per temperature regime | the misses of a cold spell then widen the next cold days rather than the mild ones; on the eleven BAs (`docs/phase_e_intervals2.md`) the per-regime level reaches 89.5 % coverage over the year with bands 4 % narrower than the adaptive intervals and the lowest pinball loss at the 5th percentile on the coldest mornings, but covers 77 % of the hours inside the storms and 81 % on the coldest mornings, like the other variants: the 85 % criterion is not met |
| Nearest-temperature pool (`AdaptiveIntervals(nearest=40)`) | of the known days of the target day's regime over the last year, the 40 nearest in forecast daily minimum temperature give both the median correction and the band | the regime pool still mixes a −15 °C day with a +5 °C one; on the eleven BAs (`docs/phase_e_intervals3.md`) the pool takes the MAPE from 2.56 % to 2.53 %, the under-forecast at the peak from −1.85 % to −1.74 % and the coverage on the coldest mornings from 80.7 % to 84.3 %, widening the band there only (+9 %); an exponential tail beyond the pool's outer deciles changes nothing and was not adopted; inside the storms coverage stays at 78 % |
| Peak read at a higher quantile (`AdaptiveIntervals(peak="quantile", peak_quantile=0.60)`) | at the hours whose forecast is within 3 % of the forecast maximum (half weight at the neighbouring hours) the point is read at the 60th percentile of the pool's errors instead of the median; the band moves with it; the shift is never downward | the corrected point is a median per hour and the actual peak is a maximum over noisy hours, so the error measured at it is biased downward even for an unbiased forecast; on the eleven BAs (`docs/phase_e_peak.md`) the mean error at the peak goes from −0.79 % to −0.03 % and the under-forecast from −1.85 % to −1.44 % for 0.016 point of MAPE, better inside the storms at all 22 event-BA pairs (Uri −3.26 % to −2.71 %, Elliott −3.20 % to −2.70 %, against −2.00 % and −2.43 % for `DF`); replacing the hourly correction by the median error at the actual peak hour (`peak="lift"`) does the same at a slightly higher cost |
| Forecast irradiance (`hrrr_grib`, `Loader(irradiance=True)`, `AdditiveModel(irradiance=True)`) | the HRRR surface downward short-wave flux, read from the GRIB2 archive by byte range (the Zarr archive lacks it before 2025), kept as seen at each day's cut-off; a column of the boosting and, times the installed capacity, a linear term of the additive model in place of the cloud term | not adopted: at ISO-NE and CAISO (`docs/phase_e_irradiance.md`) the boosting does not move (3.60 % and 3.03 %) and the additive model gets worse (3.86 % to 4.06 %, 3.72 % to 3.77 %); the flux is instantaneous at the top of the hour, half an hour off the hourly load mean, and the term replaced rather than joined the cloud term, two things a later test could change; the limit appears to be the weather model's sky forecast 17 to 45 h ahead, not the variable |
| Hourly forecasts (`evaluate(hourly=True)`) | the 24 values of every model, of `DF`, of the outcome and of the 5th and 95th percentiles are stored per BA and day | diagnostics by hour and month (`scripts/diagnose.py`, `docs/diagnostics.md`) and any later analysis without rerunning the models |

## 6. Special days and daily shapes

The calendar (`grid_sentinel.calendar_us`) holds the federal holidays with their observance, the day
after Thanksgiving, 24 and 31 December and Super Bowl Sunday, each mapped to the day type it resembles
in Note 2. Three treatments were compared: substitution by that day type (the default), indicators of
the special-day kind on top of it, and a separate model fitted on special days and weekends (at least
30 days). Indicators were adopted; the separate model changes nothing.

Daily shapes (`clusters.py`, `docs/day_clusters.md`) are the 24 hourly values divided by the day's mean.
k-means (k-means++ seeding, 20 initialisations, seed 0) and the silhouette are implemented in numpy so
that the result is the same on any machine. Shapes are clustered **within each temperature regime**, k
between 2 and 5 by silhouette, because across regimes the clusters are the regimes themselves. The
distance to the nearest centroid flags atypical days; large documented load-shed days sit in the top
6 % of each BA, small ones do not. As a forecasting feature in place of the calendar day type, the
cluster label makes every model worse by about 0.9 point.

## 7. Cleaning the history

The control cleaning is the gross-fault guard of section 2. The alternative (`cleaning.py`) runs the
grid-data-sentinel composite with the BA's temperature as context, one year at a time, warmed up on
the year before, and repairs the flagged hours by equivalent days; the outcome is never cleaned. On the
ten BAs it changes the annual mean by 0.01 point.

## 8. Tried and not adopted

| Attempt | Effect on the demand-weighted MAPE | Decision |
|---|---|---|
| Shape-cluster label in place of the day type | worse by 0.9 point | used for labelling and detection only |
| Explicit cold and heat terms (degrees below 32 F at the hour and over 24 h, consecutive cold hours, degrees above 85 F) | none; no consistent effect at the storm peaks | not adopted |
| Separate special-day model | none | not adopted |
| The regression as a third ensemble member | 2.78 against 2.77 | not adopted |
| History cleaned by grid-data-sentinel | 0.01 | kept as a control run |
| A neural network | not implemented | deferred |
| Wind speed and wind chill (phase H) | boosting alone better by 0.02; the corrected recipe worse by 0.007 and by 0.02 in winter | not adopted (section 8f) |
| Humidity block in the boosting alone, additive model unchanged (phase H) | worse than with the apparent temperature by 0.03, by 0.08 in summer | not adopted (section 8f) |
| HRRR dew point corrected by its own recent bias per local hour, 30 known days (phase H) | the additive model better by 0.03, the boosting worse by 0.04 in summer, the recipe worse by 0.012 and by 0.034 in summer at every BA (`docs/phase_h_dewpoint_bias.md`) | not adopted (section 8f) |
| Linear humidity terms in the additive model instead of the apparent temperature (phase H) | level over the year, worse by 0.04 in summer | not adopted (section 8f) |

## 8a. The recipe in one run

The pieces above were tested in groups, each on the BA-days its own models could score. The recipe that phase E settled on was then run once on the eleven BAs (`scripts/run_phase_e.py --groups final`, `docs/phase_e_final.md`) so that the reported numbers come from a single set of days: 2.56 % against 3.04 % for `DF` on 8163 BA-days (median 2.23 %, ahead on 61 % of the days; Diebold-Mariano significant at 5 % at ten of the eleven BAs, FPL being a tie), under-forecast at the peak −1.85 % against −1.26 %, interval coverage 89.5 % over the year, 76.9 % inside the storms and 80.7 % on the coldest mornings. Against `DF` with its own trailing hourly bias removed (2.17 %) the recipe is behind at ten BAs.

## 8b. Phase F: the recipe after three more tests

Phase F tested one change per limitation, on the same development days, and kept two (`docs/phase_e_intervals3.md`, `docs/phase_e_peak.md`, `docs/phase_e_irradiance.md`; the pieces are described in the table of section 5). The recipe after phase F, run once on the eleven BAs (`scripts/run_phase_e.py --groups final2`, `docs/phase_f_final.md`): 2.55 % against 3.04 % for `DF` on 8163 BA-days (median 2.21 %, ahead on 61 % of the days, Diebold-Mariano significant at ten of the eleven BAs), mean error at the actual peak +0.10 % (was −0.79 %) and under-forecast at the peak −1.37 % (was −1.85 %; `DF` −1.26 %), interval coverage 88.9 % over the year, 79.0 % inside the storms and 84.6 % on the coldest mornings (were 89.5, 76.9 and 80.7 %). Against `DF` with its own trailing hourly bias removed (2.17 %) the recipe is still behind at ten BAs.

## 8c. Frozen evaluation

The recipe of section 8b was frozen and run once on 1 January 2023 to 31 December 2025 on the eleven development BAs (`scripts/run_phase_e.py --groups frozen --start 2023-01-01 --end 2025-12-31`, `docs/frozen_evaluation.md`), the models learning day by day from the six years before each day; nothing was changed after these numbers were seen. Results on 10 470 BA-days: 2.52 % against 3.22 % for `DF` (median 2.18 % against 2.90 %; ahead on 62 % of the days; Diebold-Mariano significant at 5 % at ten of the eleven BAs, NYISO being level), error at the actual peak +0.06 %, under-forecast at the peak −1.37 % against −1.31 %, interval coverage 89.1 % over the year, 80.8 % inside the two winter events (January 2024 and January 2025) and 84.5 % on the coldest mornings. Against `DF` with its own trailing hourly bias removed (2.16 %) the recipe is ahead at SPP only. Two features of the benchmark in these years are documented in `docs/df_hourly_bias_2023_2025.md`: CAISO's published `DF` degrades to 5.5 to 8.1 %, which CAISO's own OASIS series resolve into two parts: the EIA-930 demand column carries hour labels one hour off from 14 June 2022 on (the forecast column equals CAISO's day-ahead forecast exactly), and CAISO's forecast error against its own actual load grew from 2.5 % in January 2022 to 6.1 % in January 2025; and NYISO's `DF` is published as zero on three days (which the complete-case rule does not remove, since only the outcome is checked for plausibility). The FPL outcome has four days with a spike at the peak of two to five times the forecast within the plausibility bounds; they stay in the tables. No firm load was shed in the two winter events of the period: FERC's review of the January 2024 Arctic storms (Technical Talk with ReliabilityFirst, 15 July 2024, pp. 14 and 19: "zero system operator initiated load shed") and the FERC/NERC joint staff report on the January 2025 Arctic events (April 2025, p. 4: "no firm load shed"), so `docs/load_shed_days.csv` has no rows for these years.

## 8d. Protocol v2

Three rules were added to the evaluation after the frozen run, all about the data rather than the models (`docs/phase_g_protocol.md`). A BA-day on which the published forecast is missing, non-positive or more than 50 % away from the outcome at any hour is a reporting fault of the benchmark and is left out for every model (34 BA-days of the development period, among them three NYISO days with a published forecast of zero). An hour more than 40 % away from the mean of its two neighbours is a fault in the outcome, and its day is left out (17 BA-days; the gross-fault guard of 0.2 to 5 times the recent median had let through FPL hours of 67 GW in a 15 GW system). And the documented hour-label offsets of the published series (`docs/hour_label_offsets.csv`: PJM's forecast is stamped one hour early from February 2019, CAISO's demand one hour late from 14 June 2022, both checked against the operators' own published series) are applied when the files are read, for the models and for `DF` alike. The recipe barely moves under protocol v2 (2.55 % to 2.54 % on the development period); the benchmark does (3.04 % to 2.69 %), because PJM's published error falls from 3.65 % to 2.45 % and CAISO's from 2.80 % to 2.38 %. Under protocol v2 the recipe is ahead of the published forecasts by 0.15 point over the eleven BAs (2.54 % against 2.69 %, better on 53 % of the days), ahead at PJM, SPP, MISO and NYISO, level at FPL, and behind at the other six. Protocol v2 is the evaluation used from here on; the numbers of sections 8a to 8c are kept as measured under the earlier rules, which is what a user of the published data would compute.

## 8e. Phase G and a second look at 2023 to 2025

Phase G tested, on the development period under protocol v2, more load memory (the load two and three weeks back and the mean of the same weekday last week) and the thermal history and shape of the day (yesterday's extremes, the heating and cooling degree-hours of the previous 72 hours, the day's range, the temperature at 07:00 and 17:00) as features of both members; the boosting's depth, rate, leaf size, regularisation, refit period and training length; the additive model's knots, validation window and penalty grid; hourly ensemble weights, a third member (the recency regression of phase B), a boosting on a ratio target, and the size of the nearest-temperature pool; and the HRRR temperature path corrected by its own recent bias per local hour (`docs/phase_g_*.md`). Three things entered the recipe: the two feature blocks on both members (additive model 3.11 % to 3.00 %, better at all eleven BAs; boosting 3.00 % to 2.94 %, better at ten) and the third member (2.54 % to 2.50 % on the corrected ensemble, better at nine). Hourly weights, the ratio target, other pool sizes and the sun's elevation outside the solar BAs changed nothing or hurt; the deeper boosting and the temperature-bias correction lift the members (the correction by 0.30 to 0.37 point at ten or eleven BAs) but barely the corrected recipe: together (`final3b`, `docs/phase_g_final_b.md`) they give 2.43 % against 2.46 %, better at seven BAs and worse at PJM and NYISO, better inside the two winter events (3.98 % against 4.09 %, peak under-forecast 2.7 against 3.0 points) and slightly worse on the annual peak, at three times the training cost; they are kept as a variant. The recipe after phase G (`final3`), run once on the development period: 2.46 % against 2.54 % for the phase F recipe and 2.69 % for `DF`, better at all eleven BAs (`docs/phase_g_final.md`).

On 2023 to 2025 under protocol v2, with the observed-temperature supplement of section 2 (`docs/frozen_evaluation_v2.md`, 11 679 BA-days), `final3` gives 2.44 % against 2.90 % for `DF` (median 2.10 % against 2.50 %, ahead on 57 % of the days, Diebold-Mariano significant at nine of the eleven BAs), coverage 89.2 % over the year, 82.1 % inside the two winter events and 84.5 % on the coldest mornings. This is a second look at those years, not a frozen evaluation: the phase F recipe had already been scored on them. The honest number is the difference between the two recipes on the same days under the same rules (`docs/frozen_evaluation_final2_v2.md`; 11 950 common BA-days): 2.446 % against 2.503 %, better at nine BAs and worse at CAISO (0.01) and ISO-NE (0.03), a gain of the same size as on the development period (0.06 against 0.08 point), which is the evidence that phase G did not fit the development period. By BA against `DF` the picture is harder than the aggregate: ahead at PJM, SPP, MISO and CAISO, behind at the other seven; ahead in each year (2.37 % against 2.68 % in 2023, 2.47 % against 2.72 % in 2024, 2.50 % against 3.28 % in 2025, demand-weighted on the common days) with the gap widening as the published forecasts worsen. Inside the events the recipe is behind the published forecasts in January 2024 (3.83 % against 3.60 %) and ahead in January 2025 (2.75 % against 3.38 %). Against `DF` with its own trailing hourly bias removed (2.05 %) the recipe is ahead at SPP only. Running the same evaluation with the IEM archive alone as the supplement instead of GHCNh first changes no BA by more than 0.007 point.

## 8f. Phase H: humidity and wind

Phase H added the observed and forecast dew point and wind: observed from the same ISD-Lite files as the temperature (dew point and wind speed columns) and the same supplements after 27 August 2025, forecast from the HRRR archive (`2m_above_ground/DPT`; `10m_above_ground/UGRD` and `VGRD` combined into a speed), 49 stations, the same 39-hour path as the temperature, the mean over the BA's stations. From them, per hour: relative humidity (Magnus), the NWS heat index (Rothfusz regression with the NWS adjustments, applied at 80 F and above), the NWS wind chill (at 50 F and below with wind of at least 3 mph) and the apparent temperature (the heat index or the wind chill where each applies, the temperature elsewhere). Tested on the development period under protocol v2, on the days the phase G recipe scored (`scripts/compare_days.py`, demand-weighted, seasons: winter December to February, summer June to September):

| Change | Year | Winter | Summer | Shoulder | BAs better / worse (year) |
|---|---|---|---|---|---|
| Boosting with dew point, dew-point depression, relative humidity and heat index as features | 2.94 % to 2.84 % (0.10) | 0.03 | 0.18 | 0.08 | 11 / 0 |
| Additive model fitted on the apparent temperature (heat index only) instead of the temperature | 3.01 % to 3.00 % (0.02) | worse by 0.01 | 0.04 | 0.01 | 9 / 1 |
| The recipe with both (`final3_h`) against the phase G recipe | **2.47 % to 2.40 % (0.07)** | 0.01 | **0.15** | 0.04 | **11 / 0** |

The forecast dew point was verified like the temperature (`docs/hrrr_dewpoint_verification.md`, 5.1 million pairs at 49 stations, 2021 to 2025, leads 17 to 45 h): bias -0.27 F, MAE 3.38 F (temperature: -1.23 F and 3.12 F), with a regression-to-the-mean pattern (too humid below 20 F of dew point by 2.2 F, too dry above 65 F by 1.6 F and in July and August by 2.0 F) and a dry bias of 3.8 F on the thirty most humid afternoons of each station, up to 10 F at inland stations (Fresno, Kansas City, Omaha) and within 1 F on the Florida coast. Humidity is the largest single gain since the multi-station temperature (phase C), and it is a summer gain: 0.15 point in June to September at every BA, 0.01 in winter. Wind and wind chill (`docs/phase_h_humidity.md`, `docs/phase_h_variants_by_season.md`) lift the boosting alone by 0.02 point (0.04 in winter) but not the corrected recipe (worse by 0.007, at seven of the eleven BAs, and worse by 0.02 in winter because the wind chill in the additive model's smooth response hurts there); linear humidity terms in the additive model instead of the apparent temperature (`docs/phase_h_humidity_linear.md`) are level over the year and worse in summer; the humidity block in the boosting alone (`docs/phase_h_humidity_boosting.md`) is worse than with the apparent temperature in the additive model too; and correcting the forecast dew point by its own recent bias per local hour, which the verification above suggested, helps the additive model but hurts the boosting (the corrected dew point no longer matches the uncorrected temperature it is combined with) and leaves the recipe worse by 0.012 (`docs/phase_h_dewpoint_bias.md`). The recipe after phase H (`final4`) is therefore the phase G recipe with the humidity block in the boosting and the apparent temperature in the additive model, without wind; the wind extraction is documented as tested and not adopted.

On 2023 to 2025 under protocol v2 (`docs/frozen_evaluation_v3.md`, 11 679 BA-days; a third look at those years) `final4` gives 2.38 % against 2.90 % for `DF` (median 2.04 % against 2.50 %, ahead on 59 % of the days, Diebold-Mariano significant at nine of the eleven BAs), coverage 89.3 % over the year, 81.8 % inside the two winter events and 84.3 % on the coldest mornings. Against the phase G recipe on the same days (`docs/phase_h_frozen_by_season.md`, 11 950 common BA-days) it is better by 0.063 point, at ten of the eleven BAs (level at CAISO), by 0.13 in summer and 0.01 in winter: the same size and the same season as on the development period. By BA against `DF`: ahead at PJM, SPP, MISO and CAISO, level at NYISO and ERCOT, behind at the other five. Against `DF` with its own hourly bias removed (2.05 %) the recipe is ahead at SPP and CAISO.

## 9. Limitations

One to five stations per BA. The 9 a.m. cut-off and the 2 h availability lag are conventions, not a
description of any operator's process. The HRRR is a weather model with its own error and not the
forecast any BA used; the BAs' forecasters have vendor weather and internal information this study
does not have. Special days, events and the ten BAs are choices of the study. Prediction intervals
are too narrow inside the storms (79 % coverage) and slightly so on the coldest mornings (85 %). A large part of the margin over the BAs' published forecasts comes from offsets and, at PJM, a one-hour misalignment in the published `DF` (section 4a); against `DF` with its own hourly bias removed the models are behind at ten of the eleven BAs. The frozen evaluation covers three later years on the same eleven BAs;
no evaluation on other BAs has been run yet.

## References

[1] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," *Journal of Business & Economic Statistics*, vol. 13, no. 3, pp. 253-263, 1995. doi:10.1080/07350015.1995.10524599

[2] D. Harvey, S. Leybourne and P. Newbold, "Testing the equality of prediction mean squared errors," *International Journal of Forecasting*, vol. 13, no. 2, pp. 281-291, 1997. doi:10.1016/S0169-2070(96)00719-4

[3] T. Hong, P. Pinson and S. Fan, "Global Energy Forecasting Competition 2012," *International Journal of Forecasting*, vol. 30, no. 2, pp. 357-363, 2014. doi:10.1016/j.ijforecast.2013.07.001

[4] P. Wang, B. Liu and T. Hong, "Electric load forecasting with recency effect: A big data approach," *International Journal of Forecasting*, vol. 32, no. 3, pp. 585-597, 2016. doi:10.1016/j.ijforecast.2015.09.006

[5] R. J. Hyndman and S. Fan, "Density forecasting for long-term peak electricity demand," *IEEE Transactions on Power Systems*, vol. 25, no. 2, pp. 1142-1153, 2010. doi:10.1109/TPWRS.2009.2036017

[6] T. Hong and S. Fan, "Probabilistic electric load forecasting: A tutorial review," *International Journal of Forecasting*, vol. 32, no. 3, pp. 914-938, 2016. doi:10.1016/j.ijforecast.2015.11.011

[7] G. Chicco, "Overview and performance assessment of the clustering methods for electrical load pattern grouping," *Energy*, vol. 42, no. 1, pp. 68-80, 2012. doi:10.1016/j.energy.2011.12.031

[8] I. Gibbs and E. Candès, "Adaptive conformal inference under distribution shift," arXiv:2106.00170, 2021.
