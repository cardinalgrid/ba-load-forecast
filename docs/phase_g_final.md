# Phase G: the recipe after phase G, in one run

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). The phase F recipe with what phase G added (see `docs/methods.md`), run once on the development period.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | 2.46 | 2.12 | 0.06 | -1.33 | 1.24 | 0.55 | 0.30 | -46.79 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final3_ensemble | 2.82 | 2.47 | -1.30 | -2.19 | 1.27 | 0.48 | 0.23 | -51.51 | 8056 | 11.00 |
| final3_boosting | 2.93 | 2.59 | -1.02 | -2.09 | 1.45 | 0.43 | 0.24 | -52.42 | 8056 | 11.00 |
| final3_additive | 3.00 | 2.64 | -1.31 | -2.32 | 1.32 | 0.44 | 0.23 | -49.89 | 8056 | 11.00 |
| final3_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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
| final3 | BPAT | 2.47 | 2.14 | -0.42 | -1.46 | 1.71 | -18.15 | 0.38 | 0.25 | 746 | 6536.52 |
| final3 | CISO | 2.47 | 2.16 | 0.40 | -1.09 | 0.33 | -13.33 | 0.49 | 0.26 | 719 | 25193.76 |
| final3 | DUK | 3.29 | 2.98 | -0.05 | -1.88 | 1.36 | -16.27 | 0.39 | 0.31 | 746 | 12143.29 |
| final3 | ERCO | 2.71 | 2.25 | 0.11 | -1.49 | 1.06 | -13.98 | 0.46 | 0.28 | 742 | 46834.59 |
| final3 | FPL | 3.71 | 3.26 | -0.72 | -2.61 | 1.05 | -46.79 | 0.57 | 0.64 | 665 | 15346.05 |
| final3 | ISNE | 3.40 | 2.97 | 0.36 | -1.41 | 0.51 | -14.43 | 0.30 | 0.21 | 748 | 13403.92 |
| final3 | MISO | 2.05 | 1.79 | 0.14 | -1.00 | 1.66 | -8.20 | 0.62 | 0.07 | 738 | 73700.16 |
| final3 | NYIS | 2.36 | 2.01 | 0.04 | -1.32 | 0.58 | -13.97 | 0.60 | 0.72 | 748 | 17415.28 |
| final3 | PJM | 2.20 | 1.89 | 0.05 | -1.23 | 1.37 | -10.79 | 0.60 | 0.43 | 734 | 92076.14 |
| final3 | SWPP | 2.23 | 1.88 | -0.19 | -1.33 | 1.45 | -20.49 | 0.74 | 0.11 | 741 | 31382.01 |
| final3 | TVA | 2.94 | 2.54 | 0.38 | -1.52 | 1.39 | -11.06 | 0.31 | 0.31 | 729 | 18581.23 |
| final3_additive | BPAT | 2.69 | 2.37 | -0.69 | -1.66 | 1.77 | -16.93 | 0.30 | 0.22 | 746 | 6536.52 |
| final3_additive | CISO | 3.62 | 3.05 | -2.90 | -3.78 | 0.43 | -17.65 | 0.28 | 0.12 | 719 | 25193.76 |
| final3_additive | DUK | 3.52 | 3.15 | -0.58 | -2.30 | 1.39 | -14.98 | 0.35 | 0.26 | 746 | 12143.29 |
| final3_additive | ERCO | 3.44 | 3.00 | -2.09 | -2.90 | 1.04 | -15.86 | 0.32 | 0.16 | 742 | 46834.59 |
| final3_additive | FPL | 6.20 | 5.85 | -6.52 | -7.04 | 1.14 | -49.89 | 0.27 | 0.26 | 665 | 15346.05 |
| final3_additive | ISNE | 3.71 | 3.31 | -1.05 | -2.38 | 0.53 | -19.32 | 0.24 | 0.16 | 748 | 13403.92 |
| final3_additive | MISO | 2.34 | 2.09 | -1.21 | -1.84 | 1.60 | -8.30 | 0.55 | 0.05 | 738 | 73700.16 |
| final3_additive | NYIS | 2.60 | 2.28 | -0.83 | -1.97 | 0.56 | -15.30 | 0.55 | 0.60 | 748 | 17415.28 |
| final3_additive | PJM | 2.65 | 2.30 | -0.44 | -1.63 | 1.64 | -12.14 | 0.47 | 0.39 | 734 | 92076.14 |
| final3_additive | SWPP | 2.52 | 2.09 | -0.19 | -1.55 | 1.50 | -20.78 | 0.70 | 0.10 | 741 | 31382.01 |
| final3_additive | TVA | 3.25 | 2.89 | -0.89 | -2.22 | 1.45 | -14.41 | 0.27 | 0.25 | 729 | 18581.23 |
| final3_boosting | BPAT | 2.68 | 2.40 | -0.45 | -1.59 | 2.00 | -18.49 | 0.29 | 0.24 | 746 | 6536.52 |
| final3_boosting | CISO | 2.94 | 2.60 | -2.00 | -2.61 | 0.42 | -17.41 | 0.36 | 0.16 | 719 | 25193.76 |
| final3_boosting | DUK | 3.48 | 3.01 | -0.52 | -2.25 | 1.50 | -17.80 | 0.34 | 0.27 | 746 | 12143.29 |
| final3_boosting | ERCO | 3.05 | 2.59 | -2.33 | -2.99 | 1.30 | -20.78 | 0.36 | 0.17 | 742 | 46834.59 |
| final3_boosting | FPL | 6.27 | 5.94 | -6.68 | -7.03 | 1.32 | -52.42 | 0.20 | 0.26 | 665 | 15346.05 |
| final3_boosting | ISNE | 3.69 | 3.30 | -0.71 | -2.02 | 0.55 | -18.20 | 0.24 | 0.18 | 748 | 13403.92 |
| final3_boosting | MISO | 2.33 | 2.02 | -0.55 | -1.44 | 1.70 | -10.28 | 0.55 | 0.05 | 738 | 73700.16 |
| final3_boosting | NYIS | 2.68 | 2.35 | -0.38 | -1.51 | 0.79 | -12.12 | 0.51 | 0.69 | 748 | 17415.28 |
| final3_boosting | PJM | 2.74 | 2.49 | 0.07 | -1.39 | 1.78 | -12.01 | 0.42 | 0.42 | 734 | 92076.14 |
| final3_boosting | SWPP | 2.61 | 2.15 | -0.93 | -1.97 | 1.55 | -28.20 | 0.68 | 0.08 | 741 | 31382.01 |
| final3_boosting | TVA | 3.20 | 2.80 | -0.39 | -1.92 | 1.52 | -12.82 | 0.27 | 0.28 | 729 | 18581.23 |
| final3_ensemble | BPAT | 2.51 | 2.24 | -0.79 | -1.65 | 1.71 | -18.11 | 0.36 | 0.24 | 746 | 6536.52 |
| final3_ensemble | CISO | 3.27 | 2.82 | -2.83 | -3.34 | 0.37 | -17.33 | 0.33 | 0.12 | 719 | 25193.76 |
| final3_ensemble | DUK | 3.37 | 2.94 | -0.54 | -2.22 | 1.43 | -14.33 | 0.38 | 0.27 | 746 | 12143.29 |
| final3_ensemble | ERCO | 3.10 | 2.62 | -2.37 | -2.97 | 1.04 | -15.12 | 0.37 | 0.17 | 742 | 46834.59 |
| final3_ensemble | FPL | 6.44 | 6.15 | -7.20 | -7.52 | 1.11 | -51.51 | 0.23 | 0.24 | 665 | 15346.05 |
| final3_ensemble | ISNE | 3.58 | 3.28 | -1.35 | -2.34 | 0.50 | -17.56 | 0.25 | 0.15 | 748 | 13403.92 |
| final3_ensemble | MISO | 2.19 | 1.90 | -0.97 | -1.60 | 1.67 | -7.99 | 0.59 | 0.05 | 738 | 73700.16 |
| final3_ensemble | NYIS | 2.41 | 2.07 | -0.56 | -1.60 | 0.57 | -14.88 | 0.57 | 0.67 | 748 | 17415.28 |
| final3_ensemble | PJM | 2.49 | 2.20 | -0.31 | -1.44 | 1.47 | -11.12 | 0.52 | 0.42 | 734 | 92076.14 |
| final3_ensemble | SWPP | 2.33 | 1.91 | -0.43 | -1.54 | 1.42 | -19.76 | 0.71 | 0.10 | 741 | 31382.01 |
| final3_ensemble | TVA | 3.06 | 2.69 | -0.75 | -2.08 | 1.39 | -13.72 | 0.29 | 0.26 | 729 | 18581.23 |
| final3_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final3_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final3_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final3_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final3_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final3_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final3_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final3_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final3_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final3_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final3_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |

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
| final3 | BPAT | uri | 2.48 | -0.27 | -0.91 | -5.01 | 6 |
| final3 | CISO | uri | 2.16 | -0.99 | -1.43 | -2.91 | 6 |
| final3 | DUK | uri | 3.55 | -1.49 | -2.00 | -4.38 | 6 |
| final3 | ERCO | uri | 6.35 | -8.23 | -8.23 | -8.85 | 2 |
| final3 | FPL | uri | 8.51 | -7.84 | -7.84 | -12.09 | 6 |
| final3 | ISNE | uri | 2.50 | 1.74 | -0.18 | -1.08 | 6 |
| final3 | MISO | uri | 4.03 | -3.28 | -3.55 | -7.00 | 5 |
| final3 | NYIS | uri | 2.04 | 1.96 | -0.14 | -0.85 | 6 |
| final3 | PJM | uri | 1.99 | 0.32 | -0.57 | -2.32 | 6 |
| final3 | SWPP | uri | 6.84 | -0.14 | -3.31 | -7.70 | 4 |
| final3 | TVA | uri | 3.39 | -1.46 | -2.59 | -5.67 | 6 |
| final3_additive | BPAT | uri | 2.81 | -0.35 | -1.21 | -2.29 | 6 |
| final3_additive | CISO | uri | 2.21 | 1.49 | -0.05 | -0.30 | 6 |
| final3_additive | DUK | uri | 3.49 | -1.84 | -1.91 | -6.46 | 6 |
| final3_additive | ERCO | uri | 4.34 | -4.90 | -4.90 | -7.68 | 2 |
| final3_additive | FPL | uri | 10.53 | -15.09 | -15.09 | -18.04 | 6 |
| final3_additive | ISNE | uri | 2.98 | 1.99 | -0.20 | -1.20 | 6 |
| final3_additive | MISO | uri | 3.67 | -2.41 | -3.04 | -6.36 | 5 |
| final3_additive | NYIS | uri | 2.66 | 3.01 | 0.00 | 0.00 | 6 |
| final3_additive | PJM | uri | 3.14 | 3.01 | -0.41 | -2.47 | 6 |
| final3_additive | SWPP | uri | 6.47 | 1.82 | -2.00 | -5.04 | 4 |
| final3_additive | TVA | uri | 3.46 | 0.64 | -1.03 | -2.61 | 6 |
| final3_boosting | BPAT | uri | 3.45 | 1.33 | -0.90 | -5.38 | 6 |
| final3_boosting | CISO | uri | 2.29 | -1.67 | -1.95 | -4.65 | 6 |
| final3_boosting | DUK | uri | 3.73 | -2.45 | -2.62 | -5.37 | 6 |
| final3_boosting | ERCO | uri | 8.42 | -13.34 | -13.34 | -14.88 | 2 |
| final3_boosting | FPL | uri | 8.95 | -10.96 | -10.96 | -13.77 | 6 |
| final3_boosting | ISNE | uri | 3.75 | 2.24 | -0.56 | -2.76 | 6 |
| final3_boosting | MISO | uri | 3.11 | -2.80 | -2.94 | -5.79 | 5 |
| final3_boosting | NYIS | uri | 2.63 | 0.87 | -0.61 | -3.20 | 6 |
| final3_boosting | PJM | uri | 2.04 | -0.72 | -0.98 | -1.97 | 6 |
| final3_boosting | SWPP | uri | 5.87 | -3.34 | -4.47 | -10.32 | 4 |
| final3_boosting | TVA | uri | 2.69 | -1.33 | -1.86 | -4.11 | 6 |
| final3_ensemble | BPAT | uri | 2.67 | 0.26 | -0.74 | -4.00 | 6 |
| final3_ensemble | CISO | uri | 1.91 | -0.41 | -0.88 | -2.03 | 6 |
| final3_ensemble | DUK | uri | 3.58 | -2.54 | -2.54 | -6.28 | 6 |
| final3_ensemble | ERCO | uri | 5.40 | -7.58 | -7.58 | -9.40 | 2 |
| final3_ensemble | FPL | uri | 10.53 | -13.93 | -13.93 | -16.55 | 6 |
| final3_ensemble | ISNE | uri | 2.55 | 0.93 | -0.44 | -2.53 | 6 |
| final3_ensemble | MISO | uri | 3.91 | -3.52 | -3.53 | -6.97 | 5 |
| final3_ensemble | NYIS | uri | 2.17 | 2.12 | -0.10 | -0.62 | 6 |
| final3_ensemble | PJM | uri | 2.38 | 1.14 | -0.50 | -2.80 | 6 |
| final3_ensemble | SWPP | uri | 6.37 | -1.33 | -3.67 | -7.83 | 4 |
| final3_ensemble | TVA | uri | 3.05 | -0.45 | -1.48 | -3.19 | 6 |
| final3_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final3_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final3_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final3_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final3_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final3_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final3_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final3_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final3_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final3_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final3_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
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
| final3 | BPAT | elliott | 3.13 | -1.97 | -2.42 | -5.90 | 5 |
| final3 | CISO | elliott | 3.54 | 2.85 | -0.48 | -2.39 | 5 |
| final3 | DUK | elliott | 3.14 | -1.22 | -1.38 | -3.96 | 4 |
| final3 | ERCO | elliott | 5.59 | -2.90 | -4.09 | -8.21 | 5 |
| final3 | FPL | elliott | 6.13 | -6.90 | -6.90 | -12.17 | 5 |
| final3 | ISNE | elliott | 3.73 | 2.82 | -0.85 | -3.05 | 5 |
| final3 | MISO | elliott | 3.56 | -2.51 | -3.23 | -7.75 | 5 |
| final3 | NYIS | elliott | 2.85 | -0.86 | -1.65 | -3.74 | 5 |
| final3 | PJM | elliott | 4.63 | -4.35 | -4.38 | -9.50 | 5 |
| final3 | SWPP | elliott | 4.17 | 0.34 | -1.93 | -6.07 | 5 |
| final3 | TVA | elliott | 5.17 | 4.20 | 0.00 | 0.00 | 3 |
| final3_additive | BPAT | elliott | 3.64 | -1.16 | -2.00 | -4.21 | 5 |
| final3_additive | CISO | elliott | 3.47 | 3.77 | -0.32 | -1.61 | 5 |
| final3_additive | DUK | elliott | 4.58 | -3.41 | -3.41 | -5.07 | 4 |
| final3_additive | ERCO | elliott | 7.48 | -5.62 | -6.17 | -14.01 | 5 |
| final3_additive | FPL | elliott | 10.32 | -0.39 | -5.39 | -13.75 | 5 |
| final3_additive | ISNE | elliott | 3.84 | 2.32 | -0.91 | -2.27 | 5 |
| final3_additive | MISO | elliott | 3.36 | -3.29 | -3.60 | -7.71 | 5 |
| final3_additive | NYIS | elliott | 3.13 | -0.97 | -2.04 | -4.49 | 5 |
| final3_additive | PJM | elliott | 3.53 | -0.16 | -0.93 | -4.57 | 5 |
| final3_additive | SWPP | elliott | 3.00 | -2.57 | -2.84 | -5.40 | 5 |
| final3_additive | TVA | elliott | 5.91 | 3.10 | -0.19 | -0.57 | 3 |
| final3_boosting | BPAT | elliott | 4.46 | -4.51 | -4.74 | -11.66 | 5 |
| final3_boosting | CISO | elliott | 3.96 | 1.50 | -1.06 | -4.75 | 5 |
| final3_boosting | DUK | elliott | 4.71 | -2.60 | -2.60 | -5.62 | 4 |
| final3_boosting | ERCO | elliott | 6.96 | -9.54 | -9.70 | -20.78 | 5 |
| final3_boosting | FPL | elliott | 8.83 | -15.37 | -15.37 | -19.13 | 5 |
| final3_boosting | ISNE | elliott | 3.89 | 3.39 | -0.45 | -2.23 | 5 |
| final3_boosting | MISO | elliott | 3.66 | -1.07 | -2.19 | -3.48 | 5 |
| final3_boosting | NYIS | elliott | 3.11 | 0.19 | -0.87 | -2.78 | 5 |
| final3_boosting | PJM | elliott | 5.27 | -2.75 | -3.77 | -7.24 | 5 |
| final3_boosting | SWPP | elliott | 5.50 | -1.75 | -3.68 | -11.27 | 5 |
| final3_boosting | TVA | elliott | 6.27 | 0.61 | -0.98 | -2.94 | 3 |
| final3_ensemble | BPAT | elliott | 3.65 | -2.92 | -3.28 | -8.17 | 5 |
| final3_ensemble | CISO | elliott | 3.48 | 3.19 | -0.50 | -2.52 | 5 |
| final3_ensemble | DUK | elliott | 3.76 | -3.79 | -3.79 | -5.05 | 4 |
| final3_ensemble | ERCO | elliott | 5.89 | -5.94 | -6.33 | -11.68 | 5 |
| final3_ensemble | FPL | elliott | 7.08 | -8.34 | -8.34 | -12.17 | 5 |
| final3_ensemble | ISNE | elliott | 3.63 | 3.12 | -0.66 | -2.52 | 5 |
| final3_ensemble | MISO | elliott | 3.44 | -3.02 | -3.47 | -7.67 | 5 |
| final3_ensemble | NYIS | elliott | 2.87 | -0.78 | -1.72 | -3.50 | 5 |
| final3_ensemble | PJM | elliott | 4.37 | -3.65 | -3.92 | -9.26 | 5 |
| final3_ensemble | SWPP | elliott | 3.62 | -2.63 | -3.28 | -8.54 | 5 |
| final3_ensemble | TVA | elliott | 5.40 | 2.25 | -0.98 | -1.53 | 3 |
| final3_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final3_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final3_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final3_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final3_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final3_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final3_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final3_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final3_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final3_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final3_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final3 | eve | 3.35 | 0.82 | -1.47 | 0.46 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 10 | final3_ensemble | eve | 3.45 | -0.45 | -2.13 | 0.46 | 265 |
| 8 | final3_additive | eve | 3.67 | 0.09 | -2.01 | 0.43 | 265 |
| 9 | final3_boosting | eve | 3.79 | -0.22 | -2.14 | 0.39 | 265 |
| 11 | final3_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final3 | special | 3.37 | -0.67 | -2.16 | 0.51 | 267 |
| 4 | final3_ensemble | special | 3.59 | -1.96 | -3.10 | 0.51 | 267 |
| 2 | final3_additive | special | 3.70 | -1.79 | -3.04 | 0.48 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final3_boosting | special | 3.89 | -1.72 | -2.94 | 0.47 | 267 |
| 5 | final3_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | all | 0.390 | 1.354 | 0.405 | 0.888 | 11.848 | 0.893 | 7815 |
| final3 | events | 0.455 | 1.906 | 0.685 | 0.771 | 11.996 | 0.804 | 107 |
| final3 | cold_mornings | 0.449 | 1.655 | 0.530 | 0.836 | 12.926 | 0.821 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final3 | 8.27 | -9.33 | -9.33 |
| 13224 | DUK | 2022-12-24 | final3_additive | 6.92 | -12.48 | -12.48 |
| 13225 | DUK | 2022-12-24 | final3_boosting | 9.37 | -16.02 | -16.02 |
| 13227 | DUK | 2022-12-24 | final3_ensemble | 8.39 | -12.85 | -12.85 |
| 13226 | DUK | 2022-12-24 | final3_recency | 9.27 | -9.99 | -9.99 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final3 | 31.94 | 26.81 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final3_additive | 30.43 | 28.75 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final3_boosting | 29.67 | 25.77 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final3_ensemble | 32.98 | 29.72 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final3_recency | 41.20 | 36.68 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final3 | 4.11 | 2.56 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final3_additive | 13.30 | 11.77 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final3_boosting | 3.47 | -7.67 | -7.67 |
| 13725 | ERCO | 2021-02-18 | final3_ensemble | 4.87 | 1.76 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final3_recency | 5.36 | 2.19 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final3 | 1.86 | 1.67 | 0.00 |
| 26664 | MISO | 2021-02-16 | final3_additive | 2.33 | 2.19 | 0.00 |
| 26665 | MISO | 2021-02-16 | final3_boosting | 2.22 | 0.36 | 0.00 |
| 26667 | MISO | 2021-02-16 | final3_ensemble | 1.80 | 0.38 | 0.00 |
| 26666 | MISO | 2021-02-16 | final3_recency | 3.61 | -2.07 | -2.07 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final3 | 2.99 | -2.73 | -2.73 |
| 39984 | SWPP | 2021-02-15 | final3_additive | 2.38 | 1.40 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final3_boosting | 6.26 | -8.32 | -8.32 |
| 39987 | SWPP | 2021-02-15 | final3_ensemble | 3.04 | -3.93 | -3.93 |
| 39986 | SWPP | 2021-02-15 | final3_recency | 4.81 | -5.28 | -5.28 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final3 | 3.93 | 0.11 | 0.00 |
| 39990 | SWPP | 2021-02-16 | final3_additive | 7.58 | 3.67 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final3_boosting | 3.17 | -5.46 | -5.46 |
| 39993 | SWPP | 2021-02-16 | final3_ensemble | 3.89 | -0.52 | -0.52 |
| 39992 | SWPP | 2021-02-16 | final3_recency | 2.57 | -0.10 | -0.10 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final3 | 9.30 | -11.09 | -11.09 |
| 48330 | TVA | 2022-12-23 | final3_additive | 7.72 | -3.74 | -3.74 |
| 48331 | TVA | 2022-12-23 | final3_boosting | 15.15 | -15.60 | -15.60 |
| 48333 | TVA | 2022-12-23 | final3_ensemble | 8.92 | -9.66 | -9.66 |
| 48332 | TVA | 2022-12-23 | final3_recency | 11.83 | -10.22 | -10.22 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final3 | 5.77 | -11.66 | -11.66 |
| 48336 | TVA | 2022-12-24 | final3_additive | 3.92 | -9.05 | -9.05 |
| 48337 | TVA | 2022-12-24 | final3_boosting | 6.59 | -15.23 | -15.23 |
| 48339 | TVA | 2022-12-24 | final3_ensemble | 5.71 | -11.79 | -11.79 |
| 48338 | TVA | 2022-12-24 | final3_recency | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3 | BPAT | mape | 7.673 | 0.000 | 746 |
| final3 | CISO | mape | 1.266 | 0.206 | 719 |
| final3 | DUK | mape | 6.883 | 0.000 | 746 |
| final3 | ERCO | mape | 1.350 | 0.177 | 742 |
| final3 | FPL | mape | -2.065 | 0.039 | 665 |
| final3 | ISNE | mape | 15.205 | 0.000 | 748 |
| final3 | MISO | mape | -9.814 | 0.000 | 738 |
| final3 | NYIS | mape | -4.672 | 0.000 | 748 |
| final3 | PJM | mape | -4.848 | 0.000 | 734 |
| final3 | SWPP | mape | -17.968 | 0.000 | 741 |
| final3 | TVA | mape | 12.807 | 0.000 | 729 |
| final3_additive | BPAT | mape | 11.482 | 0.000 | 746 |
| final3_additive | CISO | mape | 15.935 | 0.000 | 719 |
| final3_additive | DUK | mape | 9.584 | 0.000 | 746 |
| final3_additive | ERCO | mape | 10.610 | 0.000 | 742 |
| final3_additive | FPL | mape | 17.818 | 0.000 | 665 |
| final3_additive | ISNE | mape | 19.452 | 0.000 | 748 |
| final3_additive | MISO | mape | -4.388 | 0.000 | 738 |
| final3_additive | NYIS | mape | -1.084 | 0.278 | 748 |
| final3_additive | PJM | mape | 3.267 | 0.001 | 734 |
| final3_additive | SWPP | mape | -14.178 | 0.000 | 741 |
| final3_additive | TVA | mape | 16.280 | 0.000 | 729 |
| final3_boosting | BPAT | mape | 12.144 | 0.000 | 746 |
| final3_boosting | CISO | mape | 8.674 | 0.000 | 719 |
| final3_boosting | DUK | mape | 9.118 | 0.000 | 746 |
| final3_boosting | ERCO | mape | 5.927 | 0.000 | 742 |
| final3_boosting | FPL | mape | 20.726 | 0.000 | 665 |
| final3_boosting | ISNE | mape | 19.485 | 0.000 | 748 |
| final3_boosting | MISO | mape | -4.766 | 0.000 | 738 |
| final3_boosting | NYIS | mape | 0.149 | 0.882 | 748 |
| final3_boosting | PJM | mape | 4.850 | 0.000 | 734 |
| final3_boosting | SWPP | mape | -12.160 | 0.000 | 741 |
| final3_boosting | TVA | mape | 15.466 | 0.000 | 729 |
| final3_ensemble | BPAT | mape | 8.605 | 0.000 | 746 |
| final3_ensemble | CISO | mape | 12.505 | 0.000 | 719 |
| final3_ensemble | DUK | mape | 7.687 | 0.000 | 746 |
| final3_ensemble | ERCO | mape | 6.422 | 0.000 | 742 |
| final3_ensemble | FPL | mape | 19.894 | 0.000 | 665 |
| final3_ensemble | ISNE | mape | 18.835 | 0.000 | 748 |
| final3_ensemble | MISO | mape | -6.675 | 0.000 | 738 |
| final3_ensemble | NYIS | mape | -4.031 | 0.000 | 748 |
| final3_ensemble | PJM | mape | 0.621 | 0.534 | 734 |
| final3_ensemble | SWPP | mape | -16.672 | 0.000 | 741 |
| final3_ensemble | TVA | mape | 14.026 | 0.000 | 729 |
| final3_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final3_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final3_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final3_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final3_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final3_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final3_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final3_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final3_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final3_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final3_recency | TVA | mape | 20.369 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final3 | 0.987 |
| final3_additive | 0.965 |
| final3_boosting | 0.987 |
| final3_ensemble | 0.987 |
| final3_recency | 0.987 |
