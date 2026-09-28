# Phase L: the NBM irradiance in the PV term

Development BAs: CISO, ISNE, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). `final6i` feeds the additive model's PV term with the NBM surface short-wave flux as seen at the cut-off, in place of the cloud fraction, at the BAs with the PV terms (ISO-NE, CAISO).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.38 | 2.22 | 0.44 | -0.59 | 0.28 | 0.00 | 0.00 | -6.96 | 1467 | 2.00 |
| final6i | 2.64 | 2.30 | 0.31 | -1.11 | 0.38 | 0.46 | 0.25 | -12.80 | 1467 | 2.00 |
| final6i_boosting | 2.90 | 2.59 | -1.25 | -2.04 | 0.46 | 0.39 | 0.17 | -16.37 | 1467 | 2.00 |
| final6i_ensemble | 3.11 | 2.71 | -2.17 | -2.68 | 0.40 | 0.35 | 0.11 | -17.31 | 1467 | 2.00 |
| final6i_additive | 3.49 | 3.00 | -2.13 | -2.96 | 0.43 | 0.29 | 0.14 | -19.54 | 1467 | 2.00 |
| final6i_recency | 5.25 | 5.02 | -4.09 | -4.44 | 0.67 | 0.07 | 0.07 | -18.25 | 1467 | 2.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.24 | -6.72 |  |  | 719 | 25193.76 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 748 | 13403.92 |
| final6i | CISO | 2.37 | 2.04 | 0.29 | -1.05 | 0.32 | -12.25 | 0.52 | 0.27 | 719 | 25193.76 |
| final6i | ISNE | 3.14 | 2.79 | 0.33 | -1.23 | 0.49 | -12.80 | 0.36 | 0.20 | 748 | 13403.92 |
| final6i_additive | CISO | 3.37 | 2.82 | -2.37 | -3.13 | 0.36 | -19.54 | 0.32 | 0.14 | 719 | 25193.76 |
| final6i_additive | ISNE | 3.72 | 3.34 | -1.66 | -2.65 | 0.54 | -18.20 | 0.23 | 0.14 | 748 | 13403.92 |
| final6i_boosting | CISO | 2.72 | 2.40 | -1.55 | -2.21 | 0.41 | -15.43 | 0.42 | 0.17 | 719 | 25193.76 |
| final6i_boosting | ISNE | 3.23 | 2.94 | -0.69 | -1.71 | 0.55 | -16.37 | 0.33 | 0.17 | 748 | 13403.92 |
| final6i_ensemble | CISO | 3.00 | 2.53 | -2.42 | -2.85 | 0.35 | -15.23 | 0.39 | 0.11 | 719 | 25193.76 |
| final6i_ensemble | ISNE | 3.31 | 3.04 | -1.72 | -2.36 | 0.51 | -17.31 | 0.28 | 0.11 | 748 | 13403.92 |
| final6i_recency | CISO | 5.30 | 5.08 | -4.42 | -4.70 | 0.66 | -15.56 | 0.07 | 0.06 | 719 | 25193.76 |
| final6i_recency | ISNE | 5.17 | 4.89 | -3.45 | -3.94 | 0.70 | -18.25 | 0.05 | 0.07 | 748 | 13403.92 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| final6i | CISO | uri | 2.02 | -0.67 | -1.19 | -2.47 | 6 |
| final6i | ISNE | uri | 2.76 | 0.99 | -0.23 | -0.76 | 6 |
| final6i_additive | CISO | uri | 2.18 | 1.38 | -0.04 | -0.23 | 6 |
| final6i_additive | ISNE | uri | 3.09 | 2.09 | -0.18 | -1.09 | 6 |
| final6i_boosting | CISO | uri | 2.13 | -0.94 | -1.36 | -3.84 | 6 |
| final6i_boosting | ISNE | uri | 3.57 | 1.35 | -0.44 | -1.93 | 6 |
| final6i_ensemble | CISO | uri | 1.99 | -0.40 | -0.87 | -1.91 | 6 |
| final6i_ensemble | ISNE | uri | 2.60 | 0.45 | -0.54 | -1.86 | 6 |
| final6i_recency | CISO | uri | 3.64 | -1.65 | -1.89 | -3.45 | 6 |
| final6i_recency | ISNE | uri | 3.79 | -2.64 | -2.64 | -4.23 | 6 |
| DF | CISO | elliott | 3.38 | 1.96 | -0.88 | -4.40 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| final6i | CISO | elliott | 3.31 | 1.81 | -0.80 | -3.59 | 5 |
| final6i | ISNE | elliott | 3.47 | 2.56 | -0.55 | -1.69 | 5 |
| final6i_additive | CISO | elliott | 3.21 | 1.29 | -0.91 | -4.55 | 5 |
| final6i_additive | ISNE | elliott | 3.91 | 0.76 | -1.12 | -3.20 | 5 |
| final6i_boosting | CISO | elliott | 3.55 | 1.25 | -1.16 | -4.14 | 5 |
| final6i_boosting | ISNE | elliott | 3.33 | 1.72 | -0.37 | -0.97 | 5 |
| final6i_ensemble | CISO | elliott | 3.12 | 1.65 | -0.84 | -3.88 | 5 |
| final6i_ensemble | ISNE | elliott | 3.44 | 1.36 | -0.90 | -2.28 | 5 |
| final6i_recency | CISO | elliott | 3.89 | 2.83 | -0.52 | -2.59 | 5 |
| final6i_recency | ISNE | elliott | 4.42 | 1.58 | -1.47 | -4.05 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | DF | eve | 2.66 | 1.83 | -0.43 |  | 48 |
| 10 | final6i_ensemble | eve | 3.16 | 1.16 | -1.09 | 0.38 | 48 |
| 8 | final6i_additive | eve | 3.33 | 1.57 | -1.09 | 0.29 | 48 |
| 7 | final6i | eve | 3.39 | 2.90 | -0.71 | 0.29 | 48 |
| 9 | final6i_boosting | eve | 3.66 | 1.81 | -0.97 | 0.33 | 48 |
| 11 | final6i_recency | eve | 4.72 | -0.73 | -2.58 | 0.08 | 48 |
| 0 | DF | special | 2.61 | 0.57 | -0.87 |  | 48 |
| 4 | final6i_ensemble | special | 3.59 | -1.51 | -2.89 | 0.29 | 48 |
| 1 | final6i | special | 3.62 | 0.14 | -1.95 | 0.33 | 48 |
| 2 | final6i_additive | special | 3.79 | -1.26 | -2.82 | 0.33 | 48 |
| 3 | final6i_boosting | special | 3.81 | -0.73 | -2.31 | 0.33 | 48 |
| 5 | final6i_recency | special | 5.18 | -3.27 | -4.60 | 0.10 | 48 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6i | all | 0.382 | 1.388 | 0.407 | 0.888 | 11.993 | 0.881 | 15.779 | 1.785 | 1425 |
| final6i | events | 0.428 | 1.421 | 0.367 | 0.858 | 11.382 | 0.909 | 15.889 | 1.821 | 22 |
| final6i | cold_mornings | 0.347 | 1.237 | 0.356 | 0.908 | 11.667 | 0.883 | 14.061 | 1.587 | 60 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6i | CISO | mape | -0.405 | 0.685 | 719 |
| final6i | ISNE | mape | 13.239 | 0.000 | 748 |
| final6i_additive | CISO | mape | 13.273 | 0.000 | 719 |
| final6i_additive | ISNE | mape | 20.373 | 0.000 | 748 |
| final6i_boosting | CISO | mape | 5.422 | 0.000 | 719 |
| final6i_boosting | ISNE | mape | 15.001 | 0.000 | 748 |
| final6i_ensemble | CISO | mape | 9.209 | 0.000 | 719 |
| final6i_ensemble | ISNE | mape | 16.832 | 0.000 | 748 |
| final6i_recency | CISO | mape | 36.743 | 0.000 | 719 |
| final6i_recency | ISNE | mape | 37.408 | 0.000 | 748 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| final6i | 0.993 |
| final6i_additive | 0.965 |
| final6i_boosting | 0.993 |
| final6i_ensemble | 0.993 |
| final6i_recency | 0.993 |
