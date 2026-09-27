# Phase L: the NBM corrected by its own cold-hour bias

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). `final6c` moves the NBM path, on hours forecast below 25 F, by the median of observed minus forecast on such hours over the last 365 known days at the station (the NBM is too warm in the cold), before the plain mean with the HRRR.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6c | 2.20 | 1.89 | -0.06 | -1.22 | 1.35 | 0.63 | 0.28 | -46.48 | 4353 | 6.00 |
| final6c_ensemble | 2.43 | 2.14 | -1.50 | -2.11 | 1.34 | 0.59 | 0.20 | -50.07 | 4353 | 6.00 |
| final6c_boosting | 2.53 | 2.26 | -1.15 | -1.97 | 1.49 | 0.55 | 0.21 | -49.76 | 4353 | 6.00 |
| final6c_additive | 2.65 | 2.37 | -1.76 | -2.40 | 1.39 | 0.53 | 0.19 | -48.93 | 4353 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.06 | 0.00 | 0.00 | -47.43 | 4353 | 6.00 |
| final6c_recency | 3.16 | 2.80 | -1.66 | -2.49 | 1.69 | 0.41 | 0.19 | -51.75 | 4353 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final6c | DUK | 2.85 | 2.47 | -0.02 | -1.54 | 1.21 | -12.25 | 0.49 | 0.31 | 746 | 12143.29 |
| final6c | FPL | 3.52 | 2.95 | -0.59 | -2.26 | 1.00 | -46.48 | 0.62 | 0.68 | 665 | 15346.05 |
| final6c | MISO | 1.95 | 1.70 | 0.07 | -0.98 | 1.50 | -6.92 | 0.64 | 0.06 | 738 | 73700.16 |
| final6c | PJM | 2.04 | 1.77 | -0.12 | -1.19 | 1.32 | -10.20 | 0.64 | 0.42 | 734 | 92076.14 |
| final6c | SWPP | 2.13 | 1.74 | -0.19 | -1.24 | 1.34 | -20.02 | 0.75 | 0.10 | 741 | 31382.01 |
| final6c | TVA | 2.64 | 2.23 | 0.42 | -1.24 | 1.26 | -11.14 | 0.37 | 0.33 | 729 | 18581.23 |
| final6c_additive | DUK | 3.08 | 2.75 | -2.04 | -2.85 | 1.28 | -16.03 | 0.44 | 0.20 | 746 | 12143.29 |
| final6c_additive | FPL | 5.44 | 4.97 | -5.76 | -6.22 | 1.01 | -48.93 | 0.35 | 0.27 | 665 | 15346.05 |
| final6c_additive | MISO | 2.25 | 1.98 | -1.53 | -2.01 | 1.46 | -9.48 | 0.57 | 0.04 | 738 | 73700.16 |
| final6c_additive | PJM | 2.47 | 2.26 | -1.25 | -1.99 | 1.44 | -12.16 | 0.52 | 0.33 | 734 | 92076.14 |
| final6c_additive | SWPP | 2.38 | 2.01 | -1.58 | -2.22 | 1.35 | -21.65 | 0.70 | 0.07 | 741 | 31382.01 |
| final6c_additive | TVA | 3.01 | 2.70 | -2.05 | -2.80 | 1.33 | -14.04 | 0.30 | 0.16 | 729 | 18581.23 |
| final6c_boosting | DUK | 2.98 | 2.63 | -1.34 | -2.35 | 1.27 | -14.52 | 0.43 | 0.23 | 746 | 12143.29 |
| final6c_boosting | FPL | 5.11 | 4.84 | -5.79 | -6.09 | 1.24 | -49.76 | 0.36 | 0.29 | 665 | 15346.05 |
| final6c_boosting | MISO | 2.13 | 1.86 | -0.80 | -1.51 | 1.60 | -10.15 | 0.60 | 0.05 | 738 | 73700.16 |
| final6c_boosting | PJM | 2.35 | 2.16 | -0.56 | -1.52 | 1.48 | -11.96 | 0.55 | 0.38 | 734 | 92076.14 |
| final6c_boosting | SWPP | 2.41 | 2.03 | -1.50 | -2.23 | 1.51 | -29.36 | 0.70 | 0.06 | 741 | 31382.01 |
| final6c_boosting | TVA | 2.76 | 2.35 | -0.96 | -1.95 | 1.34 | -12.55 | 0.34 | 0.23 | 729 | 18581.23 |
| final6c_ensemble | DUK | 2.84 | 2.48 | -1.50 | -2.40 | 1.22 | -13.85 | 0.50 | 0.22 | 746 | 12143.29 |
| final6c_ensemble | FPL | 5.45 | 5.01 | -6.37 | -6.66 | 1.04 | -50.07 | 0.36 | 0.24 | 665 | 15346.05 |
| final6c_ensemble | MISO | 2.06 | 1.83 | -1.25 | -1.72 | 1.56 | -9.29 | 0.61 | 0.04 | 738 | 73700.16 |
| final6c_ensemble | PJM | 2.22 | 1.97 | -0.97 | -1.68 | 1.26 | -11.19 | 0.61 | 0.36 | 734 | 92076.14 |
| final6c_ensemble | SWPP | 2.11 | 1.71 | -1.25 | -1.86 | 1.31 | -20.20 | 0.74 | 0.06 | 741 | 31382.01 |
| final6c_ensemble | TVA | 2.67 | 2.33 | -1.49 | -2.27 | 1.20 | -12.74 | 0.36 | 0.17 | 729 | 18581.23 |
| final6c_recency | DUK | 3.45 | 3.09 | -1.07 | -2.47 | 1.47 | -15.09 | 0.35 | 0.24 | 746 | 12143.29 |
| final6c_recency | FPL | 6.76 | 6.00 | -8.06 | -8.36 | 1.20 | -51.75 | 0.25 | 0.20 | 665 | 15346.05 |
| final6c_recency | MISO | 2.84 | 2.52 | -1.56 | -2.11 | 2.04 | -13.38 | 0.43 | 0.05 | 738 | 73700.16 |
| final6c_recency | PJM | 2.89 | 2.59 | -1.15 | -2.05 | 1.65 | -17.04 | 0.38 | 0.33 | 734 | 92076.14 |
| final6c_recency | SWPP | 2.76 | 2.32 | -0.58 | -1.71 | 1.60 | -18.50 | 0.65 | 0.09 | 741 | 31382.01 |
| final6c_recency | TVA | 3.24 | 2.87 | -1.53 | -2.65 | 1.24 | -15.53 | 0.23 | 0.19 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final6c | DUK | uri | 3.56 | -2.07 | -2.28 | -5.52 | 6 |
| final6c | FPL | uri | 8.10 | -8.26 | -8.26 | -11.43 | 6 |
| final6c | MISO | uri | 3.86 | -3.37 | -3.51 | -6.92 | 5 |
| final6c | PJM | uri | 1.73 | 0.05 | -0.58 | -2.75 | 6 |
| final6c | SWPP | uri | 6.19 | 0.39 | -2.69 | -6.02 | 4 |
| final6c | TVA | uri | 3.86 | -1.19 | -2.39 | -6.16 | 6 |
| final6c_additive | DUK | uri | 3.43 | -2.90 | -2.90 | -3.67 | 6 |
| final6c_additive | FPL | uri | 9.94 | -14.30 | -14.30 | -17.55 | 6 |
| final6c_additive | MISO | uri | 3.59 | -2.56 | -3.12 | -6.45 | 5 |
| final6c_additive | PJM | uri | 2.89 | 2.32 | -0.40 | -2.43 | 6 |
| final6c_additive | SWPP | uri | 6.21 | 2.17 | -1.66 | -4.45 | 4 |
| final6c_additive | TVA | uri | 3.87 | -0.45 | -1.94 | -5.78 | 6 |
| final6c_boosting | DUK | uri | 3.38 | -3.25 | -3.25 | -6.53 | 6 |
| final6c_boosting | FPL | uri | 7.93 | -9.98 | -9.98 | -13.08 | 6 |
| final6c_boosting | MISO | uri | 2.55 | -2.88 | -2.92 | -5.24 | 5 |
| final6c_boosting | PJM | uri | 1.58 | -0.84 | -1.02 | -2.57 | 6 |
| final6c_boosting | SWPP | uri | 4.94 | -3.23 | -3.99 | -9.76 | 4 |
| final6c_boosting | TVA | uri | 3.10 | -2.51 | -2.51 | -6.09 | 6 |
| final6c_ensemble | DUK | uri | 3.56 | -3.52 | -3.52 | -4.97 | 6 |
| final6c_ensemble | FPL | uri | 9.87 | -13.10 | -13.10 | -16.14 | 6 |
| final6c_ensemble | MISO | uri | 3.68 | -3.63 | -3.63 | -6.94 | 5 |
| final6c_ensemble | PJM | uri | 2.04 | 0.59 | -0.54 | -3.05 | 6 |
| final6c_ensemble | SWPP | uri | 5.91 | -1.10 | -3.33 | -7.31 | 4 |
| final6c_ensemble | TVA | uri | 3.53 | -1.54 | -2.28 | -5.65 | 6 |
| final6c_recency | DUK | uri | 4.16 | -4.42 | -4.42 | -6.02 | 6 |
| final6c_recency | FPL | uri | 12.23 | -15.63 | -15.63 | -18.55 | 6 |
| final6c_recency | MISO | uri | 6.63 | -5.97 | -5.97 | -9.58 | 5 |
| final6c_recency | PJM | uri | 2.47 | 0.55 | -0.83 | -4.36 | 6 |
| final6c_recency | SWPP | uri | 6.54 | -2.68 | -4.54 | -10.56 | 4 |
| final6c_recency | TVA | uri | 4.19 | -1.68 | -2.76 | -5.91 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final6c | DUK | elliott | 3.05 | -2.02 | -2.09 | -5.32 | 4 |
| final6c | FPL | elliott | 5.34 | -5.31 | -5.31 | -8.93 | 5 |
| final6c | MISO | elliott | 3.44 | -2.45 | -3.16 | -6.34 | 5 |
| final6c | PJM | elliott | 4.38 | -4.24 | -4.24 | -8.69 | 5 |
| final6c | SWPP | elliott | 4.44 | 0.36 | -2.12 | -6.44 | 5 |
| final6c | TVA | elliott | 4.36 | 1.92 | 0.00 | 0.00 | 3 |
| final6c_additive | DUK | elliott | 3.85 | -4.21 | -4.21 | -6.00 | 4 |
| final6c_additive | FPL | elliott | 8.43 | -3.26 | -5.38 | -12.69 | 5 |
| final6c_additive | MISO | elliott | 3.40 | -3.69 | -3.93 | -6.55 | 5 |
| final6c_additive | PJM | elliott | 3.34 | -2.30 | -2.30 | -7.24 | 5 |
| final6c_additive | SWPP | elliott | 3.42 | -2.65 | -2.94 | -6.27 | 5 |
| final6c_additive | TVA | elliott | 5.02 | 0.55 | -0.42 | -1.20 | 3 |
| final6c_boosting | DUK | elliott | 4.05 | -3.65 | -3.65 | -6.28 | 4 |
| final6c_boosting | FPL | elliott | 8.92 | -14.63 | -14.63 | -19.75 | 5 |
| final6c_boosting | MISO | elliott | 3.41 | -2.15 | -3.06 | -4.15 | 5 |
| final6c_boosting | PJM | elliott | 3.92 | -4.33 | -4.33 | -7.50 | 5 |
| final6c_boosting | SWPP | elliott | 5.67 | -2.22 | -4.08 | -12.25 | 5 |
| final6c_boosting | TVA | elliott | 4.77 | -1.19 | -1.48 | -3.79 | 3 |
| final6c_ensemble | DUK | elliott | 3.52 | -4.72 | -4.72 | -5.75 | 4 |
| final6c_ensemble | FPL | elliott | 7.21 | -9.78 | -9.78 | -13.12 | 5 |
| final6c_ensemble | MISO | elliott | 3.45 | -3.61 | -3.95 | -7.20 | 5 |
| final6c_ensemble | PJM | elliott | 4.18 | -4.83 | -4.83 | -9.92 | 5 |
| final6c_ensemble | SWPP | elliott | 4.01 | -2.86 | -3.53 | -9.26 | 5 |
| final6c_ensemble | TVA | elliott | 4.38 | -0.87 | -1.58 | -2.59 | 3 |
| final6c_recency | DUK | elliott | 4.06 | -6.47 | -6.47 | -9.27 | 4 |
| final6c_recency | FPL | elliott | 9.77 | -10.68 | -10.68 | -16.50 | 5 |
| final6c_recency | MISO | elliott | 5.41 | -5.84 | -5.87 | -13.38 | 5 |
| final6c_recency | PJM | elliott | 6.03 | -8.12 | -8.12 | -17.04 | 5 |
| final6c_recency | SWPP | elliott | 3.59 | -3.80 | -4.25 | -10.20 | 5 |
| final6c_recency | TVA | elliott | 3.94 | -2.15 | -3.01 | -4.72 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6c_ensemble | eve | 3.34 | -1.12 | -2.37 | 0.58 | 142 |
| 7 | final6c | eve | 3.38 | 0.81 | -1.38 | 0.56 | 142 |
| 8 | final6c_additive | eve | 3.54 | -0.94 | -2.40 | 0.56 | 142 |
| 9 | final6c_boosting | eve | 3.61 | -0.79 | -2.31 | 0.55 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final6c_recency | eve | 4.06 | -1.82 | -3.08 | 0.46 | 142 |
| 1 | final6c | special | 3.27 | -0.51 | -1.88 | 0.64 | 144 |
| 4 | final6c_ensemble | special | 3.40 | -2.45 | -3.19 | 0.62 | 144 |
| 2 | final6c_additive | special | 3.47 | -2.71 | -3.37 | 0.58 | 144 |
| 3 | final6c_boosting | special | 3.75 | -2.30 | -3.23 | 0.56 | 144 |
| 5 | final6c_recency | special | 4.20 | -2.40 | -3.59 | 0.51 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6c | all | 0.388 | 1.252 | 0.365 | 0.888 | 10.980 | 0.892 | 15.062 | 1.629 | 4227 |
| final6c | events | 0.515 | 2.174 | 0.779 | 0.699 | 12.209 | 0.667 | 25.881 | 2.854 | 60 |
| final6c | cold_mornings | 0.485 | 1.627 | 0.542 | 0.809 | 12.360 | 0.806 | 20.538 | 2.157 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4439 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4438 | DUK | 2022-12-24 | final6c | 9.29 | -11.02 | -11.02 |
| 4434 | DUK | 2022-12-24 | final6c_additive | 8.54 | -12.76 | -12.76 |
| 4435 | DUK | 2022-12-24 | final6c_boosting | 10.59 | -17.02 | -17.02 |
| 4437 | DUK | 2022-12-24 | final6c_ensemble | 9.74 | -13.67 | -13.67 |
| 4436 | DUK | 2022-12-24 | final6c_recency | 10.33 | -11.11 | -11.11 |
| 8927 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8926 | MISO | 2021-02-16 | final6c | 1.68 | 1.42 | 0.00 |
| 8922 | MISO | 2021-02-16 | final6c_additive | 2.33 | 2.13 | 0.00 |
| 8923 | MISO | 2021-02-16 | final6c_boosting | 2.09 | 1.28 | 0.00 |
| 8925 | MISO | 2021-02-16 | final6c_ensemble | 1.71 | 0.70 | 0.00 |
| 8924 | MISO | 2021-02-16 | final6c_recency | 3.71 | -2.08 | -2.08 |
| 17759 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17758 | SWPP | 2021-02-15 | final6c | 2.53 | -2.32 | -2.32 |
| 17754 | SWPP | 2021-02-15 | final6c_additive | 2.67 | 1.35 | 0.00 |
| 17755 | SWPP | 2021-02-15 | final6c_boosting | 6.73 | -8.08 | -8.08 |
| 17757 | SWPP | 2021-02-15 | final6c_ensemble | 2.81 | -3.70 | -3.70 |
| 17756 | SWPP | 2021-02-15 | final6c_recency | 4.65 | -4.82 | -4.82 |
| 17765 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17764 | SWPP | 2021-02-16 | final6c | 4.01 | -0.25 | -0.25 |
| 17760 | SWPP | 2021-02-16 | final6c_additive | 7.84 | 3.67 | 0.00 |
| 17761 | SWPP | 2021-02-16 | final6c_boosting | 3.27 | -6.32 | -6.32 |
| 17763 | SWPP | 2021-02-16 | final6c_ensemble | 3.86 | -0.88 | -0.88 |
| 17762 | SWPP | 2021-02-16 | final6c_recency | 2.40 | -0.36 | -0.36 |
| 26105 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26104 | TVA | 2022-12-23 | final6c | 8.70 | -10.74 | -10.74 |
| 26100 | TVA | 2022-12-23 | final6c_additive | 6.38 | -3.59 | -3.59 |
| 26101 | TVA | 2022-12-23 | final6c_boosting | 15.86 | -16.78 | -16.78 |
| 26103 | TVA | 2022-12-23 | final6c_ensemble | 8.99 | -10.35 | -10.35 |
| 26102 | TVA | 2022-12-23 | final6c_recency | 10.00 | -11.35 | -11.35 |
| 26111 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26110 | TVA | 2022-12-24 | final6c | 5.96 | -11.82 | -11.82 |
| 26106 | TVA | 2022-12-24 | final6c_additive | 3.91 | -9.65 | -9.65 |
| 26107 | TVA | 2022-12-24 | final6c_boosting | 7.74 | -15.18 | -15.18 |
| 26109 | TVA | 2022-12-24 | final6c_ensemble | 6.29 | -12.38 | -12.38 |
| 26108 | TVA | 2022-12-24 | final6c_recency | 7.70 | -12.53 | -12.53 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6c | DUK | mape | 0.154 | 0.878 | 746 |
| final6c | FPL | mape | -3.891 | 0.000 | 665 |
| final6c | MISO | mape | -11.771 | 0.000 | 738 |
| final6c | PJM | mape | -8.460 | 0.000 | 734 |
| final6c | SWPP | mape | -19.653 | 0.000 | 741 |
| final6c | TVA | mape | 8.418 | 0.000 | 729 |
| final6c_additive | DUK | mape | 3.930 | 0.000 | 746 |
| final6c_additive | FPL | mape | 12.713 | 0.000 | 665 |
| final6c_additive | MISO | mape | -5.696 | 0.000 | 738 |
| final6c_additive | PJM | mape | 0.245 | 0.807 | 734 |
| final6c_additive | SWPP | mape | -15.483 | 0.000 | 741 |
| final6c_additive | TVA | mape | 13.683 | 0.000 | 729 |
| final6c_boosting | DUK | mape | 2.399 | 0.016 | 746 |
| final6c_boosting | FPL | mape | 11.544 | 0.000 | 665 |
| final6c_boosting | MISO | mape | -8.075 | 0.000 | 738 |
| final6c_boosting | PJM | mape | -2.106 | 0.035 | 734 |
| final6c_boosting | SWPP | mape | -14.589 | 0.000 | 741 |
| final6c_boosting | TVA | mape | 10.526 | 0.000 | 729 |
| final6c_ensemble | DUK | mape | -0.019 | 0.984 | 746 |
| final6c_ensemble | FPL | mape | 13.018 | 0.000 | 665 |
| final6c_ensemble | MISO | mape | -8.737 | 0.000 | 738 |
| final6c_ensemble | PJM | mape | -4.921 | 0.000 | 734 |
| final6c_ensemble | SWPP | mape | -19.428 | 0.000 | 741 |
| final6c_ensemble | TVA | mape | 8.746 | 0.000 | 729 |
| final6c_recency | DUK | mape | 9.505 | 0.000 | 746 |
| final6c_recency | FPL | mape | 18.297 | 0.000 | 665 |
| final6c_recency | MISO | mape | 2.458 | 0.014 | 738 |
| final6c_recency | PJM | mape | 7.790 | 0.000 | 734 |
| final6c_recency | SWPP | mape | -11.351 | 0.000 | 741 |
| final6c_recency | TVA | mape | 16.636 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final6c | 0.983 |
| final6c_additive | 0.956 |
| final6c_boosting | 0.983 |
| final6c_ensemble | 0.983 |
| final6c_recency | 0.983 |
