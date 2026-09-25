# Third look at 2023 to 2025: the recipe after phase H, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase H (`final4`: the phase G recipe with the humidity block in the boosting and the apparent temperature in the additive model) on 2023 to 2025 under protocol v2, with the observed-temperature supplement. A third look at these years: compare with `docs/frozen_evaluation_v2.md` (same days, same rules) and read the difference as an estimate.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final4 | 2.38 | 2.04 | 0.00 | -1.29 | 1.21 | 0.59 | 0.30 | -37.48 | 11679 | 11.00 |
| final4_ensemble | 2.70 | 2.36 | -1.21 | -2.06 | 1.22 | 0.53 | 0.23 | -41.19 | 11679 | 11.00 |
| final4_boosting | 2.82 | 2.48 | -1.05 | -2.02 | 1.40 | 0.49 | 0.24 | -40.82 | 11679 | 11.00 |
| final4_additive | 2.88 | 2.54 | -1.26 | -2.23 | 1.26 | 0.48 | 0.23 | -40.68 | 11679 | 11.00 |
| DF | 2.90 | 2.50 | 0.31 | -1.10 | 0.98 | 0.00 | 0.00 | -41.79 | 11679 | 11.00 |
| final4_recency | 3.53 | 3.20 | -1.34 | -2.50 | 1.57 | 0.36 | 0.22 | -42.33 | 11679 | 11.00 |

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
| final4 | BPAT | 2.24 | 1.97 | -0.09 | -1.23 | 1.43 | -16.13 | 0.44 | 0.39 | 1081 | 6762.61 |
| final4 | CISO | 2.76 | 2.51 | -0.25 | -1.53 | 1.03 | -15.14 | 0.87 | 0.40 | 1044 | 25453.81 |
| final4 | DUK | 3.21 | 2.72 | 0.42 | -1.75 | 1.35 | -14.70 | 0.39 | 0.27 | 1070 | 12295.77 |
| final4 | ERCO | 2.41 | 2.06 | -0.02 | -1.41 | 0.93 | -16.13 | 0.49 | 0.21 | 1071 | 53336.07 |
| final4 | FPL | 3.33 | 2.91 | 0.53 | -1.55 | 1.07 | -37.48 | 0.53 | 0.41 | 1003 | 16583.18 |
| final4 | ISNE | 3.70 | 3.24 | 0.08 | -1.33 | 0.47 | -21.66 | 0.31 | 0.19 | 1069 | 12999.48 |
| final4 | MISO | 1.84 | 1.60 | 0.03 | -0.98 | 1.47 | -7.12 | 0.70 | 0.08 | 1084 | 74014.33 |
| final4 | NYIS | 2.62 | 2.31 | -0.01 | -1.25 | 0.63 | -18.17 | 0.50 | 0.74 | 1058 | 17111.01 |
| final4 | PJM | 2.11 | 1.82 | 0.03 | -1.19 | 1.20 | -10.51 | 0.61 | 0.41 | 1057 | 93208.59 |
| final4 | SWPP | 2.40 | 1.84 | -0.29 | -1.43 | 1.66 | -22.68 | 0.61 | 0.34 | 1066 | 33074.81 |
| final4 | TVA | 2.75 | 2.34 | -0.05 | -1.60 | 1.39 | -13.83 | 0.36 | 0.22 | 1076 | 18806.27 |
| final4_additive | BPAT | 2.44 | 2.14 | -1.30 | -1.98 | 1.51 | -16.51 | 0.39 | 0.29 | 1081 | 6762.61 |
| final4_additive | CISO | 3.84 | 3.41 | -2.62 | -3.51 | 1.21 | -19.88 | 0.75 | 0.30 | 1044 | 25453.81 |
| final4_additive | DUK | 3.39 | 2.84 | -1.12 | -2.59 | 1.31 | -16.30 | 0.34 | 0.19 | 1070 | 12295.77 |
| final4_additive | ERCO | 3.29 | 3.06 | -2.09 | -2.86 | 0.95 | -18.27 | 0.31 | 0.12 | 1071 | 53336.07 |
| final4_additive | FPL | 4.90 | 4.59 | -4.27 | -4.92 | 0.99 | -40.68 | 0.26 | 0.12 | 1003 | 16583.18 |
| final4_additive | ISNE | 4.15 | 3.60 | -0.80 | -2.21 | 0.58 | -19.86 | 0.24 | 0.16 | 1069 | 12999.48 |
| final4_additive | MISO | 2.19 | 1.95 | -0.87 | -1.63 | 1.57 | -9.96 | 0.60 | 0.06 | 1084 | 74014.33 |
| final4_additive | NYIS | 2.86 | 2.51 | -1.14 | -2.03 | 0.59 | -18.07 | 0.48 | 0.64 | 1058 | 17111.01 |
| final4_additive | PJM | 2.47 | 2.15 | -0.46 | -1.63 | 1.28 | -12.00 | 0.53 | 0.35 | 1057 | 93208.59 |
| final4_additive | SWPP | 2.52 | 2.02 | -1.44 | -2.19 | 1.69 | -22.92 | 0.56 | 0.25 | 1066 | 33074.81 |
| final4_additive | TVA | 3.04 | 2.50 | 0.02 | -1.71 | 1.35 | -14.91 | 0.33 | 0.23 | 1076 | 18806.27 |
| final4_boosting | BPAT | 2.52 | 2.24 | -0.83 | -1.82 | 1.58 | -16.84 | 0.34 | 0.33 | 1081 | 6762.61 |
| final4_boosting | CISO | 3.15 | 2.79 | -2.13 | -2.76 | 1.12 | -14.47 | 0.81 | 0.31 | 1044 | 25453.81 |
| final4_boosting | DUK | 3.37 | 2.79 | -1.14 | -2.56 | 1.45 | -17.16 | 0.35 | 0.21 | 1070 | 12295.77 |
| final4_boosting | ERCO | 2.88 | 2.60 | -1.97 | -2.62 | 1.19 | -17.54 | 0.35 | 0.12 | 1071 | 53336.07 |
| final4_boosting | FPL | 5.14 | 4.93 | -5.27 | -5.60 | 1.33 | -40.82 | 0.20 | 0.08 | 1003 | 16583.18 |
| final4_boosting | ISNE | 3.89 | 3.40 | -0.57 | -1.67 | 0.55 | -14.76 | 0.28 | 0.17 | 1069 | 12999.48 |
| final4_boosting | MISO | 2.09 | 1.92 | -0.73 | -1.44 | 1.55 | -10.34 | 0.66 | 0.06 | 1084 | 74014.33 |
| final4_boosting | NYIS | 2.87 | 2.48 | -0.50 | -1.50 | 0.71 | -17.57 | 0.47 | 0.70 | 1058 | 17111.01 |
| final4_boosting | PJM | 2.57 | 2.26 | -0.11 | -1.39 | 1.54 | -11.57 | 0.48 | 0.40 | 1057 | 93208.59 |
| final4_boosting | SWPP | 2.91 | 2.18 | -0.97 | -2.12 | 1.88 | -21.93 | 0.51 | 0.27 | 1066 | 33074.81 |
| final4_boosting | TVA | 3.05 | 2.57 | -0.21 | -1.83 | 1.48 | -14.03 | 0.29 | 0.21 | 1076 | 18806.27 |
| final4_ensemble | BPAT | 2.31 | 2.03 | -1.37 | -1.98 | 1.40 | -16.35 | 0.41 | 0.30 | 1081 | 6762.61 |
| final4_ensemble | CISO | 3.38 | 2.95 | -2.42 | -3.15 | 1.25 | -16.62 | 0.79 | 0.31 | 1044 | 25453.81 |
| final4_ensemble | DUK | 3.25 | 2.69 | -1.03 | -2.48 | 1.31 | -15.92 | 0.37 | 0.20 | 1070 | 12295.77 |
| final4_ensemble | ERCO | 2.96 | 2.67 | -2.15 | -2.73 | 0.97 | -16.57 | 0.35 | 0.12 | 1071 | 53336.07 |
| final4_ensemble | FPL | 4.95 | 4.69 | -5.01 | -5.39 | 1.01 | -41.19 | 0.26 | 0.09 | 1003 | 16583.18 |
| final4_ensemble | ISNE | 3.89 | 3.42 | -0.96 | -1.96 | 0.54 | -18.13 | 0.28 | 0.15 | 1069 | 12999.48 |
| final4_ensemble | MISO | 2.05 | 1.84 | -0.82 | -1.46 | 1.40 | -9.60 | 0.65 | 0.05 | 1084 | 74014.33 |
| final4_ensemble | NYIS | 2.71 | 2.41 | -0.96 | -1.74 | 0.62 | -16.51 | 0.50 | 0.67 | 1058 | 17111.01 |
| final4_ensemble | PJM | 2.29 | 1.99 | -0.28 | -1.37 | 1.28 | -11.52 | 0.58 | 0.37 | 1057 | 93208.59 |
| final4_ensemble | SWPP | 2.48 | 1.94 | -1.27 | -2.09 | 1.61 | -22.55 | 0.58 | 0.26 | 1066 | 33074.81 |
| final4_ensemble | TVA | 2.93 | 2.40 | 0.01 | -1.62 | 1.28 | -14.17 | 0.35 | 0.22 | 1076 | 18806.27 |
| final4_recency | BPAT | 2.88 | 2.60 | -2.10 | -2.58 | 1.69 | -15.57 | 0.26 | 0.23 | 1081 | 6762.61 |
| final4_recency | CISO | 5.02 | 4.73 | -2.72 | -3.89 | 1.58 | -23.26 | 0.57 | 0.30 | 1044 | 25453.81 |
| final4_recency | DUK | 3.97 | 3.44 | -0.74 | -2.75 | 1.47 | -17.72 | 0.26 | 0.21 | 1070 | 12295.77 |
| final4_recency | ERCO | 3.56 | 3.24 | -2.50 | -3.22 | 1.18 | -19.88 | 0.25 | 0.11 | 1071 | 53336.07 |
| final4_recency | FPL | 6.17 | 5.75 | -5.74 | -6.30 | 1.17 | -42.33 | 0.13 | 0.10 | 1003 | 16583.18 |
| final4_recency | ISNE | 6.18 | 5.72 | -1.86 | -2.82 | 0.75 | -23.61 | 0.05 | 0.14 | 1069 | 12999.48 |
| final4_recency | MISO | 2.74 | 2.49 | -0.84 | -1.74 | 1.98 | -11.52 | 0.51 | 0.07 | 1084 | 74014.33 |
| final4_recency | NYIS | 4.16 | 3.84 | -1.39 | -2.43 | 0.94 | -13.78 | 0.24 | 0.55 | 1058 | 17111.01 |
| final4_recency | PJM | 2.91 | 2.68 | -0.21 | -1.70 | 1.71 | -12.59 | 0.36 | 0.35 | 1057 | 93208.59 |
| final4_recency | SWPP | 3.03 | 2.46 | -1.36 | -2.49 | 1.76 | -22.90 | 0.49 | 0.23 | 1066 | 33074.81 |
| final4_recency | TVA | 3.63 | 3.05 | 0.40 | -1.79 | 1.54 | -14.70 | 0.21 | 0.23 | 1076 | 18806.27 |

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
| final4 | BPAT | gerri_heather | 5.01 | -4.68 | -4.68 | -11.54 | 6 |
| final4 | CISO | gerri_heather | 2.62 | 0.80 | -0.47 | -2.48 | 6 |
| final4 | DUK | gerri_heather | 5.75 | -5.87 | -5.87 | -9.57 | 6 |
| final4 | ERCO | gerri_heather | 6.40 | -7.94 | -7.94 | -14.21 | 6 |
| final4 | FPL | gerri_heather | 4.88 | -5.04 | -5.90 | -10.22 | 6 |
| final4 | ISNE | gerri_heather | 3.61 | -0.32 | -1.39 | -5.18 | 6 |
| final4 | MISO | gerri_heather | 3.04 | -2.13 | -2.53 | -5.02 | 6 |
| final4 | NYIS | gerri_heather | 1.67 | -0.12 | -0.82 | -2.27 | 5 |
| final4 | PJM | gerri_heather | 2.84 | 0.14 | -1.02 | -3.44 | 6 |
| final4 | SWPP | gerri_heather | 5.72 | -5.69 | -5.69 | -14.59 | 6 |
| final4 | TVA | gerri_heather | 3.16 | -0.39 | -1.48 | -5.96 | 6 |
| final4_additive | BPAT | gerri_heather | 6.08 | -5.93 | -6.13 | -15.02 | 6 |
| final4_additive | CISO | gerri_heather | 2.95 | 1.79 | -0.21 | -1.11 | 6 |
| final4_additive | DUK | gerri_heather | 5.95 | -7.37 | -7.37 | -15.45 | 6 |
| final4_additive | ERCO | gerri_heather | 7.92 | -9.94 | -9.94 | -17.13 | 6 |
| final4_additive | FPL | gerri_heather | 6.52 | -8.08 | -8.08 | -14.17 | 6 |
| final4_additive | ISNE | gerri_heather | 3.99 | 0.05 | -1.83 | -6.12 | 6 |
| final4_additive | MISO | gerri_heather | 2.91 | -2.33 | -2.52 | -4.07 | 6 |
| final4_additive | NYIS | gerri_heather | 1.74 | -1.04 | -1.40 | -2.80 | 5 |
| final4_additive | PJM | gerri_heather | 2.83 | 1.44 | -0.26 | -1.25 | 6 |
| final4_additive | SWPP | gerri_heather | 7.09 | -7.70 | -7.70 | -18.12 | 6 |
| final4_additive | TVA | gerri_heather | 3.35 | 1.81 | -1.12 | -6.48 | 6 |
| final4_boosting | BPAT | gerri_heather | 6.16 | -7.15 | -7.15 | -12.80 | 6 |
| final4_boosting | CISO | gerri_heather | 2.64 | 1.27 | -0.53 | -3.15 | 6 |
| final4_boosting | DUK | gerri_heather | 5.73 | -6.21 | -6.57 | -12.50 | 6 |
| final4_boosting | ERCO | gerri_heather | 6.34 | -9.69 | -9.69 | -17.54 | 6 |
| final4_boosting | FPL | gerri_heather | 5.04 | -6.57 | -7.18 | -12.59 | 6 |
| final4_boosting | ISNE | gerri_heather | 3.47 | 0.36 | -0.70 | -3.65 | 6 |
| final4_boosting | MISO | gerri_heather | 2.49 | -2.08 | -2.78 | -6.61 | 6 |
| final4_boosting | NYIS | gerri_heather | 2.27 | 1.51 | -0.27 | -1.34 | 5 |
| final4_boosting | PJM | gerri_heather | 3.00 | 0.89 | -0.80 | -2.53 | 6 |
| final4_boosting | SWPP | gerri_heather | 6.05 | -7.25 | -7.25 | -13.19 | 6 |
| final4_boosting | TVA | gerri_heather | 3.59 | -1.39 | -3.20 | -10.42 | 6 |
| final4_ensemble | BPAT | gerri_heather | 5.41 | -5.65 | -5.65 | -12.71 | 6 |
| final4_ensemble | CISO | gerri_heather | 2.62 | 1.65 | -0.47 | -2.83 | 6 |
| final4_ensemble | DUK | gerri_heather | 5.79 | -7.16 | -7.16 | -14.48 | 6 |
| final4_ensemble | ERCO | gerri_heather | 6.26 | -8.47 | -8.47 | -12.88 | 6 |
| final4_ensemble | FPL | gerri_heather | 5.89 | -7.86 | -7.86 | -12.90 | 6 |
| final4_ensemble | ISNE | gerri_heather | 3.82 | 0.04 | -1.35 | -5.40 | 6 |
| final4_ensemble | MISO | gerri_heather | 2.75 | -2.19 | -2.66 | -5.85 | 6 |
| final4_ensemble | NYIS | gerri_heather | 1.86 | 0.02 | -0.44 | -1.69 | 5 |
| final4_ensemble | PJM | gerri_heather | 2.66 | 1.01 | -0.68 | -2.28 | 6 |
| final4_ensemble | SWPP | gerri_heather | 6.98 | -7.89 | -7.89 | -16.28 | 6 |
| final4_ensemble | TVA | gerri_heather | 2.98 | 0.94 | -1.25 | -5.72 | 6 |
| final4_recency | BPAT | gerri_heather | 4.95 | -3.60 | -3.93 | -10.22 | 6 |
| final4_recency | CISO | gerri_heather | 3.52 | 2.00 | -0.72 | -4.31 | 6 |
| final4_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final4_recency | ERCO | gerri_heather | 5.53 | -5.59 | -5.89 | -10.83 | 6 |
| final4_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final4_recency | ISNE | gerri_heather | 5.43 | -0.43 | -1.75 | -6.86 | 6 |
| final4_recency | MISO | gerri_heather | 3.32 | -2.10 | -2.68 | -7.06 | 6 |
| final4_recency | NYIS | gerri_heather | 3.53 | -0.64 | -0.83 | -2.57 | 5 |
| final4_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final4_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| final4_recency | TVA | gerri_heather | 4.68 | 2.89 | -1.21 | -7.25 | 6 |
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
| final4 | BPAT | january_2025 | 2.48 | -2.99 | -3.44 | -4.99 | 6 |
| final4 | CISO | january_2025 | 1.94 | 0.88 | -0.02 | -0.10 | 6 |
| final4 | DUK | january_2025 | 4.39 | 0.53 | -1.48 | -6.66 | 6 |
| final4 | ERCO | january_2025 | 3.24 | -4.45 | -4.45 | -7.61 | 6 |
| final4 | FPL | january_2025 | 5.39 | -5.78 | -5.78 | -12.09 | 6 |
| final4 | ISNE | january_2025 | 3.86 | -0.41 | -1.19 | -2.83 | 6 |
| final4 | MISO | january_2025 | 2.83 | -2.68 | -2.68 | -4.96 | 6 |
| final4 | NYIS | january_2025 | 1.99 | 1.52 | -0.02 | -0.12 | 5 |
| final4 | PJM | january_2025 | 2.13 | -1.41 | -1.67 | -3.83 | 6 |
| final4 | SWPP | january_2025 | 2.64 | -2.39 | -2.39 | -3.84 | 6 |
| final4 | TVA | january_2025 | 3.06 | -1.70 | -1.97 | -7.23 | 6 |
| final4_additive | BPAT | january_2025 | 3.13 | -3.47 | -3.96 | -5.55 | 6 |
| final4_additive | CISO | january_2025 | 3.46 | 2.03 | 0.00 | 0.00 | 6 |
| final4_additive | DUK | january_2025 | 4.14 | 1.37 | -0.83 | -5.01 | 6 |
| final4_additive | ERCO | january_2025 | 3.38 | -3.78 | -3.78 | -8.01 | 6 |
| final4_additive | FPL | january_2025 | 5.03 | -3.35 | -3.67 | -9.21 | 6 |
| final4_additive | ISNE | january_2025 | 3.43 | 0.05 | -1.05 | -3.20 | 6 |
| final4_additive | MISO | january_2025 | 2.92 | -2.45 | -2.51 | -4.71 | 6 |
| final4_additive | NYIS | january_2025 | 1.73 | -0.55 | -1.03 | -2.66 | 5 |
| final4_additive | PJM | january_2025 | 2.43 | 0.89 | -0.35 | -1.50 | 6 |
| final4_additive | SWPP | january_2025 | 3.53 | -3.65 | -3.65 | -6.13 | 6 |
| final4_additive | TVA | january_2025 | 3.79 | -1.37 | -2.27 | -6.67 | 6 |
| final4_boosting | BPAT | january_2025 | 3.34 | -5.87 | -5.89 | -8.91 | 6 |
| final4_boosting | CISO | january_2025 | 2.47 | 0.50 | -0.47 | -1.25 | 6 |
| final4_boosting | DUK | january_2025 | 4.22 | -2.83 | -2.83 | -8.85 | 6 |
| final4_boosting | ERCO | january_2025 | 3.46 | -6.00 | -6.00 | -7.46 | 6 |
| final4_boosting | FPL | january_2025 | 4.57 | -5.62 | -5.77 | -10.45 | 6 |
| final4_boosting | ISNE | january_2025 | 4.35 | -0.08 | -1.13 | -2.88 | 6 |
| final4_boosting | MISO | january_2025 | 2.69 | -3.26 | -3.26 | -5.06 | 6 |
| final4_boosting | NYIS | january_2025 | 2.75 | 0.99 | -0.34 | -1.28 | 5 |
| final4_boosting | PJM | january_2025 | 2.65 | -3.79 | -3.79 | -8.85 | 6 |
| final4_boosting | SWPP | january_2025 | 4.47 | -8.21 | -8.21 | -9.65 | 6 |
| final4_boosting | TVA | january_2025 | 2.91 | -2.34 | -2.43 | -5.80 | 6 |
| final4_ensemble | BPAT | january_2025 | 3.16 | -5.24 | -5.31 | -7.35 | 6 |
| final4_ensemble | CISO | january_2025 | 3.03 | 1.11 | -0.46 | -1.48 | 6 |
| final4_ensemble | DUK | january_2025 | 4.01 | -0.34 | -1.64 | -7.74 | 6 |
| final4_ensemble | ERCO | january_2025 | 3.20 | -5.41 | -5.41 | -7.45 | 6 |
| final4_ensemble | FPL | january_2025 | 4.24 | -4.26 | -4.26 | -9.62 | 6 |
| final4_ensemble | ISNE | january_2025 | 3.14 | 0.06 | -0.85 | -2.59 | 6 |
| final4_ensemble | MISO | january_2025 | 2.70 | -3.22 | -3.22 | -4.29 | 6 |
| final4_ensemble | NYIS | january_2025 | 1.25 | 0.18 | -0.35 | -0.88 | 5 |
| final4_ensemble | PJM | january_2025 | 2.28 | -1.72 | -1.86 | -4.00 | 6 |
| final4_ensemble | SWPP | january_2025 | 4.02 | -5.54 | -5.54 | -6.30 | 6 |
| final4_ensemble | TVA | january_2025 | 2.74 | -1.88 | -2.00 | -5.67 | 6 |
| final4_recency | BPAT | january_2025 | 3.27 | -6.31 | -6.31 | -8.11 | 6 |
| final4_recency | CISO | january_2025 | 5.72 | 0.91 | -2.66 | -5.17 | 6 |
| final4_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final4_recency | ERCO | january_2025 | 3.97 | -6.76 | -6.76 | -7.58 | 6 |
| final4_recency | FPL | january_2025 | 5.22 | -3.46 | -3.78 | -8.95 | 6 |
| final4_recency | ISNE | january_2025 | 3.79 | 0.28 | -0.90 | -4.07 | 6 |
| final4_recency | MISO | january_2025 | 3.41 | -4.01 | -4.01 | -5.00 | 6 |
| final4_recency | NYIS | january_2025 | 3.11 | -0.05 | -0.87 | -3.05 | 5 |
| final4_recency | PJM | january_2025 | 2.99 | -2.46 | -2.46 | -4.93 | 6 |
| final4_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.84 | 6 |
| final4_recency | TVA | january_2025 | 2.77 | -1.87 | -2.32 | -4.39 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final4 | eve | 3.03 | 0.95 | -1.27 | 0.49 | 322 |
| 10 | final4_ensemble | eve | 3.11 | -0.24 | -1.80 | 0.47 | 322 |
| 8 | final4_additive | eve | 3.18 | -0.21 | -1.92 | 0.44 | 322 |
| 6 | DF | eve | 3.30 | 0.52 | -1.35 |  | 322 |
| 9 | final4_boosting | eve | 3.34 | -0.16 | -1.79 | 0.43 | 322 |
| 11 | final4_recency | eve | 4.08 | -0.47 | -2.33 | 0.34 | 322 |
| 1 | final4 | special | 3.29 | -0.15 | -1.93 | 0.51 | 336 |
| 2 | final4_additive | special | 3.53 | -1.39 | -2.78 | 0.46 | 336 |
| 4 | final4_ensemble | special | 3.54 | -1.22 | -2.59 | 0.46 | 336 |
| 0 | DF | special | 3.56 | 0.06 | -1.69 |  | 336 |
| 3 | final4_boosting | special | 3.75 | -1.09 | -2.51 | 0.43 | 336 |
| 5 | final4_recency | special | 4.53 | -1.24 | -3.02 | 0.33 | 336 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final4 | all | 0.390 | 1.334 | 0.395 | 0.893 | 11.668 | 0.898 | 11448 |
| final4 | events | 0.434 | 1.801 | 0.659 | 0.818 | 12.938 | 0.792 | 130 |
| final4 | cold_mornings | 0.444 | 1.679 | 0.561 | 0.843 | 13.222 | 0.858 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final4 | BPAT | mape | 5.627 | 0.000 | 1081 |
| final4 | CISO | mape | -34.175 | 0.000 | 1044 |
| final4 | DUK | mape | 9.984 | 0.000 | 1070 |
| final4 | ERCO | mape | 0.072 | 0.943 | 1071 |
| final4 | FPL | mape | 2.116 | 0.034 | 1003 |
| final4 | ISNE | mape | 18.469 | 0.000 | 1069 |
| final4 | MISO | mape | -17.864 | 0.000 | 1084 |
| final4 | NYIS | mape | 0.089 | 0.929 | 1058 |
| final4 | PJM | mape | -7.355 | 0.000 | 1057 |
| final4 | SWPP | mape | -15.724 | 0.000 | 1066 |
| final4 | TVA | mape | 9.835 | 0.000 | 1076 |
| final4_additive | BPAT | mape | 9.697 | 0.000 | 1081 |
| final4_additive | CISO | mape | -18.119 | 0.000 | 1044 |
| final4_additive | DUK | mape | 12.113 | 0.000 | 1070 |
| final4_additive | ERCO | mape | 14.249 | 0.000 | 1071 |
| final4_additive | FPL | mape | 22.465 | 0.000 | 1003 |
| final4_additive | ISNE | mape | 23.228 | 0.000 | 1069 |
| final4_additive | MISO | mape | -10.085 | 0.000 | 1084 |
| final4_additive | NYIS | mape | 4.110 | 0.000 | 1058 |
| final4_additive | PJM | mape | 1.557 | 0.119 | 1057 |
| final4_additive | SWPP | mape | -14.460 | 0.000 | 1066 |
| final4_additive | TVA | mape | 14.208 | 0.000 | 1076 |
| final4_boosting | BPAT | mape | 11.906 | 0.000 | 1081 |
| final4_boosting | CISO | mape | -26.768 | 0.000 | 1044 |
| final4_boosting | DUK | mape | 12.239 | 0.000 | 1070 |
| final4_boosting | ERCO | mape | 8.539 | 0.000 | 1071 |
| final4_boosting | FPL | mape | 25.464 | 0.000 | 1003 |
| final4_boosting | ISNE | mape | 20.444 | 0.000 | 1069 |
| final4_boosting | MISO | mape | -12.487 | 0.000 | 1084 |
| final4_boosting | NYIS | mape | 4.135 | 0.000 | 1058 |
| final4_boosting | PJM | mape | 3.667 | 0.000 | 1057 |
| final4_boosting | SWPP | mape | -11.781 | 0.000 | 1066 |
| final4_boosting | TVA | mape | 15.127 | 0.000 | 1076 |
| final4_ensemble | BPAT | mape | 7.147 | 0.000 | 1081 |
| final4_ensemble | CISO | mape | -24.156 | 0.000 | 1044 |
| final4_ensemble | DUK | mape | 10.237 | 0.000 | 1070 |
| final4_ensemble | ERCO | mape | 9.602 | 0.000 | 1071 |
| final4_ensemble | FPL | mape | 23.417 | 0.000 | 1003 |
| final4_ensemble | ISNE | mape | 21.096 | 0.000 | 1069 |
| final4_ensemble | MISO | mape | -13.150 | 0.000 | 1084 |
| final4_ensemble | NYIS | mape | 1.701 | 0.089 | 1058 |
| final4_ensemble | PJM | mape | -2.744 | 0.006 | 1057 |
| final4_ensemble | SWPP | mape | -15.103 | 0.000 | 1066 |
| final4_ensemble | TVA | mape | 12.384 | 0.000 | 1076 |
| final4_recency | BPAT | mape | 18.198 | 0.000 | 1081 |
| final4_recency | CISO | mape | -3.852 | 0.000 | 1044 |
| final4_recency | DUK | mape | 19.470 | 0.000 | 1070 |
| final4_recency | ERCO | mape | 17.844 | 0.000 | 1071 |
| final4_recency | FPL | mape | 32.918 | 0.000 | 1003 |
| final4_recency | ISNE | mape | 44.406 | 0.000 | 1069 |
| final4_recency | MISO | mape | 0.344 | 0.731 | 1084 |
| final4_recency | NYIS | mape | 21.581 | 0.000 | 1058 |
| final4_recency | PJM | mape | 11.820 | 0.000 | 1057 |
| final4_recency | SWPP | mape | -9.941 | 0.000 | 1066 |
| final4_recency | TVA | mape | 21.905 | 0.000 | 1076 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final4 | 0.991 |
| final4_additive | 0.969 |
| final4_boosting | 0.991 |
| final4_ensemble | 0.991 |
| final4_recency | 0.991 |
