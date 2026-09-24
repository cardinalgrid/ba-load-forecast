# Phase H: humidity in the boosting only

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3_hp` is the phase G recipe with the humidity block in the boosting and the additive model unchanged. Compare with `docs/phase_h_humidity_only.md`, `docs/phase_h_humidity_linear.md` and `docs/phase_g_final.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_hp | 2.42 | 2.09 | 0.04 | -1.32 | 1.25 | 0.56 | 0.30 | -46.79 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final3_hp_ensemble | 2.77 | 2.43 | -1.28 | -2.15 | 1.27 | 0.49 | 0.23 | -51.26 | 8056 | 11.00 |
| final3_hp_boosting | 2.83 | 2.49 | -0.97 | -2.00 | 1.42 | 0.45 | 0.25 | -51.51 | 8056 | 11.00 |
| final3_hp_additive | 3.00 | 2.64 | -1.31 | -2.32 | 1.32 | 0.44 | 0.23 | -49.89 | 8056 | 11.00 |
| final3_hp_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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
| final3_hp | BPAT | 2.47 | 2.16 | -0.41 | -1.45 | 1.72 | -17.91 | 0.38 | 0.26 | 746 | 6536.52 |
| final3_hp | CISO | 2.45 | 2.15 | 0.37 | -1.10 | 0.34 | -12.41 | 0.49 | 0.26 | 719 | 25193.76 |
| final3_hp | DUK | 3.23 | 2.91 | -0.04 | -1.83 | 1.36 | -15.35 | 0.40 | 0.31 | 746 | 12143.29 |
| final3_hp | ERCO | 2.65 | 2.19 | 0.07 | -1.46 | 1.03 | -13.87 | 0.47 | 0.28 | 742 | 46834.59 |
| final3_hp | FPL | 3.68 | 3.21 | -0.77 | -2.60 | 1.07 | -46.79 | 0.58 | 0.64 | 665 | 15346.05 |
| final3_hp | ISNE | 3.23 | 2.82 | 0.43 | -1.28 | 0.51 | -15.04 | 0.34 | 0.21 | 748 | 13403.92 |
| final3_hp | MISO | 2.02 | 1.78 | 0.08 | -1.02 | 1.69 | -7.70 | 0.63 | 0.07 | 738 | 73700.16 |
| final3_hp | NYIS | 2.28 | 1.98 | 0.01 | -1.29 | 0.57 | -12.65 | 0.61 | 0.74 | 748 | 17415.28 |
| final3_hp | PJM | 2.17 | 1.90 | 0.02 | -1.22 | 1.40 | -10.14 | 0.60 | 0.43 | 734 | 92076.14 |
| final3_hp | SWPP | 2.21 | 1.85 | -0.19 | -1.31 | 1.45 | -20.35 | 0.74 | 0.11 | 741 | 31382.01 |
| final3_hp | TVA | 2.88 | 2.47 | 0.33 | -1.48 | 1.37 | -10.89 | 0.32 | 0.31 | 729 | 18581.23 |
| final3_hp_additive | BPAT | 2.69 | 2.37 | -0.69 | -1.66 | 1.77 | -16.93 | 0.30 | 0.22 | 746 | 6536.52 |
| final3_hp_additive | CISO | 3.62 | 3.05 | -2.90 | -3.78 | 0.43 | -17.65 | 0.28 | 0.12 | 719 | 25193.76 |
| final3_hp_additive | DUK | 3.52 | 3.15 | -0.58 | -2.30 | 1.39 | -14.98 | 0.35 | 0.26 | 746 | 12143.29 |
| final3_hp_additive | ERCO | 3.44 | 3.00 | -2.09 | -2.90 | 1.04 | -15.86 | 0.32 | 0.16 | 742 | 46834.59 |
| final3_hp_additive | FPL | 6.20 | 5.85 | -6.52 | -7.04 | 1.14 | -49.89 | 0.27 | 0.26 | 665 | 15346.05 |
| final3_hp_additive | ISNE | 3.71 | 3.31 | -1.05 | -2.38 | 0.53 | -19.32 | 0.24 | 0.16 | 748 | 13403.92 |
| final3_hp_additive | MISO | 2.34 | 2.09 | -1.21 | -1.84 | 1.60 | -8.30 | 0.55 | 0.05 | 738 | 73700.16 |
| final3_hp_additive | NYIS | 2.60 | 2.28 | -0.83 | -1.97 | 0.56 | -15.30 | 0.55 | 0.60 | 748 | 17415.28 |
| final3_hp_additive | PJM | 2.65 | 2.30 | -0.44 | -1.63 | 1.64 | -12.14 | 0.47 | 0.39 | 734 | 92076.14 |
| final3_hp_additive | SWPP | 2.52 | 2.09 | -0.19 | -1.55 | 1.50 | -20.78 | 0.70 | 0.10 | 741 | 31382.01 |
| final3_hp_additive | TVA | 3.25 | 2.89 | -0.89 | -2.22 | 1.45 | -14.41 | 0.27 | 0.25 | 729 | 18581.23 |
| final3_hp_boosting | BPAT | 2.66 | 2.41 | -0.52 | -1.60 | 1.99 | -17.63 | 0.30 | 0.25 | 746 | 6536.52 |
| final3_hp_boosting | CISO | 2.89 | 2.58 | -1.91 | -2.52 | 0.44 | -16.09 | 0.37 | 0.15 | 719 | 25193.76 |
| final3_hp_boosting | DUK | 3.32 | 2.90 | -0.97 | -2.34 | 1.40 | -18.14 | 0.37 | 0.26 | 746 | 12143.29 |
| final3_hp_boosting | ERCO | 2.96 | 2.55 | -2.43 | -2.97 | 1.33 | -19.98 | 0.36 | 0.16 | 742 | 46834.59 |
| final3_hp_boosting | FPL | 6.03 | 5.61 | -6.48 | -6.83 | 1.30 | -51.51 | 0.21 | 0.28 | 665 | 15346.05 |
| final3_hp_boosting | ISNE | 3.44 | 3.09 | -0.22 | -1.52 | 0.53 | -16.39 | 0.29 | 0.19 | 748 | 13403.92 |
| final3_hp_boosting | MISO | 2.24 | 1.92 | -0.45 | -1.33 | 1.64 | -9.61 | 0.57 | 0.06 | 738 | 73700.16 |
| final3_hp_boosting | NYIS | 2.56 | 2.27 | -0.12 | -1.32 | 0.74 | -11.42 | 0.53 | 0.73 | 748 | 17415.28 |
| final3_hp_boosting | PJM | 2.66 | 2.40 | 0.19 | -1.28 | 1.72 | -13.24 | 0.44 | 0.43 | 734 | 92076.14 |
| final3_hp_boosting | SWPP | 2.52 | 2.05 | -1.10 | -2.04 | 1.59 | -29.46 | 0.70 | 0.08 | 741 | 31382.01 |
| final3_hp_boosting | TVA | 3.08 | 2.64 | -0.60 | -1.91 | 1.50 | -12.10 | 0.30 | 0.27 | 729 | 18581.23 |
| final3_hp_ensemble | BPAT | 2.50 | 2.22 | -0.82 | -1.66 | 1.70 | -17.86 | 0.37 | 0.23 | 746 | 6536.52 |
| final3_hp_ensemble | CISO | 3.23 | 2.76 | -2.77 | -3.29 | 0.36 | -16.72 | 0.34 | 0.12 | 719 | 25193.76 |
| final3_hp_ensemble | DUK | 3.29 | 2.85 | -0.70 | -2.23 | 1.42 | -14.06 | 0.40 | 0.26 | 746 | 12143.29 |
| final3_hp_ensemble | ERCO | 3.05 | 2.62 | -2.40 | -2.96 | 1.04 | -15.35 | 0.39 | 0.16 | 742 | 46834.59 |
| final3_hp_ensemble | FPL | 6.35 | 5.95 | -7.13 | -7.45 | 1.07 | -51.26 | 0.23 | 0.24 | 665 | 15346.05 |
| final3_hp_ensemble | ISNE | 3.42 | 3.16 | -1.14 | -2.11 | 0.51 | -16.67 | 0.27 | 0.15 | 748 | 13403.92 |
| final3_hp_ensemble | MISO | 2.15 | 1.90 | -0.92 | -1.56 | 1.65 | -7.75 | 0.60 | 0.05 | 738 | 73700.16 |
| final3_hp_ensemble | NYIS | 2.34 | 2.03 | -0.47 | -1.51 | 0.55 | -13.96 | 0.59 | 0.69 | 748 | 17415.28 |
| final3_hp_ensemble | PJM | 2.45 | 2.16 | -0.27 | -1.40 | 1.52 | -10.79 | 0.53 | 0.42 | 734 | 92076.14 |
| final3_hp_ensemble | SWPP | 2.29 | 1.88 | -0.50 | -1.56 | 1.39 | -19.73 | 0.73 | 0.09 | 741 | 31382.01 |
| final3_hp_ensemble | TVA | 3.01 | 2.62 | -0.83 | -2.07 | 1.36 | -13.60 | 0.31 | 0.25 | 729 | 18581.23 |
| final3_hp_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final3_hp_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final3_hp_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final3_hp_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final3_hp_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final3_hp_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final3_hp_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final3_hp_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final3_hp_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final3_hp_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final3_hp_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |

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
| final3_hp | BPAT | uri | 2.49 | -0.43 | -0.94 | -4.69 | 6 |
| final3_hp | CISO | uri | 2.14 | -0.98 | -1.45 | -2.98 | 6 |
| final3_hp | DUK | uri | 3.60 | -1.41 | -1.92 | -3.70 | 6 |
| final3_hp | ERCO | uri | 6.45 | -7.91 | -7.91 | -8.31 | 2 |
| final3_hp | FPL | uri | 8.46 | -7.76 | -7.76 | -11.15 | 6 |
| final3_hp | ISNE | uri | 2.57 | 1.78 | -0.03 | -0.18 | 6 |
| final3_hp | MISO | uri | 3.88 | -3.33 | -3.57 | -7.09 | 5 |
| final3_hp | NYIS | uri | 2.10 | 2.20 | -0.11 | -0.68 | 6 |
| final3_hp | PJM | uri | 1.96 | 0.24 | -0.64 | -2.60 | 6 |
| final3_hp | SWPP | uri | 6.65 | -0.29 | -3.33 | -7.63 | 4 |
| final3_hp | TVA | uri | 3.60 | -1.47 | -2.68 | -6.07 | 6 |
| final3_hp_additive | BPAT | uri | 2.81 | -0.35 | -1.21 | -2.29 | 6 |
| final3_hp_additive | CISO | uri | 2.21 | 1.49 | -0.05 | -0.30 | 6 |
| final3_hp_additive | DUK | uri | 3.49 | -1.84 | -1.91 | -6.46 | 6 |
| final3_hp_additive | ERCO | uri | 4.34 | -4.90 | -4.90 | -7.68 | 2 |
| final3_hp_additive | FPL | uri | 10.53 | -15.09 | -15.09 | -18.04 | 6 |
| final3_hp_additive | ISNE | uri | 2.98 | 1.99 | -0.20 | -1.20 | 6 |
| final3_hp_additive | MISO | uri | 3.67 | -2.41 | -3.04 | -6.36 | 5 |
| final3_hp_additive | NYIS | uri | 2.66 | 3.01 | 0.00 | 0.00 | 6 |
| final3_hp_additive | PJM | uri | 3.14 | 3.01 | -0.41 | -2.47 | 6 |
| final3_hp_additive | SWPP | uri | 6.47 | 1.82 | -2.00 | -5.04 | 4 |
| final3_hp_additive | TVA | uri | 3.46 | 0.64 | -1.03 | -2.61 | 6 |
| final3_hp_boosting | BPAT | uri | 3.02 | 0.67 | -0.94 | -4.88 | 6 |
| final3_hp_boosting | CISO | uri | 2.48 | -1.79 | -2.03 | -4.80 | 6 |
| final3_hp_boosting | DUK | uri | 3.71 | -2.23 | -2.39 | -5.90 | 6 |
| final3_hp_boosting | ERCO | uri | 8.50 | -12.13 | -12.13 | -14.13 | 2 |
| final3_hp_boosting | FPL | uri | 8.44 | -10.23 | -10.23 | -13.90 | 6 |
| final3_hp_boosting | ISNE | uri | 3.92 | 2.28 | -0.13 | -0.71 | 6 |
| final3_hp_boosting | MISO | uri | 2.32 | -2.46 | -2.59 | -5.34 | 5 |
| final3_hp_boosting | NYIS | uri | 2.85 | 1.95 | -0.35 | -2.12 | 6 |
| final3_hp_boosting | PJM | uri | 2.09 | -0.31 | -0.82 | -2.01 | 6 |
| final3_hp_boosting | SWPP | uri | 5.35 | -3.53 | -4.41 | -10.11 | 4 |
| final3_hp_boosting | TVA | uri | 3.19 | -0.94 | -1.79 | -4.74 | 6 |
| final3_hp_ensemble | BPAT | uri | 2.60 | 0.03 | -0.76 | -3.83 | 6 |
| final3_hp_ensemble | CISO | uri | 1.95 | -0.45 | -0.91 | -2.08 | 6 |
| final3_hp_ensemble | DUK | uri | 3.60 | -2.47 | -2.47 | -6.45 | 6 |
| final3_hp_ensemble | ERCO | uri | 5.42 | -7.25 | -7.25 | -8.84 | 2 |
| final3_hp_ensemble | FPL | uri | 10.33 | -13.61 | -13.61 | -16.38 | 6 |
| final3_hp_ensemble | ISNE | uri | 2.52 | 0.98 | -0.29 | -1.61 | 6 |
| final3_hp_ensemble | MISO | uri | 3.65 | -3.41 | -3.42 | -6.91 | 5 |
| final3_hp_ensemble | NYIS | uri | 2.27 | 2.46 | -0.05 | -0.29 | 6 |
| final3_hp_ensemble | PJM | uri | 2.44 | 1.26 | -0.48 | -2.87 | 6 |
| final3_hp_ensemble | SWPP | uri | 6.19 | -1.39 | -3.64 | -7.75 | 4 |
| final3_hp_ensemble | TVA | uri | 3.32 | -0.32 | -1.46 | -3.41 | 6 |
| final3_hp_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final3_hp_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final3_hp_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final3_hp_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final3_hp_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final3_hp_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final3_hp_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final3_hp_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final3_hp_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final3_hp_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final3_hp_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
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
| final3_hp | BPAT | elliott | 3.07 | -1.87 | -2.32 | -5.64 | 5 |
| final3_hp | CISO | elliott | 3.59 | 2.91 | -0.47 | -2.35 | 5 |
| final3_hp | DUK | elliott | 3.13 | -1.24 | -1.47 | -4.16 | 4 |
| final3_hp | ERCO | elliott | 5.62 | -2.79 | -3.93 | -7.86 | 5 |
| final3_hp | FPL | elliott | 6.06 | -6.89 | -6.89 | -12.17 | 5 |
| final3_hp | ISNE | elliott | 3.54 | 2.61 | -0.67 | -2.33 | 5 |
| final3_hp | MISO | elliott | 3.52 | -2.58 | -3.28 | -7.70 | 5 |
| final3_hp | NYIS | elliott | 2.86 | -0.90 | -1.72 | -3.91 | 5 |
| final3_hp | PJM | elliott | 4.59 | -4.39 | -4.39 | -9.46 | 5 |
| final3_hp | SWPP | elliott | 4.27 | 0.30 | -2.09 | -6.40 | 5 |
| final3_hp | TVA | elliott | 5.12 | 4.16 | 0.00 | 0.00 | 3 |
| final3_hp_additive | BPAT | elliott | 3.64 | -1.16 | -2.00 | -4.21 | 5 |
| final3_hp_additive | CISO | elliott | 3.47 | 3.77 | -0.32 | -1.61 | 5 |
| final3_hp_additive | DUK | elliott | 4.58 | -3.41 | -3.41 | -5.07 | 4 |
| final3_hp_additive | ERCO | elliott | 7.48 | -5.62 | -6.17 | -14.01 | 5 |
| final3_hp_additive | FPL | elliott | 10.32 | -0.39 | -5.39 | -13.75 | 5 |
| final3_hp_additive | ISNE | elliott | 3.84 | 2.32 | -0.91 | -2.27 | 5 |
| final3_hp_additive | MISO | elliott | 3.36 | -3.29 | -3.60 | -7.71 | 5 |
| final3_hp_additive | NYIS | elliott | 3.13 | -0.97 | -2.04 | -4.49 | 5 |
| final3_hp_additive | PJM | elliott | 3.53 | -0.16 | -0.93 | -4.57 | 5 |
| final3_hp_additive | SWPP | elliott | 3.00 | -2.57 | -2.84 | -5.40 | 5 |
| final3_hp_additive | TVA | elliott | 5.91 | 3.10 | -0.19 | -0.57 | 3 |
| final3_hp_boosting | BPAT | elliott | 4.31 | -4.47 | -4.63 | -10.92 | 5 |
| final3_hp_boosting | CISO | elliott | 4.05 | 1.78 | -0.93 | -4.24 | 5 |
| final3_hp_boosting | DUK | elliott | 4.61 | -3.06 | -3.06 | -6.88 | 4 |
| final3_hp_boosting | ERCO | elliott | 7.14 | -9.31 | -9.31 | -19.98 | 5 |
| final3_hp_boosting | FPL | elliott | 8.80 | -14.67 | -14.67 | -20.48 | 5 |
| final3_hp_boosting | ISNE | elliott | 3.75 | 3.12 | -0.14 | -0.69 | 5 |
| final3_hp_boosting | MISO | elliott | 3.53 | -1.28 | -2.27 | -4.18 | 5 |
| final3_hp_boosting | NYIS | elliott | 3.13 | 0.26 | -0.90 | -3.64 | 5 |
| final3_hp_boosting | PJM | elliott | 5.00 | -2.32 | -3.08 | -6.22 | 5 |
| final3_hp_boosting | SWPP | elliott | 5.72 | -1.57 | -4.02 | -12.13 | 5 |
| final3_hp_boosting | TVA | elliott | 6.28 | 1.24 | -0.93 | -2.78 | 3 |
| final3_hp_ensemble | BPAT | elliott | 3.62 | -2.93 | -3.26 | -7.94 | 5 |
| final3_hp_ensemble | CISO | elliott | 3.49 | 3.30 | -0.47 | -2.33 | 5 |
| final3_hp_ensemble | DUK | elliott | 3.74 | -3.93 | -3.93 | -4.89 | 4 |
| final3_hp_ensemble | ERCO | elliott | 5.91 | -5.85 | -6.18 | -11.37 | 5 |
| final3_hp_ensemble | FPL | elliott | 6.99 | -8.26 | -8.26 | -12.17 | 5 |
| final3_hp_ensemble | ISNE | elliott | 3.54 | 3.01 | -0.49 | -1.94 | 5 |
| final3_hp_ensemble | MISO | elliott | 3.42 | -3.09 | -3.49 | -7.63 | 5 |
| final3_hp_ensemble | NYIS | elliott | 2.90 | -0.74 | -1.75 | -3.79 | 5 |
| final3_hp_ensemble | PJM | elliott | 4.29 | -3.52 | -3.71 | -9.02 | 5 |
| final3_hp_ensemble | SWPP | elliott | 3.71 | -2.57 | -3.36 | -8.87 | 5 |
| final3_hp_ensemble | TVA | elliott | 5.38 | 2.45 | -0.94 | -1.45 | 3 |
| final3_hp_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final3_hp_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final3_hp_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final3_hp_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final3_hp_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final3_hp_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final3_hp_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final3_hp_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final3_hp_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final3_hp_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final3_hp_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final3_hp | eve | 3.33 | 0.84 | -1.44 | 0.44 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 10 | final3_hp_ensemble | eve | 3.42 | -0.41 | -2.07 | 0.47 | 265 |
| 8 | final3_hp_additive | eve | 3.67 | 0.09 | -2.01 | 0.43 | 265 |
| 9 | final3_hp_boosting | eve | 3.77 | -0.12 | -2.03 | 0.38 | 265 |
| 11 | final3_hp_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final3_hp | special | 3.35 | -0.65 | -2.14 | 0.52 | 267 |
| 4 | final3_hp_ensemble | special | 3.54 | -1.90 | -3.03 | 0.52 | 267 |
| 2 | final3_hp_additive | special | 3.70 | -1.79 | -3.04 | 0.48 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final3_hp_boosting | special | 3.83 | -1.57 | -2.79 | 0.46 | 267 |
| 5 | final3_hp_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_hp | all | 0.386 | 1.326 | 0.396 | 0.889 | 11.631 | 0.890 | 7815 |
| final3_hp | events | 0.449 | 1.903 | 0.669 | 0.764 | 11.934 | 0.794 | 107 |
| final3_hp | cold_mornings | 0.450 | 1.651 | 0.526 | 0.831 | 12.828 | 0.806 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final3_hp | 8.36 | -9.80 | -9.80 |
| 13224 | DUK | 2022-12-24 | final3_hp_additive | 6.92 | -12.48 | -12.48 |
| 13225 | DUK | 2022-12-24 | final3_hp_boosting | 9.96 | -18.19 | -18.19 |
| 13227 | DUK | 2022-12-24 | final3_hp_ensemble | 8.63 | -13.58 | -13.58 |
| 13226 | DUK | 2022-12-24 | final3_hp_recency | 9.27 | -9.99 | -9.99 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final3_hp | 31.92 | 26.00 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final3_hp_additive | 30.43 | 28.75 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final3_hp_boosting | 29.50 | 23.26 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final3_hp_ensemble | 32.86 | 28.70 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final3_hp_recency | 41.20 | 36.68 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final3_hp | 5.03 | 3.64 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final3_hp_additive | 13.30 | 11.77 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final3_hp_boosting | 2.92 | -4.68 | -4.68 |
| 13725 | ERCO | 2021-02-18 | final3_hp_ensemble | 5.84 | 2.84 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final3_hp_recency | 5.36 | 2.19 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final3_hp | 2.07 | 1.92 | 0.00 |
| 26664 | MISO | 2021-02-16 | final3_hp_additive | 2.33 | 2.19 | 0.00 |
| 26665 | MISO | 2021-02-16 | final3_hp_boosting | 3.03 | 1.40 | 0.00 |
| 26667 | MISO | 2021-02-16 | final3_hp_ensemble | 2.06 | 0.75 | 0.00 |
| 26666 | MISO | 2021-02-16 | final3_hp_recency | 3.61 | -2.07 | -2.07 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final3_hp | 2.90 | -2.64 | -2.64 |
| 39984 | SWPP | 2021-02-15 | final3_hp_additive | 2.38 | 1.40 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final3_hp_boosting | 6.23 | -8.01 | -8.01 |
| 39987 | SWPP | 2021-02-15 | final3_hp_ensemble | 3.00 | -3.81 | -3.81 |
| 39986 | SWPP | 2021-02-15 | final3_hp_recency | 4.81 | -5.28 | -5.28 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final3_hp | 3.83 | 0.08 | 0.00 |
| 39990 | SWPP | 2021-02-16 | final3_hp_additive | 7.58 | 3.67 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final3_hp_boosting | 3.13 | -5.72 | -5.72 |
| 39993 | SWPP | 2021-02-16 | final3_hp_ensemble | 3.84 | -0.61 | -0.61 |
| 39992 | SWPP | 2021-02-16 | final3_hp_recency | 2.57 | -0.10 | -0.10 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final3_hp | 9.14 | -11.15 | -11.15 |
| 48330 | TVA | 2022-12-23 | final3_hp_additive | 7.72 | -3.74 | -3.74 |
| 48331 | TVA | 2022-12-23 | final3_hp_boosting | 14.01 | -15.52 | -15.52 |
| 48333 | TVA | 2022-12-23 | final3_hp_ensemble | 8.66 | -9.62 | -9.62 |
| 48332 | TVA | 2022-12-23 | final3_hp_recency | 11.83 | -10.22 | -10.22 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final3_hp | 6.08 | -11.68 | -11.68 |
| 48336 | TVA | 2022-12-24 | final3_hp_additive | 3.92 | -9.05 | -9.05 |
| 48337 | TVA | 2022-12-24 | final3_hp_boosting | 7.32 | -15.52 | -15.52 |
| 48339 | TVA | 2022-12-24 | final3_hp_ensemble | 5.93 | -11.86 | -11.86 |
| 48338 | TVA | 2022-12-24 | final3_hp_recency | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3_hp | BPAT | mape | 7.635 | 0.000 | 746 |
| final3_hp | CISO | mape | 0.977 | 0.329 | 719 |
| final3_hp | DUK | mape | 6.054 | 0.000 | 746 |
| final3_hp | ERCO | mape | 0.389 | 0.697 | 742 |
| final3_hp | FPL | mape | -2.475 | 0.013 | 665 |
| final3_hp | ISNE | mape | 13.903 | 0.000 | 748 |
| final3_hp | MISO | mape | -10.331 | 0.000 | 738 |
| final3_hp | NYIS | mape | -6.156 | 0.000 | 748 |
| final3_hp | PJM | mape | -5.435 | 0.000 | 734 |
| final3_hp | SWPP | mape | -18.290 | 0.000 | 741 |
| final3_hp | TVA | mape | 11.940 | 0.000 | 729 |
| final3_hp_additive | BPAT | mape | 11.482 | 0.000 | 746 |
| final3_hp_additive | CISO | mape | 15.935 | 0.000 | 719 |
| final3_hp_additive | DUK | mape | 9.584 | 0.000 | 746 |
| final3_hp_additive | ERCO | mape | 10.610 | 0.000 | 742 |
| final3_hp_additive | FPL | mape | 17.818 | 0.000 | 665 |
| final3_hp_additive | ISNE | mape | 19.452 | 0.000 | 748 |
| final3_hp_additive | MISO | mape | -4.388 | 0.000 | 738 |
| final3_hp_additive | NYIS | mape | -1.084 | 0.278 | 748 |
| final3_hp_additive | PJM | mape | 3.267 | 0.001 | 734 |
| final3_hp_additive | SWPP | mape | -14.178 | 0.000 | 741 |
| final3_hp_additive | TVA | mape | 16.280 | 0.000 | 729 |
| final3_hp_boosting | BPAT | mape | 11.635 | 0.000 | 746 |
| final3_hp_boosting | CISO | mape | 7.964 | 0.000 | 719 |
| final3_hp_boosting | DUK | mape | 7.113 | 0.000 | 746 |
| final3_hp_boosting | ERCO | mape | 4.778 | 0.000 | 742 |
| final3_hp_boosting | FPL | mape | 19.065 | 0.000 | 665 |
| final3_hp_boosting | ISNE | mape | 17.090 | 0.000 | 748 |
| final3_hp_boosting | MISO | mape | -6.295 | 0.000 | 738 |
| final3_hp_boosting | NYIS | mape | -1.698 | 0.089 | 748 |
| final3_hp_boosting | PJM | mape | 3.537 | 0.000 | 734 |
| final3_hp_boosting | SWPP | mape | -13.466 | 0.000 | 741 |
| final3_hp_boosting | TVA | mape | 13.792 | 0.000 | 729 |
| final3_hp_ensemble | BPAT | mape | 8.441 | 0.000 | 746 |
| final3_hp_ensemble | CISO | mape | 12.010 | 0.000 | 719 |
| final3_hp_ensemble | DUK | mape | 6.619 | 0.000 | 746 |
| final3_hp_ensemble | ERCO | mape | 5.774 | 0.000 | 742 |
| final3_hp_ensemble | FPL | mape | 19.301 | 0.000 | 665 |
| final3_hp_ensemble | ISNE | mape | 17.685 | 0.000 | 748 |
| final3_hp_ensemble | MISO | mape | -7.408 | 0.000 | 738 |
| final3_hp_ensemble | NYIS | mape | -5.300 | 0.000 | 748 |
| final3_hp_ensemble | PJM | mape | -0.256 | 0.798 | 734 |
| final3_hp_ensemble | SWPP | mape | -17.316 | 0.000 | 741 |
| final3_hp_ensemble | TVA | mape | 13.275 | 0.000 | 729 |
| final3_hp_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final3_hp_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final3_hp_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final3_hp_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final3_hp_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final3_hp_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final3_hp_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final3_hp_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final3_hp_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final3_hp_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final3_hp_recency | TVA | mape | 20.369 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final3_hp | 0.987 |
| final3_hp_additive | 0.965 |
| final3_hp_boosting | 0.987 |
| final3_hp_ensemble | 0.987 |
| final3_hp_recency | 0.987 |
