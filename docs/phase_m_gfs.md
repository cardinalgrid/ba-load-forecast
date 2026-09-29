# Phase M: the GFS as a third weather model

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final7` is the phase K recipe with the temperature path taken as the mean, hour by hour, of the HRRR, the NBM and the GFS 0.25 degree run available at the cut-off (a 5 h availability lag: 06 UTC in most zones), each model where it has the hour; before 23 March 2021 the GFS archive is three-hourly and its path is interpolated. Compare with `docs/phase_k_nbm_blend.md` (`final6n`, same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final7 | 2.22 | 1.93 | -0.03 | -1.22 | 1.36 | 0.62 | 0.27 | -46.77 | 4365 | 6.00 |
| final7_ensemble | 2.54 | 2.23 | -1.84 | -2.33 | 1.32 | 0.54 | 0.18 | -49.54 | 4365 | 6.00 |
| final7_boosting | 2.57 | 2.33 | -1.49 | -2.17 | 1.55 | 0.53 | 0.20 | -49.45 | 4365 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.05 | 0.00 | 0.00 | -47.43 | 4365 | 6.00 |
| final7_additive | 2.79 | 2.44 | -2.04 | -2.60 | 1.42 | 0.49 | 0.18 | -48.51 | 4365 | 6.00 |
| final7_recency | 3.27 | 2.87 | -2.12 | -2.75 | 1.66 | 0.39 | 0.17 | -50.91 | 4365 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final7 | DUK | 2.84 | 2.53 | -0.03 | -1.55 | 1.22 | -12.64 | 0.48 | 0.32 | 747 | 12145.43 |
| final7 | FPL | 3.34 | 2.78 | -0.35 | -2.00 | 0.98 | -46.77 | 0.63 | 0.70 | 666 | 15342.04 |
| final7 | MISO | 1.98 | 1.72 | 0.08 | -0.99 | 1.55 | -7.14 | 0.65 | 0.06 | 741 | 73714.43 |
| final7 | PJM | 2.05 | 1.82 | -0.13 | -1.17 | 1.34 | -9.41 | 0.63 | 0.42 | 735 | 92099.88 |
| final7 | SWPP | 2.26 | 1.87 | -0.02 | -1.28 | 1.35 | -18.93 | 0.73 | 0.10 | 744 | 31394.87 |
| final7 | TVA | 2.61 | 2.27 | 0.24 | -1.34 | 1.14 | -11.14 | 0.37 | 0.32 | 732 | 18589.75 |
| final7_additive | DUK | 3.19 | 2.91 | -2.30 | -3.01 | 1.23 | -15.39 | 0.40 | 0.19 | 747 | 12145.43 |
| final7_additive | FPL | 4.71 | 4.21 | -4.82 | -5.34 | 1.00 | -48.51 | 0.44 | 0.34 | 666 | 15342.04 |
| final7_additive | MISO | 2.33 | 2.02 | -1.71 | -2.14 | 1.52 | -10.10 | 0.55 | 0.04 | 741 | 73714.43 |
| final7_additive | PJM | 2.74 | 2.38 | -1.76 | -2.36 | 1.46 | -13.10 | 0.44 | 0.31 | 735 | 92099.88 |
| final7_additive | SWPP | 2.53 | 2.10 | -1.71 | -2.38 | 1.36 | -21.49 | 0.68 | 0.07 | 744 | 31394.87 |
| final7_additive | TVA | 3.49 | 3.20 | -2.83 | -3.44 | 1.37 | -15.16 | 0.25 | 0.13 | 732 | 18589.75 |
| final7_boosting | DUK | 3.03 | 2.73 | -1.59 | -2.49 | 1.32 | -14.77 | 0.41 | 0.22 | 747 | 12145.43 |
| final7_boosting | FPL | 4.10 | 3.81 | -4.73 | -5.12 | 1.14 | -49.45 | 0.50 | 0.35 | 666 | 15342.04 |
| final7_boosting | MISO | 2.19 | 1.91 | -1.12 | -1.70 | 1.64 | -9.57 | 0.60 | 0.04 | 741 | 73714.43 |
| final7_boosting | PJM | 2.50 | 2.37 | -1.12 | -1.84 | 1.60 | -12.43 | 0.51 | 0.35 | 735 | 92099.88 |
| final7_boosting | SWPP | 2.51 | 2.10 | -1.70 | -2.46 | 1.56 | -29.36 | 0.69 | 0.05 | 744 | 31394.87 |
| final7_boosting | TVA | 2.98 | 2.66 | -1.78 | -2.50 | 1.37 | -12.99 | 0.29 | 0.17 | 732 | 18589.75 |
| final7_ensemble | DUK | 2.91 | 2.59 | -1.79 | -2.56 | 1.22 | -13.56 | 0.46 | 0.20 | 747 | 12145.43 |
| final7_ensemble | FPL | 4.48 | 4.08 | -5.22 | -5.56 | 1.01 | -49.54 | 0.47 | 0.31 | 666 | 15342.04 |
| final7_ensemble | MISO | 2.17 | 1.88 | -1.52 | -1.91 | 1.53 | -9.33 | 0.59 | 0.04 | 741 | 73714.43 |
| final7_ensemble | PJM | 2.46 | 2.16 | -1.56 | -2.07 | 1.27 | -11.98 | 0.53 | 0.31 | 735 | 92099.88 |
| final7_ensemble | SWPP | 2.26 | 1.87 | -1.44 | -2.09 | 1.25 | -20.09 | 0.71 | 0.06 | 744 | 31394.87 |
| final7_ensemble | TVA | 3.06 | 2.78 | -2.36 | -2.93 | 1.21 | -13.80 | 0.28 | 0.12 | 732 | 18589.75 |
| final7_recency | DUK | 3.46 | 3.16 | -1.48 | -2.67 | 1.51 | -14.71 | 0.33 | 0.21 | 747 | 12145.43 |
| final7_recency | FPL | 5.78 | 5.01 | -6.66 | -7.01 | 1.15 | -50.91 | 0.35 | 0.26 | 666 | 15342.04 |
| final7_recency | MISO | 3.00 | 2.62 | -1.92 | -2.36 | 1.95 | -15.10 | 0.41 | 0.04 | 741 | 73714.43 |
| final7_recency | PJM | 3.13 | 2.75 | -1.91 | -2.49 | 1.60 | -16.58 | 0.34 | 0.29 | 735 | 92099.88 |
| final7_recency | SWPP | 2.87 | 2.44 | -0.91 | -1.98 | 1.64 | -18.58 | 0.64 | 0.08 | 744 | 31394.87 |
| final7_recency | TVA | 3.57 | 3.21 | -2.62 | -3.35 | 1.27 | -15.30 | 0.21 | 0.13 | 732 | 18589.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final7 | DUK | uri | 4.07 | -3.32 | -3.74 | -8.88 | 6 |
| final7 | FPL | uri | 7.27 | -7.69 | -7.69 | -10.29 | 6 |
| final7 | MISO | uri | 3.86 | -3.50 | -3.55 | -7.14 | 5 |
| final7 | PJM | uri | 1.81 | 0.56 | -0.49 | -2.39 | 6 |
| final7 | SWPP | uri | 6.45 | 1.30 | -2.41 | -5.50 | 4 |
| final7 | TVA | uri | 4.16 | -1.09 | -2.33 | -6.68 | 6 |
| final7_additive | DUK | uri | 3.76 | -3.97 | -3.97 | -6.69 | 6 |
| final7_additive | FPL | uri | 9.25 | -13.56 | -13.56 | -17.35 | 6 |
| final7_additive | MISO | uri | 3.58 | -2.44 | -3.00 | -6.26 | 5 |
| final7_additive | PJM | uri | 3.14 | 2.76 | -0.37 | -2.24 | 6 |
| final7_additive | SWPP | uri | 6.21 | 2.88 | -1.24 | -3.86 | 4 |
| final7_additive | TVA | uri | 4.23 | -0.02 | -1.72 | -5.47 | 6 |
| final7_boosting | DUK | uri | 3.69 | -5.15 | -5.15 | -9.61 | 6 |
| final7_boosting | FPL | uri | 6.69 | -9.26 | -9.26 | -13.03 | 6 |
| final7_boosting | MISO | uri | 2.76 | -3.05 | -3.05 | -5.72 | 5 |
| final7_boosting | PJM | uri | 1.73 | -0.16 | -0.79 | -1.63 | 6 |
| final7_boosting | SWPP | uri | 5.50 | -2.26 | -3.85 | -9.78 | 4 |
| final7_boosting | TVA | uri | 3.44 | -1.97 | -2.01 | -6.11 | 6 |
| final7_ensemble | DUK | uri | 3.95 | -4.91 | -4.91 | -8.07 | 6 |
| final7_ensemble | FPL | uri | 8.99 | -12.42 | -12.42 | -15.93 | 6 |
| final7_ensemble | MISO | uri | 3.71 | -3.60 | -3.60 | -7.00 | 5 |
| final7_ensemble | PJM | uri | 2.26 | 1.10 | -0.44 | -2.62 | 6 |
| final7_ensemble | SWPP | uri | 6.15 | -0.35 | -3.10 | -6.85 | 4 |
| final7_ensemble | TVA | uri | 3.86 | -1.15 | -2.00 | -5.61 | 6 |
| final7_recency | DUK | uri | 4.69 | -5.67 | -5.67 | -8.14 | 6 |
| final7_recency | FPL | uri | 11.44 | -14.91 | -14.91 | -18.07 | 6 |
| final7_recency | MISO | uri | 6.41 | -5.81 | -5.81 | -9.51 | 5 |
| final7_recency | PJM | uri | 2.54 | 0.91 | -0.74 | -4.31 | 6 |
| final7_recency | SWPP | uri | 6.75 | -2.20 | -4.48 | -10.45 | 4 |
| final7_recency | TVA | uri | 4.54 | -1.47 | -2.53 | -5.88 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final7 | DUK | elliott | 3.16 | -2.50 | -2.50 | -6.10 | 4 |
| final7 | FPL | elliott | 5.54 | -6.10 | -6.10 | -9.67 | 5 |
| final7 | MISO | elliott | 3.63 | -2.69 | -3.39 | -6.44 | 5 |
| final7 | PJM | elliott | 4.30 | -4.56 | -4.56 | -8.71 | 5 |
| final7 | SWPP | elliott | 4.17 | -0.87 | -2.57 | -8.36 | 5 |
| final7 | TVA | elliott | 4.11 | 1.72 | 0.00 | 0.00 | 3 |
| final7_additive | DUK | elliott | 4.22 | -5.19 | -5.19 | -7.67 | 4 |
| final7_additive | FPL | elliott | 6.92 | -3.95 | -4.92 | -11.50 | 5 |
| final7_additive | MISO | elliott | 3.49 | -3.82 | -4.02 | -6.45 | 5 |
| final7_additive | PJM | elliott | 3.30 | -2.45 | -2.45 | -7.24 | 5 |
| final7_additive | SWPP | elliott | 3.48 | -2.75 | -2.99 | -6.48 | 5 |
| final7_additive | TVA | elliott | 5.00 | 0.25 | -1.11 | -2.28 | 3 |
| final7_boosting | DUK | elliott | 4.09 | -3.97 | -3.97 | -6.28 | 4 |
| final7_boosting | FPL | elliott | 9.06 | -14.39 | -14.39 | -20.17 | 5 |
| final7_boosting | MISO | elliott | 3.49 | -2.18 | -3.21 | -4.39 | 5 |
| final7_boosting | PJM | elliott | 3.83 | -4.31 | -4.31 | -7.50 | 5 |
| final7_boosting | SWPP | elliott | 4.65 | -3.78 | -4.60 | -13.41 | 5 |
| final7_boosting | TVA | elliott | 4.29 | -0.97 | -1.25 | -3.01 | 3 |
| final7_ensemble | DUK | elliott | 3.84 | -5.48 | -5.48 | -6.97 | 4 |
| final7_ensemble | FPL | elliott | 7.50 | -10.19 | -10.19 | -13.83 | 5 |
| final7_ensemble | MISO | elliott | 3.72 | -4.07 | -4.33 | -7.49 | 5 |
| final7_ensemble | PJM | elliott | 4.06 | -4.83 | -4.83 | -9.83 | 5 |
| final7_ensemble | SWPP | elliott | 4.09 | -4.42 | -4.67 | -10.97 | 5 |
| final7_ensemble | TVA | elliott | 4.29 | -1.04 | -1.97 | -3.01 | 3 |
| final7_recency | DUK | elliott | 4.50 | -7.55 | -7.55 | -11.30 | 4 |
| final7_recency | FPL | elliott | 9.93 | -12.16 | -12.16 | -17.52 | 5 |
| final7_recency | MISO | elliott | 6.71 | -7.65 | -7.65 | -15.10 | 5 |
| final7_recency | PJM | elliott | 5.94 | -8.02 | -8.02 | -16.58 | 5 |
| final7_recency | SWPP | elliott | 5.01 | -7.27 | -7.27 | -13.61 | 5 |
| final7_recency | TVA | elliott | 4.13 | -2.56 | -3.64 | -5.73 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final7_ensemble | eve | 3.27 | -1.51 | -2.60 | 0.61 | 142 |
| 7 | final7 | eve | 3.37 | 0.69 | -1.46 | 0.59 | 142 |
| 9 | final7_boosting | eve | 3.47 | -1.17 | -2.47 | 0.56 | 142 |
| 8 | final7_additive | eve | 3.48 | -1.27 | -2.58 | 0.54 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final7_recency | eve | 4.02 | -2.35 | -3.41 | 0.49 | 142 |
| 1 | final7 | special | 3.23 | -0.48 | -1.84 | 0.65 | 144 |
| 4 | final7_ensemble | special | 3.34 | -2.71 | -3.29 | 0.63 | 144 |
| 2 | final7_additive | special | 3.44 | -2.99 | -3.52 | 0.59 | 144 |
| 3 | final7_boosting | special | 3.65 | -2.52 | -3.23 | 0.54 | 144 |
| 5 | final7_recency | special | 4.11 | -2.79 | -3.74 | 0.54 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final7 | all | 0.386 | 1.251 | 0.363 | 0.887 | 10.951 | 0.886 | 14.978 | 1.625 | 4240 |
| final7 | events | 0.513 | 2.185 | 0.796 | 0.699 | 12.176 | 0.667 | 26.197 | 2.877 | 60 |
| final7 | cold_mornings | 0.472 | 1.627 | 0.551 | 0.813 | 12.328 | 0.783 | 20.447 | 2.152 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final7 | 10.16 | -10.52 | -10.52 |
| 4440 | DUK | 2022-12-24 | final7_additive | 9.53 | -12.94 | -12.94 |
| 4441 | DUK | 2022-12-24 | final7_boosting | 11.04 | -17.22 | -17.22 |
| 4443 | DUK | 2022-12-24 | final7_ensemble | 10.48 | -14.29 | -14.29 |
| 4442 | DUK | 2022-12-24 | final7_recency | 11.05 | -12.51 | -12.51 |
| 8939 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8938 | MISO | 2021-02-16 | final7 | 1.68 | 1.31 | 0.00 |
| 8934 | MISO | 2021-02-16 | final7_additive | 2.35 | 2.12 | 0.00 |
| 8935 | MISO | 2021-02-16 | final7_boosting | 1.73 | 1.02 | 0.00 |
| 8937 | MISO | 2021-02-16 | final7_ensemble | 1.68 | 0.55 | 0.00 |
| 8936 | MISO | 2021-02-16 | final7_recency | 3.66 | -2.23 | -2.23 |
| 17795 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17794 | SWPP | 2021-02-15 | final7 | 2.40 | -2.00 | -2.00 |
| 17790 | SWPP | 2021-02-15 | final7_additive | 2.76 | 1.36 | 0.00 |
| 17791 | SWPP | 2021-02-15 | final7_boosting | 6.58 | -8.08 | -8.08 |
| 17793 | SWPP | 2021-02-15 | final7_ensemble | 2.77 | -3.66 | -3.66 |
| 17792 | SWPP | 2021-02-15 | final7_recency | 4.73 | -4.95 | -4.95 |
| 17801 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17800 | SWPP | 2021-02-16 | final7 | 4.24 | 0.49 | 0.00 |
| 17796 | SWPP | 2021-02-16 | final7_additive | 7.82 | 3.65 | 0.00 |
| 17797 | SWPP | 2021-02-16 | final7_boosting | 3.24 | -6.32 | -6.32 |
| 17799 | SWPP | 2021-02-16 | final7_ensemble | 3.84 | -0.79 | -0.79 |
| 17798 | SWPP | 2021-02-16 | final7_recency | 2.34 | -0.38 | -0.38 |
| 26177 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26176 | TVA | 2022-12-23 | final7 | 9.19 | -11.92 | -11.92 |
| 26172 | TVA | 2022-12-23 | final7_additive | 6.72 | -4.40 | -4.40 |
| 26173 | TVA | 2022-12-23 | final7_boosting | 14.67 | -15.48 | -15.48 |
| 26175 | TVA | 2022-12-23 | final7_ensemble | 9.31 | -10.80 | -10.80 |
| 26174 | TVA | 2022-12-23 | final7_recency | 11.00 | -13.23 | -13.23 |
| 26183 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26182 | TVA | 2022-12-24 | final7 | 6.24 | -14.28 | -14.28 |
| 26178 | TVA | 2022-12-24 | final7_additive | 3.87 | -9.81 | -9.81 |
| 26179 | TVA | 2022-12-24 | final7_boosting | 7.17 | -15.18 | -15.18 |
| 26181 | TVA | 2022-12-24 | final7_ensemble | 6.07 | -12.56 | -12.56 |
| 26180 | TVA | 2022-12-24 | final7_recency | 7.77 | -12.88 | -12.88 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final7 | DUK | mape | 0.125 | 0.900 | 747 |
| final7 | FPL | mape | -6.261 | 0.000 | 666 |
| final7 | MISO | mape | -11.346 | 0.000 | 741 |
| final7 | PJM | mape | -8.071 | 0.000 | 735 |
| final7 | SWPP | mape | -17.739 | 0.000 | 744 |
| final7 | TVA | mape | 8.134 | 0.000 | 732 |
| final7_additive | DUK | mape | 5.531 | 0.000 | 747 |
| final7_additive | FPL | mape | 7.995 | 0.000 | 666 |
| final7_additive | MISO | mape | -4.460 | 0.000 | 741 |
| final7_additive | PJM | mape | 4.898 | 0.000 | 735 |
| final7_additive | SWPP | mape | -13.239 | 0.000 | 744 |
| final7_additive | TVA | mape | 18.679 | 0.000 | 732 |
| final7_boosting | DUK | mape | 3.146 | 0.002 | 747 |
| final7_boosting | FPL | mape | 2.680 | 0.007 | 666 |
| final7_boosting | MISO | mape | -6.930 | 0.000 | 741 |
| final7_boosting | PJM | mape | 0.772 | 0.440 | 735 |
| final7_boosting | SWPP | mape | -13.123 | 0.000 | 744 |
| final7_boosting | TVA | mape | 13.732 | 0.000 | 732 |
| final7_ensemble | DUK | mape | 1.182 | 0.237 | 747 |
| final7_ensemble | FPL | mape | 6.301 | 0.000 | 666 |
| final7_ensemble | MISO | mape | -6.900 | 0.000 | 741 |
| final7_ensemble | PJM | mape | 0.063 | 0.950 | 735 |
| final7_ensemble | SWPP | mape | -16.841 | 0.000 | 744 |
| final7_ensemble | TVA | mape | 14.450 | 0.000 | 732 |
| final7_recency | DUK | mape | 9.991 | 0.000 | 747 |
| final7_recency | FPL | mape | 14.262 | 0.000 | 666 |
| final7_recency | MISO | mape | 4.260 | 0.000 | 741 |
| final7_recency | PJM | mape | 11.343 | 0.000 | 735 |
| final7_recency | SWPP | mape | -9.622 | 0.000 | 744 |
| final7_recency | TVA | mape | 19.841 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final7 | 0.986 |
| final7_additive | 0.959 |
| final7_boosting | 0.986 |
| final7_ensemble | 0.986 |
| final7_recency | 0.986 |
