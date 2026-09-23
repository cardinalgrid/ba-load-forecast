# The phase F recipe on 2023 to 2025 under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The phase F recipe (`final2`) on 2023 to 2025 scored under protocol v2, the reference for `docs/frozen_evaluation_v2.md` (same days, same rules).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | 2.50 | 2.16 | 0.11 | -1.32 | 1.26 | 0.56 | 0.30 | -37.07 | 11815 | 11.00 |
| final_ensemble | 2.80 | 2.46 | -1.04 | -2.06 | 1.27 | 0.49 | 0.24 | -41.29 | 11815 | 11.00 |
| DF | 2.89 | 2.50 | 0.31 | -1.10 | 0.97 | 0.00 | 0.00 | -41.79 | 11815 | 11.00 |
| final_boosting | 2.98 | 2.65 | -0.99 | -2.09 | 1.44 | 0.45 | 0.24 | -41.64 | 11815 | 11.00 |
| final_additive | 3.00 | 2.63 | -1.11 | -2.22 | 1.34 | 0.46 | 0.23 | -40.92 | 11815 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.00 | 1.80 | -0.38 | -1.20 | 1.24 | -15.51 |  |  | 1087 | 6761.53 |
| DF | CISO | 5.36 | 5.12 | -1.73 | -2.61 | 1.18 | -33.79 |  |  | 1067 | 25391.65 |
| DF | DUK | 2.65 | 2.31 | 0.43 | -1.26 | 1.02 | -13.08 |  |  | 1078 | 12276.81 |
| DF | ERCO | 2.40 | 1.99 | 0.78 | -0.80 | 1.01 | -11.36 |  |  | 1081 | 53269.08 |
| DF | FPL | 3.21 | 3.06 | -0.59 | -1.70 | 1.12 | -41.79 |  |  | 1034 | 16561.38 |
| DF | ISNE | 2.57 | 2.51 | 0.39 | -0.45 | 0.33 | -5.42 |  |  | 1079 | 12995.31 |
| DF | MISO | 2.71 | 2.50 | 2.02 | -0.23 | 0.85 | -6.54 |  |  | 1088 | 74077.99 |
| DF | NYIS | 2.62 | 2.46 | -2.43 | -2.58 | 0.43 | -10.12 |  |  | 1070 | 17097.43 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1069 | 93064.27 |
| DF | SWPP | 4.33 | 2.47 | 1.42 | -1.38 | 1.48 | -17.10 |  |  | 1078 | 33075.46 |
| DF | TVA | 2.28 | 1.96 | 0.58 | -0.89 | 1.01 | -8.44 |  |  | 1084 | 18791.86 |
| final2 | BPAT | 2.36 | 2.05 | 0.03 | -1.26 | 1.42 | -17.46 | 0.40 | 0.39 | 1087 | 6761.53 |
| final2 | CISO | 2.76 | 2.51 | -0.10 | -1.47 | 1.03 | -15.24 | 0.87 | 0.41 | 1067 | 25391.65 |
| final2 | DUK | 3.38 | 2.83 | 0.44 | -1.86 | 1.34 | -15.38 | 0.34 | 0.27 | 1078 | 12276.81 |
| final2 | ERCO | 2.51 | 2.14 | -0.07 | -1.49 | 1.01 | -16.09 | 0.44 | 0.21 | 1081 | 53269.08 |
| final2 | FPL | 3.51 | 3.03 | 0.57 | -1.66 | 1.11 | -37.07 | 0.52 | 0.40 | 1034 | 16561.38 |
| final2 | ISNE | 3.81 | 3.30 | 0.42 | -1.26 | 0.51 | -23.75 | 0.30 | 0.21 | 1079 | 12995.31 |
| final2 | MISO | 1.90 | 1.71 | 0.15 | -0.98 | 1.46 | -8.60 | 0.69 | 0.08 | 1088 | 74077.99 |
| final2 | NYIS | 2.84 | 2.49 | 0.14 | -1.27 | 0.62 | -17.56 | 0.47 | 0.72 | 1070 | 17097.43 |
| final2 | PJM | 2.25 | 1.92 | 0.20 | -1.21 | 1.31 | -10.63 | 0.58 | 0.42 | 1069 | 93064.27 |
| final2 | SWPP | 2.56 | 2.05 | -0.26 | -1.52 | 1.80 | -24.21 | 0.57 | 0.33 | 1078 | 33075.46 |
| final2 | TVA | 2.93 | 2.54 | 0.13 | -1.68 | 1.36 | -14.17 | 0.32 | 0.23 | 1084 | 18791.86 |
| final_additive | BPAT | 2.61 | 2.29 | -1.68 | -2.30 | 1.56 | -16.77 | 0.33 | 0.26 | 1087 | 6761.53 |
| final_additive | CISO | 3.98 | 3.59 | -2.51 | -3.55 | 1.18 | -21.20 | 0.73 | 0.31 | 1067 | 25391.65 |
| final_additive | DUK | 3.61 | 3.03 | -0.70 | -2.55 | 1.41 | -17.49 | 0.32 | 0.21 | 1078 | 12276.81 |
| final_additive | ERCO | 3.23 | 2.87 | -1.98 | -2.73 | 1.01 | -18.90 | 0.31 | 0.12 | 1081 | 53269.08 |
| final_additive | FPL | 4.92 | 4.55 | -4.36 | -5.05 | 0.99 | -40.92 | 0.28 | 0.12 | 1034 | 16561.38 |
| final_additive | ISNE | 4.30 | 3.73 | -0.71 | -2.29 | 0.58 | -22.92 | 0.23 | 0.17 | 1079 | 12995.31 |
| final_additive | MISO | 2.31 | 2.06 | -0.93 | -1.70 | 1.70 | -10.32 | 0.58 | 0.06 | 1088 | 74077.99 |
| final_additive | NYIS | 3.11 | 2.70 | -1.01 | -2.08 | 0.63 | -18.17 | 0.43 | 0.62 | 1070 | 17097.43 |
| final_additive | PJM | 2.59 | 2.26 | -0.33 | -1.62 | 1.41 | -12.48 | 0.48 | 0.35 | 1069 | 93064.27 |
| final_additive | SWPP | 2.73 | 2.19 | -0.78 | -2.01 | 1.75 | -23.04 | 0.55 | 0.28 | 1078 | 33075.46 |
| final_additive | TVA | 3.29 | 2.80 | 0.57 | -1.66 | 1.30 | -16.29 | 0.27 | 0.25 | 1084 | 18791.86 |
| final_boosting | BPAT | 2.60 | 2.25 | -0.74 | -1.80 | 1.53 | -17.90 | 0.33 | 0.33 | 1087 | 6761.53 |
| final_boosting | CISO | 3.21 | 2.87 | -2.22 | -2.87 | 1.13 | -15.52 | 0.79 | 0.31 | 1067 | 25391.65 |
| final_boosting | DUK | 3.60 | 3.08 | -0.87 | -2.60 | 1.44 | -16.85 | 0.32 | 0.21 | 1078 | 12276.81 |
| final_boosting | ERCO | 2.93 | 2.62 | -1.67 | -2.47 | 1.13 | -17.65 | 0.34 | 0.13 | 1081 | 53269.08 |
| final_boosting | FPL | 5.61 | 5.34 | -5.53 | -5.87 | 1.38 | -41.64 | 0.17 | 0.08 | 1034 | 16561.38 |
| final_boosting | ISNE | 4.07 | 3.54 | -1.00 | -2.06 | 0.60 | -22.84 | 0.25 | 0.16 | 1079 | 12995.31 |
| final_boosting | MISO | 2.18 | 2.05 | -0.57 | -1.42 | 1.61 | -9.16 | 0.62 | 0.07 | 1088 | 74077.99 |
| final_boosting | NYIS | 3.09 | 2.69 | -0.88 | -1.84 | 0.76 | -16.34 | 0.42 | 0.64 | 1070 | 17097.43 |
| final_boosting | PJM | 2.77 | 2.48 | -0.26 | -1.61 | 1.67 | -12.43 | 0.41 | 0.38 | 1069 | 93064.27 |
| final_boosting | SWPP | 3.08 | 2.41 | -0.52 | -2.00 | 1.89 | -22.89 | 0.50 | 0.27 | 1078 | 33075.46 |
| final_boosting | TVA | 3.30 | 2.84 | 0.20 | -1.79 | 1.45 | -16.13 | 0.24 | 0.22 | 1084 | 18791.86 |
| final_ensemble | BPAT | 2.41 | 2.10 | -1.21 | -1.97 | 1.41 | -17.25 | 0.38 | 0.29 | 1087 | 6761.53 |
| final_ensemble | CISO | 3.31 | 2.91 | -2.32 | -3.07 | 1.11 | -16.30 | 0.80 | 0.32 | 1067 | 25391.65 |
| final_ensemble | DUK | 3.45 | 2.83 | -0.79 | -2.51 | 1.41 | -16.96 | 0.35 | 0.21 | 1078 | 12276.81 |
| final_ensemble | ERCO | 2.91 | 2.58 | -1.80 | -2.52 | 0.96 | -16.89 | 0.35 | 0.12 | 1081 | 53269.08 |
| final_ensemble | FPL | 4.96 | 4.59 | -4.87 | -5.28 | 1.05 | -41.29 | 0.27 | 0.10 | 1034 | 16561.38 |
| final_ensemble | ISNE | 3.95 | 3.44 | -0.85 | -2.06 | 0.55 | -22.88 | 0.27 | 0.16 | 1079 | 12995.31 |
| final_ensemble | MISO | 2.10 | 1.92 | -0.75 | -1.48 | 1.50 | -9.14 | 0.64 | 0.06 | 1088 | 74077.99 |
| final_ensemble | NYIS | 2.89 | 2.55 | -0.92 | -1.84 | 0.61 | -17.17 | 0.46 | 0.65 | 1070 | 17097.43 |
| final_ensemble | PJM | 2.50 | 2.22 | -0.29 | -1.52 | 1.36 | -12.26 | 0.50 | 0.38 | 1069 | 93064.27 |
| final_ensemble | SWPP | 2.73 | 2.17 | -0.68 | -1.94 | 1.72 | -22.96 | 0.55 | 0.28 | 1078 | 33075.46 |
| final_ensemble | TVA | 3.17 | 2.72 | 0.38 | -1.66 | 1.32 | -15.36 | 0.27 | 0.23 | 1084 | 18791.86 |

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
| final2 | BPAT | gerri_heather | 5.31 | -5.27 | -5.27 | -13.30 | 6 |
| final2 | CISO | gerri_heather | 3.29 | 2.09 | -0.17 | -1.02 | 6 |
| final2 | DUK | gerri_heather | 5.77 | -5.90 | -5.90 | -10.44 | 6 |
| final2 | ERCO | gerri_heather | 6.85 | -8.61 | -8.61 | -14.51 | 6 |
| final2 | FPL | gerri_heather | 5.16 | -4.75 | -5.79 | -10.66 | 6 |
| final2 | ISNE | gerri_heather | 4.01 | -0.10 | -1.28 | -4.74 | 6 |
| final2 | MISO | gerri_heather | 2.65 | -1.58 | -1.97 | -4.95 | 6 |
| final2 | NYIS | gerri_heather | 2.08 | 0.58 | -0.42 | -2.10 | 5 |
| final2 | PJM | gerri_heather | 2.71 | -0.64 | -1.45 | -3.63 | 6 |
| final2 | SWPP | gerri_heather | 5.32 | -5.10 | -5.10 | -12.96 | 6 |
| final2 | TVA | gerri_heather | 2.96 | -0.71 | -2.01 | -5.88 | 6 |
| final_additive | BPAT | gerri_heather | 6.00 | -5.74 | -6.16 | -16.77 | 6 |
| final_additive | CISO | gerri_heather | 3.35 | 2.30 | -0.23 | -0.88 | 6 |
| final_additive | DUK | gerri_heather | 6.19 | -7.11 | -7.15 | -15.60 | 6 |
| final_additive | ERCO | gerri_heather | 8.46 | -10.54 | -10.54 | -17.41 | 6 |
| final_additive | FPL | gerri_heather | 6.47 | -8.00 | -8.00 | -14.44 | 6 |
| final_additive | ISNE | gerri_heather | 4.29 | 0.71 | -1.50 | -5.35 | 6 |
| final_additive | MISO | gerri_heather | 2.51 | -1.56 | -1.73 | -3.85 | 6 |
| final_additive | NYIS | gerri_heather | 2.45 | -0.90 | -1.49 | -3.22 | 5 |
| final_additive | PJM | gerri_heather | 2.96 | 1.47 | -0.20 | -0.86 | 6 |
| final_additive | SWPP | gerri_heather | 7.14 | -7.50 | -7.50 | -17.67 | 6 |
| final_additive | TVA | gerri_heather | 3.69 | 1.63 | -1.13 | -6.77 | 6 |
| final_boosting | BPAT | gerri_heather | 5.60 | -6.79 | -6.79 | -12.34 | 6 |
| final_boosting | CISO | gerri_heather | 3.73 | 2.86 | -0.29 | -1.72 | 6 |
| final_boosting | DUK | gerri_heather | 5.75 | -6.31 | -6.46 | -10.78 | 6 |
| final_boosting | ERCO | gerri_heather | 5.53 | -7.55 | -7.55 | -10.72 | 6 |
| final_boosting | FPL | gerri_heather | 5.51 | -7.18 | -7.51 | -13.51 | 6 |
| final_boosting | ISNE | gerri_heather | 4.05 | 0.24 | -0.73 | -3.98 | 6 |
| final_boosting | MISO | gerri_heather | 2.41 | -1.53 | -2.47 | -6.72 | 6 |
| final_boosting | NYIS | gerri_heather | 2.90 | 1.82 | -0.22 | -1.12 | 5 |
| final_boosting | PJM | gerri_heather | 2.44 | 0.19 | -1.03 | -3.13 | 6 |
| final_boosting | SWPP | gerri_heather | 6.01 | -7.00 | -7.00 | -12.41 | 6 |
| final_boosting | TVA | gerri_heather | 3.88 | -0.34 | -2.75 | -9.28 | 6 |
| final_ensemble | BPAT | gerri_heather | 5.54 | -6.31 | -6.31 | -14.38 | 6 |
| final_ensemble | CISO | gerri_heather | 3.39 | 2.58 | -0.22 | -1.30 | 6 |
| final_ensemble | DUK | gerri_heather | 5.82 | -6.72 | -6.81 | -13.22 | 6 |
| final_ensemble | ERCO | gerri_heather | 6.73 | -8.93 | -8.93 | -13.78 | 6 |
| final_ensemble | FPL | gerri_heather | 5.75 | -7.61 | -7.61 | -14.00 | 6 |
| final_ensemble | ISNE | gerri_heather | 4.00 | 0.46 | -1.06 | -4.63 | 6 |
| final_ensemble | MISO | gerri_heather | 2.41 | -1.55 | -2.03 | -5.29 | 6 |
| final_ensemble | NYIS | gerri_heather | 2.04 | 0.57 | -0.41 | -2.07 | 5 |
| final_ensemble | PJM | gerri_heather | 2.55 | 0.86 | -0.49 | -1.92 | 6 |
| final_ensemble | SWPP | gerri_heather | 6.53 | -7.26 | -7.26 | -15.00 | 6 |
| final_ensemble | TVA | gerri_heather | 3.13 | 0.65 | -1.56 | -5.28 | 6 |
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
| final2 | BPAT | january_2025 | 2.84 | -3.22 | -3.72 | -5.27 | 6 |
| final2 | CISO | january_2025 | 1.84 | 0.53 | -0.19 | -0.96 | 6 |
| final2 | DUK | january_2025 | 4.70 | -0.27 | -1.87 | -6.91 | 6 |
| final2 | ERCO | january_2025 | 3.25 | -4.63 | -4.63 | -8.14 | 6 |
| final2 | FPL | january_2025 | 4.90 | -5.50 | -5.50 | -11.30 | 6 |
| final2 | ISNE | january_2025 | 3.81 | -0.63 | -1.41 | -3.04 | 6 |
| final2 | MISO | january_2025 | 2.67 | -2.71 | -2.71 | -4.48 | 6 |
| final2 | NYIS | january_2025 | 2.01 | 1.50 | 0.00 | 0.00 | 5 |
| final2 | PJM | january_2025 | 2.06 | -1.29 | -1.56 | -3.65 | 6 |
| final2 | SWPP | january_2025 | 3.07 | -3.03 | -3.03 | -4.51 | 6 |
| final2 | TVA | january_2025 | 3.58 | -2.23 | -2.48 | -8.06 | 6 |
| final_additive | BPAT | january_2025 | 3.21 | -3.46 | -3.98 | -5.57 | 6 |
| final_additive | CISO | january_2025 | 3.91 | 1.96 | -0.11 | -0.58 | 6 |
| final_additive | DUK | january_2025 | 4.07 | 0.48 | -1.20 | -6.26 | 6 |
| final_additive | ERCO | january_2025 | 3.47 | -4.64 | -4.64 | -9.56 | 6 |
| final_additive | FPL | january_2025 | 4.94 | -4.46 | -4.46 | -10.31 | 6 |
| final_additive | ISNE | january_2025 | 3.47 | -0.02 | -1.20 | -4.19 | 6 |
| final_additive | MISO | january_2025 | 2.76 | -2.92 | -2.92 | -4.82 | 6 |
| final_additive | NYIS | january_2025 | 1.85 | -0.44 | -0.96 | -3.26 | 5 |
| final_additive | PJM | january_2025 | 2.30 | 0.78 | -0.23 | -1.21 | 6 |
| final_additive | SWPP | january_2025 | 3.94 | -3.92 | -3.92 | -5.99 | 6 |
| final_additive | TVA | january_2025 | 3.71 | -1.97 | -2.53 | -7.25 | 6 |
| final_boosting | BPAT | january_2025 | 3.68 | -6.42 | -6.42 | -9.31 | 6 |
| final_boosting | CISO | january_2025 | 2.10 | -0.19 | -0.85 | -2.79 | 6 |
| final_boosting | DUK | january_2025 | 4.58 | -1.88 | -2.55 | -8.47 | 6 |
| final_boosting | ERCO | january_2025 | 3.58 | -5.83 | -5.83 | -7.84 | 6 |
| final_boosting | FPL | january_2025 | 4.55 | -5.79 | -5.84 | -11.11 | 6 |
| final_boosting | ISNE | january_2025 | 4.01 | 0.66 | -0.76 | -2.29 | 6 |
| final_boosting | MISO | january_2025 | 2.41 | -2.76 | -2.76 | -4.77 | 6 |
| final_boosting | NYIS | january_2025 | 2.64 | 0.97 | -0.11 | -0.53 | 5 |
| final_boosting | PJM | january_2025 | 2.74 | -3.96 | -4.15 | -9.57 | 6 |
| final_boosting | SWPP | january_2025 | 4.33 | -7.54 | -7.54 | -8.61 | 6 |
| final_boosting | TVA | january_2025 | 3.22 | -2.68 | -2.68 | -6.15 | 6 |
| final_ensemble | BPAT | january_2025 | 3.41 | -5.02 | -5.23 | -7.21 | 6 |
| final_ensemble | CISO | january_2025 | 2.61 | 0.67 | -0.48 | -1.91 | 6 |
| final_ensemble | DUK | january_2025 | 4.23 | -0.72 | -1.88 | -7.38 | 6 |
| final_ensemble | ERCO | january_2025 | 3.24 | -5.24 | -5.24 | -8.62 | 6 |
| final_ensemble | FPL | january_2025 | 4.36 | -5.14 | -5.14 | -10.19 | 6 |
| final_ensemble | ISNE | january_2025 | 3.38 | 0.30 | -0.86 | -2.48 | 6 |
| final_ensemble | MISO | january_2025 | 2.48 | -2.84 | -2.84 | -4.17 | 6 |
| final_ensemble | NYIS | january_2025 | 1.79 | 0.32 | -0.35 | -1.12 | 5 |
| final_ensemble | PJM | january_2025 | 2.02 | -1.46 | -1.65 | -3.61 | 6 |
| final_ensemble | SWPP | january_2025 | 4.07 | -5.61 | -5.61 | -7.22 | 6 |
| final_ensemble | TVA | january_2025 | 3.12 | -2.34 | -2.34 | -6.68 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | final2 | eve | 3.07 | 0.94 | -1.35 | 0.47 | 326 |
| 9 | final_ensemble | eve | 3.19 | -0.17 | -1.88 | 0.45 | 326 |
| 5 | DF | eve | 3.29 | 0.52 | -1.34 |  | 326 |
| 7 | final_additive | eve | 3.31 | -0.18 | -2.00 | 0.42 | 326 |
| 8 | final_boosting | eve | 3.49 | -0.19 | -1.93 | 0.39 | 326 |
| 1 | final2 | special | 3.23 | -0.22 | -1.96 | 0.50 | 339 |
| 4 | final_ensemble | special | 3.48 | -1.27 | -2.61 | 0.47 | 339 |
| 0 | DF | special | 3.55 | 0.07 | -1.68 |  | 339 |
| 2 | final_additive | special | 3.65 | -1.38 | -2.81 | 0.46 | 339 |
| 3 | final_boosting | special | 3.79 | -1.18 | -2.59 | 0.41 | 339 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.405 | 1.401 | 0.417 | 0.893 | 12.334 | 0.896 | 11584 |
| final2 | events | 0.466 | 1.850 | 0.714 | 0.807 | 12.976 | 0.777 | 130 |
| final2 | cold_mornings | 0.472 | 1.699 | 0.576 | 0.843 | 13.410 | 0.836 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | BPAT | mape | 8.090 | 0.000 | 1087 |
| final2 | CISO | mape | -34.719 | 0.000 | 1067 |
| final2 | DUK | mape | 12.562 | 0.000 | 1078 |
| final2 | ERCO | mape | 2.264 | 0.024 | 1081 |
| final2 | FPL | mape | 5.096 | 0.000 | 1034 |
| final2 | ISNE | mape | 19.067 | 0.000 | 1079 |
| final2 | MISO | mape | -16.689 | 0.000 | 1088 |
| final2 | NYIS | mape | 3.589 | 0.000 | 1070 |
| final2 | PJM | mape | -3.476 | 0.001 | 1069 |
| final2 | SWPP | mape | -14.497 | 0.000 | 1078 |
| final2 | TVA | mape | 13.373 | 0.000 | 1084 |
| final_additive | BPAT | mape | 13.279 | 0.000 | 1087 |
| final_additive | CISO | mape | -16.742 | 0.000 | 1067 |
| final_additive | DUK | mape | 15.031 | 0.000 | 1078 |
| final_additive | ERCO | mape | 13.790 | 0.000 | 1081 |
| final_additive | FPL | mape | 21.946 | 0.000 | 1034 |
| final_additive | ISNE | mape | 24.950 | 0.000 | 1079 |
| final_additive | MISO | mape | -7.621 | 0.000 | 1088 |
| final_additive | NYIS | mape | 7.748 | 0.000 | 1070 |
| final_additive | PJM | mape | 4.362 | 0.000 | 1069 |
| final_additive | SWPP | mape | -12.740 | 0.000 | 1078 |
| final_additive | TVA | mape | 18.451 | 0.000 | 1084 |
| final_boosting | BPAT | mape | 12.945 | 0.000 | 1087 |
| final_boosting | CISO | mape | -26.514 | 0.000 | 1067 |
| final_boosting | DUK | mape | 15.104 | 0.000 | 1078 |
| final_boosting | ERCO | mape | 9.489 | 0.000 | 1081 |
| final_boosting | FPL | mape | 30.391 | 0.000 | 1034 |
| final_boosting | ISNE | mape | 22.839 | 0.000 | 1079 |
| final_boosting | MISO | mape | -10.375 | 0.000 | 1088 |
| final_boosting | NYIS | mape | 7.663 | 0.000 | 1070 |
| final_boosting | PJM | mape | 8.484 | 0.000 | 1069 |
| final_boosting | SWPP | mape | -10.259 | 0.000 | 1078 |
| final_boosting | TVA | mape | 19.356 | 0.000 | 1084 |
| final_ensemble | BPAT | mape | 9.320 | 0.000 | 1087 |
| final_ensemble | CISO | mape | -25.517 | 0.000 | 1067 |
| final_ensemble | DUK | mape | 12.981 | 0.000 | 1078 |
| final_ensemble | ERCO | mape | 9.116 | 0.000 | 1081 |
| final_ensemble | FPL | mape | 22.970 | 0.000 | 1034 |
| final_ensemble | ISNE | mape | 21.135 | 0.000 | 1079 |
| final_ensemble | MISO | mape | -12.098 | 0.000 | 1088 |
| final_ensemble | NYIS | mape | 4.412 | 0.000 | 1070 |
| final_ensemble | PJM | mape | 2.449 | 0.014 | 1069 |
| final_ensemble | SWPP | mape | -13.064 | 0.000 | 1078 |
| final_ensemble | TVA | mape | 16.930 | 0.000 | 1084 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final2 | 0.991 |
| final_additive | 0.980 |
| final_boosting | 0.991 |
| final_ensemble | 0.991 |
