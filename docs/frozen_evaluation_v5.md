# Fifth look at 2023 to 2025: the recipe after phase K, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase K (`final6`) on 2023 to 2025 under protocol v2, with the observed-temperature supplement. A fifth look at these years: compare with `docs/frozen_evaluation_v4.md` (same days, same rules) and read the difference as an estimate.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6 | 2.22 | 1.91 | -0.02 | -1.19 | 1.13 | 0.63 | 0.30 | -38.91 | 11679 | 11.00 |
| final6_ensemble | 2.42 | 2.13 | -1.63 | -2.18 | 1.13 | 0.58 | 0.20 | -40.71 | 11679 | 11.00 |
| final6_boosting | 2.49 | 2.19 | -1.51 | -2.14 | 1.29 | 0.55 | 0.21 | -41.40 | 11679 | 11.00 |
| final6_additive | 2.65 | 2.35 | -1.66 | -2.36 | 1.18 | 0.53 | 0.20 | -39.90 | 11679 | 11.00 |
| DF | 2.90 | 2.50 | 0.31 | -1.10 | 0.98 | 0.00 | 0.00 | -41.79 | 11679 | 11.00 |
| final6_recency | 3.23 | 2.91 | -1.79 | -2.57 | 1.47 | 0.41 | 0.18 | -40.90 | 11679 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.00 | 1.80 | -0.38 | -1.20 | 1.24 | -15.51 |  |  | 1081 | 6762.61 |
| DF | CISO | 5.36 | 5.12 | -1.74 | -2.63 | 1.20 | -33.79 |  |  | 1044 | 25453.81 |
| DF | DUK | 2.65 | 2.31 | 0.43 | -1.26 | 1.02 | -13.08 |  |  | 1070 | 12295.77 |
| DF | ERCO | 2.40 | 1.99 | 0.79 | -0.80 | 1.01 | -11.36 |  |  | 1071 | 53336.07 |
| DF | FPL | 3.21 | 3.06 | -0.60 | -1.71 | 1.12 | -41.79 |  |  | 1003 | 16583.18 |
| DF | ISNE | 2.56 | 2.51 | 0.40 | -0.45 | 0.33 | -5.42 |  |  | 1069 | 12999.48 |
| DF | MISO | 2.72 | 2.51 | 2.03 | -0.22 | 0.85 | -6.54 |  |  | 1084 | 74014.33 |
| DF | NYIS | 2.62 | 2.46 | -2.44 | -2.59 | 0.43 | -10.12 |  |  | 1058 | 17111.01 |
| DF | PJM | 2.40 | 2.17 | -0.54 | -1.17 | 0.95 | -7.65 |  |  | 1057 | 93208.59 |
| DF | SWPP | 4.33 | 2.46 | 1.42 | -1.38 | 1.49 | -17.10 |  |  | 1066 | 33074.81 |
| DF | TVA | 2.28 | 1.96 | 0.57 | -0.89 | 1.00 | -8.44 |  |  | 1076 | 18806.27 |
| final6 | BPAT | 2.11 | 1.89 | -0.13 | -1.17 | 1.35 | -16.32 | 0.47 | 0.39 | 1081 | 6762.61 |
| final6 | CISO | 2.63 | 2.40 | -0.30 | -1.46 | 1.08 | -16.36 | 0.90 | 0.40 | 1044 | 25453.81 |
| final6 | DUK | 2.84 | 2.36 | 0.40 | -1.50 | 1.19 | -12.45 | 0.46 | 0.27 | 1070 | 12295.77 |
| final6 | ERCO | 2.22 | 1.86 | 0.01 | -1.24 | 0.87 | -16.59 | 0.55 | 0.22 | 1071 | 53336.07 |
| final6 | FPL | 3.11 | 2.72 | 0.54 | -1.38 | 0.95 | -38.91 | 0.60 | 0.42 | 1003 | 16583.18 |
| final6 | ISNE | 3.59 | 3.20 | 0.04 | -1.28 | 0.51 | -21.77 | 0.31 | 0.19 | 1069 | 12999.48 |
| final6 | MISO | 1.74 | 1.53 | 0.02 | -0.90 | 1.36 | -6.66 | 0.74 | 0.08 | 1084 | 74014.33 |
| final6 | NYIS | 2.50 | 2.19 | -0.05 | -1.18 | 0.59 | -18.74 | 0.53 | 0.75 | 1058 | 17111.01 |
| final6 | PJM | 1.93 | 1.67 | -0.08 | -1.12 | 1.12 | -9.43 | 0.67 | 0.41 | 1057 | 93208.59 |
| final6 | SWPP | 2.32 | 1.79 | -0.24 | -1.35 | 1.56 | -22.65 | 0.62 | 0.35 | 1066 | 33074.81 |
| final6 | TVA | 2.44 | 2.07 | 0.00 | -1.36 | 1.23 | -12.21 | 0.43 | 0.20 | 1076 | 18806.27 |
| final6_additive | BPAT | 2.33 | 2.05 | -1.76 | -2.23 | 1.36 | -16.98 | 0.40 | 0.25 | 1081 | 6762.61 |
| final6_additive | CISO | 3.32 | 3.04 | -2.35 | -3.01 | 1.14 | -20.95 | 0.82 | 0.29 | 1044 | 25453.81 |
| final6_additive | DUK | 3.07 | 2.65 | -1.71 | -2.78 | 1.27 | -15.45 | 0.40 | 0.15 | 1070 | 12295.77 |
| final6_additive | ERCO | 3.10 | 2.82 | -2.47 | -3.03 | 0.92 | -18.71 | 0.34 | 0.10 | 1071 | 53336.07 |
| final6_additive | FPL | 4.05 | 3.70 | -3.40 | -4.11 | 0.97 | -39.90 | 0.40 | 0.14 | 1003 | 16583.18 |
| final6_additive | ISNE | 3.91 | 3.45 | -1.24 | -2.29 | 0.58 | -19.70 | 0.28 | 0.14 | 1069 | 12999.48 |
| final6_additive | MISO | 2.03 | 1.87 | -1.22 | -1.78 | 1.44 | -9.40 | 0.64 | 0.04 | 1084 | 74014.33 |
| final6_additive | NYIS | 2.78 | 2.45 | -1.45 | -2.15 | 0.60 | -17.38 | 0.48 | 0.58 | 1058 | 17111.01 |
| final6_additive | PJM | 2.25 | 1.95 | -1.11 | -1.89 | 1.20 | -11.55 | 0.58 | 0.30 | 1057 | 93208.59 |
| final6_additive | SWPP | 2.59 | 2.12 | -2.14 | -2.66 | 1.62 | -23.12 | 0.54 | 0.20 | 1066 | 33074.81 |
| final6_additive | TVA | 2.72 | 2.32 | -0.98 | -2.12 | 1.12 | -11.50 | 0.37 | 0.15 | 1076 | 18806.27 |
| final6_boosting | BPAT | 2.28 | 2.02 | -1.32 | -1.99 | 1.61 | -17.87 | 0.40 | 0.30 | 1081 | 6762.61 |
| final6_boosting | CISO | 2.86 | 2.59 | -1.76 | -2.35 | 1.10 | -16.09 | 0.85 | 0.33 | 1044 | 25453.81 |
| final6_boosting | DUK | 2.98 | 2.55 | -1.76 | -2.70 | 1.26 | -14.51 | 0.41 | 0.16 | 1070 | 12295.77 |
| final6_boosting | ERCO | 2.62 | 2.32 | -2.30 | -2.75 | 1.12 | -16.04 | 0.43 | 0.09 | 1071 | 53336.07 |
| final6_boosting | FPL | 3.98 | 3.68 | -4.13 | -4.47 | 1.23 | -41.40 | 0.35 | 0.09 | 1003 | 16583.18 |
| final6_boosting | ISNE | 3.65 | 3.17 | -0.96 | -1.80 | 0.57 | -14.33 | 0.30 | 0.14 | 1069 | 12999.48 |
| final6_boosting | MISO | 1.89 | 1.70 | -1.12 | -1.62 | 1.37 | -10.33 | 0.69 | 0.04 | 1084 | 74014.33 |
| final6_boosting | NYIS | 2.59 | 2.26 | -0.90 | -1.60 | 0.69 | -18.89 | 0.52 | 0.69 | 1058 | 17111.01 |
| final6_boosting | PJM | 2.20 | 1.96 | -1.04 | -1.75 | 1.41 | -10.71 | 0.58 | 0.32 | 1057 | 93208.59 |
| final6_boosting | SWPP | 2.70 | 2.09 | -1.66 | -2.38 | 1.75 | -22.68 | 0.54 | 0.24 | 1066 | 33074.81 |
| final6_boosting | TVA | 2.63 | 2.28 | -0.99 | -2.02 | 1.28 | -12.62 | 0.36 | 0.15 | 1076 | 18806.27 |
| final6_ensemble | BPAT | 2.18 | 1.92 | -1.78 | -2.18 | 1.33 | -16.94 | 0.45 | 0.26 | 1081 | 6762.61 |
| final6_ensemble | CISO | 2.99 | 2.70 | -2.09 | -2.66 | 1.28 | -17.63 | 0.86 | 0.31 | 1044 | 25453.81 |
| final6_ensemble | DUK | 2.84 | 2.43 | -1.64 | -2.61 | 1.15 | -14.24 | 0.45 | 0.15 | 1070 | 12295.77 |
| final6_ensemble | ERCO | 2.71 | 2.43 | -2.48 | -2.85 | 0.84 | -17.43 | 0.40 | 0.08 | 1071 | 53336.07 |
| final6_ensemble | FPL | 3.85 | 3.60 | -3.92 | -4.33 | 0.91 | -40.71 | 0.41 | 0.11 | 1003 | 16583.18 |
| final6_ensemble | ISNE | 3.71 | 3.30 | -1.41 | -2.11 | 0.53 | -18.46 | 0.29 | 0.11 | 1069 | 12999.48 |
| final6_ensemble | MISO | 1.87 | 1.70 | -1.21 | -1.64 | 1.31 | -9.26 | 0.69 | 0.05 | 1084 | 74014.33 |
| final6_ensemble | NYIS | 2.59 | 2.31 | -1.30 | -1.87 | 0.65 | -16.67 | 0.52 | 0.64 | 1058 | 17111.01 |
| final6_ensemble | PJM | 2.04 | 1.79 | -1.04 | -1.68 | 1.16 | -10.03 | 0.66 | 0.30 | 1057 | 93208.59 |
| final6_ensemble | SWPP | 2.40 | 1.87 | -1.96 | -2.44 | 1.51 | -22.94 | 0.59 | 0.22 | 1066 | 33074.81 |
| final6_ensemble | TVA | 2.47 | 2.05 | -0.87 | -1.85 | 1.12 | -11.54 | 0.44 | 0.16 | 1076 | 18806.27 |
| final6_recency | BPAT | 2.79 | 2.46 | -2.42 | -2.75 | 1.52 | -15.86 | 0.30 | 0.21 | 1081 | 6762.61 |
| final6_recency | CISO | 4.59 | 4.36 | -2.37 | -3.30 | 1.64 | -22.01 | 0.63 | 0.30 | 1044 | 25453.81 |
| final6_recency | DUK | 3.47 | 3.07 | -1.43 | -2.77 | 1.35 | -16.77 | 0.33 | 0.17 | 1070 | 12295.77 |
| final6_recency | ERCO | 3.28 | 2.92 | -2.80 | -3.29 | 1.07 | -19.74 | 0.31 | 0.08 | 1071 | 53336.07 |
| final6_recency | FPL | 4.95 | 4.57 | -4.44 | -5.06 | 1.09 | -40.90 | 0.23 | 0.11 | 1003 | 16583.18 |
| final6_recency | ISNE | 6.02 | 5.51 | -2.46 | -3.09 | 0.76 | -23.93 | 0.04 | 0.10 | 1069 | 12999.48 |
| final6_recency | MISO | 2.54 | 2.29 | -1.31 | -1.89 | 1.79 | -11.11 | 0.54 | 0.05 | 1084 | 74014.33 |
| final6_recency | NYIS | 4.14 | 3.82 | -1.77 | -2.64 | 0.91 | -13.29 | 0.24 | 0.49 | 1058 | 17111.01 |
| final6_recency | PJM | 2.70 | 2.48 | -0.98 | -1.97 | 1.61 | -10.45 | 0.42 | 0.29 | 1057 | 93208.59 |
| final6_recency | SWPP | 2.90 | 2.31 | -2.17 | -2.81 | 1.71 | -23.02 | 0.50 | 0.19 | 1066 | 33074.81 |
| final6_recency | TVA | 3.03 | 2.57 | -0.61 | -1.95 | 1.43 | -13.32 | 0.29 | 0.17 | 1076 | 18806.27 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | gerri_heather | 3.76 | 0.98 | -1.48 | -3.76 | 6 |
| DF | CISO | gerri_heather | 4.87 | 0.22 | -0.77 | -2.41 | 6 |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | ERCO | gerri_heather | 4.26 | 1.90 | -1.57 | -9.43 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | NYIS | gerri_heather | 3.41 | -2.81 | -2.81 | -3.64 | 5 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| DF | TVA | gerri_heather | 3.50 | 2.67 | -0.73 | -4.40 | 6 |
| final6 | BPAT | gerri_heather | 3.82 | -3.09 | -3.34 | -8.99 | 6 |
| final6 | CISO | gerri_heather | 2.60 | 0.77 | -0.48 | -2.36 | 6 |
| final6 | DUK | gerri_heather | 5.17 | -5.03 | -5.03 | -8.22 | 6 |
| final6 | ERCO | gerri_heather | 6.30 | -6.72 | -6.72 | -11.12 | 6 |
| final6 | FPL | gerri_heather | 4.79 | -5.26 | -6.11 | -10.11 | 6 |
| final6 | ISNE | gerri_heather | 3.36 | -0.04 | -0.98 | -3.97 | 6 |
| final6 | MISO | gerri_heather | 2.77 | -1.92 | -2.17 | -4.40 | 6 |
| final6 | NYIS | gerri_heather | 1.85 | 0.59 | -0.25 | -0.90 | 5 |
| final6 | PJM | gerri_heather | 2.70 | -0.32 | -1.09 | -3.87 | 6 |
| final6 | SWPP | gerri_heather | 5.69 | -5.62 | -5.62 | -13.93 | 6 |
| final6 | TVA | gerri_heather | 2.70 | 0.10 | -1.04 | -3.84 | 6 |
| final6_additive | BPAT | gerri_heather | 5.07 | -4.94 | -5.05 | -10.36 | 6 |
| final6_additive | CISO | gerri_heather | 2.85 | 1.24 | -0.51 | -1.77 | 6 |
| final6_additive | DUK | gerri_heather | 5.77 | -7.70 | -7.70 | -15.45 | 6 |
| final6_additive | ERCO | gerri_heather | 8.01 | -10.19 | -10.19 | -15.45 | 6 |
| final6_additive | FPL | gerri_heather | 6.32 | -7.54 | -7.54 | -12.70 | 6 |
| final6_additive | ISNE | gerri_heather | 3.86 | -0.69 | -1.99 | -5.62 | 6 |
| final6_additive | MISO | gerri_heather | 2.94 | -3.01 | -3.01 | -4.83 | 6 |
| final6_additive | NYIS | gerri_heather | 2.24 | -1.89 | -2.06 | -3.53 | 5 |
| final6_additive | PJM | gerri_heather | 2.51 | -0.10 | -0.83 | -2.76 | 6 |
| final6_additive | SWPP | gerri_heather | 7.00 | -8.28 | -8.28 | -18.01 | 6 |
| final6_additive | TVA | gerri_heather | 3.02 | -0.48 | -1.93 | -5.89 | 6 |
| final6_boosting | BPAT | gerri_heather | 5.78 | -7.36 | -7.36 | -13.85 | 6 |
| final6_boosting | CISO | gerri_heather | 2.60 | 0.85 | -0.61 | -3.53 | 6 |
| final6_boosting | DUK | gerri_heather | 5.20 | -6.42 | -6.42 | -11.77 | 6 |
| final6_boosting | ERCO | gerri_heather | 7.20 | -10.14 | -10.14 | -16.04 | 6 |
| final6_boosting | FPL | gerri_heather | 5.06 | -6.02 | -7.00 | -12.62 | 6 |
| final6_boosting | ISNE | gerri_heather | 3.50 | -0.53 | -1.42 | -4.73 | 6 |
| final6_boosting | MISO | gerri_heather | 2.90 | -3.31 | -3.58 | -6.38 | 6 |
| final6_boosting | NYIS | gerri_heather | 2.08 | 0.91 | -0.17 | -0.63 | 5 |
| final6_boosting | PJM | gerri_heather | 2.75 | -1.32 | -2.24 | -4.19 | 6 |
| final6_boosting | SWPP | gerri_heather | 6.32 | -7.45 | -7.45 | -14.25 | 6 |
| final6_boosting | TVA | gerri_heather | 3.33 | -3.23 | -4.10 | -10.20 | 6 |
| final6_ensemble | BPAT | gerri_heather | 4.74 | -5.24 | -5.24 | -11.04 | 6 |
| final6_ensemble | CISO | gerri_heather | 2.55 | 0.96 | -0.56 | -3.35 | 6 |
| final6_ensemble | DUK | gerri_heather | 5.53 | -7.53 | -7.53 | -14.24 | 6 |
| final6_ensemble | ERCO | gerri_heather | 7.14 | -9.20 | -9.20 | -13.12 | 6 |
| final6_ensemble | FPL | gerri_heather | 5.78 | -7.37 | -7.37 | -12.39 | 6 |
| final6_ensemble | ISNE | gerri_heather | 3.77 | -0.75 | -1.72 | -5.51 | 6 |
| final6_ensemble | MISO | gerri_heather | 2.85 | -3.12 | -3.23 | -5.71 | 6 |
| final6_ensemble | NYIS | gerri_heather | 2.14 | -0.69 | -1.03 | -1.96 | 5 |
| final6_ensemble | PJM | gerri_heather | 2.43 | -0.67 | -1.45 | -3.87 | 6 |
| final6_ensemble | SWPP | gerri_heather | 7.12 | -8.32 | -8.32 | -16.43 | 6 |
| final6_ensemble | TVA | gerri_heather | 2.41 | -1.01 | -1.79 | -4.44 | 6 |
| final6_recency | BPAT | gerri_heather | 4.26 | -3.00 | -3.55 | -8.79 | 6 |
| final6_recency | CISO | gerri_heather | 3.47 | 0.81 | -0.80 | -4.79 | 6 |
| final6_recency | DUK | gerri_heather | 6.40 | -8.59 | -8.59 | -15.68 | 6 |
| final6_recency | ERCO | gerri_heather | 6.80 | -7.02 | -7.03 | -14.20 | 6 |
| final6_recency | FPL | gerri_heather | 6.80 | -8.44 | -8.44 | -13.72 | 6 |
| final6_recency | ISNE | gerri_heather | 5.36 | -1.12 | -2.01 | -6.43 | 6 |
| final6_recency | MISO | gerri_heather | 3.56 | -2.98 | -3.13 | -7.06 | 6 |
| final6_recency | NYIS | gerri_heather | 3.81 | -1.55 | -1.55 | -3.20 | 5 |
| final6_recency | PJM | gerri_heather | 3.19 | -0.53 | -1.80 | -4.90 | 6 |
| final6_recency | SWPP | gerri_heather | 8.47 | -9.32 | -9.32 | -17.09 | 6 |
| final6_recency | TVA | gerri_heather | 4.00 | 1.25 | -1.23 | -6.25 | 6 |
| DF | BPAT | january_2025 | 2.46 | -0.63 | -1.13 | -5.68 | 6 |
| DF | CISO | january_2025 | 6.30 | -4.14 | -4.14 | -7.74 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | ERCO | january_2025 | 3.99 | 0.33 | -0.83 | -2.52 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | NYIS | january_2025 | 3.90 | -3.63 | -3.63 | -4.31 | 5 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| DF | TVA | january_2025 | 2.96 | 1.69 | -0.29 | -1.52 | 6 |
| final6 | BPAT | january_2025 | 2.10 | -2.13 | -2.56 | -4.18 | 6 |
| final6 | CISO | january_2025 | 2.01 | 1.74 | 0.00 | 0.00 | 6 |
| final6 | DUK | january_2025 | 3.84 | 2.25 | -1.06 | -4.75 | 6 |
| final6 | ERCO | january_2025 | 2.66 | -2.91 | -2.91 | -6.54 | 6 |
| final6 | FPL | january_2025 | 6.79 | -7.27 | -7.27 | -13.17 | 6 |
| final6 | ISNE | january_2025 | 3.85 | 0.65 | -0.54 | -1.79 | 6 |
| final6 | MISO | january_2025 | 2.47 | -2.14 | -2.14 | -3.47 | 6 |
| final6 | NYIS | january_2025 | 2.04 | 2.09 | 0.00 | 0.00 | 5 |
| final6 | PJM | january_2025 | 1.84 | -0.90 | -1.40 | -3.70 | 6 |
| final6 | SWPP | january_2025 | 2.50 | -2.18 | -2.18 | -2.99 | 6 |
| final6 | TVA | january_2025 | 3.33 | -0.91 | -1.63 | -4.60 | 6 |
| final6_additive | BPAT | january_2025 | 2.74 | -3.46 | -3.77 | -5.12 | 6 |
| final6_additive | CISO | january_2025 | 2.89 | 1.09 | -0.18 | -0.91 | 6 |
| final6_additive | DUK | january_2025 | 3.70 | 0.74 | -0.84 | -5.03 | 6 |
| final6_additive | ERCO | january_2025 | 3.45 | -3.84 | -3.87 | -7.13 | 6 |
| final6_additive | FPL | january_2025 | 5.59 | -5.68 | -5.68 | -10.34 | 6 |
| final6_additive | ISNE | january_2025 | 3.57 | -0.86 | -1.43 | -3.80 | 6 |
| final6_additive | MISO | january_2025 | 2.86 | -2.74 | -2.74 | -4.75 | 6 |
| final6_additive | NYIS | january_2025 | 1.88 | -1.25 | -1.59 | -3.22 | 5 |
| final6_additive | PJM | january_2025 | 2.26 | -0.26 | -0.85 | -1.96 | 6 |
| final6_additive | SWPP | january_2025 | 3.51 | -3.70 | -3.70 | -6.06 | 6 |
| final6_additive | TVA | january_2025 | 4.06 | -2.53 | -3.10 | -7.01 | 6 |
| final6_boosting | BPAT | january_2025 | 3.24 | -6.16 | -6.16 | -9.13 | 6 |
| final6_boosting | CISO | january_2025 | 2.07 | -0.23 | -0.78 | -2.58 | 6 |
| final6_boosting | DUK | january_2025 | 3.50 | -2.76 | -2.79 | -8.41 | 6 |
| final6_boosting | ERCO | january_2025 | 3.28 | -5.78 | -5.78 | -8.22 | 6 |
| final6_boosting | FPL | january_2025 | 5.85 | -8.56 | -8.56 | -15.42 | 6 |
| final6_boosting | ISNE | january_2025 | 4.41 | -0.93 | -1.94 | -4.98 | 6 |
| final6_boosting | MISO | january_2025 | 2.87 | -4.05 | -4.05 | -5.81 | 6 |
| final6_boosting | NYIS | january_2025 | 1.92 | -0.17 | -0.89 | -2.13 | 5 |
| final6_boosting | PJM | january_2025 | 2.81 | -4.74 | -4.74 | -9.19 | 6 |
| final6_boosting | SWPP | january_2025 | 4.38 | -8.40 | -8.40 | -10.73 | 6 |
| final6_boosting | TVA | january_2025 | 3.37 | -4.22 | -4.22 | -6.67 | 6 |
| final6_ensemble | BPAT | january_2025 | 2.98 | -5.31 | -5.31 | -7.43 | 6 |
| final6_ensemble | CISO | january_2025 | 2.59 | 0.23 | -0.81 | -2.19 | 6 |
| final6_ensemble | DUK | january_2025 | 3.48 | -0.76 | -1.72 | -7.67 | 6 |
| final6_ensemble | ERCO | january_2025 | 3.15 | -5.39 | -5.39 | -7.31 | 6 |
| final6_ensemble | FPL | january_2025 | 5.48 | -7.27 | -7.27 | -12.79 | 6 |
| final6_ensemble | ISNE | january_2025 | 3.29 | -0.87 | -1.43 | -3.79 | 6 |
| final6_ensemble | MISO | january_2025 | 2.80 | -3.68 | -3.68 | -4.94 | 6 |
| final6_ensemble | NYIS | january_2025 | 1.28 | -0.73 | -1.04 | -1.55 | 5 |
| final6_ensemble | PJM | january_2025 | 2.33 | -2.77 | -2.77 | -5.01 | 6 |
| final6_ensemble | SWPP | january_2025 | 4.06 | -5.74 | -5.74 | -6.07 | 6 |
| final6_ensemble | TVA | january_2025 | 3.17 | -3.32 | -3.32 | -5.55 | 6 |
| final6_recency | BPAT | january_2025 | 3.26 | -6.27 | -6.27 | -8.07 | 6 |
| final6_recency | CISO | january_2025 | 4.99 | -0.36 | -3.00 | -5.59 | 6 |
| final6_recency | DUK | january_2025 | 4.24 | -0.27 | -2.06 | -9.58 | 6 |
| final6_recency | ERCO | january_2025 | 3.99 | -6.84 | -6.84 | -7.49 | 6 |
| final6_recency | FPL | january_2025 | 6.20 | -7.46 | -7.46 | -12.18 | 6 |
| final6_recency | ISNE | january_2025 | 4.15 | -0.78 | -1.44 | -4.55 | 6 |
| final6_recency | MISO | january_2025 | 3.62 | -4.31 | -4.31 | -5.73 | 6 |
| final6_recency | NYIS | january_2025 | 3.39 | -1.06 | -1.40 | -3.76 | 5 |
| final6_recency | PJM | january_2025 | 3.13 | -3.18 | -3.18 | -5.90 | 6 |
| final6_recency | SWPP | january_2025 | 4.71 | -5.37 | -5.37 | -8.46 | 6 |
| final6_recency | TVA | january_2025 | 3.21 | -3.10 | -3.26 | -4.73 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6_ensemble | eve | 2.77 | -0.83 | -1.92 | 0.56 | 322 |
| 7 | final6 | eve | 2.85 | 0.73 | -1.27 | 0.51 | 322 |
| 8 | final6_additive | eve | 2.89 | -0.84 | -2.12 | 0.52 | 322 |
| 9 | final6_boosting | eve | 2.95 | -0.72 | -1.89 | 0.52 | 322 |
| 6 | DF | eve | 3.30 | 0.52 | -1.35 |  | 322 |
| 11 | final6_recency | eve | 3.73 | -1.10 | -2.36 | 0.39 | 322 |
| 1 | final6 | special | 3.16 | -0.28 | -1.94 | 0.54 | 336 |
| 4 | final6_ensemble | special | 3.25 | -1.77 | -2.80 | 0.52 | 336 |
| 2 | final6_additive | special | 3.32 | -2.00 | -3.09 | 0.50 | 336 |
| 3 | final6_boosting | special | 3.38 | -1.60 | -2.68 | 0.48 | 336 |
| 0 | DF | special | 3.56 | 0.06 | -1.69 |  | 336 |
| 5 | final6_recency | special | 4.18 | -1.83 | -3.14 | 0.38 | 336 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6 | all | 0.368 | 1.246 | 0.362 | 0.892 | 10.798 | 0.901 | 14.604 | 1.614 | 11446 |
| final6 | events | 0.406 | 1.720 | 0.653 | 0.819 | 12.108 | 0.792 | 21.169 | 2.287 | 130 |
| final6 | cold_mornings | 0.416 | 1.542 | 0.559 | 0.847 | 12.249 | 0.873 | 19.494 | 2.033 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6 | BPAT | mape | 2.807 | 0.005 | 1081 |
| final6 | CISO | mape | -37.352 | 0.000 | 1044 |
| final6 | DUK | mape | 3.934 | 0.000 | 1070 |
| final6 | ERCO | mape | -4.146 | 0.000 | 1071 |
| final6 | FPL | mape | -1.804 | 0.071 | 1003 |
| final6 | ISNE | mape | 17.660 | 0.000 | 1069 |
| final6 | MISO | mape | -20.555 | 0.000 | 1084 |
| final6 | NYIS | mape | -2.260 | 0.024 | 1058 |
| final6 | PJM | mape | -12.392 | 0.000 | 1057 |
| final6 | SWPP | mape | -16.487 | 0.000 | 1066 |
| final6 | TVA | mape | 4.014 | 0.000 | 1076 |
| final6_additive | BPAT | mape | 7.923 | 0.000 | 1081 |
| final6_additive | CISO | mape | -27.171 | 0.000 | 1044 |
| final6_additive | DUK | mape | 8.015 | 0.000 | 1070 |
| final6_additive | ERCO | mape | 11.243 | 0.000 | 1071 |
| final6_additive | FPL | mape | 13.270 | 0.000 | 1003 |
| final6_additive | ISNE | mape | 21.049 | 0.000 | 1069 |
| final6_additive | MISO | mape | -13.213 | 0.000 | 1084 |
| final6_additive | NYIS | mape | 2.943 | 0.003 | 1058 |
| final6_additive | PJM | mape | -4.065 | 0.000 | 1057 |
| final6_additive | SWPP | mape | -13.752 | 0.000 | 1066 |
| final6_additive | TVA | mape | 9.747 | 0.000 | 1076 |
| final6_boosting | BPAT | mape | 7.041 | 0.000 | 1081 |
| final6_boosting | CISO | mape | -32.720 | 0.000 | 1044 |
| final6_boosting | DUK | mape | 6.645 | 0.000 | 1070 |
| final6_boosting | ERCO | mape | 4.044 | 0.000 | 1071 |
| final6_boosting | FPL | mape | 13.920 | 0.000 | 1003 |
| final6_boosting | ISNE | mape | 18.255 | 0.000 | 1069 |
| final6_boosting | MISO | mape | -16.625 | 0.000 | 1084 |
| final6_boosting | NYIS | mape | -0.449 | 0.653 | 1058 |
| final6_boosting | PJM | mape | -5.311 | 0.000 | 1057 |
| final6_boosting | SWPP | mape | -13.701 | 0.000 | 1066 |
| final6_boosting | TVA | mape | 8.264 | 0.000 | 1076 |
| final6_ensemble | BPAT | mape | 4.370 | 0.000 | 1081 |
| final6_ensemble | CISO | mape | -32.100 | 0.000 | 1044 |
| final6_ensemble | DUK | mape | 3.818 | 0.000 | 1070 |
| final6_ensemble | ERCO | mape | 5.386 | 0.000 | 1071 |
| final6_ensemble | FPL | mape | 11.235 | 0.000 | 1003 |
| final6_ensemble | ISNE | mape | 19.686 | 0.000 | 1069 |
| final6_ensemble | MISO | mape | -16.857 | 0.000 | 1084 |
| final6_ensemble | NYIS | mape | -0.583 | 0.560 | 1058 |
| final6_ensemble | PJM | mape | -10.711 | 0.000 | 1057 |
| final6_ensemble | SWPP | mape | -15.616 | 0.000 | 1066 |
| final6_ensemble | TVA | mape | 4.436 | 0.000 | 1076 |
| final6_recency | BPAT | mape | 16.430 | 0.000 | 1081 |
| final6_recency | CISO | mape | -9.404 | 0.000 | 1044 |
| final6_recency | DUK | mape | 13.821 | 0.000 | 1070 |
| final6_recency | ERCO | mape | 13.715 | 0.000 | 1071 |
| final6_recency | FPL | mape | 24.346 | 0.000 | 1003 |
| final6_recency | ISNE | mape | 44.207 | 0.000 | 1069 |
| final6_recency | MISO | mape | -3.268 | 0.001 | 1084 |
| final6_recency | NYIS | mape | 22.916 | 0.000 | 1058 |
| final6_recency | PJM | mape | 7.270 | 0.000 | 1057 |
| final6_recency | SWPP | mape | -10.856 | 0.000 | 1066 |
| final6_recency | TVA | mape | 14.789 | 0.000 | 1076 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final6 | 0.991 |
| final6_additive | 0.969 |
| final6_boosting | 0.991 |
| final6_ensemble | 0.991 |
| final6_recency | 0.991 |
