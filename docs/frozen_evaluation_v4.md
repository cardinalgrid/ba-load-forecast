# Fourth look at 2023 to 2025: the recipe after phase I, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase I (`final5`: the phase H recipe with the wind block in the boosting, the peak read at the 70th percentile on the coldest decile of days and 23 quantiles) on 2023 to 2025 under protocol v2, with the observed-temperature supplement. A fourth look at these years: compare with `docs/frozen_evaluation_v3.md` (same days, same rules) and read the difference as an estimate.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | 2.38 | 2.04 | 0.07 | -1.26 | 1.21 | 0.59 | 0.30 | -38.32 | 11679 | 11.00 |
| final5_ensemble | 2.70 | 2.36 | -1.21 | -2.06 | 1.24 | 0.52 | 0.24 | -41.64 | 11679 | 11.00 |
| final5_boosting | 2.81 | 2.48 | -1.05 | -2.02 | 1.41 | 0.49 | 0.24 | -42.11 | 11679 | 11.00 |
| final5_additive | 2.88 | 2.54 | -1.26 | -2.23 | 1.26 | 0.48 | 0.23 | -40.68 | 11679 | 11.00 |
| DF | 2.90 | 2.50 | 0.31 | -1.10 | 0.98 | 0.00 | 0.00 | -41.79 | 11679 | 11.00 |
| final5_recency | 3.53 | 3.20 | -1.34 | -2.50 | 1.57 | 0.36 | 0.22 | -42.33 | 11679 | 11.00 |

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
| final5 | BPAT | 2.24 | 1.97 | -0.03 | -1.20 | 1.43 | -16.54 | 0.44 | 0.39 | 1081 | 6762.61 |
| final5 | CISO | 2.77 | 2.54 | -0.22 | -1.53 | 1.07 | -15.36 | 0.87 | 0.40 | 1044 | 25453.81 |
| final5 | DUK | 3.22 | 2.70 | 0.54 | -1.72 | 1.34 | -14.60 | 0.38 | 0.27 | 1070 | 12295.77 |
| final5 | ERCO | 2.40 | 2.04 | 0.06 | -1.38 | 0.94 | -16.69 | 0.49 | 0.21 | 1071 | 53336.07 |
| final5 | FPL | 3.33 | 2.92 | 0.63 | -1.51 | 1.05 | -38.32 | 0.53 | 0.41 | 1003 | 16583.18 |
| final5 | ISNE | 3.70 | 3.27 | 0.13 | -1.31 | 0.49 | -22.24 | 0.31 | 0.19 | 1069 | 12999.48 |
| final5 | MISO | 1.84 | 1.58 | 0.07 | -0.95 | 1.46 | -7.21 | 0.70 | 0.08 | 1084 | 74014.33 |
| final5 | NYIS | 2.62 | 2.31 | 0.04 | -1.23 | 0.62 | -18.56 | 0.51 | 0.73 | 1058 | 17111.01 |
| final5 | PJM | 2.10 | 1.81 | 0.09 | -1.15 | 1.17 | -10.41 | 0.62 | 0.42 | 1057 | 93208.59 |
| final5 | SWPP | 2.39 | 1.84 | -0.24 | -1.39 | 1.72 | -22.84 | 0.61 | 0.34 | 1066 | 33074.81 |
| final5 | TVA | 2.76 | 2.35 | 0.08 | -1.54 | 1.37 | -14.16 | 0.37 | 0.22 | 1076 | 18806.27 |
| final5_additive | BPAT | 2.44 | 2.14 | -1.30 | -1.98 | 1.51 | -16.51 | 0.39 | 0.29 | 1081 | 6762.61 |
| final5_additive | CISO | 3.84 | 3.41 | -2.62 | -3.51 | 1.21 | -19.88 | 0.75 | 0.30 | 1044 | 25453.81 |
| final5_additive | DUK | 3.39 | 2.84 | -1.12 | -2.59 | 1.31 | -16.30 | 0.34 | 0.19 | 1070 | 12295.77 |
| final5_additive | ERCO | 3.29 | 3.06 | -2.09 | -2.86 | 0.95 | -18.27 | 0.31 | 0.12 | 1071 | 53336.07 |
| final5_additive | FPL | 4.90 | 4.59 | -4.27 | -4.92 | 0.99 | -40.68 | 0.26 | 0.12 | 1003 | 16583.18 |
| final5_additive | ISNE | 4.15 | 3.60 | -0.80 | -2.21 | 0.58 | -19.86 | 0.24 | 0.16 | 1069 | 12999.48 |
| final5_additive | MISO | 2.19 | 1.95 | -0.87 | -1.63 | 1.57 | -9.96 | 0.60 | 0.06 | 1084 | 74014.33 |
| final5_additive | NYIS | 2.86 | 2.51 | -1.14 | -2.03 | 0.59 | -18.07 | 0.48 | 0.64 | 1058 | 17111.01 |
| final5_additive | PJM | 2.47 | 2.15 | -0.46 | -1.63 | 1.28 | -12.00 | 0.53 | 0.35 | 1057 | 93208.59 |
| final5_additive | SWPP | 2.52 | 2.02 | -1.44 | -2.19 | 1.69 | -22.92 | 0.56 | 0.25 | 1066 | 33074.81 |
| final5_additive | TVA | 3.04 | 2.50 | 0.02 | -1.71 | 1.35 | -14.91 | 0.33 | 0.23 | 1076 | 18806.27 |
| final5_boosting | BPAT | 2.52 | 2.20 | -0.82 | -1.82 | 1.69 | -17.99 | 0.34 | 0.32 | 1081 | 6762.61 |
| final5_boosting | CISO | 3.18 | 2.85 | -2.14 | -2.77 | 1.14 | -15.40 | 0.80 | 0.32 | 1044 | 25453.81 |
| final5_boosting | DUK | 3.40 | 2.86 | -1.10 | -2.56 | 1.41 | -17.85 | 0.35 | 0.21 | 1070 | 12295.77 |
| final5_boosting | ERCO | 2.88 | 2.57 | -1.95 | -2.62 | 1.16 | -16.04 | 0.35 | 0.12 | 1071 | 53336.07 |
| final5_boosting | FPL | 5.10 | 4.83 | -5.23 | -5.55 | 1.39 | -42.11 | 0.21 | 0.08 | 1003 | 16583.18 |
| final5_boosting | ISNE | 3.88 | 3.40 | -0.59 | -1.67 | 0.56 | -14.88 | 0.28 | 0.17 | 1069 | 12999.48 |
| final5_boosting | MISO | 2.08 | 1.88 | -0.75 | -1.47 | 1.57 | -10.35 | 0.66 | 0.05 | 1084 | 74014.33 |
| final5_boosting | NYIS | 2.85 | 2.50 | -0.56 | -1.53 | 0.74 | -18.83 | 0.47 | 0.70 | 1058 | 17111.01 |
| final5_boosting | PJM | 2.55 | 2.27 | -0.09 | -1.39 | 1.53 | -11.45 | 0.48 | 0.40 | 1057 | 93208.59 |
| final5_boosting | SWPP | 2.89 | 2.23 | -0.96 | -2.10 | 1.85 | -21.91 | 0.52 | 0.28 | 1066 | 33074.81 |
| final5_boosting | TVA | 3.07 | 2.61 | -0.16 | -1.79 | 1.52 | -14.55 | 0.29 | 0.21 | 1076 | 18806.27 |
| final5_ensemble | BPAT | 2.30 | 2.03 | -1.37 | -1.97 | 1.42 | -16.75 | 0.41 | 0.30 | 1081 | 6762.61 |
| final5_ensemble | CISO | 3.39 | 2.96 | -2.42 | -3.15 | 1.26 | -17.01 | 0.80 | 0.31 | 1044 | 25453.81 |
| final5_ensemble | DUK | 3.26 | 2.70 | -1.02 | -2.48 | 1.32 | -15.94 | 0.38 | 0.20 | 1070 | 12295.77 |
| final5_ensemble | ERCO | 2.96 | 2.67 | -2.14 | -2.73 | 0.97 | -17.10 | 0.36 | 0.12 | 1071 | 53336.07 |
| final5_ensemble | FPL | 4.93 | 4.70 | -4.99 | -5.37 | 1.02 | -41.64 | 0.25 | 0.09 | 1003 | 16583.18 |
| final5_ensemble | ISNE | 3.89 | 3.42 | -0.97 | -1.95 | 0.52 | -18.62 | 0.27 | 0.15 | 1069 | 12999.48 |
| final5_ensemble | MISO | 2.05 | 1.85 | -0.83 | -1.47 | 1.45 | -9.69 | 0.65 | 0.06 | 1084 | 74014.33 |
| final5_ensemble | NYIS | 2.71 | 2.42 | -0.98 | -1.76 | 0.65 | -17.04 | 0.50 | 0.66 | 1058 | 17111.01 |
| final5_ensemble | PJM | 2.29 | 2.00 | -0.28 | -1.36 | 1.32 | -11.46 | 0.57 | 0.38 | 1057 | 93208.59 |
| final5_ensemble | SWPP | 2.47 | 1.91 | -1.27 | -2.09 | 1.58 | -22.54 | 0.59 | 0.25 | 1066 | 33074.81 |
| final5_ensemble | TVA | 2.93 | 2.39 | 0.03 | -1.61 | 1.28 | -14.35 | 0.35 | 0.23 | 1076 | 18806.27 |
| final5_recency | BPAT | 2.88 | 2.60 | -2.10 | -2.58 | 1.69 | -15.57 | 0.26 | 0.23 | 1081 | 6762.61 |
| final5_recency | CISO | 5.02 | 4.73 | -2.72 | -3.89 | 1.58 | -23.26 | 0.57 | 0.30 | 1044 | 25453.81 |
| final5_recency | DUK | 3.97 | 3.44 | -0.74 | -2.75 | 1.47 | -17.72 | 0.26 | 0.21 | 1070 | 12295.77 |
| final5_recency | ERCO | 3.56 | 3.24 | -2.50 | -3.22 | 1.18 | -19.88 | 0.25 | 0.11 | 1071 | 53336.07 |
| final5_recency | FPL | 6.17 | 5.75 | -5.74 | -6.30 | 1.17 | -42.33 | 0.13 | 0.10 | 1003 | 16583.18 |
| final5_recency | ISNE | 6.18 | 5.72 | -1.86 | -2.82 | 0.75 | -23.61 | 0.05 | 0.14 | 1069 | 12999.48 |
| final5_recency | MISO | 2.74 | 2.49 | -0.84 | -1.74 | 1.98 | -11.52 | 0.51 | 0.07 | 1084 | 74014.33 |
| final5_recency | NYIS | 4.16 | 3.84 | -1.39 | -2.43 | 0.94 | -13.78 | 0.24 | 0.55 | 1058 | 17111.01 |
| final5_recency | PJM | 2.91 | 2.68 | -0.21 | -1.70 | 1.71 | -12.59 | 0.36 | 0.35 | 1057 | 93208.59 |
| final5_recency | SWPP | 3.03 | 2.46 | -1.36 | -2.49 | 1.76 | -22.90 | 0.49 | 0.23 | 1066 | 33074.81 |
| final5_recency | TVA | 3.63 | 3.05 | 0.40 | -1.79 | 1.54 | -14.70 | 0.21 | 0.23 | 1076 | 18806.27 |

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
| final5 | BPAT | gerri_heather | 4.91 | -3.82 | -3.91 | -11.18 | 6 |
| final5 | CISO | gerri_heather | 2.64 | 0.74 | -0.54 | -2.96 | 6 |
| final5 | DUK | gerri_heather | 5.76 | -5.41 | -5.41 | -8.96 | 6 |
| final5 | ERCO | gerri_heather | 6.23 | -7.16 | -7.16 | -13.58 | 6 |
| final5 | FPL | gerri_heather | 4.75 | -4.66 | -5.61 | -9.99 | 6 |
| final5 | ISNE | gerri_heather | 3.59 | -0.12 | -1.22 | -5.31 | 6 |
| final5 | MISO | gerri_heather | 3.00 | -1.50 | -2.03 | -4.08 | 6 |
| final5 | NYIS | gerri_heather | 1.65 | 0.56 | -0.27 | -1.17 | 5 |
| final5 | PJM | gerri_heather | 2.86 | 0.30 | -0.85 | -2.89 | 6 |
| final5 | SWPP | gerri_heather | 5.59 | -5.18 | -5.18 | -14.27 | 6 |
| final5 | TVA | gerri_heather | 3.12 | 1.13 | -0.77 | -3.99 | 6 |
| final5_additive | BPAT | gerri_heather | 6.08 | -5.93 | -6.13 | -15.02 | 6 |
| final5_additive | CISO | gerri_heather | 2.95 | 1.79 | -0.21 | -1.11 | 6 |
| final5_additive | DUK | gerri_heather | 5.95 | -7.37 | -7.37 | -15.45 | 6 |
| final5_additive | ERCO | gerri_heather | 7.92 | -9.94 | -9.94 | -17.13 | 6 |
| final5_additive | FPL | gerri_heather | 6.52 | -8.08 | -8.08 | -14.17 | 6 |
| final5_additive | ISNE | gerri_heather | 3.99 | 0.05 | -1.83 | -6.12 | 6 |
| final5_additive | MISO | gerri_heather | 2.91 | -2.33 | -2.52 | -4.07 | 6 |
| final5_additive | NYIS | gerri_heather | 1.74 | -1.04 | -1.40 | -2.80 | 5 |
| final5_additive | PJM | gerri_heather | 2.83 | 1.44 | -0.26 | -1.25 | 6 |
| final5_additive | SWPP | gerri_heather | 7.09 | -7.70 | -7.70 | -18.12 | 6 |
| final5_additive | TVA | gerri_heather | 3.35 | 1.81 | -1.12 | -6.48 | 6 |
| final5_boosting | BPAT | gerri_heather | 6.59 | -7.82 | -7.82 | -14.76 | 6 |
| final5_boosting | CISO | gerri_heather | 2.67 | 0.96 | -0.84 | -5.03 | 6 |
| final5_boosting | DUK | gerri_heather | 5.82 | -6.22 | -6.43 | -11.77 | 6 |
| final5_boosting | ERCO | gerri_heather | 6.49 | -9.56 | -9.56 | -16.04 | 6 |
| final5_boosting | FPL | gerri_heather | 4.93 | -6.04 | -6.87 | -12.09 | 6 |
| final5_boosting | ISNE | gerri_heather | 3.56 | 0.06 | -1.16 | -4.94 | 6 |
| final5_boosting | MISO | gerri_heather | 2.80 | -1.82 | -2.73 | -6.25 | 6 |
| final5_boosting | NYIS | gerri_heather | 2.24 | 1.87 | -0.04 | -0.21 | 5 |
| final5_boosting | PJM | gerri_heather | 2.84 | 0.34 | -1.17 | -2.21 | 6 |
| final5_boosting | SWPP | gerri_heather | 6.17 | -7.23 | -7.23 | -14.15 | 6 |
| final5_boosting | TVA | gerri_heather | 3.63 | -1.15 | -3.20 | -10.20 | 6 |
| final5_ensemble | BPAT | gerri_heather | 5.54 | -5.87 | -5.87 | -13.42 | 6 |
| final5_ensemble | CISO | gerri_heather | 2.64 | 1.54 | -0.59 | -3.54 | 6 |
| final5_ensemble | DUK | gerri_heather | 5.85 | -7.18 | -7.18 | -14.26 | 6 |
| final5_ensemble | ERCO | gerri_heather | 6.26 | -8.42 | -8.42 | -12.46 | 6 |
| final5_ensemble | FPL | gerri_heather | 5.75 | -7.65 | -7.65 | -12.93 | 6 |
| final5_ensemble | ISNE | gerri_heather | 3.86 | -0.07 | -1.49 | -5.88 | 6 |
| final5_ensemble | MISO | gerri_heather | 2.81 | -2.09 | -2.64 | -5.72 | 6 |
| final5_ensemble | NYIS | gerri_heather | 1.86 | 0.17 | -0.36 | -1.26 | 5 |
| final5_ensemble | PJM | gerri_heather | 2.60 | 0.82 | -0.72 | -2.02 | 6 |
| final5_ensemble | SWPP | gerri_heather | 7.03 | -7.87 | -7.87 | -16.60 | 6 |
| final5_ensemble | TVA | gerri_heather | 2.94 | 1.04 | -1.16 | -5.47 | 6 |
| final5_recency | BPAT | gerri_heather | 4.95 | -3.60 | -3.93 | -10.22 | 6 |
| final5_recency | CISO | gerri_heather | 3.52 | 2.00 | -0.72 | -4.31 | 6 |
| final5_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final5_recency | ERCO | gerri_heather | 5.53 | -5.59 | -5.89 | -10.83 | 6 |
| final5_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final5_recency | ISNE | gerri_heather | 5.43 | -0.43 | -1.75 | -6.86 | 6 |
| final5_recency | MISO | gerri_heather | 3.32 | -2.10 | -2.68 | -7.06 | 6 |
| final5_recency | NYIS | gerri_heather | 3.53 | -0.64 | -0.83 | -2.57 | 5 |
| final5_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final5_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| final5_recency | TVA | gerri_heather | 4.68 | 2.89 | -1.21 | -7.25 | 6 |
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
| final5 | BPAT | january_2025 | 2.48 | -2.63 | -3.15 | -4.45 | 6 |
| final5 | CISO | january_2025 | 2.06 | 1.49 | 0.00 | 0.00 | 6 |
| final5 | DUK | january_2025 | 4.52 | 1.85 | -1.38 | -5.93 | 6 |
| final5 | ERCO | january_2025 | 3.06 | -3.50 | -3.50 | -7.47 | 6 |
| final5 | FPL | january_2025 | 5.16 | -4.58 | -4.58 | -10.83 | 6 |
| final5 | ISNE | january_2025 | 3.85 | 0.17 | -0.83 | -2.29 | 6 |
| final5 | MISO | january_2025 | 2.75 | -2.39 | -2.39 | -4.21 | 6 |
| final5 | NYIS | january_2025 | 2.13 | 2.17 | 0.00 | 0.00 | 5 |
| final5 | PJM | january_2025 | 2.08 | -1.01 | -1.39 | -3.43 | 6 |
| final5 | SWPP | january_2025 | 2.43 | -1.91 | -1.91 | -3.32 | 6 |
| final5 | TVA | january_2025 | 3.18 | -0.14 | -1.22 | -5.93 | 6 |
| final5_additive | BPAT | january_2025 | 3.13 | -3.47 | -3.96 | -5.55 | 6 |
| final5_additive | CISO | january_2025 | 3.46 | 2.03 | 0.00 | 0.00 | 6 |
| final5_additive | DUK | january_2025 | 4.14 | 1.37 | -0.83 | -5.01 | 6 |
| final5_additive | ERCO | january_2025 | 3.38 | -3.78 | -3.78 | -8.01 | 6 |
| final5_additive | FPL | january_2025 | 5.03 | -3.35 | -3.67 | -9.21 | 6 |
| final5_additive | ISNE | january_2025 | 3.43 | 0.05 | -1.05 | -3.20 | 6 |
| final5_additive | MISO | january_2025 | 2.92 | -2.45 | -2.51 | -4.71 | 6 |
| final5_additive | NYIS | january_2025 | 1.73 | -0.55 | -1.03 | -2.66 | 5 |
| final5_additive | PJM | january_2025 | 2.43 | 0.89 | -0.35 | -1.50 | 6 |
| final5_additive | SWPP | january_2025 | 3.53 | -3.65 | -3.65 | -6.13 | 6 |
| final5_additive | TVA | january_2025 | 3.79 | -1.37 | -2.27 | -6.67 | 6 |
| final5_boosting | BPAT | january_2025 | 3.58 | -6.34 | -6.34 | -8.93 | 6 |
| final5_boosting | CISO | january_2025 | 2.46 | 0.59 | -0.51 | -1.72 | 6 |
| final5_boosting | DUK | january_2025 | 4.11 | -2.59 | -2.67 | -8.53 | 6 |
| final5_boosting | ERCO | january_2025 | 3.24 | -5.32 | -5.32 | -8.22 | 6 |
| final5_boosting | FPL | january_2025 | 4.40 | -5.16 | -5.16 | -10.17 | 6 |
| final5_boosting | ISNE | january_2025 | 4.35 | -0.44 | -1.51 | -3.67 | 6 |
| final5_boosting | MISO | january_2025 | 2.84 | -3.56 | -3.56 | -5.12 | 6 |
| final5_boosting | NYIS | january_2025 | 2.67 | 0.86 | -0.36 | -1.12 | 5 |
| final5_boosting | PJM | january_2025 | 2.72 | -4.21 | -4.21 | -9.07 | 6 |
| final5_boosting | SWPP | january_2025 | 4.28 | -8.06 | -8.06 | -10.57 | 6 |
| final5_boosting | TVA | january_2025 | 3.14 | -2.75 | -2.75 | -5.46 | 6 |
| final5_ensemble | BPAT | january_2025 | 3.23 | -5.39 | -5.43 | -7.34 | 6 |
| final5_ensemble | CISO | january_2025 | 3.08 | 1.16 | -0.47 | -1.69 | 6 |
| final5_ensemble | DUK | january_2025 | 3.98 | -0.25 | -1.61 | -7.63 | 6 |
| final5_ensemble | ERCO | january_2025 | 3.16 | -5.18 | -5.18 | -7.52 | 6 |
| final5_ensemble | FPL | january_2025 | 4.18 | -4.10 | -4.10 | -9.52 | 6 |
| final5_ensemble | ISNE | january_2025 | 3.13 | -0.07 | -0.93 | -2.88 | 6 |
| final5_ensemble | MISO | january_2025 | 2.72 | -3.33 | -3.33 | -4.32 | 6 |
| final5_ensemble | NYIS | january_2025 | 1.22 | 0.14 | -0.33 | -0.82 | 5 |
| final5_ensemble | PJM | january_2025 | 2.27 | -1.87 | -1.98 | -4.11 | 6 |
| final5_ensemble | SWPP | january_2025 | 3.97 | -5.54 | -5.54 | -6.16 | 6 |
| final5_ensemble | TVA | january_2025 | 2.82 | -2.03 | -2.12 | -5.54 | 6 |
| final5_recency | BPAT | january_2025 | 3.27 | -6.31 | -6.31 | -8.11 | 6 |
| final5_recency | CISO | january_2025 | 5.72 | 0.91 | -2.66 | -5.17 | 6 |
| final5_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final5_recency | ERCO | january_2025 | 3.97 | -6.76 | -6.76 | -7.58 | 6 |
| final5_recency | FPL | january_2025 | 5.22 | -3.46 | -3.78 | -8.95 | 6 |
| final5_recency | ISNE | january_2025 | 3.79 | 0.28 | -0.90 | -4.07 | 6 |
| final5_recency | MISO | january_2025 | 3.41 | -4.01 | -4.01 | -5.00 | 6 |
| final5_recency | NYIS | january_2025 | 3.11 | -0.05 | -0.87 | -3.05 | 5 |
| final5_recency | PJM | january_2025 | 2.99 | -2.46 | -2.46 | -4.93 | 6 |
| final5_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.84 | 6 |
| final5_recency | TVA | january_2025 | 2.77 | -1.87 | -2.32 | -4.39 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final5 | eve | 3.05 | 1.01 | -1.26 | 0.50 | 322 |
| 10 | final5_ensemble | eve | 3.12 | -0.26 | -1.81 | 0.47 | 322 |
| 8 | final5_additive | eve | 3.18 | -0.21 | -1.92 | 0.44 | 322 |
| 6 | DF | eve | 3.30 | 0.52 | -1.35 |  | 322 |
| 9 | final5_boosting | eve | 3.34 | -0.19 | -1.80 | 0.43 | 322 |
| 11 | final5_recency | eve | 4.08 | -0.47 | -2.33 | 0.34 | 322 |
| 1 | final5 | special | 3.31 | 0.01 | -1.90 | 0.50 | 336 |
| 2 | final5_additive | special | 3.53 | -1.39 | -2.78 | 0.46 | 336 |
| 4 | final5_ensemble | special | 3.54 | -1.20 | -2.59 | 0.46 | 336 |
| 0 | DF | special | 3.56 | 0.06 | -1.69 |  | 336 |
| 3 | final5_boosting | special | 3.74 | -1.03 | -2.48 | 0.42 | 336 |
| 5 | final5_recency | special | 4.53 | -1.24 | -3.02 | 0.33 | 336 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final5 | all | 0.390 | 1.334 | 0.395 | 0.893 | 11.690 | 0.896 | 15.691 | 1.728 | 11448 |
| final5 | events | 0.432 | 1.781 | 0.644 | 0.825 | 13.022 | 0.838 | 21.522 | 2.348 | 130 |
| final5 | cold_mornings | 0.442 | 1.675 | 0.561 | 0.845 | 13.326 | 0.879 | 20.055 | 2.183 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final5 | BPAT | mape | 5.526 | 0.000 | 1081 |
| final5 | CISO | mape | -34.141 | 0.000 | 1044 |
| final5 | DUK | mape | 10.171 | 0.000 | 1070 |
| final5 | ERCO | mape | 0.002 | 0.998 | 1071 |
| final5 | FPL | mape | 2.203 | 0.028 | 1003 |
| final5 | ISNE | mape | 18.548 | 0.000 | 1069 |
| final5 | MISO | mape | -17.843 | 0.000 | 1084 |
| final5 | NYIS | mape | -0.002 | 0.998 | 1058 |
| final5 | PJM | mape | -7.440 | 0.000 | 1057 |
| final5 | SWPP | mape | -15.823 | 0.000 | 1066 |
| final5 | TVA | mape | 10.014 | 0.000 | 1076 |
| final5_additive | BPAT | mape | 9.697 | 0.000 | 1081 |
| final5_additive | CISO | mape | -18.119 | 0.000 | 1044 |
| final5_additive | DUK | mape | 12.113 | 0.000 | 1070 |
| final5_additive | ERCO | mape | 14.249 | 0.000 | 1071 |
| final5_additive | FPL | mape | 22.465 | 0.000 | 1003 |
| final5_additive | ISNE | mape | 23.228 | 0.000 | 1069 |
| final5_additive | MISO | mape | -10.085 | 0.000 | 1084 |
| final5_additive | NYIS | mape | 4.110 | 0.000 | 1058 |
| final5_additive | PJM | mape | 1.557 | 0.119 | 1057 |
| final5_additive | SWPP | mape | -14.460 | 0.000 | 1066 |
| final5_additive | TVA | mape | 14.208 | 0.000 | 1076 |
| final5_boosting | BPAT | mape | 11.820 | 0.000 | 1081 |
| final5_boosting | CISO | mape | -26.421 | 0.000 | 1044 |
| final5_boosting | DUK | mape | 12.729 | 0.000 | 1070 |
| final5_boosting | ERCO | mape | 8.595 | 0.000 | 1071 |
| final5_boosting | FPL | mape | 27.245 | 0.000 | 1003 |
| final5_boosting | ISNE | mape | 20.343 | 0.000 | 1069 |
| final5_boosting | MISO | mape | -12.608 | 0.000 | 1084 |
| final5_boosting | NYIS | mape | 3.839 | 0.000 | 1058 |
| final5_boosting | PJM | mape | 3.345 | 0.001 | 1057 |
| final5_boosting | SWPP | mape | -11.927 | 0.000 | 1066 |
| final5_boosting | TVA | mape | 15.336 | 0.000 | 1076 |
| final5_ensemble | BPAT | mape | 6.995 | 0.000 | 1081 |
| final5_ensemble | CISO | mape | -24.000 | 0.000 | 1044 |
| final5_ensemble | DUK | mape | 10.396 | 0.000 | 1070 |
| final5_ensemble | ERCO | mape | 9.687 | 0.000 | 1071 |
| final5_ensemble | FPL | mape | 23.325 | 0.000 | 1003 |
| final5_ensemble | ISNE | mape | 21.124 | 0.000 | 1069 |
| final5_ensemble | MISO | mape | -13.168 | 0.000 | 1084 |
| final5_ensemble | NYIS | mape | 1.642 | 0.101 | 1058 |
| final5_ensemble | PJM | mape | -2.895 | 0.004 | 1057 |
| final5_ensemble | SWPP | mape | -15.154 | 0.000 | 1066 |
| final5_ensemble | TVA | mape | 12.397 | 0.000 | 1076 |
| final5_recency | BPAT | mape | 18.198 | 0.000 | 1081 |
| final5_recency | CISO | mape | -3.852 | 0.000 | 1044 |
| final5_recency | DUK | mape | 19.470 | 0.000 | 1070 |
| final5_recency | ERCO | mape | 17.844 | 0.000 | 1071 |
| final5_recency | FPL | mape | 32.918 | 0.000 | 1003 |
| final5_recency | ISNE | mape | 44.406 | 0.000 | 1069 |
| final5_recency | MISO | mape | 0.344 | 0.731 | 1084 |
| final5_recency | NYIS | mape | 21.581 | 0.000 | 1058 |
| final5_recency | PJM | mape | 11.820 | 0.000 | 1057 |
| final5_recency | SWPP | mape | -9.941 | 0.000 | 1066 |
| final5_recency | TVA | mape | 21.905 | 0.000 | 1076 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final5 | 0.991 |
| final5_additive | 0.969 |
| final5_boosting | 0.991 |
| final5_ensemble | 0.991 |
| final5_recency | 0.991 |
