# Phase N: station weights, the GFS left out on cold days

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final8q` is `final8` (HRRR, NBM and GFS weighted per station by their 30-day error) except on days whose temperature path minimum falls below the tenth percentile of the station's observed daily minima over the last 365 days known at the cut-off: there the GFS leaves the mean and the HRRR and the NBM carry it. Compare with `docs/phase_n_weights3.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8q | 2.19 | 1.89 | -0.05 | -1.21 | 1.34 | 0.63 | 0.28 | -46.62 | 4365 | 6.00 |
| final8q_ensemble | 2.45 | 2.15 | -1.74 | -2.24 | 1.32 | 0.57 | 0.18 | -49.12 | 4365 | 6.00 |
| final8q_boosting | 2.50 | 2.22 | -1.41 | -2.10 | 1.51 | 0.55 | 0.20 | -48.89 | 4365 | 6.00 |
| final8q_additive | 2.70 | 2.38 | -1.95 | -2.51 | 1.40 | 0.51 | 0.18 | -48.25 | 4365 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.05 | 0.00 | 0.00 | -47.43 | 4365 | 6.00 |
| final8q_recency | 3.18 | 2.80 | -1.97 | -2.62 | 1.68 | 0.40 | 0.17 | -50.47 | 4365 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final8q | DUK | 2.83 | 2.49 | 0.02 | -1.52 | 1.20 | -13.99 | 0.50 | 0.32 | 747 | 12145.43 |
| final8q | FPL | 3.40 | 2.82 | -0.09 | -1.88 | 0.97 | -46.62 | 0.63 | 0.71 | 666 | 15342.04 |
| final8q | MISO | 1.96 | 1.69 | 0.07 | -0.99 | 1.49 | -6.94 | 0.66 | 0.06 | 741 | 73714.43 |
| final8q | PJM | 2.01 | 1.77 | -0.22 | -1.20 | 1.35 | -10.68 | 0.65 | 0.42 | 735 | 92099.88 |
| final8q | SWPP | 2.22 | 1.83 | -0.06 | -1.27 | 1.32 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final8q | TVA | 2.60 | 2.30 | 0.27 | -1.33 | 1.14 | -11.13 | 0.39 | 0.32 | 732 | 18589.75 |
| final8q_additive | DUK | 3.17 | 2.88 | -2.34 | -3.04 | 1.25 | -16.21 | 0.42 | 0.19 | 747 | 12145.43 |
| final8q_additive | FPL | 4.66 | 4.15 | -4.65 | -5.25 | 1.03 | -48.25 | 0.45 | 0.35 | 666 | 15342.04 |
| final8q_additive | MISO | 2.29 | 1.99 | -1.67 | -2.10 | 1.47 | -10.13 | 0.56 | 0.04 | 741 | 73714.43 |
| final8q_additive | PJM | 2.59 | 2.29 | -1.64 | -2.23 | 1.43 | -12.60 | 0.48 | 0.31 | 735 | 92099.88 |
| final8q_additive | SWPP | 2.48 | 2.06 | -1.70 | -2.35 | 1.38 | -21.65 | 0.69 | 0.07 | 744 | 31394.87 |
| final8q_additive | TVA | 3.30 | 3.05 | -2.58 | -3.23 | 1.39 | -14.44 | 0.26 | 0.13 | 732 | 18589.75 |
| final8q_boosting | DUK | 2.99 | 2.67 | -1.65 | -2.51 | 1.33 | -16.10 | 0.42 | 0.22 | 747 | 12145.43 |
| final8q_boosting | FPL | 3.97 | 3.66 | -4.48 | -4.94 | 1.18 | -48.89 | 0.52 | 0.36 | 666 | 15342.04 |
| final8q_boosting | MISO | 2.17 | 1.89 | -1.04 | -1.66 | 1.58 | -9.57 | 0.60 | 0.04 | 741 | 73714.43 |
| final8q_boosting | PJM | 2.38 | 2.20 | -1.06 | -1.78 | 1.53 | -12.20 | 0.54 | 0.35 | 735 | 92099.88 |
| final8q_boosting | SWPP | 2.46 | 2.03 | -1.69 | -2.41 | 1.58 | -29.38 | 0.69 | 0.06 | 744 | 31394.87 |
| final8q_boosting | TVA | 2.84 | 2.50 | -1.53 | -2.31 | 1.37 | -12.55 | 0.32 | 0.19 | 732 | 18589.75 |
| final8q_ensemble | DUK | 2.87 | 2.52 | -1.84 | -2.58 | 1.29 | -13.99 | 0.46 | 0.19 | 747 | 12145.43 |
| final8q_ensemble | FPL | 4.37 | 3.93 | -4.98 | -5.39 | 0.99 | -49.12 | 0.50 | 0.33 | 666 | 15342.04 |
| final8q_ensemble | MISO | 2.13 | 1.86 | -1.46 | -1.86 | 1.50 | -9.36 | 0.60 | 0.03 | 741 | 73714.43 |
| final8q_ensemble | PJM | 2.33 | 2.08 | -1.44 | -1.96 | 1.27 | -11.61 | 0.56 | 0.32 | 735 | 92099.88 |
| final8q_ensemble | SWPP | 2.20 | 1.82 | -1.42 | -2.03 | 1.27 | -20.14 | 0.72 | 0.06 | 744 | 31394.87 |
| final8q_ensemble | TVA | 2.87 | 2.58 | -2.08 | -2.70 | 1.23 | -12.60 | 0.31 | 0.12 | 732 | 18589.75 |
| final8q_recency | DUK | 3.42 | 3.12 | -1.52 | -2.67 | 1.54 | -15.26 | 0.35 | 0.21 | 747 | 12145.43 |
| final8q_recency | FPL | 5.67 | 4.90 | -6.37 | -6.79 | 1.15 | -50.47 | 0.36 | 0.27 | 666 | 15342.04 |
| final8q_recency | MISO | 2.95 | 2.59 | -1.85 | -2.30 | 2.00 | -15.59 | 0.42 | 0.04 | 741 | 73714.43 |
| final8q_recency | PJM | 3.00 | 2.66 | -1.71 | -2.33 | 1.64 | -16.39 | 0.36 | 0.29 | 735 | 92099.88 |
| final8q_recency | SWPP | 2.81 | 2.40 | -0.86 | -1.91 | 1.65 | -18.61 | 0.65 | 0.08 | 744 | 31394.87 |
| final8q_recency | TVA | 3.38 | 3.06 | -2.27 | -3.06 | 1.27 | -15.37 | 0.22 | 0.15 | 732 | 18589.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final8q | DUK | uri | 4.40 | -3.38 | -3.71 | -9.09 | 6 |
| final8q | FPL | uri | 7.30 | -7.05 | -7.05 | -10.61 | 6 |
| final8q | MISO | uri | 3.93 | -3.39 | -3.63 | -6.94 | 5 |
| final8q | PJM | uri | 1.89 | 0.24 | -0.70 | -2.82 | 6 |
| final8q | SWPP | uri | 6.42 | -0.06 | -3.21 | -7.46 | 4 |
| final8q | TVA | uri | 3.76 | -1.49 | -2.67 | -5.92 | 6 |
| final8q_additive | DUK | uri | 4.12 | -4.21 | -4.21 | -6.69 | 6 |
| final8q_additive | FPL | uri | 9.32 | -13.69 | -13.69 | -16.61 | 6 |
| final8q_additive | MISO | uri | 3.63 | -2.43 | -3.06 | -6.47 | 5 |
| final8q_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final8q_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final8q_additive | TVA | uri | 3.69 | 0.22 | -1.33 | -3.63 | 6 |
| final8q_boosting | DUK | uri | 4.04 | -5.11 | -5.11 | -9.61 | 6 |
| final8q_boosting | FPL | uri | 6.70 | -9.18 | -9.18 | -13.79 | 6 |
| final8q_boosting | MISO | uri | 2.45 | -2.58 | -2.68 | -4.81 | 5 |
| final8q_boosting | PJM | uri | 1.95 | -0.50 | -0.92 | -2.57 | 6 |
| final8q_boosting | SWPP | uri | 5.08 | -3.51 | -4.28 | -9.79 | 4 |
| final8q_boosting | TVA | uri | 3.46 | -1.30 | -1.93 | -4.27 | 6 |
| final8q_ensemble | DUK | uri | 4.29 | -5.05 | -5.05 | -8.06 | 6 |
| final8q_ensemble | FPL | uri | 9.00 | -12.43 | -12.43 | -15.76 | 6 |
| final8q_ensemble | MISO | uri | 3.72 | -3.49 | -3.49 | -6.78 | 5 |
| final8q_ensemble | PJM | uri | 2.39 | 1.17 | -0.51 | -3.07 | 6 |
| final8q_ensemble | SWPP | uri | 6.13 | -1.40 | -3.63 | -7.72 | 4 |
| final8q_ensemble | TVA | uri | 3.59 | -0.66 | -1.70 | -4.09 | 6 |
| final8q_recency | DUK | uri | 5.00 | -5.86 | -5.86 | -8.14 | 6 |
| final8q_recency | FPL | uri | 11.58 | -15.01 | -15.01 | -17.89 | 6 |
| final8q_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final8q_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final8q_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final8q_recency | TVA | uri | 4.05 | -0.91 | -2.11 | -4.57 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final8q | DUK | elliott | 3.11 | -1.87 | -2.11 | -5.56 | 4 |
| final8q | FPL | elliott | 5.52 | -5.69 | -5.69 | -9.51 | 5 |
| final8q | MISO | elliott | 3.64 | -2.86 | -3.52 | -6.79 | 5 |
| final8q | PJM | elliott | 4.32 | -4.26 | -4.26 | -8.66 | 5 |
| final8q | SWPP | elliott | 4.08 | -0.81 | -2.38 | -7.63 | 5 |
| final8q | TVA | elliott | 4.08 | 0.30 | -0.47 | -1.40 | 3 |
| final8q_additive | DUK | elliott | 3.89 | -4.32 | -4.32 | -6.30 | 4 |
| final8q_additive | FPL | elliott | 7.43 | -3.39 | -4.83 | -11.76 | 5 |
| final8q_additive | MISO | elliott | 3.51 | -3.79 | -4.00 | -6.60 | 5 |
| final8q_additive | PJM | elliott | 3.37 | -2.64 | -2.64 | -7.54 | 5 |
| final8q_additive | SWPP | elliott | 3.44 | -2.75 | -3.00 | -6.28 | 5 |
| final8q_additive | TVA | elliott | 4.73 | -0.54 | -0.59 | -1.27 | 3 |
| final8q_boosting | DUK | elliott | 4.03 | -3.08 | -3.08 | -6.28 | 4 |
| final8q_boosting | FPL | elliott | 8.75 | -13.82 | -13.82 | -20.04 | 5 |
| final8q_boosting | MISO | elliott | 3.52 | -2.09 | -3.12 | -4.27 | 5 |
| final8q_boosting | PJM | elliott | 3.88 | -4.52 | -4.52 | -7.50 | 5 |
| final8q_boosting | SWPP | elliott | 4.60 | -3.35 | -4.18 | -12.42 | 5 |
| final8q_boosting | TVA | elliott | 4.33 | -2.05 | -2.05 | -3.07 | 3 |
| final8q_ensemble | DUK | elliott | 3.60 | -4.60 | -4.60 | -5.80 | 4 |
| final8q_ensemble | FPL | elliott | 7.12 | -9.55 | -9.55 | -13.65 | 5 |
| final8q_ensemble | MISO | elliott | 3.69 | -4.03 | -4.30 | -7.76 | 5 |
| final8q_ensemble | PJM | elliott | 4.16 | -4.98 | -4.98 | -9.90 | 5 |
| final8q_ensemble | SWPP | elliott | 3.99 | -4.19 | -4.46 | -10.42 | 5 |
| final8q_ensemble | TVA | elliott | 4.07 | -2.07 | -2.07 | -2.63 | 3 |
| final8q_recency | DUK | elliott | 4.08 | -6.68 | -6.68 | -9.35 | 4 |
| final8q_recency | FPL | elliott | 9.67 | -11.11 | -11.11 | -16.78 | 5 |
| final8q_recency | MISO | elliott | 6.72 | -7.67 | -7.67 | -15.59 | 5 |
| final8q_recency | PJM | elliott | 5.96 | -8.01 | -8.01 | -16.39 | 5 |
| final8q_recency | SWPP | elliott | 4.79 | -6.95 | -6.95 | -13.10 | 5 |
| final8q_recency | TVA | elliott | 3.83 | -3.80 | -3.80 | -4.81 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final8q_ensemble | eve | 3.22 | -1.32 | -2.44 | 0.61 | 142 |
| 7 | final8q | eve | 3.36 | 0.78 | -1.42 | 0.58 | 142 |
| 9 | final8q_boosting | eve | 3.41 | -0.95 | -2.30 | 0.58 | 142 |
| 8 | final8q_additive | eve | 3.43 | -1.12 | -2.45 | 0.61 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final8q_recency | eve | 3.98 | -2.14 | -3.25 | 0.49 | 142 |
| 1 | final8q | special | 3.25 | -0.43 | -1.81 | 0.62 | 144 |
| 4 | final8q_ensemble | special | 3.29 | -2.53 | -3.16 | 0.62 | 144 |
| 2 | final8q_additive | special | 3.39 | -2.83 | -3.37 | 0.61 | 144 |
| 3 | final8q_boosting | special | 3.61 | -2.35 | -3.12 | 0.57 | 144 |
| 5 | final8q_recency | special | 4.07 | -2.57 | -3.58 | 0.56 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8q | all | 0.386 | 1.242 | 0.358 | 0.887 | 10.837 | 0.886 | 14.874 | 1.613 | 4239 |
| final8q | events | 0.477 | 2.183 | 0.811 | 0.719 | 12.549 | 0.667 | 25.758 | 2.871 | 60 |
| final8q | cold_mornings | 0.480 | 1.690 | 0.569 | 0.807 | 12.690 | 0.756 | 20.984 | 2.226 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final8q | 9.66 | -11.22 | -11.22 |
| 4440 | DUK | 2022-12-24 | final8q_additive | 8.92 | -12.68 | -12.68 |
| 4441 | DUK | 2022-12-24 | final8q_boosting | 10.90 | -17.09 | -17.09 |
| 4443 | DUK | 2022-12-24 | final8q_ensemble | 10.08 | -13.84 | -13.84 |
| 4442 | DUK | 2022-12-24 | final8q_recency | 10.63 | -11.43 | -11.43 |
| 8939 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8938 | MISO | 2021-02-16 | final8q | 1.63 | 1.67 | 0.00 |
| 8934 | MISO | 2021-02-16 | final8q_additive | 2.38 | 2.18 | 0.00 |
| 8935 | MISO | 2021-02-16 | final8q_boosting | 1.96 | 1.33 | 0.00 |
| 8937 | MISO | 2021-02-16 | final8q_ensemble | 1.67 | 0.72 | 0.00 |
| 8936 | MISO | 2021-02-16 | final8q_recency | 3.61 | -2.07 | -2.07 |
| 17795 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17794 | SWPP | 2021-02-15 | final8q | 3.17 | -2.45 | -2.45 |
| 17790 | SWPP | 2021-02-15 | final8q_additive | 2.24 | 1.30 | 0.00 |
| 17791 | SWPP | 2021-02-15 | final8q_boosting | 6.97 | -8.54 | -8.54 |
| 17793 | SWPP | 2021-02-15 | final8q_ensemble | 3.29 | -4.01 | -4.01 |
| 17792 | SWPP | 2021-02-15 | final8q_recency | 4.81 | -5.28 | -5.28 |
| 17801 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17800 | SWPP | 2021-02-16 | final8q | 3.95 | 0.03 | 0.00 |
| 17796 | SWPP | 2021-02-16 | final8q_additive | 7.74 | 3.67 | 0.00 |
| 17797 | SWPP | 2021-02-16 | final8q_boosting | 3.27 | -6.32 | -6.32 |
| 17799 | SWPP | 2021-02-16 | final8q_ensemble | 3.84 | -0.80 | -0.80 |
| 17798 | SWPP | 2021-02-16 | final8q_recency | 2.57 | -0.10 | -0.10 |
| 26177 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26176 | TVA | 2022-12-23 | final8q | 9.58 | -11.20 | -11.20 |
| 26172 | TVA | 2022-12-23 | final8q_additive | 6.10 | -4.61 | -4.61 |
| 26173 | TVA | 2022-12-23 | final8q_boosting | 15.03 | -15.47 | -15.47 |
| 26175 | TVA | 2022-12-23 | final8q_ensemble | 9.72 | -10.91 | -10.91 |
| 26174 | TVA | 2022-12-23 | final8q_recency | 10.25 | -13.32 | -13.32 |
| 26183 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26182 | TVA | 2022-12-24 | final8q | 6.03 | -13.09 | -13.09 |
| 26178 | TVA | 2022-12-24 | final8q_additive | 4.10 | -10.03 | -10.03 |
| 26179 | TVA | 2022-12-24 | final8q_boosting | 7.18 | -15.19 | -15.19 |
| 26181 | TVA | 2022-12-24 | final8q_ensemble | 6.22 | -12.64 | -12.64 |
| 26180 | TVA | 2022-12-24 | final8q_recency | 7.90 | -12.89 | -12.89 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final8q | DUK | mape | -0.128 | 0.898 | 747 |
| final8q | FPL | mape | -5.356 | 0.000 | 666 |
| final8q | MISO | mape | -11.707 | 0.000 | 741 |
| final8q | PJM | mape | -9.119 | 0.000 | 735 |
| final8q | SWPP | mape | -18.196 | 0.000 | 744 |
| final8q | TVA | mape | 8.105 | 0.000 | 732 |
| final8q_additive | DUK | mape | 5.128 | 0.000 | 747 |
| final8q_additive | FPL | mape | 7.456 | 0.000 | 666 |
| final8q_additive | MISO | mape | -4.983 | 0.000 | 741 |
| final8q_additive | PJM | mape | 2.410 | 0.016 | 735 |
| final8q_additive | SWPP | mape | -13.847 | 0.000 | 744 |
| final8q_additive | TVA | mape | 17.187 | 0.000 | 732 |
| final8q_boosting | DUK | mape | 2.604 | 0.009 | 747 |
| final8q_boosting | FPL | mape | 1.155 | 0.248 | 666 |
| final8q_boosting | MISO | mape | -7.227 | 0.000 | 741 |
| final8q_boosting | PJM | mape | -1.477 | 0.140 | 735 |
| final8q_boosting | SWPP | mape | -13.734 | 0.000 | 744 |
| final8q_boosting | TVA | mape | 11.823 | 0.000 | 732 |
| final8q_ensemble | DUK | mape | 0.628 | 0.530 | 747 |
| final8q_ensemble | FPL | mape | 5.294 | 0.000 | 666 |
| final8q_ensemble | MISO | mape | -7.479 | 0.000 | 741 |
| final8q_ensemble | PJM | mape | -2.705 | 0.007 | 735 |
| final8q_ensemble | SWPP | mape | -17.623 | 0.000 | 744 |
| final8q_ensemble | TVA | mape | 12.124 | 0.000 | 732 |
| final8q_recency | DUK | mape | 9.401 | 0.000 | 747 |
| final8q_recency | FPL | mape | 13.632 | 0.000 | 666 |
| final8q_recency | MISO | mape | 3.739 | 0.000 | 741 |
| final8q_recency | PJM | mape | 9.510 | 0.000 | 735 |
| final8q_recency | SWPP | mape | -10.358 | 0.000 | 744 |
| final8q_recency | TVA | mape | 18.374 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final8q | 0.986 |
| final8q_additive | 0.959 |
| final8q_boosting | 0.986 |
| final8q_ensemble | 0.986 |
| final8q_recency | 0.986 |
