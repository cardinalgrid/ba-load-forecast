# Phase E: the installed PV capacity as a feature

BAs with large solar behind the load: CISO, ISNE, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `boosting_ml_pv` is the sky boosting with three more columns: the installed PV capacity of the month (MW, from Forms EIA-861M and EIA-860M), that capacity times the sun's elevation, and the same times one minus the forecast cloud fraction; `ens_pv` and `ens_pv_bc_regime` are the ensemble and the corrected ensemble built on it. Compare with `docs/phase_e_sky.md` (same BAs and days, without the capacity terms).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.65 | 2.35 | 0.24 | -0.71 | 0.39 | 0.00 | 0.00 | -6.96 | 1489 | 2.00 |
| ens_pv_bc_regime | 3.01 | 2.63 | -0.63 | -1.81 | 0.41 | 0.43 | 0.21 | -20.43 | 1489 | 2.00 |
| boosting_ml_pv | 3.26 | 2.92 | -1.66 | -2.49 | 0.50 | 0.37 | 0.17 | -21.43 | 1489 | 2.00 |
| ens_pv | 3.31 | 2.89 | -2.05 | -2.85 | 0.42 | 0.36 | 0.16 | -20.71 | 1489 | 2.00 |
| additive_ml_special | 3.98 | 3.57 | -2.59 | -3.56 | 0.43 | 0.25 | 0.14 | -22.39 | 1489 | 2.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| additive_ml_special | CISO | 3.86 | 3.50 | -3.12 | -3.96 | 0.37 | -18.80 | 0.29 | 0.14 | 737 | 25196.91 |
| additive_ml_special | ISNE | 4.22 | 3.71 | -1.60 | -2.79 | 0.53 | -22.39 | 0.17 | 0.15 | 752 | 13392.81 |
| boosting_ml_pv | CISO | 3.04 | 2.70 | -2.12 | -2.72 | 0.45 | -18.66 | 0.43 | 0.18 | 737 | 25196.91 |
| boosting_ml_pv | ISNE | 3.67 | 3.34 | -0.81 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 752 | 13392.81 |
| ens_pv | CISO | 3.13 | 2.70 | -2.52 | -3.15 | 0.37 | -18.72 | 0.43 | 0.15 | 737 | 25196.91 |
| ens_pv | ISNE | 3.66 | 3.25 | -1.17 | -2.30 | 0.52 | -20.71 | 0.24 | 0.16 | 752 | 13392.81 |
| ens_pv_bc_regime | CISO | 2.70 | 2.39 | -0.76 | -1.80 | 0.38 | -14.49 | 0.50 | 0.23 | 737 | 25196.91 |
| ens_pv_bc_regime | ISNE | 3.58 | 3.08 | -0.38 | -1.85 | 0.48 | -20.43 | 0.28 | 0.17 | 752 | 13392.81 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| additive_ml_special | CISO | uri | 2.30 | 1.97 | 0.00 | 0.00 | 6 |
| additive_ml_special | ISNE | uri | 3.16 | 0.95 | -0.46 | -2.03 | 6 |
| boosting_ml_pv | CISO | uri | 1.85 | -0.83 | -0.99 | -2.55 | 6 |
| boosting_ml_pv | ISNE | uri | 3.32 | 1.07 | -0.73 | -3.06 | 6 |
| ens_pv | CISO | uri | 1.74 | 0.58 | -0.15 | -0.67 | 6 |
| ens_pv | ISNE | uri | 3.04 | 1.01 | -0.48 | -2.52 | 6 |
| ens_pv_bc_regime | CISO | uri | 1.85 | -0.49 | -0.89 | -1.74 | 6 |
| ens_pv_bc_regime | ISNE | uri | 2.97 | 1.58 | -0.35 | -2.10 | 6 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| additive_ml_special | CISO | elliott | 3.89 | 2.67 | -0.55 | -2.75 | 5 |
| additive_ml_special | ISNE | elliott | 4.53 | 0.92 | -0.90 | -3.30 | 5 |
| boosting_ml_pv | CISO | elliott | 3.86 | 1.39 | -0.79 | -3.74 | 5 |
| boosting_ml_pv | ISNE | elliott | 3.32 | 2.41 | -0.31 | -1.57 | 5 |
| ens_pv | CISO | elliott | 3.36 | 1.92 | -0.67 | -3.33 | 5 |
| ens_pv | ISNE | elliott | 3.52 | 1.77 | -0.55 | -1.40 | 5 |
| ens_pv_bc_regime | CISO | elliott | 3.17 | 1.15 | -0.87 | -4.10 | 5 |
| ens_pv_bc_regime | ISNE | elliott | 3.40 | 0.98 | -0.86 | -2.15 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | DF | eve | 2.90 | 1.72 | -0.42 |  | 49 |
| 8 | ens_pv | eve | 3.61 | 1.70 | -1.28 | 0.39 | 49 |
| 9 | ens_pv_bc_regime | eve | 3.73 | 2.68 | -0.84 | 0.43 | 49 |
| 6 | additive_ml_special | eve | 3.88 | 1.53 | -1.65 | 0.37 | 49 |
| 7 | boosting_ml_pv | eve | 3.91 | 1.83 | -1.11 | 0.37 | 49 |
| 0 | DF | special | 2.80 | 0.38 | -0.92 |  | 49 |
| 4 | ens_pv_bc_regime | special | 3.71 | -0.11 | -2.15 | 0.31 | 49 |
| 3 | ens_pv | special | 3.77 | -1.20 | -2.84 | 0.33 | 49 |
| 2 | boosting_ml_pv | special | 3.90 | -1.01 | -2.54 | 0.33 | 49 |
| 1 | additive_ml_special | special | 4.29 | -1.41 | -3.34 | 0.27 | 49 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_pv_bc_regime | all | 0.422 | 1.583 | 0.457 | 0.863 | 12.113 | 0.874 | 1447 |
| ens_pv_bc_regime | events | 0.451 | 1.405 | 0.376 | 0.860 | 10.960 | 0.909 | 22 |
| ens_pv_bc_regime | cold_mornings | 0.315 | 1.255 | 0.366 | 0.896 | 11.395 | 0.950 | 60 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_ml_special | CISO | mape | 13.851 | 0.000 | 737 |
| additive_ml_special | ISNE | mape | 24.101 | 0.000 | 752 |
| boosting_ml_pv | CISO | mape | 3.470 | 0.001 | 737 |
| boosting_ml_pv | ISNE | mape | 19.009 | 0.000 | 752 |
| ens_pv | CISO | mape | 4.570 | 0.000 | 737 |
| ens_pv | ISNE | mape | 18.679 | 0.000 | 752 |
| ens_pv_bc_regime | CISO | mape | -1.475 | 0.140 | 737 |
| ens_pv_bc_regime | ISNE | mape | 16.876 | 0.000 | 752 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| additive_ml_special | 0.982 |
| boosting_ml_pv | 0.996 |
| ens_pv | 0.996 |
| ens_pv_bc_regime | 0.996 |
