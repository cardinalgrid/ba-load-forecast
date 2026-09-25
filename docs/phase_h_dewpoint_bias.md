# Phase H: the dew point path corrected by its own recent bias

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final4b` is `final4` with the HRRR dew point of every station moved by the median of the forecast's own error at that local hour over the last 30 known days (forecast as seen at the cut-off against the airport observation), the temperature correction of phase G applied to the dew point. Compare with `docs/phase_h_humidity_only.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final4b | 2.40 | 2.08 | 0.06 | -1.28 | 1.24 | 0.56 | 0.30 | -46.55 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final4b_ensemble | 2.74 | 2.41 | -1.19 | -2.08 | 1.27 | 0.49 | 0.24 | -50.92 | 8056 | 11.00 |
| final4b_boosting | 2.84 | 2.50 | -0.80 | -1.92 | 1.43 | 0.45 | 0.25 | -51.49 | 8056 | 11.00 |
| final4b_additive | 2.96 | 2.61 | -1.22 | -2.24 | 1.32 | 0.44 | 0.23 | -49.11 | 8056 | 11.00 |
| final4b_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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
| final4b | BPAT | 2.46 | 2.15 | -0.42 | -1.45 | 1.74 | -17.90 | 0.38 | 0.26 | 746 | 6536.52 |
| final4b | CISO | 2.44 | 2.13 | 0.39 | -1.10 | 0.34 | -12.22 | 0.49 | 0.27 | 719 | 25193.76 |
| final4b | DUK | 3.19 | 2.86 | 0.01 | -1.76 | 1.33 | -16.70 | 0.40 | 0.32 | 746 | 12143.29 |
| final4b | ERCO | 2.61 | 2.18 | 0.05 | -1.41 | 1.02 | -13.97 | 0.48 | 0.29 | 742 | 46834.59 |
| final4b | FPL | 3.63 | 3.18 | -0.81 | -2.58 | 1.03 | -46.55 | 0.60 | 0.65 | 665 | 15346.05 |
| final4b | ISNE | 3.21 | 2.85 | 0.41 | -1.26 | 0.50 | -15.58 | 0.35 | 0.21 | 748 | 13403.92 |
| final4b | MISO | 2.02 | 1.76 | 0.14 | -0.99 | 1.67 | -7.66 | 0.63 | 0.07 | 738 | 73700.16 |
| final4b | NYIS | 2.25 | 1.95 | 0.00 | -1.28 | 0.58 | -12.60 | 0.62 | 0.73 | 748 | 17415.28 |
| final4b | PJM | 2.15 | 1.90 | 0.04 | -1.20 | 1.38 | -9.98 | 0.61 | 0.44 | 734 | 92076.14 |
| final4b | SWPP | 2.22 | 1.86 | -0.12 | -1.26 | 1.45 | -19.45 | 0.74 | 0.11 | 741 | 31382.01 |
| final4b | TVA | 2.86 | 2.49 | 0.43 | -1.41 | 1.38 | -10.87 | 0.32 | 0.32 | 729 | 18581.23 |
| final4b_additive | BPAT | 2.67 | 2.36 | -0.70 | -1.67 | 1.80 | -16.90 | 0.31 | 0.23 | 746 | 6536.52 |
| final4b_additive | CISO | 3.56 | 3.04 | -2.78 | -3.67 | 0.41 | -17.92 | 0.29 | 0.13 | 719 | 25193.76 |
| final4b_additive | DUK | 3.41 | 2.97 | -0.72 | -2.29 | 1.37 | -16.17 | 0.37 | 0.28 | 746 | 12143.29 |
| final4b_additive | ERCO | 3.52 | 3.18 | -2.18 | -2.98 | 1.08 | -16.29 | 0.31 | 0.15 | 742 | 46834.59 |
| final4b_additive | FPL | 5.85 | 5.39 | -5.36 | -5.97 | 1.09 | -49.11 | 0.29 | 0.32 | 665 | 15346.05 |
| final4b_additive | ISNE | 3.64 | 3.25 | -1.09 | -2.33 | 0.51 | -21.27 | 0.25 | 0.16 | 748 | 13403.92 |
| final4b_additive | MISO | 2.27 | 2.02 | -0.90 | -1.67 | 1.60 | -8.60 | 0.56 | 0.05 | 738 | 73700.16 |
| final4b_additive | NYIS | 2.55 | 2.24 | -0.88 | -1.96 | 0.54 | -15.16 | 0.56 | 0.60 | 748 | 17415.28 |
| final4b_additive | PJM | 2.63 | 2.31 | -0.33 | -1.59 | 1.67 | -11.71 | 0.46 | 0.39 | 734 | 92076.14 |
| final4b_additive | SWPP | 2.43 | 2.01 | -0.59 | -1.67 | 1.45 | -19.62 | 0.71 | 0.09 | 741 | 31382.01 |
| final4b_additive | TVA | 3.26 | 2.86 | -0.88 | -2.25 | 1.45 | -15.23 | 0.25 | 0.26 | 729 | 18581.23 |
| final4b_boosting | BPAT | 2.67 | 2.41 | -0.46 | -1.58 | 1.99 | -17.63 | 0.29 | 0.25 | 746 | 6536.52 |
| final4b_boosting | CISO | 2.85 | 2.56 | -1.82 | -2.45 | 0.42 | -15.48 | 0.38 | 0.16 | 719 | 25193.76 |
| final4b_boosting | DUK | 3.39 | 2.90 | -0.53 | -2.16 | 1.41 | -18.14 | 0.37 | 0.28 | 746 | 12143.29 |
| final4b_boosting | ERCO | 2.96 | 2.56 | -2.30 | -2.89 | 1.35 | -20.30 | 0.36 | 0.16 | 742 | 46834.59 |
| final4b_boosting | FPL | 5.95 | 5.50 | -6.23 | -6.61 | 1.28 | -51.49 | 0.22 | 0.30 | 665 | 15346.05 |
| final4b_boosting | ISNE | 3.40 | 3.10 | -0.32 | -1.58 | 0.51 | -16.39 | 0.30 | 0.18 | 748 | 13403.92 |
| final4b_boosting | MISO | 2.24 | 1.93 | -0.32 | -1.27 | 1.65 | -9.52 | 0.57 | 0.06 | 738 | 73700.16 |
| final4b_boosting | NYIS | 2.56 | 2.26 | -0.03 | -1.26 | 0.77 | -11.69 | 0.55 | 0.73 | 748 | 17415.28 |
| final4b_boosting | PJM | 2.67 | 2.43 | 0.42 | -1.20 | 1.73 | -13.24 | 0.43 | 0.45 | 734 | 92076.14 |
| final4b_boosting | SWPP | 2.56 | 2.09 | -0.90 | -1.93 | 1.60 | -29.56 | 0.69 | 0.08 | 741 | 31382.01 |
| final4b_boosting | TVA | 3.14 | 2.68 | -0.34 | -1.83 | 1.53 | -12.10 | 0.28 | 0.29 | 729 | 18581.23 |
| final4b_ensemble | BPAT | 2.50 | 2.22 | -0.80 | -1.65 | 1.69 | -17.85 | 0.37 | 0.23 | 746 | 6536.52 |
| final4b_ensemble | CISO | 3.17 | 2.73 | -2.69 | -3.22 | 0.37 | -16.55 | 0.34 | 0.12 | 719 | 25193.76 |
| final4b_ensemble | DUK | 3.26 | 2.81 | -0.59 | -2.15 | 1.42 | -15.03 | 0.40 | 0.27 | 746 | 12143.29 |
| final4b_ensemble | ERCO | 3.04 | 2.63 | -2.39 | -2.93 | 1.09 | -15.07 | 0.39 | 0.15 | 742 | 46834.59 |
| final4b_ensemble | FPL | 6.16 | 5.74 | -6.60 | -6.95 | 1.05 | -50.92 | 0.24 | 0.25 | 665 | 15346.05 |
| final4b_ensemble | ISNE | 3.39 | 3.11 | -1.19 | -2.12 | 0.49 | -17.26 | 0.27 | 0.15 | 748 | 13403.92 |
| final4b_ensemble | MISO | 2.12 | 1.87 | -0.77 | -1.46 | 1.64 | -8.29 | 0.61 | 0.05 | 738 | 73700.16 |
| final4b_ensemble | NYIS | 2.31 | 2.00 | -0.46 | -1.49 | 0.57 | -13.39 | 0.60 | 0.70 | 748 | 17415.28 |
| final4b_ensemble | PJM | 2.43 | 2.16 | -0.15 | -1.35 | 1.51 | -10.57 | 0.54 | 0.43 | 734 | 92076.14 |
| final4b_ensemble | SWPP | 2.25 | 1.85 | -0.56 | -1.55 | 1.38 | -19.25 | 0.73 | 0.09 | 741 | 31382.01 |
| final4b_ensemble | TVA | 3.01 | 2.63 | -0.73 | -2.02 | 1.34 | -13.60 | 0.29 | 0.27 | 729 | 18581.23 |
| final4b_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final4b_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final4b_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final4b_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final4b_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final4b_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final4b_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final4b_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final4b_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final4b_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final4b_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |

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
| final4b | BPAT | uri | 2.50 | -0.43 | -1.00 | -4.80 | 6 |
| final4b | CISO | uri | 2.14 | -0.99 | -1.44 | -2.96 | 6 |
| final4b | DUK | uri | 3.60 | -1.43 | -1.92 | -3.61 | 6 |
| final4b | ERCO | uri | 6.47 | -8.24 | -8.24 | -8.38 | 2 |
| final4b | FPL | uri | 8.18 | -7.31 | -7.31 | -10.07 | 6 |
| final4b | ISNE | uri | 2.53 | 1.72 | -0.06 | -0.39 | 6 |
| final4b | MISO | uri | 3.88 | -3.36 | -3.59 | -7.17 | 5 |
| final4b | NYIS | uri | 2.11 | 2.17 | -0.13 | -0.75 | 6 |
| final4b | PJM | uri | 1.94 | 0.17 | -0.63 | -2.42 | 6 |
| final4b | SWPP | uri | 6.71 | -0.31 | -3.37 | -7.71 | 4 |
| final4b | TVA | uri | 3.63 | -1.58 | -2.75 | -6.19 | 6 |
| final4b_additive | BPAT | uri | 2.81 | -0.36 | -1.22 | -2.30 | 6 |
| final4b_additive | CISO | uri | 2.17 | 1.37 | -0.07 | -0.42 | 6 |
| final4b_additive | DUK | uri | 3.45 | -1.94 | -1.98 | -6.44 | 6 |
| final4b_additive | ERCO | uri | 4.29 | -5.84 | -5.84 | -7.94 | 2 |
| final4b_additive | FPL | uri | 10.36 | -14.93 | -14.93 | -17.55 | 6 |
| final4b_additive | ISNE | uri | 2.94 | 1.92 | -0.21 | -1.25 | 6 |
| final4b_additive | MISO | uri | 3.63 | -2.43 | -3.06 | -6.47 | 5 |
| final4b_additive | NYIS | uri | 2.64 | 2.93 | 0.00 | 0.00 | 6 |
| final4b_additive | PJM | uri | 3.14 | 2.98 | -0.40 | -2.43 | 6 |
| final4b_additive | SWPP | uri | 6.55 | 1.73 | -2.09 | -5.13 | 4 |
| final4b_additive | TVA | uri | 3.45 | 0.35 | -1.19 | -3.00 | 6 |
| final4b_boosting | BPAT | uri | 3.09 | 0.84 | -0.92 | -4.84 | 6 |
| final4b_boosting | CISO | uri | 2.45 | -1.70 | -1.95 | -4.89 | 6 |
| final4b_boosting | DUK | uri | 3.64 | -2.41 | -2.60 | -5.93 | 6 |
| final4b_boosting | ERCO | uri | 8.53 | -12.15 | -12.15 | -14.15 | 2 |
| final4b_boosting | FPL | uri | 8.25 | -9.96 | -9.96 | -13.63 | 6 |
| final4b_boosting | ISNE | uri | 3.66 | 1.85 | -0.31 | -1.02 | 6 |
| final4b_boosting | MISO | uri | 2.37 | -2.52 | -2.65 | -5.46 | 5 |
| final4b_boosting | NYIS | uri | 2.69 | 1.45 | -0.50 | -2.69 | 6 |
| final4b_boosting | PJM | uri | 2.01 | -0.70 | -0.92 | -2.06 | 6 |
| final4b_boosting | SWPP | uri | 5.42 | -3.48 | -4.47 | -10.18 | 4 |
| final4b_boosting | TVA | uri | 3.21 | -1.38 | -2.12 | -5.24 | 6 |
| final4b_ensemble | BPAT | uri | 2.62 | 0.08 | -0.75 | -3.82 | 6 |
| final4b_ensemble | CISO | uri | 1.95 | -0.46 | -0.93 | -2.16 | 6 |
| final4b_ensemble | DUK | uri | 3.59 | -2.56 | -2.56 | -6.45 | 6 |
| final4b_ensemble | ERCO | uri | 5.56 | -7.58 | -7.58 | -8.94 | 2 |
| final4b_ensemble | FPL | uri | 10.18 | -13.43 | -13.43 | -16.35 | 6 |
| final4b_ensemble | ISNE | uri | 2.50 | 0.81 | -0.36 | -1.90 | 6 |
| final4b_ensemble | MISO | uri | 3.64 | -3.44 | -3.45 | -6.98 | 5 |
| final4b_ensemble | NYIS | uri | 2.22 | 2.26 | -0.09 | -0.54 | 6 |
| final4b_ensemble | PJM | uri | 2.40 | 1.11 | -0.48 | -2.87 | 6 |
| final4b_ensemble | SWPP | uri | 6.23 | -1.42 | -3.70 | -7.87 | 4 |
| final4b_ensemble | TVA | uri | 3.34 | -0.57 | -1.65 | -3.72 | 6 |
| final4b_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final4b_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final4b_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final4b_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final4b_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final4b_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final4b_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final4b_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final4b_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final4b_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final4b_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
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
| final4b | BPAT | elliott | 3.10 | -1.86 | -2.31 | -5.70 | 5 |
| final4b | CISO | elliott | 3.60 | 2.96 | -0.46 | -2.28 | 5 |
| final4b | DUK | elliott | 3.13 | -1.17 | -1.44 | -4.04 | 4 |
| final4b | ERCO | elliott | 5.75 | -2.80 | -3.94 | -8.01 | 5 |
| final4b | FPL | elliott | 6.41 | -7.88 | -7.88 | -12.40 | 5 |
| final4b | ISNE | elliott | 3.52 | 2.50 | -0.75 | -2.61 | 5 |
| final4b | MISO | elliott | 3.51 | -2.52 | -3.21 | -7.46 | 5 |
| final4b | NYIS | elliott | 2.83 | -0.84 | -1.63 | -3.71 | 5 |
| final4b | PJM | elliott | 4.63 | -4.34 | -4.34 | -9.55 | 5 |
| final4b | SWPP | elliott | 4.34 | 0.37 | -2.08 | -6.12 | 5 |
| final4b | TVA | elliott | 5.17 | 4.23 | 0.00 | 0.00 | 3 |
| final4b_additive | BPAT | elliott | 3.64 | -1.20 | -2.01 | -4.25 | 5 |
| final4b_additive | CISO | elliott | 3.47 | 4.03 | -0.24 | -1.21 | 5 |
| final4b_additive | DUK | elliott | 4.52 | -3.26 | -3.26 | -5.10 | 4 |
| final4b_additive | ERCO | elliott | 7.87 | -5.54 | -6.11 | -14.39 | 5 |
| final4b_additive | FPL | elliott | 10.99 | -2.80 | -6.82 | -18.07 | 5 |
| final4b_additive | ISNE | elliott | 3.77 | 2.15 | -0.94 | -2.69 | 5 |
| final4b_additive | MISO | elliott | 3.32 | -3.01 | -3.33 | -6.85 | 5 |
| final4b_additive | NYIS | elliott | 3.06 | -0.88 | -1.90 | -4.52 | 5 |
| final4b_additive | PJM | elliott | 3.54 | -0.27 | -1.00 | -4.98 | 5 |
| final4b_additive | SWPP | elliott | 3.13 | -2.41 | -2.70 | -5.88 | 5 |
| final4b_additive | TVA | elliott | 6.00 | 3.14 | -0.19 | -0.57 | 3 |
| final4b_boosting | BPAT | elliott | 4.28 | -4.35 | -4.51 | -10.92 | 5 |
| final4b_boosting | CISO | elliott | 4.05 | 1.78 | -0.93 | -4.24 | 5 |
| final4b_boosting | DUK | elliott | 4.62 | -3.06 | -3.06 | -6.93 | 4 |
| final4b_boosting | ERCO | elliott | 7.15 | -9.41 | -9.41 | -20.30 | 5 |
| final4b_boosting | FPL | elliott | 8.76 | -14.66 | -14.66 | -20.48 | 5 |
| final4b_boosting | ISNE | elliott | 3.58 | 2.90 | -0.32 | -1.62 | 5 |
| final4b_boosting | MISO | elliott | 3.55 | -1.31 | -2.30 | -4.17 | 5 |
| final4b_boosting | NYIS | elliott | 3.12 | 0.17 | -0.95 | -3.67 | 5 |
| final4b_boosting | PJM | elliott | 5.07 | -2.21 | -2.95 | -6.22 | 5 |
| final4b_boosting | SWPP | elliott | 5.74 | -1.50 | -4.05 | -12.13 | 5 |
| final4b_boosting | TVA | elliott | 6.30 | 1.23 | -0.93 | -2.80 | 3 |
| final4b_ensemble | BPAT | elliott | 3.60 | -2.88 | -3.21 | -7.93 | 5 |
| final4b_ensemble | CISO | elliott | 3.50 | 3.39 | -0.44 | -2.19 | 5 |
| final4b_ensemble | DUK | elliott | 3.70 | -3.87 | -3.87 | -4.84 | 4 |
| final4b_ensemble | ERCO | elliott | 6.05 | -5.85 | -6.18 | -11.54 | 5 |
| final4b_ensemble | FPL | elliott | 7.34 | -9.28 | -9.28 | -12.40 | 5 |
| final4b_ensemble | ISNE | elliott | 3.49 | 2.87 | -0.57 | -2.20 | 5 |
| final4b_ensemble | MISO | elliott | 3.41 | -3.00 | -3.41 | -7.38 | 5 |
| final4b_ensemble | NYIS | elliott | 2.85 | -0.74 | -1.72 | -3.56 | 5 |
| final4b_ensemble | PJM | elliott | 4.33 | -3.54 | -3.71 | -9.19 | 5 |
| final4b_ensemble | SWPP | elliott | 3.75 | -2.49 | -3.31 | -8.60 | 5 |
| final4b_ensemble | TVA | elliott | 5.41 | 2.46 | -0.94 | -1.45 | 3 |
| final4b_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final4b_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final4b_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final4b_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final4b_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final4b_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final4b_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final4b_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final4b_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final4b_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final4b_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final4b | eve | 3.34 | 0.86 | -1.43 | 0.44 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 10 | final4b_ensemble | eve | 3.42 | -0.40 | -2.07 | 0.47 | 265 |
| 8 | final4b_additive | eve | 3.64 | -0.02 | -2.03 | 0.44 | 265 |
| 9 | final4b_boosting | eve | 3.81 | 0.01 | -2.00 | 0.39 | 265 |
| 11 | final4b_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final4b | special | 3.36 | -0.60 | -2.11 | 0.54 | 267 |
| 4 | final4b_ensemble | special | 3.53 | -1.86 | -2.99 | 0.52 | 267 |
| 2 | final4b_additive | special | 3.67 | -1.74 | -2.98 | 0.49 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final4b_boosting | special | 3.86 | -1.50 | -2.78 | 0.47 | 267 |
| 5 | final4b_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final4b | all | 0.386 | 1.317 | 0.393 | 0.889 | 11.592 | 0.891 | 7815 |
| final4b | events | 0.452 | 1.905 | 0.663 | 0.761 | 11.922 | 0.804 | 107 |
| final4b | cold_mornings | 0.451 | 1.655 | 0.528 | 0.834 | 12.872 | 0.821 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final4b | 8.40 | -9.99 | -9.99 |
| 13224 | DUK | 2022-12-24 | final4b_additive | 7.22 | -13.03 | -13.03 |
| 13225 | DUK | 2022-12-24 | final4b_boosting | 9.94 | -18.11 | -18.11 |
| 13227 | DUK | 2022-12-24 | final4b_ensemble | 8.73 | -13.75 | -13.75 |
| 13226 | DUK | 2022-12-24 | final4b_recency | 9.27 | -9.99 | -9.99 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final4b | 32.63 | 25.83 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final4b_additive | 32.00 | 28.88 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final4b_boosting | 29.43 | 23.23 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final4b_ensemble | 33.40 | 28.75 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final4b_recency | 41.20 | 36.68 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final4b | 5.20 | 3.86 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final4b_additive | 13.29 | 11.84 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final4b_boosting | 2.85 | -4.49 | -4.49 |
| 13725 | ERCO | 2021-02-18 | final4b_ensemble | 5.89 | 2.95 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final4b_recency | 5.36 | 2.19 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final4b | 2.06 | 1.89 | 0.00 |
| 26664 | MISO | 2021-02-16 | final4b_additive | 2.38 | 2.18 | 0.00 |
| 26665 | MISO | 2021-02-16 | final4b_boosting | 3.00 | 1.40 | 0.00 |
| 26667 | MISO | 2021-02-16 | final4b_ensemble | 2.07 | 0.75 | 0.00 |
| 26666 | MISO | 2021-02-16 | final4b_recency | 3.61 | -2.07 | -2.07 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final4b | 2.99 | -2.69 | -2.69 |
| 39984 | SWPP | 2021-02-15 | final4b_additive | 2.24 | 1.30 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final4b_boosting | 6.24 | -8.04 | -8.04 |
| 39987 | SWPP | 2021-02-15 | final4b_ensemble | 3.08 | -3.88 | -3.88 |
| 39986 | SWPP | 2021-02-15 | final4b_recency | 4.81 | -5.28 | -5.28 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final4b | 3.92 | 0.01 | 0.00 |
| 39990 | SWPP | 2021-02-16 | final4b_additive | 7.74 | 3.67 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final4b_boosting | 3.17 | -5.68 | -5.68 |
| 39993 | SWPP | 2021-02-16 | final4b_ensemble | 3.90 | -0.63 | -0.63 |
| 39992 | SWPP | 2021-02-16 | final4b_recency | 2.57 | -0.10 | -0.10 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final4b | 8.87 | -11.20 | -11.20 |
| 48330 | TVA | 2022-12-23 | final4b_additive | 7.33 | -3.19 | -3.19 |
| 48331 | TVA | 2022-12-23 | final4b_boosting | 14.13 | -15.65 | -15.65 |
| 48333 | TVA | 2022-12-23 | final4b_ensemble | 8.41 | -9.50 | -9.50 |
| 48332 | TVA | 2022-12-23 | final4b_recency | 11.83 | -10.22 | -10.22 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final4b | 6.00 | -11.71 | -11.71 |
| 48336 | TVA | 2022-12-24 | final4b_additive | 3.82 | -9.06 | -9.06 |
| 48337 | TVA | 2022-12-24 | final4b_boosting | 7.33 | -15.53 | -15.53 |
| 48339 | TVA | 2022-12-24 | final4b_ensemble | 5.90 | -11.89 | -11.89 |
| 48338 | TVA | 2022-12-24 | final4b_recency | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final4b | BPAT | mape | 7.577 | 0.000 | 746 |
| final4b | CISO | mape | 0.884 | 0.377 | 719 |
| final4b | DUK | mape | 5.637 | 0.000 | 746 |
| final4b | ERCO | mape | -0.159 | 0.874 | 742 |
| final4b | FPL | mape | -3.053 | 0.002 | 665 |
| final4b | ISNE | mape | 13.782 | 0.000 | 748 |
| final4b | MISO | mape | -10.474 | 0.000 | 738 |
| final4b | NYIS | mape | -6.524 | 0.000 | 748 |
| final4b | PJM | mape | -5.812 | 0.000 | 734 |
| final4b | SWPP | mape | -18.262 | 0.000 | 741 |
| final4b | TVA | mape | 11.734 | 0.000 | 729 |
| final4b_additive | BPAT | mape | 11.205 | 0.000 | 746 |
| final4b_additive | CISO | mape | 15.445 | 0.000 | 719 |
| final4b_additive | DUK | mape | 8.372 | 0.000 | 746 |
| final4b_additive | ERCO | mape | 11.984 | 0.000 | 742 |
| final4b_additive | FPL | mape | 16.155 | 0.000 | 665 |
| final4b_additive | ISNE | mape | 19.161 | 0.000 | 748 |
| final4b_additive | MISO | mape | -5.549 | 0.000 | 738 |
| final4b_additive | NYIS | mape | -1.852 | 0.064 | 748 |
| final4b_additive | PJM | mape | 2.986 | 0.003 | 734 |
| final4b_additive | SWPP | mape | -15.322 | 0.000 | 741 |
| final4b_additive | TVA | mape | 15.810 | 0.000 | 729 |
| final4b_boosting | BPAT | mape | 11.871 | 0.000 | 746 |
| final4b_boosting | CISO | mape | 7.457 | 0.000 | 719 |
| final4b_boosting | DUK | mape | 8.043 | 0.000 | 746 |
| final4b_boosting | ERCO | mape | 4.737 | 0.000 | 742 |
| final4b_boosting | FPL | mape | 18.355 | 0.000 | 665 |
| final4b_boosting | ISNE | mape | 16.837 | 0.000 | 748 |
| final4b_boosting | MISO | mape | -6.347 | 0.000 | 738 |
| final4b_boosting | NYIS | mape | -1.745 | 0.081 | 748 |
| final4b_boosting | PJM | mape | 3.653 | 0.000 | 734 |
| final4b_boosting | SWPP | mape | -13.047 | 0.000 | 741 |
| final4b_boosting | TVA | mape | 14.983 | 0.000 | 729 |
| final4b_ensemble | BPAT | mape | 8.383 | 0.000 | 746 |
| final4b_ensemble | CISO | mape | 11.396 | 0.000 | 719 |
| final4b_ensemble | DUK | mape | 6.305 | 0.000 | 746 |
| final4b_ensemble | ERCO | mape | 5.830 | 0.000 | 742 |
| final4b_ensemble | FPL | mape | 18.432 | 0.000 | 665 |
| final4b_ensemble | ISNE | mape | 17.389 | 0.000 | 748 |
| final4b_ensemble | MISO | mape | -7.971 | 0.000 | 738 |
| final4b_ensemble | NYIS | mape | -5.728 | 0.000 | 748 |
| final4b_ensemble | PJM | mape | -0.652 | 0.514 | 734 |
| final4b_ensemble | SWPP | mape | -17.872 | 0.000 | 741 |
| final4b_ensemble | TVA | mape | 13.296 | 0.000 | 729 |
| final4b_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final4b_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final4b_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final4b_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final4b_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final4b_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final4b_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final4b_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final4b_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final4b_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final4b_recency | TVA | mape | 20.369 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final4b | 0.987 |
| final4b_additive | 0.965 |
| final4b_boosting | 0.987 |
| final4b_ensemble | 0.987 |
| final4b_recency | 0.987 |
