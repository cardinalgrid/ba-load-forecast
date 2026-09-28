# Phase L: the NBM dew point and wind blended into the fields

Development BAs: ERCO, FPL, PJM, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). `final6f` averages the NBM dew point and wind speed with the HRRR paths of those fields, hour by hour, before the humidity and wind blocks are built (the temperature is already averaged).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6f | 2.35 | 2.00 | -0.10 | -1.34 | 1.17 | 0.58 | 0.39 | -46.39 | 2870 | 4.00 |
| DF | 2.61 | 2.29 | -0.51 | -1.47 | 0.99 | 0.00 | 0.00 | -47.43 | 2870 | 4.00 |
| final6f_ensemble | 2.70 | 2.37 | -1.84 | -2.46 | 1.13 | 0.51 | 0.27 | -49.96 | 2870 | 4.00 |
| final6f_boosting | 2.73 | 2.43 | -1.48 | -2.29 | 1.35 | 0.48 | 0.30 | -49.61 | 2870 | 4.00 |
| final6f_additive | 2.99 | 2.69 | -1.92 | -2.63 | 1.25 | 0.44 | 0.26 | -48.78 | 2870 | 4.00 |
| final6f_recency | 3.43 | 3.02 | -2.23 | -3.02 | 1.39 | 0.33 | 0.26 | -51.75 | 2870 | 4.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ERCO | 2.62 | 2.11 | 0.51 | -1.11 | 0.81 | -14.36 |  |  | 742 | 46834.59 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final6f | ERCO | 2.46 | 2.00 | -0.10 | -1.35 | 0.89 | -15.81 | 0.53 | 0.27 | 742 | 46834.59 |
| final6f | FPL | 3.54 | 2.99 | -0.63 | -2.30 | 1.00 | -46.39 | 0.62 | 0.68 | 665 | 15346.05 |
| final6f | PJM | 2.03 | 1.79 | -0.12 | -1.19 | 1.32 | -10.11 | 0.64 | 0.42 | 734 | 92076.14 |
| final6f | TVA | 2.62 | 2.24 | 0.41 | -1.24 | 1.25 | -11.15 | 0.38 | 0.33 | 729 | 18581.23 |
| final6f_additive | ERCO | 3.32 | 2.92 | -2.42 | -3.04 | 0.95 | -16.57 | 0.34 | 0.12 | 742 | 46834.59 |
| final6f_additive | FPL | 5.29 | 4.78 | -5.25 | -5.77 | 1.00 | -48.78 | 0.38 | 0.33 | 665 | 15346.05 |
| final6f_additive | PJM | 2.45 | 2.24 | -1.12 | -1.90 | 1.43 | -11.58 | 0.53 | 0.34 | 734 | 92076.14 |
| final6f_additive | TVA | 2.95 | 2.63 | -1.85 | -2.62 | 1.32 | -14.04 | 0.31 | 0.17 | 729 | 18581.23 |
| final6f_boosting | ERCO | 2.75 | 2.32 | -2.35 | -2.86 | 1.18 | -20.57 | 0.41 | 0.15 | 742 | 46834.59 |
| final6f_boosting | FPL | 5.02 | 4.73 | -5.58 | -5.90 | 1.22 | -49.61 | 0.38 | 0.30 | 665 | 15346.05 |
| final6f_boosting | PJM | 2.33 | 2.12 | -0.47 | -1.47 | 1.45 | -12.54 | 0.55 | 0.39 | 734 | 92076.14 |
| final6f_boosting | TVA | 2.72 | 2.33 | -0.88 | -1.90 | 1.37 | -12.55 | 0.35 | 0.23 | 729 | 18581.23 |
| final6f_ensemble | ERCO | 2.82 | 2.44 | -2.47 | -2.90 | 0.90 | -15.56 | 0.42 | 0.13 | 742 | 46834.59 |
| final6f_ensemble | FPL | 5.36 | 4.87 | -6.11 | -6.41 | 1.02 | -49.96 | 0.37 | 0.26 | 665 | 15346.05 |
| final6f_ensemble | PJM | 2.21 | 1.93 | -0.89 | -1.63 | 1.25 | -11.19 | 0.61 | 0.36 | 734 | 92076.14 |
| final6f_ensemble | TVA | 2.64 | 2.30 | -1.41 | -2.20 | 1.22 | -12.74 | 0.36 | 0.18 | 729 | 18581.23 |
| final6f_recency | ERCO | 3.48 | 2.98 | -2.74 | -3.36 | 1.05 | -19.11 | 0.30 | 0.15 | 742 | 46834.59 |
| final6f_recency | FPL | 6.76 | 6.00 | -8.06 | -8.36 | 1.20 | -51.75 | 0.25 | 0.20 | 665 | 15346.05 |
| final6f_recency | PJM | 2.89 | 2.58 | -1.14 | -2.04 | 1.62 | -17.18 | 0.38 | 0.33 | 734 | 92076.14 |
| final6f_recency | TVA | 3.24 | 2.87 | -1.53 | -2.65 | 1.24 | -15.53 | 0.23 | 0.19 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final6f | ERCO | uri | 6.79 | -9.15 | -9.15 | -10.29 | 2 |
| final6f | FPL | uri | 8.06 | -8.21 | -8.21 | -11.18 | 6 |
| final6f | PJM | uri | 1.72 | 0.08 | -0.56 | -2.58 | 6 |
| final6f | TVA | uri | 3.78 | -1.10 | -2.24 | -6.13 | 6 |
| final6f_additive | ERCO | uri | 5.26 | -6.89 | -6.89 | -9.48 | 2 |
| final6f_additive | FPL | uri | 9.94 | -14.30 | -14.30 | -17.55 | 6 |
| final6f_additive | PJM | uri | 2.82 | 2.27 | -0.40 | -2.43 | 6 |
| final6f_additive | TVA | uri | 3.85 | -0.54 | -1.94 | -5.78 | 6 |
| final6f_boosting | ERCO | uri | 8.77 | -14.35 | -14.35 | -15.78 | 2 |
| final6f_boosting | FPL | uri | 7.80 | -9.81 | -9.81 | -13.08 | 6 |
| final6f_boosting | PJM | uri | 1.53 | -0.96 | -1.06 | -2.57 | 6 |
| final6f_boosting | TVA | uri | 3.01 | -2.51 | -2.51 | -6.00 | 6 |
| final6f_ensemble | ERCO | uri | 6.42 | -9.21 | -9.21 | -10.94 | 2 |
| final6f_ensemble | FPL | uri | 9.82 | -13.03 | -13.03 | -16.13 | 6 |
| final6f_ensemble | PJM | uri | 1.98 | 0.51 | -0.56 | -3.05 | 6 |
| final6f_ensemble | TVA | uri | 3.46 | -1.61 | -2.27 | -5.65 | 6 |
| final6f_recency | ERCO | uri | 6.07 | -5.61 | -5.61 | -10.26 | 2 |
| final6f_recency | FPL | uri | 12.23 | -15.63 | -15.63 | -18.55 | 6 |
| final6f_recency | PJM | uri | 2.45 | 0.50 | -0.84 | -4.36 | 6 |
| final6f_recency | TVA | uri | 4.13 | -1.79 | -2.76 | -5.91 | 6 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final6f | ERCO | elliott | 5.83 | -2.27 | -3.46 | -9.09 | 5 |
| final6f | FPL | elliott | 5.39 | -5.37 | -5.37 | -9.18 | 5 |
| final6f | PJM | elliott | 4.41 | -4.19 | -4.19 | -8.67 | 5 |
| final6f | TVA | elliott | 4.42 | 1.88 | 0.00 | 0.00 | 3 |
| final6f_additive | ERCO | elliott | 7.51 | -5.85 | -6.23 | -12.82 | 5 |
| final6f_additive | FPL | elliott | 8.43 | -3.26 | -5.38 | -12.69 | 5 |
| final6f_additive | PJM | elliott | 3.32 | -2.07 | -2.07 | -7.07 | 5 |
| final6f_additive | TVA | elliott | 5.03 | 0.60 | -0.36 | -1.07 | 3 |
| final6f_boosting | ERCO | elliott | 7.37 | -11.20 | -11.20 | -20.57 | 5 |
| final6f_boosting | FPL | elliott | 8.79 | -14.48 | -14.48 | -19.75 | 5 |
| final6f_boosting | PJM | elliott | 3.96 | -4.30 | -4.30 | -7.29 | 5 |
| final6f_boosting | TVA | elliott | 4.95 | -1.20 | -1.44 | -3.68 | 3 |
| final6f_ensemble | ERCO | elliott | 6.34 | -7.15 | -7.19 | -11.98 | 5 |
| final6f_ensemble | FPL | elliott | 7.18 | -9.79 | -9.79 | -13.24 | 5 |
| final6f_ensemble | PJM | elliott | 4.18 | -4.74 | -4.74 | -9.83 | 5 |
| final6f_ensemble | TVA | elliott | 4.40 | -0.86 | -1.53 | -2.51 | 3 |
| final6f_recency | ERCO | elliott | 4.87 | -3.15 | -3.59 | -9.01 | 5 |
| final6f_recency | FPL | elliott | 9.77 | -10.68 | -10.68 | -16.50 | 5 |
| final6f_recency | PJM | elliott | 6.05 | -8.15 | -8.15 | -17.18 | 5 |
| final6f_recency | TVA | elliott | 3.92 | -2.14 | -2.96 | -4.63 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | DF | eve | 3.55 | -0.72 | -2.22 |  | 94 |
| 7 | final6f | eve | 3.55 | -0.03 | -1.80 | 0.46 | 94 |
| 10 | final6f_ensemble | eve | 3.64 | -2.36 | -3.24 | 0.48 | 94 |
| 9 | final6f_boosting | eve | 3.84 | -2.21 | -3.30 | 0.45 | 94 |
| 8 | final6f_additive | eve | 3.99 | -1.80 | -3.00 | 0.48 | 94 |
| 11 | final6f_recency | eve | 4.32 | -3.24 | -4.10 | 0.38 | 94 |
| 1 | final6f | special | 3.43 | -1.23 | -2.30 | 0.55 | 95 |
| 4 | final6f_ensemble | special | 3.78 | -3.63 | -4.10 | 0.54 | 95 |
| 0 | DF | special | 3.86 | -0.82 | -2.29 |  | 95 |
| 2 | final6f_additive | special | 3.95 | -3.19 | -3.80 | 0.47 | 95 |
| 3 | final6f_boosting | special | 3.97 | -3.75 | -4.19 | 0.49 | 95 |
| 5 | final6f_recency | special | 4.71 | -4.08 | -4.98 | 0.38 | 95 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6f | all | 0.407 | 1.322 | 0.400 | 0.888 | 11.679 | 0.893 | 16.127 | 1.728 | 2786 |
| final6f | events | 0.514 | 2.452 | 0.813 | 0.745 | 13.951 | 0.737 | 26.523 | 3.187 | 38 |
| final6f | cold_mornings | 0.526 | 1.894 | 0.663 | 0.832 | 14.534 | 0.800 | 23.774 | 2.544 | 120 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 449 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 448 | ERCO | 2021-02-17 | final6f | 31.37 | 24.59 | 0.00 |
| 444 | ERCO | 2021-02-17 | final6f_additive | 29.56 | 25.22 | 0.00 |
| 445 | ERCO | 2021-02-17 | final6f_boosting | 28.84 | 22.88 | 0.00 |
| 447 | ERCO | 2021-02-17 | final6f_ensemble | 31.65 | 26.06 | 0.00 |
| 446 | ERCO | 2021-02-17 | final6f_recency | 38.48 | 31.79 | 0.00 |
| 455 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 454 | ERCO | 2021-02-18 | final6f | 4.09 | 2.64 | 0.00 |
| 450 | ERCO | 2021-02-18 | final6f_additive | 13.29 | 11.84 | 0.00 |
| 451 | ERCO | 2021-02-18 | final6f_boosting | 4.23 | -7.71 | -7.71 |
| 453 | ERCO | 2021-02-18 | final6f_ensemble | 4.35 | 1.55 | 0.00 |
| 452 | ERCO | 2021-02-18 | final6f_recency | 5.36 | 2.19 | 0.00 |
| 17195 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 17194 | TVA | 2022-12-23 | final6f | 8.58 | -10.64 | -10.64 |
| 17190 | TVA | 2022-12-23 | final6f_additive | 6.41 | -3.28 | -3.28 |
| 17191 | TVA | 2022-12-23 | final6f_boosting | 15.73 | -16.79 | -16.79 |
| 17193 | TVA | 2022-12-23 | final6f_ensemble | 8.87 | -10.24 | -10.24 |
| 17192 | TVA | 2022-12-23 | final6f_recency | 10.04 | -11.25 | -11.25 |
| 17201 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 17200 | TVA | 2022-12-24 | final6f | 5.72 | -11.54 | -11.54 |
| 17196 | TVA | 2022-12-24 | final6f_additive | 3.83 | -9.09 | -9.09 |
| 17197 | TVA | 2022-12-24 | final6f_boosting | 7.62 | -15.18 | -15.18 |
| 17199 | TVA | 2022-12-24 | final6f_ensemble | 6.19 | -12.13 | -12.13 |
| 17198 | TVA | 2022-12-24 | final6f_recency | 7.58 | -12.30 | -12.30 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6f | ERCO | mape | -2.845 | 0.004 | 742 |
| final6f | FPL | mape | -3.721 | 0.000 | 665 |
| final6f | PJM | mape | -8.480 | 0.000 | 734 |
| final6f | TVA | mape | 8.270 | 0.000 | 729 |
| final6f_additive | ERCO | mape | 9.553 | 0.000 | 742 |
| final6f_additive | FPL | mape | 11.481 | 0.000 | 665 |
| final6f_additive | PJM | mape | -0.153 | 0.878 | 734 |
| final6f_additive | TVA | mape | 12.872 | 0.000 | 729 |
| final6f_boosting | ERCO | mape | 1.897 | 0.058 | 742 |
| final6f_boosting | FPL | mape | 10.697 | 0.000 | 665 |
| final6f_boosting | PJM | mape | -2.455 | 0.014 | 734 |
| final6f_boosting | TVA | mape | 10.010 | 0.000 | 729 |
| final6f_ensemble | ERCO | mape | 2.910 | 0.004 | 742 |
| final6f_ensemble | FPL | mape | 12.234 | 0.000 | 665 |
| final6f_ensemble | PJM | mape | -5.193 | 0.000 | 734 |
| final6f_ensemble | TVA | mape | 8.346 | 0.000 | 729 |
| final6f_recency | ERCO | mape | 10.661 | 0.000 | 742 |
| final6f_recency | FPL | mape | 18.297 | 0.000 | 665 |
| final6f_recency | PJM | mape | 7.743 | 0.000 | 734 |
| final6f_recency | TVA | mape | 16.613 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.982 |
| final6f | 0.978 |
| final6f_additive | 0.945 |
| final6f_boosting | 0.978 |
| final6f_ensemble | 0.978 |
| final6f_recency | 0.978 |
