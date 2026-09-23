# The phase F recipe on 2023 to 2025 under protocol v2

Development BAs: FPL, ISNE, MISO, PJM, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The phase F recipe (`final2`) on 2023 to 2025 scored under protocol v2, the reference for `docs/frozen_evaluation_v2.md` (same days, same rules).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | 2.38 | 2.07 | 0.23 | -1.21 | 1.31 | 0.57 | 0.27 | -37.07 | 5354 | 5.00 |
| DF | 2.57 | 2.35 | 0.49 | -0.82 | 0.89 | 0.00 | 0.00 | -41.79 | 5354 | 5.00 |
| final_ensemble | 2.70 | 2.41 | -0.77 | -1.84 | 1.34 | 0.50 | 0.22 | -41.29 | 5354 | 5.00 |
| final_additive | 2.84 | 2.49 | -0.79 | -1.95 | 1.42 | 0.46 | 0.21 | -40.92 | 5354 | 5.00 |
| final_boosting | 2.92 | 2.65 | -0.76 | -1.91 | 1.56 | 0.44 | 0.22 | -41.64 | 5354 | 5.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | FPL | 3.21 | 3.06 | -0.59 | -1.70 | 1.12 | -41.79 |  |  | 1034 | 16561.38 |
| DF | ISNE | 2.57 | 2.51 | 0.39 | -0.45 | 0.33 | -5.42 |  |  | 1079 | 12995.31 |
| DF | MISO | 2.71 | 2.50 | 2.02 | -0.23 | 0.85 | -6.54 |  |  | 1088 | 74077.99 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1069 | 93064.27 |
| DF | TVA | 2.28 | 1.96 | 0.58 | -0.89 | 1.01 | -8.44 |  |  | 1084 | 18791.86 |
| final2 | FPL | 3.51 | 3.02 | 0.56 | -1.66 | 1.11 | -37.07 | 0.52 | 0.40 | 1034 | 16561.38 |
| final2 | ISNE | 3.81 | 3.30 | 0.41 | -1.27 | 0.51 | -23.75 | 0.30 | 0.21 | 1079 | 12995.31 |
| final2 | MISO | 1.90 | 1.70 | 0.15 | -0.98 | 1.48 | -8.60 | 0.69 | 0.08 | 1088 | 74077.99 |
| final2 | PJM | 2.26 | 1.93 | 0.22 | -1.21 | 1.32 | -10.63 | 0.58 | 0.42 | 1069 | 93064.27 |
| final2 | TVA | 2.93 | 2.53 | 0.15 | -1.67 | 1.36 | -14.17 | 0.32 | 0.23 | 1084 | 18791.86 |
| final_additive | FPL | 4.92 | 4.55 | -4.36 | -5.05 | 0.99 | -40.92 | 0.28 | 0.12 | 1034 | 16561.38 |
| final_additive | ISNE | 4.30 | 3.73 | -0.71 | -2.29 | 0.58 | -22.92 | 0.23 | 0.17 | 1079 | 12995.31 |
| final_additive | MISO | 2.31 | 2.04 | -0.93 | -1.70 | 1.69 | -10.32 | 0.58 | 0.06 | 1088 | 74077.99 |
| final_additive | PJM | 2.59 | 2.26 | -0.33 | -1.62 | 1.41 | -12.48 | 0.48 | 0.35 | 1069 | 93064.27 |
| final_additive | TVA | 3.29 | 2.79 | 0.57 | -1.66 | 1.30 | -16.29 | 0.27 | 0.24 | 1084 | 18791.86 |
| final_boosting | FPL | 5.61 | 5.36 | -5.55 | -5.88 | 1.38 | -41.64 | 0.17 | 0.08 | 1034 | 16561.38 |
| final_boosting | ISNE | 4.07 | 3.52 | -1.01 | -2.07 | 0.62 | -22.84 | 0.25 | 0.15 | 1079 | 12995.31 |
| final_boosting | MISO | 2.19 | 2.05 | -0.57 | -1.43 | 1.62 | -8.98 | 0.62 | 0.07 | 1088 | 74077.99 |
| final_boosting | PJM | 2.77 | 2.48 | -0.23 | -1.60 | 1.69 | -12.43 | 0.41 | 0.38 | 1069 | 93064.27 |
| final_boosting | TVA | 3.31 | 2.82 | 0.23 | -1.78 | 1.46 | -16.13 | 0.24 | 0.22 | 1084 | 18791.86 |
| final_ensemble | FPL | 4.95 | 4.59 | -4.88 | -5.29 | 1.07 | -41.29 | 0.27 | 0.10 | 1034 | 16561.38 |
| final_ensemble | ISNE | 3.95 | 3.42 | -0.85 | -2.07 | 0.56 | -22.88 | 0.27 | 0.16 | 1079 | 12995.31 |
| final_ensemble | MISO | 2.10 | 1.91 | -0.75 | -1.48 | 1.50 | -9.14 | 0.64 | 0.06 | 1088 | 74077.99 |
| final_ensemble | PJM | 2.50 | 2.21 | -0.28 | -1.51 | 1.36 | -12.02 | 0.51 | 0.38 | 1069 | 93064.27 |
| final_ensemble | TVA | 3.17 | 2.70 | 0.40 | -1.66 | 1.31 | -15.36 | 0.27 | 0.23 | 1084 | 18791.86 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | TVA | gerri_heather | 3.50 | 2.67 | -0.73 | -4.40 | 6 |
| final2 | FPL | gerri_heather | 5.16 | -4.75 | -5.79 | -10.66 | 6 |
| final2 | ISNE | gerri_heather | 4.01 | -0.10 | -1.28 | -4.74 | 6 |
| final2 | MISO | gerri_heather | 2.65 | -1.58 | -1.97 | -4.95 | 6 |
| final2 | PJM | gerri_heather | 2.71 | -0.64 | -1.45 | -3.63 | 6 |
| final2 | TVA | gerri_heather | 2.96 | -0.71 | -2.01 | -5.88 | 6 |
| final_additive | FPL | gerri_heather | 6.47 | -8.00 | -8.00 | -14.44 | 6 |
| final_additive | ISNE | gerri_heather | 4.29 | 0.71 | -1.50 | -5.35 | 6 |
| final_additive | MISO | gerri_heather | 2.51 | -1.56 | -1.73 | -3.85 | 6 |
| final_additive | PJM | gerri_heather | 2.96 | 1.47 | -0.20 | -0.86 | 6 |
| final_additive | TVA | gerri_heather | 3.69 | 1.63 | -1.13 | -6.77 | 6 |
| final_boosting | FPL | gerri_heather | 5.51 | -7.18 | -7.51 | -13.51 | 6 |
| final_boosting | ISNE | gerri_heather | 4.05 | 0.24 | -0.73 | -3.98 | 6 |
| final_boosting | MISO | gerri_heather | 2.41 | -1.53 | -2.47 | -6.72 | 6 |
| final_boosting | PJM | gerri_heather | 2.44 | 0.19 | -1.03 | -3.13 | 6 |
| final_boosting | TVA | gerri_heather | 3.88 | -0.34 | -2.75 | -9.28 | 6 |
| final_ensemble | FPL | gerri_heather | 5.75 | -7.61 | -7.61 | -14.00 | 6 |
| final_ensemble | ISNE | gerri_heather | 4.00 | 0.46 | -1.06 | -4.63 | 6 |
| final_ensemble | MISO | gerri_heather | 2.41 | -1.55 | -2.03 | -5.29 | 6 |
| final_ensemble | PJM | gerri_heather | 2.55 | 0.86 | -0.49 | -1.92 | 6 |
| final_ensemble | TVA | gerri_heather | 3.13 | 0.65 | -1.56 | -5.28 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | TVA | january_2025 | 2.96 | 1.69 | -0.29 | -1.52 | 6 |
| final2 | FPL | january_2025 | 5.13 | -5.88 | -5.88 | -11.89 | 6 |
| final2 | ISNE | january_2025 | 3.81 | -0.92 | -1.54 | -3.06 | 6 |
| final2 | MISO | january_2025 | 2.66 | -2.86 | -2.86 | -4.40 | 6 |
| final2 | PJM | january_2025 | 2.11 | -1.09 | -1.42 | -2.98 | 6 |
| final2 | TVA | january_2025 | 3.42 | -2.18 | -2.35 | -7.58 | 6 |
| final_additive | FPL | january_2025 | 4.93 | -4.48 | -4.48 | -10.32 | 6 |
| final_additive | ISNE | january_2025 | 3.48 | -0.02 | -1.20 | -4.19 | 6 |
| final_additive | MISO | january_2025 | 2.76 | -2.91 | -2.91 | -4.80 | 6 |
| final_additive | PJM | january_2025 | 2.30 | 0.77 | -0.24 | -1.22 | 6 |
| final_additive | TVA | january_2025 | 3.71 | -1.97 | -2.52 | -7.21 | 6 |
| final_boosting | FPL | january_2025 | 4.71 | -6.26 | -6.26 | -11.78 | 6 |
| final_boosting | ISNE | january_2025 | 3.83 | 0.04 | -0.94 | -2.89 | 6 |
| final_boosting | MISO | january_2025 | 2.45 | -2.94 | -2.94 | -4.99 | 6 |
| final_boosting | PJM | january_2025 | 2.76 | -3.62 | -3.82 | -8.46 | 6 |
| final_boosting | TVA | january_2025 | 2.96 | -2.56 | -2.56 | -5.24 | 6 |
| final_ensemble | FPL | january_2025 | 4.37 | -5.40 | -5.40 | -10.56 | 6 |
| final_ensemble | ISNE | january_2025 | 3.36 | -0.00 | -0.93 | -2.50 | 6 |
| final_ensemble | MISO | january_2025 | 2.46 | -2.93 | -2.93 | -4.10 | 6 |
| final_ensemble | PJM | january_2025 | 2.05 | -1.30 | -1.55 | -3.07 | 6 |
| final_ensemble | TVA | january_2025 | 2.96 | -2.28 | -2.28 | -6.20 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | DF | eve | 2.88 | 1.25 | -0.64 |  | 146 |
| 6 | final2 | eve | 3.29 | 1.18 | -1.37 | 0.43 | 146 |
| 9 | final_ensemble | eve | 3.47 | 0.09 | -1.88 | 0.41 | 146 |
| 7 | final_additive | eve | 3.53 | 0.25 | -1.92 | 0.36 | 146 |
| 8 | final_boosting | eve | 3.85 | -0.11 | -2.02 | 0.32 | 146 |
| 0 | DF | special | 3.05 | 0.98 | -0.88 |  | 153 |
| 1 | final2 | special | 3.40 | 0.16 | -1.84 | 0.44 | 153 |
| 4 | final_ensemble | special | 3.69 | -0.85 | -2.39 | 0.40 | 153 |
| 2 | final_additive | special | 3.80 | -0.75 | -2.50 | 0.39 | 153 |
| 3 | final_boosting | special | 4.07 | -0.99 | -2.49 | 0.35 | 153 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.408 | 1.439 | 0.429 | 0.895 | 12.854 | 0.902 | 5249 |
| final2 | events | 0.472 | 1.730 | 0.557 | 0.850 | 13.527 | 0.867 | 60 |
| final2 | cold_mornings | 0.500 | 1.784 | 0.554 | 0.844 | 14.353 | 0.860 | 150 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | FPL | mape | 5.013 | 0.000 | 1034 |
| final2 | ISNE | mape | 19.019 | 0.000 | 1079 |
| final2 | MISO | mape | -16.716 | 0.000 | 1088 |
| final2 | PJM | mape | -3.321 | 0.001 | 1069 |
| final2 | TVA | mape | 13.379 | 0.000 | 1084 |
| final_additive | FPL | mape | 21.948 | 0.000 | 1034 |
| final_additive | ISNE | mape | 24.950 | 0.000 | 1079 |
| final_additive | MISO | mape | -7.632 | 0.000 | 1088 |
| final_additive | PJM | mape | 4.353 | 0.000 | 1069 |
| final_additive | TVA | mape | 18.450 | 0.000 | 1084 |
| final_boosting | FPL | mape | 30.336 | 0.000 | 1034 |
| final_boosting | ISNE | mape | 22.817 | 0.000 | 1079 |
| final_boosting | MISO | mape | -10.256 | 0.000 | 1088 |
| final_boosting | PJM | mape | 8.478 | 0.000 | 1069 |
| final_boosting | TVA | mape | 19.306 | 0.000 | 1084 |
| final_ensemble | FPL | mape | 22.882 | 0.000 | 1034 |
| final_ensemble | ISNE | mape | 21.081 | 0.000 | 1079 |
| final_ensemble | MISO | mape | -12.003 | 0.000 | 1088 |
| final_ensemble | PJM | mape | 2.461 | 0.014 | 1069 |
| final_ensemble | TVA | mape | 16.937 | 0.000 | 1084 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.992 |
| final2 | 0.989 |
| final_additive | 0.977 |
| final_boosting | 0.989 |
| final_ensemble | 0.989 |
