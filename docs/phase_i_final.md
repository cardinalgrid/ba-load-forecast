# Phase I: the candidate recipe on the development years

Development BAs: DUK, NYIS, PJM, SWPP, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final5` is `final4` with the wind block in the boosting (apparent temperature without wind chill in the additive model) and the point read at the 70th percentile around the peak on the coldest decile of days, with 23 quantiles. Compare with `docs/phase_i_events.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | 2.25 | 1.96 | -0.02 | -1.27 | 1.33 | 0.62 | 0.39 | -20.03 | 2969 | 4.00 |
| final5_ensemble | 2.42 | 2.13 | -0.54 | -1.57 | 1.37 | 0.58 | 0.37 | -20.05 | 2969 | 4.00 |
| final5_additive | 2.63 | 2.30 | -0.88 | -1.89 | 1.46 | 0.52 | 0.33 | -21.10 | 2969 | 4.00 |
| final5_boosting | 2.65 | 2.35 | -0.25 | -1.54 | 1.54 | 0.51 | 0.38 | -29.02 | 2969 | 4.00 |
| DF | 2.78 | 2.54 | -0.11 | -1.27 | 1.02 | 0.00 | 0.00 | -19.98 | 2969 | 4.00 |
| final5_recency | 3.15 | 2.78 | -0.48 | -1.85 | 1.74 | 0.38 | 0.34 | -19.85 | 2969 | 4.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.67 | 0.40 | -12.87 |  |  | 748 | 17415.28 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| final5 | DUK | 3.18 | 2.88 | 0.05 | -1.74 | 1.37 | -14.98 | 0.41 | 0.31 | 746 | 12143.29 |
| final5 | NYIS | 2.25 | 1.96 | 0.02 | -1.27 | 0.55 | -12.87 | 0.61 | 0.72 | 748 | 17415.28 |
| final5 | PJM | 2.15 | 1.88 | 0.02 | -1.20 | 1.44 | -10.65 | 0.61 | 0.43 | 734 | 92076.14 |
| final5 | SWPP | 2.17 | 1.82 | -0.18 | -1.28 | 1.41 | -20.03 | 0.75 | 0.11 | 741 | 31382.01 |
| final5_additive | DUK | 3.33 | 2.95 | -1.57 | -2.69 | 1.36 | -16.17 | 0.39 | 0.24 | 746 | 12143.29 |
| final5_additive | NYIS | 2.54 | 2.22 | -1.04 | -2.04 | 0.54 | -15.21 | 0.56 | 0.59 | 748 | 17415.28 |
| final5_additive | PJM | 2.64 | 2.33 | -0.65 | -1.72 | 1.64 | -11.72 | 0.47 | 0.38 | 734 | 92076.14 |
| final5_additive | SWPP | 2.38 | 1.98 | -1.20 | -1.97 | 1.46 | -21.10 | 0.70 | 0.08 | 741 | 31382.01 |
| final5_boosting | DUK | 3.35 | 2.93 | -0.89 | -2.32 | 1.46 | -18.54 | 0.36 | 0.27 | 746 | 12143.29 |
| final5_boosting | NYIS | 2.52 | 2.22 | -0.17 | -1.32 | 0.69 | -10.62 | 0.54 | 0.72 | 748 | 17415.28 |
| final5_boosting | PJM | 2.64 | 2.39 | 0.13 | -1.29 | 1.71 | -11.82 | 0.45 | 0.44 | 734 | 92076.14 |
| final5_boosting | SWPP | 2.49 | 2.10 | -1.14 | -2.08 | 1.52 | -29.02 | 0.70 | 0.07 | 741 | 31382.01 |
| final5_ensemble | DUK | 3.19 | 2.79 | -1.03 | -2.34 | 1.38 | -14.72 | 0.42 | 0.25 | 746 | 12143.29 |
| final5_ensemble | NYIS | 2.30 | 2.01 | -0.56 | -1.53 | 0.54 | -13.55 | 0.59 | 0.69 | 748 | 17415.28 |
| final5_ensemble | PJM | 2.43 | 2.20 | -0.36 | -1.43 | 1.52 | -10.67 | 0.54 | 0.42 | 734 | 92076.14 |
| final5_ensemble | SWPP | 2.16 | 1.77 | -0.88 | -1.69 | 1.37 | -20.05 | 0.75 | 0.09 | 741 | 31382.01 |
| final5_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final5_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final5_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final5_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| final5 | DUK | uri | 3.52 | -1.55 | -1.93 | -4.06 | 6 |
| final5 | NYIS | uri | 2.11 | 2.17 | -0.14 | -0.86 | 6 |
| final5 | PJM | uri | 1.90 | 0.26 | -0.68 | -2.76 | 6 |
| final5 | SWPP | uri | 6.61 | -0.23 | -3.30 | -7.61 | 4 |
| final5_additive | DUK | uri | 3.45 | -1.94 | -1.98 | -6.44 | 6 |
| final5_additive | NYIS | uri | 2.64 | 2.93 | 0.00 | 0.00 | 6 |
| final5_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final5_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final5_boosting | DUK | uri | 3.61 | -2.41 | -2.49 | -4.95 | 6 |
| final5_boosting | NYIS | uri | 2.76 | 1.53 | -0.44 | -2.67 | 6 |
| final5_boosting | PJM | uri | 1.95 | -0.50 | -0.92 | -2.57 | 6 |
| final5_boosting | SWPP | uri | 5.08 | -3.51 | -4.28 | -9.79 | 4 |
| final5_ensemble | DUK | uri | 3.55 | -2.56 | -2.56 | -6.14 | 6 |
| final5_ensemble | NYIS | uri | 2.25 | 2.29 | -0.09 | -0.53 | 6 |
| final5_ensemble | PJM | uri | 2.40 | 1.18 | -0.51 | -3.07 | 6 |
| final5_ensemble | SWPP | uri | 6.12 | -1.42 | -3.63 | -7.73 | 4 |
| final5_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final5_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final5_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final5_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| final5 | DUK | elliott | 3.16 | -0.29 | -1.21 | -3.05 | 4 |
| final5 | NYIS | elliott | 2.84 | 0.02 | -1.17 | -2.64 | 5 |
| final5 | PJM | elliott | 4.50 | -4.08 | -4.11 | -9.03 | 5 |
| final5 | SWPP | elliott | 4.29 | 0.87 | -1.79 | -5.43 | 5 |
| final5_additive | DUK | elliott | 4.52 | -3.26 | -3.26 | -5.10 | 4 |
| final5_additive | NYIS | elliott | 3.06 | -0.88 | -1.90 | -4.52 | 5 |
| final5_additive | PJM | elliott | 3.54 | -0.27 | -1.00 | -4.98 | 5 |
| final5_additive | SWPP | elliott | 3.13 | -2.41 | -2.70 | -5.88 | 5 |
| final5_boosting | DUK | elliott | 4.68 | -3.05 | -3.05 | -6.31 | 4 |
| final5_boosting | NYIS | elliott | 3.11 | 0.61 | -0.73 | -2.96 | 5 |
| final5_boosting | PJM | elliott | 4.64 | -2.47 | -3.04 | -6.44 | 5 |
| final5_boosting | SWPP | elliott | 5.45 | -1.84 | -3.83 | -11.88 | 5 |
| final5_ensemble | DUK | elliott | 3.71 | -3.87 | -3.87 | -4.96 | 4 |
| final5_ensemble | NYIS | elliott | 2.87 | -0.59 | -1.63 | -3.31 | 5 |
| final5_ensemble | PJM | elliott | 4.24 | -3.61 | -3.81 | -9.24 | 5 |
| final5_ensemble | SWPP | elliott | 3.65 | -2.59 | -3.28 | -8.56 | 5 |
| final5_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final5_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final5_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final5_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final5 | eve | 3.03 | 1.08 | -1.04 | 0.55 | 98 |
| 10 | final5_ensemble | eve | 3.10 | 0.33 | -1.38 | 0.57 | 98 |
| 8 | final5_additive | eve | 3.13 | 0.31 | -1.46 | 0.57 | 98 |
| 9 | final5_boosting | eve | 3.44 | 0.98 | -1.18 | 0.52 | 98 |
| 6 | DF | eve | 3.64 | 0.92 | -1.28 |  | 98 |
| 11 | final5_recency | eve | 3.91 | -0.45 | -2.12 | 0.41 | 98 |
| 2 | final5_additive | special | 3.13 | -1.50 | -2.53 | 0.63 | 99 |
| 4 | final5_ensemble | special | 3.16 | -0.89 | -2.19 | 0.65 | 99 |
| 1 | final5 | special | 3.18 | -0.05 | -1.76 | 0.65 | 99 |
| 3 | final5_boosting | special | 3.49 | -0.22 | -1.78 | 0.61 | 99 |
| 5 | final5_recency | special | 4.13 | -1.00 | -2.68 | 0.51 | 99 |
| 0 | DF | special | 4.33 | 0.05 | -1.94 |  | 99 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | all | 0.371 | 1.224 | 0.366 | 0.890 | 10.989 | 0.891 | 14.732 | 1.594 | 2884 |
| final5 | events | 0.433 | 1.737 | 0.578 | 0.768 | 10.988 | 0.829 | 20.219 | 2.293 | 41 |
| final5 | cold_mornings | 0.412 | 1.511 | 0.488 | 0.814 | 11.284 | 0.808 | 18.000 | 1.974 | 120 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4439 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4438 | DUK | 2022-12-24 | final5 | 8.38 | -9.34 | -9.34 |
| 4434 | DUK | 2022-12-24 | final5_additive | 7.22 | -13.03 | -13.03 |
| 4435 | DUK | 2022-12-24 | final5_boosting | 9.91 | -17.04 | -17.04 |
| 4437 | DUK | 2022-12-24 | final5_ensemble | 8.72 | -13.40 | -13.40 |
| 4436 | DUK | 2022-12-24 | final5_recency | 9.27 | -9.99 | -9.99 |
| 13823 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 13822 | SWPP | 2021-02-15 | final5 | 3.23 | -2.81 | -2.81 |
| 13818 | SWPP | 2021-02-15 | final5_additive | 2.24 | 1.30 | 0.00 |
| 13819 | SWPP | 2021-02-15 | final5_boosting | 6.97 | -8.54 | -8.54 |
| 13821 | SWPP | 2021-02-15 | final5_ensemble | 3.32 | -4.06 | -4.06 |
| 13820 | SWPP | 2021-02-15 | final5_recency | 4.81 | -5.28 | -5.28 |
| 13829 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 13828 | SWPP | 2021-02-16 | final5 | 3.79 | -0.23 | -0.23 |
| 13824 | SWPP | 2021-02-16 | final5_additive | 7.74 | 3.67 | 0.00 |
| 13825 | SWPP | 2021-02-16 | final5_boosting | 3.27 | -6.32 | -6.32 |
| 13827 | SWPP | 2021-02-16 | final5_ensemble | 3.83 | -0.86 | -0.86 |
| 13826 | SWPP | 2021-02-16 | final5_recency | 2.57 | -0.10 | -0.10 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final5 | DUK | mape | 5.428 | 0.000 | 746 |
| final5 | NYIS | mape | -6.553 | 0.000 | 748 |
| final5 | PJM | mape | -5.868 | 0.000 | 734 |
| final5 | SWPP | mape | -18.944 | 0.000 | 741 |
| final5_additive | DUK | mape | 7.194 | 0.000 | 746 |
| final5_additive | NYIS | mape | -1.981 | 0.048 | 748 |
| final5_additive | PJM | mape | 3.225 | 0.001 | 734 |
| final5_additive | SWPP | mape | -15.827 | 0.000 | 741 |
| final5_boosting | DUK | mape | 7.523 | 0.000 | 746 |
| final5_boosting | NYIS | mape | -2.270 | 0.023 | 748 |
| final5_boosting | PJM | mape | 3.149 | 0.002 | 734 |
| final5_boosting | SWPP | mape | -13.824 | 0.000 | 741 |
| final5_ensemble | DUK | mape | 5.356 | 0.000 | 746 |
| final5_ensemble | NYIS | mape | -5.945 | 0.000 | 748 |
| final5_ensemble | PJM | mape | -0.624 | 0.532 | 734 |
| final5_ensemble | SWPP | mape | -18.982 | 0.000 | 741 |
| final5_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final5_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final5_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final5_recency | SWPP | mape | -9.646 | 0.000 | 741 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.995 |
| final5 | 0.992 |
| final5_additive | 0.978 |
| final5_boosting | 0.992 |
| final5_ensemble | 0.992 |
| final5_recency | 0.992 |
