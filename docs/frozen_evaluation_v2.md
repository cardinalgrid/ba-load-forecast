# Second look at 2023 to 2025: the recipe after phase G, under protocol v2

Development BAs: DUK, FPL, PJM, SWPP, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase G on 2023 to 2025 under protocol v2. This is a second look at these years: the choices of phase G were made on the development period, but the frozen run of `final2` had already been seen; the honest reading compares this table with `docs/frozen_evaluation.md` and treats the difference as an estimate, not a proof.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | 2.45 | 2.07 | 0.08 | -1.38 | 1.35 | 0.57 | 0.38 | -35.37 | 4196 | 4.00 |
| final3_ensemble | 2.78 | 2.43 | -0.97 | -2.07 | 1.35 | 0.50 | 0.31 | -40.43 | 4196 | 4.00 |
| final3_additive | 2.87 | 2.47 | -0.86 | -2.10 | 1.33 | 0.48 | 0.30 | -40.44 | 4196 | 4.00 |
| DF | 2.92 | 2.34 | -0.05 | -1.28 | 1.09 | 0.00 | 0.00 | -41.79 | 4196 | 4.00 |
| final3_boosting | 3.10 | 2.73 | -0.97 | -2.21 | 1.63 | 0.41 | 0.31 | -38.96 | 4196 | 4.00 |
| final3_recency | 3.37 | 3.02 | -1.09 | -2.44 | 1.64 | 0.35 | 0.28 | -42.33 | 4196 | 4.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.65 | 2.31 | 0.43 | -1.26 | 1.02 | -13.08 |  |  | 1070 | 12295.77 |
| DF | FPL | 3.21 | 3.06 | -0.60 | -1.71 | 1.12 | -41.79 |  |  | 1003 | 16583.18 |
| DF | PJM | 2.40 | 2.17 | -0.54 | -1.17 | 0.95 | -7.65 |  |  | 1057 | 93208.59 |
| DF | SWPP | 4.33 | 2.46 | 1.42 | -1.38 | 1.49 | -17.10 |  |  | 1066 | 33074.81 |
| final3 | DUK | 3.33 | 2.78 | 0.47 | -1.84 | 1.34 | -15.01 | 0.36 | 0.27 | 1070 | 12295.77 |
| final3 | FPL | 3.43 | 2.96 | 0.58 | -1.66 | 1.06 | -35.37 | 0.51 | 0.39 | 1003 | 16583.18 |
| final3 | PJM | 2.16 | 1.87 | 0.06 | -1.23 | 1.26 | -10.24 | 0.59 | 0.40 | 1057 | 93208.59 |
| final3 | SWPP | 2.44 | 1.89 | -0.27 | -1.48 | 1.73 | -22.68 | 0.60 | 0.34 | 1066 | 33074.81 |
| final3_additive | DUK | 3.54 | 2.94 | -0.60 | -2.44 | 1.34 | -17.10 | 0.32 | 0.21 | 1070 | 12295.77 |
| final3_additive | FPL | 4.96 | 4.59 | -4.68 | -5.28 | 0.99 | -40.44 | 0.27 | 0.11 | 1003 | 16583.18 |
| final3_additive | PJM | 2.47 | 2.16 | -0.28 | -1.55 | 1.28 | -11.99 | 0.52 | 0.36 | 1057 | 93208.59 |
| final3_additive | SWPP | 2.69 | 2.13 | -0.65 | -1.92 | 1.65 | -21.92 | 0.55 | 0.28 | 1066 | 33074.81 |
| final3_boosting | DUK | 3.50 | 2.96 | -0.92 | -2.54 | 1.50 | -17.89 | 0.34 | 0.22 | 1070 | 12295.77 |
| final3_boosting | FPL | 5.42 | 5.19 | -5.50 | -5.83 | 1.34 | -38.96 | 0.19 | 0.08 | 1003 | 16583.18 |
| final3_boosting | PJM | 2.67 | 2.40 | -0.29 | -1.59 | 1.62 | -11.62 | 0.43 | 0.37 | 1057 | 93208.59 |
| final3_boosting | SWPP | 3.02 | 2.31 | -0.64 | -2.05 | 1.85 | -21.31 | 0.51 | 0.27 | 1066 | 33074.81 |
| final3_ensemble | DUK | 3.39 | 2.80 | -0.76 | -2.45 | 1.32 | -16.39 | 0.35 | 0.22 | 1070 | 12295.77 |
| final3_ensemble | FPL | 5.09 | 4.83 | -5.24 | -5.61 | 1.02 | -40.43 | 0.24 | 0.09 | 1003 | 16583.18 |
| final3_ensemble | PJM | 2.35 | 2.07 | -0.28 | -1.42 | 1.31 | -11.68 | 0.54 | 0.38 | 1057 | 93208.59 |
| final3_ensemble | SWPP | 2.62 | 2.08 | -0.87 | -2.01 | 1.64 | -22.00 | 0.56 | 0.27 | 1066 | 33074.81 |
| final3_recency | DUK | 3.97 | 3.44 | -0.74 | -2.75 | 1.47 | -17.72 | 0.26 | 0.21 | 1070 | 12295.77 |
| final3_recency | FPL | 6.17 | 5.75 | -5.73 | -6.30 | 1.17 | -42.33 | 0.13 | 0.10 | 1003 | 16583.18 |
| final3_recency | PJM | 2.91 | 2.68 | -0.21 | -1.70 | 1.71 | -12.59 | 0.36 | 0.35 | 1057 | 93208.59 |
| final3_recency | SWPP | 3.03 | 2.46 | -1.36 | -2.49 | 1.76 | -22.90 | 0.49 | 0.23 | 1066 | 33074.81 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| final3 | DUK | gerri_heather | 5.81 | -5.87 | -5.87 | -9.23 | 6 |
| final3 | FPL | gerri_heather | 4.77 | -5.17 | -5.58 | -9.75 | 6 |
| final3 | PJM | gerri_heather | 2.85 | -0.24 | -1.17 | -3.81 | 6 |
| final3 | SWPP | gerri_heather | 5.47 | -5.42 | -5.42 | -13.96 | 6 |
| final3_additive | DUK | gerri_heather | 5.92 | -7.33 | -7.33 | -15.52 | 6 |
| final3_additive | FPL | gerri_heather | 6.20 | -7.54 | -7.54 | -13.25 | 6 |
| final3_additive | PJM | gerri_heather | 2.82 | 1.45 | -0.25 | -1.13 | 6 |
| final3_additive | SWPP | gerri_heather | 7.06 | -7.68 | -7.68 | -18.06 | 6 |
| final3_boosting | DUK | gerri_heather | 5.75 | -6.18 | -6.52 | -12.16 | 6 |
| final3_boosting | FPL | gerri_heather | 5.68 | -8.78 | -8.78 | -13.39 | 6 |
| final3_boosting | PJM | gerri_heather | 2.77 | -0.14 | -1.32 | -3.77 | 6 |
| final3_boosting | SWPP | gerri_heather | 5.51 | -6.72 | -6.72 | -12.29 | 6 |
| final3_ensemble | DUK | gerri_heather | 5.86 | -7.13 | -7.13 | -14.37 | 6 |
| final3_ensemble | FPL | gerri_heather | 6.03 | -8.28 | -8.28 | -12.77 | 6 |
| final3_ensemble | PJM | gerri_heather | 2.61 | 0.66 | -0.74 | -2.65 | 6 |
| final3_ensemble | SWPP | gerri_heather | 6.77 | -7.69 | -7.69 | -15.92 | 6 |
| final3_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final3_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final3_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final3_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| final3 | DUK | january_2025 | 4.49 | 0.44 | -1.63 | -6.68 | 6 |
| final3 | FPL | january_2025 | 5.52 | -5.99 | -5.99 | -13.07 | 6 |
| final3 | PJM | january_2025 | 2.08 | -1.36 | -1.59 | -3.13 | 6 |
| final3 | SWPP | january_2025 | 2.64 | -2.44 | -2.44 | -3.80 | 6 |
| final3_additive | DUK | january_2025 | 4.08 | 1.24 | -0.85 | -5.06 | 6 |
| final3_additive | FPL | january_2025 | 4.73 | -3.67 | -3.88 | -9.71 | 6 |
| final3_additive | PJM | january_2025 | 2.43 | 0.84 | -0.36 | -1.51 | 6 |
| final3_additive | SWPP | january_2025 | 3.55 | -3.63 | -3.63 | -6.13 | 6 |
| final3_boosting | DUK | january_2025 | 4.49 | -2.71 | -3.17 | -8.26 | 6 |
| final3_boosting | FPL | january_2025 | 4.71 | -6.94 | -6.94 | -13.56 | 6 |
| final3_boosting | PJM | january_2025 | 2.50 | -3.92 | -3.92 | -7.15 | 6 |
| final3_boosting | SWPP | january_2025 | 4.55 | -8.49 | -8.49 | -9.83 | 6 |
| final3_ensemble | DUK | january_2025 | 4.09 | -0.31 | -1.74 | -7.54 | 6 |
| final3_ensemble | FPL | january_2025 | 4.30 | -4.86 | -4.86 | -10.98 | 6 |
| final3_ensemble | PJM | january_2025 | 2.21 | -1.71 | -1.81 | -3.33 | 6 |
| final3_ensemble | SWPP | january_2025 | 4.05 | -5.64 | -5.64 | -6.19 | 6 |
| final3_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final3_recency | FPL | january_2025 | 5.22 | -3.48 | -3.79 | -8.98 | 6 |
| final3_recency | PJM | january_2025 | 2.98 | -2.47 | -2.47 | -4.93 | 6 |
| final3_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.85 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final3 | eve | 3.22 | 0.90 | -1.44 | 0.53 | 116 |
| 8 | final3_additive | eve | 3.44 | -0.45 | -2.22 | 0.47 | 116 |
| 10 | final3_ensemble | eve | 3.45 | -0.64 | -2.23 | 0.52 | 116 |
| 9 | final3_boosting | eve | 3.82 | -0.93 | -2.52 | 0.39 | 116 |
| 6 | DF | eve | 3.84 | 1.67 | -0.95 |  | 116 |
| 11 | final3_recency | eve | 4.10 | -0.62 | -2.47 | 0.38 | 116 |
| 1 | final3 | special | 3.38 | 0.29 | -1.61 | 0.52 | 122 |
| 2 | final3_additive | special | 3.69 | -1.11 | -2.65 | 0.51 | 122 |
| 4 | final3_ensemble | special | 3.72 | -1.25 | -2.64 | 0.50 | 122 |
| 3 | final3_boosting | special | 4.07 | -1.51 | -2.87 | 0.37 | 122 |
| 0 | DF | special | 4.09 | 1.33 | -1.13 |  | 122 |
| 5 | final3_recency | special | 4.38 | -1.17 | -2.91 | 0.36 | 122 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | all | 0.431 | 1.421 | 0.454 | 0.891 | 12.962 | 0.892 | 4112 |
| final3 | events | 0.516 | 2.101 | 0.938 | 0.768 | 14.468 | 0.729 | 48 |
| final3 | cold_mornings | 0.499 | 1.880 | 0.693 | 0.831 | 15.487 | 0.842 | 120 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3 | DUK | mape | 11.726 | 0.000 | 1070 |
| final3 | FPL | mape | 3.999 | 0.000 | 1003 |
| final3 | PJM | mape | -5.973 | 0.000 | 1057 |
| final3 | SWPP | mape | -15.306 | 0.000 | 1066 |
| final3_additive | DUK | mape | 14.064 | 0.000 | 1070 |
| final3_additive | FPL | mape | 22.501 | 0.000 | 1003 |
| final3_additive | PJM | mape | 1.665 | 0.096 | 1057 |
| final3_additive | SWPP | mape | -12.991 | 0.000 | 1066 |
| final3_boosting | DUK | mape | 14.098 | 0.000 | 1070 |
| final3_boosting | FPL | mape | 28.932 | 0.000 | 1003 |
| final3_boosting | PJM | mape | 6.169 | 0.000 | 1057 |
| final3_boosting | SWPP | mape | -10.740 | 0.000 | 1066 |
| final3_ensemble | DUK | mape | 12.219 | 0.000 | 1070 |
| final3_ensemble | FPL | mape | 24.183 | 0.000 | 1003 |
| final3_ensemble | PJM | mape | -1.276 | 0.202 | 1057 |
| final3_ensemble | SWPP | mape | -13.833 | 0.000 | 1066 |
| final3_recency | DUK | mape | 19.472 | 0.000 | 1070 |
| final3_recency | FPL | mape | 32.912 | 0.000 | 1003 |
| final3_recency | PJM | mape | 11.821 | 0.000 | 1057 |
| final3_recency | SWPP | mape | -9.942 | 0.000 | 1066 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.990 |
| final3 | 0.987 |
| final3_additive | 0.957 |
| final3_boosting | 0.987 |
| final3_ensemble | 0.987 |
| final3_recency | 0.987 |
