# Phase F: forecast irradiance as a feature

BAs with large solar behind the load: CISO, ISNE, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `*_irr` models receive the HRRR forecast surface short-wave flux as seen at each day's cut-off (GRIB2 archive, from December 2020): the boosting as a column, the additive model as the installed PV capacity times the flux, in place of the capacity times the cloud fraction. `final_nn40` and `final_nn40_irr` are the corrected ensembles with the nearest-temperature pool, without and with it.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.65 | 2.35 | 0.24 | -0.71 | 0.39 | 0.00 | 0.00 | -6.96 | 1489 | 2.00 |
| final_nn40 | 2.87 | 2.53 | -0.30 | -1.60 | 0.43 | 0.46 | 0.23 | -16.24 | 1489 | 2.00 |
| final_nn40_irr | 2.91 | 2.57 | -0.26 | -1.57 | 0.43 | 0.45 | 0.24 | -17.47 | 1489 | 2.00 |
| final_boosting | 3.22 | 2.90 | -1.65 | -2.48 | 0.51 | 0.37 | 0.18 | -21.50 | 1489 | 2.00 |
| final_boosting_irr | 3.22 | 2.90 | -1.65 | -2.48 | 0.51 | 0.37 | 0.18 | -21.50 | 1489 | 2.00 |
| final_ensemble | 3.23 | 2.78 | -1.93 | -2.79 | 0.43 | 0.39 | 0.16 | -18.61 | 1489 | 2.00 |
| final_ensemble_irr | 3.26 | 2.83 | -1.91 | -2.76 | 0.44 | 0.38 | 0.16 | -19.16 | 1489 | 2.00 |
| final_additive | 3.77 | 3.29 | -2.31 | -3.37 | 0.46 | 0.28 | 0.15 | -20.55 | 1489 | 2.00 |
| final_additive_irr | 3.87 | 3.42 | -2.27 | -3.32 | 0.47 | 0.27 | 0.14 | -21.77 | 1489 | 2.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| final_additive | CISO | 3.72 | 3.19 | -2.94 | -3.83 | 0.41 | -18.17 | 0.32 | 0.15 | 737 | 25196.91 |
| final_additive | ISNE | 3.86 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 752 | 13392.81 |
| final_additive_irr | CISO | 3.77 | 3.32 | -2.80 | -3.70 | 0.43 | -17.81 | 0.31 | 0.14 | 737 | 25196.91 |
| final_additive_irr | ISNE | 4.06 | 3.62 | -1.27 | -2.63 | 0.56 | -21.77 | 0.19 | 0.16 | 752 | 13392.81 |
| final_boosting | CISO | 3.02 | 2.70 | -2.10 | -2.70 | 0.46 | -18.99 | 0.43 | 0.18 | 737 | 25196.91 |
| final_boosting | ISNE | 3.61 | 3.28 | -0.80 | -2.05 | 0.62 | -21.50 | 0.27 | 0.17 | 752 | 13392.81 |
| final_boosting_irr | CISO | 3.02 | 2.70 | -2.10 | -2.70 | 0.46 | -18.99 | 0.43 | 0.18 | 737 | 25196.91 |
| final_boosting_irr | ISNE | 3.61 | 3.28 | -0.80 | -2.05 | 0.62 | -21.50 | 0.27 | 0.17 | 752 | 13392.81 |
| final_ensemble | CISO | 3.08 | 2.63 | -2.45 | -3.10 | 0.38 | -18.61 | 0.45 | 0.16 | 737 | 25196.91 |
| final_ensemble | ISNE | 3.49 | 3.07 | -0.96 | -2.19 | 0.53 | -18.23 | 0.28 | 0.16 | 752 | 13392.81 |
| final_ensemble_irr | CISO | 3.10 | 2.65 | -2.39 | -3.04 | 0.39 | -18.43 | 0.44 | 0.16 | 737 | 25196.91 |
| final_ensemble_irr | ISNE | 3.56 | 3.16 | -1.02 | -2.25 | 0.53 | -19.16 | 0.26 | 0.16 | 752 | 13392.81 |
| final_nn40 | CISO | 2.61 | 2.34 | -0.36 | -1.55 | 0.37 | -13.90 | 0.53 | 0.26 | 737 | 25196.91 |
| final_nn40 | ISNE | 3.37 | 2.90 | -0.18 | -1.70 | 0.53 | -16.24 | 0.32 | 0.18 | 752 | 13392.81 |
| final_nn40_irr | CISO | 2.63 | 2.34 | -0.36 | -1.53 | 0.38 | -13.86 | 0.53 | 0.26 | 737 | 25196.91 |
| final_nn40_irr | ISNE | 3.43 | 3.01 | -0.08 | -1.65 | 0.54 | -17.47 | 0.30 | 0.19 | 752 | 13392.81 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| final_additive | CISO | uri | 2.40 | 2.19 | 0.00 | 0.00 | 6 |
| final_additive | ISNE | uri | 2.56 | 1.52 | -0.29 | -1.49 | 6 |
| final_additive_irr | CISO | uri | 2.50 | 2.19 | 0.00 | 0.00 | 6 |
| final_additive_irr | ISNE | uri | 3.12 | 1.51 | -0.35 | -1.18 | 6 |
| final_boosting | CISO | uri | 1.92 | -0.89 | -1.15 | -2.76 | 6 |
| final_boosting | ISNE | uri | 3.25 | 0.85 | -0.77 | -3.07 | 6 |
| final_boosting_irr | CISO | uri | 1.92 | -0.89 | -1.15 | -2.76 | 6 |
| final_boosting_irr | ISNE | uri | 3.25 | 0.85 | -0.77 | -3.07 | 6 |
| final_ensemble | CISO | uri | 1.62 | 0.60 | -0.16 | -0.62 | 6 |
| final_ensemble | ISNE | uri | 2.76 | 1.22 | -0.40 | -2.21 | 6 |
| final_ensemble_irr | CISO | uri | 1.72 | 0.59 | -0.16 | -0.62 | 6 |
| final_ensemble_irr | ISNE | uri | 2.99 | 1.20 | -0.39 | -2.07 | 6 |
| final_nn40 | CISO | uri | 1.86 | -0.43 | -0.98 | -2.06 | 6 |
| final_nn40 | ISNE | uri | 2.65 | 1.18 | -0.42 | -2.06 | 6 |
| final_nn40_irr | CISO | uri | 1.89 | -0.47 | -1.03 | -2.16 | 6 |
| final_nn40_irr | ISNE | uri | 2.98 | 1.18 | -0.38 | -1.93 | 6 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| final_additive | CISO | elliott | 3.76 | 2.62 | -0.56 | -2.81 | 5 |
| final_additive | ISNE | elliott | 3.99 | 1.75 | -0.62 | -2.38 | 5 |
| final_additive_irr | CISO | elliott | 3.97 | 2.15 | -0.64 | -3.22 | 5 |
| final_additive_irr | ISNE | elliott | 4.34 | 1.88 | -0.69 | -2.27 | 5 |
| final_boosting | CISO | elliott | 3.63 | 1.17 | -0.89 | -3.69 | 5 |
| final_boosting | ISNE | elliott | 3.40 | 2.44 | -0.38 | -1.47 | 5 |
| final_boosting_irr | CISO | elliott | 3.63 | 1.17 | -0.89 | -3.69 | 5 |
| final_boosting_irr | ISNE | elliott | 3.40 | 2.44 | -0.38 | -1.47 | 5 |
| final_ensemble | CISO | elliott | 3.37 | 1.82 | -0.66 | -3.29 | 5 |
| final_ensemble | ISNE | elliott | 3.36 | 2.11 | -0.49 | -1.34 | 5 |
| final_ensemble_irr | CISO | elliott | 3.29 | 1.59 | -0.70 | -3.49 | 5 |
| final_ensemble_irr | ISNE | elliott | 3.51 | 2.18 | -0.52 | -1.35 | 5 |
| final_nn40 | CISO | elliott | 2.94 | 0.90 | -1.00 | -4.38 | 5 |
| final_nn40 | ISNE | elliott | 3.43 | 0.90 | -1.07 | -2.81 | 5 |
| final_nn40_irr | CISO | elliott | 2.82 | 0.65 | -1.10 | -4.41 | 5 |
| final_nn40_irr | ISNE | elliott | 3.61 | 1.00 | -1.10 | -2.97 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | DF | eve | 2.90 | 1.72 | -0.42 |  | 49 |
| 14 | final_ensemble | eve | 3.51 | 1.90 | -1.13 | 0.37 | 49 |
| 16 | final_nn40 | eve | 3.51 | 2.50 | -0.86 | 0.45 | 49 |
| 17 | final_nn40_irr | eve | 3.58 | 2.61 | -0.84 | 0.45 | 49 |
| 15 | final_ensemble_irr | eve | 3.59 | 1.94 | -1.10 | 0.37 | 49 |
| 10 | final_additive | eve | 3.64 | 2.04 | -1.26 | 0.37 | 49 |
| 11 | final_additive_irr | eve | 3.86 | 2.13 | -1.20 | 0.33 | 49 |
| 12 | final_boosting | eve | 3.92 | 1.81 | -1.11 | 0.39 | 49 |
| 13 | final_boosting_irr | eve | 3.92 | 1.81 | -1.11 | 0.39 | 49 |
| 0 | DF | special | 2.80 | 0.38 | -0.92 |  | 49 |
| 7 | final_nn40 | special | 3.64 | -0.36 | -2.26 | 0.37 | 49 |
| 8 | final_nn40_irr | special | 3.67 | -0.22 | -2.20 | 0.35 | 49 |
| 5 | final_ensemble | special | 3.67 | -0.98 | -2.61 | 0.33 | 49 |
| 6 | final_ensemble_irr | special | 3.75 | -0.90 | -2.60 | 0.31 | 49 |
| 3 | final_boosting | special | 3.87 | -1.05 | -2.49 | 0.27 | 49 |
| 4 | final_boosting_irr | special | 3.87 | -1.05 | -2.49 | 0.27 | 49 |
| 1 | final_additive | special | 4.07 | -0.88 | -2.85 | 0.31 | 49 |
| 2 | final_additive_irr | special | 4.29 | -0.69 | -2.85 | 0.29 | 49 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final_nn40 | all | 0.406 | 1.505 | 0.450 | 0.889 | 13.032 | 0.898 | 1447 |
| final_nn40_irr | all | 0.405 | 1.525 | 0.461 | 0.889 | 13.232 | 0.903 | 1447 |
| final_nn40 | events | 0.429 | 1.339 | 0.363 | 0.883 | 11.504 | 0.909 | 22 |
| final_nn40_irr | events | 0.430 | 1.395 | 0.372 | 0.879 | 11.850 | 0.909 | 22 |
| final_nn40 | cold_mornings | 0.323 | 1.285 | 0.376 | 0.910 | 11.733 | 0.950 | 60 |
| final_nn40_irr | cold_mornings | 0.325 | 1.311 | 0.385 | 0.912 | 12.113 | 0.950 | 60 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final_additive | CISO | mape | 12.049 | 0.000 | 737 |
| final_additive | ISNE | mape | 21.098 | 0.000 | 752 |
| final_additive_irr | CISO | mape | 12.690 | 0.000 | 737 |
| final_additive_irr | ISNE | mape | 22.527 | 0.000 | 752 |
| final_boosting | CISO | mape | 3.135 | 0.002 | 737 |
| final_boosting | ISNE | mape | 18.335 | 0.000 | 752 |
| final_boosting_irr | CISO | mape | 3.135 | 0.002 | 737 |
| final_boosting_irr | ISNE | mape | 18.335 | 0.000 | 752 |
| final_ensemble | CISO | mape | 3.951 | 0.000 | 737 |
| final_ensemble | ISNE | mape | 16.914 | 0.000 | 752 |
| final_ensemble_irr | CISO | mape | 4.233 | 0.000 | 737 |
| final_ensemble_irr | ISNE | mape | 17.528 | 0.000 | 752 |
| final_nn40 | CISO | mape | -2.861 | 0.004 | 737 |
| final_nn40 | ISNE | mape | 14.842 | 0.000 | 752 |
| final_nn40_irr | CISO | mape | -2.552 | 0.011 | 737 |
| final_nn40_irr | ISNE | mape | 15.561 | 0.000 | 752 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| final_additive | 0.982 |
| final_additive_irr | 0.982 |
| final_boosting | 0.996 |
| final_boosting_irr | 0.996 |
| final_ensemble | 0.996 |
| final_ensemble_irr | 0.996 |
| final_nn40 | 0.996 |
| final_nn40_irr | 0.996 |
