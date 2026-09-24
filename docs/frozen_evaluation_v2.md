# Second look at 2023 to 2025: the recipe after phase G, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase G on 2023 to 2025 under protocol v2. This is a second look at these years: the choices of phase G were made on the development period, but the frozen run of `final2` had already been seen; the honest reading compares this table with `docs/frozen_evaluation.md` and treats the difference as an estimate, not a proof.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | 2.44 | 2.10 | 0.04 | -1.34 | 1.24 | 0.57 | 0.30 | -35.37 | 11679 | 11.00 |
| final3_ensemble | 2.76 | 2.42 | -1.11 | -2.07 | 1.25 | 0.51 | 0.24 | -40.43 | 11679 | 11.00 |
| final3_additive | 2.89 | 2.52 | -1.01 | -2.12 | 1.26 | 0.48 | 0.24 | -40.44 | 11679 | 11.00 |
| DF | 2.90 | 2.50 | 0.31 | -1.10 | 0.98 | 0.00 | 0.00 | -41.79 | 11679 | 11.00 |
| final3_boosting | 2.91 | 2.58 | -1.03 | -2.08 | 1.45 | 0.46 | 0.24 | -38.96 | 11679 | 11.00 |
| final3_recency | 3.53 | 3.20 | -1.34 | -2.50 | 1.57 | 0.36 | 0.22 | -42.33 | 11679 | 11.00 |

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
| final3 | BPAT | 2.25 | 1.99 | -0.09 | -1.24 | 1.44 | -16.37 | 0.43 | 0.40 | 1081 | 6762.61 |
| final3 | CISO | 2.76 | 2.53 | -0.26 | -1.55 | 1.05 | -15.23 | 0.87 | 0.40 | 1044 | 25453.81 |
| final3 | DUK | 3.34 | 2.79 | 0.48 | -1.84 | 1.34 | -15.01 | 0.37 | 0.27 | 1070 | 12295.77 |
| final3 | ERCO | 2.46 | 2.08 | -0.04 | -1.48 | 0.94 | -16.62 | 0.46 | 0.21 | 1071 | 53336.07 |
| final3 | FPL | 3.44 | 2.97 | 0.57 | -1.66 | 1.05 | -35.37 | 0.51 | 0.39 | 1003 | 16583.18 |
| final3 | ISNE | 3.83 | 3.33 | 0.19 | -1.35 | 0.46 | -22.15 | 0.30 | 0.20 | 1069 | 12999.48 |
| final3 | MISO | 1.89 | 1.65 | 0.09 | -1.00 | 1.53 | -7.74 | 0.69 | 0.08 | 1084 | 74014.33 |
| final3 | NYIS | 2.72 | 2.38 | 0.07 | -1.26 | 0.66 | -17.44 | 0.49 | 0.74 | 1058 | 17111.01 |
| final3 | PJM | 2.16 | 1.89 | 0.06 | -1.23 | 1.27 | -10.24 | 0.60 | 0.40 | 1057 | 93208.59 |
| final3 | SWPP | 2.45 | 1.89 | -0.27 | -1.48 | 1.70 | -22.81 | 0.60 | 0.34 | 1066 | 33074.81 |
| final3 | TVA | 2.91 | 2.50 | -0.03 | -1.72 | 1.38 | -14.29 | 0.34 | 0.22 | 1076 | 18806.27 |
| final3_additive | BPAT | 2.45 | 2.14 | -1.29 | -1.98 | 1.52 | -16.50 | 0.38 | 0.29 | 1081 | 6762.61 |
| final3_additive | CISO | 3.83 | 3.42 | -2.66 | -3.54 | 1.21 | -20.57 | 0.75 | 0.30 | 1044 | 25453.81 |
| final3_additive | DUK | 3.54 | 2.94 | -0.60 | -2.44 | 1.35 | -17.10 | 0.32 | 0.21 | 1070 | 12295.77 |
| final3_additive | ERCO | 3.08 | 2.72 | -1.74 | -2.53 | 0.94 | -18.16 | 0.33 | 0.13 | 1071 | 53336.07 |
| final3_additive | FPL | 4.96 | 4.59 | -4.68 | -5.28 | 0.99 | -40.44 | 0.27 | 0.11 | 1003 | 16583.18 |
| final3_additive | ISNE | 4.16 | 3.65 | -0.82 | -2.25 | 0.59 | -20.50 | 0.24 | 0.16 | 1069 | 12999.48 |
| final3_additive | MISO | 2.19 | 1.93 | -0.70 | -1.53 | 1.57 | -9.86 | 0.62 | 0.06 | 1084 | 74014.33 |
| final3_additive | NYIS | 2.91 | 2.55 | -1.01 | -2.02 | 0.59 | -18.41 | 0.46 | 0.64 | 1058 | 17111.01 |
| final3_additive | PJM | 2.47 | 2.16 | -0.28 | -1.55 | 1.28 | -11.98 | 0.52 | 0.36 | 1057 | 93208.59 |
| final3_additive | SWPP | 2.69 | 2.13 | -0.65 | -1.92 | 1.65 | -21.92 | 0.55 | 0.28 | 1066 | 33074.81 |
| final3_additive | TVA | 3.27 | 2.79 | 0.73 | -1.55 | 1.31 | -16.52 | 0.27 | 0.25 | 1076 | 18806.27 |
| final3_boosting | BPAT | 2.55 | 2.21 | -0.66 | -1.74 | 1.56 | -17.77 | 0.34 | 0.34 | 1081 | 6762.61 |
| final3_boosting | CISO | 3.15 | 2.82 | -2.07 | -2.73 | 1.17 | -14.28 | 0.81 | 0.31 | 1044 | 25453.81 |
| final3_boosting | DUK | 3.50 | 2.99 | -0.91 | -2.55 | 1.48 | -17.84 | 0.33 | 0.21 | 1070 | 12295.77 |
| final3_boosting | ERCO | 2.91 | 2.61 | -1.78 | -2.54 | 1.15 | -17.41 | 0.35 | 0.13 | 1071 | 53336.07 |
| final3_boosting | FPL | 5.42 | 5.19 | -5.51 | -5.84 | 1.36 | -38.96 | 0.19 | 0.08 | 1003 | 16583.18 |
| final3_boosting | ISNE | 4.06 | 3.53 | -0.96 | -2.05 | 0.56 | -19.19 | 0.25 | 0.16 | 1069 | 12999.48 |
| final3_boosting | MISO | 2.15 | 1.99 | -0.65 | -1.45 | 1.61 | -11.22 | 0.64 | 0.06 | 1084 | 74014.33 |
| final3_boosting | NYIS | 2.97 | 2.58 | -0.78 | -1.70 | 0.77 | -15.43 | 0.43 | 0.66 | 1058 | 17111.01 |
| final3_boosting | PJM | 2.67 | 2.40 | -0.27 | -1.57 | 1.69 | -11.68 | 0.43 | 0.37 | 1057 | 93208.59 |
| final3_boosting | SWPP | 3.02 | 2.31 | -0.64 | -2.04 | 1.84 | -21.72 | 0.51 | 0.27 | 1066 | 33074.81 |
| final3_boosting | TVA | 3.23 | 2.79 | 0.06 | -1.85 | 1.49 | -14.45 | 0.26 | 0.22 | 1076 | 18806.27 |
| final3_ensemble | BPAT | 2.31 | 2.07 | -1.31 | -1.95 | 1.44 | -16.55 | 0.41 | 0.30 | 1081 | 6762.61 |
| final3_ensemble | CISO | 3.37 | 2.95 | -2.40 | -3.15 | 1.26 | -16.59 | 0.79 | 0.31 | 1044 | 25453.81 |
| final3_ensemble | DUK | 3.39 | 2.81 | -0.75 | -2.46 | 1.33 | -16.39 | 0.35 | 0.21 | 1070 | 12295.77 |
| final3_ensemble | ERCO | 2.94 | 2.59 | -1.98 | -2.63 | 0.97 | -17.18 | 0.36 | 0.12 | 1071 | 53336.07 |
| final3_ensemble | FPL | 5.09 | 4.82 | -5.24 | -5.62 | 1.02 | -40.43 | 0.24 | 0.09 | 1003 | 16583.18 |
| final3_ensemble | ISNE | 4.02 | 3.53 | -1.13 | -2.14 | 0.54 | -20.39 | 0.25 | 0.14 | 1069 | 12999.48 |
| final3_ensemble | MISO | 2.08 | 1.88 | -0.74 | -1.45 | 1.45 | -9.48 | 0.65 | 0.06 | 1084 | 74014.33 |
| final3_ensemble | NYIS | 2.81 | 2.47 | -1.01 | -1.84 | 0.65 | -15.51 | 0.48 | 0.65 | 1058 | 17111.01 |
| final3_ensemble | PJM | 2.35 | 2.07 | -0.27 | -1.41 | 1.32 | -11.68 | 0.55 | 0.38 | 1057 | 93208.59 |
| final3_ensemble | SWPP | 2.62 | 2.07 | -0.87 | -2.00 | 1.65 | -22.14 | 0.56 | 0.27 | 1066 | 33074.81 |
| final3_ensemble | TVA | 3.14 | 2.64 | 0.39 | -1.61 | 1.28 | -14.86 | 0.30 | 0.23 | 1076 | 18806.27 |
| final3_recency | BPAT | 2.88 | 2.60 | -2.10 | -2.58 | 1.69 | -15.57 | 0.26 | 0.23 | 1081 | 6762.61 |
| final3_recency | CISO | 5.02 | 4.73 | -2.72 | -3.89 | 1.58 | -23.26 | 0.57 | 0.30 | 1044 | 25453.81 |
| final3_recency | DUK | 3.97 | 3.44 | -0.74 | -2.75 | 1.47 | -17.72 | 0.26 | 0.21 | 1070 | 12295.77 |
| final3_recency | ERCO | 3.56 | 3.24 | -2.50 | -3.22 | 1.18 | -19.88 | 0.25 | 0.11 | 1071 | 53336.07 |
| final3_recency | FPL | 6.17 | 5.75 | -5.74 | -6.30 | 1.17 | -42.33 | 0.13 | 0.10 | 1003 | 16583.18 |
| final3_recency | ISNE | 6.18 | 5.72 | -1.86 | -2.82 | 0.75 | -23.61 | 0.05 | 0.14 | 1069 | 12999.48 |
| final3_recency | MISO | 2.74 | 2.49 | -0.84 | -1.74 | 1.98 | -11.52 | 0.51 | 0.07 | 1084 | 74014.33 |
| final3_recency | NYIS | 4.16 | 3.84 | -1.39 | -2.43 | 0.94 | -13.78 | 0.24 | 0.55 | 1058 | 17111.01 |
| final3_recency | PJM | 2.91 | 2.68 | -0.21 | -1.70 | 1.71 | -12.59 | 0.36 | 0.35 | 1057 | 93208.59 |
| final3_recency | SWPP | 3.03 | 2.46 | -1.36 | -2.49 | 1.76 | -22.90 | 0.49 | 0.23 | 1066 | 33074.81 |
| final3_recency | TVA | 3.63 | 3.05 | 0.40 | -1.79 | 1.54 | -14.70 | 0.21 | 0.23 | 1076 | 18806.27 |

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
| final3 | BPAT | gerri_heather | 5.18 | -4.75 | -4.75 | -12.13 | 6 |
| final3 | CISO | gerri_heather | 2.69 | 1.08 | -0.40 | -2.27 | 6 |
| final3 | DUK | gerri_heather | 5.81 | -5.87 | -5.87 | -9.23 | 6 |
| final3 | ERCO | gerri_heather | 6.25 | -7.77 | -7.77 | -13.30 | 6 |
| final3 | FPL | gerri_heather | 4.77 | -5.17 | -5.58 | -9.75 | 6 |
| final3 | ISNE | gerri_heather | 3.78 | -0.26 | -1.38 | -5.47 | 6 |
| final3 | MISO | gerri_heather | 2.98 | -2.15 | -2.56 | -4.79 | 6 |
| final3 | NYIS | gerri_heather | 1.79 | 0.04 | -0.76 | -2.10 | 5 |
| final3 | PJM | gerri_heather | 2.85 | -0.24 | -1.17 | -3.81 | 6 |
| final3 | SWPP | gerri_heather | 5.47 | -5.42 | -5.42 | -13.96 | 6 |
| final3 | TVA | gerri_heather | 3.13 | -0.30 | -1.43 | -5.75 | 6 |
| final3_additive | BPAT | gerri_heather | 6.37 | -6.20 | -6.37 | -16.50 | 6 |
| final3_additive | CISO | gerri_heather | 2.97 | 1.78 | -0.23 | -1.14 | 6 |
| final3_additive | DUK | gerri_heather | 5.92 | -7.33 | -7.33 | -15.52 | 6 |
| final3_additive | ERCO | gerri_heather | 7.99 | -9.83 | -9.83 | -16.86 | 6 |
| final3_additive | FPL | gerri_heather | 6.20 | -7.54 | -7.54 | -13.25 | 6 |
| final3_additive | ISNE | gerri_heather | 4.00 | 0.04 | -1.84 | -6.05 | 6 |
| final3_additive | MISO | gerri_heather | 3.01 | -2.49 | -2.67 | -4.06 | 6 |
| final3_additive | NYIS | gerri_heather | 1.80 | -1.05 | -1.48 | -3.10 | 5 |
| final3_additive | PJM | gerri_heather | 2.82 | 1.45 | -0.25 | -1.13 | 6 |
| final3_additive | SWPP | gerri_heather | 7.06 | -7.68 | -7.68 | -18.06 | 6 |
| final3_additive | TVA | gerri_heather | 3.29 | 1.78 | -1.10 | -6.45 | 6 |
| final3_boosting | BPAT | gerri_heather | 6.64 | -7.67 | -7.67 | -13.59 | 6 |
| final3_boosting | CISO | gerri_heather | 2.93 | 1.62 | -0.48 | -2.86 | 6 |
| final3_boosting | DUK | gerri_heather | 5.75 | -6.18 | -6.52 | -12.16 | 6 |
| final3_boosting | ERCO | gerri_heather | 5.81 | -9.80 | -9.80 | -17.25 | 6 |
| final3_boosting | FPL | gerri_heather | 5.68 | -8.78 | -8.78 | -13.39 | 6 |
| final3_boosting | ISNE | gerri_heather | 3.76 | 0.34 | -0.96 | -4.63 | 6 |
| final3_boosting | MISO | gerri_heather | 2.29 | -2.09 | -2.84 | -5.63 | 6 |
| final3_boosting | NYIS | gerri_heather | 2.15 | 1.37 | -0.24 | -1.19 | 5 |
| final3_boosting | PJM | gerri_heather | 2.77 | -0.14 | -1.32 | -3.77 | 6 |
| final3_boosting | SWPP | gerri_heather | 5.51 | -6.72 | -6.72 | -12.29 | 6 |
| final3_boosting | TVA | gerri_heather | 3.67 | -0.80 | -2.76 | -9.70 | 6 |
| final3_ensemble | BPAT | gerri_heather | 5.61 | -5.91 | -5.91 | -13.48 | 6 |
| final3_ensemble | CISO | gerri_heather | 2.71 | 1.78 | -0.45 | -2.73 | 6 |
| final3_ensemble | DUK | gerri_heather | 5.86 | -7.13 | -7.13 | -14.37 | 6 |
| final3_ensemble | ERCO | gerri_heather | 6.15 | -8.50 | -8.50 | -12.11 | 6 |
| final3_ensemble | FPL | gerri_heather | 6.03 | -8.28 | -8.28 | -12.77 | 6 |
| final3_ensemble | ISNE | gerri_heather | 3.93 | 0.02 | -1.42 | -5.74 | 6 |
| final3_ensemble | MISO | gerri_heather | 2.71 | -2.25 | -2.73 | -5.48 | 6 |
| final3_ensemble | NYIS | gerri_heather | 1.86 | -0.04 | -0.47 | -1.61 | 5 |
| final3_ensemble | PJM | gerri_heather | 2.61 | 0.66 | -0.74 | -2.65 | 6 |
| final3_ensemble | SWPP | gerri_heather | 6.77 | -7.69 | -7.69 | -15.92 | 6 |
| final3_ensemble | TVA | gerri_heather | 3.01 | 1.17 | -1.13 | -5.55 | 6 |
| final3_recency | BPAT | gerri_heather | 4.95 | -3.60 | -3.93 | -10.22 | 6 |
| final3_recency | CISO | gerri_heather | 3.52 | 2.00 | -0.72 | -4.31 | 6 |
| final3_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final3_recency | ERCO | gerri_heather | 5.53 | -5.59 | -5.89 | -10.83 | 6 |
| final3_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final3_recency | ISNE | gerri_heather | 5.43 | -0.43 | -1.75 | -6.86 | 6 |
| final3_recency | MISO | gerri_heather | 3.32 | -2.10 | -2.68 | -7.06 | 6 |
| final3_recency | NYIS | gerri_heather | 3.53 | -0.64 | -0.83 | -2.57 | 5 |
| final3_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final3_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| final3_recency | TVA | gerri_heather | 4.68 | 2.89 | -1.21 | -7.25 | 6 |
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
| final3 | BPAT | january_2025 | 2.59 | -3.10 | -3.53 | -4.83 | 6 |
| final3 | CISO | january_2025 | 1.88 | 0.62 | -0.01 | -0.06 | 6 |
| final3 | DUK | january_2025 | 4.39 | 0.69 | -1.56 | -6.49 | 6 |
| final3 | ERCO | january_2025 | 3.18 | -4.10 | -4.10 | -7.42 | 6 |
| final3 | FPL | january_2025 | 5.49 | -6.12 | -6.12 | -12.66 | 6 |
| final3 | ISNE | january_2025 | 3.89 | -0.37 | -1.16 | -2.80 | 6 |
| final3 | MISO | january_2025 | 2.70 | -2.57 | -2.57 | -4.82 | 6 |
| final3 | NYIS | january_2025 | 2.04 | 1.47 | -0.02 | -0.12 | 5 |
| final3 | PJM | january_2025 | 2.08 | -1.35 | -1.59 | -3.31 | 6 |
| final3 | SWPP | january_2025 | 2.56 | -2.19 | -2.19 | -3.75 | 6 |
| final3 | TVA | january_2025 | 3.03 | -1.69 | -1.93 | -7.21 | 6 |
| final3_additive | BPAT | january_2025 | 3.13 | -3.48 | -3.97 | -5.57 | 6 |
| final3_additive | CISO | january_2025 | 3.47 | 1.91 | 0.00 | 0.00 | 6 |
| final3_additive | DUK | january_2025 | 4.08 | 1.23 | -0.85 | -5.06 | 6 |
| final3_additive | ERCO | january_2025 | 3.27 | -3.81 | -3.81 | -7.91 | 6 |
| final3_additive | FPL | january_2025 | 4.73 | -3.66 | -3.87 | -9.69 | 6 |
| final3_additive | ISNE | january_2025 | 3.42 | 0.02 | -1.08 | -3.27 | 6 |
| final3_additive | MISO | january_2025 | 2.91 | -2.38 | -2.46 | -4.67 | 6 |
| final3_additive | NYIS | january_2025 | 1.72 | -0.51 | -0.99 | -2.50 | 5 |
| final3_additive | PJM | january_2025 | 2.45 | 0.88 | -0.35 | -1.52 | 6 |
| final3_additive | SWPP | january_2025 | 3.56 | -3.63 | -3.63 | -6.14 | 6 |
| final3_additive | TVA | january_2025 | 3.73 | -1.35 | -2.27 | -6.75 | 6 |
| final3_boosting | BPAT | january_2025 | 3.58 | -5.93 | -5.95 | -8.26 | 6 |
| final3_boosting | CISO | january_2025 | 2.33 | 0.38 | -0.51 | -1.49 | 6 |
| final3_boosting | DUK | january_2025 | 4.24 | -1.96 | -2.52 | -7.69 | 6 |
| final3_boosting | ERCO | january_2025 | 3.58 | -5.93 | -5.93 | -7.15 | 6 |
| final3_boosting | FPL | january_2025 | 4.78 | -7.41 | -7.41 | -12.98 | 6 |
| final3_boosting | ISNE | january_2025 | 4.24 | -0.06 | -1.31 | -3.32 | 6 |
| final3_boosting | MISO | january_2025 | 2.48 | -2.85 | -2.85 | -4.46 | 6 |
| final3_boosting | NYIS | january_2025 | 2.83 | 0.80 | -0.40 | -1.31 | 5 |
| final3_boosting | PJM | january_2025 | 2.44 | -3.99 | -3.99 | -8.00 | 6 |
| final3_boosting | SWPP | january_2025 | 4.24 | -7.82 | -7.82 | -9.07 | 6 |
| final3_boosting | TVA | january_2025 | 2.91 | -2.33 | -2.46 | -6.14 | 6 |
| final3_ensemble | BPAT | january_2025 | 3.23 | -5.26 | -5.33 | -7.12 | 6 |
| final3_ensemble | CISO | january_2025 | 2.98 | 1.02 | -0.50 | -1.51 | 6 |
| final3_ensemble | DUK | january_2025 | 4.02 | -0.07 | -1.62 | -7.35 | 6 |
| final3_ensemble | ERCO | january_2025 | 3.21 | -5.37 | -5.37 | -7.32 | 6 |
| final3_ensemble | FPL | january_2025 | 4.24 | -5.04 | -5.04 | -10.74 | 6 |
| final3_ensemble | ISNE | january_2025 | 3.15 | 0.06 | -0.86 | -2.62 | 6 |
| final3_ensemble | MISO | january_2025 | 2.58 | -3.04 | -3.04 | -4.26 | 6 |
| final3_ensemble | NYIS | january_2025 | 1.26 | 0.12 | -0.35 | -0.89 | 5 |
| final3_ensemble | PJM | january_2025 | 2.20 | -1.73 | -1.85 | -3.61 | 6 |
| final3_ensemble | SWPP | january_2025 | 3.93 | -5.43 | -5.43 | -6.12 | 6 |
| final3_ensemble | TVA | january_2025 | 2.68 | -1.86 | -1.93 | -5.81 | 6 |
| final3_recency | BPAT | january_2025 | 3.27 | -6.31 | -6.31 | -8.11 | 6 |
| final3_recency | CISO | january_2025 | 5.72 | 0.91 | -2.66 | -5.17 | 6 |
| final3_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final3_recency | ERCO | january_2025 | 3.97 | -6.76 | -6.76 | -7.58 | 6 |
| final3_recency | FPL | january_2025 | 5.22 | -3.46 | -3.78 | -8.95 | 6 |
| final3_recency | ISNE | january_2025 | 3.79 | 0.28 | -0.90 | -4.07 | 6 |
| final3_recency | MISO | january_2025 | 3.41 | -4.01 | -4.01 | -5.00 | 6 |
| final3_recency | NYIS | january_2025 | 3.11 | -0.05 | -0.87 | -3.05 | 5 |
| final3_recency | PJM | january_2025 | 2.99 | -2.46 | -2.46 | -4.93 | 6 |
| final3_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.84 | 6 |
| final3_recency | TVA | january_2025 | 2.77 | -1.87 | -2.32 | -4.39 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final3 | eve | 3.13 | 1.06 | -1.30 | 0.49 | 322 |
| 10 | final3_ensemble | eve | 3.22 | -0.13 | -1.85 | 0.46 | 322 |
| 8 | final3_additive | eve | 3.26 | 0.03 | -1.89 | 0.42 | 322 |
| 6 | DF | eve | 3.30 | 0.52 | -1.35 |  | 322 |
| 9 | final3_boosting | eve | 3.47 | -0.12 | -1.86 | 0.40 | 322 |
| 11 | final3_recency | eve | 4.08 | -0.47 | -2.33 | 0.34 | 322 |
| 1 | final3 | special | 3.32 | -0.03 | -1.89 | 0.50 | 336 |
| 0 | DF | special | 3.56 | 0.06 | -1.69 |  | 336 |
| 2 | final3_additive | special | 3.60 | -1.23 | -2.76 | 0.45 | 336 |
| 4 | final3_ensemble | special | 3.60 | -1.12 | -2.61 | 0.47 | 336 |
| 3 | final3_boosting | special | 3.80 | -1.00 | -2.52 | 0.40 | 336 |
| 5 | final3_recency | special | 4.53 | -1.24 | -3.02 | 0.33 | 336 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | all | 0.395 | 1.372 | 0.410 | 0.892 | 12.081 | 0.896 | 11448 |
| final3 | events | 0.437 | 1.797 | 0.654 | 0.821 | 13.100 | 0.808 | 130 |
| final3 | cold_mornings | 0.444 | 1.674 | 0.560 | 0.845 | 13.282 | 0.867 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3 | BPAT | mape | 5.760 | 0.000 | 1081 |
| final3 | CISO | mape | -34.358 | 0.000 | 1044 |
| final3 | DUK | mape | 11.742 | 0.000 | 1070 |
| final3 | ERCO | mape | 1.226 | 0.220 | 1071 |
| final3 | FPL | mape | 4.027 | 0.000 | 1003 |
| final3 | ISNE | mape | 19.358 | 0.000 | 1069 |
| final3 | MISO | mape | -16.593 | 0.000 | 1084 |
| final3 | NYIS | mape | 1.612 | 0.107 | 1058 |
| final3 | PJM | mape | -5.928 | 0.000 | 1057 |
| final3 | SWPP | mape | -15.299 | 0.000 | 1066 |
| final3 | TVA | mape | 12.567 | 0.000 | 1076 |
| final3_additive | BPAT | mape | 9.933 | 0.000 | 1081 |
| final3_additive | CISO | mape | -18.191 | 0.000 | 1044 |
| final3_additive | DUK | mape | 14.076 | 0.000 | 1070 |
| final3_additive | ERCO | mape | 11.406 | 0.000 | 1071 |
| final3_additive | FPL | mape | 22.486 | 0.000 | 1003 |
| final3_additive | ISNE | mape | 23.328 | 0.000 | 1069 |
| final3_additive | MISO | mape | -10.150 | 0.000 | 1084 |
| final3_additive | NYIS | mape | 4.770 | 0.000 | 1058 |
| final3_additive | PJM | mape | 1.668 | 0.095 | 1057 |
| final3_additive | SWPP | mape | -12.972 | 0.000 | 1066 |
| final3_additive | TVA | mape | 18.370 | 0.000 | 1076 |
| final3_boosting | BPAT | mape | 12.293 | 0.000 | 1081 |
| final3_boosting | CISO | mape | -27.354 | 0.000 | 1044 |
| final3_boosting | DUK | mape | 14.165 | 0.000 | 1070 |
| final3_boosting | ERCO | mape | 9.142 | 0.000 | 1071 |
| final3_boosting | FPL | mape | 28.931 | 0.000 | 1003 |
| final3_boosting | ISNE | mape | 22.374 | 0.000 | 1069 |
| final3_boosting | MISO | mape | -11.077 | 0.000 | 1084 |
| final3_boosting | NYIS | mape | 5.818 | 0.000 | 1058 |
| final3_boosting | PJM | mape | 6.270 | 0.000 | 1057 |
| final3_boosting | SWPP | mape | -10.692 | 0.000 | 1066 |
| final3_boosting | TVA | mape | 17.773 | 0.000 | 1076 |
| final3_ensemble | BPAT | mape | 7.343 | 0.000 | 1081 |
| final3_ensemble | CISO | mape | -24.493 | 0.000 | 1044 |
| final3_ensemble | DUK | mape | 12.238 | 0.000 | 1070 |
| final3_ensemble | ERCO | mape | 9.310 | 0.000 | 1071 |
| final3_ensemble | FPL | mape | 24.184 | 0.000 | 1003 |
| final3_ensemble | ISNE | mape | 22.338 | 0.000 | 1069 |
| final3_ensemble | MISO | mape | -12.336 | 0.000 | 1084 |
| final3_ensemble | NYIS | mape | 3.191 | 0.001 | 1058 |
| final3_ensemble | PJM | mape | -1.238 | 0.216 | 1057 |
| final3_ensemble | SWPP | mape | -13.834 | 0.000 | 1066 |
| final3_ensemble | TVA | mape | 16.045 | 0.000 | 1076 |
| final3_recency | BPAT | mape | 18.198 | 0.000 | 1081 |
| final3_recency | CISO | mape | -3.852 | 0.000 | 1044 |
| final3_recency | DUK | mape | 19.470 | 0.000 | 1070 |
| final3_recency | ERCO | mape | 17.844 | 0.000 | 1071 |
| final3_recency | FPL | mape | 32.918 | 0.000 | 1003 |
| final3_recency | ISNE | mape | 44.406 | 0.000 | 1069 |
| final3_recency | MISO | mape | 0.344 | 0.731 | 1084 |
| final3_recency | NYIS | mape | 21.581 | 0.000 | 1058 |
| final3_recency | PJM | mape | 11.820 | 0.000 | 1057 |
| final3_recency | SWPP | mape | -9.941 | 0.000 | 1066 |
| final3_recency | TVA | mape | 21.905 | 0.000 | 1076 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final3 | 0.991 |
| final3_additive | 0.969 |
| final3_boosting | 0.991 |
| final3_ensemble | 0.991 |
| final3_recency | 0.991 |
