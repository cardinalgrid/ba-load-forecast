# Phase G: feature blocks

Development BAs: BPAT, DUK, MISO, NYIS, PJM, SWPP, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `*_xload` adds the load two and three weeks back and the mean of the same weekday last week; `*_xtemp` adds yesterday's extremes, the heating and cooling degree-hours of the previous 72 hours, the day's range and its temperature at 07:00 and 17:00; `boosting_xsun` gives every BA the sun's elevation; `*_xall` combines them.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| additive_xall | 2.58 | 2.25 | -0.69 | -1.75 | 1.52 | 0.52 | 0.25 | -20.78 | 4453 | 6.00 |
| additive_xtemp | 2.60 | 2.28 | -0.78 | -1.81 | 1.60 | 0.51 | 0.25 | -21.23 | 4453 | 6.00 |
| boosting_xall | 2.63 | 2.31 | -0.34 | -1.54 | 1.64 | 0.49 | 0.26 | -28.20 | 4453 | 6.00 |
| boosting_xtemp | 2.65 | 2.32 | -0.31 | -1.55 | 1.59 | 0.50 | 0.26 | -29.50 | 4453 | 6.00 |
| boosting_xload | 2.66 | 2.34 | -0.31 | -1.55 | 1.60 | 0.50 | 0.26 | -27.93 | 4453 | 6.00 |
| additive_xload | 2.67 | 2.34 | -0.79 | -1.83 | 1.64 | 0.50 | 0.24 | -19.71 | 4453 | 6.00 |
| final_additive | 2.69 | 2.36 | -0.88 | -1.90 | 1.65 | 0.49 | 0.24 | -20.36 | 4453 | 6.00 |
| boosting_xsun | 2.70 | 2.35 | -0.30 | -1.57 | 1.71 | 0.49 | 0.27 | -28.44 | 4453 | 6.00 |
| final_boosting | 2.70 | 2.35 | -0.30 | -1.57 | 1.71 | 0.49 | 0.27 | -28.44 | 4453 | 6.00 |
| DF | 2.72 | 2.45 | 0.62 | -0.92 | 1.02 | 0.00 | 0.00 | -19.98 | 4453 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.06 | 1.80 | 0.20 | -0.95 | 1.45 | -19.35 |  |  | 746 | 6536.52 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.67 | 0.40 | -12.87 |  |  | 748 | 17415.28 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| additive_xall | BPAT | 2.69 | 2.37 | -0.69 | -1.66 | 1.77 | -16.93 | 0.30 | 0.22 | 746 | 6536.52 |
| additive_xall | DUK | 3.52 | 3.15 | -0.58 | -2.30 | 1.39 | -14.98 | 0.35 | 0.26 | 746 | 12143.29 |
| additive_xall | MISO | 2.34 | 2.09 | -1.21 | -1.84 | 1.60 | -8.30 | 0.55 | 0.05 | 738 | 73700.16 |
| additive_xall | NYIS | 2.60 | 2.28 | -0.83 | -1.97 | 0.56 | -15.30 | 0.55 | 0.60 | 748 | 17415.28 |
| additive_xall | PJM | 2.65 | 2.30 | -0.44 | -1.63 | 1.64 | -12.14 | 0.47 | 0.39 | 734 | 92076.14 |
| additive_xall | SWPP | 2.52 | 2.09 | -0.19 | -1.55 | 1.50 | -20.78 | 0.70 | 0.10 | 741 | 31382.01 |
| additive_xload | BPAT | 2.79 | 2.47 | -0.85 | -1.79 | 1.84 | -18.70 | 0.29 | 0.22 | 746 | 6536.52 |
| additive_xload | DUK | 3.58 | 3.19 | -0.61 | -2.35 | 1.35 | -14.69 | 0.36 | 0.25 | 746 | 12143.29 |
| additive_xload | MISO | 2.43 | 2.19 | -1.28 | -1.90 | 1.82 | -8.66 | 0.53 | 0.05 | 738 | 73700.16 |
| additive_xload | NYIS | 2.70 | 2.32 | -0.72 | -1.94 | 0.59 | -13.89 | 0.53 | 0.61 | 748 | 17415.28 |
| additive_xload | PJM | 2.78 | 2.40 | -0.61 | -1.77 | 1.73 | -12.68 | 0.44 | 0.37 | 734 | 92076.14 |
| additive_xload | SWPP | 2.55 | 2.13 | -0.22 | -1.57 | 1.60 | -19.71 | 0.69 | 0.10 | 741 | 31382.01 |
| additive_xtemp | BPAT | 2.70 | 2.37 | -0.73 | -1.68 | 1.81 | -16.75 | 0.31 | 0.22 | 746 | 6536.52 |
| additive_xtemp | DUK | 3.52 | 3.08 | -0.64 | -2.32 | 1.42 | -14.55 | 0.36 | 0.27 | 746 | 12143.29 |
| additive_xtemp | MISO | 2.37 | 2.11 | -1.35 | -1.94 | 1.76 | -9.47 | 0.54 | 0.05 | 738 | 73700.16 |
| additive_xtemp | NYIS | 2.64 | 2.28 | -0.88 | -2.06 | 0.55 | -15.69 | 0.54 | 0.60 | 748 | 17415.28 |
| additive_xtemp | PJM | 2.68 | 2.37 | -0.51 | -1.69 | 1.73 | -11.80 | 0.45 | 0.39 | 734 | 92076.14 |
| additive_xtemp | SWPP | 2.50 | 2.06 | -0.25 | -1.57 | 1.45 | -21.23 | 0.70 | 0.10 | 741 | 31382.01 |
| boosting_xall | BPAT | 2.68 | 2.40 | -0.45 | -1.59 | 2.00 | -18.49 | 0.29 | 0.24 | 746 | 6536.52 |
| boosting_xall | DUK | 3.48 | 3.01 | -0.52 | -2.25 | 1.50 | -17.80 | 0.34 | 0.27 | 746 | 12143.29 |
| boosting_xall | MISO | 2.33 | 2.02 | -0.55 | -1.44 | 1.70 | -10.28 | 0.55 | 0.05 | 738 | 73700.16 |
| boosting_xall | NYIS | 2.68 | 2.35 | -0.38 | -1.51 | 0.79 | -12.12 | 0.51 | 0.69 | 748 | 17415.28 |
| boosting_xall | PJM | 2.74 | 2.49 | 0.07 | -1.39 | 1.78 | -12.01 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xall | SWPP | 2.61 | 2.15 | -0.93 | -1.97 | 1.55 | -28.20 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xload | BPAT | 2.69 | 2.40 | -0.41 | -1.56 | 2.04 | -17.96 | 0.27 | 0.24 | 746 | 6536.52 |
| boosting_xload | DUK | 3.55 | 3.15 | -0.49 | -2.27 | 1.44 | -16.27 | 0.34 | 0.26 | 746 | 12143.29 |
| boosting_xload | MISO | 2.35 | 2.06 | -0.52 | -1.46 | 1.61 | -9.78 | 0.55 | 0.06 | 738 | 73700.16 |
| boosting_xload | NYIS | 2.68 | 2.38 | -0.44 | -1.56 | 0.74 | -14.66 | 0.51 | 0.67 | 748 | 17415.28 |
| boosting_xload | PJM | 2.79 | 2.49 | 0.12 | -1.39 | 1.72 | -12.65 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xload | SWPP | 2.60 | 2.20 | -0.87 | -1.94 | 1.69 | -27.93 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xsun | BPAT | 2.73 | 2.43 | -0.45 | -1.58 | 2.01 | -18.16 | 0.27 | 0.24 | 746 | 6536.52 |
| boosting_xsun | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| boosting_xsun | MISO | 2.41 | 2.07 | -0.51 | -1.44 | 1.81 | -11.84 | 0.54 | 0.06 | 738 | 73700.16 |
| boosting_xsun | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.75 | -14.02 | 0.51 | 0.66 | 748 | 17415.28 |
| boosting_xsun | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xsun | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xtemp | BPAT | 2.73 | 2.45 | -0.49 | -1.62 | 1.94 | -17.98 | 0.28 | 0.24 | 746 | 6536.52 |
| boosting_xtemp | DUK | 3.49 | 3.03 | -0.51 | -2.25 | 1.43 | -17.27 | 0.38 | 0.27 | 746 | 12143.29 |
| boosting_xtemp | MISO | 2.38 | 2.08 | -0.53 | -1.45 | 1.70 | -9.96 | 0.56 | 0.05 | 738 | 73700.16 |
| boosting_xtemp | NYIS | 2.67 | 2.33 | -0.39 | -1.54 | 0.74 | -12.68 | 0.51 | 0.66 | 748 | 17415.28 |
| boosting_xtemp | PJM | 2.73 | 2.47 | 0.10 | -1.39 | 1.64 | -11.49 | 0.43 | 0.41 | 734 | 92076.14 |
| boosting_xtemp | SWPP | 2.66 | 2.16 | -0.85 | -1.94 | 1.62 | -29.50 | 0.67 | 0.08 | 741 | 31382.01 |
| final_additive | BPAT | 2.80 | 2.44 | -0.88 | -1.80 | 1.84 | -18.41 | 0.29 | 0.22 | 746 | 6536.52 |
| final_additive | DUK | 3.56 | 3.15 | -0.71 | -2.39 | 1.42 | -14.75 | 0.34 | 0.27 | 746 | 12143.29 |
| final_additive | MISO | 2.44 | 2.18 | -1.43 | -1.99 | 1.83 | -9.48 | 0.54 | 0.05 | 738 | 73700.16 |
| final_additive | NYIS | 2.72 | 2.37 | -0.87 | -2.09 | 0.60 | -15.67 | 0.51 | 0.59 | 748 | 17415.28 |
| final_additive | PJM | 2.81 | 2.47 | -0.68 | -1.84 | 1.77 | -12.10 | 0.42 | 0.37 | 734 | 92076.14 |
| final_additive | SWPP | 2.53 | 2.11 | -0.28 | -1.59 | 1.49 | -20.36 | 0.70 | 0.10 | 741 | 31382.01 |
| final_boosting | BPAT | 2.73 | 2.43 | -0.45 | -1.58 | 2.01 | -18.16 | 0.27 | 0.24 | 746 | 6536.52 |
| final_boosting | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| final_boosting | MISO | 2.41 | 2.07 | -0.51 | -1.44 | 1.81 | -11.84 | 0.54 | 0.06 | 738 | 73700.16 |
| final_boosting | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.75 | -14.02 | 0.51 | 0.66 | 748 | 17415.28 |
| final_boosting | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| final_boosting | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | uri | 2.77 | -0.21 | -1.69 | -6.97 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| additive_xall | BPAT | uri | 2.81 | -0.35 | -1.21 | -2.29 | 6 |
| additive_xall | DUK | uri | 3.49 | -1.84 | -1.91 | -6.46 | 6 |
| additive_xall | MISO | uri | 3.67 | -2.41 | -3.04 | -6.36 | 5 |
| additive_xall | NYIS | uri | 2.66 | 3.01 | 0.00 | 0.00 | 6 |
| additive_xall | PJM | uri | 3.14 | 3.01 | -0.41 | -2.47 | 6 |
| additive_xall | SWPP | uri | 6.47 | 1.82 | -2.00 | -5.04 | 4 |
| additive_xload | BPAT | uri | 3.07 | -0.01 | -1.08 | -2.31 | 6 |
| additive_xload | DUK | uri | 3.45 | -2.22 | -2.22 | -6.93 | 6 |
| additive_xload | MISO | uri | 3.81 | -3.11 | -3.48 | -6.98 | 5 |
| additive_xload | NYIS | uri | 2.51 | 2.56 | 0.00 | 0.00 | 6 |
| additive_xload | PJM | uri | 3.11 | 2.58 | -0.37 | -2.24 | 6 |
| additive_xload | SWPP | uri | 6.41 | 1.23 | -2.16 | -5.48 | 4 |
| additive_xtemp | BPAT | uri | 2.89 | -0.60 | -1.46 | -2.84 | 6 |
| additive_xtemp | DUK | uri | 3.46 | -2.33 | -2.35 | -7.06 | 6 |
| additive_xtemp | MISO | uri | 3.39 | -1.58 | -2.30 | -4.60 | 5 |
| additive_xtemp | NYIS | uri | 2.33 | 2.45 | 0.00 | 0.00 | 6 |
| additive_xtemp | PJM | uri | 3.00 | 2.79 | -0.47 | -2.80 | 6 |
| additive_xtemp | SWPP | uri | 6.59 | 2.33 | -1.74 | -4.71 | 4 |
| boosting_xall | BPAT | uri | 3.45 | 1.33 | -0.90 | -5.38 | 6 |
| boosting_xall | DUK | uri | 3.73 | -2.45 | -2.62 | -5.37 | 6 |
| boosting_xall | MISO | uri | 3.11 | -2.80 | -2.94 | -5.79 | 5 |
| boosting_xall | NYIS | uri | 2.63 | 0.87 | -0.61 | -3.20 | 6 |
| boosting_xall | PJM | uri | 2.04 | -0.72 | -0.98 | -1.97 | 6 |
| boosting_xall | SWPP | uri | 5.87 | -3.34 | -4.47 | -10.32 | 4 |
| boosting_xload | BPAT | uri | 3.40 | 1.21 | -0.87 | -5.05 | 6 |
| boosting_xload | DUK | uri | 3.57 | -2.86 | -2.93 | -4.81 | 6 |
| boosting_xload | MISO | uri | 3.02 | -3.17 | -3.17 | -5.44 | 5 |
| boosting_xload | NYIS | uri | 2.58 | 0.98 | -0.81 | -2.49 | 6 |
| boosting_xload | PJM | uri | 2.04 | -1.19 | -1.40 | -3.32 | 6 |
| boosting_xload | SWPP | uri | 5.28 | -3.27 | -4.40 | -10.34 | 4 |
| boosting_xsun | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| boosting_xsun | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_xsun | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_xsun | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| boosting_xsun | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_xsun | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_xtemp | BPAT | uri | 3.40 | 0.79 | -0.92 | -5.38 | 6 |
| boosting_xtemp | DUK | uri | 3.60 | -2.52 | -2.58 | -5.65 | 6 |
| boosting_xtemp | MISO | uri | 3.06 | -3.26 | -3.31 | -6.50 | 5 |
| boosting_xtemp | NYIS | uri | 2.36 | 1.14 | -0.42 | -2.50 | 6 |
| boosting_xtemp | PJM | uri | 1.86 | -0.63 | -1.04 | -3.39 | 6 |
| boosting_xtemp | SWPP | uri | 5.79 | -2.74 | -4.18 | -9.79 | 4 |
| final_additive | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| final_additive | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| final_boosting | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| final_boosting | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| final_boosting | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| final_boosting | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| additive_xall | BPAT | elliott | 3.64 | -1.16 | -2.00 | -4.21 | 5 |
| additive_xall | DUK | elliott | 4.58 | -3.41 | -3.41 | -5.07 | 4 |
| additive_xall | MISO | elliott | 3.36 | -3.29 | -3.60 | -7.71 | 5 |
| additive_xall | NYIS | elliott | 3.13 | -0.97 | -2.04 | -4.49 | 5 |
| additive_xall | PJM | elliott | 3.53 | -0.16 | -0.93 | -4.57 | 5 |
| additive_xall | SWPP | elliott | 3.00 | -2.57 | -2.84 | -5.40 | 5 |
| additive_xload | BPAT | elliott | 4.35 | -1.18 | -2.22 | -4.53 | 5 |
| additive_xload | DUK | elliott | 4.26 | -3.35 | -3.35 | -4.89 | 4 |
| additive_xload | MISO | elliott | 3.46 | -3.43 | -3.68 | -6.87 | 5 |
| additive_xload | NYIS | elliott | 3.45 | -2.17 | -2.47 | -5.12 | 5 |
| additive_xload | PJM | elliott | 3.79 | -1.37 | -1.98 | -8.99 | 5 |
| additive_xload | SWPP | elliott | 3.36 | -2.66 | -2.88 | -6.85 | 5 |
| additive_xtemp | BPAT | elliott | 3.73 | -1.41 | -2.26 | -4.53 | 5 |
| additive_xtemp | DUK | elliott | 4.63 | -2.45 | -2.47 | -5.20 | 4 |
| additive_xtemp | MISO | elliott | 3.32 | -2.99 | -3.43 | -6.61 | 5 |
| additive_xtemp | NYIS | elliott | 3.02 | -0.76 | -1.77 | -4.35 | 5 |
| additive_xtemp | PJM | elliott | 3.60 | -0.12 | -0.90 | -4.52 | 5 |
| additive_xtemp | SWPP | elliott | 3.33 | -2.50 | -2.97 | -6.48 | 5 |
| boosting_xall | BPAT | elliott | 4.46 | -4.51 | -4.74 | -11.66 | 5 |
| boosting_xall | DUK | elliott | 4.71 | -2.60 | -2.60 | -5.62 | 4 |
| boosting_xall | MISO | elliott | 3.66 | -1.07 | -2.19 | -3.48 | 5 |
| boosting_xall | NYIS | elliott | 3.11 | 0.19 | -0.87 | -2.78 | 5 |
| boosting_xall | PJM | elliott | 5.27 | -2.75 | -3.77 | -7.24 | 5 |
| boosting_xall | SWPP | elliott | 5.50 | -1.75 | -3.68 | -11.27 | 5 |
| boosting_xload | BPAT | elliott | 4.56 | -5.02 | -5.12 | -12.47 | 5 |
| boosting_xload | DUK | elliott | 4.64 | -3.33 | -3.33 | -6.47 | 4 |
| boosting_xload | MISO | elliott | 3.30 | -1.53 | -2.45 | -4.59 | 5 |
| boosting_xload | NYIS | elliott | 2.87 | -0.76 | -1.65 | -3.86 | 5 |
| boosting_xload | PJM | elliott | 5.09 | -2.53 | -3.43 | -6.72 | 5 |
| boosting_xload | SWPP | elliott | 5.00 | -2.74 | -4.31 | -11.73 | 5 |
| boosting_xsun | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| boosting_xsun | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| boosting_xsun | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| boosting_xsun | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| boosting_xsun | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| boosting_xsun | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| boosting_xtemp | BPAT | elliott | 4.55 | -5.11 | -5.22 | -11.46 | 5 |
| boosting_xtemp | DUK | elliott | 4.65 | -3.11 | -3.11 | -6.79 | 4 |
| boosting_xtemp | MISO | elliott | 3.99 | -0.24 | -1.76 | -3.39 | 5 |
| boosting_xtemp | NYIS | elliott | 3.03 | 0.01 | -1.04 | -4.08 | 5 |
| boosting_xtemp | PJM | elliott | 5.38 | -1.56 | -2.95 | -5.92 | 5 |
| boosting_xtemp | SWPP | elliott | 4.59 | -1.33 | -3.29 | -10.96 | 5 |
| final_additive | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| final_additive | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| final_additive | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| final_additive | NYIS | elliott | 3.27 | -1.91 | -2.37 | -3.71 | 5 |
| final_additive | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| final_additive | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| final_boosting | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| final_boosting | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| final_boosting | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| final_boosting | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| final_boosting | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| final_boosting | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | additive_xall | eve | 3.14 | 0.40 | -1.48 | 0.52 | 148 |
| 12 | additive_xload | eve | 3.19 | 0.11 | -1.59 | 0.49 | 148 |
| 13 | additive_xtemp | eve | 3.23 | 0.50 | -1.49 | 0.53 | 148 |
| 18 | final_additive | eve | 3.25 | 0.13 | -1.65 | 0.49 | 148 |
| 14 | boosting_xall | eve | 3.44 | 0.42 | -1.52 | 0.48 | 148 |
| 10 | DF | eve | 3.47 | 1.06 | -1.12 |  | 148 |
| 17 | boosting_xtemp | eve | 3.52 | 0.46 | -1.56 | 0.49 | 148 |
| 15 | boosting_xload | eve | 3.54 | 0.50 | -1.57 | 0.47 | 148 |
| 16 | boosting_xsun | eve | 3.60 | 0.58 | -1.57 | 0.46 | 148 |
| 19 | final_boosting | eve | 3.60 | 0.58 | -1.57 | 0.46 | 148 |
| 1 | additive_xall | special | 3.02 | -1.29 | -2.32 | 0.56 | 149 |
| 3 | additive_xtemp | special | 3.07 | -1.17 | -2.26 | 0.59 | 149 |
| 2 | additive_xload | special | 3.13 | -1.51 | -2.45 | 0.56 | 149 |
| 8 | final_additive | special | 3.18 | -1.37 | -2.40 | 0.56 | 149 |
| 5 | boosting_xload | special | 3.45 | -0.65 | -2.07 | 0.54 | 149 |
| 4 | boosting_xall | special | 3.49 | -0.63 | -2.05 | 0.56 | 149 |
| 6 | boosting_xsun | special | 3.57 | -0.59 | -2.13 | 0.50 | 149 |
| 9 | final_boosting | special | 3.57 | -0.59 | -2.13 | 0.50 | 149 |
| 7 | boosting_xtemp | special | 3.58 | -0.59 | -2.10 | 0.54 | 149 |
| 0 | DF | special | 3.96 | 0.34 | -1.62 |  | 149 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 14859 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 14854 | DUK | 2022-12-24 | additive_xall | 6.92 | -12.48 | -12.48 |
| 14852 | DUK | 2022-12-24 | additive_xload | 6.45 | -12.81 | -12.81 |
| 14853 | DUK | 2022-12-24 | additive_xtemp | 7.27 | -12.54 | -12.54 |
| 14858 | DUK | 2022-12-24 | boosting_xall | 9.37 | -16.02 | -16.02 |
| 14855 | DUK | 2022-12-24 | boosting_xload | 10.22 | -17.91 | -17.91 |
| 14857 | DUK | 2022-12-24 | boosting_xsun | 9.36 | -15.80 | -15.80 |
| 14856 | DUK | 2022-12-24 | boosting_xtemp | 9.25 | -15.80 | -15.80 |
| 14850 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 14851 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 15689 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 15684 | MISO | 2021-02-16 | additive_xall | 2.33 | 2.19 | 0.00 |
| 15682 | MISO | 2021-02-16 | additive_xload | 2.16 | 1.93 | 0.00 |
| 15683 | MISO | 2021-02-16 | additive_xtemp | 2.58 | 2.31 | 0.00 |
| 15688 | MISO | 2021-02-16 | boosting_xall | 2.22 | 0.36 | 0.00 |
| 15685 | MISO | 2021-02-16 | boosting_xload | 1.99 | -0.79 | -0.79 |
| 15687 | MISO | 2021-02-16 | boosting_xsun | 2.11 | 0.99 | 0.00 |
| 15686 | MISO | 2021-02-16 | boosting_xtemp | 2.65 | 1.84 | 0.00 |
| 15680 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 15681 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 37889 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 37884 | SWPP | 2021-02-15 | additive_xall | 2.38 | 1.40 | 0.00 |
| 37882 | SWPP | 2021-02-15 | additive_xload | 2.31 | 1.02 | 0.00 |
| 37883 | SWPP | 2021-02-15 | additive_xtemp | 2.77 | 1.43 | 0.00 |
| 37888 | SWPP | 2021-02-15 | boosting_xall | 6.26 | -8.32 | -8.32 |
| 37885 | SWPP | 2021-02-15 | boosting_xload | 6.27 | -8.52 | -8.52 |
| 37887 | SWPP | 2021-02-15 | boosting_xsun | 5.58 | -7.79 | -7.79 |
| 37886 | SWPP | 2021-02-15 | boosting_xtemp | 6.09 | -8.25 | -8.25 |
| 37880 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 37881 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 37899 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 37894 | SWPP | 2021-02-16 | additive_xall | 7.58 | 3.67 | 0.00 |
| 37892 | SWPP | 2021-02-16 | additive_xload | 7.54 | 3.32 | 0.00 |
| 37893 | SWPP | 2021-02-16 | additive_xtemp | 8.04 | 3.60 | 0.00 |
| 37898 | SWPP | 2021-02-16 | boosting_xall | 3.17 | -5.46 | -5.46 |
| 37895 | SWPP | 2021-02-16 | boosting_xload | 3.36 | -5.76 | -5.76 |
| 37897 | SWPP | 2021-02-16 | boosting_xsun | 3.72 | -6.44 | -6.44 |
| 37896 | SWPP | 2021-02-16 | boosting_xtemp | 3.40 | -6.73 | -6.73 |
| 37890 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 37891 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_xall | BPAT | mape | 11.482 | 0.000 | 746 |
| additive_xall | DUK | mape | 9.584 | 0.000 | 746 |
| additive_xall | MISO | mape | -4.388 | 0.000 | 738 |
| additive_xall | NYIS | mape | -1.084 | 0.278 | 748 |
| additive_xall | PJM | mape | 3.267 | 0.001 | 734 |
| additive_xall | SWPP | mape | -14.178 | 0.000 | 741 |
| additive_xload | BPAT | mape | 12.646 | 0.000 | 746 |
| additive_xload | DUK | mape | 10.259 | 0.000 | 746 |
| additive_xload | MISO | mape | -3.172 | 0.002 | 738 |
| additive_xload | NYIS | mape | 0.446 | 0.656 | 748 |
| additive_xload | PJM | mape | 5.370 | 0.000 | 734 |
| additive_xload | SWPP | mape | -13.822 | 0.000 | 741 |
| additive_xtemp | BPAT | mape | 11.555 | 0.000 | 746 |
| additive_xtemp | DUK | mape | 9.520 | 0.000 | 746 |
| additive_xtemp | MISO | mape | -3.895 | 0.000 | 738 |
| additive_xtemp | NYIS | mape | -0.387 | 0.699 | 748 |
| additive_xtemp | PJM | mape | 3.899 | 0.000 | 734 |
| additive_xtemp | SWPP | mape | -14.616 | 0.000 | 741 |
| boosting_xall | BPAT | mape | 12.144 | 0.000 | 746 |
| boosting_xall | DUK | mape | 9.118 | 0.000 | 746 |
| boosting_xall | MISO | mape | -4.766 | 0.000 | 738 |
| boosting_xall | NYIS | mape | 0.149 | 0.882 | 748 |
| boosting_xall | PJM | mape | 4.850 | 0.000 | 734 |
| boosting_xall | SWPP | mape | -12.160 | 0.000 | 741 |
| boosting_xload | BPAT | mape | 12.370 | 0.000 | 746 |
| boosting_xload | DUK | mape | 9.985 | 0.000 | 746 |
| boosting_xload | MISO | mape | -4.422 | 0.000 | 738 |
| boosting_xload | NYIS | mape | 0.166 | 0.868 | 748 |
| boosting_xload | PJM | mape | 5.717 | 0.000 | 734 |
| boosting_xload | SWPP | mape | -12.425 | 0.000 | 741 |
| boosting_xsun | BPAT | mape | 12.657 | 0.000 | 746 |
| boosting_xsun | DUK | mape | 10.195 | 0.000 | 746 |
| boosting_xsun | MISO | mape | -3.538 | 0.000 | 738 |
| boosting_xsun | NYIS | mape | 0.493 | 0.622 | 748 |
| boosting_xsun | PJM | mape | 6.019 | 0.000 | 734 |
| boosting_xsun | SWPP | mape | -11.363 | 0.000 | 741 |
| boosting_xtemp | BPAT | mape | 12.660 | 0.000 | 746 |
| boosting_xtemp | DUK | mape | 9.116 | 0.000 | 746 |
| boosting_xtemp | MISO | mape | -3.999 | 0.000 | 738 |
| boosting_xtemp | NYIS | mape | 0.104 | 0.917 | 748 |
| boosting_xtemp | PJM | mape | 4.787 | 0.000 | 734 |
| boosting_xtemp | SWPP | mape | -11.830 | 0.000 | 741 |
| final_additive | BPAT | mape | 12.508 | 0.000 | 746 |
| final_additive | DUK | mape | 10.073 | 0.000 | 746 |
| final_additive | MISO | mape | -2.864 | 0.004 | 738 |
| final_additive | NYIS | mape | 0.793 | 0.428 | 748 |
| final_additive | PJM | mape | 5.791 | 0.000 | 734 |
| final_additive | SWPP | mape | -14.285 | 0.000 | 741 |
| final_boosting | BPAT | mape | 12.657 | 0.000 | 746 |
| final_boosting | DUK | mape | 10.195 | 0.000 | 746 |
| final_boosting | MISO | mape | -3.538 | 0.000 | 738 |
| final_boosting | NYIS | mape | 0.493 | 0.622 | 748 |
| final_boosting | PJM | mape | 6.019 | 0.000 | 734 |
| final_boosting | SWPP | mape | -11.363 | 0.000 | 741 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.996 |
| additive_xall | 0.977 |
| additive_xload | 0.977 |
| additive_xtemp | 0.985 |
| boosting_xall | 0.992 |
| boosting_xload | 0.992 |
| boosting_xsun | 0.992 |
| boosting_xtemp | 0.992 |
| final_additive | 0.985 |
| final_boosting | 0.992 |
