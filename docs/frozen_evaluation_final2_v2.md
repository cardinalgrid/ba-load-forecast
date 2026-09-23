# The phase F recipe on 2023 to 2025 under protocol v2

Development BAs: FPL, ISNE, PJM, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The phase F recipe (`final2`) on 2023 to 2025 scored under protocol v2, the reference for `docs/frozen_evaluation_v2.md` (same days, same rules).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.53 | 2.33 | -0.45 | -1.16 | 0.91 | 0.00 | 0.00 | -41.79 | 3182 | 3.00 |
| final2 | 2.59 | 2.22 | 0.29 | -1.28 | 1.21 | 0.54 | 0.40 | -37.07 | 3182 | 3.00 |
| final_ensemble | 2.99 | 2.66 | -0.96 | -2.08 | 1.24 | 0.45 | 0.32 | -41.29 | 3182 | 3.00 |
| final_additive | 3.08 | 2.72 | -0.92 | -2.15 | 1.27 | 0.42 | 0.30 | -40.92 | 3182 | 3.00 |
| final_boosting | 3.29 | 2.98 | -1.03 | -2.22 | 1.53 | 0.36 | 0.31 | -41.64 | 3182 | 3.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | FPL | 3.21 | 3.06 | -0.59 | -1.70 | 1.12 | -41.79 |  |  | 1034 | 16561.38 |
| DF | ISNE | 2.57 | 2.51 | 0.39 | -0.45 | 0.33 | -5.42 |  |  | 1079 | 12995.31 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1069 | 93064.27 |
| final2 | FPL | 3.51 | 3.02 | 0.56 | -1.66 | 1.11 | -37.07 | 0.52 | 0.40 | 1034 | 16561.38 |
| final2 | ISNE | 3.81 | 3.30 | 0.41 | -1.27 | 0.51 | -23.75 | 0.30 | 0.21 | 1079 | 12995.31 |
| final2 | PJM | 2.26 | 1.93 | 0.22 | -1.21 | 1.32 | -10.63 | 0.58 | 0.42 | 1069 | 93064.27 |
| final_additive | FPL | 4.92 | 4.55 | -4.36 | -5.05 | 0.99 | -40.92 | 0.28 | 0.12 | 1034 | 16561.38 |
| final_additive | ISNE | 4.30 | 3.73 | -0.71 | -2.29 | 0.58 | -22.92 | 0.23 | 0.17 | 1079 | 12995.31 |
| final_additive | PJM | 2.59 | 2.26 | -0.33 | -1.62 | 1.41 | -12.48 | 0.48 | 0.35 | 1069 | 93064.27 |
| final_boosting | FPL | 5.61 | 5.36 | -5.55 | -5.88 | 1.38 | -41.64 | 0.17 | 0.08 | 1034 | 16561.38 |
| final_boosting | ISNE | 4.07 | 3.52 | -1.01 | -2.07 | 0.62 | -22.84 | 0.25 | 0.15 | 1079 | 12995.31 |
| final_boosting | PJM | 2.77 | 2.48 | -0.23 | -1.60 | 1.69 | -12.43 | 0.41 | 0.38 | 1069 | 93064.27 |
| final_ensemble | FPL | 4.95 | 4.59 | -4.88 | -5.29 | 1.07 | -41.29 | 0.27 | 0.10 | 1034 | 16561.38 |
| final_ensemble | ISNE | 3.95 | 3.42 | -0.85 | -2.07 | 0.56 | -22.88 | 0.27 | 0.16 | 1079 | 12995.31 |
| final_ensemble | PJM | 2.50 | 2.21 | -0.28 | -1.51 | 1.36 | -12.02 | 0.51 | 0.38 | 1069 | 93064.27 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| final2 | FPL | gerri_heather | 5.16 | -4.75 | -5.79 | -10.66 | 6 |
| final2 | ISNE | gerri_heather | 4.01 | -0.10 | -1.28 | -4.74 | 6 |
| final2 | PJM | gerri_heather | 2.71 | -0.64 | -1.45 | -3.63 | 6 |
| final_additive | FPL | gerri_heather | 6.47 | -8.00 | -8.00 | -14.44 | 6 |
| final_additive | ISNE | gerri_heather | 4.29 | 0.71 | -1.50 | -5.35 | 6 |
| final_additive | PJM | gerri_heather | 2.96 | 1.47 | -0.20 | -0.86 | 6 |
| final_boosting | FPL | gerri_heather | 5.51 | -7.18 | -7.51 | -13.51 | 6 |
| final_boosting | ISNE | gerri_heather | 4.05 | 0.24 | -0.73 | -3.98 | 6 |
| final_boosting | PJM | gerri_heather | 2.44 | 0.19 | -1.03 | -3.13 | 6 |
| final_ensemble | FPL | gerri_heather | 5.75 | -7.61 | -7.61 | -14.00 | 6 |
| final_ensemble | ISNE | gerri_heather | 4.00 | 0.46 | -1.06 | -4.63 | 6 |
| final_ensemble | PJM | gerri_heather | 2.55 | 0.86 | -0.49 | -1.92 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| final2 | FPL | january_2025 | 5.13 | -5.88 | -5.88 | -11.89 | 6 |
| final2 | ISNE | january_2025 | 3.81 | -0.92 | -1.54 | -3.06 | 6 |
| final2 | PJM | january_2025 | 2.11 | -1.09 | -1.42 | -2.98 | 6 |
| final_additive | FPL | january_2025 | 4.93 | -4.48 | -4.48 | -10.32 | 6 |
| final_additive | ISNE | january_2025 | 3.48 | -0.02 | -1.20 | -4.19 | 6 |
| final_additive | PJM | january_2025 | 2.30 | 0.77 | -0.24 | -1.22 | 6 |
| final_boosting | FPL | january_2025 | 4.71 | -6.26 | -6.26 | -11.78 | 6 |
| final_boosting | ISNE | january_2025 | 3.83 | 0.04 | -0.94 | -2.89 | 6 |
| final_boosting | PJM | january_2025 | 2.76 | -3.62 | -3.82 | -8.46 | 6 |
| final_ensemble | FPL | january_2025 | 4.37 | -5.40 | -5.40 | -10.56 | 6 |
| final_ensemble | ISNE | january_2025 | 3.36 | -0.00 | -0.93 | -2.50 | 6 |
| final_ensemble | PJM | january_2025 | 2.05 | -1.30 | -1.55 | -3.07 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | DF | eve | 2.83 | 0.65 | -0.83 |  | 88 |
| 6 | final2 | eve | 3.42 | 0.77 | -1.68 | 0.45 | 88 |
| 7 | final_additive | eve | 3.65 | -0.80 | -2.60 | 0.40 | 88 |
| 9 | final_ensemble | eve | 3.65 | -0.96 | -2.56 | 0.40 | 88 |
| 8 | final_boosting | eve | 4.19 | -1.19 | -2.79 | 0.26 | 88 |
| 0 | DF | special | 3.15 | 0.59 | -1.05 |  | 92 |
| 1 | final2 | special | 3.68 | 0.16 | -2.05 | 0.45 | 92 |
| 4 | final_ensemble | special | 4.03 | -1.52 | -3.08 | 0.40 | 92 |
| 2 | final_additive | special | 4.15 | -1.33 | -3.17 | 0.40 | 92 |
| 3 | final_boosting | special | 4.48 | -1.74 | -3.23 | 0.33 | 92 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.454 | 1.598 | 0.489 | 0.896 | 14.550 | 0.898 | 3119 |
| final2 | events | 0.538 | 1.910 | 0.687 | 0.825 | 14.253 | 0.833 | 36 |
| final2 | cold_mornings | 0.576 | 1.951 | 0.638 | 0.841 | 15.824 | 0.878 | 90 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | FPL | mape | 5.013 | 0.000 | 1034 |
| final2 | ISNE | mape | 19.019 | 0.000 | 1079 |
| final2 | PJM | mape | -3.321 | 0.001 | 1069 |
| final_additive | FPL | mape | 21.948 | 0.000 | 1034 |
| final_additive | ISNE | mape | 24.950 | 0.000 | 1079 |
| final_additive | PJM | mape | 4.353 | 0.000 | 1069 |
| final_boosting | FPL | mape | 30.336 | 0.000 | 1034 |
| final_boosting | ISNE | mape | 22.817 | 0.000 | 1079 |
| final_boosting | PJM | mape | 8.478 | 0.000 | 1069 |
| final_ensemble | FPL | mape | 22.882 | 0.000 | 1034 |
| final_ensemble | ISNE | mape | 21.081 | 0.000 | 1079 |
| final_ensemble | PJM | mape | 2.461 | 0.014 | 1069 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.988 |
| final2 | 0.984 |
| final_additive | 0.968 |
| final_boosting | 0.984 |
| final_ensemble | 0.984 |
