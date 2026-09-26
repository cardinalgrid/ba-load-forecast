# Phase I: the candidate recipe on the development years

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final5` is `final4` with the wind block in the boosting (apparent temperature without wind chill in the additive model) and the point read at the 70th percentile around the peak on the coldest decile of days, with 23 quantiles. Compare with `docs/phase_i_events.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | 2.39 | 2.07 | 0.05 | -1.28 | 1.24 | 0.57 | 0.30 | -46.49 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final5_ensemble | 2.74 | 2.42 | -1.39 | -2.19 | 1.28 | 0.50 | 0.23 | -50.92 | 8056 | 11.00 |
| final5_boosting | 2.83 | 2.50 | -1.00 | -2.01 | 1.40 | 0.46 | 0.25 | -51.31 | 8056 | 11.00 |
| final5_additive | 2.99 | 2.65 | -1.60 | -2.46 | 1.31 | 0.44 | 0.21 | -49.25 | 8056 | 11.00 |
| final5_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

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

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final5 | eve | 3.31 | 0.89 | -1.42 | 0.44 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 10 | final5_ensemble | eve | 3.39 | -0.55 | -2.14 | 0.48 | 265 |
| 8 | final5_additive | eve | 3.62 | -0.28 | -2.15 | 0.45 | 265 |
| 9 | final5_boosting | eve | 3.73 | -0.16 | -2.05 | 0.40 | 265 |
| 11 | final5_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final5 | special | 3.34 | -0.57 | -2.10 | 0.54 | 267 |
| 4 | final5_ensemble | special | 3.52 | -2.01 | -3.07 | 0.52 | 267 |
| 2 | final5_additive | special | 3.67 | -2.02 | -3.12 | 0.49 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final5_boosting | special | 3.79 | -1.67 | -2.84 | 0.46 | 267 |
| 5 | final5_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | all | 0.385 | 1.310 | 0.391 | 0.889 | 11.538 | 0.892 | 15.511 | 1.699 | 7815 |
| final5 | events | 0.458 | 1.889 | 0.645 | 0.764 | 11.876 | 0.804 | 22.059 | 2.481 | 107 |
| final5 | cold_mornings | 0.453 | 1.659 | 0.522 | 0.829 | 12.804 | 0.818 | 19.503 | 2.167 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13229 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13228 | DUK | 2022-12-24 | final5 | 8.38 | -9.34 | -9.34 |
| 13224 | DUK | 2022-12-24 | final5_additive | 7.22 | -13.03 | -13.03 |
| 13225 | DUK | 2022-12-24 | final5_boosting | 9.91 | -17.04 | -17.04 |
| 13227 | DUK | 2022-12-24 | final5_ensemble | 8.72 | -13.40 | -13.40 |
| 13226 | DUK | 2022-12-24 | final5_recency | 9.27 | -9.99 | -9.99 |
| 13721 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13720 | ERCO | 2021-02-17 | final5 | 32.80 | 26.25 | 0.00 |
| 13716 | ERCO | 2021-02-17 | final5_additive | 32.00 | 28.88 | 0.00 |
| 13717 | ERCO | 2021-02-17 | final5_boosting | 29.91 | 24.19 | 0.00 |
| 13719 | ERCO | 2021-02-17 | final5_ensemble | 33.60 | 29.13 | 0.00 |
| 13718 | ERCO | 2021-02-17 | final5_recency | 41.20 | 36.68 | 0.00 |
| 13727 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13726 | ERCO | 2021-02-18 | final5 | 3.98 | 2.79 | 0.00 |
| 13722 | ERCO | 2021-02-18 | final5_additive | 13.29 | 11.84 | 0.00 |
| 13723 | ERCO | 2021-02-18 | final5_boosting | 4.23 | -7.71 | -7.71 |
| 13725 | ERCO | 2021-02-18 | final5_ensemble | 4.48 | 1.69 | 0.00 |
| 13724 | ERCO | 2021-02-18 | final5_recency | 5.36 | 2.19 | 0.00 |
| 26669 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26668 | MISO | 2021-02-16 | final5 | 1.60 | 1.89 | 0.00 |
| 26664 | MISO | 2021-02-16 | final5_additive | 2.38 | 2.18 | 0.00 |
| 26665 | MISO | 2021-02-16 | final5_boosting | 1.96 | 1.33 | 0.00 |
| 26667 | MISO | 2021-02-16 | final5_ensemble | 1.66 | 0.73 | 0.00 |
| 26666 | MISO | 2021-02-16 | final5_recency | 3.61 | -2.07 | -2.07 |
| 39989 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 39988 | SWPP | 2021-02-15 | final5 | 3.23 | -2.81 | -2.81 |
| 39984 | SWPP | 2021-02-15 | final5_additive | 2.24 | 1.30 | 0.00 |
| 39985 | SWPP | 2021-02-15 | final5_boosting | 6.97 | -8.54 | -8.54 |
| 39987 | SWPP | 2021-02-15 | final5_ensemble | 3.32 | -4.06 | -4.06 |
| 39986 | SWPP | 2021-02-15 | final5_recency | 4.81 | -5.28 | -5.28 |
| 39995 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 39994 | SWPP | 2021-02-16 | final5 | 3.79 | -0.23 | -0.23 |
| 39990 | SWPP | 2021-02-16 | final5_additive | 7.74 | 3.67 | 0.00 |
| 39991 | SWPP | 2021-02-16 | final5_boosting | 3.27 | -6.32 | -6.32 |
| 39993 | SWPP | 2021-02-16 | final5_ensemble | 3.83 | -0.86 | -0.86 |
| 39992 | SWPP | 2021-02-16 | final5_recency | 2.57 | -0.10 | -0.10 |
| 48335 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48334 | TVA | 2022-12-23 | final5 | 8.91 | -10.35 | -10.35 |
| 48330 | TVA | 2022-12-23 | final5_additive | 7.33 | -3.19 | -3.19 |
| 48331 | TVA | 2022-12-23 | final5_boosting | 15.23 | -16.37 | -16.37 |
| 48333 | TVA | 2022-12-23 | final5_ensemble | 8.63 | -9.78 | -9.78 |
| 48332 | TVA | 2022-12-23 | final5_recency | 11.83 | -10.22 | -10.22 |
| 48341 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48340 | TVA | 2022-12-24 | final5 | 5.45 | -10.41 | -10.41 |
| 48336 | TVA | 2022-12-24 | final5_additive | 3.82 | -9.06 | -9.06 |
| 48337 | TVA | 2022-12-24 | final5_boosting | 7.15 | -15.20 | -15.20 |
| 48339 | TVA | 2022-12-24 | final5_ensemble | 5.87 | -11.81 | -11.81 |
| 48338 | TVA | 2022-12-24 | final5_recency | 7.21 | -11.36 | -11.36 |

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
