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
| Adaptive level on the regime-conditional errors (`AdaptiveIntervals(by_regime=True, alpha_by_regime=...)`) | the error pool of the regime-conditional intervals (365 days) read at the adaptive level; with `alpha_by_regime` one level per temperature regime | the misses of a cold spell then widen the next cold days rather than the mild ones; tested in `docs/phase_e_intervals2.md` |
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

## 9. Limitations

One to five stations per BA. The 9 a.m. cut-off and the 2 h availability lag are conventions, not a
description of any operator's process. The HRRR is a weather model with its own error and not the
forecast any BA used; the BAs' forecasters have vendor weather and internal information this study
does not have. Special days, events and the ten BAs are choices of the study. Prediction intervals
are too narrow on the coldest mornings. A large part of the margin over the BAs' published forecasts comes from offsets and, at PJM, a one-hour misalignment in the published `DF` (section 4a); against `DF` with its own hourly bias removed the models are behind at ten of the eleven BAs. Results are for the development period and BAs; no
out-of-sample evaluation on other BAs or years has been run yet.

## References

[1] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," *Journal of Business & Economic Statistics*, vol. 13, no. 3, pp. 253-263, 1995. doi:10.1080/07350015.1995.10524599

[2] D. Harvey, S. Leybourne and P. Newbold, "Testing the equality of prediction mean squared errors," *International Journal of Forecasting*, vol. 13, no. 2, pp. 281-291, 1997. doi:10.1016/S0169-2070(96)00719-4

[3] T. Hong, P. Pinson and S. Fan, "Global Energy Forecasting Competition 2012," *International Journal of Forecasting*, vol. 30, no. 2, pp. 357-363, 2014. doi:10.1016/j.ijforecast.2013.07.001

[4] P. Wang, B. Liu and T. Hong, "Electric load forecasting with recency effect: A big data approach," *International Journal of Forecasting*, vol. 32, no. 3, pp. 585-597, 2016. doi:10.1016/j.ijforecast.2015.09.006

[5] R. J. Hyndman and S. Fan, "Density forecasting for long-term peak electricity demand," *IEEE Transactions on Power Systems*, vol. 25, no. 2, pp. 1142-1153, 2010. doi:10.1109/TPWRS.2009.2036017

[6] T. Hong and S. Fan, "Probabilistic electric load forecasting: A tutorial review," *International Journal of Forecasting*, vol. 32, no. 3, pp. 914-938, 2016. doi:10.1016/j.ijforecast.2015.11.011

[7] G. Chicco, "Overview and performance assessment of the clustering methods for electrical load pattern grouping," *Energy*, vol. 42, no. 1, pp. 68-80, 2012. doi:10.1016/j.energy.2011.12.031

[8] I. Gibbs and E. Candès, "Adaptive conformal inference under distribution shift," arXiv:2106.00170, 2021.
