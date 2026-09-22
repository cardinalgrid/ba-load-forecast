# Phase E: the sun and the forecast cloud cover as features

BAs where behind-the-meter solar matters: CISO, FPL, ISNE, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `boosting_ml_sky` is the boosting with the cosine of the solar zenith angle, the HRRR total cloud cover as seen at each day's cut-off (available from December 2020) and their product; `ens_sky` and `ens_sky_bc_regime` are the ensemble and the corrected ensemble built on it, next to the same models without those features.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 3.01 | 2.72 | -0.95 | -1.74 | 0.62 | 0.00 | 0.00 | -53.60 | 2189 | 3.00 |
| ens_sky_bc_regime | 3.26 | 2.88 | -1.15 | -2.37 | 0.62 | 0.47 | 0.30 | -49.04 | 2189 | 3.00 |
| ens_bc_regime | 3.33 | 2.96 | -1.25 | -2.43 | 0.64 | 0.46 | 0.30 | -49.03 | 2189 | 3.00 |
| ens_sky | 4.09 | 3.69 | -3.37 | -4.05 | 0.64 | 0.34 | 0.19 | -53.32 | 2189 | 3.00 |
| boosting_ml_sky | 4.12 | 3.78 | -3.17 | -3.85 | 0.74 | 0.32 | 0.21 | -52.17 | 2189 | 3.00 |
| ens_recent | 4.15 | 3.77 | -3.45 | -4.11 | 0.64 | 0.32 | 0.18 | -53.35 | 2189 | 3.00 |
| boosting_ml | 4.22 | 3.87 | -3.31 | -3.96 | 0.78 | 0.30 | 0.20 | -52.25 | 2189 | 3.00 |
| additive_ml_special | 4.61 | 4.15 | -3.71 | -4.57 | 0.63 | 0.26 | 0.18 | -54.20 | 2189 | 3.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | FPL | 3.92 | 3.63 | -3.97 | -4.36 | 1.21 | -53.60 |  |  | 700 | 15274.07 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| additive_ml_special | CISO | 3.86 | 3.50 | -3.12 | -3.96 | 0.37 | -18.80 | 0.29 | 0.14 | 737 | 25196.91 |
| additive_ml_special | FPL | 6.20 | 5.63 | -6.55 | -7.12 | 1.15 | -54.20 | 0.29 | 0.28 | 700 | 15274.07 |
| additive_ml_special | ISNE | 4.22 | 3.71 | -1.60 | -2.79 | 0.53 | -22.39 | 0.17 | 0.15 | 752 | 13392.81 |
| boosting_ml | CISO | 3.11 | 2.78 | -2.24 | -2.82 | 0.49 | -18.95 | 0.41 | 0.17 | 737 | 25196.91 |
| boosting_ml | FPL | 6.29 | 5.93 | -6.96 | -7.30 | 1.39 | -52.25 | 0.20 | 0.27 | 700 | 15274.07 |
| boosting_ml | ISNE | 3.93 | 3.56 | -1.18 | -2.30 | 0.63 | -21.45 | 0.22 | 0.16 | 752 | 13392.81 |
| boosting_ml_sky | CISO | 3.05 | 2.72 | -2.19 | -2.78 | 0.47 | -18.72 | 0.43 | 0.18 | 737 | 25196.91 |
| boosting_ml_sky | FPL | 6.27 | 5.94 | -6.83 | -7.18 | 1.34 | -52.17 | 0.19 | 0.28 | 700 | 15274.07 |
| boosting_ml_sky | ISNE | 3.67 | 3.31 | -0.85 | -2.08 | 0.59 | -21.17 | 0.24 | 0.17 | 752 | 13392.81 |
| ens_bc_regime | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| ens_bc_regime | ISNE | 3.74 | 3.31 | -0.51 | -1.95 | 0.50 | -21.57 | 0.26 | 0.16 | 752 | 13392.81 |
| ens_recent | CISO | 3.16 | 2.78 | -2.58 | -3.21 | 0.39 | -18.88 | 0.42 | 0.15 | 737 | 25196.91 |
| ens_recent | FPL | 6.05 | 5.68 | -6.70 | -7.08 | 1.17 | -53.35 | 0.26 | 0.27 | 700 | 15274.07 |
| ens_recent | ISNE | 3.83 | 3.46 | -1.36 | -2.42 | 0.52 | -21.88 | 0.22 | 0.14 | 752 | 13392.81 |
| ens_sky | CISO | 3.13 | 2.70 | -2.56 | -3.18 | 0.37 | -18.76 | 0.44 | 0.16 | 737 | 25196.91 |
| ens_sky | FPL | 6.05 | 5.69 | -6.64 | -7.03 | 1.17 | -53.32 | 0.26 | 0.28 | 700 | 15274.07 |
| ens_sky | ISNE | 3.65 | 3.26 | -1.19 | -2.29 | 0.53 | -20.77 | 0.25 | 0.15 | 752 | 13392.81 |
| ens_sky_bc_regime | CISO | 2.70 | 2.39 | -0.77 | -1.80 | 0.38 | -14.79 | 0.50 | 0.22 | 737 | 25196.91 |
| ens_sky_bc_regime | FPL | 3.91 | 3.45 | -2.45 | -3.74 | 1.14 | -49.04 | 0.57 | 0.56 | 700 | 15274.07 |
| ens_sky_bc_regime | ISNE | 3.57 | 3.15 | -0.40 | -1.85 | 0.49 | -20.00 | 0.30 | 0.16 | 752 | 13392.81 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| additive_ml_special | CISO | uri | 2.30 | 1.97 | 0.00 | 0.00 | 6 |
| additive_ml_special | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| additive_ml_special | ISNE | uri | 3.16 | 0.95 | -0.46 | -2.03 | 6 |
| boosting_ml | CISO | uri | 1.94 | -1.22 | -1.32 | -3.36 | 6 |
| boosting_ml | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| boosting_ml | ISNE | uri | 3.45 | 1.14 | -0.75 | -3.08 | 6 |
| boosting_ml_sky | CISO | uri | 1.95 | -1.00 | -1.24 | -2.68 | 6 |
| boosting_ml_sky | FPL | uri | 9.23 | -11.08 | -11.08 | -14.45 | 6 |
| boosting_ml_sky | ISNE | uri | 3.41 | 1.13 | -0.81 | -3.19 | 6 |
| ens_bc_regime | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| ens_bc_regime | ISNE | uri | 3.06 | 1.67 | -0.35 | -2.09 | 6 |
| ens_recent | CISO | uri | 1.78 | 0.44 | -0.28 | -1.40 | 6 |
| ens_recent | FPL | uri | 9.92 | -12.91 | -12.91 | -15.50 | 6 |
| ens_recent | ISNE | uri | 3.16 | 1.04 | -0.49 | -2.53 | 6 |
| ens_sky | CISO | uri | 1.79 | 0.54 | -0.20 | -0.96 | 6 |
| ens_sky | FPL | uri | 9.84 | -12.94 | -12.94 | -15.84 | 6 |
| ens_sky | ISNE | uri | 3.06 | 1.04 | -0.52 | -2.59 | 6 |
| ens_sky_bc_regime | CISO | uri | 1.93 | -0.39 | -0.88 | -1.74 | 6 |
| ens_sky_bc_regime | FPL | uri | 8.48 | -9.81 | -9.81 | -11.87 | 6 |
| ens_sky_bc_regime | ISNE | uri | 2.98 | 1.50 | -0.43 | -2.30 | 6 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| additive_ml_special | CISO | elliott | 3.89 | 2.67 | -0.55 | -2.75 | 5 |
| additive_ml_special | FPL | elliott | 11.83 | -1.71 | -7.55 | -19.18 | 5 |
| additive_ml_special | ISNE | elliott | 4.53 | 0.92 | -0.90 | -3.30 | 5 |
| boosting_ml | CISO | elliott | 3.66 | 1.13 | -0.69 | -3.11 | 5 |
| boosting_ml | FPL | elliott | 9.68 | -16.11 | -16.11 | -23.65 | 5 |
| boosting_ml | ISNE | elliott | 3.61 | 2.38 | -0.33 | -1.12 | 5 |
| boosting_ml_sky | CISO | elliott | 3.65 | 1.05 | -0.95 | -4.11 | 5 |
| boosting_ml_sky | FPL | elliott | 8.77 | -14.30 | -14.30 | -21.13 | 5 |
| boosting_ml_sky | ISNE | elliott | 3.36 | 2.69 | -0.24 | -0.61 | 5 |
| ens_bc_regime | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| ens_bc_regime | ISNE | elliott | 3.65 | 0.91 | -0.90 | -2.60 | 5 |
| ens_recent | CISO | elliott | 3.27 | 1.77 | -0.59 | -2.96 | 5 |
| ens_recent | FPL | elliott | 8.81 | -10.29 | -10.53 | -14.82 | 5 |
| ens_recent | ISNE | elliott | 3.77 | 1.69 | -0.60 | -1.85 | 5 |
| ens_sky | CISO | elliott | 3.27 | 1.72 | -0.71 | -3.54 | 5 |
| ens_sky | FPL | elliott | 8.57 | -9.24 | -9.84 | -14.44 | 5 |
| ens_sky | ISNE | elliott | 3.51 | 1.92 | -0.52 | -1.75 | 5 |
| ens_sky_bc_regime | CISO | elliott | 3.05 | 0.97 | -0.96 | -4.31 | 5 |
| ens_sky_bc_regime | FPL | elliott | 7.78 | -8.31 | -8.90 | -14.44 | 5 |
| ens_sky_bc_regime | ISNE | elliott | 3.41 | 1.15 | -0.82 | -2.52 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | DF | eve | 3.39 | -0.34 | -1.84 |  | 72 |
| 15 | ens_sky_bc_regime | eve | 4.07 | 1.08 | -1.78 | 0.44 | 72 |
| 12 | ens_bc_regime | eve | 4.12 | 1.03 | -1.83 | 0.40 | 72 |
| 14 | ens_sky | eve | 4.26 | -0.52 | -2.74 | 0.43 | 72 |
| 13 | ens_recent | eve | 4.32 | -0.55 | -2.78 | 0.39 | 72 |
| 11 | boosting_ml_sky | eve | 4.48 | -0.80 | -2.88 | 0.32 | 72 |
| 10 | boosting_ml | eve | 4.61 | -0.87 | -3.01 | 0.31 | 72 |
| 9 | additive_ml_special | eve | 4.75 | -0.15 | -3.00 | 0.33 | 72 |
| 0 | DF | special | 3.52 | -1.28 | -2.24 |  | 72 |
| 7 | ens_sky_bc_regime | special | 4.06 | -1.56 | -3.11 | 0.40 | 72 |
| 4 | ens_bc_regime | special | 4.14 | -1.60 | -3.19 | 0.35 | 72 |
| 6 | ens_sky | special | 4.56 | -3.34 | -4.47 | 0.40 | 72 |
| 5 | ens_recent | special | 4.63 | -3.38 | -4.54 | 0.35 | 72 |
| 3 | boosting_ml_sky | special | 4.72 | -3.61 | -4.62 | 0.31 | 72 |
| 2 | boosting_ml | special | 4.87 | -3.70 | -4.77 | 0.26 | 72 |
| 1 | additive_ml_special | special | 5.15 | -2.89 | -4.62 | 0.31 | 72 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_bc_regime | all | 0.476 | 1.732 | 0.502 | 0.864 | 13.170 | 0.863 | 2118 |
| ens_sky_bc_regime | all | 0.467 | 1.692 | 0.492 | 0.864 | 12.891 | 0.864 | 2118 |
| ens_bc_regime | events | 0.517 | 2.083 | 0.647 | 0.763 | 11.923 | 0.793 | 29 |
| ens_sky_bc_regime | events | 0.508 | 2.036 | 0.646 | 0.756 | 11.590 | 0.759 | 29 |
| ens_bc_regime | cold_mornings | 0.490 | 1.700 | 0.466 | 0.864 | 13.372 | 0.900 | 90 |
| ens_sky_bc_regime | cold_mornings | 0.489 | 1.678 | 0.451 | 0.867 | 13.038 | 0.878 | 90 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_ml_special | CISO | mape | 13.851 | 0.000 | 737 |
| additive_ml_special | FPL | mape | 17.271 | 0.000 | 700 |
| additive_ml_special | ISNE | mape | 24.101 | 0.000 | 752 |
| boosting_ml | CISO | mape | 4.432 | 0.000 | 737 |
| boosting_ml | FPL | mape | 21.017 | 0.000 | 700 |
| boosting_ml | ISNE | mape | 21.959 | 0.000 | 752 |
| boosting_ml_sky | CISO | mape | 3.561 | 0.000 | 737 |
| boosting_ml_sky | FPL | mape | 20.797 | 0.000 | 700 |
| boosting_ml_sky | ISNE | mape | 18.945 | 0.000 | 752 |
| ens_bc_regime | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime | FPL | mape | -0.133 | 0.895 | 700 |
| ens_bc_regime | ISNE | mape | 18.609 | 0.000 | 752 |
| ens_recent | CISO | mape | 4.977 | 0.000 | 737 |
| ens_recent | FPL | mape | 18.299 | 0.000 | 700 |
| ens_recent | ISNE | mape | 20.729 | 0.000 | 752 |
| ens_sky | CISO | mape | 4.547 | 0.000 | 737 |
| ens_sky | FPL | mape | 18.207 | 0.000 | 700 |
| ens_sky | ISNE | mape | 18.560 | 0.000 | 752 |
| ens_sky_bc_regime | CISO | mape | -1.460 | 0.144 | 737 |
| ens_sky_bc_regime | FPL | mape | -0.164 | 0.870 | 700 |
| ens_sky_bc_regime | ISNE | mape | 16.703 | 0.000 | 752 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.984 |
| additive_ml_special | 0.964 |
| boosting_ml | 0.985 |
| boosting_ml_sky | 0.985 |
| ens_bc_regime | 0.985 |
| ens_recent | 0.985 |
| ens_sky | 0.985 |
| ens_sky_bc_regime | 0.985 |
