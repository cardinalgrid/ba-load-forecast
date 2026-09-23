# Phase G: the recipe with the deeper boosting and the temperature-bias correction

Development BAs: PJM, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3b` is `final3` with the boosting at 800 iterations, rate 0.03 and 63 leaves, and the HRRR temperature path corrected by its own recent bias per local hour (30 known days). Compare with `docs/phase_g_final.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | 2.25 | 1.94 | -0.25 | -1.40 | 1.36 | 0.60 | 0.38 | -11.54 | 734 | 1.00 |
| final3b_ensemble | 2.26 | 1.94 | -1.36 | -2.04 | 1.33 | 0.59 | 0.28 | -11.06 | 734 | 1.00 |
| final3b_boosting | 2.30 | 2.00 | -0.85 | -1.78 | 1.46 | 0.58 | 0.35 | -10.70 | 734 | 1.00 |
| DF | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | 0.00 | 0.00 | -8.98 | 734 | 1.00 |
| final3b_additive | 2.47 | 2.13 | -1.43 | -2.19 | 1.49 | 0.52 | 0.27 | -13.39 | 734 | 1.00 |
| final3b_recency | 3.03 | 2.71 | -1.96 | -2.68 | 1.96 | 0.37 | 0.26 | -18.17 | 734 | 1.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| final3b | PJM | 2.25 | 1.94 | -0.25 | -1.40 | 1.36 | -11.54 | 0.60 | 0.38 | 734 | 92076.14 |
| final3b_additive | PJM | 2.47 | 2.13 | -1.43 | -2.19 | 1.49 | -13.39 | 0.52 | 0.27 | 734 | 92076.14 |
| final3b_boosting | PJM | 2.30 | 2.00 | -0.85 | -1.78 | 1.46 | -10.70 | 0.58 | 0.35 | 734 | 92076.14 |
| final3b_ensemble | PJM | 2.26 | 1.94 | -1.36 | -2.04 | 1.33 | -11.06 | 0.59 | 0.28 | 734 | 92076.14 |
| final3b_recency | PJM | 3.03 | 2.71 | -1.96 | -2.68 | 1.96 | -18.17 | 0.37 | 0.26 | 734 | 92076.14 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| final3b | PJM | uri | 1.91 | 0.66 | -0.59 | -2.98 | 6 |
| final3b_additive | PJM | uri | 2.36 | 1.32 | -0.63 | -3.23 | 6 |
| final3b_boosting | PJM | uri | 1.48 | -0.75 | -1.14 | -3.50 | 6 |
| final3b_ensemble | PJM | uri | 1.87 | -0.01 | -0.85 | -3.86 | 6 |
| final3b_recency | PJM | uri | 2.59 | -0.45 | -1.25 | -5.20 | 6 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| final3b | PJM | elliott | 4.52 | -3.10 | -3.43 | -7.28 | 5 |
| final3b_additive | PJM | elliott | 3.52 | -2.15 | -2.30 | -5.07 | 5 |
| final3b_boosting | PJM | elliott | 4.81 | -3.75 | -4.30 | -8.86 | 5 |
| final3b_ensemble | PJM | elliott | 4.47 | -4.80 | -4.80 | -9.23 | 5 |
| final3b_recency | PJM | elliott | 6.50 | -9.08 | -9.08 | -18.17 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final3b_ensemble | eve | 2.71 | -1.12 | -2.17 | 0.68 | 25 |
| 8 | final3b_additive | eve | 2.74 | -0.39 | -1.66 | 0.56 | 25 |
| 7 | final3b | eve | 2.93 | 0.22 | -1.51 | 0.64 | 25 |
| 9 | final3b_boosting | eve | 2.95 | -0.54 | -2.01 | 0.56 | 25 |
| 6 | DF | eve | 3.34 | 1.85 | -0.77 |  | 25 |
| 11 | final3b_recency | eve | 3.64 | -2.77 | -3.54 | 0.48 | 25 |
| 1 | final3b | special | 2.77 | -1.08 | -2.09 | 0.60 | 25 |
| 4 | final3b_ensemble | special | 2.83 | -2.35 | -3.13 | 0.60 | 25 |
| 2 | final3b_additive | special | 2.87 | -2.42 | -3.16 | 0.48 | 25 |
| 3 | final3b_boosting | special | 3.19 | -2.03 | -3.02 | 0.60 | 25 |
| 0 | DF | special | 3.64 | 1.33 | -1.04 |  | 25 |
| 5 | final3b_recency | special | 3.76 | -2.73 | -3.70 | 0.44 | 25 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | all | 0.331 | 1.125 | 0.320 | 0.887 | 9.671 | 0.886 | 713 |
| final3b | events | 0.372 | 1.547 | 0.698 | 0.777 | 10.038 | 0.818 | 11 |
| final3b | cold_mornings | 0.346 | 1.291 | 0.510 | 0.835 | 9.588 | 0.767 | 30 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3b | PJM | mape | -3.836 | 0.000 | 734 |
| final3b_additive | PJM | mape | 0.239 | 0.811 | 734 |
| final3b_boosting | PJM | mape | -2.947 | 0.003 | 734 |
| final3b_ensemble | PJM | mape | -3.849 | 0.000 | 734 |
| final3b_recency | PJM | mape | 9.283 | 0.000 | 734 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final3b | 0.991 |
| final3b_additive | 0.966 |
| final3b_boosting | 0.991 |
| final3b_ensemble | 0.991 |
| final3b_recency | 0.991 |
