# Phase J: the hot and cold peak quantile and cold-day training weights

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final5` is the phase I recipe; `final5b` reads the point at the 70th percentile around the peak also when the forecast maximum is in the coldest decile of known maxima or in the hottest decile; `final5c` fits the additive and boosting members with training weights that grow with the distance of the day's observed minimum below the coldest decile of the training days. Compare on the winter events, the coldest mornings and the year.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | 2.39 | 2.07 | 0.05 | -1.28 | 1.24 | 0.57 | 0.30 | -46.49 | 8056 | 11.00 |
| final5c | 2.39 | 2.07 | 0.05 | -1.27 | 1.22 | 0.57 | 0.30 | -46.61 | 8056 | 11.00 |
| final5b | 2.40 | 2.08 | 0.20 | -1.22 | 1.24 | 0.56 | 0.31 | -46.49 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final5_ensemble | 2.74 | 2.42 | -1.39 | -2.19 | 1.28 | 0.50 | 0.23 | -50.92 | 8056 | 11.00 |
| final5b_ensemble | 2.74 | 2.42 | -1.39 | -2.19 | 1.28 | 0.50 | 0.23 | -50.92 | 8056 | 11.00 |
| final5c_ensemble | 2.75 | 2.42 | -1.39 | -2.19 | 1.26 | 0.49 | 0.23 | -51.10 | 8056 | 11.00 |
| final5_boosting | 2.83 | 2.50 | -1.00 | -2.01 | 1.40 | 0.46 | 0.25 | -51.31 | 8056 | 11.00 |
| final5b_boosting | 2.83 | 2.50 | -1.00 | -2.01 | 1.40 | 0.46 | 0.25 | -51.31 | 8056 | 11.00 |
| final5c_boosting | 2.85 | 2.53 | -0.98 | -2.01 | 1.42 | 0.46 | 0.25 | -51.72 | 8056 | 11.00 |
| final5_additive | 2.99 | 2.65 | -1.60 | -2.46 | 1.31 | 0.44 | 0.21 | -49.25 | 8056 | 11.00 |
| final5b_additive | 2.99 | 2.65 | -1.60 | -2.46 | 1.31 | 0.44 | 0.21 | -49.25 | 8056 | 11.00 |
| final5c_additive | 2.99 | 2.65 | -1.60 | -2.46 | 1.31 | 0.44 | 0.21 | -49.35 | 8056 | 11.00 |
| final5_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |
| final5b_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |
| final5c_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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
| final5 | BPAT | 2.45 | 2.13 | -0.37 | -1.43 | 1.71 | -17.95 | 0.38 | 0.25 | 746 | 6536.52 |
| final5 | CISO | 2.44 | 2.14 | 0.45 | -1.07 | 0.33 | -12.72 | 0.50 | 0.26 | 719 | 25193.76 |
| final5 | DUK | 3.18 | 2.88 | 0.05 | -1.74 | 1.37 | -14.98 | 0.41 | 0.31 | 746 | 12143.29 |
| final5 | ERCO | 2.60 | 2.17 | 0.03 | -1.40 | 1.05 | -14.08 | 0.49 | 0.29 | 742 | 46834.59 |
| final5 | FPL | 3.63 | 3.19 | -0.77 | -2.55 | 1.04 | -46.49 | 0.60 | 0.65 | 665 | 15346.05 |
| final5 | ISNE | 3.19 | 2.80 | 0.37 | -1.28 | 0.51 | -15.57 | 0.35 | 0.21 | 748 | 13403.92 |
| final5 | MISO | 2.01 | 1.75 | 0.13 | -0.99 | 1.62 | -7.49 | 0.63 | 0.07 | 738 | 73700.16 |
| final5 | NYIS | 2.25 | 1.96 | 0.02 | -1.27 | 0.55 | -12.87 | 0.61 | 0.72 | 748 | 17415.28 |
| final5 | PJM | 2.15 | 1.88 | 0.02 | -1.20 | 1.44 | -10.65 | 0.61 | 0.43 | 734 | 92076.14 |
| final5 | SWPP | 2.17 | 1.82 | -0.18 | -1.28 | 1.41 | -20.03 | 0.75 | 0.11 | 741 | 31382.01 |
| final5 | TVA | 2.83 | 2.46 | 0.40 | -1.38 | 1.37 | -11.13 | 0.33 | 0.33 | 729 | 18581.23 |
| final5_additive | BPAT | 2.67 | 2.36 | -0.73 | -1.68 | 1.79 | -16.90 | 0.31 | 0.23 | 746 | 6536.52 |
| final5_additive | CISO | 3.60 | 3.04 | -2.81 | -3.70 | 0.40 | -17.92 | 0.29 | 0.13 | 719 | 25193.76 |
| final5_additive | DUK | 3.33 | 2.95 | -1.57 | -2.69 | 1.36 | -16.17 | 0.39 | 0.24 | 746 | 12143.29 |
| final5_additive | ERCO | 3.65 | 3.31 | -2.63 | -3.32 | 1.07 | -16.29 | 0.30 | 0.14 | 742 | 46834.59 |
| final5_additive | FPL | 6.15 | 5.77 | -6.17 | -6.69 | 1.08 | -49.25 | 0.26 | 0.25 | 665 | 15346.05 |
| final5_additive | ISNE | 3.66 | 3.30 | -1.16 | -2.39 | 0.51 | -21.27 | 0.25 | 0.16 | 748 | 13403.92 |
| final5_additive | MISO | 2.29 | 2.03 | -1.25 | -1.84 | 1.59 | -8.60 | 0.55 | 0.05 | 738 | 73700.16 |
| final5_additive | NYIS | 2.54 | 2.22 | -1.04 | -2.04 | 0.54 | -15.21 | 0.56 | 0.59 | 748 | 17415.28 |
| final5_additive | PJM | 2.64 | 2.33 | -0.65 | -1.72 | 1.64 | -11.72 | 0.47 | 0.38 | 734 | 92076.14 |
| final5_additive | SWPP | 2.38 | 1.98 | -1.20 | -1.97 | 1.46 | -21.10 | 0.70 | 0.08 | 741 | 31382.01 |
| final5_additive | TVA | 3.20 | 2.83 | -1.56 | -2.57 | 1.47 | -15.27 | 0.27 | 0.22 | 729 | 18581.23 |
| final5_boosting | BPAT | 2.64 | 2.38 | -0.57 | -1.65 | 1.95 | -17.45 | 0.30 | 0.24 | 746 | 6536.52 |
| final5_boosting | CISO | 2.89 | 2.58 | -1.99 | -2.57 | 0.42 | -16.56 | 0.37 | 0.16 | 719 | 25193.76 |
| final5_boosting | DUK | 3.35 | 2.93 | -0.89 | -2.32 | 1.46 | -18.54 | 0.36 | 0.27 | 746 | 12143.29 |
| final5_boosting | ERCO | 2.96 | 2.56 | -2.35 | -2.94 | 1.28 | -19.79 | 0.38 | 0.17 | 742 | 46834.59 |
| final5_boosting | FPL | 6.07 | 5.69 | -6.47 | -6.84 | 1.28 | -51.31 | 0.21 | 0.27 | 665 | 15346.05 |
| final5_boosting | ISNE | 3.45 | 3.12 | -0.27 | -1.57 | 0.54 | -17.19 | 0.30 | 0.19 | 748 | 13403.92 |
| final5_boosting | MISO | 2.25 | 1.96 | -0.50 | -1.37 | 1.61 | -9.73 | 0.57 | 0.06 | 738 | 73700.16 |
| final5_boosting | NYIS | 2.52 | 2.22 | -0.17 | -1.32 | 0.69 | -10.62 | 0.54 | 0.72 | 748 | 17415.28 |
| final5_boosting | PJM | 2.64 | 2.39 | 0.13 | -1.29 | 1.71 | -11.82 | 0.45 | 0.44 | 734 | 92076.14 |
| final5_boosting | SWPP | 2.49 | 2.10 | -1.14 | -2.08 | 1.52 | -29.02 | 0.70 | 0.07 | 741 | 31382.01 |
| final5_boosting | TVA | 3.08 | 2.61 | -0.58 | -1.88 | 1.59 | -13.00 | 0.29 | 0.27 | 729 | 18581.23 |
| final5_ensemble | BPAT | 2.48 | 2.23 | -0.84 | -1.68 | 1.73 | -17.80 | 0.37 | 0.23 | 746 | 6536.52 |
| final5_ensemble | CISO | 3.23 | 2.74 | -2.79 | -3.29 | 0.36 | -17.07 | 0.35 | 0.12 | 719 | 25193.76 |
| final5_ensemble | DUK | 3.19 | 2.79 | -1.03 | -2.34 | 1.38 | -14.72 | 0.42 | 0.25 | 746 | 12143.29 |
| final5_ensemble | ERCO | 3.08 | 2.68 | -2.53 | -3.05 | 1.06 | -14.56 | 0.38 | 0.16 | 742 | 46834.59 |
| final5_ensemble | FPL | 6.34 | 5.97 | -7.00 | -7.32 | 1.06 | -50.92 | 0.22 | 0.23 | 665 | 15346.05 |
| final5_ensemble | ISNE | 3.40 | 3.08 | -1.19 | -2.12 | 0.50 | -17.57 | 0.27 | 0.15 | 748 | 13403.92 |
| final5_ensemble | MISO | 2.14 | 1.87 | -0.96 | -1.56 | 1.67 | -8.12 | 0.60 | 0.05 | 738 | 73700.16 |
| final5_ensemble | NYIS | 2.30 | 2.01 | -0.56 | -1.53 | 0.54 | -13.55 | 0.59 | 0.69 | 748 | 17415.28 |
| final5_ensemble | PJM | 2.43 | 2.20 | -0.36 | -1.43 | 1.52 | -10.67 | 0.54 | 0.42 | 734 | 92076.14 |
| final5_ensemble | SWPP | 2.16 | 1.77 | -0.88 | -1.69 | 1.37 | -20.05 | 0.75 | 0.09 | 741 | 31382.01 |
| final5_ensemble | TVA | 2.94 | 2.55 | -1.06 | -2.13 | 1.37 | -13.91 | 0.31 | 0.25 | 729 | 18581.23 |
| final5_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final5_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final5_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final5_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final5_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final5_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final5_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final5_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final5_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final5_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final5_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |
| final5b | BPAT | 2.46 | 2.13 | -0.24 | -1.36 | 1.70 | -17.95 | 0.38 | 0.26 | 746 | 6536.52 |
| final5b | CISO | 2.45 | 2.14 | 0.65 | -0.99 | 0.36 | -12.09 | 0.50 | 0.28 | 719 | 25193.76 |
| final5b | DUK | 3.20 | 2.92 | 0.26 | -1.67 | 1.36 | -14.98 | 0.40 | 0.32 | 746 | 12143.29 |
| final5b | ERCO | 2.62 | 2.18 | 0.22 | -1.34 | 1.04 | -14.08 | 0.48 | 0.29 | 742 | 46834.59 |
| final5b | FPL | 3.64 | 3.22 | -0.55 | -2.46 | 1.03 | -46.49 | 0.60 | 0.67 | 665 | 15346.05 |
| final5b | ISNE | 3.20 | 2.83 | 0.58 | -1.20 | 0.50 | -15.57 | 0.35 | 0.21 | 748 | 13403.92 |
| final5b | MISO | 2.02 | 1.76 | 0.24 | -0.95 | 1.59 | -7.49 | 0.62 | 0.07 | 738 | 73700.16 |
| final5b | NYIS | 2.27 | 1.98 | 0.21 | -1.20 | 0.57 | -12.87 | 0.60 | 0.74 | 748 | 17415.28 |
| final5b | PJM | 2.16 | 1.90 | 0.16 | -1.15 | 1.43 | -10.65 | 0.60 | 0.44 | 734 | 92076.14 |
| final5b | SWPP | 2.17 | 1.84 | -0.06 | -1.22 | 1.42 | -20.03 | 0.75 | 0.11 | 741 | 31382.01 |
| final5b | TVA | 2.85 | 2.47 | 0.57 | -1.34 | 1.37 | -11.13 | 0.33 | 0.34 | 729 | 18581.23 |
| final5b_additive | BPAT | 2.67 | 2.36 | -0.73 | -1.68 | 1.79 | -16.90 | 0.31 | 0.23 | 746 | 6536.52 |
| final5b_additive | CISO | 3.60 | 3.04 | -2.81 | -3.70 | 0.40 | -17.92 | 0.29 | 0.13 | 719 | 25193.76 |
| final5b_additive | DUK | 3.33 | 2.95 | -1.57 | -2.69 | 1.36 | -16.17 | 0.39 | 0.24 | 746 | 12143.29 |
| final5b_additive | ERCO | 3.65 | 3.31 | -2.63 | -3.32 | 1.07 | -16.29 | 0.30 | 0.14 | 742 | 46834.59 |
| final5b_additive | FPL | 6.15 | 5.77 | -6.17 | -6.69 | 1.08 | -49.25 | 0.26 | 0.25 | 665 | 15346.05 |
| final5b_additive | ISNE | 3.66 | 3.30 | -1.16 | -2.39 | 0.51 | -21.27 | 0.25 | 0.16 | 748 | 13403.92 |
| final5b_additive | MISO | 2.29 | 2.03 | -1.25 | -1.84 | 1.59 | -8.60 | 0.55 | 0.05 | 738 | 73700.16 |
| final5b_additive | NYIS | 2.54 | 2.22 | -1.04 | -2.04 | 0.54 | -15.21 | 0.56 | 0.59 | 748 | 17415.28 |
| final5b_additive | PJM | 2.64 | 2.33 | -0.65 | -1.72 | 1.64 | -11.72 | 0.47 | 0.38 | 734 | 92076.14 |
| final5b_additive | SWPP | 2.38 | 1.98 | -1.20 | -1.97 | 1.46 | -21.10 | 0.70 | 0.08 | 741 | 31382.01 |
| final5b_additive | TVA | 3.20 | 2.83 | -1.56 | -2.57 | 1.47 | -15.27 | 0.27 | 0.22 | 729 | 18581.23 |
| final5b_boosting | BPAT | 2.64 | 2.38 | -0.57 | -1.65 | 1.95 | -17.45 | 0.30 | 0.24 | 746 | 6536.52 |
| final5b_boosting | CISO | 2.89 | 2.58 | -1.99 | -2.57 | 0.42 | -16.56 | 0.37 | 0.16 | 719 | 25193.76 |
| final5b_boosting | DUK | 3.35 | 2.93 | -0.89 | -2.32 | 1.46 | -18.54 | 0.36 | 0.27 | 746 | 12143.29 |
| final5b_boosting | ERCO | 2.96 | 2.56 | -2.35 | -2.94 | 1.28 | -19.79 | 0.38 | 0.17 | 742 | 46834.59 |
| final5b_boosting | FPL | 6.07 | 5.69 | -6.47 | -6.84 | 1.28 | -51.31 | 0.21 | 0.27 | 665 | 15346.05 |
| final5b_boosting | ISNE | 3.45 | 3.12 | -0.27 | -1.57 | 0.54 | -17.19 | 0.30 | 0.19 | 748 | 13403.92 |
| final5b_boosting | MISO | 2.25 | 1.96 | -0.50 | -1.37 | 1.61 | -9.73 | 0.57 | 0.06 | 738 | 73700.16 |
| final5b_boosting | NYIS | 2.52 | 2.22 | -0.17 | -1.32 | 0.69 | -10.62 | 0.54 | 0.72 | 748 | 17415.28 |
| final5b_boosting | PJM | 2.64 | 2.39 | 0.13 | -1.29 | 1.71 | -11.82 | 0.45 | 0.44 | 734 | 92076.14 |
| final5b_boosting | SWPP | 2.49 | 2.10 | -1.14 | -2.08 | 1.52 | -29.02 | 0.70 | 0.07 | 741 | 31382.01 |
| final5b_boosting | TVA | 3.08 | 2.61 | -0.58 | -1.88 | 1.59 | -13.00 | 0.29 | 0.27 | 729 | 18581.23 |
| final5b_ensemble | BPAT | 2.48 | 2.23 | -0.84 | -1.68 | 1.73 | -17.80 | 0.37 | 0.23 | 746 | 6536.52 |
| final5b_ensemble | CISO | 3.23 | 2.74 | -2.79 | -3.29 | 0.36 | -17.07 | 0.35 | 0.12 | 719 | 25193.76 |
| final5b_ensemble | DUK | 3.19 | 2.79 | -1.03 | -2.34 | 1.38 | -14.72 | 0.42 | 0.25 | 746 | 12143.29 |
| final5b_ensemble | ERCO | 3.08 | 2.68 | -2.53 | -3.05 | 1.06 | -14.56 | 0.38 | 0.16 | 742 | 46834.59 |
| final5b_ensemble | FPL | 6.34 | 5.97 | -7.00 | -7.32 | 1.06 | -50.92 | 0.22 | 0.23 | 665 | 15346.05 |
| final5b_ensemble | ISNE | 3.40 | 3.08 | -1.19 | -2.12 | 0.50 | -17.57 | 0.27 | 0.15 | 748 | 13403.92 |
| final5b_ensemble | MISO | 2.14 | 1.87 | -0.96 | -1.56 | 1.67 | -8.12 | 0.60 | 0.05 | 738 | 73700.16 |
| final5b_ensemble | NYIS | 2.30 | 2.01 | -0.56 | -1.53 | 0.54 | -13.55 | 0.59 | 0.69 | 748 | 17415.28 |
| final5b_ensemble | PJM | 2.43 | 2.20 | -0.36 | -1.43 | 1.52 | -10.67 | 0.54 | 0.42 | 734 | 92076.14 |
| final5b_ensemble | SWPP | 2.16 | 1.77 | -0.88 | -1.69 | 1.37 | -20.05 | 0.75 | 0.09 | 741 | 31382.01 |
| final5b_ensemble | TVA | 2.94 | 2.55 | -1.06 | -2.13 | 1.37 | -13.91 | 0.31 | 0.25 | 729 | 18581.23 |
| final5b_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final5b_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final5b_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final5b_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final5b_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final5b_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final5b_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final5b_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final5b_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final5b_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final5b_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |
| final5c | BPAT | 2.46 | 2.13 | -0.37 | -1.42 | 1.74 | -17.62 | 0.37 | 0.25 | 746 | 6536.52 |
| final5c | CISO | 2.46 | 2.19 | 0.49 | -1.08 | 0.35 | -13.04 | 0.49 | 0.27 | 719 | 25193.76 |
| final5c | DUK | 3.19 | 2.83 | 0.06 | -1.74 | 1.39 | -15.52 | 0.40 | 0.31 | 746 | 12143.29 |
| final5c | ERCO | 2.61 | 2.18 | 0.02 | -1.39 | 1.00 | -14.11 | 0.49 | 0.28 | 742 | 46834.59 |
| final5c | FPL | 3.64 | 3.21 | -0.76 | -2.53 | 1.06 | -46.61 | 0.60 | 0.66 | 665 | 15346.05 |
| final5c | ISNE | 3.19 | 2.81 | 0.37 | -1.27 | 0.49 | -15.42 | 0.34 | 0.21 | 748 | 13403.92 |
| final5c | MISO | 2.01 | 1.72 | 0.16 | -0.97 | 1.59 | -10.19 | 0.63 | 0.07 | 738 | 73700.16 |
| final5c | NYIS | 2.25 | 1.95 | 0.01 | -1.28 | 0.56 | -13.90 | 0.61 | 0.72 | 748 | 17415.28 |
| final5c | PJM | 2.15 | 1.89 | 0.03 | -1.19 | 1.38 | -10.62 | 0.61 | 0.43 | 734 | 92076.14 |
| final5c | SWPP | 2.18 | 1.84 | -0.21 | -1.30 | 1.47 | -19.58 | 0.75 | 0.12 | 741 | 31382.01 |
| final5c | TVA | 2.84 | 2.46 | 0.37 | -1.41 | 1.29 | -12.53 | 0.33 | 0.33 | 729 | 18581.23 |
| final5c_additive | BPAT | 2.69 | 2.38 | -0.69 | -1.66 | 1.80 | -16.33 | 0.30 | 0.23 | 746 | 6536.52 |
| final5c_additive | CISO | 3.59 | 3.06 | -2.77 | -3.65 | 0.41 | -18.01 | 0.29 | 0.13 | 719 | 25193.76 |
| final5c_additive | DUK | 3.33 | 2.94 | -1.45 | -2.62 | 1.34 | -16.17 | 0.39 | 0.24 | 746 | 12143.29 |
| final5c_additive | ERCO | 3.67 | 3.31 | -2.66 | -3.36 | 1.08 | -16.44 | 0.29 | 0.14 | 742 | 46834.59 |
| final5c_additive | FPL | 6.26 | 5.87 | -6.39 | -6.89 | 1.07 | -49.35 | 0.26 | 0.25 | 665 | 15346.05 |
| final5c_additive | ISNE | 3.64 | 3.26 | -1.08 | -2.34 | 0.53 | -21.13 | 0.24 | 0.16 | 748 | 13403.92 |
| final5c_additive | MISO | 2.27 | 2.03 | -1.19 | -1.80 | 1.55 | -11.26 | 0.56 | 0.05 | 738 | 73700.16 |
| final5c_additive | NYIS | 2.52 | 2.22 | -0.89 | -1.95 | 0.55 | -14.89 | 0.57 | 0.61 | 748 | 17415.28 |
| final5c_additive | PJM | 2.66 | 2.30 | -0.70 | -1.76 | 1.63 | -11.51 | 0.45 | 0.38 | 734 | 92076.14 |
| final5c_additive | SWPP | 2.37 | 2.00 | -1.23 | -1.99 | 1.52 | -21.03 | 0.71 | 0.09 | 741 | 31382.01 |
| final5c_additive | TVA | 3.21 | 2.85 | -1.63 | -2.63 | 1.50 | -15.56 | 0.27 | 0.23 | 729 | 18581.23 |
| final5c_boosting | BPAT | 2.63 | 2.36 | -0.58 | -1.65 | 2.04 | -16.49 | 0.30 | 0.25 | 746 | 6536.52 |
| final5c_boosting | CISO | 2.92 | 2.64 | -1.99 | -2.59 | 0.43 | -16.52 | 0.37 | 0.15 | 719 | 25193.76 |
| final5c_boosting | DUK | 3.37 | 2.93 | -0.94 | -2.36 | 1.53 | -18.64 | 0.36 | 0.27 | 746 | 12143.29 |
| final5c_boosting | ERCO | 3.00 | 2.60 | -2.35 | -2.96 | 1.30 | -19.50 | 0.37 | 0.16 | 742 | 46834.59 |
| final5c_boosting | FPL | 6.02 | 5.66 | -6.28 | -6.69 | 1.29 | -51.72 | 0.22 | 0.28 | 665 | 15346.05 |
| final5c_boosting | ISNE | 3.43 | 3.09 | -0.26 | -1.54 | 0.60 | -16.66 | 0.29 | 0.19 | 748 | 13403.92 |
| final5c_boosting | MISO | 2.27 | 1.97 | -0.49 | -1.36 | 1.69 | -9.61 | 0.56 | 0.05 | 738 | 73700.16 |
| final5c_boosting | NYIS | 2.57 | 2.31 | -0.10 | -1.32 | 0.79 | -12.07 | 0.55 | 0.71 | 748 | 17415.28 |
| final5c_boosting | PJM | 2.65 | 2.42 | 0.18 | -1.27 | 1.67 | -11.31 | 0.46 | 0.44 | 734 | 92076.14 |
| final5c_boosting | SWPP | 2.53 | 2.12 | -1.19 | -2.12 | 1.57 | -31.08 | 0.71 | 0.08 | 741 | 31382.01 |
| final5c_boosting | TVA | 3.13 | 2.64 | -0.55 | -1.92 | 1.55 | -12.66 | 0.29 | 0.28 | 729 | 18581.23 |
| final5c_ensemble | BPAT | 2.48 | 2.23 | -0.84 | -1.68 | 1.79 | -17.32 | 0.37 | 0.24 | 746 | 6536.52 |
| final5c_ensemble | CISO | 3.24 | 2.75 | -2.77 | -3.29 | 0.36 | -17.08 | 0.34 | 0.12 | 719 | 25193.76 |
| final5c_ensemble | DUK | 3.20 | 2.79 | -1.01 | -2.33 | 1.37 | -15.08 | 0.42 | 0.25 | 746 | 12143.29 |
| final5c_ensemble | ERCO | 3.10 | 2.72 | -2.54 | -3.06 | 1.05 | -14.79 | 0.38 | 0.15 | 742 | 46834.59 |
| final5c_ensemble | FPL | 6.37 | 5.99 | -7.01 | -7.34 | 1.07 | -51.10 | 0.22 | 0.23 | 665 | 15346.05 |
| final5c_ensemble | ISNE | 3.38 | 3.14 | -1.16 | -2.10 | 0.50 | -17.31 | 0.26 | 0.15 | 748 | 13403.92 |
| final5c_ensemble | MISO | 2.13 | 1.86 | -0.93 | -1.54 | 1.59 | -9.66 | 0.61 | 0.05 | 738 | 73700.16 |
| final5c_ensemble | NYIS | 2.30 | 1.98 | -0.49 | -1.49 | 0.57 | -13.82 | 0.60 | 0.70 | 748 | 17415.28 |
| final5c_ensemble | PJM | 2.43 | 2.17 | -0.36 | -1.43 | 1.49 | -10.55 | 0.54 | 0.42 | 734 | 92076.14 |
| final5c_ensemble | SWPP | 2.17 | 1.77 | -0.91 | -1.71 | 1.39 | -19.41 | 0.74 | 0.09 | 741 | 31382.01 |
| final5c_ensemble | TVA | 2.95 | 2.55 | -1.08 | -2.16 | 1.39 | -13.83 | 0.31 | 0.25 | 729 | 18581.23 |
| final5c_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final5c_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final5c_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final5c_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final5c_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final5c_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final5c_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final5c_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final5c_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final5c_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final5c_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |

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
| final5 | BPAT | uri | 2.43 | -0.16 | -0.85 | -4.96 | 6 |
| final5 | CISO | uri | 2.00 | -0.68 | -1.17 | -2.56 | 6 |
| final5 | DUK | uri | 3.52 | -1.55 | -1.93 | -4.06 | 6 |
| final5 | ERCO | uri | 6.40 | -8.60 | -8.60 | -9.02 | 2 |
| final5 | FPL | uri | 8.30 | -7.40 | -7.40 | -10.30 | 6 |
| final5 | ISNE | uri | 2.53 | 1.62 | -0.09 | -0.43 | 6 |
| final5 | MISO | uri | 3.91 | -3.33 | -3.56 | -6.83 | 5 |
| final5 | NYIS | uri | 2.11 | 2.17 | -0.14 | -0.86 | 6 |
| final5 | PJM | uri | 1.90 | 0.26 | -0.68 | -2.76 | 6 |
| final5 | SWPP | uri | 6.61 | -0.23 | -3.30 | -7.61 | 4 |
| final5 | TVA | uri | 3.55 | -1.39 | -2.60 | -5.66 | 6 |
| final5_additive | BPAT | uri | 2.81 | -0.36 | -1.22 | -2.30 | 6 |
| final5_additive | CISO | uri | 2.17 | 1.37 | -0.07 | -0.42 | 6 |
| final5_additive | DUK | uri | 3.45 | -1.94 | -1.98 | -6.44 | 6 |
| final5_additive | ERCO | uri | 4.29 | -5.84 | -5.84 | -7.94 | 2 |
| final5_additive | FPL | uri | 10.36 | -14.93 | -14.93 | -17.55 | 6 |
| final5_additive | ISNE | uri | 2.94 | 1.92 | -0.21 | -1.25 | 6 |
| final5_additive | MISO | uri | 3.63 | -2.43 | -3.06 | -6.47 | 5 |
| final5_additive | NYIS | uri | 2.64 | 2.93 | 0.00 | 0.00 | 6 |
| final5_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final5_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final5_additive | TVA | uri | 3.45 | 0.35 | -1.19 | -3.00 | 6 |
| final5_boosting | BPAT | uri | 2.92 | 0.83 | -0.94 | -5.67 | 6 |
| final5_boosting | CISO | uri | 2.06 | -1.00 | -1.38 | -3.88 | 6 |
| final5_boosting | DUK | uri | 3.61 | -2.41 | -2.49 | -4.95 | 6 |
| final5_boosting | ERCO | uri | 8.51 | -13.40 | -13.40 | -15.36 | 2 |
| final5_boosting | FPL | uri | 8.60 | -10.26 | -10.26 | -13.08 | 6 |
| final5_boosting | ISNE | uri | 3.87 | 2.07 | -0.42 | -1.79 | 6 |
| final5_boosting | MISO | uri | 2.45 | -2.58 | -2.68 | -4.81 | 5 |
| final5_boosting | NYIS | uri | 2.76 | 1.53 | -0.44 | -2.67 | 6 |
| final5_boosting | PJM | uri | 1.95 | -0.50 | -0.92 | -2.57 | 6 |
| final5_boosting | SWPP | uri | 5.08 | -3.51 | -4.28 | -9.79 | 4 |
| final5_boosting | TVA | uri | 3.17 | -1.16 | -1.79 | -3.71 | 6 |
| final5_ensemble | BPAT | uri | 2.55 | 0.11 | -0.78 | -4.15 | 6 |
| final5_ensemble | CISO | uri | 1.83 | -0.22 | -0.71 | -1.81 | 6 |
| final5_ensemble | DUK | uri | 3.55 | -2.56 | -2.56 | -6.14 | 6 |
| final5_ensemble | ERCO | uri | 5.56 | -8.00 | -8.00 | -9.38 | 2 |
| final5_ensemble | FPL | uri | 10.33 | -13.57 | -13.57 | -16.16 | 6 |
| final5_ensemble | ISNE | uri | 2.51 | 0.87 | -0.40 | -1.88 | 6 |
| final5_ensemble | MISO | uri | 3.69 | -3.47 | -3.47 | -6.74 | 5 |
| final5_ensemble | NYIS | uri | 2.25 | 2.29 | -0.09 | -0.53 | 6 |
| final5_ensemble | PJM | uri | 2.40 | 1.18 | -0.51 | -3.07 | 6 |
| final5_ensemble | SWPP | uri | 6.12 | -1.42 | -3.63 | -7.73 | 4 |
| final5_ensemble | TVA | uri | 3.30 | -0.49 | -1.53 | -3.47 | 6 |
| final5_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final5_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final5_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final5_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final5_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final5_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final5_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final5_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final5_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final5_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final5_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| final5b | BPAT | uri | 2.43 | -0.16 | -0.85 | -4.96 | 6 |
| final5b | CISO | uri | 2.00 | -0.68 | -1.17 | -2.56 | 6 |
| final5b | DUK | uri | 3.52 | -1.55 | -1.93 | -4.06 | 6 |
| final5b | ERCO | uri | 6.40 | -8.60 | -8.60 | -9.02 | 2 |
| final5b | FPL | uri | 8.30 | -7.40 | -7.40 | -10.30 | 6 |
| final5b | ISNE | uri | 2.53 | 1.62 | -0.09 | -0.43 | 6 |
| final5b | MISO | uri | 3.91 | -3.33 | -3.56 | -6.83 | 5 |
| final5b | NYIS | uri | 2.11 | 2.17 | -0.14 | -0.86 | 6 |
| final5b | PJM | uri | 1.90 | 0.26 | -0.68 | -2.76 | 6 |
| final5b | SWPP | uri | 6.61 | -0.23 | -3.30 | -7.61 | 4 |
| final5b | TVA | uri | 3.55 | -1.39 | -2.60 | -5.66 | 6 |
| final5b_additive | BPAT | uri | 2.81 | -0.36 | -1.22 | -2.30 | 6 |
| final5b_additive | CISO | uri | 2.17 | 1.37 | -0.07 | -0.42 | 6 |
| final5b_additive | DUK | uri | 3.45 | -1.94 | -1.98 | -6.44 | 6 |
| final5b_additive | ERCO | uri | 4.29 | -5.84 | -5.84 | -7.94 | 2 |
| final5b_additive | FPL | uri | 10.36 | -14.93 | -14.93 | -17.55 | 6 |
| final5b_additive | ISNE | uri | 2.94 | 1.92 | -0.21 | -1.25 | 6 |
| final5b_additive | MISO | uri | 3.63 | -2.43 | -3.06 | -6.47 | 5 |
| final5b_additive | NYIS | uri | 2.64 | 2.93 | 0.00 | 0.00 | 6 |
| final5b_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final5b_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final5b_additive | TVA | uri | 3.45 | 0.35 | -1.19 | -3.00 | 6 |
| final5b_boosting | BPAT | uri | 2.92 | 0.83 | -0.94 | -5.67 | 6 |
| final5b_boosting | CISO | uri | 2.06 | -1.00 | -1.38 | -3.88 | 6 |
| final5b_boosting | DUK | uri | 3.61 | -2.41 | -2.49 | -4.95 | 6 |
| final5b_boosting | ERCO | uri | 8.51 | -13.40 | -13.40 | -15.36 | 2 |
| final5b_boosting | FPL | uri | 8.60 | -10.26 | -10.26 | -13.08 | 6 |
| final5b_boosting | ISNE | uri | 3.87 | 2.07 | -0.42 | -1.79 | 6 |
| final5b_boosting | MISO | uri | 2.45 | -2.58 | -2.68 | -4.81 | 5 |
| final5b_boosting | NYIS | uri | 2.76 | 1.53 | -0.44 | -2.67 | 6 |
| final5b_boosting | PJM | uri | 1.95 | -0.50 | -0.92 | -2.57 | 6 |
| final5b_boosting | SWPP | uri | 5.08 | -3.51 | -4.28 | -9.79 | 4 |
| final5b_boosting | TVA | uri | 3.17 | -1.16 | -1.79 | -3.71 | 6 |
| final5b_ensemble | BPAT | uri | 2.55 | 0.11 | -0.78 | -4.15 | 6 |
| final5b_ensemble | CISO | uri | 1.83 | -0.22 | -0.71 | -1.81 | 6 |
| final5b_ensemble | DUK | uri | 3.55 | -2.56 | -2.56 | -6.14 | 6 |
| final5b_ensemble | ERCO | uri | 5.56 | -8.00 | -8.00 | -9.38 | 2 |
| final5b_ensemble | FPL | uri | 10.33 | -13.57 | -13.57 | -16.16 | 6 |
| final5b_ensemble | ISNE | uri | 2.51 | 0.87 | -0.40 | -1.88 | 6 |
| final5b_ensemble | MISO | uri | 3.69 | -3.47 | -3.47 | -6.74 | 5 |
| final5b_ensemble | NYIS | uri | 2.25 | 2.29 | -0.09 | -0.53 | 6 |
| final5b_ensemble | PJM | uri | 2.40 | 1.18 | -0.51 | -3.07 | 6 |
| final5b_ensemble | SWPP | uri | 6.12 | -1.42 | -3.63 | -7.73 | 4 |
| final5b_ensemble | TVA | uri | 3.30 | -0.49 | -1.53 | -3.47 | 6 |
| final5b_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final5b_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final5b_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final5b_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final5b_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final5b_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final5b_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final5b_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final5b_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final5b_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final5b_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| final5c | BPAT | uri | 2.41 | 0.10 | -0.81 | -4.61 | 6 |
| final5c | CISO | uri | 2.18 | -0.65 | -1.18 | -2.53 | 6 |
| final5c | DUK | uri | 3.65 | -1.50 | -1.76 | -3.84 | 6 |
| final5c | ERCO | uri | 6.23 | -8.19 | -8.19 | -8.58 | 2 |
| final5c | FPL | uri | 8.52 | -7.63 | -7.63 | -11.39 | 6 |
| final5c | ISNE | uri | 2.62 | 1.64 | -0.12 | -0.75 | 6 |
| final5c | MISO | uri | 4.18 | -3.17 | -3.39 | -6.84 | 5 |
| final5c | NYIS | uri | 2.11 | 2.17 | -0.14 | -0.84 | 6 |
| final5c | PJM | uri | 1.90 | 0.13 | -0.64 | -2.65 | 6 |
| final5c | SWPP | uri | 6.61 | 0.31 | -2.79 | -5.91 | 4 |
| final5c | TVA | uri | 3.39 | -1.90 | -2.98 | -6.50 | 6 |
| final5c_additive | BPAT | uri | 2.71 | -0.13 | -0.97 | -2.11 | 6 |
| final5c_additive | CISO | uri | 2.21 | 1.45 | -0.05 | -0.28 | 6 |
| final5c_additive | DUK | uri | 3.55 | -2.41 | -2.41 | -6.57 | 6 |
| final5c_additive | ERCO | uri | 4.50 | -5.85 | -5.85 | -8.51 | 2 |
| final5c_additive | FPL | uri | 10.95 | -15.52 | -15.52 | -17.87 | 6 |
| final5c_additive | ISNE | uri | 3.01 | 1.97 | -0.18 | -1.09 | 6 |
| final5c_additive | MISO | uri | 3.40 | -2.02 | -2.69 | -5.53 | 5 |
| final5c_additive | NYIS | uri | 2.67 | 2.91 | 0.00 | 0.00 | 6 |
| final5c_additive | PJM | uri | 3.01 | 2.74 | -0.53 | -3.18 | 6 |
| final5c_additive | SWPP | uri | 6.20 | 2.79 | -1.22 | -4.87 | 4 |
| final5c_additive | TVA | uri | 3.46 | 0.06 | -1.48 | -3.67 | 6 |
| final5c_boosting | BPAT | uri | 3.11 | 1.55 | -0.94 | -5.12 | 6 |
| final5c_boosting | CISO | uri | 2.40 | -1.25 | -1.68 | -4.08 | 6 |
| final5c_boosting | DUK | uri | 3.78 | -2.00 | -2.00 | -4.38 | 6 |
| final5c_boosting | ERCO | uri | 7.78 | -11.87 | -11.87 | -14.20 | 2 |
| final5c_boosting | FPL | uri | 8.67 | -10.34 | -10.34 | -13.17 | 6 |
| final5c_boosting | ISNE | uri | 4.02 | 1.85 | -0.25 | -1.13 | 6 |
| final5c_boosting | MISO | uri | 3.54 | -3.09 | -3.09 | -6.27 | 5 |
| final5c_boosting | NYIS | uri | 2.82 | 2.03 | -0.36 | -2.13 | 6 |
| final5c_boosting | PJM | uri | 1.91 | -0.32 | -0.64 | -1.47 | 6 |
| final5c_boosting | SWPP | uri | 6.04 | -3.03 | -4.15 | -10.04 | 4 |
| final5c_boosting | TVA | uri | 2.42 | -1.99 | -2.53 | -4.97 | 6 |
| final5c_ensemble | BPAT | uri | 2.57 | 0.46 | -0.66 | -3.93 | 6 |
| final5c_ensemble | CISO | uri | 1.96 | -0.29 | -0.80 | -1.84 | 6 |
| final5c_ensemble | DUK | uri | 3.65 | -2.59 | -2.59 | -6.00 | 6 |
| final5c_ensemble | ERCO | uri | 5.39 | -7.45 | -7.45 | -8.92 | 2 |
| final5c_ensemble | FPL | uri | 10.58 | -13.83 | -13.83 | -16.33 | 6 |
| final5c_ensemble | ISNE | uri | 2.56 | 0.83 | -0.32 | -1.94 | 6 |
| final5c_ensemble | MISO | uri | 4.01 | -3.49 | -3.49 | -6.91 | 5 |
| final5c_ensemble | NYIS | uri | 2.23 | 2.44 | -0.07 | -0.40 | 6 |
| final5c_ensemble | PJM | uri | 2.37 | 1.20 | -0.49 | -2.92 | 6 |
| final5c_ensemble | SWPP | uri | 6.25 | -0.90 | -3.20 | -6.44 | 4 |
| final5c_ensemble | TVA | uri | 3.03 | -0.88 | -1.89 | -4.07 | 6 |
| final5c_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final5c_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final5c_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final5c_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final5c_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final5c_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final5c_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final5c_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final5c_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final5c_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final5c_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
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
| final5 | BPAT | elliott | 3.09 | -1.86 | -2.24 | -5.87 | 5 |
| final5 | CISO | elliott | 3.60 | 3.07 | -0.42 | -2.11 | 5 |
| final5 | DUK | elliott | 3.16 | -0.29 | -1.21 | -3.05 | 4 |
| final5 | ERCO | elliott | 5.50 | -1.87 | -3.24 | -6.91 | 5 |
| final5 | FPL | elliott | 6.39 | -7.74 | -7.74 | -12.88 | 5 |
| final5 | ISNE | elliott | 3.59 | 3.07 | -0.60 | -2.38 | 5 |
| final5 | MISO | elliott | 3.44 | -2.06 | -2.84 | -7.00 | 5 |
| final5 | NYIS | elliott | 2.84 | 0.02 | -1.17 | -2.64 | 5 |
| final5 | PJM | elliott | 4.50 | -4.08 | -4.11 | -9.03 | 5 |
| final5 | SWPP | elliott | 4.29 | 0.87 | -1.79 | -5.43 | 5 |
| final5 | TVA | elliott | 5.43 | 5.28 | 0.00 | 0.00 | 3 |
| final5_additive | BPAT | elliott | 3.64 | -1.20 | -2.01 | -4.25 | 5 |
| final5_additive | CISO | elliott | 3.47 | 4.03 | -0.24 | -1.21 | 5 |
| final5_additive | DUK | elliott | 4.52 | -3.26 | -3.26 | -5.10 | 4 |
| final5_additive | ERCO | elliott | 7.87 | -5.54 | -6.11 | -14.39 | 5 |
| final5_additive | FPL | elliott | 10.99 | -2.80 | -6.82 | -18.07 | 5 |
| final5_additive | ISNE | elliott | 3.77 | 2.15 | -0.94 | -2.69 | 5 |
| final5_additive | MISO | elliott | 3.32 | -3.01 | -3.33 | -6.85 | 5 |
| final5_additive | NYIS | elliott | 3.06 | -0.88 | -1.90 | -4.52 | 5 |
| final5_additive | PJM | elliott | 3.54 | -0.27 | -1.00 | -4.98 | 5 |
| final5_additive | SWPP | elliott | 3.13 | -2.41 | -2.70 | -5.88 | 5 |
| final5_additive | TVA | elliott | 6.00 | 3.14 | -0.19 | -0.57 | 3 |
| final5_boosting | BPAT | elliott | 4.23 | -5.34 | -5.34 | -11.66 | 5 |
| final5_boosting | CISO | elliott | 4.04 | 1.93 | -0.82 | -3.86 | 5 |
| final5_boosting | DUK | elliott | 4.68 | -3.05 | -3.05 | -6.31 | 4 |
| final5_boosting | ERCO | elliott | 6.96 | -9.55 | -9.58 | -19.79 | 5 |
| final5_boosting | FPL | elliott | 8.94 | -14.59 | -14.59 | -19.67 | 5 |
| final5_boosting | ISNE | elliott | 3.95 | 3.32 | -0.22 | -1.12 | 5 |
| final5_boosting | MISO | elliott | 3.41 | -1.13 | -2.26 | -4.00 | 5 |
| final5_boosting | NYIS | elliott | 3.11 | 0.61 | -0.73 | -2.96 | 5 |
| final5_boosting | PJM | elliott | 4.64 | -2.47 | -3.04 | -6.44 | 5 |
| final5_boosting | SWPP | elliott | 5.45 | -1.84 | -3.83 | -11.88 | 5 |
| final5_boosting | TVA | elliott | 6.16 | 0.77 | -1.10 | -3.31 | 3 |
| final5_ensemble | BPAT | elliott | 3.66 | -3.26 | -3.51 | -8.22 | 5 |
| final5_ensemble | CISO | elliott | 3.50 | 3.43 | -0.41 | -2.06 | 5 |
| final5_ensemble | DUK | elliott | 3.71 | -3.87 | -3.87 | -4.96 | 4 |
| final5_ensemble | ERCO | elliott | 5.97 | -5.91 | -6.26 | -11.39 | 5 |
| final5_ensemble | FPL | elliott | 7.34 | -9.19 | -9.19 | -12.88 | 5 |
| final5_ensemble | ISNE | elliott | 3.58 | 3.02 | -0.57 | -2.02 | 5 |
| final5_ensemble | MISO | elliott | 3.39 | -2.94 | -3.40 | -7.45 | 5 |
| final5_ensemble | NYIS | elliott | 2.87 | -0.59 | -1.63 | -3.31 | 5 |
| final5_ensemble | PJM | elliott | 4.24 | -3.61 | -3.81 | -9.24 | 5 |
| final5_ensemble | SWPP | elliott | 3.65 | -2.59 | -3.28 | -8.56 | 5 |
| final5_ensemble | TVA | elliott | 5.36 | 2.30 | -0.92 | -1.53 | 3 |
| final5_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final5_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final5_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final5_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final5_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final5_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final5_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final5_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final5_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final5_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final5_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |
| final5b | BPAT | elliott | 3.09 | -1.86 | -2.24 | -5.87 | 5 |
| final5b | CISO | elliott | 3.62 | 3.19 | -0.42 | -2.11 | 5 |
| final5b | DUK | elliott | 3.20 | -0.03 | -0.95 | -3.05 | 4 |
| final5b | ERCO | elliott | 5.50 | -1.87 | -3.24 | -6.91 | 5 |
| final5b | FPL | elliott | 6.39 | -7.74 | -7.74 | -12.88 | 5 |
| final5b | ISNE | elliott | 3.59 | 3.07 | -0.60 | -2.38 | 5 |
| final5b | MISO | elliott | 3.44 | -2.06 | -2.84 | -7.00 | 5 |
| final5b | NYIS | elliott | 2.84 | 0.02 | -1.17 | -2.64 | 5 |
| final5b | PJM | elliott | 4.50 | -4.08 | -4.11 | -9.03 | 5 |
| final5b | SWPP | elliott | 4.29 | 0.87 | -1.79 | -5.43 | 5 |
| final5b | TVA | elliott | 5.43 | 5.28 | 0.00 | 0.00 | 3 |
| final5b_additive | BPAT | elliott | 3.64 | -1.20 | -2.01 | -4.25 | 5 |
| final5b_additive | CISO | elliott | 3.47 | 4.03 | -0.24 | -1.21 | 5 |
| final5b_additive | DUK | elliott | 4.52 | -3.26 | -3.26 | -5.10 | 4 |
| final5b_additive | ERCO | elliott | 7.87 | -5.54 | -6.11 | -14.39 | 5 |
| final5b_additive | FPL | elliott | 10.99 | -2.80 | -6.82 | -18.07 | 5 |
| final5b_additive | ISNE | elliott | 3.77 | 2.15 | -0.94 | -2.69 | 5 |
| final5b_additive | MISO | elliott | 3.32 | -3.01 | -3.33 | -6.85 | 5 |
| final5b_additive | NYIS | elliott | 3.06 | -0.88 | -1.90 | -4.52 | 5 |
| final5b_additive | PJM | elliott | 3.54 | -0.27 | -1.00 | -4.98 | 5 |
| final5b_additive | SWPP | elliott | 3.13 | -2.41 | -2.70 | -5.88 | 5 |
| final5b_additive | TVA | elliott | 6.00 | 3.14 | -0.19 | -0.57 | 3 |
| final5b_boosting | BPAT | elliott | 4.23 | -5.34 | -5.34 | -11.66 | 5 |
| final5b_boosting | CISO | elliott | 4.04 | 1.93 | -0.82 | -3.86 | 5 |
| final5b_boosting | DUK | elliott | 4.68 | -3.05 | -3.05 | -6.31 | 4 |
| final5b_boosting | ERCO | elliott | 6.96 | -9.55 | -9.58 | -19.79 | 5 |
| final5b_boosting | FPL | elliott | 8.94 | -14.59 | -14.59 | -19.67 | 5 |
| final5b_boosting | ISNE | elliott | 3.95 | 3.32 | -0.22 | -1.12 | 5 |
| final5b_boosting | MISO | elliott | 3.41 | -1.13 | -2.26 | -4.00 | 5 |
| final5b_boosting | NYIS | elliott | 3.11 | 0.61 | -0.73 | -2.96 | 5 |
| final5b_boosting | PJM | elliott | 4.64 | -2.47 | -3.04 | -6.44 | 5 |
| final5b_boosting | SWPP | elliott | 5.45 | -1.84 | -3.83 | -11.88 | 5 |
| final5b_boosting | TVA | elliott | 6.16 | 0.77 | -1.10 | -3.31 | 3 |
| final5b_ensemble | BPAT | elliott | 3.66 | -3.26 | -3.51 | -8.22 | 5 |
| final5b_ensemble | CISO | elliott | 3.50 | 3.43 | -0.41 | -2.06 | 5 |
| final5b_ensemble | DUK | elliott | 3.71 | -3.87 | -3.87 | -4.96 | 4 |
| final5b_ensemble | ERCO | elliott | 5.97 | -5.91 | -6.26 | -11.39 | 5 |
| final5b_ensemble | FPL | elliott | 7.34 | -9.19 | -9.19 | -12.88 | 5 |
| final5b_ensemble | ISNE | elliott | 3.58 | 3.02 | -0.57 | -2.02 | 5 |
| final5b_ensemble | MISO | elliott | 3.39 | -2.94 | -3.40 | -7.45 | 5 |
| final5b_ensemble | NYIS | elliott | 2.87 | -0.59 | -1.63 | -3.31 | 5 |
| final5b_ensemble | PJM | elliott | 4.24 | -3.61 | -3.81 | -9.24 | 5 |
| final5b_ensemble | SWPP | elliott | 3.65 | -2.59 | -3.28 | -8.56 | 5 |
| final5b_ensemble | TVA | elliott | 5.36 | 2.30 | -0.92 | -1.53 | 3 |
| final5b_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final5b_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final5b_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final5b_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final5b_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final5b_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final5b_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final5b_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final5b_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final5b_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final5b_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |
| final5c | BPAT | elliott | 3.11 | -1.98 | -2.40 | -6.64 | 5 |
| final5c | CISO | elliott | 3.53 | 3.18 | -0.40 | -2.02 | 5 |
| final5c | DUK | elliott | 3.39 | 0.34 | -0.84 | -1.71 | 4 |
| final5c | ERCO | elliott | 5.35 | -2.48 | -3.45 | -6.92 | 5 |
| final5c | FPL | elliott | 5.96 | -7.12 | -7.12 | -12.32 | 5 |
| final5c | ISNE | elliott | 3.41 | 2.92 | -0.60 | -1.95 | 5 |
| final5c | MISO | elliott | 3.76 | -2.70 | -3.50 | -10.19 | 5 |
| final5c | NYIS | elliott | 2.79 | 0.01 | -1.24 | -2.95 | 5 |
| final5c | PJM | elliott | 4.84 | -4.78 | -4.78 | -10.62 | 5 |
| final5c | SWPP | elliott | 4.16 | 0.89 | -1.42 | -4.32 | 5 |
| final5c | TVA | elliott | 5.49 | 5.53 | 0.00 | 0.00 | 3 |
| final5c_additive | BPAT | elliott | 3.59 | -1.27 | -2.00 | -4.35 | 5 |
| final5c_additive | CISO | elliott | 3.48 | 4.27 | -0.18 | -0.89 | 5 |
| final5c_additive | DUK | elliott | 4.76 | -2.30 | -2.30 | -4.85 | 4 |
| final5c_additive | ERCO | elliott | 7.84 | -5.10 | -5.46 | -12.76 | 5 |
| final5c_additive | FPL | elliott | 10.60 | -2.86 | -6.76 | -17.04 | 5 |
| final5c_additive | ISNE | elliott | 3.57 | 2.19 | -0.89 | -2.66 | 5 |
| final5c_additive | MISO | elliott | 3.45 | -3.85 | -4.19 | -11.26 | 5 |
| final5c_additive | NYIS | elliott | 3.08 | -0.61 | -1.80 | -4.13 | 5 |
| final5c_additive | PJM | elliott | 3.67 | -0.14 | -1.13 | -5.66 | 5 |
| final5c_additive | SWPP | elliott | 2.73 | -2.44 | -2.56 | -5.71 | 5 |
| final5c_additive | TVA | elliott | 5.92 | 2.97 | -0.23 | -0.69 | 3 |
| final5c_boosting | BPAT | elliott | 4.22 | -5.29 | -5.42 | -13.38 | 5 |
| final5c_boosting | CISO | elliott | 3.95 | 2.03 | -0.80 | -3.98 | 5 |
| final5c_boosting | DUK | elliott | 4.52 | -2.54 | -2.54 | -5.84 | 4 |
| final5c_boosting | ERCO | elliott | 6.92 | -11.31 | -11.31 | -19.50 | 5 |
| final5c_boosting | FPL | elliott | 7.20 | -12.70 | -12.70 | -15.48 | 5 |
| final5c_boosting | ISNE | elliott | 3.57 | 3.06 | -0.08 | -0.42 | 5 |
| final5c_boosting | MISO | elliott | 4.06 | -1.51 | -2.58 | -4.90 | 5 |
| final5c_boosting | NYIS | elliott | 3.13 | 1.03 | -0.70 | -2.96 | 5 |
| final5c_boosting | PJM | elliott | 4.91 | -3.27 | -3.62 | -7.43 | 5 |
| final5c_boosting | SWPP | elliott | 5.39 | -1.23 | -3.12 | -10.17 | 5 |
| final5c_boosting | TVA | elliott | 6.15 | 1.05 | -0.11 | -0.32 | 3 |
| final5c_ensemble | BPAT | elliott | 3.60 | -3.27 | -3.57 | -8.85 | 5 |
| final5c_ensemble | CISO | elliott | 3.48 | 3.59 | -0.39 | -1.96 | 5 |
| final5c_ensemble | DUK | elliott | 3.81 | -3.36 | -3.36 | -4.98 | 4 |
| final5c_ensemble | ERCO | elliott | 5.75 | -6.39 | -6.39 | -10.72 | 5 |
| final5c_ensemble | FPL | elliott | 6.89 | -8.61 | -8.61 | -12.32 | 5 |
| final5c_ensemble | ISNE | elliott | 3.43 | 2.94 | -0.57 | -1.65 | 5 |
| final5c_ensemble | MISO | elliott | 3.60 | -3.42 | -3.83 | -9.66 | 5 |
| final5c_ensemble | NYIS | elliott | 2.83 | -0.36 | -1.58 | -3.29 | 5 |
| final5c_ensemble | PJM | elliott | 4.40 | -3.85 | -3.86 | -9.85 | 5 |
| final5c_ensemble | SWPP | elliott | 3.56 | -2.37 | -2.97 | -7.36 | 5 |
| final5c_ensemble | TVA | elliott | 5.31 | 2.31 | -0.45 | -0.83 | 3 |
| final5c_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final5c_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final5c_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final5c_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final5c_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final5c_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final5c_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final5c_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final5c_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final5c_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final5c_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | final5 | eve | 3.31 | 0.89 | -1.42 | 0.44 | 265 |
| 22 | final5b | eve | 3.32 | 0.99 | -1.39 | 0.44 | 265 |
| 27 | final5c | eve | 3.34 | 0.89 | -1.43 | 0.45 | 265 |
| 16 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 20 | final5_ensemble | eve | 3.39 | -0.55 | -2.14 | 0.48 | 265 |
| 25 | final5b_ensemble | eve | 3.39 | -0.55 | -2.14 | 0.48 | 265 |
| 30 | final5c_ensemble | eve | 3.42 | -0.53 | -2.13 | 0.48 | 265 |
| 18 | final5_additive | eve | 3.62 | -0.28 | -2.15 | 0.45 | 265 |
| 23 | final5b_additive | eve | 3.62 | -0.28 | -2.15 | 0.45 | 265 |
| 28 | final5c_additive | eve | 3.62 | -0.26 | -2.15 | 0.46 | 265 |
| 19 | final5_boosting | eve | 3.73 | -0.16 | -2.05 | 0.40 | 265 |
| 24 | final5b_boosting | eve | 3.73 | -0.16 | -2.05 | 0.40 | 265 |
| 29 | final5c_boosting | eve | 3.78 | -0.08 | -2.02 | 0.42 | 265 |
| 21 | final5_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 26 | final5b_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 31 | final5c_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final5 | special | 3.34 | -0.57 | -2.10 | 0.54 | 267 |
| 6 | final5b | special | 3.34 | -0.46 | -2.05 | 0.54 | 267 |
| 11 | final5c | special | 3.35 | -0.52 | -2.09 | 0.54 | 267 |
| 4 | final5_ensemble | special | 3.52 | -2.01 | -3.07 | 0.52 | 267 |
| 9 | final5b_ensemble | special | 3.52 | -2.01 | -3.07 | 0.52 | 267 |
| 14 | final5c_ensemble | special | 3.53 | -1.97 | -3.07 | 0.53 | 267 |
| 2 | final5_additive | special | 3.67 | -2.02 | -3.12 | 0.49 | 267 |
| 7 | final5b_additive | special | 3.67 | -2.02 | -3.12 | 0.49 | 267 |
| 12 | final5c_additive | special | 3.68 | -1.99 | -3.10 | 0.49 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final5_boosting | special | 3.79 | -1.67 | -2.84 | 0.46 | 267 |
| 8 | final5b_boosting | special | 3.79 | -1.67 | -2.84 | 0.46 | 267 |
| 13 | final5c_boosting | special | 3.87 | -1.57 | -2.86 | 0.48 | 267 |
| 5 | final5_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |
| 10 | final5b_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |
| 15 | final5c_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | all | 0.385 | 1.310 | 0.391 | 0.889 | 11.538 | 0.892 | 15.511 | 1.699 | 7815 |
| final5b | all | 0.386 | 1.317 | 0.392 | 0.888 | 11.562 | 0.893 | 15.562 | 1.707 | 7815 |
| final5c | all | 0.386 | 1.313 | 0.390 | 0.889 | 11.538 | 0.891 | 15.531 | 1.702 | 7815 |
| final5 | events | 0.458 | 1.889 | 0.645 | 0.764 | 11.876 | 0.804 | 22.059 | 2.481 | 107 |
| final5b | events | 0.460 | 1.891 | 0.646 | 0.764 | 11.858 | 0.804 | 22.114 | 2.483 | 107 |
| final5c | events | 0.476 | 1.914 | 0.664 | 0.758 | 11.861 | 0.813 | 22.794 | 2.522 | 107 |
| final5 | cold_mornings | 0.453 | 1.659 | 0.522 | 0.829 | 12.804 | 0.818 | 19.503 | 2.167 | 330 |
| final5b | cold_mornings | 0.454 | 1.659 | 0.522 | 0.829 | 12.804 | 0.818 | 19.519 | 2.167 | 330 |
| final5c | cold_mornings | 0.458 | 1.639 | 0.524 | 0.831 | 12.811 | 0.821 | 19.641 | 2.152 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 35279 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 35268 | DUK | 2022-12-24 | final5 | 8.38 | -9.34 | -9.34 |
| 35264 | DUK | 2022-12-24 | final5_additive | 7.22 | -13.03 | -13.03 |
| 35265 | DUK | 2022-12-24 | final5_boosting | 9.91 | -17.04 | -17.04 |
| 35267 | DUK | 2022-12-24 | final5_ensemble | 8.72 | -13.40 | -13.40 |
| 35266 | DUK | 2022-12-24 | final5_recency | 9.27 | -9.99 | -9.99 |
| 35273 | DUK | 2022-12-24 | final5b | 8.38 | -9.34 | -9.34 |
| 35269 | DUK | 2022-12-24 | final5b_additive | 7.22 | -13.03 | -13.03 |
| 35270 | DUK | 2022-12-24 | final5b_boosting | 9.91 | -17.04 | -17.04 |
| 35272 | DUK | 2022-12-24 | final5b_ensemble | 8.72 | -13.40 | -13.40 |
| 35271 | DUK | 2022-12-24 | final5b_recency | 9.27 | -9.99 | -9.99 |
| 35278 | DUK | 2022-12-24 | final5c | 8.47 | -10.69 | -10.69 |
| 35274 | DUK | 2022-12-24 | final5c_additive | 6.75 | -13.12 | -13.12 |
| 35275 | DUK | 2022-12-24 | final5c_boosting | 10.68 | -19.37 | -19.37 |
| 35277 | DUK | 2022-12-24 | final5c_ensemble | 8.81 | -14.22 | -14.22 |
| 35276 | DUK | 2022-12-24 | final5c_recency | 9.27 | -9.99 | -9.99 |
| 36591 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 36580 | ERCO | 2021-02-17 | final5 | 32.80 | 26.25 | 0.00 |
| 36576 | ERCO | 2021-02-17 | final5_additive | 32.00 | 28.88 | 0.00 |
| 36577 | ERCO | 2021-02-17 | final5_boosting | 29.91 | 24.19 | 0.00 |
| 36579 | ERCO | 2021-02-17 | final5_ensemble | 33.60 | 29.13 | 0.00 |
| 36578 | ERCO | 2021-02-17 | final5_recency | 41.20 | 36.68 | 0.00 |
| 36585 | ERCO | 2021-02-17 | final5b | 32.80 | 26.25 | 0.00 |
| 36581 | ERCO | 2021-02-17 | final5b_additive | 32.00 | 28.88 | 0.00 |
| 36582 | ERCO | 2021-02-17 | final5b_boosting | 29.91 | 24.19 | 0.00 |
| 36584 | ERCO | 2021-02-17 | final5b_ensemble | 33.60 | 29.13 | 0.00 |
| 36583 | ERCO | 2021-02-17 | final5b_recency | 41.20 | 36.68 | 0.00 |
| 36590 | ERCO | 2021-02-17 | final5c | 32.37 | 26.21 | 0.00 |
| 36586 | ERCO | 2021-02-17 | final5c_additive | 31.33 | 28.82 | 0.00 |
| 36587 | ERCO | 2021-02-17 | final5c_boosting | 29.40 | 23.68 | 0.00 |
| 36589 | ERCO | 2021-02-17 | final5c_ensemble | 33.14 | 28.88 | 0.00 |
| 36588 | ERCO | 2021-02-17 | final5c_recency | 41.20 | 36.68 | 0.00 |
| 36607 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 36596 | ERCO | 2021-02-18 | final5 | 3.98 | 2.79 | 0.00 |
| 36592 | ERCO | 2021-02-18 | final5_additive | 13.29 | 11.84 | 0.00 |
| 36593 | ERCO | 2021-02-18 | final5_boosting | 4.23 | -7.71 | -7.71 |
| 36595 | ERCO | 2021-02-18 | final5_ensemble | 4.48 | 1.69 | 0.00 |
| 36594 | ERCO | 2021-02-18 | final5_recency | 5.36 | 2.19 | 0.00 |
| 36601 | ERCO | 2021-02-18 | final5b | 3.98 | 2.79 | 0.00 |
| 36597 | ERCO | 2021-02-18 | final5b_additive | 13.29 | 11.84 | 0.00 |
| 36598 | ERCO | 2021-02-18 | final5b_boosting | 4.23 | -7.71 | -7.71 |
| 36600 | ERCO | 2021-02-18 | final5b_ensemble | 4.48 | 1.69 | 0.00 |
| 36599 | ERCO | 2021-02-18 | final5b_recency | 5.36 | 2.19 | 0.00 |
| 36606 | ERCO | 2021-02-18 | final5c | 6.74 | 6.72 | 0.00 |
| 36602 | ERCO | 2021-02-18 | final5c_additive | 14.01 | 13.10 | 0.00 |
| 36603 | ERCO | 2021-02-18 | final5c_boosting | 3.62 | 1.64 | 0.00 |
| 36605 | ERCO | 2021-02-18 | final5c_ensemble | 7.34 | 5.81 | 0.00 |
| 36604 | ERCO | 2021-02-18 | final5c_recency | 5.36 | 2.19 | 0.00 |
| 71119 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 71108 | MISO | 2021-02-16 | final5 | 1.60 | 1.89 | 0.00 |
| 71104 | MISO | 2021-02-16 | final5_additive | 2.38 | 2.18 | 0.00 |
| 71105 | MISO | 2021-02-16 | final5_boosting | 1.96 | 1.33 | 0.00 |
| 71107 | MISO | 2021-02-16 | final5_ensemble | 1.66 | 0.73 | 0.00 |
| 71106 | MISO | 2021-02-16 | final5_recency | 3.61 | -2.07 | -2.07 |
| 71113 | MISO | 2021-02-16 | final5b | 1.60 | 1.89 | 0.00 |
| 71109 | MISO | 2021-02-16 | final5b_additive | 2.38 | 2.18 | 0.00 |
| 71110 | MISO | 2021-02-16 | final5b_boosting | 1.96 | 1.33 | 0.00 |
| 71112 | MISO | 2021-02-16 | final5b_ensemble | 1.66 | 0.73 | 0.00 |
| 71111 | MISO | 2021-02-16 | final5b_recency | 3.61 | -2.07 | -2.07 |
| 71118 | MISO | 2021-02-16 | final5c | 1.98 | 1.97 | 0.00 |
| 71114 | MISO | 2021-02-16 | final5c_additive | 2.62 | 2.76 | 0.00 |
| 71115 | MISO | 2021-02-16 | final5c_boosting | 2.13 | 0.48 | 0.00 |
| 71117 | MISO | 2021-02-16 | final5c_ensemble | 1.92 | 0.66 | 0.00 |
| 71116 | MISO | 2021-02-16 | final5c_recency | 3.61 | -2.07 | -2.07 |
| 106639 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 106628 | SWPP | 2021-02-15 | final5 | 3.23 | -2.81 | -2.81 |
| 106624 | SWPP | 2021-02-15 | final5_additive | 2.24 | 1.30 | 0.00 |
| 106625 | SWPP | 2021-02-15 | final5_boosting | 6.97 | -8.54 | -8.54 |
| 106627 | SWPP | 2021-02-15 | final5_ensemble | 3.32 | -4.06 | -4.06 |
| 106626 | SWPP | 2021-02-15 | final5_recency | 4.81 | -5.28 | -5.28 |
| 106633 | SWPP | 2021-02-15 | final5b | 3.23 | -2.81 | -2.81 |
| 106629 | SWPP | 2021-02-15 | final5b_additive | 2.24 | 1.30 | 0.00 |
| 106630 | SWPP | 2021-02-15 | final5b_boosting | 6.97 | -8.54 | -8.54 |
| 106632 | SWPP | 2021-02-15 | final5b_ensemble | 3.32 | -4.06 | -4.06 |
| 106631 | SWPP | 2021-02-15 | final5b_recency | 4.81 | -5.28 | -5.28 |
| 106638 | SWPP | 2021-02-15 | final5c | 2.94 | -2.49 | -2.49 |
| 106634 | SWPP | 2021-02-15 | final5c_additive | 4.68 | 2.21 | 0.00 |
| 106635 | SWPP | 2021-02-15 | final5c_boosting | 6.38 | -8.86 | -8.86 |
| 106637 | SWPP | 2021-02-15 | final5c_ensemble | 2.99 | -3.84 | -3.84 |
| 106636 | SWPP | 2021-02-15 | final5c_recency | 4.81 | -5.28 | -5.28 |
| 106655 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 106644 | SWPP | 2021-02-16 | final5 | 3.79 | -0.23 | -0.23 |
| 106640 | SWPP | 2021-02-16 | final5_additive | 7.74 | 3.67 | 0.00 |
| 106641 | SWPP | 2021-02-16 | final5_boosting | 3.27 | -6.32 | -6.32 |
| 106643 | SWPP | 2021-02-16 | final5_ensemble | 3.83 | -0.86 | -0.86 |
| 106642 | SWPP | 2021-02-16 | final5_recency | 2.57 | -0.10 | -0.10 |
| 106649 | SWPP | 2021-02-16 | final5b | 3.79 | -0.23 | -0.23 |
| 106645 | SWPP | 2021-02-16 | final5b_additive | 7.74 | 3.67 | 0.00 |
| 106646 | SWPP | 2021-02-16 | final5b_boosting | 3.27 | -6.32 | -6.32 |
| 106648 | SWPP | 2021-02-16 | final5b_ensemble | 3.83 | -0.86 | -0.86 |
| 106647 | SWPP | 2021-02-16 | final5b_recency | 2.57 | -0.10 | -0.10 |
| 106654 | SWPP | 2021-02-16 | final5c | 4.68 | -0.03 | -0.03 |
| 106650 | SWPP | 2021-02-16 | final5c_additive | 9.39 | 4.55 | 0.00 |
| 106651 | SWPP | 2021-02-16 | final5c_boosting | 3.43 | -6.96 | -6.96 |
| 106653 | SWPP | 2021-02-16 | final5c_ensemble | 4.60 | -0.70 | -0.70 |
| 106652 | SWPP | 2021-02-16 | final5c_recency | 2.57 | -0.10 | -0.10 |
| 128895 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 128884 | TVA | 2022-12-23 | final5 | 8.91 | -10.35 | -10.35 |
| 128880 | TVA | 2022-12-23 | final5_additive | 7.33 | -3.19 | -3.19 |
| 128881 | TVA | 2022-12-23 | final5_boosting | 15.23 | -16.37 | -16.37 |
| 128883 | TVA | 2022-12-23 | final5_ensemble | 8.63 | -9.78 | -9.78 |
| 128882 | TVA | 2022-12-23 | final5_recency | 11.83 | -10.22 | -10.22 |
| 128889 | TVA | 2022-12-23 | final5b | 8.91 | -10.35 | -10.35 |
| 128885 | TVA | 2022-12-23 | final5b_additive | 7.33 | -3.19 | -3.19 |
| 128886 | TVA | 2022-12-23 | final5b_boosting | 15.23 | -16.37 | -16.37 |
| 128888 | TVA | 2022-12-23 | final5b_ensemble | 8.63 | -9.78 | -9.78 |
| 128887 | TVA | 2022-12-23 | final5b_recency | 11.83 | -10.22 | -10.22 |
| 128894 | TVA | 2022-12-23 | final5c | 8.71 | -9.69 | -9.69 |
| 128890 | TVA | 2022-12-23 | final5c_additive | 7.67 | -1.71 | -1.71 |
| 128891 | TVA | 2022-12-23 | final5c_boosting | 15.53 | -15.67 | -15.67 |
| 128893 | TVA | 2022-12-23 | final5c_ensemble | 8.60 | -9.03 | -9.03 |
| 128892 | TVA | 2022-12-23 | final5c_recency | 11.83 | -10.22 | -10.22 |
| 128911 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 128900 | TVA | 2022-12-24 | final5 | 5.45 | -10.41 | -10.41 |
| 128896 | TVA | 2022-12-24 | final5_additive | 3.82 | -9.06 | -9.06 |
| 128897 | TVA | 2022-12-24 | final5_boosting | 7.15 | -15.20 | -15.20 |
| 128899 | TVA | 2022-12-24 | final5_ensemble | 5.87 | -11.81 | -11.81 |
| 128898 | TVA | 2022-12-24 | final5_recency | 7.21 | -11.36 | -11.36 |
| 128905 | TVA | 2022-12-24 | final5b | 5.45 | -10.41 | -10.41 |
| 128901 | TVA | 2022-12-24 | final5b_additive | 3.82 | -9.06 | -9.06 |
| 128902 | TVA | 2022-12-24 | final5b_boosting | 7.15 | -15.20 | -15.20 |
| 128904 | TVA | 2022-12-24 | final5b_ensemble | 5.87 | -11.81 | -11.81 |
| 128903 | TVA | 2022-12-24 | final5b_recency | 7.21 | -11.36 | -11.36 |
| 128910 | TVA | 2022-12-24 | final5c | 5.17 | -11.83 | -11.83 |
| 128906 | TVA | 2022-12-24 | final5c_additive | 4.00 | -9.61 | -9.61 |
| 128907 | TVA | 2022-12-24 | final5c_boosting | 5.95 | -13.49 | -13.49 |
| 128909 | TVA | 2022-12-24 | final5c_ensemble | 5.45 | -11.44 | -11.44 |
| 128908 | TVA | 2022-12-24 | final5c_recency | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final5 | BPAT | mape | 7.401 | 0.000 | 746 |
| final5 | CISO | mape | 0.871 | 0.384 | 719 |
| final5 | DUK | mape | 5.428 | 0.000 | 746 |
| final5 | ERCO | mape | -0.450 | 0.653 | 742 |
| final5 | FPL | mape | -2.973 | 0.003 | 665 |
| final5 | ISNE | mape | 13.637 | 0.000 | 748 |
| final5 | MISO | mape | -10.511 | 0.000 | 738 |
| final5 | NYIS | mape | -6.553 | 0.000 | 748 |
| final5 | PJM | mape | -5.868 | 0.000 | 734 |
| final5 | SWPP | mape | -18.944 | 0.000 | 741 |
| final5 | TVA | mape | 11.074 | 0.000 | 729 |
| final5_additive | BPAT | mape | 11.120 | 0.000 | 746 |
| final5_additive | CISO | mape | 15.689 | 0.000 | 719 |
| final5_additive | DUK | mape | 7.194 | 0.000 | 746 |
| final5_additive | ERCO | mape | 12.990 | 0.000 | 742 |
| final5_additive | FPL | mape | 17.832 | 0.000 | 665 |
| final5_additive | ISNE | mape | 19.445 | 0.000 | 748 |
| final5_additive | MISO | mape | -5.134 | 0.000 | 738 |
| final5_additive | NYIS | mape | -1.981 | 0.048 | 748 |
| final5_additive | PJM | mape | 3.225 | 0.001 | 734 |
| final5_additive | SWPP | mape | -15.827 | 0.000 | 741 |
| final5_additive | TVA | mape | 15.024 | 0.000 | 729 |
| final5_boosting | BPAT | mape | 11.385 | 0.000 | 746 |
| final5_boosting | CISO | mape | 7.873 | 0.000 | 719 |
| final5_boosting | DUK | mape | 7.523 | 0.000 | 746 |
| final5_boosting | ERCO | mape | 4.791 | 0.000 | 742 |
| final5_boosting | FPL | mape | 19.104 | 0.000 | 665 |
| final5_boosting | ISNE | mape | 17.407 | 0.000 | 748 |
| final5_boosting | MISO | mape | -6.182 | 0.000 | 738 |
| final5_boosting | NYIS | mape | -2.270 | 0.023 | 748 |
| final5_boosting | PJM | mape | 3.149 | 0.002 | 734 |
| final5_boosting | SWPP | mape | -13.824 | 0.000 | 741 |
| final5_boosting | TVA | mape | 13.850 | 0.000 | 729 |
| final5_ensemble | BPAT | mape | 8.161 | 0.000 | 746 |
| final5_ensemble | CISO | mape | 11.919 | 0.000 | 719 |
| final5_ensemble | DUK | mape | 5.356 | 0.000 | 746 |
| final5_ensemble | ERCO | mape | 6.226 | 0.000 | 742 |
| final5_ensemble | FPL | mape | 19.459 | 0.000 | 665 |
| final5_ensemble | ISNE | mape | 17.591 | 0.000 | 748 |
| final5_ensemble | MISO | mape | -7.594 | 0.000 | 738 |
| final5_ensemble | NYIS | mape | -5.945 | 0.000 | 748 |
| final5_ensemble | PJM | mape | -0.624 | 0.532 | 734 |
| final5_ensemble | SWPP | mape | -18.982 | 0.000 | 741 |
| final5_ensemble | TVA | mape | 12.114 | 0.000 | 729 |
| final5_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final5_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final5_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final5_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final5_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final5_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final5_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final5_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final5_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final5_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final5_recency | TVA | mape | 20.369 | 0.000 | 729 |
| final5b | BPAT | mape | 7.527 | 0.000 | 746 |
| final5b | CISO | mape | 0.993 | 0.321 | 719 |
| final5b | DUK | mape | 5.739 | 0.000 | 746 |
| final5b | ERCO | mape | -0.113 | 0.910 | 742 |
| final5b | FPL | mape | -2.832 | 0.005 | 665 |
| final5b | ISNE | mape | 13.803 | 0.000 | 748 |
| final5b | MISO | mape | -10.385 | 0.000 | 738 |
| final5b | NYIS | mape | -6.252 | 0.000 | 748 |
| final5b | PJM | mape | -5.617 | 0.000 | 734 |
| final5b | SWPP | mape | -18.955 | 0.000 | 741 |
| final5b | TVA | mape | 11.504 | 0.000 | 729 |
| final5b_additive | BPAT | mape | 11.120 | 0.000 | 746 |
| final5b_additive | CISO | mape | 15.689 | 0.000 | 719 |
| final5b_additive | DUK | mape | 7.194 | 0.000 | 746 |
| final5b_additive | ERCO | mape | 12.990 | 0.000 | 742 |
| final5b_additive | FPL | mape | 17.832 | 0.000 | 665 |
| final5b_additive | ISNE | mape | 19.445 | 0.000 | 748 |
| final5b_additive | MISO | mape | -5.134 | 0.000 | 738 |
| final5b_additive | NYIS | mape | -1.981 | 0.048 | 748 |
| final5b_additive | PJM | mape | 3.225 | 0.001 | 734 |
| final5b_additive | SWPP | mape | -15.827 | 0.000 | 741 |
| final5b_additive | TVA | mape | 15.024 | 0.000 | 729 |
| final5b_boosting | BPAT | mape | 11.385 | 0.000 | 746 |
| final5b_boosting | CISO | mape | 7.873 | 0.000 | 719 |
| final5b_boosting | DUK | mape | 7.523 | 0.000 | 746 |
| final5b_boosting | ERCO | mape | 4.791 | 0.000 | 742 |
| final5b_boosting | FPL | mape | 19.104 | 0.000 | 665 |
| final5b_boosting | ISNE | mape | 17.407 | 0.000 | 748 |
| final5b_boosting | MISO | mape | -6.182 | 0.000 | 738 |
| final5b_boosting | NYIS | mape | -2.270 | 0.023 | 748 |
| final5b_boosting | PJM | mape | 3.149 | 0.002 | 734 |
| final5b_boosting | SWPP | mape | -13.824 | 0.000 | 741 |
| final5b_boosting | TVA | mape | 13.850 | 0.000 | 729 |
| final5b_ensemble | BPAT | mape | 8.161 | 0.000 | 746 |
| final5b_ensemble | CISO | mape | 11.919 | 0.000 | 719 |
| final5b_ensemble | DUK | mape | 5.356 | 0.000 | 746 |
| final5b_ensemble | ERCO | mape | 6.226 | 0.000 | 742 |
| final5b_ensemble | FPL | mape | 19.459 | 0.000 | 665 |
| final5b_ensemble | ISNE | mape | 17.591 | 0.000 | 748 |
| final5b_ensemble | MISO | mape | -7.594 | 0.000 | 738 |
| final5b_ensemble | NYIS | mape | -5.945 | 0.000 | 748 |
| final5b_ensemble | PJM | mape | -0.624 | 0.532 | 734 |
| final5b_ensemble | SWPP | mape | -18.982 | 0.000 | 741 |
| final5b_ensemble | TVA | mape | 12.114 | 0.000 | 729 |
| final5b_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final5b_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final5b_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final5b_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final5b_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final5b_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final5b_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final5b_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final5b_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final5b_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final5b_recency | TVA | mape | 20.369 | 0.000 | 729 |
| final5c | BPAT | mape | 7.519 | 0.000 | 746 |
| final5c | CISO | mape | 1.139 | 0.255 | 719 |
| final5c | DUK | mape | 5.568 | 0.000 | 746 |
| final5c | ERCO | mape | -0.185 | 0.853 | 742 |
| final5c | FPL | mape | -2.864 | 0.004 | 665 |
| final5c | ISNE | mape | 13.645 | 0.000 | 748 |
| final5c | MISO | mape | -10.455 | 0.000 | 738 |
| final5c | NYIS | mape | -6.525 | 0.000 | 748 |
| final5c | PJM | mape | -5.872 | 0.000 | 734 |
| final5c | SWPP | mape | -18.864 | 0.000 | 741 |
| final5c | TVA | mape | 11.341 | 0.000 | 729 |
| final5c_additive | BPAT | mape | 11.456 | 0.000 | 746 |
| final5c_additive | CISO | mape | 15.510 | 0.000 | 719 |
| final5c_additive | DUK | mape | 7.100 | 0.000 | 746 |
| final5c_additive | ERCO | mape | 13.270 | 0.000 | 742 |
| final5c_additive | FPL | mape | 18.685 | 0.000 | 665 |
| final5c_additive | ISNE | mape | 19.317 | 0.000 | 748 |
| final5c_additive | MISO | mape | -5.514 | 0.000 | 738 |
| final5c_additive | NYIS | mape | -2.318 | 0.020 | 748 |
| final5c_additive | PJM | mape | 3.478 | 0.001 | 734 |
| final5c_additive | SWPP | mape | -15.937 | 0.000 | 741 |
| final5c_additive | TVA | mape | 15.264 | 0.000 | 729 |
| final5c_boosting | BPAT | mape | 11.278 | 0.000 | 746 |
| final5c_boosting | CISO | mape | 8.311 | 0.000 | 719 |
| final5c_boosting | DUK | mape | 7.927 | 0.000 | 746 |
| final5c_boosting | ERCO | mape | 5.433 | 0.000 | 742 |
| final5c_boosting | FPL | mape | 19.118 | 0.000 | 665 |
| final5c_boosting | ISNE | mape | 17.295 | 0.000 | 748 |
| final5c_boosting | MISO | mape | -5.911 | 0.000 | 738 |
| final5c_boosting | NYIS | mape | -1.517 | 0.129 | 748 |
| final5c_boosting | PJM | mape | 3.368 | 0.001 | 734 |
| final5c_boosting | SWPP | mape | -13.241 | 0.000 | 741 |
| final5c_boosting | TVA | mape | 14.600 | 0.000 | 729 |
| final5c_ensemble | BPAT | mape | 8.194 | 0.000 | 746 |
| final5c_ensemble | CISO | mape | 11.932 | 0.000 | 719 |
| final5c_ensemble | DUK | mape | 5.475 | 0.000 | 746 |
| final5c_ensemble | ERCO | mape | 6.525 | 0.000 | 742 |
| final5c_ensemble | FPL | mape | 19.710 | 0.000 | 665 |
| final5c_ensemble | ISNE | mape | 17.602 | 0.000 | 748 |
| final5c_ensemble | MISO | mape | -7.746 | 0.000 | 738 |
| final5c_ensemble | NYIS | mape | -5.910 | 0.000 | 748 |
| final5c_ensemble | PJM | mape | -0.564 | 0.573 | 734 |
| final5c_ensemble | SWPP | mape | -18.850 | 0.000 | 741 |
| final5c_ensemble | TVA | mape | 12.296 | 0.000 | 729 |
| final5c_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final5c_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final5c_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final5c_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final5c_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final5c_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final5c_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final5c_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final5c_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final5c_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final5c_recency | TVA | mape | 20.369 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final5 | 0.987 |
| final5_additive | 0.965 |
| final5_boosting | 0.987 |
| final5_ensemble | 0.987 |
| final5_recency | 0.987 |
| final5b | 0.987 |
| final5b_additive | 0.965 |
| final5b_boosting | 0.987 |
| final5b_ensemble | 0.987 |
| final5b_recency | 0.987 |
| final5c | 0.987 |
| final5c_additive | 0.965 |
| final5c_boosting | 0.987 |
| final5c_ensemble | 0.987 |
| final5c_recency | 0.987 |
