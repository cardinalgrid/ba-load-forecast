# Phase N: station weights, with cold-day weights from the cold hours

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final8c` is `final8` (HRRR, NBM and GFS weighted per station by their 30-day error) except on days whose temperature path dips below 25 F: there the weights come from each model's error on the observed hours below 25 F over the last 365 days known at the cut-off (at least 48 such hours, else the 30-day weights). Compare with `docs/phase_n_weights3.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8c | 2.19 | 1.89 | -0.06 | -1.21 | 1.31 | 0.64 | 0.28 | -46.62 | 4365 | 6.00 |
| final8c_ensemble | 2.44 | 2.14 | -1.78 | -2.27 | 1.30 | 0.57 | 0.18 | -49.11 | 4365 | 6.00 |
| final8c_boosting | 2.48 | 2.22 | -1.47 | -2.13 | 1.52 | 0.56 | 0.20 | -48.89 | 4365 | 6.00 |
| final8c_additive | 2.70 | 2.37 | -1.99 | -2.54 | 1.41 | 0.51 | 0.18 | -48.25 | 4365 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.05 | 0.00 | 0.00 | -47.43 | 4365 | 6.00 |
| final8c_recency | 3.17 | 2.79 | -2.01 | -2.65 | 1.64 | 0.41 | 0.17 | -50.47 | 4365 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final8c | DUK | 2.80 | 2.49 | 0.02 | -1.50 | 1.16 | -12.80 | 0.50 | 0.32 | 747 | 12145.43 |
| final8c | FPL | 3.36 | 2.80 | -0.22 | -1.93 | 0.97 | -46.62 | 0.63 | 0.70 | 666 | 15342.04 |
| final8c | MISO | 1.96 | 1.70 | 0.08 | -0.99 | 1.50 | -6.96 | 0.65 | 0.06 | 741 | 73714.43 |
| final8c | PJM | 2.01 | 1.77 | -0.21 | -1.19 | 1.27 | -9.60 | 0.65 | 0.42 | 735 | 92099.88 |
| final8c | SWPP | 2.22 | 1.82 | -0.07 | -1.28 | 1.31 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final8c | TVA | 2.57 | 2.24 | 0.26 | -1.33 | 1.17 | -11.14 | 0.39 | 0.32 | 732 | 18589.75 |
| final8c_additive | DUK | 3.14 | 2.84 | -2.34 | -3.03 | 1.20 | -15.60 | 0.42 | 0.19 | 747 | 12145.43 |
| final8c_additive | FPL | 4.61 | 4.08 | -4.73 | -5.26 | 1.00 | -48.25 | 0.45 | 0.35 | 666 | 15342.04 |
| final8c_additive | MISO | 2.30 | 1.99 | -1.71 | -2.13 | 1.54 | -10.13 | 0.56 | 0.04 | 741 | 73714.43 |
| final8c_additive | PJM | 2.59 | 2.29 | -1.68 | -2.26 | 1.43 | -12.60 | 0.48 | 0.30 | 735 | 92099.88 |
| final8c_additive | SWPP | 2.48 | 2.07 | -1.72 | -2.36 | 1.35 | -21.65 | 0.69 | 0.07 | 744 | 31394.87 |
| final8c_additive | TVA | 3.27 | 3.06 | -2.65 | -3.27 | 1.38 | -14.44 | 0.27 | 0.12 | 732 | 18589.75 |
| final8c_boosting | DUK | 2.97 | 2.67 | -1.65 | -2.50 | 1.30 | -14.77 | 0.43 | 0.22 | 747 | 12145.43 |
| final8c_boosting | FPL | 3.93 | 3.61 | -4.56 | -4.98 | 1.12 | -48.89 | 0.52 | 0.36 | 666 | 15342.04 |
| final8c_boosting | MISO | 2.16 | 1.87 | -1.11 | -1.70 | 1.64 | -9.57 | 0.61 | 0.04 | 741 | 73714.43 |
| final8c_boosting | PJM | 2.37 | 2.19 | -1.11 | -1.80 | 1.54 | -12.20 | 0.55 | 0.34 | 735 | 92099.88 |
| final8c_boosting | SWPP | 2.47 | 2.06 | -1.71 | -2.44 | 1.56 | -29.38 | 0.69 | 0.06 | 744 | 31394.87 |
| final8c_boosting | TVA | 2.80 | 2.50 | -1.59 | -2.33 | 1.36 | -12.55 | 0.32 | 0.18 | 732 | 18589.75 |
| final8c_ensemble | DUK | 2.85 | 2.52 | -1.84 | -2.57 | 1.23 | -13.67 | 0.46 | 0.19 | 747 | 12145.43 |
| final8c_ensemble | FPL | 4.31 | 3.90 | -5.07 | -5.43 | 0.98 | -49.11 | 0.51 | 0.33 | 666 | 15342.04 |
| final8c_ensemble | MISO | 2.13 | 1.87 | -1.51 | -1.89 | 1.48 | -9.36 | 0.60 | 0.03 | 741 | 73714.43 |
| final8c_ensemble | PJM | 2.32 | 2.05 | -1.49 | -1.98 | 1.26 | -11.61 | 0.57 | 0.32 | 735 | 92099.88 |
| final8c_ensemble | SWPP | 2.21 | 1.81 | -1.44 | -2.05 | 1.25 | -20.14 | 0.72 | 0.06 | 744 | 31394.87 |
| final8c_ensemble | TVA | 2.84 | 2.54 | -2.15 | -2.74 | 1.18 | -12.60 | 0.31 | 0.12 | 732 | 18589.75 |
| final8c_recency | DUK | 3.41 | 3.12 | -1.52 | -2.67 | 1.53 | -14.88 | 0.35 | 0.21 | 747 | 12145.43 |
| final8c_recency | FPL | 5.60 | 4.84 | -6.48 | -6.86 | 1.14 | -50.47 | 0.37 | 0.27 | 666 | 15342.04 |
| final8c_recency | MISO | 2.96 | 2.60 | -1.89 | -2.33 | 1.94 | -15.03 | 0.42 | 0.04 | 741 | 73714.43 |
| final8c_recency | PJM | 2.99 | 2.64 | -1.75 | -2.35 | 1.59 | -16.00 | 0.37 | 0.29 | 735 | 92099.88 |
| final8c_recency | SWPP | 2.81 | 2.40 | -0.88 | -1.93 | 1.63 | -18.61 | 0.64 | 0.08 | 744 | 31394.87 |
| final8c_recency | TVA | 3.35 | 3.01 | -2.35 | -3.12 | 1.24 | -15.37 | 0.22 | 0.14 | 732 | 18589.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final8c | DUK | uri | 4.07 | -3.32 | -3.74 | -8.88 | 6 |
| final8c | FPL | uri | 7.27 | -7.69 | -7.69 | -10.29 | 6 |
| final8c | MISO | uri | 3.89 | -3.42 | -3.50 | -6.96 | 5 |
| final8c | PJM | uri | 1.76 | 0.40 | -0.52 | -2.40 | 6 |
| final8c | SWPP | uri | 6.50 | 1.35 | -2.40 | -5.44 | 4 |
| final8c | TVA | uri | 4.16 | -1.09 | -2.33 | -6.68 | 6 |
| final8c_additive | DUK | uri | 3.76 | -3.97 | -3.97 | -6.69 | 6 |
| final8c_additive | FPL | uri | 9.25 | -13.56 | -13.56 | -17.35 | 6 |
| final8c_additive | MISO | uri | 3.65 | -2.67 | -3.16 | -6.51 | 5 |
| final8c_additive | PJM | uri | 3.00 | 2.53 | -0.38 | -2.27 | 6 |
| final8c_additive | SWPP | uri | 6.29 | 2.97 | -1.20 | -3.87 | 4 |
| final8c_additive | TVA | uri | 4.23 | -0.02 | -1.72 | -5.47 | 6 |
| final8c_boosting | DUK | uri | 3.69 | -5.15 | -5.15 | -9.61 | 6 |
| final8c_boosting | FPL | uri | 6.69 | -9.26 | -9.26 | -13.03 | 6 |
| final8c_boosting | MISO | uri | 2.76 | -3.11 | -3.11 | -5.76 | 5 |
| final8c_boosting | PJM | uri | 1.70 | -0.23 | -0.88 | -1.65 | 6 |
| final8c_boosting | SWPP | uri | 5.53 | -2.28 | -3.87 | -9.77 | 4 |
| final8c_boosting | TVA | uri | 3.44 | -1.97 | -2.01 | -6.11 | 6 |
| final8c_ensemble | DUK | uri | 3.95 | -4.91 | -4.91 | -8.07 | 6 |
| final8c_ensemble | FPL | uri | 8.99 | -12.42 | -12.42 | -15.93 | 6 |
| final8c_ensemble | MISO | uri | 3.79 | -3.76 | -3.76 | -7.16 | 5 |
| final8c_ensemble | PJM | uri | 2.15 | 0.94 | -0.46 | -2.62 | 6 |
| final8c_ensemble | SWPP | uri | 6.20 | -0.30 | -3.10 | -6.79 | 4 |
| final8c_ensemble | TVA | uri | 3.86 | -1.15 | -2.00 | -5.61 | 6 |
| final8c_recency | DUK | uri | 4.69 | -5.67 | -5.67 | -8.14 | 6 |
| final8c_recency | FPL | uri | 11.44 | -14.91 | -14.91 | -18.07 | 6 |
| final8c_recency | MISO | uri | 6.61 | -6.01 | -6.01 | -9.70 | 5 |
| final8c_recency | PJM | uri | 2.45 | 0.70 | -0.79 | -4.31 | 6 |
| final8c_recency | SWPP | uri | 6.80 | -2.15 | -4.48 | -10.44 | 4 |
| final8c_recency | TVA | uri | 4.54 | -1.47 | -2.53 | -5.88 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final8c | DUK | elliott | 3.16 | -2.60 | -2.60 | -6.20 | 4 |
| final8c | FPL | elliott | 5.66 | -6.22 | -6.22 | -9.76 | 5 |
| final8c | MISO | elliott | 3.67 | -2.91 | -3.53 | -6.48 | 5 |
| final8c | PJM | elliott | 4.32 | -4.43 | -4.43 | -8.76 | 5 |
| final8c | SWPP | elliott | 4.17 | -0.90 | -2.54 | -8.37 | 5 |
| final8c | TVA | elliott | 3.96 | 0.39 | -0.50 | -1.51 | 3 |
| final8c_additive | DUK | elliott | 4.02 | -5.09 | -5.09 | -7.49 | 4 |
| final8c_additive | FPL | elliott | 6.78 | -3.95 | -4.79 | -11.21 | 5 |
| final8c_additive | MISO | elliott | 3.52 | -3.96 | -4.14 | -6.55 | 5 |
| final8c_additive | PJM | elliott | 3.39 | -2.86 | -2.86 | -7.58 | 5 |
| final8c_additive | SWPP | elliott | 3.47 | -2.76 | -3.00 | -6.43 | 5 |
| final8c_additive | TVA | elliott | 4.63 | -1.13 | -1.13 | -2.10 | 3 |
| final8c_boosting | DUK | elliott | 3.97 | -3.95 | -3.95 | -6.26 | 4 |
| final8c_boosting | FPL | elliott | 8.92 | -14.07 | -14.07 | -20.17 | 5 |
| final8c_boosting | MISO | elliott | 3.59 | -2.37 | -3.39 | -4.42 | 5 |
| final8c_boosting | PJM | elliott | 3.90 | -4.59 | -4.59 | -7.59 | 5 |
| final8c_boosting | SWPP | elliott | 4.69 | -3.62 | -4.45 | -13.41 | 5 |
| final8c_boosting | TVA | elliott | 4.17 | -2.18 | -2.18 | -3.45 | 3 |
| final8c_ensemble | DUK | elliott | 3.76 | -5.43 | -5.43 | -6.83 | 4 |
| final8c_ensemble | FPL | elliott | 7.42 | -10.08 | -10.08 | -13.94 | 5 |
| final8c_ensemble | MISO | elliott | 3.79 | -4.19 | -4.45 | -7.58 | 5 |
| final8c_ensemble | PJM | elliott | 4.13 | -5.06 | -5.06 | -9.90 | 5 |
| final8c_ensemble | SWPP | elliott | 4.08 | -4.35 | -4.60 | -10.92 | 5 |
| final8c_ensemble | TVA | elliott | 4.05 | -2.55 | -2.55 | -3.22 | 3 |
| final8c_recency | DUK | elliott | 4.39 | -7.54 | -7.54 | -10.64 | 4 |
| final8c_recency | FPL | elliott | 9.94 | -12.10 | -12.10 | -17.32 | 5 |
| final8c_recency | MISO | elliott | 6.72 | -7.65 | -7.65 | -15.03 | 5 |
| final8c_recency | PJM | elliott | 5.92 | -7.98 | -7.98 | -16.00 | 5 |
| final8c_recency | SWPP | elliott | 4.94 | -7.16 | -7.16 | -13.48 | 5 |
| final8c_recency | TVA | elliott | 3.96 | -4.51 | -4.51 | -5.53 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final8c_ensemble | eve | 3.22 | -1.41 | -2.51 | 0.62 | 142 |
| 7 | final8c | eve | 3.36 | 0.73 | -1.46 | 0.58 | 142 |
| 8 | final8c_additive | eve | 3.41 | -1.21 | -2.51 | 0.58 | 142 |
| 9 | final8c_boosting | eve | 3.42 | -1.07 | -2.37 | 0.58 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final8c_recency | eve | 3.98 | -2.23 | -3.32 | 0.49 | 142 |
| 1 | final8c | special | 3.22 | -0.44 | -1.80 | 0.64 | 144 |
| 4 | final8c_ensemble | special | 3.27 | -2.66 | -3.24 | 0.64 | 144 |
| 2 | final8c_additive | special | 3.37 | -2.93 | -3.44 | 0.62 | 144 |
| 3 | final8c_boosting | special | 3.58 | -2.50 | -3.22 | 0.57 | 144 |
| 5 | final8c_recency | special | 4.05 | -2.70 | -3.66 | 0.56 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8c | all | 0.385 | 1.236 | 0.356 | 0.887 | 10.793 | 0.888 | 14.816 | 1.605 | 4239 |
| final8c | events | 0.512 | 2.189 | 0.801 | 0.699 | 12.171 | 0.667 | 26.249 | 2.885 | 60 |
| final8c | cold_mornings | 0.467 | 1.620 | 0.552 | 0.816 | 12.299 | 0.811 | 20.383 | 2.145 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final8c | 10.34 | -11.50 | -11.50 |
| 4440 | DUK | 2022-12-24 | final8c_additive | 9.86 | -13.14 | -13.14 |
| 4441 | DUK | 2022-12-24 | final8c_boosting | 11.11 | -17.18 | -17.18 |
| 4443 | DUK | 2022-12-24 | final8c_ensemble | 10.69 | -14.39 | -14.39 |
| 4442 | DUK | 2022-12-24 | final8c_recency | 11.27 | -12.65 | -12.65 |
| 8939 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8938 | MISO | 2021-02-16 | final8c | 1.66 | 1.40 | 0.00 |
| 8934 | MISO | 2021-02-16 | final8c_additive | 2.27 | 2.09 | 0.00 |
| 8935 | MISO | 2021-02-16 | final8c_boosting | 1.69 | 1.02 | 0.00 |
| 8937 | MISO | 2021-02-16 | final8c_ensemble | 1.65 | 0.55 | 0.00 |
| 8936 | MISO | 2021-02-16 | final8c_recency | 3.79 | -2.22 | -2.22 |
| 17795 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17794 | SWPP | 2021-02-15 | final8c | 2.43 | -2.01 | -2.01 |
| 17790 | SWPP | 2021-02-15 | final8c_additive | 2.78 | 1.37 | 0.00 |
| 17791 | SWPP | 2021-02-15 | final8c_boosting | 6.62 | -8.08 | -8.08 |
| 17793 | SWPP | 2021-02-15 | final8c_ensemble | 2.77 | -3.67 | -3.67 |
| 17792 | SWPP | 2021-02-15 | final8c_recency | 4.75 | -4.97 | -4.97 |
| 17801 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17800 | SWPP | 2021-02-16 | final8c | 4.24 | 0.53 | 0.00 |
| 17796 | SWPP | 2021-02-16 | final8c_additive | 7.82 | 3.66 | 0.00 |
| 17797 | SWPP | 2021-02-16 | final8c_boosting | 3.26 | -6.32 | -6.32 |
| 17799 | SWPP | 2021-02-16 | final8c_ensemble | 3.83 | -0.76 | -0.76 |
| 17798 | SWPP | 2021-02-16 | final8c_recency | 2.34 | -0.28 | -0.28 |
| 26177 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26176 | TVA | 2022-12-23 | final8c | 9.99 | -12.13 | -12.13 |
| 26172 | TVA | 2022-12-23 | final8c_additive | 6.42 | -6.22 | -6.22 |
| 26173 | TVA | 2022-12-23 | final8c_boosting | 14.99 | -15.32 | -15.32 |
| 26175 | TVA | 2022-12-23 | final8c_ensemble | 10.10 | -11.52 | -11.52 |
| 26174 | TVA | 2022-12-23 | final8c_recency | 10.32 | -13.65 | -13.65 |
| 26183 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26182 | TVA | 2022-12-24 | final8c | 6.48 | -14.56 | -14.56 |
| 26178 | TVA | 2022-12-24 | final8c_additive | 4.39 | -10.71 | -10.71 |
| 26179 | TVA | 2022-12-24 | final8c_boosting | 7.36 | -15.24 | -15.24 |
| 26181 | TVA | 2022-12-24 | final8c_ensemble | 6.46 | -13.00 | -13.00 |
| 26180 | TVA | 2022-12-24 | final8c_recency | 8.13 | -13.21 | -13.21 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final8c | DUK | mape | -0.615 | 0.539 | 747 |
| final8c | FPL | mape | -5.936 | 0.000 | 666 |
| final8c | MISO | mape | -11.730 | 0.000 | 741 |
| final8c | PJM | mape | -9.079 | 0.000 | 735 |
| final8c | SWPP | mape | -18.325 | 0.000 | 744 |
| final8c | TVA | mape | 7.547 | 0.000 | 732 |
| final8c_additive | DUK | mape | 4.827 | 0.000 | 747 |
| final8c_additive | FPL | mape | 7.070 | 0.000 | 666 |
| final8c_additive | MISO | mape | -4.910 | 0.000 | 741 |
| final8c_additive | PJM | mape | 2.388 | 0.017 | 735 |
| final8c_additive | SWPP | mape | -13.866 | 0.000 | 744 |
| final8c_additive | TVA | mape | 16.809 | 0.000 | 732 |
| final8c_boosting | DUK | mape | 2.173 | 0.030 | 747 |
| final8c_boosting | FPL | mape | 0.552 | 0.581 | 666 |
| final8c_boosting | MISO | mape | -7.440 | 0.000 | 741 |
| final8c_boosting | PJM | mape | -1.728 | 0.084 | 735 |
| final8c_boosting | SWPP | mape | -13.648 | 0.000 | 744 |
| final8c_boosting | TVA | mape | 11.467 | 0.000 | 732 |
| final8c_ensemble | DUK | mape | 0.242 | 0.809 | 747 |
| final8c_ensemble | FPL | mape | 4.700 | 0.000 | 666 |
| final8c_ensemble | MISO | mape | -7.464 | 0.000 | 741 |
| final8c_ensemble | PJM | mape | -2.853 | 0.004 | 735 |
| final8c_ensemble | SWPP | mape | -17.624 | 0.000 | 744 |
| final8c_ensemble | TVA | mape | 11.700 | 0.000 | 732 |
| final8c_recency | DUK | mape | 9.168 | 0.000 | 747 |
| final8c_recency | FPL | mape | 13.107 | 0.000 | 666 |
| final8c_recency | MISO | mape | 3.795 | 0.000 | 741 |
| final8c_recency | PJM | mape | 9.374 | 0.000 | 735 |
| final8c_recency | SWPP | mape | -10.379 | 0.000 | 744 |
| final8c_recency | TVA | mape | 18.030 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final8c | 0.986 |
| final8c_additive | 0.959 |
| final8c_boosting | 0.986 |
| final8c_ensemble | 0.986 |
| final8c_recency | 0.986 |
