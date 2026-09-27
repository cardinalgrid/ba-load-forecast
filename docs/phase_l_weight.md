# Phase L: 0.7 weight on the NBM in the temperature blend

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). `final6w` weights the NBM 0.7 and the HRRR 0.3 (the inverse-variance weights of the two verifications).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6w | 2.20 | 1.88 | -0.05 | -1.22 | 1.32 | 0.63 | 0.27 | -46.40 | 4353 | 6.00 |
| final6w_ensemble | 2.39 | 2.08 | -1.64 | -2.19 | 1.30 | 0.60 | 0.18 | -49.68 | 4353 | 6.00 |
| final6w_boosting | 2.48 | 2.20 | -1.31 | -2.05 | 1.46 | 0.56 | 0.21 | -49.02 | 4353 | 6.00 |
| final6w_additive | 2.63 | 2.33 | -1.90 | -2.49 | 1.36 | 0.53 | 0.17 | -48.78 | 4353 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.06 | 0.00 | 0.00 | -47.43 | 4353 | 6.00 |
| final6w_recency | 3.11 | 2.73 | -1.81 | -2.55 | 1.64 | 0.42 | 0.17 | -51.42 | 4353 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final6w | DUK | 2.79 | 2.39 | 0.02 | -1.49 | 1.20 | -12.76 | 0.52 | 0.32 | 746 | 12143.29 |
| final6w | FPL | 3.57 | 2.96 | -0.47 | -2.18 | 0.98 | -46.40 | 0.62 | 0.69 | 665 | 15346.05 |
| final6w | MISO | 1.95 | 1.69 | 0.05 | -1.00 | 1.47 | -7.25 | 0.65 | 0.06 | 738 | 73700.16 |
| final6w | PJM | 2.03 | 1.76 | -0.13 | -1.19 | 1.30 | -10.30 | 0.65 | 0.42 | 734 | 92076.14 |
| final6w | SWPP | 2.15 | 1.76 | -0.17 | -1.25 | 1.26 | -19.95 | 0.75 | 0.10 | 741 | 31382.01 |
| final6w | TVA | 2.62 | 2.21 | 0.41 | -1.25 | 1.22 | -11.14 | 0.39 | 0.33 | 729 | 18581.23 |
| final6w_additive | DUK | 3.06 | 2.75 | -2.19 | -2.95 | 1.26 | -16.55 | 0.44 | 0.20 | 746 | 12143.29 |
| final6w_additive | FPL | 5.20 | 4.67 | -5.58 | -6.04 | 1.01 | -48.78 | 0.39 | 0.28 | 665 | 15346.05 |
| final6w_additive | MISO | 2.25 | 1.96 | -1.63 | -2.09 | 1.47 | -9.85 | 0.58 | 0.04 | 738 | 73700.16 |
| final6w_additive | PJM | 2.45 | 2.21 | -1.45 | -2.11 | 1.37 | -12.54 | 0.51 | 0.31 | 734 | 92076.14 |
| final6w_additive | SWPP | 2.41 | 2.00 | -1.73 | -2.34 | 1.32 | -21.87 | 0.70 | 0.06 | 741 | 31382.01 |
| final6w_additive | TVA | 3.02 | 2.73 | -2.22 | -2.93 | 1.32 | -13.53 | 0.31 | 0.13 | 729 | 18581.23 |
| final6w_boosting | DUK | 2.93 | 2.59 | -1.50 | -2.43 | 1.25 | -12.28 | 0.46 | 0.22 | 746 | 12143.29 |
| final6w_boosting | FPL | 4.78 | 4.44 | -5.48 | -5.82 | 1.20 | -49.02 | 0.43 | 0.30 | 665 | 15346.05 |
| final6w_boosting | MISO | 2.11 | 1.84 | -0.92 | -1.59 | 1.63 | -10.53 | 0.61 | 0.05 | 738 | 73700.16 |
| final6w_boosting | PJM | 2.30 | 2.10 | -0.82 | -1.65 | 1.39 | -11.83 | 0.57 | 0.36 | 734 | 92076.14 |
| final6w_boosting | SWPP | 2.42 | 1.98 | -1.66 | -2.34 | 1.53 | -28.19 | 0.70 | 0.06 | 741 | 31382.01 |
| final6w_boosting | TVA | 2.71 | 2.34 | -1.11 | -2.05 | 1.39 | -12.55 | 0.35 | 0.22 | 729 | 18581.23 |
| final6w_ensemble | DUK | 2.79 | 2.39 | -1.67 | -2.49 | 1.21 | -14.44 | 0.51 | 0.20 | 746 | 12143.29 |
| final6w_ensemble | FPL | 5.13 | 4.65 | -6.09 | -6.39 | 1.05 | -49.68 | 0.41 | 0.26 | 665 | 15346.05 |
| final6w_ensemble | MISO | 2.06 | 1.81 | -1.36 | -1.80 | 1.52 | -9.72 | 0.62 | 0.03 | 738 | 73700.16 |
| final6w_ensemble | PJM | 2.19 | 1.90 | -1.19 | -1.81 | 1.23 | -11.41 | 0.62 | 0.33 | 734 | 92076.14 |
| final6w_ensemble | SWPP | 2.13 | 1.72 | -1.40 | -1.97 | 1.26 | -20.24 | 0.74 | 0.06 | 741 | 31382.01 |
| final6w_ensemble | TVA | 2.64 | 2.32 | -1.65 | -2.38 | 1.17 | -12.76 | 0.36 | 0.14 | 729 | 18581.23 |
| final6w_recency | DUK | 3.36 | 3.01 | -1.28 | -2.53 | 1.42 | -15.54 | 0.38 | 0.22 | 746 | 12143.29 |
| final6w_recency | FPL | 6.41 | 5.50 | -7.70 | -8.03 | 1.15 | -51.42 | 0.31 | 0.21 | 665 | 15346.05 |
| final6w_recency | MISO | 2.84 | 2.49 | -1.70 | -2.20 | 1.98 | -13.17 | 0.43 | 0.04 | 738 | 73700.16 |
| final6w_recency | PJM | 2.85 | 2.57 | -1.35 | -2.14 | 1.57 | -16.33 | 0.38 | 0.30 | 734 | 92076.14 |
| final6w_recency | SWPP | 2.75 | 2.30 | -0.75 | -1.79 | 1.60 | -18.69 | 0.65 | 0.08 | 741 | 31382.01 |
| final6w_recency | TVA | 3.19 | 2.77 | -1.73 | -2.73 | 1.21 | -15.53 | 0.23 | 0.16 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final6w | DUK | uri | 3.80 | -2.57 | -2.89 | -6.08 | 6 |
| final6w | FPL | uri | 7.83 | -8.18 | -8.18 | -11.05 | 6 |
| final6w | MISO | uri | 3.87 | -3.34 | -3.45 | -6.93 | 5 |
| final6w | PJM | uri | 1.67 | -0.11 | -0.59 | -2.50 | 6 |
| final6w | SWPP | uri | 6.12 | 0.48 | -2.55 | -5.63 | 4 |
| final6w | TVA | uri | 4.03 | -1.34 | -2.47 | -6.59 | 6 |
| final6w_additive | DUK | uri | 3.55 | -3.29 | -3.29 | -4.78 | 6 |
| final6w_additive | FPL | uri | 9.73 | -13.93 | -13.93 | -17.55 | 6 |
| final6w_additive | MISO | uri | 3.66 | -2.75 | -3.24 | -6.62 | 5 |
| final6w_additive | PJM | uri | 2.69 | 2.00 | -0.40 | -2.43 | 6 |
| final6w_additive | SWPP | uri | 5.94 | 2.18 | -1.49 | -4.18 | 4 |
| final6w_additive | TVA | uri | 4.05 | -0.97 | -2.26 | -6.88 | 6 |
| final6w_boosting | DUK | uri | 3.71 | -4.39 | -4.39 | -7.23 | 6 |
| final6w_boosting | FPL | uri | 7.54 | -9.66 | -9.66 | -13.08 | 6 |
| final6w_boosting | MISO | uri | 2.77 | -3.08 | -3.13 | -5.72 | 5 |
| final6w_boosting | PJM | uri | 1.52 | -1.31 | -1.41 | -2.57 | 6 |
| final6w_boosting | SWPP | uri | 4.82 | -3.23 | -3.99 | -9.76 | 4 |
| final6w_boosting | TVA | uri | 3.53 | -3.22 | -3.22 | -7.55 | 6 |
| final6w_ensemble | DUK | uri | 3.78 | -4.16 | -4.16 | -6.17 | 6 |
| final6w_ensemble | FPL | uri | 9.60 | -12.78 | -12.78 | -16.15 | 6 |
| final6w_ensemble | MISO | uri | 3.82 | -3.81 | -3.81 | -7.23 | 5 |
| final6w_ensemble | PJM | uri | 1.87 | 0.20 | -0.60 | -3.05 | 6 |
| final6w_ensemble | SWPP | uri | 5.72 | -1.09 | -3.24 | -7.13 | 4 |
| final6w_ensemble | TVA | uri | 3.77 | -2.14 | -2.75 | -6.69 | 6 |
| final6w_recency | DUK | uri | 4.34 | -4.83 | -4.83 | -7.00 | 6 |
| final6w_recency | FPL | uri | 12.01 | -15.27 | -15.27 | -18.55 | 6 |
| final6w_recency | MISO | uri | 6.75 | -6.12 | -6.12 | -9.80 | 5 |
| final6w_recency | PJM | uri | 2.36 | 0.21 | -0.88 | -4.36 | 6 |
| final6w_recency | SWPP | uri | 6.37 | -2.72 | -4.49 | -10.54 | 4 |
| final6w_recency | TVA | uri | 4.32 | -2.24 | -3.12 | -6.74 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final6w | DUK | elliott | 3.08 | -2.27 | -2.47 | -5.56 | 4 |
| final6w | FPL | elliott | 5.45 | -5.85 | -5.85 | -9.12 | 5 |
| final6w | MISO | elliott | 3.44 | -2.60 | -3.31 | -5.94 | 5 |
| final6w | PJM | elliott | 4.34 | -4.01 | -4.01 | -8.62 | 5 |
| final6w | SWPP | elliott | 4.58 | 0.24 | -2.24 | -7.03 | 5 |
| final6w | TVA | elliott | 4.16 | 0.08 | -0.63 | -1.89 | 3 |
| final6w_additive | DUK | elliott | 3.70 | -4.55 | -4.55 | -6.53 | 4 |
| final6w_additive | FPL | elliott | 7.56 | -3.55 | -4.98 | -11.58 | 5 |
| final6w_additive | MISO | elliott | 3.48 | -3.99 | -4.19 | -6.64 | 5 |
| final6w_additive | PJM | elliott | 3.40 | -2.66 | -2.66 | -7.43 | 5 |
| final6w_additive | SWPP | elliott | 3.56 | -2.80 | -3.07 | -6.46 | 5 |
| final6w_additive | TVA | elliott | 4.69 | -0.81 | -0.81 | -1.28 | 3 |
| final6w_boosting | DUK | elliott | 3.91 | -3.24 | -3.24 | -6.28 | 4 |
| final6w_boosting | FPL | elliott | 8.78 | -14.35 | -14.35 | -20.17 | 5 |
| final6w_boosting | MISO | elliott | 3.46 | -2.51 | -3.42 | -4.61 | 5 |
| final6w_boosting | PJM | elliott | 3.89 | -4.47 | -4.47 | -7.50 | 5 |
| final6w_boosting | SWPP | elliott | 5.76 | -2.28 | -4.13 | -12.45 | 5 |
| final6w_boosting | TVA | elliott | 4.69 | -2.50 | -2.50 | -4.04 | 3 |
| final6w_ensemble | DUK | elliott | 3.49 | -4.84 | -4.84 | -5.98 | 4 |
| final6w_ensemble | FPL | elliott | 7.19 | -9.87 | -9.87 | -13.46 | 5 |
| final6w_ensemble | MISO | elliott | 3.55 | -3.88 | -4.22 | -7.09 | 5 |
| final6w_ensemble | PJM | elliott | 4.19 | -4.99 | -4.99 | -9.92 | 5 |
| final6w_ensemble | SWPP | elliott | 4.14 | -2.98 | -3.63 | -9.64 | 5 |
| final6w_ensemble | TVA | elliott | 4.19 | -2.36 | -2.36 | -2.96 | 3 |
| final6w_recency | DUK | elliott | 4.12 | -6.93 | -6.93 | -9.36 | 4 |
| final6w_recency | FPL | elliott | 9.79 | -11.30 | -11.30 | -16.68 | 5 |
| final6w_recency | MISO | elliott | 5.49 | -5.98 | -5.98 | -13.17 | 5 |
| final6w_recency | PJM | elliott | 5.97 | -8.06 | -8.06 | -16.33 | 5 |
| final6w_recency | SWPP | elliott | 3.79 | -4.00 | -4.46 | -10.66 | 5 |
| final6w_recency | TVA | elliott | 3.81 | -3.97 | -3.97 | -4.82 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6w_ensemble | eve | 3.28 | -1.22 | -2.41 | 0.61 | 142 |
| 7 | final6w | eve | 3.37 | 0.84 | -1.37 | 0.56 | 142 |
| 8 | final6w_additive | eve | 3.48 | -1.07 | -2.46 | 0.58 | 142 |
| 9 | final6w_boosting | eve | 3.55 | -0.88 | -2.31 | 0.56 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final6w_recency | eve | 3.97 | -1.92 | -3.11 | 0.48 | 142 |
| 1 | final6w | special | 3.22 | -0.40 | -1.79 | 0.65 | 144 |
| 4 | final6w_ensemble | special | 3.33 | -2.55 | -3.23 | 0.63 | 144 |
| 2 | final6w_additive | special | 3.41 | -2.88 | -3.46 | 0.58 | 144 |
| 3 | final6w_boosting | special | 3.67 | -2.34 | -3.19 | 0.56 | 144 |
| 5 | final6w_recency | special | 4.08 | -2.53 | -3.61 | 0.52 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6w | all | 0.389 | 1.251 | 0.363 | 0.887 | 10.918 | 0.890 | 15.024 | 1.628 | 4227 |
| final6w | events | 0.508 | 2.180 | 0.792 | 0.697 | 12.139 | 0.667 | 25.992 | 2.864 | 60 |
| final6w | cold_mornings | 0.464 | 1.589 | 0.542 | 0.812 | 12.080 | 0.811 | 20.125 | 2.109 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4439 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4438 | DUK | 2022-12-24 | final6w | 9.79 | -10.95 | -10.95 |
| 4434 | DUK | 2022-12-24 | final6w_additive | 9.13 | -12.65 | -12.65 |
| 4435 | DUK | 2022-12-24 | final6w_boosting | 10.94 | -17.09 | -17.09 |
| 4437 | DUK | 2022-12-24 | final6w_ensemble | 10.21 | -13.82 | -13.82 |
| 4436 | DUK | 2022-12-24 | final6w_recency | 10.79 | -11.59 | -11.59 |
| 8927 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8926 | MISO | 2021-02-16 | final6w | 1.64 | 1.30 | 0.00 |
| 8922 | MISO | 2021-02-16 | final6w_additive | 2.19 | 1.98 | 0.00 |
| 8923 | MISO | 2021-02-16 | final6w_boosting | 1.51 | 0.96 | 0.00 |
| 8925 | MISO | 2021-02-16 | final6w_ensemble | 1.55 | 0.48 | 0.00 |
| 8924 | MISO | 2021-02-16 | final6w_recency | 3.92 | -2.26 | -2.26 |
| 17759 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17758 | SWPP | 2021-02-15 | final6w | 2.51 | -2.28 | -2.28 |
| 17754 | SWPP | 2021-02-15 | final6w_additive | 2.68 | 1.34 | 0.00 |
| 17755 | SWPP | 2021-02-15 | final6w_boosting | 6.66 | -8.08 | -8.08 |
| 17757 | SWPP | 2021-02-15 | final6w_ensemble | 2.80 | -3.67 | -3.67 |
| 17756 | SWPP | 2021-02-15 | final6w_recency | 4.67 | -4.83 | -4.83 |
| 17765 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17764 | SWPP | 2021-02-16 | final6w | 3.92 | -0.02 | -0.02 |
| 17760 | SWPP | 2021-02-16 | final6w_additive | 7.66 | 3.64 | 0.00 |
| 17761 | SWPP | 2021-02-16 | final6w_boosting | 3.37 | -6.32 | -6.32 |
| 17763 | SWPP | 2021-02-16 | final6w_ensemble | 3.71 | -0.91 | -0.91 |
| 17762 | SWPP | 2021-02-16 | final6w_recency | 2.30 | -0.57 | -0.57 |
| 26105 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26104 | TVA | 2022-12-23 | final6w | 9.41 | -11.23 | -11.23 |
| 26100 | TVA | 2022-12-23 | final6w_additive | 6.23 | -4.79 | -4.79 |
| 26101 | TVA | 2022-12-23 | final6w_boosting | 16.16 | -17.06 | -17.06 |
| 26103 | TVA | 2022-12-23 | final6w_ensemble | 9.76 | -11.04 | -11.04 |
| 26102 | TVA | 2022-12-23 | final6w_recency | 9.55 | -11.84 | -11.84 |
| 26111 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26110 | TVA | 2022-12-24 | final6w | 6.17 | -12.11 | -12.11 |
| 26106 | TVA | 2022-12-24 | final6w_additive | 4.19 | -10.10 | -10.10 |
| 26107 | TVA | 2022-12-24 | final6w_boosting | 7.91 | -15.18 | -15.18 |
| 26109 | TVA | 2022-12-24 | final6w_ensemble | 6.49 | -12.60 | -12.60 |
| 26108 | TVA | 2022-12-24 | final6w_recency | 7.92 | -12.69 | -12.69 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6w | DUK | mape | -0.825 | 0.409 | 746 |
| final6w | FPL | mape | -3.190 | 0.001 | 665 |
| final6w | MISO | mape | -11.769 | 0.000 | 738 |
| final6w | PJM | mape | -8.711 | 0.000 | 734 |
| final6w | SWPP | mape | -19.298 | 0.000 | 741 |
| final6w | TVA | mape | 8.079 | 0.000 | 729 |
| final6w_additive | DUK | mape | 3.619 | 0.000 | 746 |
| final6w_additive | FPL | mape | 10.789 | 0.000 | 665 |
| final6w_additive | MISO | mape | -5.664 | 0.000 | 738 |
| final6w_additive | PJM | mape | -0.237 | 0.813 | 734 |
| final6w_additive | SWPP | mape | -14.885 | 0.000 | 741 |
| final6w_additive | TVA | mape | 13.906 | 0.000 | 729 |
| final6w_boosting | DUK | mape | 1.590 | 0.112 | 746 |
| final6w_boosting | FPL | mape | 8.477 | 0.000 | 665 |
| final6w_boosting | MISO | mape | -8.403 | 0.000 | 738 |
| final6w_boosting | PJM | mape | -3.266 | 0.001 | 734 |
| final6w_boosting | SWPP | mape | -14.270 | 0.000 | 741 |
| final6w_boosting | TVA | mape | 10.088 | 0.000 | 729 |
| final6w_ensemble | DUK | mape | -0.832 | 0.406 | 746 |
| final6w_ensemble | FPL | mape | 10.371 | 0.000 | 665 |
| final6w_ensemble | MISO | mape | -8.815 | 0.000 | 738 |
| final6w_ensemble | PJM | mape | -5.720 | 0.000 | 734 |
| final6w_ensemble | SWPP | mape | -18.854 | 0.000 | 741 |
| final6w_ensemble | TVA | mape | 8.626 | 0.000 | 729 |
| final6w_recency | DUK | mape | 8.302 | 0.000 | 746 |
| final6w_recency | FPL | mape | 16.160 | 0.000 | 665 |
| final6w_recency | MISO | mape | 2.392 | 0.017 | 738 |
| final6w_recency | PJM | mape | 7.106 | 0.000 | 734 |
| final6w_recency | SWPP | mape | -11.425 | 0.000 | 741 |
| final6w_recency | TVA | mape | 16.030 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final6w | 0.983 |
| final6w_additive | 0.956 |
| final6w_boosting | 0.983 |
| final6w_ensemble | 0.983 |
| final6w_recency | 0.983 |
