# Phase L: the 0.7 weight and the cold-hour bias together

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). `final6wc` applies both changes.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6wc | 2.20 | 1.88 | -0.05 | -1.22 | 1.31 | 0.63 | 0.27 | -46.40 | 4353 | 6.00 |
| final6wc_ensemble | 2.39 | 2.08 | -1.64 | -2.20 | 1.30 | 0.60 | 0.18 | -49.68 | 4353 | 6.00 |
| final6wc_boosting | 2.48 | 2.20 | -1.31 | -2.06 | 1.47 | 0.56 | 0.20 | -49.02 | 4353 | 6.00 |
| final6wc_additive | 2.63 | 2.33 | -1.90 | -2.49 | 1.37 | 0.53 | 0.17 | -48.78 | 4353 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.06 | 0.00 | 0.00 | -47.43 | 4353 | 6.00 |
| final6wc_recency | 3.11 | 2.73 | -1.81 | -2.55 | 1.65 | 0.42 | 0.18 | -51.42 | 4353 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final6wc | DUK | 2.79 | 2.39 | 0.02 | -1.49 | 1.20 | -12.76 | 0.52 | 0.32 | 746 | 12143.29 |
| final6wc | FPL | 3.57 | 2.96 | -0.47 | -2.18 | 0.98 | -46.40 | 0.62 | 0.69 | 665 | 15346.05 |
| final6wc | MISO | 1.95 | 1.69 | 0.06 | -0.99 | 1.48 | -7.25 | 0.64 | 0.06 | 738 | 73700.16 |
| final6wc | PJM | 2.03 | 1.76 | -0.14 | -1.20 | 1.27 | -10.49 | 0.64 | 0.41 | 734 | 92076.14 |
| final6wc | SWPP | 2.15 | 1.76 | -0.17 | -1.25 | 1.27 | -19.95 | 0.74 | 0.10 | 741 | 31382.01 |
| final6wc | TVA | 2.62 | 2.21 | 0.41 | -1.24 | 1.22 | -11.14 | 0.39 | 0.33 | 729 | 18581.23 |
| final6wc_additive | DUK | 3.06 | 2.75 | -2.19 | -2.95 | 1.26 | -16.55 | 0.44 | 0.20 | 746 | 12143.29 |
| final6wc_additive | FPL | 5.20 | 4.67 | -5.58 | -6.04 | 1.01 | -48.78 | 0.39 | 0.28 | 665 | 15346.05 |
| final6wc_additive | MISO | 2.25 | 1.97 | -1.62 | -2.08 | 1.48 | -9.85 | 0.58 | 0.04 | 738 | 73700.16 |
| final6wc_additive | PJM | 2.45 | 2.21 | -1.47 | -2.12 | 1.38 | -12.54 | 0.51 | 0.31 | 734 | 92076.14 |
| final6wc_additive | SWPP | 2.41 | 2.00 | -1.72 | -2.34 | 1.32 | -21.87 | 0.70 | 0.06 | 741 | 31382.01 |
| final6wc_additive | TVA | 3.02 | 2.73 | -2.22 | -2.93 | 1.32 | -13.53 | 0.31 | 0.13 | 729 | 18581.23 |
| final6wc_boosting | DUK | 2.93 | 2.59 | -1.50 | -2.43 | 1.25 | -12.28 | 0.46 | 0.22 | 746 | 12143.29 |
| final6wc_boosting | FPL | 4.78 | 4.44 | -5.48 | -5.82 | 1.20 | -49.02 | 0.43 | 0.30 | 665 | 15346.05 |
| final6wc_boosting | MISO | 2.11 | 1.85 | -0.91 | -1.58 | 1.62 | -10.53 | 0.60 | 0.05 | 738 | 73700.16 |
| final6wc_boosting | PJM | 2.30 | 2.09 | -0.83 | -1.66 | 1.41 | -11.83 | 0.57 | 0.36 | 734 | 92076.14 |
| final6wc_boosting | SWPP | 2.42 | 1.98 | -1.66 | -2.34 | 1.54 | -28.19 | 0.70 | 0.05 | 741 | 31382.01 |
| final6wc_boosting | TVA | 2.71 | 2.35 | -1.10 | -2.05 | 1.39 | -12.55 | 0.35 | 0.22 | 729 | 18581.23 |
| final6wc_ensemble | DUK | 2.79 | 2.39 | -1.67 | -2.49 | 1.21 | -14.44 | 0.51 | 0.20 | 746 | 12143.29 |
| final6wc_ensemble | FPL | 5.13 | 4.65 | -6.09 | -6.39 | 1.05 | -49.68 | 0.41 | 0.26 | 665 | 15346.05 |
| final6wc_ensemble | MISO | 2.06 | 1.81 | -1.35 | -1.80 | 1.52 | -9.72 | 0.62 | 0.03 | 738 | 73700.16 |
| final6wc_ensemble | PJM | 2.19 | 1.91 | -1.20 | -1.82 | 1.21 | -11.41 | 0.62 | 0.34 | 734 | 92076.14 |
| final6wc_ensemble | SWPP | 2.13 | 1.72 | -1.39 | -1.96 | 1.26 | -20.24 | 0.74 | 0.06 | 741 | 31382.01 |
| final6wc_ensemble | TVA | 2.65 | 2.32 | -1.65 | -2.38 | 1.17 | -12.76 | 0.36 | 0.14 | 729 | 18581.23 |
| final6wc_recency | DUK | 3.36 | 3.01 | -1.28 | -2.53 | 1.42 | -15.54 | 0.38 | 0.22 | 746 | 12143.29 |
| final6wc_recency | FPL | 6.41 | 5.50 | -7.70 | -8.03 | 1.15 | -51.42 | 0.31 | 0.21 | 665 | 15346.05 |
| final6wc_recency | MISO | 2.84 | 2.49 | -1.69 | -2.20 | 2.02 | -13.18 | 0.43 | 0.04 | 738 | 73700.16 |
| final6wc_recency | PJM | 2.85 | 2.56 | -1.36 | -2.15 | 1.58 | -16.18 | 0.38 | 0.30 | 734 | 92076.14 |
| final6wc_recency | SWPP | 2.74 | 2.30 | -0.74 | -1.78 | 1.60 | -18.69 | 0.65 | 0.08 | 741 | 31382.01 |
| final6wc_recency | TVA | 3.19 | 2.76 | -1.73 | -2.73 | 1.20 | -15.53 | 0.23 | 0.16 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final6wc | DUK | uri | 3.80 | -2.57 | -2.89 | -6.08 | 6 |
| final6wc | FPL | uri | 7.83 | -8.18 | -8.18 | -11.05 | 6 |
| final6wc | MISO | uri | 3.81 | -3.35 | -3.48 | -6.92 | 5 |
| final6wc | PJM | uri | 1.67 | -0.12 | -0.58 | -2.71 | 6 |
| final6wc | SWPP | uri | 6.20 | 0.53 | -2.54 | -5.62 | 4 |
| final6wc | TVA | uri | 4.08 | -1.23 | -2.47 | -6.59 | 6 |
| final6wc_additive | DUK | uri | 3.55 | -3.29 | -3.29 | -4.78 | 6 |
| final6wc_additive | FPL | uri | 9.73 | -13.93 | -13.93 | -17.55 | 6 |
| final6wc_additive | MISO | uri | 3.57 | -2.61 | -3.14 | -6.43 | 5 |
| final6wc_additive | PJM | uri | 2.79 | 2.06 | -0.40 | -2.43 | 6 |
| final6wc_additive | SWPP | uri | 6.09 | 2.35 | -1.48 | -4.17 | 4 |
| final6wc_additive | TVA | uri | 4.08 | -0.85 | -2.26 | -6.88 | 6 |
| final6wc_boosting | DUK | uri | 3.71 | -4.39 | -4.39 | -7.23 | 6 |
| final6wc_boosting | FPL | uri | 7.54 | -9.66 | -9.66 | -13.08 | 6 |
| final6wc_boosting | MISO | uri | 2.65 | -3.02 | -3.07 | -5.66 | 5 |
| final6wc_boosting | PJM | uri | 1.53 | -1.25 | -1.37 | -2.57 | 6 |
| final6wc_boosting | SWPP | uri | 4.93 | -3.23 | -3.99 | -9.76 | 4 |
| final6wc_boosting | TVA | uri | 3.53 | -3.19 | -3.19 | -7.55 | 6 |
| final6wc_ensemble | DUK | uri | 3.78 | -4.16 | -4.16 | -6.17 | 6 |
| final6wc_ensemble | FPL | uri | 9.60 | -12.78 | -12.78 | -16.15 | 6 |
| final6wc_ensemble | MISO | uri | 3.69 | -3.69 | -3.69 | -7.09 | 5 |
| final6wc_ensemble | PJM | uri | 1.91 | 0.26 | -0.58 | -3.05 | 6 |
| final6wc_ensemble | SWPP | uri | 5.84 | -1.00 | -3.24 | -7.12 | 4 |
| final6wc_ensemble | TVA | uri | 3.82 | -2.04 | -2.75 | -6.69 | 6 |
| final6wc_recency | DUK | uri | 4.34 | -4.83 | -4.83 | -7.00 | 6 |
| final6wc_recency | FPL | uri | 12.01 | -15.27 | -15.27 | -18.55 | 6 |
| final6wc_recency | MISO | uri | 6.60 | -6.00 | -6.00 | -9.65 | 5 |
| final6wc_recency | PJM | uri | 2.38 | 0.28 | -0.86 | -4.36 | 6 |
| final6wc_recency | SWPP | uri | 6.47 | -2.63 | -4.49 | -10.54 | 4 |
| final6wc_recency | TVA | uri | 4.40 | -2.08 | -3.12 | -6.74 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final6wc | DUK | elliott | 3.08 | -2.27 | -2.47 | -5.55 | 4 |
| final6wc | FPL | elliott | 5.45 | -5.85 | -5.85 | -9.12 | 5 |
| final6wc | MISO | elliott | 3.48 | -2.66 | -3.37 | -5.98 | 5 |
| final6wc | PJM | elliott | 4.32 | -4.01 | -4.01 | -8.45 | 5 |
| final6wc | SWPP | elliott | 4.59 | 0.25 | -2.18 | -6.67 | 5 |
| final6wc | TVA | elliott | 4.14 | 0.14 | -0.58 | -1.75 | 3 |
| final6wc_additive | DUK | elliott | 3.70 | -4.54 | -4.54 | -6.51 | 4 |
| final6wc_additive | FPL | elliott | 7.56 | -3.55 | -4.98 | -11.58 | 5 |
| final6wc_additive | MISO | elliott | 3.48 | -3.99 | -4.19 | -6.63 | 5 |
| final6wc_additive | PJM | elliott | 3.48 | -2.99 | -2.99 | -7.68 | 5 |
| final6wc_additive | SWPP | elliott | 3.55 | -2.75 | -3.03 | -6.42 | 5 |
| final6wc_additive | TVA | elliott | 4.68 | -0.86 | -0.86 | -1.47 | 3 |
| final6wc_boosting | DUK | elliott | 3.91 | -3.24 | -3.24 | -6.28 | 4 |
| final6wc_boosting | FPL | elliott | 8.78 | -14.35 | -14.35 | -20.17 | 5 |
| final6wc_boosting | MISO | elliott | 3.46 | -2.51 | -3.42 | -4.61 | 5 |
| final6wc_boosting | PJM | elliott | 3.96 | -4.64 | -4.64 | -7.81 | 5 |
| final6wc_boosting | SWPP | elliott | 5.80 | -2.25 | -4.11 | -12.37 | 5 |
| final6wc_boosting | TVA | elliott | 4.67 | -2.43 | -2.43 | -3.83 | 3 |
| final6wc_ensemble | DUK | elliott | 3.49 | -4.83 | -4.83 | -5.96 | 4 |
| final6wc_ensemble | FPL | elliott | 7.19 | -9.87 | -9.87 | -13.46 | 5 |
| final6wc_ensemble | MISO | elliott | 3.55 | -3.88 | -4.22 | -7.10 | 5 |
| final6wc_ensemble | PJM | elliott | 4.24 | -5.15 | -5.15 | -10.06 | 5 |
| final6wc_ensemble | SWPP | elliott | 4.15 | -2.92 | -3.60 | -9.50 | 5 |
| final6wc_ensemble | TVA | elliott | 4.21 | -2.36 | -2.36 | -2.97 | 3 |
| final6wc_recency | DUK | elliott | 4.12 | -6.92 | -6.92 | -9.36 | 4 |
| final6wc_recency | FPL | elliott | 9.79 | -11.30 | -11.30 | -16.68 | 5 |
| final6wc_recency | MISO | elliott | 5.49 | -5.98 | -5.98 | -13.18 | 5 |
| final6wc_recency | PJM | elliott | 5.96 | -8.03 | -8.03 | -16.18 | 5 |
| final6wc_recency | SWPP | elliott | 3.72 | -3.87 | -4.35 | -10.49 | 5 |
| final6wc_recency | TVA | elliott | 3.84 | -3.98 | -3.98 | -4.95 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6wc_ensemble | eve | 3.29 | -1.22 | -2.42 | 0.61 | 142 |
| 7 | final6wc | eve | 3.37 | 0.84 | -1.37 | 0.56 | 142 |
| 8 | final6wc_additive | eve | 3.48 | -1.08 | -2.47 | 0.58 | 142 |
| 9 | final6wc_boosting | eve | 3.55 | -0.88 | -2.31 | 0.56 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final6wc_recency | eve | 3.97 | -1.92 | -3.11 | 0.48 | 142 |
| 1 | final6wc | special | 3.22 | -0.40 | -1.79 | 0.65 | 144 |
| 4 | final6wc_ensemble | special | 3.33 | -2.55 | -3.23 | 0.63 | 144 |
| 2 | final6wc_additive | special | 3.42 | -2.88 | -3.47 | 0.58 | 144 |
| 3 | final6wc_boosting | special | 3.67 | -2.35 | -3.20 | 0.56 | 144 |
| 5 | final6wc_recency | special | 4.09 | -2.52 | -3.61 | 0.52 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6wc | all | 0.389 | 1.251 | 0.363 | 0.887 | 10.920 | 0.888 | 15.035 | 1.628 | 4227 |
| final6wc | events | 0.512 | 2.184 | 0.784 | 0.701 | 12.169 | 0.667 | 25.927 | 2.870 | 60 |
| final6wc | cold_mornings | 0.469 | 1.597 | 0.545 | 0.816 | 12.123 | 0.811 | 20.274 | 2.123 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4439 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4438 | DUK | 2022-12-24 | final6wc | 9.78 | -10.94 | -10.94 |
| 4434 | DUK | 2022-12-24 | final6wc_additive | 9.11 | -12.65 | -12.65 |
| 4435 | DUK | 2022-12-24 | final6wc_boosting | 10.94 | -17.09 | -17.09 |
| 4437 | DUK | 2022-12-24 | final6wc_ensemble | 10.20 | -13.81 | -13.81 |
| 4436 | DUK | 2022-12-24 | final6wc_recency | 10.77 | -11.57 | -11.57 |
| 8927 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8926 | MISO | 2021-02-16 | final6wc | 1.70 | 1.24 | 0.00 |
| 8922 | MISO | 2021-02-16 | final6wc_additive | 2.31 | 2.11 | 0.00 |
| 8923 | MISO | 2021-02-16 | final6wc_boosting | 1.68 | 0.96 | 0.00 |
| 8925 | MISO | 2021-02-16 | final6wc_ensemble | 1.66 | 0.58 | 0.00 |
| 8924 | MISO | 2021-02-16 | final6wc_recency | 3.75 | -2.08 | -2.08 |
| 17759 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17758 | SWPP | 2021-02-15 | final6wc | 2.46 | -2.18 | -2.18 |
| 17754 | SWPP | 2021-02-15 | final6wc_additive | 2.84 | 1.38 | 0.00 |
| 17755 | SWPP | 2021-02-15 | final6wc_boosting | 6.67 | -8.08 | -8.08 |
| 17757 | SWPP | 2021-02-15 | final6wc_ensemble | 2.73 | -3.61 | -3.61 |
| 17756 | SWPP | 2021-02-15 | final6wc_recency | 4.66 | -4.67 | -4.67 |
| 17765 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17764 | SWPP | 2021-02-16 | final6wc | 4.08 | 0.02 | 0.00 |
| 17760 | SWPP | 2021-02-16 | final6wc_additive | 7.88 | 3.66 | 0.00 |
| 17761 | SWPP | 2021-02-16 | final6wc_boosting | 3.24 | -6.32 | -6.32 |
| 17763 | SWPP | 2021-02-16 | final6wc_ensemble | 3.87 | -0.86 | -0.86 |
| 17762 | SWPP | 2021-02-16 | final6wc_recency | 2.37 | -0.47 | -0.47 |
| 26105 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26104 | TVA | 2022-12-23 | final6wc | 9.54 | -11.57 | -11.57 |
| 26100 | TVA | 2022-12-23 | final6wc_additive | 6.34 | -5.44 | -5.44 |
| 26101 | TVA | 2022-12-23 | final6wc_boosting | 16.28 | -17.28 | -17.28 |
| 26103 | TVA | 2022-12-23 | final6wc_ensemble | 9.96 | -11.39 | -11.39 |
| 26102 | TVA | 2022-12-23 | final6wc_recency | 9.50 | -12.00 | -12.00 |
| 26111 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26110 | TVA | 2022-12-24 | final6wc | 6.52 | -13.17 | -13.17 |
| 26106 | TVA | 2022-12-24 | final6wc_additive | 4.47 | -10.80 | -10.80 |
| 26107 | TVA | 2022-12-24 | final6wc_boosting | 8.10 | -15.23 | -15.23 |
| 26109 | TVA | 2022-12-24 | final6wc_ensemble | 6.71 | -12.97 | -12.97 |
| 26108 | TVA | 2022-12-24 | final6wc_recency | 8.10 | -13.02 | -13.02 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6wc | DUK | mape | -0.825 | 0.409 | 746 |
| final6wc | FPL | mape | -3.190 | 0.001 | 665 |
| final6wc | MISO | mape | -11.751 | 0.000 | 738 |
| final6wc | PJM | mape | -8.670 | 0.000 | 734 |
| final6wc | SWPP | mape | -19.345 | 0.000 | 741 |
| final6wc | TVA | mape | 8.108 | 0.000 | 729 |
| final6wc_additive | DUK | mape | 3.619 | 0.000 | 746 |
| final6wc_additive | FPL | mape | 10.789 | 0.000 | 665 |
| final6wc_additive | MISO | mape | -5.663 | 0.000 | 738 |
| final6wc_additive | PJM | mape | -0.154 | 0.877 | 734 |
| final6wc_additive | SWPP | mape | -14.921 | 0.000 | 741 |
| final6wc_additive | TVA | mape | 13.927 | 0.000 | 729 |
| final6wc_boosting | DUK | mape | 1.590 | 0.112 | 746 |
| final6wc_boosting | FPL | mape | 8.477 | 0.000 | 665 |
| final6wc_boosting | MISO | mape | -8.405 | 0.000 | 738 |
| final6wc_boosting | PJM | mape | -3.257 | 0.001 | 734 |
| final6wc_boosting | SWPP | mape | -14.350 | 0.000 | 741 |
| final6wc_boosting | TVA | mape | 10.120 | 0.000 | 729 |
| final6wc_ensemble | DUK | mape | -0.832 | 0.406 | 746 |
| final6wc_ensemble | FPL | mape | 10.371 | 0.000 | 665 |
| final6wc_ensemble | MISO | mape | -8.822 | 0.000 | 738 |
| final6wc_ensemble | PJM | mape | -5.639 | 0.000 | 734 |
| final6wc_ensemble | SWPP | mape | -18.940 | 0.000 | 741 |
| final6wc_ensemble | TVA | mape | 8.660 | 0.000 | 729 |
| final6wc_recency | DUK | mape | 8.302 | 0.000 | 746 |
| final6wc_recency | FPL | mape | 16.160 | 0.000 | 665 |
| final6wc_recency | MISO | mape | 2.379 | 0.017 | 738 |
| final6wc_recency | PJM | mape | 7.196 | 0.000 | 734 |
| final6wc_recency | SWPP | mape | -11.475 | 0.000 | 741 |
| final6wc_recency | TVA | mape | 16.062 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final6wc | 0.983 |
| final6wc_additive | 0.956 |
| final6wc_boosting | 0.983 |
| final6wc_ensemble | 0.983 |
| final6wc_recency | 0.983 |
