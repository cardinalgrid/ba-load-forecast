# Phase G: the recipe with the deeper boosting and the temperature-bias correction

Development BAs: ISNE, MISO, PJM, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3b` is `final3` with the boosting at 800 iterations, rate 0.03 and 63 leaves, and the HRRR temperature path corrected by its own recent bias per local hour (30 known days). Compare with `docs/phase_g_final.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | 2.22 | 1.93 | -0.22 | -1.30 | 1.38 | 0.59 | 0.24 | -15.22 | 2220 | 3.00 |
| final3b_ensemble | 2.25 | 1.96 | -1.36 | -1.97 | 1.38 | 0.58 | 0.17 | -16.62 | 2220 | 3.00 |
| final3b_boosting | 2.29 | 2.00 | -0.82 | -1.69 | 1.43 | 0.57 | 0.21 | -18.53 | 2220 | 3.00 |
| final3b_additive | 2.44 | 2.12 | -1.45 | -2.13 | 1.46 | 0.53 | 0.17 | -17.56 | 2220 | 3.00 |
| DF | 2.53 | 2.27 | 0.62 | -0.77 | 0.97 | 0.00 | 0.00 | -8.98 | 2220 | 3.00 |
| final3b_recency | 3.11 | 2.79 | -2.00 | -2.64 | 1.95 | 0.38 | 0.15 | -19.39 | 2220 | 3.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 748 | 13403.92 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| final3b | ISNE | 3.33 | 2.94 | 0.08 | -1.47 | 0.49 | -15.22 | 0.32 | 0.21 | 748 | 13403.92 |
| final3b | MISO | 1.98 | 1.74 | -0.23 | -1.15 | 1.57 | -8.80 | 0.63 | 0.06 | 738 | 73700.16 |
| final3b | PJM | 2.25 | 1.94 | -0.25 | -1.40 | 1.36 | -11.54 | 0.60 | 0.38 | 734 | 92076.14 |
| final3b_additive | ISNE | 3.53 | 3.18 | -1.20 | -2.26 | 0.51 | -17.56 | 0.25 | 0.15 | 748 | 13403.92 |
| final3b_additive | MISO | 2.20 | 1.91 | -1.53 | -2.03 | 1.60 | -9.16 | 0.59 | 0.04 | 738 | 73700.16 |
| final3b_additive | PJM | 2.47 | 2.13 | -1.43 | -2.19 | 1.49 | -13.39 | 0.52 | 0.27 | 734 | 92076.14 |
| final3b_boosting | ISNE | 3.42 | 3.04 | -0.51 | -1.75 | 0.54 | -18.53 | 0.29 | 0.17 | 748 | 13403.92 |
| final3b_boosting | MISO | 2.08 | 1.81 | -0.83 | -1.58 | 1.56 | -10.10 | 0.61 | 0.04 | 738 | 73700.16 |
| final3b_boosting | PJM | 2.30 | 2.00 | -0.85 | -1.78 | 1.46 | -10.70 | 0.58 | 0.35 | 734 | 92076.14 |
| final3b_ensemble | ISNE | 3.38 | 3.02 | -1.46 | -2.27 | 0.48 | -16.62 | 0.28 | 0.12 | 748 | 13403.92 |
| final3b_ensemble | MISO | 2.02 | 1.81 | -1.33 | -1.82 | 1.59 | -8.96 | 0.63 | 0.04 | 738 | 73700.16 |
| final3b_ensemble | PJM | 2.26 | 1.94 | -1.36 | -2.04 | 1.33 | -11.06 | 0.59 | 0.28 | 734 | 92076.14 |
| final3b_recency | ISNE | 5.07 | 4.74 | -3.26 | -3.89 | 0.79 | -19.39 | 0.07 | 0.09 | 748 | 13403.92 |
| final3b_recency | MISO | 2.86 | 2.52 | -1.82 | -2.37 | 2.16 | -13.40 | 0.44 | 0.04 | 738 | 73700.16 |
| final3b_recency | PJM | 3.03 | 2.71 | -1.96 | -2.68 | 1.96 | -18.17 | 0.37 | 0.26 | 734 | 92076.14 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| final3b | ISNE | uri | 2.33 | 1.05 | -0.34 | -1.97 | 6 |
| final3b | MISO | uri | 3.55 | -2.77 | -3.06 | -6.61 | 5 |
| final3b | PJM | uri | 1.91 | 0.66 | -0.59 | -2.98 | 6 |
| final3b_additive | ISNE | uri | 2.44 | 0.57 | -0.57 | -2.76 | 6 |
| final3b_additive | MISO | uri | 3.82 | -2.88 | -3.35 | -6.79 | 5 |
| final3b_additive | PJM | uri | 2.36 | 1.32 | -0.63 | -3.23 | 6 |
| final3b_boosting | ISNE | uri | 3.29 | 0.90 | -0.75 | -2.87 | 6 |
| final3b_boosting | MISO | uri | 3.23 | -3.77 | -3.77 | -6.96 | 5 |
| final3b_boosting | PJM | uri | 1.48 | -0.75 | -1.14 | -3.50 | 6 |
| final3b_ensemble | ISNE | uri | 2.33 | -0.59 | -1.13 | -3.76 | 6 |
| final3b_ensemble | MISO | uri | 4.09 | -4.14 | -4.14 | -7.68 | 5 |
| final3b_ensemble | PJM | uri | 1.87 | -0.01 | -0.85 | -3.86 | 6 |
| final3b_recency | ISNE | uri | 4.19 | -4.15 | -4.15 | -6.32 | 6 |
| final3b_recency | MISO | uri | 7.10 | -6.36 | -6.36 | -9.83 | 5 |
| final3b_recency | PJM | uri | 2.59 | -0.45 | -1.25 | -5.20 | 6 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| final3b | ISNE | elliott | 3.54 | 2.52 | -0.95 | -2.92 | 5 |
| final3b | MISO | elliott | 3.43 | -2.29 | -2.95 | -5.88 | 5 |
| final3b | PJM | elliott | 4.52 | -3.10 | -3.43 | -7.28 | 5 |
| final3b_additive | ISNE | elliott | 3.89 | -0.40 | -2.00 | -5.32 | 5 |
| final3b_additive | MISO | elliott | 3.32 | -3.87 | -4.02 | -7.52 | 5 |
| final3b_additive | PJM | elliott | 3.52 | -2.15 | -2.30 | -5.07 | 5 |
| final3b_boosting | ISNE | elliott | 3.64 | 1.79 | -1.01 | -3.89 | 5 |
| final3b_boosting | MISO | elliott | 3.61 | -2.83 | -3.51 | -4.98 | 5 |
| final3b_boosting | PJM | elliott | 4.81 | -3.75 | -4.30 | -8.86 | 5 |
| final3b_ensemble | ISNE | elliott | 3.49 | 0.94 | -1.58 | -4.93 | 5 |
| final3b_ensemble | MISO | elliott | 3.44 | -3.89 | -4.13 | -7.27 | 5 |
| final3b_ensemble | PJM | elliott | 4.47 | -4.80 | -4.80 | -9.23 | 5 |
| final3b_recency | ISNE | elliott | 4.23 | 1.17 | -2.00 | -6.17 | 5 |
| final3b_recency | MISO | elliott | 5.41 | -5.86 | -5.86 | -13.40 | 5 |
| final3b_recency | PJM | elliott | 6.50 | -9.08 | -9.08 | -18.17 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final3b_ensemble | eve | 3.04 | -0.38 | -1.96 | 0.55 | 75 |
| 8 | final3b_additive | eve | 3.14 | -0.05 | -1.86 | 0.49 | 75 |
| 7 | final3b | eve | 3.23 | 1.03 | -1.37 | 0.52 | 75 |
| 9 | final3b_boosting | eve | 3.38 | 0.41 | -1.64 | 0.59 | 75 |
| 6 | DF | eve | 3.43 | 1.88 | -0.66 |  | 75 |
| 11 | final3b_recency | eve | 4.03 | -1.99 | -3.18 | 0.43 | 75 |
| 1 | final3b | special | 3.08 | -0.97 | -2.23 | 0.56 | 75 |
| 4 | final3b_ensemble | special | 3.10 | -2.33 | -3.22 | 0.55 | 75 |
| 2 | final3b_additive | special | 3.12 | -2.57 | -3.37 | 0.45 | 75 |
| 0 | DF | special | 3.37 | 0.99 | -0.91 |  | 75 |
| 3 | final3b_boosting | special | 3.40 | -1.53 | -2.71 | 0.55 | 75 |
| 5 | final3b_recency | special | 4.21 | -3.28 | -4.26 | 0.37 | 75 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | all | 0.356 | 1.263 | 0.358 | 0.888 | 10.743 | 0.893 | 2157 |
| final3b | events | 0.434 | 1.572 | 0.635 | 0.753 | 10.455 | 0.750 | 32 |
| final3b | cold_mornings | 0.351 | 1.320 | 0.454 | 0.843 | 10.244 | 0.800 | 90 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4943 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 4942 | MISO | 2021-02-16 | final3b | 2.54 | 2.57 | 0.00 |
| 4938 | MISO | 2021-02-16 | final3b_additive | 2.09 | 2.11 | 0.00 |
| 4939 | MISO | 2021-02-16 | final3b_boosting | 2.37 | 1.39 | 0.00 |
| 4941 | MISO | 2021-02-16 | final3b_ensemble | 1.82 | 0.71 | 0.00 |
| 4940 | MISO | 2021-02-16 | final3b_recency | 3.84 | -2.24 | -2.24 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3b | ISNE | mape | 14.757 | 0.000 | 748 |
| final3b | MISO | mape | -11.024 | 0.000 | 738 |
| final3b | PJM | mape | -3.836 | 0.000 | 734 |
| final3b_additive | ISNE | mape | 18.501 | 0.000 | 748 |
| final3b_additive | MISO | mape | -6.465 | 0.000 | 738 |
| final3b_additive | PJM | mape | 0.239 | 0.811 | 734 |
| final3b_boosting | ISNE | mape | 15.711 | 0.000 | 748 |
| final3b_boosting | MISO | mape | -9.101 | 0.000 | 738 |
| final3b_boosting | PJM | mape | -2.947 | 0.003 | 734 |
| final3b_ensemble | ISNE | mape | 16.636 | 0.000 | 748 |
| final3b_ensemble | MISO | mape | -9.574 | 0.000 | 738 |
| final3b_ensemble | PJM | mape | -3.849 | 0.000 | 734 |
| final3b_recency | ISNE | mape | 34.962 | 0.000 | 748 |
| final3b_recency | MISO | mape | 2.640 | 0.008 | 738 |
| final3b_recency | PJM | mape | 9.283 | 0.000 | 734 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.996 |
| final3b | 0.993 |
| final3b_additive | 0.974 |
| final3b_boosting | 0.993 |
| final3b_ensemble | 0.993 |
| final3b_recency | 0.993 |
