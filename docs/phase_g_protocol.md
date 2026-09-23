# Phase G: the recipe under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The phase F recipe (`final2`), scored under protocol v2: a day on which the published forecast is missing, non-positive or more than 50 % away from the outcome at any hour is left out for every model, as is a day with an hour more than 40 % away from the mean of its neighbours; and the documented hour-label offsets (`docs/hour_label_offsets.csv`: PJM forecast +1 h from February 2019, CAISO demand -1 h from 14 June 2022) are applied to the published series before anything else, for the models and for `DF` alike.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | 2.54 | 2.21 | 0.13 | -1.35 | 1.32 | 0.53 | 0.29 | -47.24 | 8151 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8151 | 11.00 |
| final_ensemble | 2.85 | 2.50 | -1.20 | -2.16 | 1.28 | 0.46 | 0.23 | -51.36 | 8151 | 11.00 |
| final_boosting | 3.00 | 2.65 | -0.97 | -2.10 | 1.49 | 0.42 | 0.24 | -51.98 | 8151 | 11.00 |
| final_additive | 3.11 | 2.74 | -1.44 | -2.44 | 1.41 | 0.42 | 0.22 | -50.91 | 8151 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.38 | 2.15 | 0.39 | -0.65 | 0.24 | -6.72 |  |  | 737 | 25196.34 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | FPL | 3.88 | 3.60 | -3.54 | -3.93 | 1.15 | -47.43 |  |  | 690 | 15275.13 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 2.45 | 2.23 | -0.60 | -1.27 | 1.04 | -8.98 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.21 | -19.98 |  |  | 745 | 31350.31 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| final2 | BPAT | 2.55 | 2.21 | -0.24 | -1.41 | 1.81 | -18.21 | 0.37 | 0.26 | 750 | 6533.15 |
| final2 | CISO | 2.58 | 2.24 | 0.55 | -1.12 | 0.33 | -12.29 | 0.47 | 0.26 | 737 | 25196.34 |
| final2 | DUK | 3.36 | 3.03 | 0.11 | -1.85 | 1.32 | -15.78 | 0.39 | 0.32 | 750 | 12129.97 |
| final2 | ERCO | 2.79 | 2.38 | 0.20 | -1.47 | 1.12 | -13.56 | 0.44 | 0.28 | 746 | 46782.53 |
| final2 | FPL | 3.73 | 3.32 | -0.57 | -2.52 | 1.12 | -47.24 | 0.59 | 0.64 | 690 | 15275.13 |
| final2 | ISNE | 3.43 | 2.98 | 0.64 | -1.35 | 0.51 | -17.43 | 0.30 | 0.22 | 752 | 13392.81 |
| final2 | MISO | 2.10 | 1.87 | 0.11 | -1.03 | 1.63 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2 | NYIS | 2.48 | 2.10 | 0.19 | -1.30 | 0.58 | -12.50 | 0.57 | 0.71 | 752 | 17400.75 |
| final2 | PJM | 2.29 | 1.98 | 0.05 | -1.31 | 1.64 | -10.41 | 0.56 | 0.42 | 744 | 91927.69 |
| final2 | SWPP | 2.37 | 1.98 | -0.08 | -1.35 | 1.46 | -20.96 | 0.72 | 0.11 | 745 | 31350.31 |
| final2 | TVA | 3.02 | 2.63 | 0.40 | -1.52 | 1.36 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final_additive | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| final_additive | CISO | 3.78 | 3.16 | -2.87 | -3.82 | 0.42 | -18.17 | 0.25 | 0.13 | 737 | 25196.34 |
| final_additive | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| final_additive | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
| final_additive | FPL | 6.18 | 5.61 | -6.17 | -6.74 | 1.08 | -50.91 | 0.29 | 0.27 | 690 | 15275.13 |
| final_additive | ISNE | 3.86 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 752 | 13392.81 |
| final_additive | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| final_additive | NYIS | 2.72 | 2.37 | -0.86 | -2.08 | 0.60 | -15.67 | 0.51 | 0.60 | 752 | 17400.75 |
| final_additive | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.42 | 0.37 | 744 | 91927.69 |
| final_additive | SWPP | 2.53 | 2.11 | -0.29 | -1.59 | 1.50 | -20.36 | 0.70 | 0.10 | 745 | 31350.31 |
| final_additive | TVA | 3.35 | 2.97 | -1.05 | -2.35 | 1.42 | -14.12 | 0.25 | 0.26 | 739 | 18562.62 |
| final_boosting | BPAT | 2.73 | 2.43 | -0.43 | -1.57 | 2.00 | -18.16 | 0.27 | 0.24 | 750 | 6533.15 |
| final_boosting | CISO | 3.01 | 2.63 | -2.03 | -2.64 | 0.40 | -18.66 | 0.35 | 0.15 | 737 | 25196.34 |
| final_boosting | DUK | 3.58 | 3.12 | -0.42 | -2.27 | 1.50 | -16.82 | 0.33 | 0.27 | 750 | 12129.97 |
| final_boosting | ERCO | 3.13 | 2.72 | -2.27 | -2.98 | 1.29 | -15.00 | 0.35 | 0.18 | 746 | 46782.53 |
| final_boosting | FPL | 6.27 | 5.91 | -6.58 | -6.93 | 1.33 | -51.98 | 0.20 | 0.27 | 690 | 15275.13 |
| final_boosting | ISNE | 3.67 | 3.34 | -0.81 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 752 | 13392.81 |
| final_boosting | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| final_boosting | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.74 | -14.02 | 0.51 | 0.66 | 752 | 17400.75 |
| final_boosting | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.41 | 0.42 | 744 | 91927.69 |
| final_boosting | SWPP | 2.67 | 2.18 | -0.92 | -1.99 | 1.65 | -28.44 | 0.68 | 0.08 | 745 | 31350.31 |
| final_boosting | TVA | 3.28 | 2.85 | -0.22 | -1.84 | 1.54 | -15.24 | 0.24 | 0.30 | 739 | 18562.62 |
| final_ensemble | BPAT | 2.59 | 2.27 | -0.66 | -1.61 | 1.83 | -18.29 | 0.32 | 0.23 | 750 | 6533.15 |
| final_ensemble | CISO | 3.09 | 2.60 | -2.37 | -3.05 | 0.35 | -18.43 | 0.37 | 0.14 | 737 | 25196.34 |
| final_ensemble | DUK | 3.43 | 2.97 | -0.56 | -2.26 | 1.33 | -15.64 | 0.37 | 0.27 | 750 | 12129.97 |
| final_ensemble | ERCO | 3.13 | 2.70 | -2.25 | -2.89 | 1.07 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| final_ensemble | FPL | 6.03 | 5.64 | -6.32 | -6.70 | 1.10 | -51.36 | 0.26 | 0.27 | 690 | 15275.13 |
| final_ensemble | ISNE | 3.53 | 3.16 | -0.96 | -2.20 | 0.53 | -19.48 | 0.26 | 0.16 | 752 | 13392.81 |
| final_ensemble | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| final_ensemble | NYIS | 2.49 | 2.14 | -0.64 | -1.71 | 0.56 | -13.90 | 0.56 | 0.65 | 752 | 17400.75 |
| final_ensemble | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.46 | 0.39 | 744 | 91927.69 |
| final_ensemble | SWPP | 2.44 | 1.98 | -0.59 | -1.71 | 1.47 | -21.47 | 0.71 | 0.09 | 745 | 31350.31 |
| final_ensemble | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |

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
| final2 | BPAT | uri | 2.87 | 0.04 | -0.92 | -4.38 | 6 |
| final2 | CISO | uri | 1.79 | 0.24 | -0.41 | -1.10 | 6 |
| final2 | DUK | uri | 3.51 | -1.08 | -1.67 | -4.03 | 6 |
| final2 | ERCO | uri | 7.11 | -9.52 | -9.52 | -10.27 | 2 |
| final2 | FPL | uri | 7.94 | -7.78 | -7.78 | -11.49 | 6 |
| final2 | ISNE | uri | 2.76 | 2.18 | -0.15 | -0.87 | 6 |
| final2 | MISO | uri | 3.44 | -2.39 | -2.82 | -5.84 | 5 |
| final2 | NYIS | uri | 2.03 | 2.22 | -0.14 | -0.82 | 6 |
| final2 | PJM | uri | 1.86 | 0.07 | -0.65 | -2.07 | 6 |
| final2 | SWPP | uri | 6.41 | 1.17 | -2.28 | -5.30 | 4 |
| final2 | TVA | uri | 3.04 | -1.89 | -2.67 | -5.67 | 6 |
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
| final_ensemble | BPAT | uri | 2.95 | 0.23 | -0.68 | -3.44 | 6 |
| final_ensemble | CISO | uri | 1.62 | 0.63 | -0.14 | -0.62 | 6 |
| final_ensemble | DUK | uri | 3.42 | -2.79 | -2.79 | -6.10 | 6 |
| final_ensemble | ERCO | uri | 6.28 | -9.24 | -9.24 | -9.46 | 2 |
| final_ensemble | FPL | uri | 9.92 | -12.91 | -12.91 | -15.50 | 6 |
| final_ensemble | ISNE | uri | 2.81 | 1.32 | -0.38 | -2.20 | 6 |
| final_ensemble | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| final_ensemble | NYIS | uri | 2.11 | 1.50 | -0.23 | -1.35 | 6 |
| final_ensemble | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| final_ensemble | SWPP | uri | 6.08 | -0.39 | -2.96 | -6.25 | 4 |
| final_ensemble | TVA | uri | 2.71 | -1.06 | -1.72 | -3.36 | 6 |
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
| final2 | BPAT | elliott | 3.70 | -2.63 | -3.01 | -6.46 | 5 |
| final2 | CISO | elliott | 3.19 | 2.15 | -0.43 | -2.17 | 5 |
| final2 | DUK | elliott | 3.14 | -1.01 | -1.49 | -4.41 | 4 |
| final2 | ERCO | elliott | 6.82 | -1.38 | -3.86 | -9.30 | 5 |
| final2 | FPL | elliott | 7.90 | -9.00 | -9.23 | -14.82 | 5 |
| final2 | ISNE | elliott | 3.51 | 1.63 | -0.72 | -2.23 | 5 |
| final2 | MISO | elliott | 3.42 | -1.58 | -2.69 | -4.10 | 5 |
| final2 | NYIS | elliott | 2.78 | -0.62 | -1.45 | -3.18 | 5 |
| final2 | PJM | elliott | 4.26 | -2.70 | -3.11 | -6.29 | 5 |
| final2 | SWPP | elliott | 4.56 | 0.73 | -1.68 | -4.76 | 5 |
| final2 | TVA | elliott | 6.70 | 4.69 | 0.00 | 0.00 | 3 |
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
| final_ensemble | BPAT | elliott | 4.21 | -3.47 | -3.90 | -8.35 | 5 |
| final_ensemble | CISO | elliott | 3.46 | 2.80 | -0.43 | -2.17 | 5 |
| final_ensemble | DUK | elliott | 3.71 | -3.00 | -3.00 | -3.88 | 4 |
| final_ensemble | ERCO | elliott | 6.73 | -4.28 | -5.36 | -12.60 | 5 |
| final_ensemble | FPL | elliott | 8.81 | -10.29 | -10.53 | -14.82 | 5 |
| final_ensemble | ISNE | elliott | 3.39 | 2.09 | -0.44 | -1.16 | 5 |
| final_ensemble | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| final_ensemble | NYIS | elliott | 2.73 | -1.04 | -1.83 | -3.53 | 5 |
| final_ensemble | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| final_ensemble | SWPP | elliott | 4.12 | -2.20 | -3.22 | -7.26 | 5 |
| final_ensemble | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | DF | eve | 3.37 | 0.49 | -1.42 |  | 268 |
| 6 | final2 | eve | 3.54 | 1.15 | -1.45 | 0.41 | 268 |
| 9 | final_ensemble | eve | 3.62 | -0.11 | -2.04 | 0.43 | 268 |
| 7 | final_additive | eve | 3.83 | -0.12 | -2.19 | 0.40 | 268 |
| 8 | final_boosting | eve | 3.86 | -0.07 | -2.12 | 0.40 | 268 |
| 1 | final2 | special | 3.43 | -0.43 | -2.05 | 0.50 | 270 |
| 4 | final_ensemble | special | 3.62 | -1.73 | -2.89 | 0.50 | 270 |
| 0 | DF | special | 3.70 | -0.13 | -1.77 |  | 270 |
| 2 | final_additive | special | 3.84 | -1.83 | -3.08 | 0.46 | 270 |
| 3 | final_boosting | special | 3.93 | -1.60 | -2.93 | 0.42 | 270 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.404 | 1.393 | 0.416 | 0.890 | 12.214 | 0.888 | 7909 |
| final2 | events | 0.509 | 1.919 | 0.571 | 0.789 | 12.452 | 0.822 | 107 |
| final2 | cold_mornings | 0.473 | 1.676 | 0.485 | 0.846 | 13.124 | 0.806 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 11154 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 11153 | DUK | 2022-12-24 | final2 | 8.29 | -11.33 | -11.33 |
| 11150 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 11151 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 11152 | DUK | 2022-12-24 | final_ensemble | 8.26 | -14.16 | -14.16 |
| 11564 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 11563 | ERCO | 2021-02-17 | final2 | 29.35 | 23.99 | 0.00 |
| 11560 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 11561 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 11562 | ERCO | 2021-02-17 | final_ensemble | 30.28 | 26.83 | 0.00 |
| 11569 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 11568 | ERCO | 2021-02-18 | final2 | 7.05 | 5.55 | 0.00 |
| 11565 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 11566 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 11567 | ERCO | 2021-02-18 | final_ensemble | 7.68 | 4.44 | 0.00 |
| 22519 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 22518 | MISO | 2021-02-16 | final2 | 2.57 | 2.89 | 0.00 |
| 22515 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 22516 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 22517 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 33729 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 33728 | SWPP | 2021-02-15 | final2 | 1.83 | -1.71 | -1.71 |
| 33725 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 33726 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 33727 | SWPP | 2021-02-15 | final_ensemble | 2.21 | -3.25 | -3.25 |
| 33734 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 33733 | SWPP | 2021-02-16 | final2 | 6.21 | -0.62 | -0.62 |
| 33730 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 33731 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 33732 | SWPP | 2021-02-16 | final_ensemble | 5.49 | -1.39 | -1.39 |
| 40754 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 40753 | TVA | 2022-12-23 | final2 | 10.26 | -11.56 | -11.56 |
| 40750 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 40751 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 40752 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 40759 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 40758 | TVA | 2022-12-24 | final2 | 4.45 | -11.23 | -11.23 |
| 40755 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 40756 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 40757 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | BPAT | mape | 8.954 | 0.000 | 750 |
| final2 | CISO | mape | 3.258 | 0.001 | 737 |
| final2 | DUK | mape | 7.740 | 0.000 | 750 |
| final2 | ERCO | mape | 2.537 | 0.011 | 746 |
| final2 | FPL | mape | -1.848 | 0.065 | 690 |
| final2 | ISNE | mape | 15.636 | 0.000 | 752 |
| final2 | MISO | mape | -8.862 | 0.000 | 746 |
| final2 | NYIS | mape | -2.877 | 0.004 | 752 |
| final2 | PJM | mape | -3.041 | 0.002 | 744 |
| final2 | SWPP | mape | -16.355 | 0.000 | 745 |
| final2 | TVA | mape | 13.923 | 0.000 | 739 |
| final_additive | BPAT | mape | 12.541 | 0.000 | 750 |
| final_additive | CISO | mape | 17.909 | 0.000 | 737 |
| final_additive | DUK | mape | 10.152 | 0.000 | 750 |
| final_additive | ERCO | mape | 11.907 | 0.000 | 746 |
| final_additive | FPL | mape | 17.250 | 0.000 | 690 |
| final_additive | ISNE | mape | 21.098 | 0.000 | 752 |
| final_additive | MISO | mape | -2.885 | 0.004 | 746 |
| final_additive | NYIS | mape | 0.771 | 0.441 | 752 |
| final_additive | PJM | mape | 5.999 | 0.000 | 744 |
| final_additive | SWPP | mape | -14.342 | 0.000 | 745 |
| final_additive | TVA | mape | 17.307 | 0.000 | 739 |
| final_boosting | BPAT | mape | 12.457 | 0.000 | 750 |
| final_boosting | CISO | mape | 9.338 | 0.000 | 737 |
| final_boosting | DUK | mape | 10.290 | 0.000 | 750 |
| final_boosting | ERCO | mape | 6.704 | 0.000 | 746 |
| final_boosting | FPL | mape | 20.982 | 0.000 | 690 |
| final_boosting | ISNE | mape | 19.009 | 0.000 | 752 |
| final_boosting | MISO | mape | -3.438 | 0.001 | 746 |
| final_boosting | NYIS | mape | 0.532 | 0.595 | 752 |
| final_boosting | PJM | mape | 6.357 | 0.000 | 744 |
| final_boosting | SWPP | mape | -11.466 | 0.000 | 745 |
| final_boosting | TVA | mape | 16.453 | 0.000 | 739 |
| final_ensemble | BPAT | mape | 9.782 | 0.000 | 750 |
| final_ensemble | CISO | mape | 10.077 | 0.000 | 737 |
| final_ensemble | DUK | mape | 8.508 | 0.000 | 750 |
| final_ensemble | ERCO | mape | 6.848 | 0.000 | 746 |
| final_ensemble | FPL | mape | 18.289 | 0.000 | 690 |
| final_ensemble | ISNE | mape | 17.396 | 0.000 | 752 |
| final_ensemble | MISO | mape | -6.116 | 0.000 | 746 |
| final_ensemble | NYIS | mape | -2.860 | 0.004 | 752 |
| final_ensemble | PJM | mape | 2.785 | 0.005 | 744 |
| final_ensemble | SWPP | mape | -15.252 | 0.000 | 745 |
| final_ensemble | TVA | mape | 14.766 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final2 | 0.987 |
| final_additive | 0.976 |
| final_boosting | 0.987 |
| final_ensemble | 0.987 |
