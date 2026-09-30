# Sixth look at 2023 to 2025: the recipe after phase N, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase N (`final8q`: HRRR, NBM and GFS weighted per station by their recent error, the GFS left out on days below the station's cold decile) on 2023 to 2025 under protocol v2. A sixth look at these years: compare with `docs/frozen_evaluation_v5.md` (same days, same rules) and read the difference as an estimate.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8q | 2.20 | 1.90 | -0.05 | -1.18 | 1.11 | 0.63 | 0.30 | -39.02 | 11700 | 11.00 |
| final8q_ensemble | 2.37 | 2.10 | -1.72 | -2.20 | 1.10 | 0.59 | 0.18 | -40.27 | 11700 | 11.00 |
| final8q_boosting | 2.44 | 2.13 | -1.61 | -2.17 | 1.25 | 0.56 | 0.20 | -41.52 | 11700 | 11.00 |
| final8q_additive | 2.61 | 2.32 | -1.73 | -2.38 | 1.18 | 0.54 | 0.19 | -39.18 | 11700 | 11.00 |
| DF | 2.90 | 2.50 | 0.31 | -1.10 | 0.98 | 0.00 | 0.00 | -41.79 | 11700 | 11.00 |
| final8q_recency | 3.18 | 2.85 | -1.91 | -2.58 | 1.45 | 0.41 | 0.17 | -39.99 | 11700 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.00 | 1.80 | -0.38 | -1.20 | 1.24 | -15.51 |  |  | 1081 | 6762.61 |
| DF | CISO | 5.36 | 5.12 | -1.74 | -2.63 | 1.20 | -33.79 |  |  | 1044 | 25453.81 |
| DF | DUK | 2.65 | 2.31 | 0.43 | -1.26 | 1.02 | -13.08 |  |  | 1075 | 12295.45 |
| DF | ERCO | 2.40 | 1.99 | 0.79 | -0.80 | 1.01 | -11.36 |  |  | 1071 | 53336.07 |
| DF | FPL | 3.21 | 3.06 | -0.60 | -1.71 | 1.13 | -41.79 |  |  | 1007 | 16591.11 |
| DF | ISNE | 2.56 | 2.51 | 0.39 | -0.45 | 0.33 | -5.42 |  |  | 1073 | 13001.44 |
| DF | MISO | 2.72 | 2.51 | 2.03 | -0.22 | 0.85 | -6.54 |  |  | 1084 | 74014.33 |
| DF | NYIS | 2.62 | 2.46 | -2.43 | -2.58 | 0.43 | -10.12 |  |  | 1062 | 17115.05 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1061 | 93218.11 |
| DF | SWPP | 4.33 | 2.46 | 1.42 | -1.38 | 1.49 | -17.10 |  |  | 1066 | 33074.81 |
| DF | TVA | 2.28 | 1.96 | 0.57 | -0.89 | 1.00 | -8.44 |  |  | 1076 | 18806.27 |
| final8q | BPAT | 2.10 | 1.87 | -0.21 | -1.21 | 1.42 | -16.59 | 0.48 | 0.38 | 1081 | 6762.61 |
| final8q | CISO | 2.62 | 2.41 | -0.35 | -1.46 | 1.05 | -15.45 | 0.90 | 0.39 | 1044 | 25453.81 |
| final8q | DUK | 2.76 | 2.32 | 0.37 | -1.45 | 1.12 | -12.57 | 0.47 | 0.27 | 1075 | 12295.45 |
| final8q | ERCO | 2.21 | 1.87 | 0.05 | -1.20 | 0.87 | -16.19 | 0.54 | 0.23 | 1071 | 53336.07 |
| final8q | FPL | 3.10 | 2.65 | 0.54 | -1.32 | 0.93 | -39.02 | 0.60 | 0.43 | 1007 | 16591.11 |
| final8q | ISNE | 3.52 | 3.19 | -0.01 | -1.27 | 0.52 | -19.45 | 0.33 | 0.19 | 1073 | 13001.44 |
| final8q | MISO | 1.74 | 1.52 | -0.01 | -0.90 | 1.29 | -6.79 | 0.73 | 0.08 | 1084 | 74014.33 |
| final8q | NYIS | 2.47 | 2.13 | -0.05 | -1.17 | 0.60 | -18.33 | 0.54 | 0.75 | 1062 | 17115.05 |
| final8q | PJM | 1.93 | 1.66 | -0.15 | -1.13 | 1.12 | -10.32 | 0.67 | 0.41 | 1061 | 93218.11 |
| final8q | SWPP | 2.30 | 1.78 | -0.22 | -1.33 | 1.55 | -22.69 | 0.62 | 0.35 | 1066 | 33074.81 |
| final8q | TVA | 2.39 | 2.05 | -0.11 | -1.38 | 1.23 | -11.92 | 0.44 | 0.19 | 1076 | 18806.27 |
| final8q_additive | BPAT | 2.33 | 2.05 | -1.76 | -2.24 | 1.42 | -17.09 | 0.40 | 0.24 | 1081 | 6762.61 |
| final8q_additive | CISO | 2.98 | 2.74 | -1.64 | -2.37 | 1.14 | -20.80 | 0.87 | 0.31 | 1044 | 25453.81 |
| final8q_additive | DUK | 3.03 | 2.62 | -1.88 | -2.84 | 1.27 | -15.45 | 0.40 | 0.14 | 1075 | 12295.45 |
| final8q_additive | ERCO | 2.95 | 2.68 | -2.31 | -2.89 | 0.93 | -18.78 | 0.38 | 0.10 | 1071 | 53336.07 |
| final8q_additive | FPL | 3.68 | 3.29 | -2.62 | -3.50 | 0.97 | -39.18 | 0.45 | 0.18 | 1007 | 16591.11 |
| final8q_additive | ISNE | 3.85 | 3.37 | -1.20 | -2.22 | 0.58 | -18.49 | 0.29 | 0.14 | 1073 | 13001.44 |
| final8q_additive | MISO | 2.03 | 1.84 | -1.37 | -1.87 | 1.43 | -9.30 | 0.65 | 0.05 | 1084 | 74014.33 |
| final8q_additive | NYIS | 2.79 | 2.46 | -1.48 | -2.17 | 0.60 | -16.91 | 0.49 | 0.58 | 1062 | 17115.05 |
| final8q_additive | PJM | 2.28 | 2.03 | -1.45 | -2.11 | 1.18 | -11.98 | 0.57 | 0.26 | 1061 | 93218.11 |
| final8q_additive | SWPP | 2.65 | 2.20 | -2.38 | -2.84 | 1.62 | -23.36 | 0.53 | 0.19 | 1066 | 33074.81 |
| final8q_additive | TVA | 2.79 | 2.46 | -1.56 | -2.48 | 1.08 | -12.21 | 0.35 | 0.13 | 1076 | 18806.27 |
| final8q_boosting | BPAT | 2.24 | 1.97 | -1.36 | -1.99 | 1.60 | -18.09 | 0.40 | 0.29 | 1081 | 6762.61 |
| final8q_boosting | CISO | 2.72 | 2.46 | -1.12 | -1.88 | 1.07 | -15.29 | 0.88 | 0.35 | 1044 | 25453.81 |
| final8q_boosting | DUK | 2.96 | 2.54 | -1.90 | -2.75 | 1.29 | -14.30 | 0.41 | 0.15 | 1075 | 12295.45 |
| final8q_boosting | ERCO | 2.50 | 2.17 | -2.14 | -2.60 | 1.04 | -16.04 | 0.45 | 0.10 | 1071 | 53336.07 |
| final8q_boosting | FPL | 3.46 | 3.21 | -2.98 | -3.56 | 1.15 | -41.52 | 0.47 | 0.15 | 1007 | 16591.11 |
| final8q_boosting | ISNE | 3.60 | 3.15 | -0.92 | -1.75 | 0.56 | -14.39 | 0.31 | 0.14 | 1073 | 13001.44 |
| final8q_boosting | MISO | 1.88 | 1.68 | -1.36 | -1.75 | 1.38 | -10.32 | 0.69 | 0.04 | 1084 | 74014.33 |
| final8q_boosting | NYIS | 2.53 | 2.20 | -0.86 | -1.56 | 0.66 | -18.13 | 0.53 | 0.69 | 1062 | 17115.05 |
| final8q_boosting | PJM | 2.22 | 1.95 | -1.51 | -2.03 | 1.29 | -12.58 | 0.58 | 0.27 | 1061 | 93218.11 |
| final8q_boosting | SWPP | 2.69 | 2.11 | -1.93 | -2.54 | 1.80 | -22.72 | 0.54 | 0.22 | 1066 | 33074.81 |
| final8q_boosting | TVA | 2.68 | 2.42 | -1.54 | -2.36 | 1.28 | -12.57 | 0.35 | 0.12 | 1076 | 18806.27 |
| final8q_ensemble | BPAT | 2.16 | 1.93 | -1.79 | -2.17 | 1.30 | -17.06 | 0.45 | 0.25 | 1081 | 6762.61 |
| final8q_ensemble | CISO | 2.76 | 2.56 | -1.40 | -2.09 | 1.27 | -17.15 | 0.89 | 0.33 | 1044 | 25453.81 |
| final8q_ensemble | DUK | 2.79 | 2.39 | -1.81 | -2.66 | 1.18 | -14.56 | 0.45 | 0.15 | 1075 | 12295.45 |
| final8q_ensemble | ERCO | 2.54 | 2.24 | -2.29 | -2.68 | 0.80 | -17.49 | 0.45 | 0.08 | 1071 | 53336.07 |
| final8q_ensemble | FPL | 3.34 | 3.04 | -2.88 | -3.47 | 0.91 | -40.27 | 0.52 | 0.15 | 1007 | 16591.11 |
| final8q_ensemble | ISNE | 3.66 | 3.26 | -1.37 | -2.05 | 0.53 | -17.87 | 0.29 | 0.11 | 1073 | 13001.44 |
| final8q_ensemble | MISO | 1.88 | 1.72 | -1.43 | -1.78 | 1.26 | -9.25 | 0.69 | 0.04 | 1084 | 74014.33 |
| final8q_ensemble | NYIS | 2.59 | 2.29 | -1.31 | -1.88 | 0.62 | -16.11 | 0.52 | 0.63 | 1062 | 17115.05 |
| final8q_ensemble | PJM | 2.08 | 1.84 | -1.48 | -1.95 | 1.13 | -10.76 | 0.64 | 0.24 | 1061 | 93218.11 |
| final8q_ensemble | SWPP | 2.44 | 1.91 | -2.23 | -2.63 | 1.45 | -23.14 | 0.58 | 0.19 | 1066 | 33074.81 |
| final8q_ensemble | TVA | 2.51 | 2.17 | -1.46 | -2.21 | 1.15 | -12.30 | 0.41 | 0.12 | 1076 | 18806.27 |
| final8q_recency | BPAT | 2.77 | 2.46 | -2.41 | -2.73 | 1.46 | -15.93 | 0.29 | 0.20 | 1081 | 6762.61 |
| final8q_recency | CISO | 4.47 | 4.23 | -1.55 | -2.73 | 1.66 | -20.64 | 0.66 | 0.33 | 1044 | 25453.81 |
| final8q_recency | DUK | 3.39 | 3.03 | -1.66 | -2.85 | 1.33 | -18.09 | 0.32 | 0.17 | 1075 | 12295.45 |
| final8q_recency | ERCO | 3.10 | 2.71 | -2.57 | -3.07 | 1.02 | -19.91 | 0.35 | 0.08 | 1071 | 53336.07 |
| final8q_recency | FPL | 4.32 | 4.02 | -3.15 | -3.96 | 1.07 | -39.99 | 0.32 | 0.15 | 1007 | 16591.11 |
| final8q_recency | ISNE | 6.03 | 5.58 | -2.42 | -3.05 | 0.75 | -23.25 | 0.04 | 0.10 | 1073 | 13001.44 |
| final8q_recency | MISO | 2.55 | 2.29 | -1.59 | -2.05 | 1.74 | -11.32 | 0.54 | 0.05 | 1084 | 74014.33 |
| final8q_recency | NYIS | 4.19 | 3.88 | -1.88 | -2.72 | 0.89 | -13.68 | 0.22 | 0.48 | 1062 | 17115.05 |
| final8q_recency | PJM | 2.72 | 2.48 | -1.50 | -2.22 | 1.60 | -10.56 | 0.40 | 0.24 | 1061 | 93218.11 |
| final8q_recency | SWPP | 2.95 | 2.35 | -2.52 | -3.01 | 1.71 | -23.32 | 0.49 | 0.17 | 1066 | 33074.81 |
| final8q_recency | TVA | 2.93 | 2.53 | -1.30 | -2.28 | 1.44 | -13.73 | 0.32 | 0.14 | 1076 | 18806.27 |

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
| final8q | BPAT | gerri_heather | 3.65 | -2.70 | -3.04 | -7.76 | 6 |
| final8q | CISO | gerri_heather | 2.62 | 0.78 | -0.47 | -2.20 | 6 |
| final8q | DUK | gerri_heather | 5.16 | -4.92 | -4.92 | -8.36 | 6 |
| final8q | ERCO | gerri_heather | 6.17 | -6.31 | -6.31 | -11.37 | 6 |
| final8q | FPL | gerri_heather | 4.53 | -5.55 | -6.01 | -10.37 | 6 |
| final8q | ISNE | gerri_heather | 3.42 | -0.00 | -1.12 | -4.40 | 6 |
| final8q | MISO | gerri_heather | 2.71 | -1.94 | -2.12 | -4.62 | 6 |
| final8q | NYIS | gerri_heather | 1.99 | 0.17 | -0.59 | -1.04 | 5 |
| final8q | PJM | gerri_heather | 2.70 | -0.51 | -1.14 | -3.61 | 6 |
| final8q | SWPP | gerri_heather | 5.54 | -5.60 | -5.60 | -13.63 | 6 |
| final8q | TVA | gerri_heather | 2.69 | -0.38 | -1.00 | -3.83 | 6 |
| final8q_additive | BPAT | gerri_heather | 4.77 | -4.47 | -4.60 | -8.22 | 6 |
| final8q_additive | CISO | gerri_heather | 2.68 | 1.00 | -0.56 | -1.91 | 6 |
| final8q_additive | DUK | gerri_heather | 5.90 | -7.67 | -7.67 | -15.45 | 6 |
| final8q_additive | ERCO | gerri_heather | 8.10 | -10.35 | -10.35 | -15.06 | 6 |
| final8q_additive | FPL | gerri_heather | 6.06 | -6.96 | -6.96 | -11.85 | 6 |
| final8q_additive | ISNE | gerri_heather | 3.91 | -0.65 | -2.01 | -5.43 | 6 |
| final8q_additive | MISO | gerri_heather | 3.00 | -3.19 | -3.19 | -5.21 | 6 |
| final8q_additive | NYIS | gerri_heather | 2.37 | -1.92 | -2.15 | -3.62 | 5 |
| final8q_additive | PJM | gerri_heather | 2.45 | -0.48 | -0.97 | -2.97 | 6 |
| final8q_additive | SWPP | gerri_heather | 6.98 | -8.36 | -8.36 | -17.99 | 6 |
| final8q_additive | TVA | gerri_heather | 3.12 | -1.11 | -2.15 | -6.41 | 6 |
| final8q_boosting | BPAT | gerri_heather | 5.61 | -7.31 | -7.31 | -13.67 | 6 |
| final8q_boosting | CISO | gerri_heather | 2.60 | 0.77 | -0.75 | -4.09 | 6 |
| final8q_boosting | DUK | gerri_heather | 5.13 | -6.25 | -6.25 | -11.77 | 6 |
| final8q_boosting | ERCO | gerri_heather | 7.44 | -10.20 | -10.20 | -16.04 | 6 |
| final8q_boosting | FPL | gerri_heather | 4.41 | -6.75 | -6.76 | -12.27 | 6 |
| final8q_boosting | ISNE | gerri_heather | 3.51 | -0.50 | -1.47 | -4.73 | 6 |
| final8q_boosting | MISO | gerri_heather | 2.99 | -3.66 | -3.73 | -7.14 | 6 |
| final8q_boosting | NYIS | gerri_heather | 2.16 | 0.71 | -0.35 | -0.95 | 5 |
| final8q_boosting | PJM | gerri_heather | 2.93 | -1.94 | -2.48 | -4.24 | 6 |
| final8q_boosting | SWPP | gerri_heather | 6.34 | -7.44 | -7.44 | -14.14 | 6 |
| final8q_boosting | TVA | gerri_heather | 3.27 | -3.89 | -4.04 | -10.20 | 6 |
| final8q_ensemble | BPAT | gerri_heather | 4.46 | -5.01 | -5.01 | -10.09 | 6 |
| final8q_ensemble | CISO | gerri_heather | 2.47 | 0.71 | -0.62 | -3.62 | 6 |
| final8q_ensemble | DUK | gerri_heather | 5.55 | -7.45 | -7.45 | -14.23 | 6 |
| final8q_ensemble | ERCO | gerri_heather | 7.42 | -9.41 | -9.41 | -13.58 | 6 |
| final8q_ensemble | FPL | gerri_heather | 5.50 | -7.27 | -7.27 | -11.72 | 6 |
| final8q_ensemble | ISNE | gerri_heather | 3.82 | -0.72 | -1.78 | -5.39 | 6 |
| final8q_ensemble | MISO | gerri_heather | 2.97 | -3.39 | -3.39 | -5.71 | 6 |
| final8q_ensemble | NYIS | gerri_heather | 2.26 | -0.82 | -1.19 | -2.15 | 5 |
| final8q_ensemble | PJM | gerri_heather | 2.44 | -1.14 | -1.68 | -4.09 | 6 |
| final8q_ensemble | SWPP | gerri_heather | 7.12 | -8.36 | -8.36 | -16.35 | 6 |
| final8q_ensemble | TVA | gerri_heather | 2.43 | -1.65 | -1.98 | -4.98 | 6 |
| final8q_recency | BPAT | gerri_heather | 4.08 | -2.81 | -3.41 | -8.79 | 6 |
| final8q_recency | CISO | gerri_heather | 3.45 | 0.34 | -0.92 | -4.80 | 6 |
| final8q_recency | DUK | gerri_heather | 6.59 | -8.62 | -8.62 | -15.68 | 6 |
| final8q_recency | ERCO | gerri_heather | 7.19 | -7.44 | -7.44 | -15.08 | 6 |
| final8q_recency | FPL | gerri_heather | 6.61 | -8.04 | -8.04 | -13.27 | 6 |
| final8q_recency | ISNE | gerri_heather | 5.41 | -1.14 | -2.10 | -6.28 | 6 |
| final8q_recency | MISO | gerri_heather | 3.74 | -3.24 | -3.26 | -7.06 | 6 |
| final8q_recency | NYIS | gerri_heather | 3.89 | -1.68 | -1.70 | -3.30 | 5 |
| final8q_recency | PJM | gerri_heather | 3.15 | -0.86 | -1.96 | -5.34 | 6 |
| final8q_recency | SWPP | gerri_heather | 8.51 | -9.42 | -9.42 | -16.99 | 6 |
| final8q_recency | TVA | gerri_heather | 3.88 | 0.69 | -1.36 | -5.88 | 6 |
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
| final8q | BPAT | january_2025 | 2.05 | -2.11 | -2.54 | -4.40 | 6 |
| final8q | CISO | january_2025 | 2.05 | 1.79 | 0.00 | 0.00 | 6 |
| final8q | DUK | january_2025 | 3.59 | 1.99 | -0.91 | -4.77 | 6 |
| final8q | ERCO | january_2025 | 2.56 | -2.29 | -2.37 | -6.12 | 6 |
| final8q | FPL | january_2025 | 7.03 | -7.89 | -7.89 | -13.06 | 6 |
| final8q | ISNE | january_2025 | 3.93 | 0.43 | -0.66 | -1.81 | 6 |
| final8q | MISO | january_2025 | 2.45 | -2.00 | -2.00 | -3.26 | 6 |
| final8q | NYIS | january_2025 | 2.02 | 2.03 | 0.00 | 0.00 | 5 |
| final8q | PJM | january_2025 | 1.75 | -0.99 | -1.41 | -3.65 | 6 |
| final8q | SWPP | january_2025 | 2.48 | -2.17 | -2.17 | -2.96 | 6 |
| final8q | TVA | january_2025 | 3.47 | -1.10 | -1.83 | -5.47 | 6 |
| final8q_additive | BPAT | january_2025 | 2.61 | -3.38 | -3.65 | -5.13 | 6 |
| final8q_additive | CISO | january_2025 | 2.73 | 0.81 | -0.24 | -1.11 | 6 |
| final8q_additive | DUK | january_2025 | 3.64 | 0.66 | -0.84 | -5.04 | 6 |
| final8q_additive | ERCO | january_2025 | 3.52 | -3.89 | -3.93 | -6.84 | 6 |
| final8q_additive | FPL | january_2025 | 6.02 | -6.30 | -6.30 | -10.68 | 6 |
| final8q_additive | ISNE | january_2025 | 3.72 | -1.20 | -1.64 | -3.96 | 6 |
| final8q_additive | MISO | january_2025 | 2.89 | -2.86 | -2.86 | -4.83 | 6 |
| final8q_additive | NYIS | january_2025 | 2.07 | -1.52 | -1.80 | -3.43 | 5 |
| final8q_additive | PJM | january_2025 | 2.27 | -0.75 | -1.25 | -2.22 | 6 |
| final8q_additive | SWPP | january_2025 | 3.50 | -3.69 | -3.69 | -6.06 | 6 |
| final8q_additive | TVA | january_2025 | 4.20 | -2.89 | -3.38 | -7.13 | 6 |
| final8q_boosting | BPAT | january_2025 | 3.08 | -6.11 | -6.11 | -9.62 | 6 |
| final8q_boosting | CISO | january_2025 | 2.00 | -0.39 | -0.85 | -2.58 | 6 |
| final8q_boosting | DUK | january_2025 | 3.39 | -2.89 | -2.92 | -8.41 | 6 |
| final8q_boosting | ERCO | january_2025 | 3.26 | -5.84 | -5.84 | -8.22 | 6 |
| final8q_boosting | FPL | january_2025 | 6.39 | -9.62 | -9.62 | -15.81 | 6 |
| final8q_boosting | ISNE | january_2025 | 4.51 | -1.41 | -2.28 | -5.10 | 6 |
| final8q_boosting | MISO | january_2025 | 2.88 | -4.10 | -4.10 | -5.87 | 6 |
| final8q_boosting | NYIS | january_2025 | 1.79 | -0.68 | -1.15 | -2.69 | 5 |
| final8q_boosting | PJM | january_2025 | 2.69 | -5.15 | -5.15 | -9.27 | 6 |
| final8q_boosting | SWPP | january_2025 | 4.37 | -8.40 | -8.40 | -10.73 | 6 |
| final8q_boosting | TVA | january_2025 | 3.46 | -4.25 | -4.25 | -6.71 | 6 |
| final8q_ensemble | BPAT | january_2025 | 2.87 | -5.25 | -5.25 | -7.61 | 6 |
| final8q_ensemble | CISO | january_2025 | 2.47 | -0.01 | -0.89 | -2.29 | 6 |
| final8q_ensemble | DUK | january_2025 | 3.37 | -0.84 | -1.71 | -7.70 | 6 |
| final8q_ensemble | ERCO | january_2025 | 3.20 | -5.47 | -5.47 | -7.26 | 6 |
| final8q_ensemble | FPL | january_2025 | 6.04 | -8.17 | -8.17 | -13.31 | 6 |
| final8q_ensemble | ISNE | january_2025 | 3.47 | -1.28 | -1.70 | -3.96 | 6 |
| final8q_ensemble | MISO | january_2025 | 2.88 | -3.78 | -3.78 | -5.12 | 6 |
| final8q_ensemble | NYIS | january_2025 | 1.43 | -1.15 | -1.38 | -2.04 | 5 |
| final8q_ensemble | PJM | january_2025 | 2.36 | -3.20 | -3.20 | -5.34 | 6 |
| final8q_ensemble | SWPP | january_2025 | 4.05 | -5.72 | -5.72 | -6.06 | 6 |
| final8q_ensemble | TVA | january_2025 | 3.40 | -3.57 | -3.57 | -5.62 | 6 |
| final8q_recency | BPAT | january_2025 | 3.27 | -6.22 | -6.22 | -8.13 | 6 |
| final8q_recency | CISO | january_2025 | 4.80 | -0.70 | -3.08 | -5.66 | 6 |
| final8q_recency | DUK | january_2025 | 4.15 | -0.34 | -2.02 | -9.64 | 6 |
| final8q_recency | ERCO | january_2025 | 4.09 | -6.92 | -6.92 | -8.05 | 6 |
| final8q_recency | FPL | january_2025 | 6.84 | -8.48 | -8.48 | -13.08 | 6 |
| final8q_recency | ISNE | january_2025 | 4.32 | -1.18 | -1.66 | -4.61 | 6 |
| final8q_recency | MISO | january_2025 | 3.72 | -4.44 | -4.44 | -5.98 | 6 |
| final8q_recency | NYIS | january_2025 | 3.57 | -1.50 | -1.66 | -4.04 | 5 |
| final8q_recency | PJM | january_2025 | 3.25 | -3.51 | -3.51 | -6.30 | 6 |
| final8q_recency | SWPP | january_2025 | 4.71 | -5.36 | -5.36 | -8.40 | 6 |
| final8q_recency | TVA | january_2025 | 3.43 | -3.47 | -3.54 | -5.71 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final8q_ensemble | eve | 2.67 | -0.87 | -1.89 | 0.57 | 322 |
| 7 | final8q | eve | 2.80 | 0.66 | -1.25 | 0.53 | 322 |
| 8 | final8q_additive | eve | 2.81 | -0.88 | -2.11 | 0.52 | 322 |
| 9 | final8q_boosting | eve | 2.83 | -0.74 | -1.84 | 0.53 | 322 |
| 6 | DF | eve | 3.30 | 0.52 | -1.35 |  | 322 |
| 11 | final8q_recency | eve | 3.62 | -1.16 | -2.34 | 0.39 | 322 |
| 1 | final8q | special | 3.08 | -0.38 | -1.96 | 0.55 | 336 |
| 4 | final8q_ensemble | special | 3.14 | -1.86 | -2.82 | 0.53 | 336 |
| 2 | final8q_additive | special | 3.23 | -2.09 | -3.11 | 0.49 | 336 |
| 3 | final8q_boosting | special | 3.28 | -1.70 | -2.73 | 0.50 | 336 |
| 0 | DF | special | 3.56 | 0.06 | -1.69 |  | 336 |
| 5 | final8q_recency | special | 4.04 | -1.92 | -3.10 | 0.39 | 336 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final8q | all | 0.363 | 1.233 | 0.359 | 0.892 | 10.707 | 0.899 | 14.442 | 1.597 | 11469 |
| final8q | events | 0.408 | 1.705 | 0.649 | 0.826 | 12.248 | 0.815 | 21.142 | 2.265 | 130 |
| final8q | cold_mornings | 0.407 | 1.517 | 0.557 | 0.853 | 12.020 | 0.867 | 19.271 | 2.004 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final8q | BPAT | mape | 2.556 | 0.011 | 1081 |
| final8q | CISO | mape | -37.524 | 0.000 | 1044 |
| final8q | DUK | mape | 2.458 | 0.014 | 1075 |
| final8q | ERCO | mape | -4.371 | 0.000 | 1071 |
| final8q | FPL | mape | -2.044 | 0.041 | 1007 |
| final8q | ISNE | mape | 17.178 | 0.000 | 1073 |
| final8q | MISO | mape | -20.775 | 0.000 | 1084 |
| final8q | NYIS | mape | -2.846 | 0.004 | 1062 |
| final8q | PJM | mape | -12.801 | 0.000 | 1061 |
| final8q | SWPP | mape | -16.580 | 0.000 | 1066 |
| final8q | TVA | mape | 2.976 | 0.003 | 1076 |
| final8q_additive | BPAT | mape | 8.013 | 0.000 | 1081 |
| final8q_additive | CISO | mape | -33.876 | 0.000 | 1044 |
| final8q_additive | DUK | mape | 7.273 | 0.000 | 1075 |
| final8q_additive | ERCO | mape | 9.289 | 0.000 | 1071 |
| final8q_additive | FPL | mape | 8.137 | 0.000 | 1007 |
| final8q_additive | ISNE | mape | 20.883 | 0.000 | 1073 |
| final8q_additive | MISO | mape | -13.105 | 0.000 | 1084 |
| final8q_additive | NYIS | mape | 3.257 | 0.001 | 1062 |
| final8q_additive | PJM | mape | -3.325 | 0.001 | 1061 |
| final8q_additive | SWPP | mape | -13.158 | 0.000 | 1066 |
| final8q_additive | TVA | mape | 10.918 | 0.000 | 1076 |
| final8q_boosting | BPAT | mape | 6.085 | 0.000 | 1081 |
| final8q_boosting | CISO | mape | -36.172 | 0.000 | 1044 |
| final8q_boosting | DUK | mape | 6.453 | 0.000 | 1075 |
| final8q_boosting | ERCO | mape | 1.779 | 0.075 | 1071 |
| final8q_boosting | FPL | mape | 4.807 | 0.000 | 1007 |
| final8q_boosting | ISNE | mape | 17.918 | 0.000 | 1073 |
| final8q_boosting | MISO | mape | -16.651 | 0.000 | 1084 |
| final8q_boosting | NYIS | mape | -1.775 | 0.076 | 1062 |
| final8q_boosting | PJM | mape | -5.042 | 0.000 | 1061 |
| final8q_boosting | SWPP | mape | -13.785 | 0.000 | 1066 |
| final8q_boosting | TVA | mape | 9.246 | 0.000 | 1076 |
| final8q_ensemble | BPAT | mape | 4.053 | 0.000 | 1081 |
| final8q_ensemble | CISO | mape | -37.145 | 0.000 | 1044 |
| final8q_ensemble | DUK | mape | 3.024 | 0.002 | 1075 |
| final8q_ensemble | ERCO | mape | 2.512 | 0.012 | 1071 |
| final8q_ensemble | FPL | mape | 2.514 | 0.012 | 1007 |
| final8q_ensemble | ISNE | mape | 19.717 | 0.000 | 1073 |
| final8q_ensemble | MISO | mape | -16.434 | 0.000 | 1084 |
| final8q_ensemble | NYIS | mape | -0.661 | 0.509 | 1062 |
| final8q_ensemble | PJM | mape | -10.030 | 0.000 | 1061 |
| final8q_ensemble | SWPP | mape | -15.151 | 0.000 | 1066 |
| final8q_ensemble | TVA | mape | 5.293 | 0.000 | 1076 |
| final8q_recency | BPAT | mape | 16.137 | 0.000 | 1081 |
| final8q_recency | CISO | mape | -10.920 | 0.000 | 1044 |
| final8q_recency | DUK | mape | 13.044 | 0.000 | 1075 |
| final8q_recency | ERCO | mape | 11.174 | 0.000 | 1071 |
| final8q_recency | FPL | mape | 17.389 | 0.000 | 1007 |
| final8q_recency | ISNE | mape | 45.646 | 0.000 | 1073 |
| final8q_recency | MISO | mape | -2.961 | 0.003 | 1084 |
| final8q_recency | NYIS | mape | 24.150 | 0.000 | 1062 |
| final8q_recency | PJM | mape | 7.941 | 0.000 | 1061 |
| final8q_recency | SWPP | mape | -10.343 | 0.000 | 1066 |
| final8q_recency | TVA | mape | 12.962 | 0.000 | 1076 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final8q | 0.993 |
| final8q_additive | 0.970 |
| final8q_boosting | 0.993 |
| final8q_ensemble | 0.993 |
| final8q_recency | 0.993 |
