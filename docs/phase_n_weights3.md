# Phase N: the weather models weighted per station by their recent error

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final8` is `final7` (HRRR, NBM and GFS in the temperature mean) with the weights of the three models set per station and per day as the inverse of each model's mean squared error at that station's observations over the last 30 days known at the cut-off (equal weights with fewer than 240 common hours). Compare with `docs/phase_k_nbm_blend.md` (`final6n`) and `docs/phase_m_gfs.md` (`final7`), same days.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8 | 2.19 | 1.90 | -0.06 | -1.21 | 1.31 | 0.63 | 0.28 | -46.62 | 4365 | 6.00 |
| final8_ensemble | 2.44 | 2.15 | -1.78 | -2.27 | 1.31 | 0.57 | 0.18 | -49.11 | 4365 | 6.00 |
| final8_boosting | 2.48 | 2.22 | -1.46 | -2.13 | 1.51 | 0.56 | 0.19 | -48.89 | 4365 | 6.00 |
| final8_additive | 2.70 | 2.37 | -1.99 | -2.54 | 1.41 | 0.51 | 0.18 | -48.25 | 4365 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.05 | 0.00 | 0.00 | -47.43 | 4365 | 6.00 |
| final8_recency | 3.17 | 2.79 | -2.01 | -2.65 | 1.63 | 0.41 | 0.17 | -50.47 | 4365 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final8 | DUK | 2.80 | 2.49 | 0.02 | -1.50 | 1.16 | -12.80 | 0.50 | 0.32 | 747 | 12145.43 |
| final8 | FPL | 3.36 | 2.80 | -0.22 | -1.93 | 0.97 | -46.62 | 0.63 | 0.70 | 666 | 15342.04 |
| final8 | MISO | 1.96 | 1.71 | 0.08 | -0.98 | 1.51 | -7.14 | 0.65 | 0.06 | 741 | 73714.43 |
| final8 | PJM | 2.01 | 1.77 | -0.21 | -1.19 | 1.25 | -9.67 | 0.65 | 0.42 | 735 | 92099.88 |
| final8 | SWPP | 2.22 | 1.82 | -0.07 | -1.27 | 1.29 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final8 | TVA | 2.58 | 2.25 | 0.26 | -1.33 | 1.17 | -11.14 | 0.39 | 0.32 | 732 | 18589.75 |
| final8_additive | DUK | 3.14 | 2.84 | -2.34 | -3.03 | 1.20 | -15.60 | 0.42 | 0.19 | 747 | 12145.43 |
| final8_additive | FPL | 4.61 | 4.08 | -4.73 | -5.26 | 1.00 | -48.25 | 0.45 | 0.35 | 666 | 15342.04 |
| final8_additive | MISO | 2.30 | 2.00 | -1.70 | -2.12 | 1.52 | -10.13 | 0.56 | 0.04 | 741 | 73714.43 |
| final8_additive | PJM | 2.60 | 2.29 | -1.68 | -2.26 | 1.44 | -12.60 | 0.48 | 0.30 | 735 | 92099.88 |
| final8_additive | SWPP | 2.48 | 2.07 | -1.72 | -2.37 | 1.35 | -21.65 | 0.69 | 0.07 | 744 | 31394.87 |
| final8_additive | TVA | 3.27 | 3.06 | -2.65 | -3.27 | 1.38 | -14.44 | 0.27 | 0.12 | 732 | 18589.75 |
| final8_boosting | DUK | 2.97 | 2.67 | -1.65 | -2.50 | 1.30 | -14.77 | 0.43 | 0.22 | 747 | 12145.43 |
| final8_boosting | FPL | 3.93 | 3.61 | -4.56 | -4.98 | 1.12 | -48.89 | 0.52 | 0.36 | 666 | 15342.04 |
| final8_boosting | MISO | 2.16 | 1.87 | -1.10 | -1.69 | 1.62 | -9.57 | 0.60 | 0.04 | 741 | 73714.43 |
| final8_boosting | PJM | 2.37 | 2.19 | -1.10 | -1.80 | 1.54 | -12.20 | 0.54 | 0.34 | 735 | 92099.88 |
| final8_boosting | SWPP | 2.47 | 2.06 | -1.71 | -2.44 | 1.56 | -29.38 | 0.69 | 0.06 | 744 | 31394.87 |
| final8_boosting | TVA | 2.80 | 2.50 | -1.59 | -2.33 | 1.36 | -12.55 | 0.33 | 0.18 | 732 | 18589.75 |
| final8_ensemble | DUK | 2.85 | 2.55 | -1.84 | -2.57 | 1.22 | -13.67 | 0.46 | 0.19 | 747 | 12145.43 |
| final8_ensemble | FPL | 4.31 | 3.90 | -5.07 | -5.43 | 0.98 | -49.11 | 0.51 | 0.33 | 666 | 15342.04 |
| final8_ensemble | MISO | 2.14 | 1.86 | -1.50 | -1.89 | 1.50 | -9.36 | 0.59 | 0.03 | 741 | 73714.43 |
| final8_ensemble | PJM | 2.32 | 2.06 | -1.48 | -1.98 | 1.27 | -11.61 | 0.57 | 0.32 | 735 | 92099.88 |
| final8_ensemble | SWPP | 2.21 | 1.81 | -1.44 | -2.06 | 1.24 | -20.14 | 0.72 | 0.06 | 744 | 31394.87 |
| final8_ensemble | TVA | 2.84 | 2.54 | -2.14 | -2.73 | 1.18 | -12.60 | 0.31 | 0.12 | 732 | 18589.75 |
| final8_recency | DUK | 3.41 | 3.12 | -1.52 | -2.67 | 1.53 | -14.88 | 0.35 | 0.21 | 747 | 12145.43 |
| final8_recency | FPL | 5.60 | 4.84 | -6.48 | -6.86 | 1.14 | -50.47 | 0.37 | 0.27 | 666 | 15342.04 |
| final8_recency | MISO | 2.96 | 2.60 | -1.89 | -2.33 | 1.92 | -15.06 | 0.42 | 0.04 | 741 | 73714.43 |
| final8_recency | PJM | 2.99 | 2.64 | -1.74 | -2.35 | 1.59 | -16.13 | 0.37 | 0.29 | 735 | 92099.88 |
| final8_recency | SWPP | 2.82 | 2.40 | -0.89 | -1.93 | 1.63 | -18.61 | 0.64 | 0.08 | 744 | 31394.87 |
| final8_recency | TVA | 3.35 | 2.99 | -2.34 | -3.12 | 1.24 | -15.37 | 0.22 | 0.14 | 732 | 18589.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final8 | DUK | uri | 4.07 | -3.32 | -3.74 | -8.88 | 6 |
| final8 | FPL | uri | 7.27 | -7.69 | -7.69 | -10.29 | 6 |
| final8 | MISO | uri | 3.86 | -3.50 | -3.55 | -7.14 | 5 |
| final8 | PJM | uri | 1.81 | 0.56 | -0.49 | -2.39 | 6 |
| final8 | SWPP | uri | 6.45 | 1.30 | -2.41 | -5.50 | 4 |
| final8 | TVA | uri | 4.16 | -1.09 | -2.33 | -6.68 | 6 |
| final8_additive | DUK | uri | 3.76 | -3.97 | -3.97 | -6.69 | 6 |
| final8_additive | FPL | uri | 9.25 | -13.56 | -13.56 | -17.35 | 6 |
| final8_additive | MISO | uri | 3.58 | -2.44 | -3.00 | -6.26 | 5 |
| final8_additive | PJM | uri | 3.14 | 2.76 | -0.37 | -2.24 | 6 |
| final8_additive | SWPP | uri | 6.21 | 2.88 | -1.24 | -3.86 | 4 |
| final8_additive | TVA | uri | 4.23 | -0.02 | -1.72 | -5.47 | 6 |
| final8_boosting | DUK | uri | 3.69 | -5.15 | -5.15 | -9.61 | 6 |
| final8_boosting | FPL | uri | 6.69 | -9.26 | -9.26 | -13.03 | 6 |
| final8_boosting | MISO | uri | 2.76 | -3.05 | -3.05 | -5.72 | 5 |
| final8_boosting | PJM | uri | 1.73 | -0.16 | -0.79 | -1.63 | 6 |
| final8_boosting | SWPP | uri | 5.50 | -2.26 | -3.85 | -9.78 | 4 |
| final8_boosting | TVA | uri | 3.44 | -1.97 | -2.01 | -6.11 | 6 |
| final8_ensemble | DUK | uri | 3.95 | -4.91 | -4.91 | -8.07 | 6 |
| final8_ensemble | FPL | uri | 8.99 | -12.42 | -12.42 | -15.93 | 6 |
| final8_ensemble | MISO | uri | 3.71 | -3.60 | -3.60 | -7.00 | 5 |
| final8_ensemble | PJM | uri | 2.26 | 1.10 | -0.44 | -2.62 | 6 |
| final8_ensemble | SWPP | uri | 6.15 | -0.35 | -3.10 | -6.85 | 4 |
| final8_ensemble | TVA | uri | 3.86 | -1.15 | -2.00 | -5.61 | 6 |
| final8_recency | DUK | uri | 4.69 | -5.67 | -5.67 | -8.14 | 6 |
| final8_recency | FPL | uri | 11.44 | -14.91 | -14.91 | -18.07 | 6 |
| final8_recency | MISO | uri | 6.41 | -5.81 | -5.81 | -9.51 | 5 |
| final8_recency | PJM | uri | 2.54 | 0.91 | -0.74 | -4.31 | 6 |
| final8_recency | SWPP | uri | 6.75 | -2.20 | -4.48 | -10.45 | 4 |
| final8_recency | TVA | uri | 4.54 | -1.47 | -2.53 | -5.88 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final8 | DUK | elliott | 3.18 | -2.74 | -2.74 | -6.05 | 4 |
| final8 | FPL | elliott | 5.66 | -6.22 | -6.22 | -9.76 | 5 |
| final8 | MISO | elliott | 3.64 | -2.83 | -3.44 | -6.36 | 5 |
| final8 | PJM | elliott | 4.32 | -4.38 | -4.38 | -8.73 | 5 |
| final8 | SWPP | elliott | 4.18 | -0.94 | -2.55 | -8.36 | 5 |
| final8 | TVA | elliott | 4.00 | 0.89 | 0.00 | 0.00 | 3 |
| final8_additive | DUK | elliott | 4.13 | -5.27 | -5.27 | -7.74 | 4 |
| final8_additive | FPL | elliott | 6.78 | -3.95 | -4.79 | -11.21 | 5 |
| final8_additive | MISO | elliott | 3.50 | -3.88 | -4.08 | -6.52 | 5 |
| final8_additive | PJM | elliott | 3.38 | -2.83 | -2.83 | -7.54 | 5 |
| final8_additive | SWPP | elliott | 3.48 | -2.76 | -3.00 | -6.40 | 5 |
| final8_additive | TVA | elliott | 4.80 | -0.55 | -1.17 | -2.28 | 3 |
| final8_boosting | DUK | elliott | 3.98 | -4.02 | -4.02 | -6.28 | 4 |
| final8_boosting | FPL | elliott | 8.92 | -14.07 | -14.07 | -20.17 | 5 |
| final8_boosting | MISO | elliott | 3.52 | -2.24 | -3.26 | -4.39 | 5 |
| final8_boosting | PJM | elliott | 3.92 | -4.63 | -4.63 | -7.59 | 5 |
| final8_boosting | SWPP | elliott | 4.70 | -3.67 | -4.45 | -13.41 | 5 |
| final8_boosting | TVA | elliott | 4.24 | -2.10 | -2.10 | -3.43 | 3 |
| final8_ensemble | DUK | elliott | 3.79 | -5.55 | -5.55 | -6.99 | 4 |
| final8_ensemble | FPL | elliott | 7.42 | -10.08 | -10.08 | -13.94 | 5 |
| final8_ensemble | MISO | elliott | 3.74 | -4.11 | -4.37 | -7.54 | 5 |
| final8_ensemble | PJM | elliott | 4.12 | -5.07 | -5.07 | -9.89 | 5 |
| final8_ensemble | SWPP | elliott | 4.09 | -4.37 | -4.61 | -10.91 | 5 |
| final8_ensemble | TVA | elliott | 4.15 | -2.05 | -2.05 | -3.24 | 3 |
| final8_recency | DUK | elliott | 4.47 | -7.67 | -7.67 | -11.20 | 4 |
| final8_recency | FPL | elliott | 9.94 | -12.10 | -12.10 | -17.32 | 5 |
| final8_recency | MISO | elliott | 6.71 | -7.65 | -7.65 | -15.06 | 5 |
| final8_recency | PJM | elliott | 5.93 | -8.00 | -8.00 | -16.13 | 5 |
| final8_recency | SWPP | elliott | 4.96 | -7.19 | -7.19 | -13.47 | 5 |
| final8_recency | TVA | elliott | 3.97 | -3.67 | -3.68 | -5.71 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final8_ensemble | eve | 3.22 | -1.41 | -2.51 | 0.62 | 142 |
| 7 | final8 | eve | 3.36 | 0.74 | -1.46 | 0.58 | 142 |
| 8 | final8_additive | eve | 3.41 | -1.20 | -2.51 | 0.58 | 142 |
| 9 | final8_boosting | eve | 3.42 | -1.07 | -2.37 | 0.58 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final8_recency | eve | 3.98 | -2.24 | -3.32 | 0.49 | 142 |
| 1 | final8 | special | 3.22 | -0.44 | -1.80 | 0.64 | 144 |
| 4 | final8_ensemble | special | 3.28 | -2.66 | -3.24 | 0.64 | 144 |
| 2 | final8_additive | special | 3.37 | -2.93 | -3.45 | 0.62 | 144 |
| 3 | final8_boosting | special | 3.58 | -2.50 | -3.22 | 0.57 | 144 |
| 5 | final8_recency | special | 4.06 | -2.71 | -3.67 | 0.56 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8 | all | 0.385 | 1.237 | 0.356 | 0.887 | 10.794 | 0.888 | 14.820 | 1.606 | 4239 |
| final8 | events | 0.511 | 2.189 | 0.795 | 0.699 | 12.178 | 0.667 | 26.130 | 2.881 | 60 |
| final8 | cold_mornings | 0.470 | 1.624 | 0.549 | 0.815 | 12.317 | 0.811 | 20.383 | 2.150 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final8 | 10.28 | -11.42 | -11.42 |
| 4440 | DUK | 2022-12-24 | final8_additive | 9.79 | -13.19 | -13.19 |
| 4441 | DUK | 2022-12-24 | final8_boosting | 11.07 | -17.18 | -17.18 |
| 4443 | DUK | 2022-12-24 | final8_ensemble | 10.64 | -14.41 | -14.41 |
| 4442 | DUK | 2022-12-24 | final8_recency | 11.22 | -12.64 | -12.64 |
| 8939 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8938 | MISO | 2021-02-16 | final8 | 1.68 | 1.31 | 0.00 |
| 8934 | MISO | 2021-02-16 | final8_additive | 2.35 | 2.12 | 0.00 |
| 8935 | MISO | 2021-02-16 | final8_boosting | 1.73 | 1.02 | 0.00 |
| 8937 | MISO | 2021-02-16 | final8_ensemble | 1.68 | 0.55 | 0.00 |
| 8936 | MISO | 2021-02-16 | final8_recency | 3.66 | -2.23 | -2.23 |
| 17795 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17794 | SWPP | 2021-02-15 | final8 | 2.40 | -2.00 | -2.00 |
| 17790 | SWPP | 2021-02-15 | final8_additive | 2.76 | 1.36 | 0.00 |
| 17791 | SWPP | 2021-02-15 | final8_boosting | 6.58 | -8.08 | -8.08 |
| 17793 | SWPP | 2021-02-15 | final8_ensemble | 2.77 | -3.66 | -3.66 |
| 17792 | SWPP | 2021-02-15 | final8_recency | 4.73 | -4.95 | -4.95 |
| 17801 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17800 | SWPP | 2021-02-16 | final8 | 4.24 | 0.49 | 0.00 |
| 17796 | SWPP | 2021-02-16 | final8_additive | 7.82 | 3.65 | 0.00 |
| 17797 | SWPP | 2021-02-16 | final8_boosting | 3.24 | -6.32 | -6.32 |
| 17799 | SWPP | 2021-02-16 | final8_ensemble | 3.84 | -0.79 | -0.79 |
| 17798 | SWPP | 2021-02-16 | final8_recency | 2.34 | -0.38 | -0.38 |
| 26177 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26176 | TVA | 2022-12-23 | final8 | 9.37 | -11.78 | -11.78 |
| 26172 | TVA | 2022-12-23 | final8_additive | 6.50 | -5.09 | -5.09 |
| 26173 | TVA | 2022-12-23 | final8_boosting | 14.68 | -15.39 | -15.39 |
| 26175 | TVA | 2022-12-23 | final8_ensemble | 9.48 | -11.07 | -11.07 |
| 26174 | TVA | 2022-12-23 | final8_recency | 10.55 | -13.43 | -13.43 |
| 26183 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26182 | TVA | 2022-12-24 | final8 | 6.23 | -14.29 | -14.29 |
| 26178 | TVA | 2022-12-24 | final8_additive | 4.09 | -10.30 | -10.30 |
| 26179 | TVA | 2022-12-24 | final8_boosting | 7.23 | -15.24 | -15.24 |
| 26181 | TVA | 2022-12-24 | final8_ensemble | 6.23 | -12.80 | -12.80 |
| 26180 | TVA | 2022-12-24 | final8_recency | 7.95 | -13.05 | -13.05 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final8 | DUK | mape | -0.607 | 0.544 | 747 |
| final8 | FPL | mape | -5.936 | 0.000 | 666 |
| final8 | MISO | mape | -11.695 | 0.000 | 741 |
| final8 | PJM | mape | -9.011 | 0.000 | 735 |
| final8 | SWPP | mape | -18.334 | 0.000 | 744 |
| final8 | TVA | mape | 7.557 | 0.000 | 732 |
| final8_additive | DUK | mape | 4.842 | 0.000 | 747 |
| final8_additive | FPL | mape | 7.070 | 0.000 | 666 |
| final8_additive | MISO | mape | -4.871 | 0.000 | 741 |
| final8_additive | PJM | mape | 2.457 | 0.014 | 735 |
| final8_additive | SWPP | mape | -13.861 | 0.000 | 744 |
| final8_additive | TVA | mape | 16.825 | 0.000 | 732 |
| final8_boosting | DUK | mape | 2.180 | 0.029 | 747 |
| final8_boosting | FPL | mape | 0.552 | 0.581 | 666 |
| final8_boosting | MISO | mape | -7.400 | 0.000 | 741 |
| final8_boosting | PJM | mape | -1.714 | 0.086 | 735 |
| final8_boosting | SWPP | mape | -13.639 | 0.000 | 744 |
| final8_boosting | TVA | mape | 11.479 | 0.000 | 732 |
| final8_ensemble | DUK | mape | 0.251 | 0.802 | 747 |
| final8_ensemble | FPL | mape | 4.700 | 0.000 | 666 |
| final8_ensemble | MISO | mape | -7.443 | 0.000 | 741 |
| final8_ensemble | PJM | mape | -2.779 | 0.005 | 735 |
| final8_ensemble | SWPP | mape | -17.614 | 0.000 | 744 |
| final8_ensemble | TVA | mape | 11.715 | 0.000 | 732 |
| final8_recency | DUK | mape | 9.176 | 0.000 | 747 |
| final8_recency | FPL | mape | 13.107 | 0.000 | 666 |
| final8_recency | MISO | mape | 3.790 | 0.000 | 741 |
| final8_recency | PJM | mape | 9.411 | 0.000 | 735 |
| final8_recency | SWPP | mape | -10.364 | 0.000 | 744 |
| final8_recency | TVA | mape | 18.031 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final8 | 0.986 |
| final8_additive | 0.959 |
| final8_boosting | 0.986 |
| final8_ensemble | 0.986 |
| final8_recency | 0.986 |
