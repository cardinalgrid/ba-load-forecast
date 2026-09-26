# Phase J: the cut-off run and the run 6 h older averaged

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final5a` is the phase I recipe fed with the mean of the HRRR run available at the cut-off and the run six hours older, hour by hour where both cover the hour (in the Eastern zone in daylight time the cut-off run is the 06 UTC one and no older run is extracted, so the recipe falls back to the single run). Compare with `docs/phase_j_extremes.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5a | 2.40 | 2.07 | 0.04 | -1.29 | 1.22 | 0.57 | 0.30 | -46.49 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final5a_ensemble | 2.76 | 2.44 | -1.40 | -2.20 | 1.26 | 0.49 | 0.23 | -50.92 | 8056 | 11.00 |
| final5a_boosting | 2.84 | 2.52 | -1.01 | -2.03 | 1.38 | 0.45 | 0.25 | -51.31 | 8056 | 11.00 |
| final5a_additive | 3.01 | 2.67 | -1.62 | -2.48 | 1.30 | 0.44 | 0.21 | -49.25 | 8056 | 11.00 |
| final5a_recency | 3.67 | 3.31 | -1.71 | -2.73 | 1.61 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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
| final5a | BPAT | 2.45 | 2.15 | -0.37 | -1.44 | 1.68 | -17.69 | 0.39 | 0.25 | 746 | 6536.52 |
| final5a | CISO | 2.42 | 2.11 | 0.44 | -1.06 | 0.31 | -11.62 | 0.50 | 0.26 | 719 | 25193.76 |
| final5a | DUK | 3.19 | 2.87 | 0.11 | -1.71 | 1.32 | -14.98 | 0.40 | 0.32 | 746 | 12143.29 |
| final5a | ERCO | 2.62 | 2.18 | -0.05 | -1.44 | 1.01 | -14.64 | 0.49 | 0.27 | 742 | 46834.59 |
| final5a | FPL | 3.64 | 3.19 | -0.83 | -2.58 | 1.04 | -46.49 | 0.60 | 0.65 | 665 | 15346.05 |
| final5a | ISNE | 3.19 | 2.79 | 0.38 | -1.27 | 0.49 | -15.57 | 0.35 | 0.21 | 748 | 13403.92 |
| final5a | MISO | 2.02 | 1.74 | 0.11 | -1.01 | 1.61 | -7.32 | 0.63 | 0.06 | 738 | 73700.16 |
| final5a | NYIS | 2.26 | 1.98 | 0.01 | -1.28 | 0.56 | -12.87 | 0.61 | 0.72 | 748 | 17415.28 |
| final5a | PJM | 2.15 | 1.89 | 0.01 | -1.21 | 1.41 | -10.54 | 0.62 | 0.43 | 734 | 92076.14 |
| final5a | SWPP | 2.16 | 1.81 | -0.17 | -1.26 | 1.37 | -19.82 | 0.75 | 0.12 | 741 | 31382.01 |
| final5a | TVA | 2.86 | 2.48 | 0.45 | -1.38 | 1.30 | -13.23 | 0.31 | 0.33 | 729 | 18581.23 |
| final5a_additive | BPAT | 2.66 | 2.35 | -0.70 | -1.66 | 1.73 | -16.92 | 0.32 | 0.23 | 746 | 6536.52 |
| final5a_additive | CISO | 3.60 | 3.07 | -2.77 | -3.66 | 0.41 | -17.40 | 0.28 | 0.12 | 719 | 25193.76 |
| final5a_additive | DUK | 3.34 | 2.94 | -1.51 | -2.67 | 1.32 | -16.17 | 0.40 | 0.24 | 746 | 12143.29 |
| final5a_additive | ERCO | 3.73 | 3.39 | -2.72 | -3.43 | 1.02 | -16.99 | 0.29 | 0.13 | 742 | 46834.59 |
| final5a_additive | FPL | 6.18 | 5.66 | -6.19 | -6.72 | 1.04 | -49.25 | 0.26 | 0.25 | 665 | 15346.05 |
| final5a_additive | ISNE | 3.66 | 3.28 | -1.17 | -2.38 | 0.51 | -21.27 | 0.25 | 0.16 | 748 | 13403.92 |
| final5a_additive | MISO | 2.33 | 2.08 | -1.31 | -1.89 | 1.60 | -8.45 | 0.55 | 0.05 | 738 | 73700.16 |
| final5a_additive | NYIS | 2.54 | 2.23 | -1.03 | -2.04 | 0.54 | -15.21 | 0.56 | 0.59 | 748 | 17415.28 |
| final5a_additive | PJM | 2.65 | 2.33 | -0.61 | -1.71 | 1.65 | -11.72 | 0.47 | 0.38 | 734 | 92076.14 |
| final5a_additive | SWPP | 2.38 | 2.00 | -1.27 | -2.02 | 1.43 | -21.27 | 0.71 | 0.08 | 741 | 31382.01 |
| final5a_additive | TVA | 3.25 | 2.92 | -1.62 | -2.62 | 1.48 | -16.43 | 0.26 | 0.22 | 729 | 18581.23 |
| final5a_boosting | BPAT | 2.65 | 2.40 | -0.51 | -1.64 | 1.85 | -16.76 | 0.30 | 0.23 | 746 | 6536.52 |
| final5a_boosting | CISO | 2.88 | 2.57 | -1.94 | -2.51 | 0.43 | -15.70 | 0.37 | 0.16 | 719 | 25193.76 |
| final5a_boosting | DUK | 3.35 | 2.90 | -0.86 | -2.31 | 1.47 | -18.83 | 0.37 | 0.27 | 746 | 12143.29 |
| final5a_boosting | ERCO | 3.04 | 2.65 | -2.42 | -3.03 | 1.27 | -20.57 | 0.37 | 0.16 | 742 | 46834.59 |
| final5a_boosting | FPL | 6.12 | 5.77 | -6.53 | -6.89 | 1.26 | -51.31 | 0.21 | 0.26 | 665 | 15346.05 |
| final5a_boosting | ISNE | 3.44 | 3.11 | -0.27 | -1.57 | 0.54 | -17.19 | 0.30 | 0.18 | 748 | 13403.92 |
| final5a_boosting | MISO | 2.27 | 1.98 | -0.56 | -1.40 | 1.59 | -9.55 | 0.56 | 0.06 | 738 | 73700.16 |
| final5a_boosting | NYIS | 2.53 | 2.23 | -0.16 | -1.32 | 0.70 | -10.62 | 0.54 | 0.72 | 748 | 17415.28 |
| final5a_boosting | PJM | 2.65 | 2.38 | 0.17 | -1.28 | 1.69 | -11.82 | 0.45 | 0.44 | 734 | 92076.14 |
| final5a_boosting | SWPP | 2.46 | 2.07 | -1.21 | -2.08 | 1.51 | -29.01 | 0.70 | 0.07 | 741 | 31382.01 |
| final5a_boosting | TVA | 3.10 | 2.62 | -0.62 | -1.91 | 1.55 | -15.26 | 0.28 | 0.26 | 729 | 18581.23 |
| final5a_ensemble | BPAT | 2.48 | 2.22 | -0.80 | -1.66 | 1.72 | -17.65 | 0.37 | 0.23 | 746 | 6536.52 |
| final5a_ensemble | CISO | 3.22 | 2.76 | -2.73 | -3.23 | 0.34 | -15.87 | 0.35 | 0.11 | 719 | 25193.76 |
| final5a_ensemble | DUK | 3.20 | 2.78 | -0.98 | -2.32 | 1.37 | -14.72 | 0.43 | 0.25 | 746 | 12143.29 |
| final5a_ensemble | ERCO | 3.16 | 2.73 | -2.60 | -3.12 | 1.06 | -15.04 | 0.38 | 0.15 | 742 | 46834.59 |
| final5a_ensemble | FPL | 6.39 | 6.05 | -7.03 | -7.37 | 1.09 | -50.92 | 0.22 | 0.23 | 665 | 15346.05 |
| final5a_ensemble | ISNE | 3.39 | 3.09 | -1.19 | -2.12 | 0.50 | -17.57 | 0.27 | 0.15 | 748 | 13403.92 |
| final5a_ensemble | MISO | 2.17 | 1.90 | -1.01 | -1.59 | 1.62 | -8.27 | 0.60 | 0.05 | 738 | 73700.16 |
| final5a_ensemble | NYIS | 2.31 | 2.01 | -0.55 | -1.53 | 0.55 | -13.55 | 0.59 | 0.69 | 748 | 17415.28 |
| final5a_ensemble | PJM | 2.44 | 2.19 | -0.32 | -1.42 | 1.50 | -10.67 | 0.54 | 0.42 | 734 | 92076.14 |
| final5a_ensemble | SWPP | 2.14 | 1.74 | -0.94 | -1.69 | 1.34 | -20.13 | 0.76 | 0.09 | 741 | 31382.01 |
| final5a_ensemble | TVA | 2.97 | 2.62 | -1.09 | -2.16 | 1.38 | -15.87 | 0.29 | 0.23 | 729 | 18581.23 |
| final5a_recency | BPAT | 3.19 | 2.83 | -1.32 | -2.19 | 1.91 | -19.02 | 0.23 | 0.20 | 746 | 6536.52 |
| final5a_recency | CISO | 5.63 | 5.35 | -4.37 | -4.84 | 0.57 | -17.61 | 0.06 | 0.08 | 719 | 25193.76 |
| final5a_recency | DUK | 3.90 | 3.54 | -0.44 | -2.44 | 1.60 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final5a_recency | ERCO | 3.78 | 3.33 | -2.79 | -3.50 | 1.22 | -19.80 | 0.28 | 0.17 | 742 | 46834.59 |
| final5a_recency | FPL | 7.76 | 7.10 | -8.89 | -9.22 | 1.24 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final5a_recency | ISNE | 5.24 | 4.96 | -2.67 | -3.43 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final5a_recency | MISO | 2.94 | 2.64 | -1.26 | -2.00 | 2.22 | -14.07 | 0.43 | 0.05 | 738 | 73700.16 |
| final5a_recency | NYIS | 3.44 | 3.04 | -0.46 | -1.82 | 0.85 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final5a_recency | PJM | 3.09 | 2.79 | -0.56 | -1.84 | 1.96 | -20.00 | 0.32 | 0.38 | 734 | 92076.14 |
| final5a_recency | SWPP | 2.87 | 2.43 | -0.19 | -1.61 | 1.58 | -18.30 | 0.61 | 0.11 | 741 | 31382.01 |
| final5a_recency | TVA | 3.58 | 3.23 | -0.99 | -2.52 | 1.55 | -15.96 | 0.20 | 0.24 | 729 | 18581.23 |

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
| final5a | BPAT | uri | 2.27 | 0.15 | -0.80 | -4.83 | 6 |
| final5a | CISO | uri | 1.96 | -0.61 | -1.08 | -2.38 | 6 |
| final5a | DUK | uri | 3.42 | -1.53 | -1.70 | -3.74 | 6 |
| final5a | ERCO | uri | 6.13 | -8.47 | -8.47 | -8.91 | 2 |
| final5a | FPL | uri | 8.97 | -9.44 | -9.44 | -12.18 | 6 |
| final5a | ISNE | uri | 2.45 | 1.37 | -0.14 | -0.55 | 6 |
| final5a | MISO | uri | 4.00 | -3.44 | -3.68 | -7.16 | 5 |
| final5a | NYIS | uri | 2.12 | 1.96 | -0.13 | -0.78 | 6 |
| final5a | PJM | uri | 1.96 | 0.36 | -0.67 | -3.23 | 6 |
| final5a | SWPP | uri | 6.53 | -0.20 | -3.22 | -7.28 | 4 |
| final5a | TVA | uri | 3.91 | -1.36 | -2.72 | -6.86 | 6 |
| final5a_additive | BPAT | uri | 2.68 | -0.13 | -0.93 | -2.07 | 6 |
| final5a_additive | CISO | uri | 2.21 | 1.43 | -0.06 | -0.35 | 6 |
| final5a_additive | DUK | uri | 3.33 | -2.01 | -2.10 | -6.21 | 6 |
| final5a_additive | ERCO | uri | 4.06 | -5.54 | -5.54 | -7.59 | 2 |
| final5a_additive | FPL | uri | 10.66 | -15.84 | -15.84 | -18.61 | 6 |
| final5a_additive | ISNE | uri | 2.72 | 1.75 | -0.18 | -1.10 | 6 |
| final5a_additive | MISO | uri | 3.62 | -2.49 | -3.09 | -6.26 | 5 |
| final5a_additive | NYIS | uri | 2.67 | 2.92 | 0.00 | 0.00 | 6 |
| final5a_additive | PJM | uri | 3.37 | 3.16 | -0.42 | -2.52 | 6 |
| final5a_additive | SWPP | uri | 6.41 | 1.71 | -2.01 | -5.09 | 4 |
| final5a_additive | TVA | uri | 3.79 | 0.51 | -1.13 | -4.09 | 6 |
| final5a_boosting | BPAT | uri | 2.83 | 1.22 | -0.88 | -5.30 | 6 |
| final5a_boosting | CISO | uri | 2.17 | -0.83 | -1.33 | -3.84 | 6 |
| final5a_boosting | DUK | uri | 3.22 | -2.77 | -2.82 | -4.95 | 6 |
| final5a_boosting | ERCO | uri | 8.31 | -13.38 | -13.38 | -15.32 | 2 |
| final5a_boosting | FPL | uri | 9.34 | -12.31 | -12.31 | -14.81 | 6 |
| final5a_boosting | ISNE | uri | 3.77 | 1.76 | -0.38 | -1.87 | 6 |
| final5a_boosting | MISO | uri | 2.49 | -2.57 | -2.67 | -5.33 | 5 |
| final5a_boosting | NYIS | uri | 2.75 | 1.26 | -0.46 | -2.67 | 6 |
| final5a_boosting | PJM | uri | 2.27 | 0.05 | -0.61 | -2.57 | 6 |
| final5a_boosting | SWPP | uri | 5.20 | -3.41 | -4.25 | -9.81 | 4 |
| final5a_boosting | TVA | uri | 3.53 | -0.99 | -1.79 | -4.67 | 6 |
| final5a_ensemble | BPAT | uri | 2.42 | 0.46 | -0.68 | -3.73 | 6 |
| final5a_ensemble | CISO | uri | 1.82 | -0.11 | -0.66 | -1.67 | 6 |
| final5a_ensemble | DUK | uri | 3.37 | -2.73 | -2.73 | -5.96 | 6 |
| final5a_ensemble | ERCO | uri | 5.18 | -7.77 | -7.77 | -9.20 | 2 |
| final5a_ensemble | FPL | uri | 10.83 | -15.02 | -15.02 | -17.89 | 6 |
| final5a_ensemble | ISNE | uri | 2.39 | 0.64 | -0.41 | -1.71 | 6 |
| final5a_ensemble | MISO | uri | 3.72 | -3.49 | -3.49 | -6.65 | 5 |
| final5a_ensemble | NYIS | uri | 2.27 | 2.17 | -0.09 | -0.56 | 6 |
| final5a_ensemble | PJM | uri | 2.68 | 1.50 | -0.52 | -3.09 | 6 |
| final5a_ensemble | SWPP | uri | 6.10 | -1.36 | -3.58 | -7.61 | 4 |
| final5a_ensemble | TVA | uri | 3.65 | -0.35 | -1.49 | -4.25 | 6 |
| final5a_recency | BPAT | uri | 2.76 | 0.20 | -0.99 | -4.16 | 6 |
| final5a_recency | CISO | uri | 3.56 | -0.85 | -1.11 | -2.64 | 6 |
| final5a_recency | DUK | uri | 3.85 | -3.44 | -3.44 | -6.69 | 6 |
| final5a_recency | ERCO | uri | 4.80 | -3.62 | -4.22 | -8.44 | 2 |
| final5a_recency | FPL | uri | 12.96 | -17.44 | -17.44 | -20.87 | 6 |
| final5a_recency | ISNE | uri | 3.63 | -2.18 | -2.18 | -4.01 | 6 |
| final5a_recency | MISO | uri | 6.66 | -5.90 | -5.90 | -9.27 | 5 |
| final5a_recency | NYIS | uri | 2.57 | 2.22 | -0.05 | -0.32 | 6 |
| final5a_recency | PJM | uri | 2.79 | 1.44 | -0.73 | -4.33 | 6 |
| final5a_recency | SWPP | uri | 6.67 | -2.72 | -4.67 | -10.55 | 4 |
| final5a_recency | TVA | uri | 4.14 | -0.60 | -1.88 | -4.01 | 6 |
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
| final5a | BPAT | elliott | 3.07 | -2.18 | -2.52 | -5.93 | 5 |
| final5a | CISO | elliott | 3.68 | 3.05 | -0.52 | -2.61 | 5 |
| final5a | DUK | elliott | 3.32 | -0.45 | -1.28 | -3.58 | 4 |
| final5a | ERCO | elliott | 5.43 | -2.20 | -3.47 | -7.56 | 5 |
| final5a | FPL | elliott | 6.18 | -7.28 | -7.28 | -12.66 | 5 |
| final5a | ISNE | elliott | 3.69 | 3.10 | -0.59 | -2.47 | 5 |
| final5a | MISO | elliott | 3.46 | -2.03 | -2.78 | -6.69 | 5 |
| final5a | NYIS | elliott | 2.92 | 0.09 | -1.24 | -2.67 | 5 |
| final5a | PJM | elliott | 4.65 | -4.26 | -4.33 | -9.49 | 5 |
| final5a | SWPP | elliott | 4.08 | 0.28 | -1.84 | -4.77 | 5 |
| final5a | TVA | elliott | 5.14 | 4.92 | 0.00 | 0.00 | 3 |
| final5a_additive | BPAT | elliott | 3.60 | -1.34 | -2.01 | -4.21 | 5 |
| final5a_additive | CISO | elliott | 3.52 | 3.96 | -0.34 | -1.70 | 5 |
| final5a_additive | DUK | elliott | 4.73 | -3.38 | -3.39 | -4.98 | 4 |
| final5a_additive | ERCO | elliott | 7.59 | -5.57 | -6.09 | -14.09 | 5 |
| final5a_additive | FPL | elliott | 10.78 | -2.43 | -6.26 | -16.84 | 5 |
| final5a_additive | ISNE | elliott | 3.81 | 2.24 | -0.88 | -2.52 | 5 |
| final5a_additive | MISO | elliott | 3.30 | -2.94 | -3.26 | -6.38 | 5 |
| final5a_additive | NYIS | elliott | 3.16 | -0.82 | -2.02 | -4.55 | 5 |
| final5a_additive | PJM | elliott | 3.76 | -0.23 | -1.01 | -5.04 | 5 |
| final5a_additive | SWPP | elliott | 3.20 | -2.69 | -2.96 | -5.85 | 5 |
| final5a_additive | TVA | elliott | 5.91 | 2.77 | -0.46 | -1.37 | 3 |
| final5a_boosting | BPAT | elliott | 4.01 | -5.30 | -5.30 | -11.72 | 5 |
| final5a_boosting | CISO | elliott | 4.05 | 1.89 | -0.85 | -4.14 | 5 |
| final5a_boosting | DUK | elliott | 4.71 | -2.94 | -2.94 | -6.39 | 4 |
| final5a_boosting | ERCO | elliott | 6.85 | -9.79 | -9.79 | -20.57 | 5 |
| final5a_boosting | FPL | elliott | 8.66 | -14.30 | -14.30 | -19.50 | 5 |
| final5a_boosting | ISNE | elliott | 3.95 | 3.28 | -0.21 | -1.05 | 5 |
| final5a_boosting | MISO | elliott | 3.45 | -1.14 | -2.24 | -4.03 | 5 |
| final5a_boosting | NYIS | elliott | 3.31 | 0.78 | -0.70 | -2.83 | 5 |
| final5a_boosting | PJM | elliott | 4.72 | -2.44 | -3.01 | -6.44 | 5 |
| final5a_boosting | SWPP | elliott | 5.34 | -2.54 | -4.56 | -11.81 | 5 |
| final5a_boosting | TVA | elliott | 5.92 | 0.03 | -1.28 | -3.32 | 3 |
| final5a_ensemble | BPAT | elliott | 3.46 | -3.31 | -3.51 | -8.04 | 5 |
| final5a_ensemble | CISO | elliott | 3.52 | 3.41 | -0.48 | -2.42 | 5 |
| final5a_ensemble | DUK | elliott | 3.90 | -3.92 | -3.92 | -5.60 | 4 |
| final5a_ensemble | ERCO | elliott | 5.85 | -6.06 | -6.36 | -11.78 | 5 |
| final5a_ensemble | FPL | elliott | 7.16 | -8.70 | -8.70 | -12.66 | 5 |
| final5a_ensemble | ISNE | elliott | 3.60 | 3.06 | -0.52 | -1.88 | 5 |
| final5a_ensemble | MISO | elliott | 3.40 | -2.92 | -3.36 | -7.28 | 5 |
| final5a_ensemble | NYIS | elliott | 2.95 | -0.47 | -1.67 | -3.26 | 5 |
| final5a_ensemble | PJM | elliott | 4.35 | -3.60 | -3.82 | -9.30 | 5 |
| final5a_ensemble | SWPP | elliott | 3.76 | -3.08 | -3.79 | -8.28 | 5 |
| final5a_ensemble | TVA | elliott | 5.19 | 1.67 | -1.21 | -2.21 | 3 |
| final5a_recency | BPAT | elliott | 4.08 | -3.22 | -3.22 | -9.89 | 5 |
| final5a_recency | CISO | elliott | 4.16 | 5.30 | -0.10 | -0.50 | 5 |
| final5a_recency | DUK | elliott | 4.24 | -5.48 | -5.48 | -9.65 | 4 |
| final5a_recency | ERCO | elliott | 4.22 | -1.65 | -2.69 | -5.95 | 5 |
| final5a_recency | FPL | elliott | 9.96 | -8.11 | -9.03 | -15.46 | 5 |
| final5a_recency | ISNE | elliott | 4.54 | 3.90 | -0.81 | -3.05 | 5 |
| final5a_recency | MISO | elliott | 5.33 | -5.56 | -5.71 | -14.07 | 5 |
| final5a_recency | NYIS | elliott | 4.00 | -1.63 | -2.43 | -4.91 | 5 |
| final5a_recency | PJM | elliott | 6.47 | -8.59 | -8.73 | -20.00 | 5 |
| final5a_recency | SWPP | elliott | 3.47 | -4.16 | -4.43 | -9.31 | 5 |
| final5a_recency | TVA | elliott | 4.72 | 2.01 | -2.64 | -4.83 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final5a | eve | 3.34 | 0.97 | -1.40 | 0.44 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 10 | final5a_ensemble | eve | 3.40 | -0.51 | -2.11 | 0.47 | 265 |
| 8 | final5a_additive | eve | 3.63 | -0.23 | -2.10 | 0.45 | 265 |
| 9 | final5a_boosting | eve | 3.74 | -0.15 | -2.07 | 0.40 | 265 |
| 11 | final5a_recency | eve | 4.26 | -1.39 | -2.89 | 0.32 | 265 |
| 1 | final5a | special | 3.35 | -0.55 | -2.09 | 0.54 | 267 |
| 4 | final5a_ensemble | special | 3.52 | -2.01 | -3.08 | 0.52 | 267 |
| 2 | final5a_additive | special | 3.67 | -2.02 | -3.11 | 0.49 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final5a_boosting | special | 3.79 | -1.71 | -2.89 | 0.47 | 267 |
| 5 | final5a_recency | special | 4.54 | -2.44 | -3.82 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5a | all | 0.385 | 1.312 | 0.390 | 0.889 | 11.546 | 0.891 | 15.511 | 1.700 | 7811 |
| final5a | events | 0.459 | 1.907 | 0.649 | 0.768 | 12.017 | 0.804 | 22.161 | 2.501 | 107 |
| final5a | cold_mornings | 0.445 | 1.669 | 0.523 | 0.834 | 12.835 | 0.818 | 19.352 | 2.173 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final5a | 8.43 | -9.78 | -9.78 |
| 13224 | DUK | 2022-12-24 | final5a_additive | 7.22 | -13.06 | -13.06 |
| 13225 | DUK | 2022-12-24 | final5a_boosting | 9.82 | -17.08 | -17.08 |
| 13227 | DUK | 2022-12-24 | final5a_ensemble | 8.67 | -13.46 | -13.46 |
| 13226 | DUK | 2022-12-24 | final5a_recency | 9.22 | -10.17 | -10.17 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final5a | 31.54 | 24.93 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final5a_additive | 30.91 | 27.66 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final5a_boosting | 29.38 | 23.56 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final5a_ensemble | 32.65 | 28.05 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final5a_recency | 39.85 | 35.13 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final5a | 3.84 | 2.62 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final5a_additive | 13.48 | 11.98 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final5a_boosting | 4.14 | -7.75 | -7.75 |
| 13725 | ERCO | 2021-02-18 | final5a_ensemble | 4.66 | 1.72 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final5a_recency | 5.41 | 2.16 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final5a | 1.47 | 2.02 | 0.00 |
| 26664 | MISO | 2021-02-16 | final5a_additive | 2.32 | 1.88 | 0.00 |
| 26665 | MISO | 2021-02-16 | final5a_boosting | 1.86 | 1.33 | 0.00 |
| 26667 | MISO | 2021-02-16 | final5a_ensemble | 1.60 | 0.54 | 0.00 |
| 26666 | MISO | 2021-02-16 | final5a_recency | 3.65 | -2.28 | -2.28 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final5a | 3.26 | -2.61 | -2.61 |
| 39984 | SWPP | 2021-02-15 | final5a_additive | 2.16 | 1.30 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final5a_boosting | 6.81 | -8.01 | -8.01 |
| 39987 | SWPP | 2021-02-15 | final5a_ensemble | 3.26 | -3.84 | -3.84 |
| 39986 | SWPP | 2021-02-15 | final5a_recency | 4.75 | -5.16 | -5.16 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final5a | 3.62 | -0.51 | -0.51 |
| 39990 | SWPP | 2021-02-16 | final5a_additive | 7.37 | 3.64 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final5a_boosting | 3.30 | -6.32 | -6.32 |
| 39993 | SWPP | 2021-02-16 | final5a_ensemble | 3.63 | -0.89 | -0.89 |
| 39992 | SWPP | 2021-02-16 | final5a_recency | 2.43 | -0.14 | -0.14 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final5a | 9.17 | -10.95 | -10.95 |
| 48330 | TVA | 2022-12-23 | final5a_additive | 7.63 | -3.32 | -3.32 |
| 48331 | TVA | 2022-12-23 | final5a_boosting | 15.15 | -16.46 | -16.46 |
| 48333 | TVA | 2022-12-23 | final5a_ensemble | 8.86 | -10.03 | -10.03 |
| 48332 | TVA | 2022-12-23 | final5a_recency | 12.72 | -10.86 | -10.86 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final5a | 5.58 | -10.56 | -10.56 |
| 48336 | TVA | 2022-12-24 | final5a_additive | 3.76 | -9.05 | -9.05 |
| 48337 | TVA | 2022-12-24 | final5a_boosting | 7.14 | -15.20 | -15.20 |
| 48339 | TVA | 2022-12-24 | final5a_ensemble | 5.84 | -11.87 | -11.87 |
| 48338 | TVA | 2022-12-24 | final5a_recency | 7.13 | -11.58 | -11.58 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final5a | BPAT | mape | 7.313 | 0.000 | 746 |
| final5a | CISO | mape | 0.432 | 0.666 | 719 |
| final5a | DUK | mape | 5.645 | 0.000 | 746 |
| final5a | ERCO | mape | -0.010 | 0.992 | 742 |
| final5a | FPL | mape | -2.770 | 0.006 | 665 |
| final5a | ISNE | mape | 13.587 | 0.000 | 748 |
| final5a | MISO | mape | -10.368 | 0.000 | 738 |
| final5a | NYIS | mape | -6.503 | 0.000 | 748 |
| final5a | PJM | mape | -5.844 | 0.000 | 734 |
| final5a | SWPP | mape | -19.251 | 0.000 | 741 |
| final5a | TVA | mape | 11.784 | 0.000 | 729 |
| final5a_additive | BPAT | mape | 10.948 | 0.000 | 746 |
| final5a_additive | CISO | mape | 15.811 | 0.000 | 719 |
| final5a_additive | DUK | mape | 7.276 | 0.000 | 746 |
| final5a_additive | ERCO | mape | 13.855 | 0.000 | 742 |
| final5a_additive | FPL | mape | 18.099 | 0.000 | 665 |
| final5a_additive | ISNE | mape | 19.306 | 0.000 | 748 |
| final5a_additive | MISO | mape | -4.484 | 0.000 | 738 |
| final5a_additive | NYIS | mape | -1.939 | 0.052 | 748 |
| final5a_additive | PJM | mape | 3.314 | 0.001 | 734 |
| final5a_additive | SWPP | mape | -15.795 | 0.000 | 741 |
| final5a_additive | TVA | mape | 15.742 | 0.000 | 729 |
| final5a_boosting | BPAT | mape | 11.398 | 0.000 | 746 |
| final5a_boosting | CISO | mape | 7.805 | 0.000 | 719 |
| final5a_boosting | DUK | mape | 7.482 | 0.000 | 746 |
| final5a_boosting | ERCO | mape | 5.764 | 0.000 | 742 |
| final5a_boosting | FPL | mape | 19.631 | 0.000 | 665 |
| final5a_boosting | ISNE | mape | 17.250 | 0.000 | 748 |
| final5a_boosting | MISO | mape | -5.773 | 0.000 | 738 |
| final5a_boosting | NYIS | mape | -2.128 | 0.033 | 748 |
| final5a_boosting | PJM | mape | 3.329 | 0.001 | 734 |
| final5a_boosting | SWPP | mape | -14.269 | 0.000 | 741 |
| final5a_boosting | TVA | mape | 14.000 | 0.000 | 729 |
| final5a_ensemble | BPAT | mape | 8.073 | 0.000 | 746 |
| final5a_ensemble | CISO | mape | 11.932 | 0.000 | 719 |
| final5a_ensemble | DUK | mape | 5.430 | 0.000 | 746 |
| final5a_ensemble | ERCO | mape | 7.132 | 0.000 | 742 |
| final5a_ensemble | FPL | mape | 19.854 | 0.000 | 665 |
| final5a_ensemble | ISNE | mape | 17.485 | 0.000 | 748 |
| final5a_ensemble | MISO | mape | -7.074 | 0.000 | 738 |
| final5a_ensemble | NYIS | mape | -5.866 | 0.000 | 748 |
| final5a_ensemble | PJM | mape | -0.404 | 0.686 | 734 |
| final5a_ensemble | SWPP | mape | -19.375 | 0.000 | 741 |
| final5a_ensemble | TVA | mape | 12.650 | 0.000 | 729 |
| final5a_recency | BPAT | mape | 17.478 | 0.000 | 746 |
| final5a_recency | CISO | mape | 37.888 | 0.000 | 719 |
| final5a_recency | DUK | mape | 14.073 | 0.000 | 746 |
| final5a_recency | ERCO | mape | 13.576 | 0.000 | 742 |
| final5a_recency | FPL | mape | 23.819 | 0.000 | 665 |
| final5a_recency | ISNE | mape | 36.645 | 0.000 | 748 |
| final5a_recency | MISO | mape | 3.695 | 0.000 | 738 |
| final5a_recency | NYIS | mape | 10.153 | 0.000 | 748 |
| final5a_recency | PJM | mape | 10.589 | 0.000 | 734 |
| final5a_recency | SWPP | mape | -10.081 | 0.000 | 741 |
| final5a_recency | TVA | mape | 20.548 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final5a | 0.987 |
| final5a_additive | 0.965 |
| final5a_boosting | 0.987 |
| final5a_ensemble | 0.987 |
| final5a_recency | 0.987 |
