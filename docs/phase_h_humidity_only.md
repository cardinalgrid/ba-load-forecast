# Phase H: humidity alone

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3_h` is the phase G recipe with the dew point, dew-point depression, relative humidity and heat index as features of the boosting and the heat index as the input of the additive model's smooth response (no wind field yet); `h_boosting` adds the block to the phase G boosting. Compare with `docs/phase_g_final.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_h | 2.39 | 2.08 | 0.01 | -1.30 | 1.25 | 0.57 | 0.30 | -46.51 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final3_h_ensemble | 2.74 | 2.42 | -1.38 | -2.18 | 1.28 | 0.50 | 0.23 | -50.98 | 8056 | 11.00 |
| final3_h_boosting | 2.83 | 2.49 | -0.97 | -2.00 | 1.42 | 0.45 | 0.25 | -51.51 | 8056 | 11.00 |
| h_boosting | 2.83 | 2.49 | -0.97 | -2.00 | 1.42 | 0.45 | 0.25 | -51.51 | 8056 | 11.00 |
| final3_h_additive | 2.99 | 2.65 | -1.60 | -2.46 | 1.31 | 0.44 | 0.21 | -49.25 | 8056 | 11.00 |
| final3_h_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.06 | 1.80 | 0.20 | -0.95 | 1.45 | -19.35 |  |  | 746 | 6536.52 |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.24 | -6.72 |  |  | 719 | 25193.76 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | ERCO | 2.62 | 2.11 | 0.51 | -1.11 | 0.81 | -14.36 |  |  | 742 | 46834.59 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 748 | 13403.92 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.67 | 0.40 | -12.87 |  |  | 748 | 17415.28 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final3_h | BPAT | 2.46 | 2.15 | -0.42 | -1.45 | 1.71 | -17.90 | 0.38 | 0.25 | 746 | 6536.52 |
| final3_h | CISO | 2.44 | 2.13 | 0.38 | -1.10 | 0.34 | -12.53 | 0.50 | 0.26 | 719 | 25193.76 |
| final3_h | DUK | 3.17 | 2.84 | -0.04 | -1.77 | 1.34 | -15.27 | 0.40 | 0.31 | 746 | 12143.29 |
| final3_h | ERCO | 2.60 | 2.20 | -0.04 | -1.43 | 1.01 | -13.99 | 0.49 | 0.29 | 742 | 46834.59 |
| final3_h | FPL | 3.62 | 3.16 | -0.80 | -2.56 | 1.03 | -46.51 | 0.59 | 0.65 | 665 | 15346.05 |
| final3_h | ISNE | 3.20 | 2.82 | 0.36 | -1.28 | 0.51 | -15.60 | 0.35 | 0.21 | 748 | 13403.92 |
| final3_h | MISO | 2.00 | 1.76 | 0.09 | -1.00 | 1.69 | -7.73 | 0.63 | 0.07 | 738 | 73700.16 |
| final3_h | NYIS | 2.26 | 1.97 | -0.03 | -1.30 | 0.56 | -12.89 | 0.62 | 0.73 | 748 | 17415.28 |
| final3_h | PJM | 2.15 | 1.90 | -0.00 | -1.21 | 1.41 | -10.08 | 0.61 | 0.43 | 734 | 92076.14 |
| final3_h | SWPP | 2.19 | 1.83 | -0.21 | -1.30 | 1.43 | -20.05 | 0.75 | 0.11 | 741 | 31382.01 |
| final3_h | TVA | 2.82 | 2.45 | 0.31 | -1.43 | 1.38 | -10.87 | 0.34 | 0.32 | 729 | 18581.23 |
| final3_h_additive | BPAT | 2.67 | 2.36 | -0.73 | -1.68 | 1.79 | -16.90 | 0.31 | 0.23 | 746 | 6536.52 |
| final3_h_additive | CISO | 3.60 | 3.04 | -2.81 | -3.70 | 0.40 | -17.92 | 0.29 | 0.13 | 719 | 25193.76 |
| final3_h_additive | DUK | 3.33 | 2.95 | -1.57 | -2.69 | 1.36 | -16.17 | 0.39 | 0.24 | 746 | 12143.29 |
| final3_h_additive | ERCO | 3.65 | 3.31 | -2.63 | -3.32 | 1.07 | -16.29 | 0.30 | 0.14 | 742 | 46834.59 |
| final3_h_additive | FPL | 6.15 | 5.77 | -6.17 | -6.69 | 1.08 | -49.25 | 0.26 | 0.25 | 665 | 15346.05 |
| final3_h_additive | ISNE | 3.66 | 3.30 | -1.16 | -2.39 | 0.51 | -21.27 | 0.25 | 0.16 | 748 | 13403.92 |
| final3_h_additive | MISO | 2.29 | 2.03 | -1.25 | -1.84 | 1.59 | -8.60 | 0.55 | 0.05 | 738 | 73700.16 |
| final3_h_additive | NYIS | 2.54 | 2.22 | -1.04 | -2.04 | 0.54 | -15.21 | 0.56 | 0.59 | 748 | 17415.28 |
| final3_h_additive | PJM | 2.64 | 2.33 | -0.65 | -1.72 | 1.64 | -11.72 | 0.47 | 0.38 | 734 | 92076.14 |
| final3_h_additive | SWPP | 2.38 | 1.98 | -1.20 | -1.97 | 1.46 | -21.10 | 0.70 | 0.08 | 741 | 31382.01 |
| final3_h_additive | TVA | 3.20 | 2.83 | -1.56 | -2.57 | 1.47 | -15.27 | 0.27 | 0.22 | 729 | 18581.23 |
| final3_h_boosting | BPAT | 2.66 | 2.41 | -0.52 | -1.60 | 1.99 | -17.63 | 0.30 | 0.25 | 746 | 6536.52 |
| final3_h_boosting | CISO | 2.89 | 2.58 | -1.91 | -2.52 | 0.44 | -16.09 | 0.37 | 0.15 | 719 | 25193.76 |
| final3_h_boosting | DUK | 3.32 | 2.90 | -0.97 | -2.34 | 1.40 | -18.14 | 0.37 | 0.26 | 746 | 12143.29 |
| final3_h_boosting | ERCO | 2.96 | 2.55 | -2.43 | -2.97 | 1.33 | -19.98 | 0.36 | 0.16 | 742 | 46834.59 |
| final3_h_boosting | FPL | 6.03 | 5.61 | -6.48 | -6.83 | 1.30 | -51.51 | 0.21 | 0.28 | 665 | 15346.05 |
| final3_h_boosting | ISNE | 3.44 | 3.09 | -0.22 | -1.52 | 0.53 | -16.39 | 0.29 | 0.19 | 748 | 13403.92 |
| final3_h_boosting | MISO | 2.24 | 1.92 | -0.45 | -1.33 | 1.64 | -9.61 | 0.57 | 0.06 | 738 | 73700.16 |
| final3_h_boosting | NYIS | 2.56 | 2.27 | -0.12 | -1.32 | 0.74 | -11.42 | 0.53 | 0.73 | 748 | 17415.28 |
| final3_h_boosting | PJM | 2.66 | 2.40 | 0.19 | -1.28 | 1.72 | -13.24 | 0.44 | 0.43 | 734 | 92076.14 |
| final3_h_boosting | SWPP | 2.52 | 2.05 | -1.10 | -2.04 | 1.59 | -29.46 | 0.70 | 0.08 | 741 | 31382.01 |
| final3_h_boosting | TVA | 3.08 | 2.64 | -0.60 | -1.91 | 1.50 | -12.10 | 0.30 | 0.27 | 729 | 18581.23 |
| final3_h_ensemble | BPAT | 2.49 | 2.22 | -0.83 | -1.67 | 1.72 | -17.85 | 0.37 | 0.23 | 746 | 6536.52 |
| final3_h_ensemble | CISO | 3.22 | 2.74 | -2.75 | -3.26 | 0.36 | -16.85 | 0.34 | 0.12 | 719 | 25193.76 |
| final3_h_ensemble | DUK | 3.18 | 2.79 | -1.06 | -2.34 | 1.41 | -15.03 | 0.42 | 0.25 | 746 | 12143.29 |
| final3_h_ensemble | ERCO | 3.08 | 2.69 | -2.56 | -3.06 | 1.06 | -14.72 | 0.37 | 0.15 | 742 | 46834.59 |
| final3_h_ensemble | FPL | 6.33 | 5.96 | -7.00 | -7.32 | 1.06 | -50.98 | 0.22 | 0.23 | 665 | 15346.05 |
| final3_h_ensemble | ISNE | 3.39 | 3.13 | -1.17 | -2.11 | 0.49 | -17.25 | 0.28 | 0.15 | 748 | 13403.92 |
| final3_h_ensemble | MISO | 2.13 | 1.87 | -0.94 | -1.54 | 1.63 | -8.27 | 0.61 | 0.05 | 738 | 73700.16 |
| final3_h_ensemble | NYIS | 2.31 | 2.00 | -0.55 | -1.53 | 0.55 | -14.01 | 0.60 | 0.69 | 748 | 17415.28 |
| final3_h_ensemble | PJM | 2.43 | 2.17 | -0.34 | -1.43 | 1.55 | -10.64 | 0.54 | 0.42 | 734 | 92076.14 |
| final3_h_ensemble | SWPP | 2.18 | 1.76 | -0.87 | -1.67 | 1.37 | -19.90 | 0.75 | 0.09 | 741 | 31382.01 |
| final3_h_ensemble | TVA | 2.94 | 2.55 | -1.07 | -2.15 | 1.36 | -13.60 | 0.31 | 0.24 | 729 | 18581.23 |
| final3_h_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final3_h_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final3_h_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final3_h_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final3_h_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final3_h_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final3_h_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final3_h_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final3_h_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final3_h_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final3_h_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |
| h_boosting | BPAT | 2.66 | 2.41 | -0.52 | -1.60 | 1.99 | -17.63 | 0.30 | 0.25 | 746 | 6536.52 |
| h_boosting | CISO | 2.89 | 2.58 | -1.91 | -2.52 | 0.44 | -16.09 | 0.37 | 0.15 | 719 | 25193.76 |
| h_boosting | DUK | 3.32 | 2.90 | -0.97 | -2.34 | 1.40 | -18.14 | 0.37 | 0.26 | 746 | 12143.29 |
| h_boosting | ERCO | 2.96 | 2.55 | -2.43 | -2.97 | 1.33 | -19.98 | 0.36 | 0.16 | 742 | 46834.59 |
| h_boosting | FPL | 6.03 | 5.61 | -6.48 | -6.83 | 1.30 | -51.51 | 0.21 | 0.28 | 665 | 15346.05 |
| h_boosting | ISNE | 3.44 | 3.09 | -0.22 | -1.52 | 0.53 | -16.39 | 0.29 | 0.19 | 748 | 13403.92 |
| h_boosting | MISO | 2.24 | 1.92 | -0.45 | -1.33 | 1.64 | -9.61 | 0.57 | 0.06 | 738 | 73700.16 |
| h_boosting | NYIS | 2.56 | 2.27 | -0.12 | -1.32 | 0.74 | -11.42 | 0.53 | 0.73 | 748 | 17415.28 |
| h_boosting | PJM | 2.66 | 2.40 | 0.19 | -1.28 | 1.72 | -13.24 | 0.44 | 0.43 | 734 | 92076.14 |
| h_boosting | SWPP | 2.52 | 2.05 | -1.10 | -2.04 | 1.59 | -29.46 | 0.70 | 0.08 | 741 | 31382.01 |
| h_boosting | TVA | 3.08 | 2.64 | -0.60 | -1.91 | 1.50 | -12.10 | 0.30 | 0.27 | 729 | 18581.23 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | uri | 2.77 | -0.21 | -1.69 | -6.97 | 6 |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final3_h | BPAT | uri | 2.49 | -0.43 | -0.95 | -4.69 | 6 |
| final3_h | CISO | uri | 2.15 | -1.01 | -1.47 | -2.94 | 6 |
| final3_h | DUK | uri | 3.59 | -1.42 | -1.92 | -3.73 | 6 |
| final3_h | ERCO | uri | 6.47 | -8.26 | -8.26 | -8.38 | 2 |
| final3_h | FPL | uri | 8.28 | -7.39 | -7.39 | -10.19 | 6 |
| final3_h | ISNE | uri | 2.57 | 1.79 | -0.03 | -0.18 | 6 |
| final3_h | MISO | uri | 3.88 | -3.34 | -3.57 | -7.12 | 5 |
| final3_h | NYIS | uri | 2.11 | 2.21 | -0.11 | -0.68 | 6 |
| final3_h | PJM | uri | 1.95 | 0.22 | -0.64 | -2.57 | 6 |
| final3_h | SWPP | uri | 6.67 | -0.31 | -3.34 | -7.67 | 4 |
| final3_h | TVA | uri | 3.60 | -1.49 | -2.71 | -6.07 | 6 |
| final3_h_additive | BPAT | uri | 2.81 | -0.36 | -1.22 | -2.30 | 6 |
| final3_h_additive | CISO | uri | 2.17 | 1.37 | -0.07 | -0.42 | 6 |
| final3_h_additive | DUK | uri | 3.45 | -1.94 | -1.98 | -6.44 | 6 |
| final3_h_additive | ERCO | uri | 4.29 | -5.84 | -5.84 | -7.94 | 2 |
| final3_h_additive | FPL | uri | 10.36 | -14.93 | -14.93 | -17.55 | 6 |
| final3_h_additive | ISNE | uri | 2.94 | 1.92 | -0.21 | -1.25 | 6 |
| final3_h_additive | MISO | uri | 3.63 | -2.43 | -3.06 | -6.47 | 5 |
| final3_h_additive | NYIS | uri | 2.64 | 2.93 | 0.00 | 0.00 | 6 |
| final3_h_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final3_h_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final3_h_additive | TVA | uri | 3.45 | 0.35 | -1.19 | -3.00 | 6 |
| final3_h_boosting | BPAT | uri | 3.02 | 0.67 | -0.94 | -4.88 | 6 |
| final3_h_boosting | CISO | uri | 2.48 | -1.79 | -2.03 | -4.80 | 6 |
| final3_h_boosting | DUK | uri | 3.71 | -2.23 | -2.39 | -5.90 | 6 |
| final3_h_boosting | ERCO | uri | 8.50 | -12.13 | -12.13 | -14.13 | 2 |
| final3_h_boosting | FPL | uri | 8.44 | -10.23 | -10.23 | -13.90 | 6 |
| final3_h_boosting | ISNE | uri | 3.92 | 2.28 | -0.13 | -0.71 | 6 |
| final3_h_boosting | MISO | uri | 2.32 | -2.46 | -2.59 | -5.34 | 5 |
| final3_h_boosting | NYIS | uri | 2.85 | 1.95 | -0.35 | -2.12 | 6 |
| final3_h_boosting | PJM | uri | 2.09 | -0.31 | -0.82 | -2.01 | 6 |
| final3_h_boosting | SWPP | uri | 5.35 | -3.53 | -4.41 | -10.11 | 4 |
| final3_h_boosting | TVA | uri | 3.19 | -0.94 | -1.79 | -4.74 | 6 |
| final3_h_ensemble | BPAT | uri | 2.60 | 0.02 | -0.76 | -3.84 | 6 |
| final3_h_ensemble | CISO | uri | 1.96 | -0.49 | -0.95 | -2.12 | 6 |
| final3_h_ensemble | DUK | uri | 3.58 | -2.50 | -2.50 | -6.45 | 6 |
| final3_h_ensemble | ERCO | uri | 5.56 | -7.59 | -7.59 | -8.94 | 2 |
| final3_h_ensemble | FPL | uri | 10.26 | -13.55 | -13.55 | -16.46 | 6 |
| final3_h_ensemble | ISNE | uri | 2.51 | 0.95 | -0.30 | -1.63 | 6 |
| final3_h_ensemble | MISO | uri | 3.64 | -3.42 | -3.43 | -6.95 | 5 |
| final3_h_ensemble | NYIS | uri | 2.27 | 2.43 | -0.06 | -0.34 | 6 |
| final3_h_ensemble | PJM | uri | 2.44 | 1.25 | -0.48 | -2.86 | 6 |
| final3_h_ensemble | SWPP | uri | 6.21 | -1.42 | -3.67 | -7.83 | 4 |
| final3_h_ensemble | TVA | uri | 3.32 | -0.42 | -1.54 | -3.54 | 6 |
| final3_h_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final3_h_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final3_h_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final3_h_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final3_h_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final3_h_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final3_h_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final3_h_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final3_h_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final3_h_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final3_h_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| h_boosting | BPAT | uri | 3.02 | 0.67 | -0.94 | -4.88 | 6 |
| h_boosting | CISO | uri | 2.48 | -1.79 | -2.03 | -4.80 | 6 |
| h_boosting | DUK | uri | 3.71 | -2.23 | -2.39 | -5.90 | 6 |
| h_boosting | ERCO | uri | 8.50 | -12.13 | -12.13 | -14.13 | 2 |
| h_boosting | FPL | uri | 8.44 | -10.23 | -10.23 | -13.90 | 6 |
| h_boosting | ISNE | uri | 3.92 | 2.28 | -0.13 | -0.71 | 6 |
| h_boosting | MISO | uri | 2.32 | -2.46 | -2.59 | -5.34 | 5 |
| h_boosting | NYIS | uri | 2.85 | 1.95 | -0.35 | -2.12 | 6 |
| h_boosting | PJM | uri | 2.09 | -0.31 | -0.82 | -2.01 | 6 |
| h_boosting | SWPP | uri | 5.35 | -3.53 | -4.41 | -10.11 | 4 |
| h_boosting | TVA | uri | 3.19 | -0.94 | -1.79 | -4.74 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | CISO | elliott | 3.38 | 1.96 | -0.88 | -4.40 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final3_h | BPAT | elliott | 3.09 | -1.87 | -2.32 | -5.65 | 5 |
| final3_h | CISO | elliott | 3.60 | 2.96 | -0.46 | -2.28 | 5 |
| final3_h | DUK | elliott | 3.09 | -1.17 | -1.42 | -3.96 | 4 |
| final3_h | ERCO | elliott | 5.75 | -2.77 | -3.91 | -7.91 | 5 |
| final3_h | FPL | elliott | 6.40 | -7.84 | -7.84 | -12.40 | 5 |
| final3_h | ISNE | elliott | 3.54 | 2.56 | -0.68 | -2.28 | 5 |
| final3_h | MISO | elliott | 3.51 | -2.52 | -3.21 | -7.45 | 5 |
| final3_h | NYIS | elliott | 2.84 | -0.85 | -1.66 | -3.68 | 5 |
| final3_h | PJM | elliott | 4.62 | -4.42 | -4.42 | -9.57 | 5 |
| final3_h | SWPP | elliott | 4.32 | 0.36 | -2.06 | -6.11 | 5 |
| final3_h | TVA | elliott | 5.16 | 4.23 | 0.00 | 0.00 | 3 |
| final3_h_additive | BPAT | elliott | 3.64 | -1.20 | -2.01 | -4.25 | 5 |
| final3_h_additive | CISO | elliott | 3.47 | 4.03 | -0.24 | -1.21 | 5 |
| final3_h_additive | DUK | elliott | 4.52 | -3.26 | -3.26 | -5.10 | 4 |
| final3_h_additive | ERCO | elliott | 7.87 | -5.54 | -6.11 | -14.39 | 5 |
| final3_h_additive | FPL | elliott | 10.99 | -2.80 | -6.82 | -18.07 | 5 |
| final3_h_additive | ISNE | elliott | 3.77 | 2.15 | -0.94 | -2.69 | 5 |
| final3_h_additive | MISO | elliott | 3.32 | -3.01 | -3.33 | -6.85 | 5 |
| final3_h_additive | NYIS | elliott | 3.06 | -0.88 | -1.90 | -4.52 | 5 |
| final3_h_additive | PJM | elliott | 3.54 | -0.27 | -1.00 | -4.98 | 5 |
| final3_h_additive | SWPP | elliott | 3.13 | -2.41 | -2.70 | -5.88 | 5 |
| final3_h_additive | TVA | elliott | 6.00 | 3.14 | -0.19 | -0.57 | 3 |
| final3_h_boosting | BPAT | elliott | 4.31 | -4.47 | -4.63 | -10.92 | 5 |
| final3_h_boosting | CISO | elliott | 4.05 | 1.78 | -0.93 | -4.24 | 5 |
| final3_h_boosting | DUK | elliott | 4.61 | -3.06 | -3.06 | -6.88 | 4 |
| final3_h_boosting | ERCO | elliott | 7.14 | -9.31 | -9.31 | -19.98 | 5 |
| final3_h_boosting | FPL | elliott | 8.80 | -14.67 | -14.67 | -20.48 | 5 |
| final3_h_boosting | ISNE | elliott | 3.75 | 3.12 | -0.14 | -0.69 | 5 |
| final3_h_boosting | MISO | elliott | 3.53 | -1.28 | -2.27 | -4.18 | 5 |
| final3_h_boosting | NYIS | elliott | 3.13 | 0.26 | -0.90 | -3.64 | 5 |
| final3_h_boosting | PJM | elliott | 5.00 | -2.32 | -3.08 | -6.22 | 5 |
| final3_h_boosting | SWPP | elliott | 5.72 | -1.57 | -4.02 | -12.13 | 5 |
| final3_h_boosting | TVA | elliott | 6.28 | 1.24 | -0.93 | -2.78 | 3 |
| final3_h_ensemble | BPAT | elliott | 3.62 | -2.94 | -3.27 | -7.95 | 5 |
| final3_h_ensemble | CISO | elliott | 3.50 | 3.39 | -0.44 | -2.19 | 5 |
| final3_h_ensemble | DUK | elliott | 3.70 | -3.87 | -3.87 | -4.85 | 4 |
| final3_h_ensemble | ERCO | elliott | 6.05 | -5.82 | -6.16 | -11.45 | 5 |
| final3_h_ensemble | FPL | elliott | 7.35 | -9.24 | -9.24 | -12.40 | 5 |
| final3_h_ensemble | ISNE | elliott | 3.54 | 2.95 | -0.51 | -1.85 | 5 |
| final3_h_ensemble | MISO | elliott | 3.40 | -2.99 | -3.39 | -7.30 | 5 |
| final3_h_ensemble | NYIS | elliott | 2.87 | -0.71 | -1.70 | -3.55 | 5 |
| final3_h_ensemble | PJM | elliott | 4.32 | -3.58 | -3.77 | -9.19 | 5 |
| final3_h_ensemble | SWPP | elliott | 3.74 | -2.51 | -3.30 | -8.59 | 5 |
| final3_h_ensemble | TVA | elliott | 5.40 | 2.46 | -0.94 | -1.45 | 3 |
| final3_h_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final3_h_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final3_h_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final3_h_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final3_h_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final3_h_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final3_h_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final3_h_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final3_h_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final3_h_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final3_h_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |
| h_boosting | BPAT | elliott | 4.31 | -4.47 | -4.63 | -10.92 | 5 |
| h_boosting | CISO | elliott | 4.05 | 1.78 | -0.93 | -4.24 | 5 |
| h_boosting | DUK | elliott | 4.61 | -3.06 | -3.06 | -6.88 | 4 |
| h_boosting | ERCO | elliott | 7.14 | -9.31 | -9.31 | -19.98 | 5 |
| h_boosting | FPL | elliott | 8.80 | -14.67 | -14.67 | -20.48 | 5 |
| h_boosting | ISNE | elliott | 3.75 | 3.12 | -0.14 | -0.69 | 5 |
| h_boosting | MISO | elliott | 3.53 | -1.28 | -2.27 | -4.18 | 5 |
| h_boosting | NYIS | elliott | 3.13 | 0.26 | -0.90 | -3.64 | 5 |
| h_boosting | PJM | elliott | 5.00 | -2.32 | -3.08 | -6.22 | 5 |
| h_boosting | SWPP | elliott | 5.72 | -1.57 | -4.02 | -12.13 | 5 |
| h_boosting | TVA | elliott | 6.28 | 1.24 | -0.93 | -2.78 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | final3_h | eve | 3.32 | 0.80 | -1.45 | 0.44 | 265 |
| 7 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 11 | final3_h_ensemble | eve | 3.40 | -0.54 | -2.12 | 0.48 | 265 |
| 9 | final3_h_additive | eve | 3.62 | -0.28 | -2.15 | 0.45 | 265 |
| 10 | final3_h_boosting | eve | 3.77 | -0.12 | -2.03 | 0.38 | 265 |
| 13 | h_boosting | eve | 3.77 | -0.12 | -2.03 | 0.38 | 265 |
| 12 | final3_h_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final3_h | special | 3.34 | -0.65 | -2.13 | 0.54 | 267 |
| 4 | final3_h_ensemble | special | 3.52 | -1.98 | -3.05 | 0.54 | 267 |
| 2 | final3_h_additive | special | 3.67 | -2.02 | -3.12 | 0.49 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final3_h_boosting | special | 3.83 | -1.57 | -2.79 | 0.46 | 267 |
| 6 | h_boosting | special | 3.83 | -1.57 | -2.79 | 0.46 | 267 |
| 5 | final3_h_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_h | all | 0.385 | 1.310 | 0.391 | 0.889 | 11.534 | 0.891 | 7815 |
| final3_h | events | 0.451 | 1.905 | 0.662 | 0.764 | 11.964 | 0.804 | 107 |
| final3_h | cold_mornings | 0.452 | 1.656 | 0.528 | 0.832 | 12.859 | 0.821 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 15434 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 15433 | DUK | 2022-12-24 | final3_h | 8.43 | -9.99 | -9.99 |
| 15429 | DUK | 2022-12-24 | final3_h_additive | 7.22 | -13.03 | -13.03 |
| 15430 | DUK | 2022-12-24 | final3_h_boosting | 9.96 | -18.19 | -18.19 |
| 15432 | DUK | 2022-12-24 | final3_h_ensemble | 8.73 | -13.78 | -13.78 |
| 15431 | DUK | 2022-12-24 | final3_h_recency | 9.27 | -9.99 | -9.99 |
| 15428 | DUK | 2022-12-24 | h_boosting | 9.96 | -18.19 | -18.19 |
| 16008 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 16007 | ERCO | 2021-02-17 | final3_h | 32.66 | 25.83 | 0.00 |
| 16003 | ERCO | 2021-02-17 | final3_h_additive | 32.00 | 28.88 | 0.00 |
| 16004 | ERCO | 2021-02-17 | final3_h_boosting | 29.50 | 23.26 | 0.00 |
| 16006 | ERCO | 2021-02-17 | final3_h_ensemble | 33.42 | 28.75 | 0.00 |
| 16005 | ERCO | 2021-02-17 | final3_h_recency | 41.20 | 36.68 | 0.00 |
| 16002 | ERCO | 2021-02-17 | h_boosting | 29.50 | 23.26 | 0.00 |
| 16015 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 16014 | ERCO | 2021-02-18 | final3_h | 5.12 | 3.77 | 0.00 |
| 16010 | ERCO | 2021-02-18 | final3_h_additive | 13.29 | 11.84 | 0.00 |
| 16011 | ERCO | 2021-02-18 | final3_h_boosting | 2.92 | -4.68 | -4.68 |
| 16013 | ERCO | 2021-02-18 | final3_h_ensemble | 5.84 | 2.86 | 0.00 |
| 16012 | ERCO | 2021-02-18 | final3_h_recency | 5.36 | 2.19 | 0.00 |
| 16009 | ERCO | 2021-02-18 | h_boosting | 2.92 | -4.68 | -4.68 |
| 31114 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 31113 | MISO | 2021-02-16 | final3_h | 2.06 | 1.88 | 0.00 |
| 31109 | MISO | 2021-02-16 | final3_h_additive | 2.38 | 2.18 | 0.00 |
| 31110 | MISO | 2021-02-16 | final3_h_boosting | 3.03 | 1.40 | 0.00 |
| 31112 | MISO | 2021-02-16 | final3_h_ensemble | 2.08 | 0.75 | 0.00 |
| 31111 | MISO | 2021-02-16 | final3_h_recency | 3.61 | -2.07 | -2.07 |
| 31108 | MISO | 2021-02-16 | h_boosting | 3.03 | 1.40 | 0.00 |
| 46654 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 46653 | SWPP | 2021-02-15 | final3_h | 2.95 | -2.66 | -2.66 |
| 46649 | SWPP | 2021-02-15 | final3_h_additive | 2.24 | 1.30 | 0.00 |
| 46650 | SWPP | 2021-02-15 | final3_h_boosting | 6.23 | -8.01 | -8.01 |
| 46652 | SWPP | 2021-02-15 | final3_h_ensemble | 3.06 | -3.85 | -3.85 |
| 46651 | SWPP | 2021-02-15 | final3_h_recency | 4.81 | -5.28 | -5.28 |
| 46648 | SWPP | 2021-02-15 | h_boosting | 6.23 | -8.01 | -8.01 |
| 46661 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 46660 | SWPP | 2021-02-16 | final3_h | 3.91 | 0.07 | 0.00 |
| 46656 | SWPP | 2021-02-16 | final3_h_additive | 7.74 | 3.67 | 0.00 |
| 46657 | SWPP | 2021-02-16 | final3_h_boosting | 3.13 | -5.72 | -5.72 |
| 46659 | SWPP | 2021-02-16 | final3_h_ensemble | 3.89 | -0.62 | -0.62 |
| 46658 | SWPP | 2021-02-16 | final3_h_recency | 2.57 | -0.10 | -0.10 |
| 46655 | SWPP | 2021-02-16 | h_boosting | 3.13 | -5.72 | -5.72 |
| 56391 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 56390 | TVA | 2022-12-23 | final3_h | 8.92 | -11.11 | -11.11 |
| 56386 | TVA | 2022-12-23 | final3_h_additive | 7.33 | -3.19 | -3.19 |
| 56387 | TVA | 2022-12-23 | final3_h_boosting | 14.01 | -15.52 | -15.52 |
| 56389 | TVA | 2022-12-23 | final3_h_ensemble | 8.37 | -9.44 | -9.44 |
| 56388 | TVA | 2022-12-23 | final3_h_recency | 11.83 | -10.22 | -10.22 |
| 56385 | TVA | 2022-12-23 | h_boosting | 14.01 | -15.52 | -15.52 |
| 56398 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 56397 | TVA | 2022-12-24 | final3_h | 6.00 | -11.72 | -11.72 |
| 56393 | TVA | 2022-12-24 | final3_h_additive | 3.82 | -9.06 | -9.06 |
| 56394 | TVA | 2022-12-24 | final3_h_boosting | 7.32 | -15.52 | -15.52 |
| 56396 | TVA | 2022-12-24 | final3_h_ensemble | 5.87 | -11.88 | -11.88 |
| 56395 | TVA | 2022-12-24 | final3_h_recency | 7.21 | -11.36 | -11.36 |
| 56392 | TVA | 2022-12-24 | h_boosting | 7.32 | -15.52 | -15.52 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3_h | BPAT | mape | 7.534 | 0.000 | 746 |
| final3_h | CISO | mape | 0.868 | 0.385 | 719 |
| final3_h | DUK | mape | 5.289 | 0.000 | 746 |
| final3_h | ERCO | mape | -0.369 | 0.712 | 742 |
| final3_h | FPL | mape | -3.084 | 0.002 | 665 |
| final3_h | ISNE | mape | 13.635 | 0.000 | 748 |
| final3_h | MISO | mape | -10.674 | 0.000 | 738 |
| final3_h | NYIS | mape | -6.554 | 0.000 | 748 |
| final3_h | PJM | mape | -5.934 | 0.000 | 734 |
| final3_h | SWPP | mape | -18.623 | 0.000 | 741 |
| final3_h | TVA | mape | 10.970 | 0.000 | 729 |
| final3_h_additive | BPAT | mape | 11.120 | 0.000 | 746 |
| final3_h_additive | CISO | mape | 15.689 | 0.000 | 719 |
| final3_h_additive | DUK | mape | 7.194 | 0.000 | 746 |
| final3_h_additive | ERCO | mape | 12.990 | 0.000 | 742 |
| final3_h_additive | FPL | mape | 17.832 | 0.000 | 665 |
| final3_h_additive | ISNE | mape | 19.445 | 0.000 | 748 |
| final3_h_additive | MISO | mape | -5.134 | 0.000 | 738 |
| final3_h_additive | NYIS | mape | -1.981 | 0.048 | 748 |
| final3_h_additive | PJM | mape | 3.225 | 0.001 | 734 |
| final3_h_additive | SWPP | mape | -15.827 | 0.000 | 741 |
| final3_h_additive | TVA | mape | 15.024 | 0.000 | 729 |
| final3_h_boosting | BPAT | mape | 11.635 | 0.000 | 746 |
| final3_h_boosting | CISO | mape | 7.964 | 0.000 | 719 |
| final3_h_boosting | DUK | mape | 7.113 | 0.000 | 746 |
| final3_h_boosting | ERCO | mape | 4.778 | 0.000 | 742 |
| final3_h_boosting | FPL | mape | 19.065 | 0.000 | 665 |
| final3_h_boosting | ISNE | mape | 17.090 | 0.000 | 748 |
| final3_h_boosting | MISO | mape | -6.295 | 0.000 | 738 |
| final3_h_boosting | NYIS | mape | -1.698 | 0.089 | 748 |
| final3_h_boosting | PJM | mape | 3.537 | 0.000 | 734 |
| final3_h_boosting | SWPP | mape | -13.466 | 0.000 | 741 |
| final3_h_boosting | TVA | mape | 13.792 | 0.000 | 729 |
| final3_h_ensemble | BPAT | mape | 8.317 | 0.000 | 746 |
| final3_h_ensemble | CISO | mape | 11.871 | 0.000 | 719 |
| final3_h_ensemble | DUK | mape | 5.251 | 0.000 | 746 |
| final3_h_ensemble | ERCO | mape | 6.168 | 0.000 | 742 |
| final3_h_ensemble | FPL | mape | 19.350 | 0.000 | 665 |
| final3_h_ensemble | ISNE | mape | 17.496 | 0.000 | 748 |
| final3_h_ensemble | MISO | mape | -7.763 | 0.000 | 738 |
| final3_h_ensemble | NYIS | mape | -5.806 | 0.000 | 748 |
| final3_h_ensemble | PJM | mape | -0.576 | 0.565 | 734 |
| final3_h_ensemble | SWPP | mape | -18.793 | 0.000 | 741 |
| final3_h_ensemble | TVA | mape | 12.054 | 0.000 | 729 |
| final3_h_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final3_h_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final3_h_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final3_h_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final3_h_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final3_h_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final3_h_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final3_h_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final3_h_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final3_h_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final3_h_recency | TVA | mape | 20.369 | 0.000 | 729 |
| h_boosting | BPAT | mape | 11.635 | 0.000 | 746 |
| h_boosting | CISO | mape | 7.964 | 0.000 | 719 |
| h_boosting | DUK | mape | 7.113 | 0.000 | 746 |
| h_boosting | ERCO | mape | 4.778 | 0.000 | 742 |
| h_boosting | FPL | mape | 19.065 | 0.000 | 665 |
| h_boosting | ISNE | mape | 17.090 | 0.000 | 748 |
| h_boosting | MISO | mape | -6.295 | 0.000 | 738 |
| h_boosting | NYIS | mape | -1.698 | 0.089 | 748 |
| h_boosting | PJM | mape | 3.537 | 0.000 | 734 |
| h_boosting | SWPP | mape | -13.466 | 0.000 | 741 |
| h_boosting | TVA | mape | 13.792 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final3_h | 0.987 |
| final3_h_additive | 0.965 |
| final3_h_boosting | 0.987 |
| final3_h_ensemble | 0.987 |
| final3_h_recency | 0.987 |
| h_boosting | 0.987 |
