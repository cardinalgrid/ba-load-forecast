# Phase G: the recipe with the deeper boosting and the temperature-bias correction

Development BAs: CISO, DUK, ERCO, ISNE, MISO, PJM, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3b` is `final3` with the boosting at 800 iterations, rate 0.03 and 63 leaves, and the HRRR temperature path corrected by its own recent bias per local hour (30 known days). Compare with `docs/phase_g_final.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | 2.40 | 2.07 | -0.14 | -1.39 | 1.22 | 0.54 | 0.25 | -17.68 | 5156 | 7.00 |
| final3b_ensemble | 2.44 | 2.11 | -1.55 | -2.21 | 1.21 | 0.53 | 0.17 | -19.35 | 5156 | 7.00 |
| final3b_boosting | 2.48 | 2.16 | -1.06 | -1.95 | 1.29 | 0.51 | 0.21 | -19.97 | 5156 | 7.00 |
| DF | 2.53 | 2.22 | 0.51 | -0.87 | 0.89 | 0.00 | 0.00 | -14.36 | 5156 | 7.00 |
| final3b_additive | 2.66 | 2.31 | -1.59 | -2.35 | 1.28 | 0.47 | 0.17 | -17.93 | 5156 | 7.00 |
| final3b_recency | 3.32 | 2.97 | -2.23 | -2.91 | 1.65 | 0.34 | 0.16 | -20.30 | 5156 | 7.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.24 | -6.72 |  |  | 719 | 25193.76 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | ERCO | 2.62 | 2.11 | 0.51 | -1.11 | 0.81 | -14.36 |  |  | 742 | 46834.59 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 748 | 13403.92 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final3b | CISO | 2.40 | 2.09 | 0.38 | -1.04 | 0.35 | -10.84 | 0.50 | 0.27 | 719 | 25193.76 |
| final3b | DUK | 3.30 | 2.91 | -0.43 | -2.17 | 1.43 | -17.68 | 0.40 | 0.29 | 746 | 12143.29 |
| final3b | ERCO | 2.63 | 2.18 | -0.12 | -1.59 | 0.98 | -15.02 | 0.47 | 0.27 | 742 | 46834.59 |
| final3b | ISNE | 3.33 | 2.94 | 0.08 | -1.47 | 0.49 | -15.22 | 0.32 | 0.21 | 748 | 13403.92 |
| final3b | MISO | 1.98 | 1.74 | -0.23 | -1.15 | 1.57 | -8.80 | 0.63 | 0.06 | 738 | 73700.16 |
| final3b | PJM | 2.25 | 1.94 | -0.25 | -1.40 | 1.36 | -11.54 | 0.60 | 0.38 | 734 | 92076.14 |
| final3b | TVA | 2.95 | 2.57 | 0.05 | -1.72 | 1.30 | -11.54 | 0.30 | 0.29 | 729 | 18581.23 |
| final3b_additive | CISO | 2.79 | 2.49 | -1.44 | -2.33 | 0.41 | -13.19 | 0.40 | 0.15 | 719 | 25193.76 |
| final3b_additive | DUK | 3.48 | 3.12 | -1.91 | -3.12 | 1.36 | -17.93 | 0.36 | 0.21 | 746 | 12143.29 |
| final3b_additive | ERCO | 3.01 | 2.56 | -1.92 | -2.77 | 1.00 | -16.87 | 0.40 | 0.15 | 742 | 46834.59 |
| final3b_additive | ISNE | 3.53 | 3.18 | -1.20 | -2.26 | 0.51 | -17.56 | 0.25 | 0.15 | 748 | 13403.92 |
| final3b_additive | MISO | 2.20 | 1.91 | -1.53 | -2.03 | 1.60 | -9.16 | 0.59 | 0.04 | 738 | 73700.16 |
| final3b_additive | PJM | 2.47 | 2.13 | -1.43 | -2.19 | 1.49 | -13.39 | 0.52 | 0.27 | 734 | 92076.14 |
| final3b_additive | TVA | 3.14 | 2.70 | -2.11 | -2.97 | 1.45 | -15.57 | 0.29 | 0.18 | 729 | 18581.23 |
| final3b_boosting | CISO | 2.47 | 2.18 | -0.36 | -1.38 | 0.38 | -14.08 | 0.50 | 0.23 | 719 | 25193.76 |
| final3b_boosting | DUK | 3.29 | 2.92 | -1.80 | -2.93 | 1.34 | -19.97 | 0.39 | 0.22 | 746 | 12143.29 |
| final3b_boosting | ERCO | 2.80 | 2.40 | -2.05 | -2.81 | 1.21 | -18.04 | 0.42 | 0.18 | 742 | 46834.59 |
| final3b_boosting | ISNE | 3.42 | 3.04 | -0.51 | -1.75 | 0.54 | -18.53 | 0.29 | 0.17 | 748 | 13403.92 |
| final3b_boosting | MISO | 2.08 | 1.81 | -0.83 | -1.58 | 1.56 | -10.10 | 0.61 | 0.04 | 738 | 73700.16 |
| final3b_boosting | PJM | 2.30 | 2.00 | -0.85 | -1.78 | 1.46 | -10.70 | 0.58 | 0.35 | 734 | 92076.14 |
| final3b_boosting | TVA | 2.92 | 2.59 | -1.38 | -2.42 | 1.29 | -13.47 | 0.31 | 0.21 | 729 | 18581.23 |
| final3b_ensemble | CISO | 2.54 | 2.33 | -1.36 | -2.00 | 0.35 | -12.22 | 0.45 | 0.15 | 719 | 25193.76 |
| final3b_ensemble | DUK | 3.27 | 2.86 | -1.92 | -3.01 | 1.33 | -19.35 | 0.41 | 0.21 | 746 | 12143.29 |
| final3b_ensemble | ERCO | 2.71 | 2.21 | -2.17 | -2.80 | 0.98 | -15.89 | 0.49 | 0.17 | 742 | 46834.59 |
| final3b_ensemble | ISNE | 3.38 | 3.02 | -1.46 | -2.27 | 0.48 | -16.62 | 0.28 | 0.12 | 748 | 13403.92 |
| final3b_ensemble | MISO | 2.02 | 1.81 | -1.33 | -1.82 | 1.59 | -8.96 | 0.63 | 0.04 | 738 | 73700.16 |
| final3b_ensemble | PJM | 2.26 | 1.94 | -1.36 | -2.04 | 1.33 | -11.06 | 0.59 | 0.28 | 734 | 92076.14 |
| final3b_ensemble | TVA | 2.90 | 2.48 | -1.95 | -2.78 | 1.31 | -13.83 | 0.33 | 0.18 | 729 | 18581.23 |
| final3b_recency | CISO | 4.60 | 4.49 | -3.23 | -3.66 | 0.63 | -14.17 | 0.11 | 0.08 | 719 | 25193.76 |
| final3b_recency | DUK | 3.83 | 3.44 | -2.09 | -3.36 | 1.42 | -20.30 | 0.30 | 0.20 | 746 | 12143.29 |
| final3b_recency | ERCO | 3.26 | 2.75 | -2.53 | -3.24 | 1.19 | -20.06 | 0.36 | 0.18 | 742 | 46834.59 |
| final3b_recency | ISNE | 5.07 | 4.74 | -3.26 | -3.89 | 0.79 | -19.39 | 0.07 | 0.09 | 748 | 13403.92 |
| final3b_recency | MISO | 2.86 | 2.52 | -1.82 | -2.37 | 2.16 | -13.40 | 0.44 | 0.04 | 738 | 73700.16 |
| final3b_recency | PJM | 3.03 | 2.71 | -1.96 | -2.68 | 1.96 | -18.17 | 0.37 | 0.26 | 734 | 92076.14 |
| final3b_recency | TVA | 3.50 | 2.99 | -2.45 | -3.40 | 1.47 | -16.04 | 0.23 | 0.18 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final3b | CISO | uri | 2.30 | -0.75 | -1.21 | -2.51 | 6 |
| final3b | DUK | uri | 3.80 | -1.58 | -2.03 | -4.44 | 6 |
| final3b | ERCO | uri | 6.33 | -8.09 | -8.09 | -8.26 | 2 |
| final3b | ISNE | uri | 2.33 | 1.05 | -0.34 | -1.97 | 6 |
| final3b | MISO | uri | 3.55 | -2.77 | -3.06 | -6.61 | 5 |
| final3b | PJM | uri | 1.91 | 0.66 | -0.59 | -2.98 | 6 |
| final3b | TVA | uri | 4.17 | -1.06 | -2.87 | -7.04 | 6 |
| final3b_additive | CISO | uri | 2.21 | -0.86 | -1.39 | -2.66 | 6 |
| final3b_additive | DUK | uri | 3.67 | -3.00 | -3.00 | -5.76 | 6 |
| final3b_additive | ERCO | uri | 6.25 | -7.15 | -7.15 | -9.52 | 2 |
| final3b_additive | ISNE | uri | 2.44 | 0.57 | -0.57 | -2.76 | 6 |
| final3b_additive | MISO | uri | 3.82 | -2.88 | -3.35 | -6.79 | 5 |
| final3b_additive | PJM | uri | 2.36 | 1.32 | -0.63 | -3.23 | 6 |
| final3b_additive | TVA | uri | 3.74 | -1.43 | -2.63 | -6.45 | 6 |
| final3b_boosting | CISO | uri | 2.42 | -1.36 | -1.70 | -3.60 | 6 |
| final3b_boosting | DUK | uri | 3.42 | -3.18 | -3.20 | -5.46 | 6 |
| final3b_boosting | ERCO | uri | 7.56 | -11.95 | -11.95 | -14.39 | 2 |
| final3b_boosting | ISNE | uri | 3.29 | 0.90 | -0.75 | -2.87 | 6 |
| final3b_boosting | MISO | uri | 3.23 | -3.77 | -3.77 | -6.96 | 5 |
| final3b_boosting | PJM | uri | 1.48 | -0.75 | -1.14 | -3.50 | 6 |
| final3b_boosting | TVA | uri | 3.72 | -3.93 | -4.45 | -9.56 | 6 |
| final3b_ensemble | CISO | uri | 2.52 | -1.96 | -2.17 | -3.24 | 6 |
| final3b_ensemble | DUK | uri | 3.67 | -3.51 | -3.51 | -5.85 | 6 |
| final3b_ensemble | ERCO | uri | 7.01 | -8.83 | -8.83 | -9.82 | 2 |
| final3b_ensemble | ISNE | uri | 2.33 | -0.59 | -1.13 | -3.76 | 6 |
| final3b_ensemble | MISO | uri | 4.09 | -4.14 | -4.14 | -7.68 | 5 |
| final3b_ensemble | PJM | uri | 1.87 | -0.01 | -0.85 | -3.86 | 6 |
| final3b_ensemble | TVA | uri | 3.69 | -2.74 | -3.62 | -7.77 | 6 |
| final3b_recency | CISO | uri | 4.35 | -3.96 | -3.96 | -6.33 | 6 |
| final3b_recency | DUK | uri | 4.20 | -4.36 | -4.36 | -6.34 | 6 |
| final3b_recency | ERCO | uri | 7.52 | -7.05 | -7.05 | -10.47 | 2 |
| final3b_recency | ISNE | uri | 4.19 | -4.15 | -4.15 | -6.32 | 6 |
| final3b_recency | MISO | uri | 7.10 | -6.36 | -6.36 | -9.83 | 5 |
| final3b_recency | PJM | uri | 2.59 | -0.45 | -1.25 | -5.20 | 6 |
| final3b_recency | TVA | uri | 4.29 | -2.69 | -3.74 | -7.55 | 6 |
| DF | CISO | elliott | 3.38 | 1.96 | -0.88 | -4.40 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final3b | CISO | elliott | 3.55 | 2.30 | -0.65 | -3.25 | 5 |
| final3b | DUK | elliott | 3.22 | -1.18 | -1.70 | -4.30 | 4 |
| final3b | ERCO | elliott | 5.18 | -1.14 | -2.82 | -6.42 | 5 |
| final3b | ISNE | elliott | 3.54 | 2.52 | -0.95 | -2.92 | 5 |
| final3b | MISO | elliott | 3.43 | -2.29 | -2.95 | -5.88 | 5 |
| final3b | PJM | elliott | 4.52 | -3.10 | -3.43 | -7.28 | 5 |
| final3b | TVA | elliott | 5.38 | 4.15 | 0.00 | 0.00 | 3 |
| final3b_additive | CISO | elliott | 3.12 | 1.13 | -1.03 | -5.17 | 5 |
| final3b_additive | DUK | elliott | 4.18 | -4.76 | -4.76 | -7.35 | 4 |
| final3b_additive | ERCO | elliott | 6.97 | -5.62 | -5.96 | -12.59 | 5 |
| final3b_additive | ISNE | elliott | 3.89 | -0.40 | -2.00 | -5.32 | 5 |
| final3b_additive | MISO | elliott | 3.32 | -3.87 | -4.02 | -7.52 | 5 |
| final3b_additive | PJM | elliott | 3.52 | -2.15 | -2.30 | -5.07 | 5 |
| final3b_additive | TVA | elliott | 5.35 | 1.75 | -0.69 | -2.08 | 3 |
| final3b_boosting | CISO | elliott | 3.14 | 0.18 | -1.22 | -5.09 | 5 |
| final3b_boosting | DUK | elliott | 3.54 | -3.91 | -3.91 | -8.85 | 4 |
| final3b_boosting | ERCO | elliott | 6.78 | -9.43 | -9.51 | -18.04 | 5 |
| final3b_boosting | ISNE | elliott | 3.64 | 1.79 | -1.01 | -3.89 | 5 |
| final3b_boosting | MISO | elliott | 3.61 | -2.83 | -3.51 | -4.98 | 5 |
| final3b_boosting | PJM | elliott | 4.81 | -3.75 | -4.30 | -8.86 | 5 |
| final3b_boosting | TVA | elliott | 5.18 | 0.30 | -0.72 | -2.16 | 3 |
| final3b_ensemble | CISO | elliott | 2.97 | 0.81 | -0.98 | -4.69 | 5 |
| final3b_ensemble | DUK | elliott | 3.84 | -5.08 | -5.08 | -7.26 | 4 |
| final3b_ensemble | ERCO | elliott | 5.79 | -6.26 | -6.48 | -10.52 | 5 |
| final3b_ensemble | ISNE | elliott | 3.49 | 0.94 | -1.58 | -4.93 | 5 |
| final3b_ensemble | MISO | elliott | 3.44 | -3.89 | -4.13 | -7.27 | 5 |
| final3b_ensemble | PJM | elliott | 4.47 | -4.80 | -4.80 | -9.23 | 5 |
| final3b_ensemble | TVA | elliott | 4.72 | 0.93 | -1.23 | -1.91 | 3 |
| final3b_recency | CISO | elliott | 3.72 | 1.67 | -0.86 | -3.29 | 5 |
| final3b_recency | DUK | elliott | 5.06 | -6.91 | -6.91 | -9.54 | 4 |
| final3b_recency | ERCO | elliott | 4.69 | -2.84 | -3.55 | -7.11 | 5 |
| final3b_recency | ISNE | elliott | 4.23 | 1.17 | -2.00 | -6.17 | 5 |
| final3b_recency | MISO | elliott | 5.41 | -5.86 | -5.86 | -13.40 | 5 |
| final3b_recency | PJM | elliott | 6.50 | -9.08 | -9.08 | -18.17 | 5 |
| final3b_recency | TVA | elliott | 4.69 | 0.66 | -3.18 | -5.49 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final3b_ensemble | eve | 3.21 | -0.83 | -2.25 | 0.48 | 168 |
| 6 | DF | eve | 3.25 | 1.28 | -0.95 |  | 168 |
| 7 | final3b | eve | 3.40 | 0.86 | -1.50 | 0.42 | 168 |
| 9 | final3b_boosting | eve | 3.48 | -0.14 | -2.02 | 0.47 | 168 |
| 8 | final3b_additive | eve | 3.50 | -0.64 | -2.28 | 0.41 | 168 |
| 11 | final3b_recency | eve | 3.94 | -2.12 | -3.17 | 0.37 | 168 |
| 4 | final3b_ensemble | special | 3.36 | -2.29 | -3.23 | 0.48 | 170 |
| 1 | final3b | special | 3.38 | -0.61 | -2.18 | 0.49 | 170 |
| 0 | DF | special | 3.40 | 0.64 | -1.16 |  | 170 |
| 2 | final3b_additive | special | 3.56 | -2.62 | -3.59 | 0.44 | 170 |
| 3 | final3b_boosting | special | 3.62 | -1.60 | -2.80 | 0.46 | 170 |
| 5 | final3b_recency | special | 4.21 | -2.92 | -3.94 | 0.36 | 170 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3b | all | 0.391 | 1.350 | 0.396 | 0.889 | 11.727 | 0.894 | 5008 |
| final3b | events | 0.460 | 1.794 | 0.553 | 0.797 | 12.190 | 0.826 | 69 |
| final3b | cold_mornings | 0.475 | 1.664 | 0.524 | 0.843 | 13.307 | 0.795 | 210 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 8753 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 8752 | DUK | 2022-12-24 | final3b | 8.17 | -10.55 | -10.55 |
| 8748 | DUK | 2022-12-24 | final3b_additive | 8.99 | -12.06 | -12.06 |
| 8749 | DUK | 2022-12-24 | final3b_boosting | 11.24 | -19.47 | -19.47 |
| 8751 | DUK | 2022-12-24 | final3b_ensemble | 10.26 | -14.17 | -14.17 |
| 8750 | DUK | 2022-12-24 | final3b_recency | 10.57 | -9.77 | -9.77 |
| 9245 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 9244 | ERCO | 2021-02-17 | final3b | 32.95 | 27.06 | 0.00 |
| 9240 | ERCO | 2021-02-17 | final3b_additive | 28.26 | 25.47 | 0.00 |
| 9241 | ERCO | 2021-02-17 | final3b_boosting | 29.27 | 23.31 | 0.00 |
| 9243 | ERCO | 2021-02-17 | final3b_ensemble | 31.45 | 26.47 | 0.00 |
| 9242 | ERCO | 2021-02-17 | final3b_recency | 38.25 | 32.04 | 0.00 |
| 9251 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 9250 | ERCO | 2021-02-18 | final3b | 6.54 | 4.93 | 0.00 |
| 9246 | ERCO | 2021-02-18 | final3b_additive | 12.49 | 11.24 | 0.00 |
| 9247 | ERCO | 2021-02-18 | final3b_boosting | 3.37 | -5.05 | -5.05 |
| 9249 | ERCO | 2021-02-18 | final3b_ensemble | 5.35 | 2.30 | 0.00 |
| 9248 | ERCO | 2021-02-18 | final3b_recency | 4.78 | 2.29 | 0.00 |
| 18203 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 18202 | MISO | 2021-02-16 | final3b | 2.54 | 2.57 | 0.00 |
| 18198 | MISO | 2021-02-16 | final3b_additive | 2.09 | 2.11 | 0.00 |
| 18199 | MISO | 2021-02-16 | final3b_boosting | 2.37 | 1.39 | 0.00 |
| 18201 | MISO | 2021-02-16 | final3b_ensemble | 1.82 | 0.71 | 0.00 |
| 18200 | MISO | 2021-02-16 | final3b_recency | 3.84 | -2.24 | -2.24 |
| 30923 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 30922 | TVA | 2022-12-23 | final3b | 7.95 | -8.79 | -8.79 |
| 30918 | TVA | 2022-12-23 | final3b_additive | 7.51 | -3.70 | -3.70 |
| 30919 | TVA | 2022-12-23 | final3b_boosting | 14.81 | -15.52 | -15.52 |
| 30921 | TVA | 2022-12-23 | final3b_ensemble | 8.93 | -10.11 | -10.11 |
| 30920 | TVA | 2022-12-23 | final3b_recency | 11.74 | -11.65 | -11.65 |
| 30929 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 30928 | TVA | 2022-12-24 | final3b | 4.55 | -9.14 | -9.14 |
| 30924 | TVA | 2022-12-24 | final3b_additive | 4.32 | -8.73 | -8.73 |
| 30925 | TVA | 2022-12-24 | final3b_boosting | 6.42 | -12.98 | -12.98 |
| 30927 | TVA | 2022-12-24 | final3b_ensemble | 5.85 | -11.26 | -11.26 |
| 30926 | TVA | 2022-12-24 | final3b_recency | 7.60 | -12.29 | -12.29 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3b | CISO | mape | 0.056 | 0.955 | 719 |
| final3b | DUK | mape | 6.873 | 0.000 | 746 |
| final3b | ERCO | mape | 0.065 | 0.948 | 742 |
| final3b | ISNE | mape | 14.757 | 0.000 | 748 |
| final3b | MISO | mape | -11.024 | 0.000 | 738 |
| final3b | PJM | mape | -3.836 | 0.000 | 734 |
| final3b | TVA | mape | 13.210 | 0.000 | 729 |
| final3b_additive | CISO | mape | 6.957 | 0.000 | 719 |
| final3b_additive | DUK | mape | 9.008 | 0.000 | 746 |
| final3b_additive | ERCO | mape | 5.669 | 0.000 | 742 |
| final3b_additive | ISNE | mape | 18.501 | 0.000 | 748 |
| final3b_additive | MISO | mape | -6.465 | 0.000 | 738 |
| final3b_additive | PJM | mape | 0.239 | 0.811 | 734 |
| final3b_additive | TVA | mape | 14.521 | 0.000 | 729 |
| final3b_boosting | CISO | mape | 1.276 | 0.202 | 719 |
| final3b_boosting | DUK | mape | 6.638 | 0.000 | 746 |
| final3b_boosting | ERCO | mape | 2.736 | 0.006 | 742 |
| final3b_boosting | ISNE | mape | 15.711 | 0.000 | 748 |
| final3b_boosting | MISO | mape | -9.101 | 0.000 | 738 |
| final3b_boosting | PJM | mape | -2.947 | 0.003 | 734 |
| final3b_boosting | TVA | mape | 12.811 | 0.000 | 729 |
| final3b_ensemble | CISO | mape | 2.793 | 0.005 | 719 |
| final3b_ensemble | DUK | mape | 6.314 | 0.000 | 746 |
| final3b_ensemble | ERCO | mape | 1.364 | 0.173 | 742 |
| final3b_ensemble | ISNE | mape | 16.636 | 0.000 | 748 |
| final3b_ensemble | MISO | mape | -9.574 | 0.000 | 738 |
| final3b_ensemble | PJM | mape | -3.849 | 0.000 | 734 |
| final3b_ensemble | TVA | mape | 11.429 | 0.000 | 729 |
| final3b_recency | CISO | mape | 32.180 | 0.000 | 719 |
| final3b_recency | DUK | mape | 13.064 | 0.000 | 746 |
| final3b_recency | ERCO | mape | 8.358 | 0.000 | 742 |
| final3b_recency | ISNE | mape | 34.962 | 0.000 | 748 |
| final3b_recency | MISO | mape | 2.640 | 0.008 | 738 |
| final3b_recency | PJM | mape | 9.283 | 0.000 | 734 |
| final3b_recency | TVA | mape | 17.453 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.996 |
| final3b | 0.992 |
| final3b_additive | 0.970 |
| final3b_boosting | 0.992 |
| final3b_ensemble | 0.992 |
| final3b_recency | 0.992 |
