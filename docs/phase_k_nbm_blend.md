# Phase K: the NBM temperature averaged with the HRRR

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final6n` averages the NBM 2 m temperature at the stations with the HRRR path hour by hour; `final6r` uses the NBM where it has the hour and the HRRR elsewhere; `final6p` keeps the HRRR path and reads the cold-day peak rule from the NBM 5th-percentile 18-hour minimum. NBM files: one GeoTIFF per element and forecast hour in the public archive, hourly to 36 h and three-hourly beyond (interpolated). Compare with `docs/phase_i_final.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6n | 2.28 | 1.95 | -0.03 | -1.23 | 1.15 | 0.60 | 0.29 | -46.48 | 8056 | 11.00 |
| final6n_ensemble | 2.54 | 2.23 | -1.70 | -2.28 | 1.14 | 0.54 | 0.20 | -50.07 | 8056 | 11.00 |
| final6n_boosting | 2.59 | 2.30 | -1.31 | -2.08 | 1.30 | 0.51 | 0.22 | -49.76 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final6n_additive | 2.83 | 2.51 | -1.94 | -2.59 | 1.19 | 0.47 | 0.19 | -48.93 | 8056 | 11.00 |
| final6n_recency | 3.44 | 3.07 | -2.03 | -2.79 | 1.45 | 0.35 | 0.19 | -51.75 | 8056 | 11.00 |

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
| final6n | BPAT | 2.30 | 2.03 | -0.43 | -1.37 | 1.69 | -17.14 | 0.43 | 0.24 | 746 | 6536.52 |
| final6n | CISO | 2.34 | 2.03 | 0.27 | -1.05 | 0.33 | -12.03 | 0.54 | 0.26 | 719 | 25193.76 |
| final6n | DUK | 2.85 | 2.47 | -0.02 | -1.54 | 1.21 | -12.25 | 0.49 | 0.31 | 746 | 12143.29 |
| final6n | ERCO | 2.46 | 1.97 | -0.09 | -1.35 | 0.88 | -15.85 | 0.53 | 0.27 | 742 | 46834.59 |
| final6n | FPL | 3.52 | 2.95 | -0.59 | -2.26 | 1.00 | -46.48 | 0.62 | 0.68 | 665 | 15346.05 |
| final6n | ISNE | 3.08 | 2.72 | 0.27 | -1.26 | 0.50 | -13.10 | 0.37 | 0.20 | 748 | 13403.92 |
| final6n | MISO | 1.95 | 1.70 | 0.07 | -0.98 | 1.52 | -6.92 | 0.64 | 0.06 | 738 | 73700.16 |
| final6n | NYIS | 2.20 | 1.93 | -0.02 | -1.26 | 0.53 | -13.94 | 0.64 | 0.74 | 748 | 17415.28 |
| final6n | PJM | 2.04 | 1.78 | -0.11 | -1.19 | 1.34 | -10.13 | 0.64 | 0.42 | 734 | 92076.14 |
| final6n | SWPP | 2.13 | 1.74 | -0.20 | -1.24 | 1.34 | -20.02 | 0.75 | 0.10 | 741 | 31382.01 |
| final6n | TVA | 2.63 | 2.23 | 0.41 | -1.24 | 1.26 | -11.14 | 0.38 | 0.33 | 729 | 18581.23 |
| final6n_additive | BPAT | 2.50 | 2.19 | -1.02 | -1.77 | 1.73 | -16.72 | 0.35 | 0.21 | 746 | 6536.52 |
| final6n_additive | CISO | 3.28 | 2.80 | -2.84 | -3.42 | 0.40 | -16.18 | 0.32 | 0.11 | 719 | 25193.76 |
| final6n_additive | DUK | 3.08 | 2.75 | -2.04 | -2.85 | 1.28 | -16.03 | 0.44 | 0.20 | 746 | 12143.29 |
| final6n_additive | ERCO | 3.44 | 3.03 | -2.77 | -3.35 | 0.96 | -16.57 | 0.33 | 0.12 | 742 | 46834.59 |
| final6n_additive | FPL | 5.44 | 4.97 | -5.76 | -6.22 | 1.01 | -48.93 | 0.35 | 0.27 | 665 | 15346.05 |
| final6n_additive | ISNE | 3.52 | 3.21 | -1.73 | -2.56 | 0.53 | -16.96 | 0.26 | 0.13 | 748 | 13403.92 |
| final6n_additive | MISO | 2.25 | 1.98 | -1.53 | -2.02 | 1.46 | -9.48 | 0.57 | 0.04 | 738 | 73700.16 |
| final6n_additive | NYIS | 2.55 | 2.22 | -1.45 | -2.29 | 0.53 | -15.21 | 0.55 | 0.57 | 748 | 17415.28 |
| final6n_additive | PJM | 2.47 | 2.25 | -1.24 | -1.98 | 1.44 | -12.16 | 0.52 | 0.33 | 734 | 92076.14 |
| final6n_additive | SWPP | 2.38 | 2.01 | -1.58 | -2.23 | 1.35 | -21.65 | 0.70 | 0.07 | 741 | 31382.01 |
| final6n_additive | TVA | 3.01 | 2.70 | -2.05 | -2.80 | 1.33 | -14.04 | 0.30 | 0.16 | 729 | 18581.23 |
| final6n_boosting | BPAT | 2.37 | 2.13 | -0.96 | -1.74 | 1.78 | -16.84 | 0.36 | 0.22 | 746 | 6536.52 |
| final6n_boosting | CISO | 2.72 | 2.39 | -1.62 | -2.22 | 0.41 | -15.48 | 0.42 | 0.16 | 719 | 25193.76 |
| final6n_boosting | DUK | 2.98 | 2.63 | -1.34 | -2.35 | 1.27 | -14.52 | 0.43 | 0.23 | 746 | 12143.29 |
| final6n_boosting | ERCO | 2.77 | 2.37 | -2.44 | -2.94 | 1.17 | -19.79 | 0.42 | 0.15 | 742 | 46834.59 |
| final6n_boosting | FPL | 5.11 | 4.84 | -5.79 | -6.09 | 1.24 | -49.76 | 0.36 | 0.29 | 665 | 15346.05 |
| final6n_boosting | ISNE | 3.25 | 3.00 | -0.76 | -1.75 | 0.54 | -16.45 | 0.33 | 0.16 | 748 | 13403.92 |
| final6n_boosting | MISO | 2.13 | 1.86 | -0.81 | -1.51 | 1.61 | -10.15 | 0.60 | 0.05 | 738 | 73700.16 |
| final6n_boosting | NYIS | 2.38 | 2.11 | -0.56 | -1.46 | 0.70 | -11.96 | 0.58 | 0.70 | 748 | 17415.28 |
| final6n_boosting | PJM | 2.35 | 2.16 | -0.55 | -1.51 | 1.49 | -11.96 | 0.55 | 0.38 | 734 | 92076.14 |
| final6n_boosting | SWPP | 2.41 | 2.03 | -1.51 | -2.24 | 1.52 | -29.36 | 0.70 | 0.06 | 741 | 31382.01 |
| final6n_boosting | TVA | 2.76 | 2.34 | -0.96 | -1.95 | 1.34 | -12.55 | 0.34 | 0.22 | 729 | 18581.23 |
| final6n_ensemble | BPAT | 2.29 | 2.03 | -1.15 | -1.78 | 1.64 | -17.36 | 0.42 | 0.20 | 746 | 6536.52 |
| final6n_ensemble | CISO | 2.98 | 2.55 | -2.64 | -3.01 | 0.37 | -15.35 | 0.39 | 0.09 | 719 | 25193.76 |
| final6n_ensemble | DUK | 2.84 | 2.48 | -1.50 | -2.40 | 1.22 | -13.85 | 0.50 | 0.22 | 746 | 12143.29 |
| final6n_ensemble | ERCO | 2.86 | 2.44 | -2.60 | -3.01 | 0.88 | -15.64 | 0.41 | 0.13 | 742 | 46834.59 |
| final6n_ensemble | FPL | 5.45 | 5.01 | -6.37 | -6.66 | 1.04 | -50.07 | 0.36 | 0.24 | 665 | 15346.05 |
| final6n_ensemble | ISNE | 3.27 | 3.03 | -1.77 | -2.36 | 0.52 | -16.86 | 0.28 | 0.11 | 748 | 13403.92 |
| final6n_ensemble | MISO | 2.06 | 1.83 | -1.25 | -1.72 | 1.55 | -9.29 | 0.62 | 0.04 | 738 | 73700.16 |
| final6n_ensemble | NYIS | 2.26 | 1.97 | -0.96 | -1.72 | 0.54 | -13.55 | 0.61 | 0.65 | 748 | 17415.28 |
| final6n_ensemble | PJM | 2.22 | 1.97 | -0.96 | -1.67 | 1.25 | -11.19 | 0.61 | 0.36 | 734 | 92076.14 |
| final6n_ensemble | SWPP | 2.11 | 1.71 | -1.25 | -1.86 | 1.31 | -20.20 | 0.74 | 0.06 | 741 | 31382.01 |
| final6n_ensemble | TVA | 2.66 | 2.33 | -1.49 | -2.27 | 1.20 | -12.74 | 0.36 | 0.17 | 729 | 18581.23 |
| final6n_recency | BPAT | 3.03 | 2.66 | -1.60 | -2.29 | 1.84 | -18.60 | 0.26 | 0.19 | 746 | 6536.52 |
| final6n_recency | CISO | 5.30 | 5.08 | -4.42 | -4.70 | 0.66 | -15.56 | 0.07 | 0.06 | 719 | 25193.76 |
| final6n_recency | DUK | 3.45 | 3.09 | -1.07 | -2.47 | 1.47 | -15.09 | 0.35 | 0.24 | 746 | 12143.29 |
| final6n_recency | ERCO | 3.48 | 2.98 | -2.74 | -3.36 | 1.05 | -19.11 | 0.30 | 0.15 | 742 | 46834.59 |
| final6n_recency | FPL | 6.76 | 6.00 | -8.06 | -8.36 | 1.20 | -51.75 | 0.25 | 0.20 | 665 | 15346.05 |
| final6n_recency | ISNE | 5.17 | 4.89 | -3.45 | -3.94 | 0.70 | -18.25 | 0.05 | 0.07 | 748 | 13403.92 |
| final6n_recency | MISO | 2.84 | 2.52 | -1.57 | -2.11 | 2.04 | -13.38 | 0.43 | 0.05 | 738 | 73700.16 |
| final6n_recency | NYIS | 3.42 | 3.08 | -0.96 | -2.05 | 0.81 | -18.20 | 0.36 | 0.59 | 748 | 17415.28 |
| final6n_recency | PJM | 2.89 | 2.58 | -1.14 | -2.04 | 1.62 | -17.18 | 0.38 | 0.33 | 734 | 92076.14 |
| final6n_recency | SWPP | 2.76 | 2.32 | -0.59 | -1.71 | 1.58 | -18.50 | 0.65 | 0.09 | 741 | 31382.01 |
| final6n_recency | TVA | 3.24 | 2.87 | -1.53 | -2.65 | 1.24 | -15.53 | 0.23 | 0.19 | 729 | 18581.23 |

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
| final6n | BPAT | uri | 2.32 | -0.55 | -1.09 | -4.88 | 6 |
| final6n | CISO | uri | 1.93 | -0.23 | -0.89 | -2.18 | 6 |
| final6n | DUK | uri | 3.56 | -2.07 | -2.28 | -5.52 | 6 |
| final6n | ERCO | uri | 6.80 | -8.87 | -8.87 | -9.79 | 2 |
| final6n | FPL | uri | 8.10 | -8.26 | -8.26 | -11.43 | 6 |
| final6n | ISNE | uri | 2.57 | 1.53 | -0.05 | -0.29 | 6 |
| final6n | MISO | uri | 3.92 | -3.35 | -3.48 | -6.92 | 5 |
| final6n | NYIS | uri | 2.13 | 2.22 | -0.07 | -0.45 | 6 |
| final6n | PJM | uri | 1.73 | 0.07 | -0.57 | -2.63 | 6 |
| final6n | SWPP | uri | 6.11 | 0.32 | -2.69 | -6.03 | 4 |
| final6n | TVA | uri | 3.81 | -1.25 | -2.39 | -6.16 | 6 |
| final6n_additive | BPAT | uri | 2.69 | -0.91 | -1.24 | -2.17 | 6 |
| final6n_additive | CISO | uri | 2.13 | 1.15 | -0.10 | -0.58 | 6 |
| final6n_additive | DUK | uri | 3.43 | -2.90 | -2.90 | -3.67 | 6 |
| final6n_additive | ERCO | uri | 5.26 | -6.89 | -6.89 | -9.48 | 2 |
| final6n_additive | FPL | uri | 9.94 | -14.30 | -14.30 | -17.55 | 6 |
| final6n_additive | ISNE | uri | 2.50 | 1.24 | -0.19 | -1.17 | 6 |
| final6n_additive | MISO | uri | 3.65 | -2.66 | -3.20 | -6.58 | 5 |
| final6n_additive | NYIS | uri | 2.54 | 2.71 | 0.00 | 0.00 | 6 |
| final6n_additive | PJM | uri | 2.82 | 2.27 | -0.40 | -2.43 | 6 |
| final6n_additive | SWPP | uri | 6.11 | 2.05 | -1.66 | -4.46 | 4 |
| final6n_additive | TVA | uri | 3.85 | -0.54 | -1.94 | -5.78 | 6 |
| final6n_boosting | BPAT | uri | 2.67 | 0.19 | -1.32 | -5.67 | 6 |
| final6n_boosting | CISO | uri | 2.04 | -0.98 | -1.37 | -3.70 | 6 |
| final6n_boosting | DUK | uri | 3.38 | -3.25 | -3.25 | -6.53 | 6 |
| final6n_boosting | ERCO | uri | 8.66 | -13.62 | -13.62 | -15.74 | 2 |
| final6n_boosting | FPL | uri | 7.93 | -9.98 | -9.98 | -13.08 | 6 |
| final6n_boosting | ISNE | uri | 3.53 | 1.27 | -0.47 | -1.79 | 6 |
| final6n_boosting | MISO | uri | 2.65 | -2.90 | -2.95 | -5.31 | 5 |
| final6n_boosting | NYIS | uri | 2.64 | 1.19 | -0.44 | -2.67 | 6 |
| final6n_boosting | PJM | uri | 1.57 | -0.86 | -1.04 | -2.57 | 6 |
| final6n_boosting | SWPP | uri | 4.88 | -3.23 | -3.99 | -9.76 | 4 |
| final6n_boosting | TVA | uri | 3.09 | -2.51 | -2.51 | -6.09 | 6 |
| final6n_ensemble | BPAT | uri | 2.34 | -0.39 | -0.85 | -4.18 | 6 |
| final6n_ensemble | CISO | uri | 1.88 | -0.48 | -0.98 | -1.98 | 6 |
| final6n_ensemble | DUK | uri | 3.56 | -3.52 | -3.52 | -4.97 | 6 |
| final6n_ensemble | ERCO | uri | 6.37 | -8.95 | -8.95 | -10.44 | 2 |
| final6n_ensemble | FPL | uri | 9.87 | -13.10 | -13.10 | -16.14 | 6 |
| final6n_ensemble | ISNE | uri | 2.28 | 0.20 | -0.50 | -1.88 | 6 |
| final6n_ensemble | MISO | uri | 3.77 | -3.70 | -3.70 | -7.05 | 5 |
| final6n_ensemble | NYIS | uri | 2.18 | 1.98 | -0.09 | -0.56 | 6 |
| final6n_ensemble | PJM | uri | 2.00 | 0.55 | -0.56 | -3.05 | 6 |
| final6n_ensemble | SWPP | uri | 5.83 | -1.17 | -3.33 | -7.31 | 4 |
| final6n_ensemble | TVA | uri | 3.49 | -1.61 | -2.28 | -5.65 | 6 |
| final6n_recency | BPAT | uri | 2.60 | -0.58 | -0.97 | -4.69 | 6 |
| final6n_recency | CISO | uri | 3.64 | -1.65 | -1.89 | -3.45 | 6 |
| final6n_recency | DUK | uri | 4.16 | -4.42 | -4.42 | -6.02 | 6 |
| final6n_recency | ERCO | uri | 6.07 | -5.61 | -5.61 | -10.26 | 2 |
| final6n_recency | FPL | uri | 12.23 | -15.63 | -15.63 | -18.55 | 6 |
| final6n_recency | ISNE | uri | 3.79 | -2.64 | -2.64 | -4.23 | 6 |
| final6n_recency | MISO | uri | 6.74 | -6.06 | -6.06 | -9.68 | 5 |
| final6n_recency | NYIS | uri | 2.44 | 1.98 | -0.03 | -0.17 | 6 |
| final6n_recency | PJM | uri | 2.45 | 0.50 | -0.84 | -4.36 | 6 |
| final6n_recency | SWPP | uri | 6.47 | -2.75 | -4.55 | -10.56 | 4 |
| final6n_recency | TVA | uri | 4.13 | -1.79 | -2.76 | -5.91 | 6 |
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
| final6n | BPAT | elliott | 2.88 | -1.99 | -2.27 | -6.12 | 5 |
| final6n | CISO | elliott | 3.35 | 2.09 | -0.66 | -3.26 | 5 |
| final6n | DUK | elliott | 3.05 | -2.02 | -2.09 | -5.33 | 4 |
| final6n | ERCO | elliott | 5.82 | -2.20 | -3.41 | -9.26 | 5 |
| final6n | FPL | elliott | 5.34 | -5.31 | -5.31 | -8.93 | 5 |
| final6n | ISNE | elliott | 3.37 | 2.57 | -0.52 | -1.48 | 5 |
| final6n | MISO | elliott | 3.44 | -2.44 | -3.16 | -6.34 | 5 |
| final6n | NYIS | elliott | 2.77 | -0.38 | -1.40 | -3.28 | 5 |
| final6n | PJM | elliott | 4.38 | -4.23 | -4.23 | -8.83 | 5 |
| final6n | SWPP | elliott | 4.47 | 0.44 | -2.08 | -6.44 | 5 |
| final6n | TVA | elliott | 4.38 | 1.88 | 0.00 | 0.00 | 3 |
| final6n_additive | BPAT | elliott | 3.66 | -1.34 | -1.93 | -4.41 | 5 |
| final6n_additive | CISO | elliott | 3.13 | 1.49 | -0.86 | -4.32 | 5 |
| final6n_additive | DUK | elliott | 3.84 | -4.22 | -4.22 | -6.01 | 4 |
| final6n_additive | ERCO | elliott | 7.51 | -5.85 | -6.23 | -12.82 | 5 |
| final6n_additive | FPL | elliott | 8.43 | -3.26 | -5.38 | -12.69 | 5 |
| final6n_additive | ISNE | elliott | 3.62 | -0.01 | -1.37 | -4.19 | 5 |
| final6n_additive | MISO | elliott | 3.40 | -3.69 | -3.93 | -6.55 | 5 |
| final6n_additive | NYIS | elliott | 3.42 | -2.23 | -2.51 | -5.23 | 5 |
| final6n_additive | PJM | elliott | 3.32 | -2.07 | -2.07 | -7.07 | 5 |
| final6n_additive | SWPP | elliott | 3.43 | -2.69 | -2.97 | -6.30 | 5 |
| final6n_additive | TVA | elliott | 5.03 | 0.60 | -0.36 | -1.07 | 3 |
| final6n_boosting | BPAT | elliott | 3.66 | -5.15 | -5.15 | -11.50 | 5 |
| final6n_boosting | CISO | elliott | 3.52 | 1.36 | -1.05 | -4.18 | 5 |
| final6n_boosting | DUK | elliott | 4.06 | -3.65 | -3.65 | -6.28 | 4 |
| final6n_boosting | ERCO | elliott | 7.36 | -11.06 | -11.06 | -19.79 | 5 |
| final6n_boosting | FPL | elliott | 8.92 | -14.63 | -14.63 | -19.75 | 5 |
| final6n_boosting | ISNE | elliott | 3.38 | 2.05 | -0.35 | -1.07 | 5 |
| final6n_boosting | MISO | elliott | 3.41 | -2.15 | -3.06 | -4.15 | 5 |
| final6n_boosting | NYIS | elliott | 2.69 | -0.06 | -1.13 | -2.95 | 5 |
| final6n_boosting | PJM | elliott | 3.88 | -4.23 | -4.23 | -7.43 | 5 |
| final6n_boosting | SWPP | elliott | 5.62 | -2.12 | -3.98 | -12.25 | 5 |
| final6n_boosting | TVA | elliott | 4.84 | -1.16 | -1.48 | -3.79 | 3 |
| final6n_ensemble | BPAT | elliott | 3.23 | -3.25 | -3.39 | -7.71 | 5 |
| final6n_ensemble | CISO | elliott | 3.12 | 1.75 | -0.77 | -3.84 | 5 |
| final6n_ensemble | DUK | elliott | 3.52 | -4.72 | -4.72 | -5.76 | 4 |
| final6n_ensemble | ERCO | elliott | 6.33 | -7.09 | -7.14 | -11.64 | 5 |
| final6n_ensemble | FPL | elliott | 7.21 | -9.78 | -9.78 | -13.12 | 5 |
| final6n_ensemble | ISNE | elliott | 3.34 | 1.21 | -0.99 | -2.58 | 5 |
| final6n_ensemble | MISO | elliott | 3.45 | -3.61 | -3.96 | -7.19 | 5 |
| final6n_ensemble | NYIS | elliott | 2.97 | -1.48 | -2.05 | -4.12 | 5 |
| final6n_ensemble | PJM | elliott | 4.15 | -4.72 | -4.72 | -9.90 | 5 |
| final6n_ensemble | SWPP | elliott | 3.99 | -2.86 | -3.51 | -9.34 | 5 |
| final6n_ensemble | TVA | elliott | 4.37 | -0.84 | -1.54 | -2.54 | 3 |
| final6n_recency | BPAT | elliott | 3.95 | -2.95 | -3.14 | -9.68 | 5 |
| final6n_recency | CISO | elliott | 3.89 | 2.83 | -0.52 | -2.59 | 5 |
| final6n_recency | DUK | elliott | 4.06 | -6.48 | -6.48 | -9.27 | 4 |
| final6n_recency | ERCO | elliott | 4.87 | -3.15 | -3.59 | -9.01 | 5 |
| final6n_recency | FPL | elliott | 9.77 | -10.68 | -10.68 | -16.50 | 5 |
| final6n_recency | ISNE | elliott | 4.42 | 1.58 | -1.47 | -4.05 | 5 |
| final6n_recency | MISO | elliott | 5.41 | -5.85 | -5.87 | -13.38 | 5 |
| final6n_recency | NYIS | elliott | 4.33 | -2.68 | -3.10 | -5.73 | 5 |
| final6n_recency | PJM | elliott | 6.05 | -8.15 | -8.15 | -17.18 | 5 |
| final6n_recency | SWPP | elliott | 3.64 | -3.90 | -4.32 | -10.32 | 5 |
| final6n_recency | TVA | elliott | 3.92 | -2.14 | -2.96 | -4.63 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6n_ensemble | eve | 3.17 | -0.87 | -2.16 | 0.51 | 265 |
| 7 | final6n | eve | 3.22 | 0.89 | -1.30 | 0.47 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 8 | final6n_additive | eve | 3.38 | -0.70 | -2.18 | 0.48 | 265 |
| 9 | final6n_boosting | eve | 3.51 | -0.45 | -2.11 | 0.46 | 265 |
| 11 | final6n_recency | eve | 3.99 | -1.79 | -2.93 | 0.35 | 265 |
| 1 | final6n | special | 3.19 | -0.56 | -1.96 | 0.58 | 267 |
| 4 | final6n_ensemble | special | 3.29 | -2.35 | -3.13 | 0.57 | 267 |
| 2 | final6n_additive | special | 3.46 | -2.45 | -3.23 | 0.50 | 267 |
| 3 | final6n_boosting | special | 3.53 | -2.00 | -2.93 | 0.53 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 5 | final6n_recency | special | 4.27 | -2.84 | -3.89 | 0.42 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6n | all | 0.375 | 1.248 | 0.367 | 0.888 | 10.918 | 0.888 | 14.827 | 1.621 | 7825 |
| final6n | events | 0.459 | 1.888 | 0.613 | 0.761 | 11.676 | 0.739 | 21.426 | 2.465 | 111 |
| final6n | cold_mornings | 0.439 | 1.564 | 0.516 | 0.834 | 12.233 | 0.824 | 19.093 | 2.070 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final6n | 9.30 | -11.05 | -11.05 |
| 13224 | DUK | 2022-12-24 | final6n_additive | 8.55 | -12.75 | -12.75 |
| 13225 | DUK | 2022-12-24 | final6n_boosting | 10.59 | -17.09 | -17.09 |
| 13227 | DUK | 2022-12-24 | final6n_ensemble | 9.74 | -13.70 | -13.70 |
| 13226 | DUK | 2022-12-24 | final6n_recency | 10.34 | -11.13 | -11.13 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final6n | 31.32 | 24.63 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final6n_additive | 29.56 | 25.22 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final6n_boosting | 28.85 | 23.03 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final6n_ensemble | 31.66 | 26.12 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final6n_recency | 38.48 | 31.79 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final6n | 4.04 | 2.60 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final6n_additive | 13.29 | 11.84 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final6n_boosting | 4.23 | -7.71 | -7.71 |
| 13725 | ERCO | 2021-02-18 | final6n_ensemble | 4.36 | 1.56 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final6n_recency | 5.36 | 2.19 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final6n | 1.60 | 1.34 | 0.00 |
| 26664 | MISO | 2021-02-16 | final6n_additive | 2.24 | 2.04 | 0.00 |
| 26665 | MISO | 2021-02-16 | final6n_boosting | 1.52 | 0.96 | 0.00 |
| 26667 | MISO | 2021-02-16 | final6n_ensemble | 1.56 | 0.52 | 0.00 |
| 26666 | MISO | 2021-02-16 | final6n_recency | 3.83 | -2.20 | -2.20 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final6n | 2.66 | -2.34 | -2.34 |
| 39984 | SWPP | 2021-02-15 | final6n_additive | 2.57 | 1.33 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final6n_boosting | 6.68 | -8.01 | -8.01 |
| 39987 | SWPP | 2021-02-15 | final6n_ensemble | 2.89 | -3.73 | -3.73 |
| 39986 | SWPP | 2021-02-15 | final6n_recency | 4.67 | -4.95 | -4.95 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final6n | 3.93 | -0.28 | -0.28 |
| 39990 | SWPP | 2021-02-16 | final6n_additive | 7.69 | 3.65 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final6n_boosting | 3.28 | -6.32 | -6.32 |
| 39993 | SWPP | 2021-02-16 | final6n_ensemble | 3.79 | -0.91 | -0.91 |
| 39992 | SWPP | 2021-02-16 | final6n_recency | 2.38 | -0.44 | -0.44 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final6n | 8.65 | -10.62 | -10.62 |
| 48330 | TVA | 2022-12-23 | final6n_additive | 6.41 | -3.28 | -3.28 |
| 48331 | TVA | 2022-12-23 | final6n_boosting | 15.84 | -16.78 | -16.78 |
| 48333 | TVA | 2022-12-23 | final6n_ensemble | 8.88 | -10.21 | -10.21 |
| 48332 | TVA | 2022-12-23 | final6n_recency | 10.04 | -11.25 | -11.25 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final6n | 5.81 | -11.61 | -11.61 |
| 48336 | TVA | 2022-12-24 | final6n_additive | 3.83 | -9.09 | -9.09 |
| 48337 | TVA | 2022-12-24 | final6n_boosting | 7.66 | -15.18 | -15.18 |
| 48339 | TVA | 2022-12-24 | final6n_ensemble | 6.20 | -12.11 | -12.11 |
| 48338 | TVA | 2022-12-24 | final6n_recency | 7.58 | -12.30 | -12.30 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6n | BPAT | mape | 4.716 | 0.000 | 746 |
| final6n | CISO | mape | -1.048 | 0.295 | 719 |
| final6n | DUK | mape | 0.154 | 0.878 | 746 |
| final6n | ERCO | mape | -2.876 | 0.004 | 742 |
| final6n | FPL | mape | -3.891 | 0.000 | 665 |
| final6n | ISNE | mape | 12.419 | 0.000 | 748 |
| final6n | MISO | mape | -11.772 | 0.000 | 738 |
| final6n | NYIS | mape | -7.527 | 0.000 | 748 |
| final6n | PJM | mape | -8.462 | 0.000 | 734 |
| final6n | SWPP | mape | -19.619 | 0.000 | 741 |
| final6n | TVA | mape | 8.370 | 0.000 | 729 |
| final6n_additive | BPAT | mape | 8.480 | 0.000 | 746 |
| final6n_additive | CISO | mape | 12.842 | 0.000 | 719 |
| final6n_additive | DUK | mape | 3.930 | 0.000 | 746 |
| final6n_additive | ERCO | mape | 10.742 | 0.000 | 742 |
| final6n_additive | FPL | mape | 12.713 | 0.000 | 665 |
| final6n_additive | ISNE | mape | 18.826 | 0.000 | 748 |
| final6n_additive | MISO | mape | -5.697 | 0.000 | 738 |
| final6n_additive | NYIS | mape | -2.024 | 0.043 | 748 |
| final6n_additive | PJM | mape | 0.199 | 0.842 | 734 |
| final6n_additive | SWPP | mape | -15.456 | 0.000 | 741 |
| final6n_additive | TVA | mape | 13.672 | 0.000 | 729 |
| final6n_boosting | BPAT | mape | 6.651 | 0.000 | 746 |
| final6n_boosting | CISO | mape | 5.426 | 0.000 | 719 |
| final6n_boosting | DUK | mape | 2.400 | 0.016 | 746 |
| final6n_boosting | ERCO | mape | 2.228 | 0.026 | 742 |
| final6n_boosting | FPL | mape | 11.544 | 0.000 | 665 |
| final6n_boosting | ISNE | mape | 15.311 | 0.000 | 748 |
| final6n_boosting | MISO | mape | -8.074 | 0.000 | 738 |
| final6n_boosting | NYIS | mape | -4.684 | 0.000 | 748 |
| final6n_boosting | PJM | mape | -2.057 | 0.040 | 734 |
| final6n_boosting | SWPP | mape | -14.524 | 0.000 | 741 |
| final6n_boosting | TVA | mape | 10.505 | 0.000 | 729 |
| final6n_ensemble | BPAT | mape | 4.738 | 0.000 | 746 |
| final6n_ensemble | CISO | mape | 9.124 | 0.000 | 719 |
| final6n_ensemble | DUK | mape | -0.019 | 0.985 | 746 |
| final6n_ensemble | ERCO | mape | 3.439 | 0.001 | 742 |
| final6n_ensemble | FPL | mape | 13.018 | 0.000 | 665 |
| final6n_ensemble | ISNE | mape | 16.442 | 0.000 | 748 |
| final6n_ensemble | MISO | mape | -8.731 | 0.000 | 738 |
| final6n_ensemble | NYIS | mape | -7.165 | 0.000 | 748 |
| final6n_ensemble | PJM | mape | -4.942 | 0.000 | 734 |
| final6n_ensemble | SWPP | mape | -19.358 | 0.000 | 741 |
| final6n_ensemble | TVA | mape | 8.721 | 0.000 | 729 |
| final6n_recency | BPAT | mape | 15.406 | 0.000 | 746 |
| final6n_recency | CISO | mape | 36.743 | 0.000 | 719 |
| final6n_recency | DUK | mape | 9.505 | 0.000 | 746 |
| final6n_recency | ERCO | mape | 10.661 | 0.000 | 742 |
| final6n_recency | FPL | mape | 18.297 | 0.000 | 665 |
| final6n_recency | ISNE | mape | 37.408 | 0.000 | 748 |
| final6n_recency | MISO | mape | 2.465 | 0.014 | 738 |
| final6n_recency | NYIS | mape | 10.390 | 0.000 | 748 |
| final6n_recency | PJM | mape | 7.743 | 0.000 | 734 |
| final6n_recency | SWPP | mape | -11.315 | 0.000 | 741 |
| final6n_recency | TVA | mape | 16.613 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final6n | 0.987 |
| final6n_additive | 0.965 |
| final6n_boosting | 0.987 |
| final6n_ensemble | 0.987 |
| final6n_recency | 0.987 |
