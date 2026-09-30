# Phase N: the HRRR and the NBM weighted per station by their recent error

Development BAs: DUK, FPL, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final8b` is `final6` with the weights of the HRRR and the NBM set per station and per day as the inverse of each model's mean squared error over the last 30 days known at the cut-off; no GFS. Compare with `docs/phase_k_nbm_blend.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8b | 2.20 | 1.88 | -0.06 | -1.22 | 1.36 | 0.63 | 0.27 | -46.36 | 4359 | 6.00 |
| final8b_ensemble | 2.39 | 2.10 | -1.60 | -2.17 | 1.32 | 0.60 | 0.18 | -49.61 | 4359 | 6.00 |
| final8b_boosting | 2.48 | 2.21 | -1.27 | -2.03 | 1.47 | 0.57 | 0.20 | -48.96 | 4359 | 6.00 |
| final8b_additive | 2.63 | 2.34 | -1.86 | -2.46 | 1.39 | 0.53 | 0.18 | -48.74 | 4359 | 6.00 |
| DF | 2.78 | 2.49 | 0.52 | -1.02 | 1.05 | 0.00 | 0.00 | -47.43 | 4359 | 6.00 |
| final8b_recency | 3.12 | 2.74 | -1.76 | -2.53 | 1.66 | 0.42 | 0.18 | -51.31 | 4359 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 739 | 73717.29 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 742 | 31388.55 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.23 | 0.97 | -11.24 |  |  | 730 | 18590.46 |
| final8b | DUK | 2.82 | 2.45 | 0.01 | -1.51 | 1.20 | -12.15 | 0.51 | 0.31 | 747 | 12145.43 |
| final8b | FPL | 3.58 | 2.96 | -0.53 | -2.23 | 1.00 | -46.36 | 0.61 | 0.68 | 666 | 15342.04 |
| final8b | MISO | 1.94 | 1.69 | 0.07 | -0.98 | 1.53 | -7.00 | 0.65 | 0.06 | 739 | 73717.29 |
| final8b | PJM | 2.03 | 1.75 | -0.15 | -1.20 | 1.34 | -10.43 | 0.64 | 0.42 | 735 | 92099.88 |
| final8b | SWPP | 2.14 | 1.75 | -0.18 | -1.26 | 1.32 | -20.00 | 0.75 | 0.10 | 742 | 31388.55 |
| final8b | TVA | 2.63 | 2.21 | 0.45 | -1.24 | 1.25 | -11.14 | 0.38 | 0.33 | 730 | 18590.46 |
| final8b_additive | DUK | 3.07 | 2.77 | -2.14 | -2.92 | 1.26 | -16.21 | 0.44 | 0.20 | 747 | 12145.43 |
| final8b_additive | FPL | 5.24 | 4.75 | -5.63 | -6.09 | 1.00 | -48.74 | 0.39 | 0.28 | 666 | 15342.04 |
| final8b_additive | MISO | 2.25 | 1.96 | -1.59 | -2.06 | 1.48 | -9.65 | 0.58 | 0.04 | 739 | 73717.29 |
| final8b_additive | PJM | 2.45 | 2.21 | -1.42 | -2.09 | 1.43 | -12.40 | 0.52 | 0.31 | 735 | 92099.88 |
| final8b_additive | SWPP | 2.40 | 2.02 | -1.66 | -2.29 | 1.35 | -21.79 | 0.70 | 0.07 | 742 | 31388.55 |
| final8b_additive | TVA | 3.01 | 2.70 | -2.17 | -2.88 | 1.31 | -13.86 | 0.30 | 0.15 | 730 | 18590.46 |
| final8b_boosting | DUK | 2.94 | 2.59 | -1.45 | -2.40 | 1.25 | -13.11 | 0.46 | 0.23 | 747 | 12145.43 |
| final8b_boosting | FPL | 4.75 | 4.42 | -5.50 | -5.83 | 1.18 | -48.96 | 0.44 | 0.30 | 666 | 15342.04 |
| final8b_boosting | MISO | 2.12 | 1.86 | -0.86 | -1.55 | 1.63 | -10.44 | 0.61 | 0.05 | 739 | 73717.29 |
| final8b_boosting | PJM | 2.30 | 2.10 | -0.80 | -1.64 | 1.44 | -12.03 | 0.56 | 0.36 | 735 | 92099.88 |
| final8b_boosting | SWPP | 2.42 | 2.00 | -1.62 | -2.32 | 1.49 | -29.38 | 0.70 | 0.06 | 742 | 31388.55 |
| final8b_boosting | TVA | 2.72 | 2.37 | -1.06 | -2.01 | 1.39 | -12.55 | 0.35 | 0.21 | 730 | 18590.46 |
| final8b_ensemble | DUK | 2.81 | 2.43 | -1.61 | -2.46 | 1.19 | -13.95 | 0.51 | 0.20 | 747 | 12145.43 |
| final8b_ensemble | FPL | 5.16 | 4.65 | -6.13 | -6.43 | 1.07 | -49.61 | 0.41 | 0.26 | 666 | 15342.04 |
| final8b_ensemble | MISO | 2.06 | 1.82 | -1.31 | -1.76 | 1.53 | -9.56 | 0.62 | 0.04 | 739 | 73717.29 |
| final8b_ensemble | PJM | 2.19 | 1.93 | -1.16 | -1.79 | 1.24 | -11.29 | 0.62 | 0.34 | 735 | 92099.88 |
| final8b_ensemble | SWPP | 2.12 | 1.71 | -1.34 | -1.93 | 1.29 | -20.24 | 0.74 | 0.06 | 742 | 31388.55 |
| final8b_ensemble | TVA | 2.65 | 2.33 | -1.60 | -2.34 | 1.21 | -12.75 | 0.36 | 0.15 | 730 | 18590.46 |
| final8b_recency | DUK | 3.40 | 3.03 | -1.20 | -2.51 | 1.46 | -15.26 | 0.37 | 0.22 | 747 | 12145.43 |
| final8b_recency | FPL | 6.46 | 5.47 | -7.76 | -8.09 | 1.18 | -51.31 | 0.30 | 0.21 | 666 | 15342.04 |
| final8b_recency | MISO | 2.84 | 2.52 | -1.63 | -2.16 | 2.02 | -13.27 | 0.43 | 0.04 | 739 | 73717.29 |
| final8b_recency | PJM | 2.86 | 2.58 | -1.32 | -2.12 | 1.60 | -16.39 | 0.39 | 0.31 | 735 | 92099.88 |
| final8b_recency | SWPP | 2.75 | 2.29 | -0.68 | -1.76 | 1.57 | -18.63 | 0.65 | 0.08 | 742 | 31388.55 |
| final8b_recency | TVA | 3.21 | 2.81 | -1.66 | -2.70 | 1.23 | -15.53 | 0.24 | 0.18 | 730 | 18590.46 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final8b | DUK | uri | 3.68 | -2.37 | -2.53 | -5.59 | 6 |
| final8b | FPL | uri | 7.74 | -8.08 | -8.08 | -11.09 | 6 |
| final8b | MISO | uri | 3.92 | -3.32 | -3.44 | -6.81 | 5 |
| final8b | PJM | uri | 1.68 | -0.13 | -0.61 | -2.60 | 6 |
| final8b | SWPP | uri | 6.11 | 0.35 | -2.68 | -5.99 | 4 |
| final8b | TVA | uri | 3.85 | -1.11 | -2.29 | -6.30 | 6 |
| final8b_additive | DUK | uri | 3.52 | -3.07 | -3.07 | -4.04 | 6 |
| final8b_additive | FPL | uri | 9.75 | -13.98 | -13.98 | -17.55 | 6 |
| final8b_additive | MISO | uri | 3.68 | -2.72 | -3.24 | -6.65 | 5 |
| final8b_additive | PJM | uri | 2.71 | 2.02 | -0.40 | -2.43 | 6 |
| final8b_additive | SWPP | uri | 6.12 | 2.08 | -1.65 | -4.45 | 4 |
| final8b_additive | TVA | uri | 3.93 | -0.68 | -2.07 | -6.29 | 6 |
| final8b_boosting | DUK | uri | 3.43 | -3.45 | -3.45 | -6.53 | 6 |
| final8b_boosting | FPL | uri | 7.44 | -9.82 | -9.82 | -13.08 | 6 |
| final8b_boosting | MISO | uri | 2.75 | -3.00 | -3.04 | -5.53 | 5 |
| final8b_boosting | PJM | uri | 1.54 | -1.21 | -1.37 | -2.57 | 6 |
| final8b_boosting | SWPP | uri | 4.88 | -3.23 | -3.99 | -9.76 | 4 |
| final8b_boosting | TVA | uri | 3.14 | -2.56 | -2.56 | -5.93 | 6 |
| final8b_ensemble | DUK | uri | 3.65 | -3.70 | -3.70 | -5.27 | 6 |
| final8b_ensemble | FPL | uri | 9.57 | -12.86 | -12.86 | -16.14 | 6 |
| final8b_ensemble | MISO | uri | 3.81 | -3.76 | -3.76 | -7.08 | 5 |
| final8b_ensemble | PJM | uri | 1.89 | 0.25 | -0.60 | -3.05 | 6 |
| final8b_ensemble | SWPP | uri | 5.83 | -1.15 | -3.32 | -7.28 | 4 |
| final8b_ensemble | TVA | uri | 3.56 | -1.72 | -2.40 | -6.05 | 6 |
| final8b_recency | DUK | uri | 4.27 | -4.60 | -4.60 | -6.29 | 6 |
| final8b_recency | FPL | uri | 12.02 | -15.32 | -15.32 | -18.55 | 6 |
| final8b_recency | MISO | uri | 6.76 | -6.11 | -6.11 | -9.77 | 5 |
| final8b_recency | PJM | uri | 2.37 | 0.24 | -0.88 | -4.36 | 6 |
| final8b_recency | SWPP | uri | 6.47 | -2.74 | -4.54 | -10.55 | 4 |
| final8b_recency | TVA | uri | 4.22 | -1.94 | -2.92 | -6.23 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final8b | DUK | elliott | 3.12 | -2.14 | -2.33 | -5.49 | 4 |
| final8b | FPL | elliott | 5.57 | -5.94 | -5.94 | -9.38 | 5 |
| final8b | MISO | elliott | 3.43 | -2.55 | -3.27 | -6.14 | 5 |
| final8b | PJM | elliott | 4.30 | -4.09 | -4.09 | -8.66 | 5 |
| final8b | SWPP | elliott | 4.52 | 0.46 | -2.08 | -6.55 | 5 |
| final8b | TVA | elliott | 4.19 | 0.34 | -0.33 | -0.98 | 3 |
| final8b_additive | DUK | elliott | 3.76 | -4.44 | -4.44 | -6.30 | 4 |
| final8b_additive | FPL | elliott | 7.62 | -3.61 | -5.06 | -11.76 | 5 |
| final8b_additive | MISO | elliott | 3.44 | -3.86 | -4.08 | -6.57 | 5 |
| final8b_additive | PJM | elliott | 3.40 | -2.68 | -2.68 | -7.54 | 5 |
| final8b_additive | SWPP | elliott | 3.46 | -2.72 | -2.99 | -6.33 | 5 |
| final8b_additive | TVA | elliott | 4.71 | -0.54 | -0.58 | -1.28 | 3 |
| final8b_boosting | DUK | elliott | 3.99 | -3.24 | -3.24 | -6.28 | 4 |
| final8b_boosting | FPL | elliott | 8.87 | -14.54 | -14.54 | -20.04 | 5 |
| final8b_boosting | MISO | elliott | 3.45 | -2.42 | -3.33 | -4.61 | 5 |
| final8b_boosting | PJM | elliott | 3.90 | -4.59 | -4.59 | -7.50 | 5 |
| final8b_boosting | SWPP | elliott | 5.66 | -2.12 | -3.98 | -12.25 | 5 |
| final8b_boosting | TVA | elliott | 4.70 | -2.17 | -2.17 | -4.04 | 3 |
| final8b_ensemble | DUK | elliott | 3.52 | -4.76 | -4.76 | -5.85 | 4 |
| final8b_ensemble | FPL | elliott | 7.28 | -10.03 | -10.03 | -13.69 | 5 |
| final8b_ensemble | MISO | elliott | 3.50 | -3.78 | -4.13 | -7.14 | 5 |
| final8b_ensemble | PJM | elliott | 4.20 | -5.03 | -5.03 | -9.94 | 5 |
| final8b_ensemble | SWPP | elliott | 4.03 | -2.88 | -3.53 | -9.39 | 5 |
| final8b_ensemble | TVA | elliott | 4.19 | -2.06 | -2.06 | -2.92 | 3 |
| final8b_recency | DUK | elliott | 4.11 | -6.77 | -6.77 | -9.35 | 4 |
| final8b_recency | FPL | elliott | 9.82 | -11.29 | -11.29 | -16.78 | 5 |
| final8b_recency | MISO | elliott | 5.45 | -5.92 | -5.92 | -13.27 | 5 |
| final8b_recency | PJM | elliott | 5.98 | -8.04 | -8.04 | -16.39 | 5 |
| final8b_recency | SWPP | elliott | 3.68 | -3.93 | -4.36 | -10.39 | 5 |
| final8b_recency | TVA | elliott | 3.80 | -3.65 | -3.65 | -4.82 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final8b_ensemble | eve | 3.28 | -1.17 | -2.38 | 0.61 | 142 |
| 7 | final8b | eve | 3.38 | 0.85 | -1.38 | 0.58 | 142 |
| 8 | final8b_additive | eve | 3.47 | -1.04 | -2.44 | 0.58 | 142 |
| 9 | final8b_boosting | eve | 3.54 | -0.80 | -2.28 | 0.57 | 142 |
| 6 | DF | eve | 3.93 | 0.94 | -1.39 |  | 142 |
| 11 | final8b_recency | eve | 3.99 | -1.88 | -3.09 | 0.47 | 142 |
| 1 | final8b | special | 3.24 | -0.47 | -1.85 | 0.65 | 144 |
| 4 | final8b_ensemble | special | 3.34 | -2.51 | -3.21 | 0.62 | 144 |
| 2 | final8b_additive | special | 3.41 | -2.83 | -3.44 | 0.58 | 144 |
| 3 | final8b_boosting | special | 3.67 | -2.31 | -3.18 | 0.56 | 144 |
| 5 | final8b_recency | special | 4.11 | -2.48 | -3.59 | 0.51 | 144 |
| 0 | DF | special | 4.25 | 0.42 | -1.61 |  | 144 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8b | all | 0.389 | 1.253 | 0.363 | 0.887 | 10.934 | 0.890 | 15.040 | 1.630 | 4233 |
| final8b | events | 0.502 | 2.166 | 0.784 | 0.699 | 12.138 | 0.667 | 25.719 | 2.842 | 60 |
| final8b | cold_mornings | 0.455 | 1.591 | 0.540 | 0.813 | 12.152 | 0.806 | 19.913 | 2.104 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final8b | 9.70 | -11.61 | -11.61 |
| 4440 | DUK | 2022-12-24 | final8b_additive | 8.92 | -12.68 | -12.68 |
| 4441 | DUK | 2022-12-24 | final8b_boosting | 10.90 | -17.09 | -17.09 |
| 4443 | DUK | 2022-12-24 | final8b_ensemble | 10.07 | -13.77 | -13.77 |
| 4442 | DUK | 2022-12-24 | final8b_recency | 10.63 | -11.43 | -11.43 |
| 8939 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 8938 | MISO | 2021-02-16 | final8b | 1.63 | 1.27 | 0.00 |
| 8934 | MISO | 2021-02-16 | final8b_additive | 2.21 | 2.07 | 0.00 |
| 8935 | MISO | 2021-02-16 | final8b_boosting | 1.52 | 0.96 | 0.00 |
| 8937 | MISO | 2021-02-16 | final8b_ensemble | 1.55 | 0.53 | 0.00 |
| 8936 | MISO | 2021-02-16 | final8b_recency | 3.85 | -2.21 | -2.21 |
| 17783 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 17782 | SWPP | 2021-02-15 | final8b | 2.55 | -2.29 | -2.29 |
| 17778 | SWPP | 2021-02-15 | final8b_additive | 2.58 | 1.33 | 0.00 |
| 17779 | SWPP | 2021-02-15 | final8b_boosting | 6.69 | -8.06 | -8.06 |
| 17781 | SWPP | 2021-02-15 | final8b_ensemble | 2.87 | -3.73 | -3.73 |
| 17780 | SWPP | 2021-02-15 | final8b_recency | 4.67 | -4.93 | -4.93 |
| 17789 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 17788 | SWPP | 2021-02-16 | final8b | 4.14 | 0.15 | 0.00 |
| 17784 | SWPP | 2021-02-16 | final8b_additive | 7.68 | 3.65 | 0.00 |
| 17785 | SWPP | 2021-02-16 | final8b_boosting | 3.27 | -6.32 | -6.32 |
| 17787 | SWPP | 2021-02-16 | final8b_ensemble | 3.78 | -0.90 | -0.90 |
| 17786 | SWPP | 2021-02-16 | final8b_recency | 2.36 | -0.42 | -0.42 |
| 26141 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26140 | TVA | 2022-12-23 | final8b | 9.29 | -11.22 | -11.22 |
| 26136 | TVA | 2022-12-23 | final8b_additive | 6.22 | -4.51 | -4.51 |
| 26137 | TVA | 2022-12-23 | final8b_boosting | 16.11 | -17.06 | -17.06 |
| 26139 | TVA | 2022-12-23 | final8b_ensemble | 9.56 | -10.87 | -10.87 |
| 26138 | TVA | 2022-12-23 | final8b_recency | 9.60 | -11.74 | -11.74 |
| 26147 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26146 | TVA | 2022-12-24 | final8b | 6.15 | -12.00 | -12.00 |
| 26142 | TVA | 2022-12-24 | final8b_additive | 4.13 | -9.98 | -9.98 |
| 26143 | TVA | 2022-12-24 | final8b_boosting | 7.82 | -15.18 | -15.18 |
| 26145 | TVA | 2022-12-24 | final8b_ensemble | 6.43 | -12.52 | -12.52 |
| 26144 | TVA | 2022-12-24 | final8b_recency | 7.87 | -12.63 | -12.63 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final8b | DUK | mape | -0.394 | 0.694 | 747 |
| final8b | FPL | mape | -3.143 | 0.002 | 666 |
| final8b | MISO | mape | -11.850 | 0.000 | 739 |
| final8b | PJM | mape | -8.743 | 0.000 | 735 |
| final8b | SWPP | mape | -19.417 | 0.000 | 742 |
| final8b | TVA | mape | 8.262 | 0.000 | 730 |
| final8b_additive | DUK | mape | 3.765 | 0.000 | 747 |
| final8b_additive | FPL | mape | 11.094 | 0.000 | 666 |
| final8b_additive | MISO | mape | -5.694 | 0.000 | 739 |
| final8b_additive | PJM | mape | -0.145 | 0.885 | 735 |
| final8b_additive | SWPP | mape | -15.113 | 0.000 | 742 |
| final8b_additive | TVA | mape | 13.685 | 0.000 | 730 |
| final8b_boosting | DUK | mape | 1.775 | 0.076 | 747 |
| final8b_boosting | FPL | mape | 8.231 | 0.000 | 666 |
| final8b_boosting | MISO | mape | -8.295 | 0.000 | 739 |
| final8b_boosting | PJM | mape | -3.219 | 0.001 | 735 |
| final8b_boosting | SWPP | mape | -14.301 | 0.000 | 742 |
| final8b_boosting | TVA | mape | 10.158 | 0.000 | 730 |
| final8b_ensemble | DUK | mape | -0.544 | 0.586 | 747 |
| final8b_ensemble | FPL | mape | 10.546 | 0.000 | 666 |
| final8b_ensemble | MISO | mape | -8.821 | 0.000 | 739 |
| final8b_ensemble | PJM | mape | -5.621 | 0.000 | 735 |
| final8b_ensemble | SWPP | mape | -19.063 | 0.000 | 742 |
| final8b_ensemble | TVA | mape | 8.594 | 0.000 | 730 |
| final8b_recency | DUK | mape | 8.816 | 0.000 | 747 |
| final8b_recency | FPL | mape | 16.341 | 0.000 | 666 |
| final8b_recency | MISO | mape | 2.424 | 0.015 | 739 |
| final8b_recency | PJM | mape | 7.231 | 0.000 | 735 |
| final8b_recency | SWPP | mape | -11.348 | 0.000 | 742 |
| final8b_recency | TVA | mape | 16.220 | 0.000 | 730 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.987 |
| final8b | 0.984 |
| final8b_additive | 0.957 |
| final8b_boosting | 0.984 |
| final8b_ensemble | 0.984 |
| final8b_recency | 0.984 |
