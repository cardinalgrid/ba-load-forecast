# Phase G: feature blocks

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `*_xload` adds the load two and three weeks back and the mean of the same weekday last week; `*_xtemp` adds yesterday's extremes, the heating and cooling degree-hours of the previous 72 hours, the day's range and its temperature at 07:00 and 17:00; `boosting_xsun` gives every BA the sun's elevation; `*_xall` combines them.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| boosting_xall | 2.93 | 2.59 | -1.02 | -2.09 | 1.45 | 0.43 | 0.24 | -52.42 | 8056 | 11.00 |
| boosting_xtemp | 2.95 | 2.60 | -0.99 | -2.08 | 1.42 | 0.44 | 0.24 | -52.47 | 8056 | 11.00 |
| boosting_xload | 2.97 | 2.62 | -0.99 | -2.10 | 1.44 | 0.43 | 0.24 | -52.24 | 8056 | 11.00 |
| boosting_xsun | 3.00 | 2.64 | -0.98 | -2.11 | 1.49 | 0.43 | 0.24 | -51.98 | 8056 | 11.00 |
| final_boosting | 3.00 | 2.64 | -0.98 | -2.11 | 1.49 | 0.43 | 0.24 | -51.98 | 8056 | 11.00 |
| additive_xall | 3.00 | 2.64 | -1.31 | -2.32 | 1.32 | 0.44 | 0.23 | -49.89 | 8056 | 11.00 |
| additive_xtemp | 3.03 | 2.65 | -1.38 | -2.38 | 1.37 | 0.43 | 0.22 | -50.04 | 8056 | 11.00 |
| additive_xload | 3.10 | 2.72 | -1.38 | -2.39 | 1.41 | 0.42 | 0.22 | -50.73 | 8056 | 11.00 |
| final_additive | 3.11 | 2.74 | -1.45 | -2.45 | 1.41 | 0.42 | 0.22 | -50.91 | 8056 | 11.00 |

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
| additive_xall | BPAT | 2.69 | 2.37 | -0.69 | -1.66 | 1.77 | -16.93 | 0.30 | 0.22 | 746 | 6536.52 |
| additive_xall | CISO | 3.62 | 3.05 | -2.90 | -3.78 | 0.43 | -17.65 | 0.28 | 0.12 | 719 | 25193.76 |
| additive_xall | DUK | 3.52 | 3.15 | -0.58 | -2.30 | 1.39 | -14.98 | 0.35 | 0.26 | 746 | 12143.29 |
| additive_xall | ERCO | 3.44 | 3.00 | -2.09 | -2.90 | 1.04 | -15.86 | 0.32 | 0.16 | 742 | 46834.59 |
| additive_xall | FPL | 6.20 | 5.85 | -6.52 | -7.04 | 1.14 | -49.89 | 0.27 | 0.26 | 665 | 15346.05 |
| additive_xall | ISNE | 3.71 | 3.31 | -1.05 | -2.38 | 0.53 | -19.32 | 0.24 | 0.16 | 748 | 13403.92 |
| additive_xall | MISO | 2.34 | 2.09 | -1.21 | -1.84 | 1.60 | -8.30 | 0.55 | 0.05 | 738 | 73700.16 |
| additive_xall | NYIS | 2.60 | 2.28 | -0.83 | -1.97 | 0.56 | -15.30 | 0.55 | 0.60 | 748 | 17415.28 |
| additive_xall | PJM | 2.65 | 2.30 | -0.44 | -1.63 | 1.64 | -12.14 | 0.47 | 0.39 | 734 | 92076.14 |
| additive_xall | SWPP | 2.52 | 2.09 | -0.19 | -1.55 | 1.50 | -20.78 | 0.70 | 0.10 | 741 | 31382.01 |
| additive_xall | TVA | 3.25 | 2.89 | -0.89 | -2.22 | 1.45 | -14.41 | 0.27 | 0.25 | 729 | 18581.23 |
| additive_xload | BPAT | 2.79 | 2.47 | -0.85 | -1.79 | 1.84 | -18.70 | 0.29 | 0.22 | 746 | 6536.52 |
| additive_xload | CISO | 3.66 | 3.17 | -2.72 | -3.64 | 0.44 | -17.90 | 0.27 | 0.13 | 719 | 25193.76 |
| additive_xload | DUK | 3.58 | 3.19 | -0.61 | -2.35 | 1.35 | -14.69 | 0.36 | 0.25 | 746 | 12143.29 |
| additive_xload | ERCO | 3.57 | 3.13 | -2.18 | -3.01 | 1.11 | -16.75 | 0.31 | 0.16 | 742 | 46834.59 |
| additive_xload | FPL | 6.37 | 5.77 | -6.55 | -7.12 | 1.10 | -50.73 | 0.26 | 0.26 | 665 | 15346.05 |
| additive_xload | ISNE | 3.82 | 3.39 | -1.04 | -2.41 | 0.54 | -20.75 | 0.20 | 0.17 | 748 | 13403.92 |
| additive_xload | MISO | 2.43 | 2.19 | -1.28 | -1.90 | 1.82 | -8.66 | 0.53 | 0.05 | 738 | 73700.16 |
| additive_xload | NYIS | 2.70 | 2.32 | -0.72 | -1.94 | 0.59 | -13.89 | 0.53 | 0.61 | 748 | 17415.28 |
| additive_xload | PJM | 2.78 | 2.40 | -0.61 | -1.77 | 1.73 | -12.68 | 0.44 | 0.37 | 734 | 92076.14 |
| additive_xload | SWPP | 2.55 | 2.13 | -0.22 | -1.57 | 1.60 | -19.71 | 0.69 | 0.10 | 741 | 31382.01 |
| additive_xload | TVA | 3.32 | 2.94 | -0.95 | -2.27 | 1.48 | -14.22 | 0.25 | 0.26 | 729 | 18581.23 |
| additive_xtemp | BPAT | 2.70 | 2.37 | -0.73 | -1.68 | 1.81 | -16.75 | 0.31 | 0.22 | 746 | 6536.52 |
| additive_xtemp | CISO | 3.75 | 3.10 | -2.95 | -3.89 | 0.42 | -18.34 | 0.27 | 0.13 | 719 | 25193.76 |
| additive_xtemp | DUK | 3.52 | 3.08 | -0.64 | -2.32 | 1.42 | -14.55 | 0.36 | 0.27 | 746 | 12143.29 |
| additive_xtemp | ERCO | 3.44 | 2.99 | -2.15 | -2.94 | 1.06 | -15.53 | 0.31 | 0.16 | 742 | 46834.59 |
| additive_xtemp | FPL | 6.14 | 5.70 | -6.39 | -6.90 | 1.09 | -50.04 | 0.28 | 0.27 | 665 | 15346.05 |
| additive_xtemp | ISNE | 3.77 | 3.41 | -1.10 | -2.46 | 0.54 | -19.72 | 0.23 | 0.16 | 748 | 13403.92 |
| additive_xtemp | MISO | 2.37 | 2.11 | -1.35 | -1.94 | 1.76 | -9.47 | 0.54 | 0.05 | 738 | 73700.16 |
| additive_xtemp | NYIS | 2.64 | 2.28 | -0.88 | -2.06 | 0.55 | -15.69 | 0.54 | 0.60 | 748 | 17415.28 |
| additive_xtemp | PJM | 2.68 | 2.37 | -0.51 | -1.69 | 1.73 | -11.80 | 0.45 | 0.39 | 734 | 92076.14 |
| additive_xtemp | SWPP | 2.50 | 2.06 | -0.25 | -1.57 | 1.45 | -21.23 | 0.70 | 0.10 | 741 | 31382.01 |
| additive_xtemp | TVA | 3.28 | 2.91 | -0.97 | -2.29 | 1.43 | -14.27 | 0.28 | 0.25 | 729 | 18581.23 |
| boosting_xall | BPAT | 2.68 | 2.40 | -0.45 | -1.59 | 2.00 | -18.49 | 0.29 | 0.24 | 746 | 6536.52 |
| boosting_xall | CISO | 2.94 | 2.60 | -2.00 | -2.61 | 0.42 | -17.41 | 0.36 | 0.16 | 719 | 25193.76 |
| boosting_xall | DUK | 3.48 | 3.01 | -0.52 | -2.25 | 1.50 | -17.80 | 0.34 | 0.27 | 746 | 12143.29 |
| boosting_xall | ERCO | 3.05 | 2.59 | -2.33 | -2.99 | 1.30 | -20.78 | 0.36 | 0.17 | 742 | 46834.59 |
| boosting_xall | FPL | 6.27 | 5.94 | -6.68 | -7.03 | 1.32 | -52.42 | 0.20 | 0.26 | 665 | 15346.05 |
| boosting_xall | ISNE | 3.69 | 3.30 | -0.71 | -2.02 | 0.55 | -18.20 | 0.24 | 0.18 | 748 | 13403.92 |
| boosting_xall | MISO | 2.33 | 2.02 | -0.55 | -1.44 | 1.70 | -10.28 | 0.55 | 0.05 | 738 | 73700.16 |
| boosting_xall | NYIS | 2.68 | 2.35 | -0.38 | -1.51 | 0.79 | -12.12 | 0.51 | 0.69 | 748 | 17415.28 |
| boosting_xall | PJM | 2.74 | 2.49 | 0.07 | -1.39 | 1.78 | -12.01 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xall | SWPP | 2.61 | 2.15 | -0.93 | -1.97 | 1.55 | -28.20 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xall | TVA | 3.20 | 2.80 | -0.39 | -1.92 | 1.52 | -12.82 | 0.27 | 0.28 | 729 | 18581.23 |
| boosting_xload | BPAT | 2.69 | 2.40 | -0.41 | -1.56 | 2.04 | -17.96 | 0.27 | 0.24 | 746 | 6536.52 |
| boosting_xload | CISO | 2.94 | 2.59 | -2.00 | -2.60 | 0.43 | -16.43 | 0.35 | 0.16 | 719 | 25193.76 |
| boosting_xload | DUK | 3.55 | 3.15 | -0.49 | -2.27 | 1.44 | -16.27 | 0.34 | 0.26 | 746 | 12143.29 |
| boosting_xload | ERCO | 3.13 | 2.69 | -2.28 | -3.00 | 1.38 | -20.67 | 0.35 | 0.17 | 742 | 46834.59 |
| boosting_xload | FPL | 6.33 | 5.99 | -6.78 | -7.13 | 1.32 | -52.24 | 0.18 | 0.27 | 665 | 15346.05 |
| boosting_xload | ISNE | 3.66 | 3.27 | -0.85 | -2.08 | 0.57 | -20.95 | 0.26 | 0.16 | 748 | 13403.92 |
| boosting_xload | MISO | 2.35 | 2.06 | -0.52 | -1.46 | 1.61 | -9.78 | 0.55 | 0.06 | 738 | 73700.16 |
| boosting_xload | NYIS | 2.68 | 2.38 | -0.44 | -1.56 | 0.74 | -14.66 | 0.51 | 0.67 | 748 | 17415.28 |
| boosting_xload | PJM | 2.79 | 2.49 | 0.12 | -1.39 | 1.72 | -12.65 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xload | SWPP | 2.60 | 2.20 | -0.87 | -1.94 | 1.69 | -27.93 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xload | TVA | 3.23 | 2.79 | -0.27 | -1.85 | 1.60 | -11.70 | 0.26 | 0.30 | 729 | 18581.23 |
| boosting_xsun | BPAT | 2.73 | 2.43 | -0.45 | -1.58 | 2.01 | -18.16 | 0.27 | 0.24 | 746 | 6536.52 |
| boosting_xsun | CISO | 2.98 | 2.63 | -1.96 | -2.58 | 0.40 | -15.52 | 0.36 | 0.16 | 719 | 25193.76 |
| boosting_xsun | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| boosting_xsun | ERCO | 3.14 | 2.73 | -2.28 | -2.99 | 1.30 | -15.00 | 0.35 | 0.18 | 742 | 46834.59 |
| boosting_xsun | FPL | 6.33 | 5.95 | -6.77 | -7.11 | 1.37 | -51.98 | 0.19 | 0.26 | 665 | 15346.05 |
| boosting_xsun | ISNE | 3.66 | 3.33 | -0.80 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 748 | 13403.92 |
| boosting_xsun | MISO | 2.41 | 2.07 | -0.51 | -1.44 | 1.81 | -11.84 | 0.54 | 0.06 | 738 | 73700.16 |
| boosting_xsun | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.75 | -14.02 | 0.51 | 0.66 | 748 | 17415.28 |
| boosting_xsun | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xsun | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xsun | TVA | 3.27 | 2.84 | -0.22 | -1.83 | 1.53 | -12.19 | 0.25 | 0.30 | 729 | 18581.23 |
| boosting_xtemp | BPAT | 2.73 | 2.45 | -0.49 | -1.62 | 1.94 | -17.98 | 0.28 | 0.24 | 746 | 6536.52 |
| boosting_xtemp | CISO | 2.99 | 2.66 | -1.95 | -2.59 | 0.41 | -16.34 | 0.37 | 0.15 | 719 | 25193.76 |
| boosting_xtemp | DUK | 3.49 | 3.03 | -0.51 | -2.25 | 1.43 | -17.27 | 0.38 | 0.27 | 746 | 12143.29 |
| boosting_xtemp | ERCO | 3.05 | 2.60 | -2.30 | -2.95 | 1.35 | -15.86 | 0.36 | 0.18 | 742 | 46834.59 |
| boosting_xtemp | FPL | 6.28 | 5.95 | -6.66 | -7.01 | 1.29 | -52.47 | 0.18 | 0.27 | 665 | 15346.05 |
| boosting_xtemp | ISNE | 3.67 | 3.25 | -0.71 | -2.01 | 0.58 | -21.78 | 0.26 | 0.16 | 748 | 13403.92 |
| boosting_xtemp | MISO | 2.38 | 2.08 | -0.53 | -1.45 | 1.70 | -9.96 | 0.56 | 0.05 | 738 | 73700.16 |
| boosting_xtemp | NYIS | 2.67 | 2.33 | -0.39 | -1.54 | 0.74 | -12.68 | 0.51 | 0.66 | 748 | 17415.28 |
| boosting_xtemp | PJM | 2.73 | 2.47 | 0.10 | -1.39 | 1.64 | -11.49 | 0.43 | 0.41 | 734 | 92076.14 |
| boosting_xtemp | SWPP | 2.66 | 2.16 | -0.85 | -1.94 | 1.62 | -29.50 | 0.67 | 0.08 | 741 | 31382.01 |
| boosting_xtemp | TVA | 3.21 | 2.77 | -0.36 | -1.89 | 1.58 | -13.33 | 0.25 | 0.28 | 729 | 18581.23 |
| final_additive | BPAT | 2.80 | 2.44 | -0.88 | -1.80 | 1.84 | -18.41 | 0.29 | 0.22 | 746 | 6536.52 |
| final_additive | CISO | 3.76 | 3.16 | -2.79 | -3.75 | 0.43 | -18.08 | 0.26 | 0.13 | 719 | 25193.76 |
| final_additive | DUK | 3.56 | 3.15 | -0.71 | -2.39 | 1.42 | -14.75 | 0.34 | 0.27 | 746 | 12143.29 |
| final_additive | ERCO | 3.57 | 3.14 | -2.24 | -3.05 | 1.11 | -16.37 | 0.30 | 0.15 | 742 | 46834.59 |
| final_additive | FPL | 6.22 | 5.64 | -6.28 | -6.87 | 1.10 | -50.91 | 0.29 | 0.27 | 665 | 15346.05 |
| final_additive | ISNE | 3.86 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 748 | 13403.92 |
| final_additive | MISO | 2.44 | 2.18 | -1.43 | -1.99 | 1.83 | -9.48 | 0.54 | 0.05 | 738 | 73700.16 |
| final_additive | NYIS | 2.72 | 2.37 | -0.87 | -2.09 | 0.60 | -15.67 | 0.51 | 0.59 | 748 | 17415.28 |
| final_additive | PJM | 2.81 | 2.47 | -0.68 | -1.84 | 1.77 | -12.10 | 0.42 | 0.37 | 734 | 92076.14 |
| final_additive | SWPP | 2.53 | 2.11 | -0.28 | -1.59 | 1.49 | -20.36 | 0.70 | 0.10 | 741 | 31382.01 |
| final_additive | TVA | 3.34 | 2.95 | -1.03 | -2.33 | 1.41 | -14.12 | 0.25 | 0.26 | 729 | 18581.23 |
| final_boosting | BPAT | 2.73 | 2.43 | -0.45 | -1.58 | 2.01 | -18.16 | 0.27 | 0.24 | 746 | 6536.52 |
| final_boosting | CISO | 2.98 | 2.63 | -1.96 | -2.58 | 0.40 | -15.52 | 0.36 | 0.16 | 719 | 25193.76 |
| final_boosting | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| final_boosting | ERCO | 3.14 | 2.73 | -2.28 | -2.99 | 1.30 | -15.00 | 0.35 | 0.18 | 742 | 46834.59 |
| final_boosting | FPL | 6.33 | 5.95 | -6.77 | -7.11 | 1.37 | -51.98 | 0.19 | 0.26 | 665 | 15346.05 |
| final_boosting | ISNE | 3.66 | 3.33 | -0.80 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 748 | 13403.92 |
| final_boosting | MISO | 2.41 | 2.07 | -0.51 | -1.44 | 1.81 | -11.84 | 0.54 | 0.06 | 738 | 73700.16 |
| final_boosting | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.75 | -14.02 | 0.51 | 0.66 | 748 | 17415.28 |
| final_boosting | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| final_boosting | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |
| final_boosting | TVA | 3.27 | 2.84 | -0.22 | -1.83 | 1.53 | -12.19 | 0.25 | 0.30 | 729 | 18581.23 |

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
| additive_xall | BPAT | uri | 2.81 | -0.35 | -1.21 | -2.29 | 6 |
| additive_xall | CISO | uri | 2.21 | 1.49 | -0.05 | -0.30 | 6 |
| additive_xall | DUK | uri | 3.49 | -1.84 | -1.91 | -6.46 | 6 |
| additive_xall | ERCO | uri | 4.34 | -4.90 | -4.90 | -7.68 | 2 |
| additive_xall | FPL | uri | 10.53 | -15.09 | -15.09 | -18.04 | 6 |
| additive_xall | ISNE | uri | 2.98 | 1.99 | -0.20 | -1.20 | 6 |
| additive_xall | MISO | uri | 3.67 | -2.41 | -3.04 | -6.36 | 5 |
| additive_xall | NYIS | uri | 2.66 | 3.01 | 0.00 | 0.00 | 6 |
| additive_xall | PJM | uri | 3.14 | 3.01 | -0.41 | -2.47 | 6 |
| additive_xall | SWPP | uri | 6.47 | 1.82 | -2.00 | -5.04 | 4 |
| additive_xall | TVA | uri | 3.46 | 0.64 | -1.03 | -2.61 | 6 |
| additive_xload | BPAT | uri | 3.07 | -0.01 | -1.08 | -2.31 | 6 |
| additive_xload | CISO | uri | 2.54 | 2.14 | 0.00 | 0.00 | 6 |
| additive_xload | DUK | uri | 3.45 | -2.22 | -2.22 | -6.93 | 6 |
| additive_xload | ERCO | uri | 4.89 | -5.83 | -5.83 | -8.07 | 2 |
| additive_xload | FPL | uri | 10.18 | -14.15 | -14.15 | -17.19 | 6 |
| additive_xload | ISNE | uri | 2.79 | 1.69 | -0.26 | -1.58 | 6 |
| additive_xload | MISO | uri | 3.81 | -3.11 | -3.48 | -6.98 | 5 |
| additive_xload | NYIS | uri | 2.51 | 2.56 | 0.00 | 0.00 | 6 |
| additive_xload | PJM | uri | 3.11 | 2.58 | -0.37 | -2.24 | 6 |
| additive_xload | SWPP | uri | 6.41 | 1.23 | -2.16 | -5.48 | 4 |
| additive_xload | TVA | uri | 3.37 | 0.11 | -1.23 | -3.01 | 6 |
| additive_xtemp | BPAT | uri | 2.89 | -0.60 | -1.46 | -2.84 | 6 |
| additive_xtemp | CISO | uri | 2.14 | 1.62 | -0.03 | -0.15 | 6 |
| additive_xtemp | DUK | uri | 3.46 | -2.33 | -2.35 | -7.06 | 6 |
| additive_xtemp | ERCO | uri | 4.17 | -4.61 | -4.61 | -7.57 | 2 |
| additive_xtemp | FPL | uri | 10.78 | -15.51 | -15.51 | -18.47 | 6 |
| additive_xtemp | ISNE | uri | 2.69 | 1.79 | -0.19 | -1.14 | 6 |
| additive_xtemp | MISO | uri | 3.39 | -1.58 | -2.30 | -4.60 | 5 |
| additive_xtemp | NYIS | uri | 2.33 | 2.45 | 0.00 | 0.00 | 6 |
| additive_xtemp | PJM | uri | 3.00 | 2.79 | -0.47 | -2.80 | 6 |
| additive_xtemp | SWPP | uri | 6.59 | 2.33 | -1.74 | -4.71 | 4 |
| additive_xtemp | TVA | uri | 3.36 | 0.57 | -0.98 | -2.41 | 6 |
| boosting_xall | BPAT | uri | 3.45 | 1.33 | -0.90 | -5.38 | 6 |
| boosting_xall | CISO | uri | 2.29 | -1.67 | -1.95 | -4.65 | 6 |
| boosting_xall | DUK | uri | 3.73 | -2.45 | -2.62 | -5.37 | 6 |
| boosting_xall | ERCO | uri | 8.42 | -13.34 | -13.34 | -14.88 | 2 |
| boosting_xall | FPL | uri | 8.95 | -10.96 | -10.96 | -13.77 | 6 |
| boosting_xall | ISNE | uri | 3.75 | 2.24 | -0.56 | -2.76 | 6 |
| boosting_xall | MISO | uri | 3.11 | -2.80 | -2.94 | -5.79 | 5 |
| boosting_xall | NYIS | uri | 2.63 | 0.87 | -0.61 | -3.20 | 6 |
| boosting_xall | PJM | uri | 2.04 | -0.72 | -0.98 | -1.97 | 6 |
| boosting_xall | SWPP | uri | 5.87 | -3.34 | -4.47 | -10.32 | 4 |
| boosting_xall | TVA | uri | 2.69 | -1.33 | -1.86 | -4.11 | 6 |
| boosting_xload | BPAT | uri | 3.40 | 1.21 | -0.87 | -5.05 | 6 |
| boosting_xload | CISO | uri | 1.90 | -0.86 | -1.33 | -3.90 | 6 |
| boosting_xload | DUK | uri | 3.57 | -2.86 | -2.93 | -4.81 | 6 |
| boosting_xload | ERCO | uri | 8.79 | -13.01 | -13.01 | -14.64 | 2 |
| boosting_xload | FPL | uri | 9.26 | -11.06 | -11.06 | -14.67 | 6 |
| boosting_xload | ISNE | uri | 3.81 | 2.12 | -0.32 | -1.65 | 6 |
| boosting_xload | MISO | uri | 3.02 | -3.17 | -3.17 | -5.44 | 5 |
| boosting_xload | NYIS | uri | 2.58 | 0.98 | -0.81 | -2.49 | 6 |
| boosting_xload | PJM | uri | 2.04 | -1.19 | -1.40 | -3.32 | 6 |
| boosting_xload | SWPP | uri | 5.28 | -3.27 | -4.40 | -10.34 | 4 |
| boosting_xload | TVA | uri | 3.03 | -2.95 | -3.36 | -6.04 | 6 |
| boosting_xsun | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| boosting_xsun | CISO | uri | 1.85 | -0.83 | -0.99 | -2.55 | 6 |
| boosting_xsun | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_xsun | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| boosting_xsun | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| boosting_xsun | ISNE | uri | 3.32 | 1.07 | -0.73 | -3.06 | 6 |
| boosting_xsun | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_xsun | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| boosting_xsun | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_xsun | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_xsun | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| boosting_xtemp | BPAT | uri | 3.40 | 0.79 | -0.92 | -5.38 | 6 |
| boosting_xtemp | CISO | uri | 2.25 | -1.19 | -1.50 | -2.94 | 6 |
| boosting_xtemp | DUK | uri | 3.60 | -2.52 | -2.58 | -5.65 | 6 |
| boosting_xtemp | ERCO | uri | 7.36 | -12.56 | -12.56 | -14.77 | 2 |
| boosting_xtemp | FPL | uri | 9.05 | -10.93 | -10.93 | -13.65 | 6 |
| boosting_xtemp | ISNE | uri | 3.46 | 0.98 | -0.82 | -3.31 | 6 |
| boosting_xtemp | MISO | uri | 3.06 | -3.26 | -3.31 | -6.50 | 5 |
| boosting_xtemp | NYIS | uri | 2.36 | 1.14 | -0.42 | -2.50 | 6 |
| boosting_xtemp | PJM | uri | 1.86 | -0.63 | -1.04 | -3.39 | 6 |
| boosting_xtemp | SWPP | uri | 5.79 | -2.74 | -4.18 | -9.79 | 4 |
| boosting_xtemp | TVA | uri | 3.01 | -1.95 | -2.54 | -5.20 | 6 |
| final_additive | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| final_additive | CISO | uri | 2.40 | 2.19 | 0.00 | 0.00 | 6 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| final_additive | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| final_additive | ISNE | uri | 2.56 | 1.52 | -0.29 | -1.49 | 6 |
| final_additive | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| final_additive | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| final_additive | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| final_boosting | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| final_boosting | CISO | uri | 1.85 | -0.83 | -0.99 | -2.55 | 6 |
| final_boosting | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| final_boosting | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| final_boosting | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| final_boosting | ISNE | uri | 3.32 | 1.07 | -0.73 | -3.06 | 6 |
| final_boosting | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| final_boosting | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| final_boosting | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
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
| additive_xall | BPAT | elliott | 3.64 | -1.16 | -2.00 | -4.21 | 5 |
| additive_xall | CISO | elliott | 3.47 | 3.77 | -0.32 | -1.61 | 5 |
| additive_xall | DUK | elliott | 4.58 | -3.41 | -3.41 | -5.07 | 4 |
| additive_xall | ERCO | elliott | 7.48 | -5.62 | -6.17 | -14.01 | 5 |
| additive_xall | FPL | elliott | 10.32 | -0.39 | -5.39 | -13.75 | 5 |
| additive_xall | ISNE | elliott | 3.84 | 2.32 | -0.91 | -2.27 | 5 |
| additive_xall | MISO | elliott | 3.36 | -3.29 | -3.60 | -7.71 | 5 |
| additive_xall | NYIS | elliott | 3.13 | -0.97 | -2.04 | -4.49 | 5 |
| additive_xall | PJM | elliott | 3.53 | -0.16 | -0.93 | -4.57 | 5 |
| additive_xall | SWPP | elliott | 3.00 | -2.57 | -2.84 | -5.40 | 5 |
| additive_xall | TVA | elliott | 5.91 | 3.10 | -0.19 | -0.57 | 3 |
| additive_xload | BPAT | elliott | 4.35 | -1.18 | -2.22 | -4.53 | 5 |
| additive_xload | CISO | elliott | 3.38 | 4.07 | -0.04 | -0.20 | 5 |
| additive_xload | DUK | elliott | 4.26 | -3.35 | -3.35 | -4.89 | 4 |
| additive_xload | ERCO | elliott | 7.84 | -5.90 | -6.66 | -13.03 | 5 |
| additive_xload | FPL | elliott | 11.54 | -2.60 | -7.60 | -18.90 | 5 |
| additive_xload | ISNE | elliott | 4.13 | 1.59 | -0.79 | -2.23 | 5 |
| additive_xload | MISO | elliott | 3.46 | -3.43 | -3.68 | -6.87 | 5 |
| additive_xload | NYIS | elliott | 3.45 | -2.17 | -2.47 | -5.12 | 5 |
| additive_xload | PJM | elliott | 3.79 | -1.37 | -1.98 | -8.99 | 5 |
| additive_xload | SWPP | elliott | 3.36 | -2.66 | -2.88 | -6.85 | 5 |
| additive_xload | TVA | elliott | 6.25 | 4.25 | -0.23 | -0.70 | 3 |
| additive_xtemp | BPAT | elliott | 3.73 | -1.41 | -2.26 | -4.53 | 5 |
| additive_xtemp | CISO | elliott | 3.61 | 3.84 | -0.36 | -1.82 | 5 |
| additive_xtemp | DUK | elliott | 4.63 | -2.45 | -2.47 | -5.20 | 4 |
| additive_xtemp | ERCO | elliott | 7.46 | -4.85 | -5.56 | -13.79 | 5 |
| additive_xtemp | FPL | elliott | 10.90 | 0.44 | -5.46 | -14.64 | 5 |
| additive_xtemp | ISNE | elliott | 3.71 | 2.50 | -0.73 | -2.33 | 5 |
| additive_xtemp | MISO | elliott | 3.32 | -2.99 | -3.43 | -6.61 | 5 |
| additive_xtemp | NYIS | elliott | 3.02 | -0.76 | -1.77 | -4.35 | 5 |
| additive_xtemp | PJM | elliott | 3.60 | -0.12 | -0.90 | -4.52 | 5 |
| additive_xtemp | SWPP | elliott | 3.33 | -2.50 | -2.97 | -6.48 | 5 |
| additive_xtemp | TVA | elliott | 6.41 | 4.17 | 0.00 | 0.00 | 3 |
| boosting_xall | BPAT | elliott | 4.46 | -4.51 | -4.74 | -11.66 | 5 |
| boosting_xall | CISO | elliott | 3.96 | 1.50 | -1.06 | -4.75 | 5 |
| boosting_xall | DUK | elliott | 4.71 | -2.60 | -2.60 | -5.62 | 4 |
| boosting_xall | ERCO | elliott | 6.96 | -9.54 | -9.70 | -20.78 | 5 |
| boosting_xall | FPL | elliott | 8.83 | -15.37 | -15.37 | -19.13 | 5 |
| boosting_xall | ISNE | elliott | 3.89 | 3.39 | -0.45 | -2.23 | 5 |
| boosting_xall | MISO | elliott | 3.66 | -1.07 | -2.19 | -3.48 | 5 |
| boosting_xall | NYIS | elliott | 3.11 | 0.19 | -0.87 | -2.78 | 5 |
| boosting_xall | PJM | elliott | 5.27 | -2.75 | -3.77 | -7.24 | 5 |
| boosting_xall | SWPP | elliott | 5.50 | -1.75 | -3.68 | -11.27 | 5 |
| boosting_xall | TVA | elliott | 6.27 | 0.61 | -0.98 | -2.94 | 3 |
| boosting_xload | BPAT | elliott | 4.56 | -5.02 | -5.12 | -12.47 | 5 |
| boosting_xload | CISO | elliott | 4.05 | 1.64 | -0.93 | -4.41 | 5 |
| boosting_xload | DUK | elliott | 4.64 | -3.33 | -3.33 | -6.47 | 4 |
| boosting_xload | ERCO | elliott | 7.17 | -7.37 | -8.35 | -20.67 | 5 |
| boosting_xload | FPL | elliott | 9.74 | -15.77 | -15.77 | -22.71 | 5 |
| boosting_xload | ISNE | elliott | 3.38 | 2.62 | -0.30 | -1.52 | 5 |
| boosting_xload | MISO | elliott | 3.30 | -1.53 | -2.45 | -4.59 | 5 |
| boosting_xload | NYIS | elliott | 2.87 | -0.76 | -1.65 | -3.86 | 5 |
| boosting_xload | PJM | elliott | 5.09 | -2.53 | -3.43 | -6.72 | 5 |
| boosting_xload | SWPP | elliott | 5.00 | -2.74 | -4.31 | -11.73 | 5 |
| boosting_xload | TVA | elliott | 6.12 | 1.27 | -1.03 | -3.08 | 3 |
| boosting_xsun | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| boosting_xsun | CISO | elliott | 3.81 | 1.69 | -0.73 | -3.66 | 5 |
| boosting_xsun | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| boosting_xsun | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| boosting_xsun | FPL | elliott | 9.68 | -16.11 | -16.11 | -23.65 | 5 |
| boosting_xsun | ISNE | elliott | 3.32 | 2.41 | -0.31 | -1.57 | 5 |
| boosting_xsun | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| boosting_xsun | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| boosting_xsun | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| boosting_xsun | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| boosting_xsun | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |
| boosting_xtemp | BPAT | elliott | 4.55 | -5.11 | -5.22 | -11.46 | 5 |
| boosting_xtemp | CISO | elliott | 4.00 | 1.97 | -0.63 | -3.16 | 5 |
| boosting_xtemp | DUK | elliott | 4.65 | -3.11 | -3.11 | -6.79 | 4 |
| boosting_xtemp | ERCO | elliott | 6.07 | -7.54 | -7.68 | -15.86 | 5 |
| boosting_xtemp | FPL | elliott | 8.72 | -14.70 | -14.70 | -19.58 | 5 |
| boosting_xtemp | ISNE | elliott | 3.51 | 3.16 | -0.31 | -1.16 | 5 |
| boosting_xtemp | MISO | elliott | 3.99 | -0.24 | -1.76 | -3.39 | 5 |
| boosting_xtemp | NYIS | elliott | 3.03 | 0.01 | -1.04 | -4.08 | 5 |
| boosting_xtemp | PJM | elliott | 5.38 | -1.56 | -2.95 | -5.92 | 5 |
| boosting_xtemp | SWPP | elliott | 4.59 | -1.33 | -3.29 | -10.96 | 5 |
| boosting_xtemp | TVA | elliott | 6.15 | -0.22 | -1.41 | -2.93 | 3 |
| final_additive | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| final_additive | CISO | elliott | 3.53 | 4.14 | -0.08 | -0.41 | 5 |
| final_additive | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| final_additive | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| final_additive | FPL | elliott | 11.83 | -1.71 | -7.55 | -19.18 | 5 |
| final_additive | ISNE | elliott | 3.99 | 1.75 | -0.62 | -2.38 | 5 |
| final_additive | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| final_additive | NYIS | elliott | 3.27 | -1.91 | -2.37 | -3.71 | 5 |
| final_additive | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| final_additive | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| final_additive | TVA | elliott | 7.91 | 5.47 | 0.00 | 0.00 | 3 |
| final_boosting | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| final_boosting | CISO | elliott | 3.81 | 1.69 | -0.73 | -3.66 | 5 |
| final_boosting | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| final_boosting | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| final_boosting | FPL | elliott | 9.68 | -16.11 | -16.11 | -23.65 | 5 |
| final_boosting | ISNE | elliott | 3.32 | 2.41 | -0.31 | -1.57 | 5 |
| final_boosting | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| final_boosting | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| final_boosting | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| final_boosting | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| final_boosting | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 11 | additive_xall | eve | 3.67 | 0.09 | -2.01 | 0.43 | 265 |
| 13 | additive_xtemp | eve | 3.76 | 0.18 | -2.02 | 0.44 | 265 |
| 12 | additive_xload | eve | 3.77 | -0.17 | -2.17 | 0.40 | 265 |
| 14 | boosting_xall | eve | 3.79 | -0.22 | -2.14 | 0.39 | 265 |
| 15 | boosting_xload | eve | 3.82 | -0.16 | -2.16 | 0.40 | 265 |
| 18 | final_additive | eve | 3.83 | -0.12 | -2.20 | 0.40 | 265 |
| 16 | boosting_xsun | eve | 3.87 | -0.07 | -2.12 | 0.40 | 265 |
| 19 | final_boosting | eve | 3.87 | -0.07 | -2.12 | 0.40 | 265 |
| 17 | boosting_xtemp | eve | 3.87 | -0.14 | -2.16 | 0.39 | 265 |
| 1 | additive_xall | special | 3.70 | -1.79 | -3.04 | 0.48 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 2 | additive_xload | special | 3.78 | -1.96 | -3.14 | 0.46 | 267 |
| 3 | additive_xtemp | special | 3.78 | -1.68 | -3.01 | 0.48 | 267 |
| 8 | final_additive | special | 3.85 | -1.83 | -3.10 | 0.46 | 267 |
| 4 | boosting_xall | special | 3.89 | -1.72 | -2.94 | 0.47 | 267 |
| 5 | boosting_xload | special | 3.89 | -1.68 | -2.93 | 0.45 | 267 |
| 6 | boosting_xsun | special | 3.94 | -1.62 | -2.95 | 0.42 | 267 |
| 9 | final_boosting | special | 3.94 | -1.62 | -2.95 | 0.42 | 267 |
| 7 | boosting_xtemp | special | 3.95 | -1.70 | -2.96 | 0.44 | 267 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 22049 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 22044 | DUK | 2022-12-24 | additive_xall | 6.92 | -12.48 | -12.48 |
| 22042 | DUK | 2022-12-24 | additive_xload | 6.45 | -12.81 | -12.81 |
| 22043 | DUK | 2022-12-24 | additive_xtemp | 7.27 | -12.54 | -12.54 |
| 22048 | DUK | 2022-12-24 | boosting_xall | 9.37 | -16.02 | -16.02 |
| 22045 | DUK | 2022-12-24 | boosting_xload | 10.22 | -17.91 | -17.91 |
| 22047 | DUK | 2022-12-24 | boosting_xsun | 9.36 | -15.80 | -15.80 |
| 22046 | DUK | 2022-12-24 | boosting_xtemp | 9.25 | -15.80 | -15.80 |
| 22040 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 22041 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 22869 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 22864 | ERCO | 2021-02-17 | additive_xall | 30.43 | 28.75 | 0.00 |
| 22862 | ERCO | 2021-02-17 | additive_xload | 31.30 | 28.65 | 0.00 |
| 22863 | ERCO | 2021-02-17 | additive_xtemp | 30.91 | 29.80 | 0.00 |
| 22868 | ERCO | 2021-02-17 | boosting_xall | 29.67 | 25.77 | 0.00 |
| 22865 | ERCO | 2021-02-17 | boosting_xload | 29.14 | 24.45 | 0.00 |
| 22867 | ERCO | 2021-02-17 | boosting_xsun | 28.91 | 24.01 | 0.00 |
| 22866 | ERCO | 2021-02-17 | boosting_xtemp | 30.00 | 24.27 | 0.00 |
| 22860 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 22861 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 22879 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 22874 | ERCO | 2021-02-18 | additive_xall | 13.30 | 11.77 | 0.00 |
| 22872 | ERCO | 2021-02-18 | additive_xload | 13.09 | 12.54 | 0.00 |
| 22873 | ERCO | 2021-02-18 | additive_xtemp | 13.38 | 11.95 | 0.00 |
| 22878 | ERCO | 2021-02-18 | boosting_xall | 3.47 | -7.67 | -7.67 |
| 22875 | ERCO | 2021-02-18 | boosting_xload | 3.01 | -4.35 | -4.35 |
| 22877 | ERCO | 2021-02-18 | boosting_xsun | 3.58 | -2.96 | -2.96 |
| 22876 | ERCO | 2021-02-18 | boosting_xtemp | 4.15 | -8.51 | -8.51 |
| 22870 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 22871 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 44449 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 44444 | MISO | 2021-02-16 | additive_xall | 2.33 | 2.19 | 0.00 |
| 44442 | MISO | 2021-02-16 | additive_xload | 2.16 | 1.93 | 0.00 |
| 44443 | MISO | 2021-02-16 | additive_xtemp | 2.58 | 2.31 | 0.00 |
| 44448 | MISO | 2021-02-16 | boosting_xall | 2.22 | 0.36 | 0.00 |
| 44445 | MISO | 2021-02-16 | boosting_xload | 1.99 | -0.79 | -0.79 |
| 44447 | MISO | 2021-02-16 | boosting_xsun | 2.11 | 0.99 | 0.00 |
| 44446 | MISO | 2021-02-16 | boosting_xtemp | 2.65 | 1.84 | 0.00 |
| 44440 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 44441 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 66649 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 66644 | SWPP | 2021-02-15 | additive_xall | 2.38 | 1.40 | 0.00 |
| 66642 | SWPP | 2021-02-15 | additive_xload | 2.31 | 1.02 | 0.00 |
| 66643 | SWPP | 2021-02-15 | additive_xtemp | 2.77 | 1.43 | 0.00 |
| 66648 | SWPP | 2021-02-15 | boosting_xall | 6.26 | -8.32 | -8.32 |
| 66645 | SWPP | 2021-02-15 | boosting_xload | 6.27 | -8.52 | -8.52 |
| 66647 | SWPP | 2021-02-15 | boosting_xsun | 5.58 | -7.79 | -7.79 |
| 66646 | SWPP | 2021-02-15 | boosting_xtemp | 6.09 | -8.25 | -8.25 |
| 66640 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 66641 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 66659 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 66654 | SWPP | 2021-02-16 | additive_xall | 7.58 | 3.67 | 0.00 |
| 66652 | SWPP | 2021-02-16 | additive_xload | 7.54 | 3.32 | 0.00 |
| 66653 | SWPP | 2021-02-16 | additive_xtemp | 8.04 | 3.60 | 0.00 |
| 66658 | SWPP | 2021-02-16 | boosting_xall | 3.17 | -5.46 | -5.46 |
| 66655 | SWPP | 2021-02-16 | boosting_xload | 3.36 | -5.76 | -5.76 |
| 66657 | SWPP | 2021-02-16 | boosting_xsun | 3.72 | -6.44 | -6.44 |
| 66656 | SWPP | 2021-02-16 | boosting_xtemp | 3.40 | -6.73 | -6.73 |
| 66650 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 66651 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 80559 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 80554 | TVA | 2022-12-23 | additive_xall | 7.72 | -3.74 | -3.74 |
| 80552 | TVA | 2022-12-23 | additive_xload | 6.91 | -4.39 | -4.39 |
| 80553 | TVA | 2022-12-23 | additive_xtemp | 6.87 | -1.82 | -1.82 |
| 80558 | TVA | 2022-12-23 | boosting_xall | 15.15 | -15.60 | -15.60 |
| 80555 | TVA | 2022-12-23 | boosting_xload | 15.35 | -16.72 | -16.72 |
| 80557 | TVA | 2022-12-23 | boosting_xsun | 13.98 | -15.00 | -15.00 |
| 80556 | TVA | 2022-12-23 | boosting_xtemp | 14.10 | -15.46 | -15.46 |
| 80550 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 80551 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 80569 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 80564 | TVA | 2022-12-24 | additive_xall | 3.92 | -9.05 | -9.05 |
| 80562 | TVA | 2022-12-24 | additive_xload | 3.73 | -9.11 | -9.11 |
| 80563 | TVA | 2022-12-24 | additive_xtemp | 3.81 | -8.56 | -8.56 |
| 80568 | TVA | 2022-12-24 | boosting_xall | 6.59 | -15.23 | -15.23 |
| 80565 | TVA | 2022-12-24 | boosting_xload | 7.02 | -15.81 | -15.81 |
| 80567 | TVA | 2022-12-24 | boosting_xsun | 6.04 | -12.78 | -12.78 |
| 80566 | TVA | 2022-12-24 | boosting_xtemp | 6.60 | -13.52 | -13.52 |
| 80560 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 80561 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_xall | BPAT | mape | 11.482 | 0.000 | 746 |
| additive_xall | CISO | mape | 15.935 | 0.000 | 719 |
| additive_xall | DUK | mape | 9.584 | 0.000 | 746 |
| additive_xall | ERCO | mape | 10.610 | 0.000 | 742 |
| additive_xall | FPL | mape | 17.818 | 0.000 | 665 |
| additive_xall | ISNE | mape | 19.452 | 0.000 | 748 |
| additive_xall | MISO | mape | -4.388 | 0.000 | 738 |
| additive_xall | NYIS | mape | -1.084 | 0.278 | 748 |
| additive_xall | PJM | mape | 3.267 | 0.001 | 734 |
| additive_xall | SWPP | mape | -14.178 | 0.000 | 741 |
| additive_xall | TVA | mape | 16.280 | 0.000 | 729 |
| additive_xload | BPAT | mape | 12.646 | 0.000 | 746 |
| additive_xload | CISO | mape | 17.043 | 0.000 | 719 |
| additive_xload | DUK | mape | 10.259 | 0.000 | 746 |
| additive_xload | ERCO | mape | 11.963 | 0.000 | 742 |
| additive_xload | FPL | mape | 17.814 | 0.000 | 665 |
| additive_xload | ISNE | mape | 20.754 | 0.000 | 748 |
| additive_xload | MISO | mape | -3.172 | 0.002 | 738 |
| additive_xload | NYIS | mape | 0.446 | 0.656 | 748 |
| additive_xload | PJM | mape | 5.370 | 0.000 | 734 |
| additive_xload | SWPP | mape | -13.822 | 0.000 | 741 |
| additive_xload | TVA | mape | 17.256 | 0.000 | 729 |
| additive_xtemp | BPAT | mape | 11.555 | 0.000 | 746 |
| additive_xtemp | CISO | mape | 16.665 | 0.000 | 719 |
| additive_xtemp | DUK | mape | 9.520 | 0.000 | 746 |
| additive_xtemp | ERCO | mape | 10.524 | 0.000 | 742 |
| additive_xtemp | FPL | mape | 17.463 | 0.000 | 665 |
| additive_xtemp | ISNE | mape | 19.903 | 0.000 | 748 |
| additive_xtemp | MISO | mape | -3.895 | 0.000 | 738 |
| additive_xtemp | NYIS | mape | -0.387 | 0.699 | 748 |
| additive_xtemp | PJM | mape | 3.899 | 0.000 | 734 |
| additive_xtemp | SWPP | mape | -14.616 | 0.000 | 741 |
| additive_xtemp | TVA | mape | 16.210 | 0.000 | 729 |
| boosting_xall | BPAT | mape | 12.144 | 0.000 | 746 |
| boosting_xall | CISO | mape | 8.674 | 0.000 | 719 |
| boosting_xall | DUK | mape | 9.118 | 0.000 | 746 |
| boosting_xall | ERCO | mape | 5.927 | 0.000 | 742 |
| boosting_xall | FPL | mape | 20.726 | 0.000 | 665 |
| boosting_xall | ISNE | mape | 19.485 | 0.000 | 748 |
| boosting_xall | MISO | mape | -4.766 | 0.000 | 738 |
| boosting_xall | NYIS | mape | 0.149 | 0.882 | 748 |
| boosting_xall | PJM | mape | 4.850 | 0.000 | 734 |
| boosting_xall | SWPP | mape | -12.160 | 0.000 | 741 |
| boosting_xall | TVA | mape | 15.466 | 0.000 | 729 |
| boosting_xload | BPAT | mape | 12.370 | 0.000 | 746 |
| boosting_xload | CISO | mape | 8.554 | 0.000 | 719 |
| boosting_xload | DUK | mape | 9.985 | 0.000 | 746 |
| boosting_xload | ERCO | mape | 6.740 | 0.000 | 742 |
| boosting_xload | FPL | mape | 20.837 | 0.000 | 665 |
| boosting_xload | ISNE | mape | 19.139 | 0.000 | 748 |
| boosting_xload | MISO | mape | -4.422 | 0.000 | 738 |
| boosting_xload | NYIS | mape | 0.166 | 0.868 | 748 |
| boosting_xload | PJM | mape | 5.717 | 0.000 | 734 |
| boosting_xload | SWPP | mape | -12.425 | 0.000 | 741 |
| boosting_xload | TVA | mape | 16.005 | 0.000 | 729 |
| boosting_xsun | BPAT | mape | 12.657 | 0.000 | 746 |
| boosting_xsun | CISO | mape | 8.983 | 0.000 | 719 |
| boosting_xsun | DUK | mape | 10.195 | 0.000 | 746 |
| boosting_xsun | ERCO | mape | 6.806 | 0.000 | 742 |
| boosting_xsun | FPL | mape | 20.956 | 0.000 | 665 |
| boosting_xsun | ISNE | mape | 18.918 | 0.000 | 748 |
| boosting_xsun | MISO | mape | -3.538 | 0.000 | 738 |
| boosting_xsun | NYIS | mape | 0.493 | 0.622 | 748 |
| boosting_xsun | PJM | mape | 6.019 | 0.000 | 734 |
| boosting_xsun | SWPP | mape | -11.363 | 0.000 | 741 |
| boosting_xsun | TVA | mape | 16.137 | 0.000 | 729 |
| boosting_xtemp | BPAT | mape | 12.660 | 0.000 | 746 |
| boosting_xtemp | CISO | mape | 9.129 | 0.000 | 719 |
| boosting_xtemp | DUK | mape | 9.116 | 0.000 | 746 |
| boosting_xtemp | ERCO | mape | 5.846 | 0.000 | 742 |
| boosting_xtemp | FPL | mape | 20.572 | 0.000 | 665 |
| boosting_xtemp | ISNE | mape | 18.865 | 0.000 | 748 |
| boosting_xtemp | MISO | mape | -3.999 | 0.000 | 738 |
| boosting_xtemp | NYIS | mape | 0.104 | 0.917 | 748 |
| boosting_xtemp | PJM | mape | 4.787 | 0.000 | 734 |
| boosting_xtemp | SWPP | mape | -11.830 | 0.000 | 741 |
| boosting_xtemp | TVA | mape | 15.671 | 0.000 | 729 |
| final_additive | BPAT | mape | 12.508 | 0.000 | 746 |
| final_additive | CISO | mape | 17.594 | 0.000 | 719 |
| final_additive | DUK | mape | 10.073 | 0.000 | 746 |
| final_additive | ERCO | mape | 11.907 | 0.000 | 742 |
| final_additive | FPL | mape | 17.131 | 0.000 | 665 |
| final_additive | ISNE | mape | 21.067 | 0.000 | 748 |
| final_additive | MISO | mape | -2.864 | 0.004 | 738 |
| final_additive | NYIS | mape | 0.793 | 0.428 | 748 |
| final_additive | PJM | mape | 5.791 | 0.000 | 734 |
| final_additive | SWPP | mape | -14.285 | 0.000 | 741 |
| final_additive | TVA | mape | 17.029 | 0.000 | 729 |
| final_boosting | BPAT | mape | 12.657 | 0.000 | 746 |
| final_boosting | CISO | mape | 8.983 | 0.000 | 719 |
| final_boosting | DUK | mape | 10.195 | 0.000 | 746 |
| final_boosting | ERCO | mape | 6.806 | 0.000 | 742 |
| final_boosting | FPL | mape | 20.956 | 0.000 | 665 |
| final_boosting | ISNE | mape | 18.918 | 0.000 | 748 |
| final_boosting | MISO | mape | -3.538 | 0.000 | 738 |
| final_boosting | NYIS | mape | 0.493 | 0.622 | 748 |
| final_boosting | PJM | mape | 6.019 | 0.000 | 734 |
| final_boosting | SWPP | mape | -11.363 | 0.000 | 741 |
| final_boosting | TVA | mape | 16.137 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| additive_xall | 0.965 |
| additive_xload | 0.965 |
| additive_xtemp | 0.976 |
| boosting_xall | 0.987 |
| boosting_xload | 0.987 |
| boosting_xsun | 0.987 |
| boosting_xtemp | 0.987 |
| final_additive | 0.976 |
| final_boosting | 0.987 |
