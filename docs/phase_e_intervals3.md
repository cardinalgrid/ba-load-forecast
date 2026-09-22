# Phase E: intervals for the coldest days

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `final` is the recipe's interval (regime-conditional errors over a year, adaptive level per regime); `final_nn40` and `final_nn60` restrict the pool to the 40 or 60 known days nearest to the target day in forecast daily minimum temperature; `final_tail` reads the outer quantiles from an exponential fitted beyond the pool's 10th and 90th percentiles; `final_nn40_tail` does both.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final_nn40 | 2.53 | 2.20 | -0.64 | -1.74 | 1.30 | 0.62 | 0.30 | -48.85 | 8163 | 11.00 |
| final_nn40_tail | 2.53 | 2.20 | -0.64 | -1.74 | 1.30 | 0.62 | 0.30 | -48.85 | 8163 | 11.00 |
| final_nn60 | 2.53 | 2.19 | -0.69 | -1.77 | 1.28 | 0.62 | 0.29 | -48.85 | 8163 | 11.00 |
| final | 2.56 | 2.23 | -0.79 | -1.85 | 1.32 | 0.61 | 0.28 | -49.03 | 8163 | 11.00 |
| final_tail | 2.56 | 2.23 | -0.79 | -1.85 | 1.32 | 0.61 | 0.28 | -49.03 | 8163 | 11.00 |
| final_ensemble | 2.86 | 2.50 | -1.22 | -2.18 | 1.29 | 0.55 | 0.28 | -53.35 | 8163 | 11.00 |
| final_boosting | 3.01 | 2.65 | -0.99 | -2.12 | 1.50 | 0.52 | 0.28 | -52.25 | 8163 | 11.00 |
| DF | 3.04 | 2.74 | 0.09 | -1.26 | 1.08 | 0.00 | 0.00 | -53.60 | 8163 | 11.00 |
| final_additive | 3.12 | 2.74 | -1.46 | -2.46 | 1.42 | 0.51 | 0.26 | -54.20 | 8163 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | FPL | 3.92 | 3.63 | -3.97 | -4.36 | 1.21 | -53.60 |  |  | 700 | 15274.07 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 3.65 | 3.48 | -1.47 | -1.91 | 1.63 | -10.72 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.85 | 3.49 | 2.60 | -0.43 | 1.25 | -19.98 |  |  | 747 | 31342.11 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| final | BPAT | 2.52 | 2.20 | -1.00 | -1.87 | 1.87 | -18.57 | 0.37 | 0.22 | 750 | 6533.15 |
| final | CISO | 2.64 | 2.37 | -0.74 | -1.78 | 0.39 | -14.13 | 0.53 | 0.23 | 737 | 25196.91 |
| final | DUK | 3.31 | 2.95 | -1.14 | -2.53 | 1.35 | -16.31 | 0.40 | 0.27 | 750 | 12129.97 |
| final | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| final | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| final | ISNE | 3.43 | 2.95 | -0.27 | -1.80 | 0.52 | -18.28 | 0.31 | 0.17 | 752 | 13392.81 |
| final | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| final | NYIS | 2.45 | 2.05 | -0.52 | -1.67 | 0.55 | -13.12 | 0.58 | 0.66 | 752 | 17400.75 |
| final | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| final | SWPP | 2.42 | 1.94 | -0.75 | -1.74 | 1.53 | -21.32 | 0.72 | 0.09 | 747 | 31342.11 |
| final | TVA | 3.04 | 2.63 | -0.72 | -2.10 | 1.51 | -15.93 | 0.28 | 0.26 | 739 | 18562.62 |
| final_additive | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| final_additive | CISO | 3.72 | 3.19 | -2.94 | -3.83 | 0.41 | -18.17 | 0.32 | 0.15 | 737 | 25196.91 |
| final_additive | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| final_additive | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
| final_additive | FPL | 6.20 | 5.63 | -6.55 | -7.12 | 1.15 | -54.20 | 0.29 | 0.28 | 700 | 15274.07 |
| final_additive | ISNE | 3.86 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 752 | 13392.81 |
| final_additive | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| final_additive | NYIS | 2.72 | 2.37 | -0.86 | -2.08 | 0.60 | -15.67 | 0.51 | 0.60 | 752 | 17400.75 |
| final_additive | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.75 | 0.51 | 744 | 91927.69 |
| final_additive | SWPP | 2.61 | 2.11 | -0.25 | -1.59 | 1.54 | -20.36 | 0.70 | 0.10 | 747 | 31342.11 |
| final_additive | TVA | 3.35 | 2.97 | -1.05 | -2.35 | 1.42 | -14.12 | 0.25 | 0.26 | 739 | 18562.62 |
| final_boosting | BPAT | 2.73 | 2.43 | -0.43 | -1.57 | 2.00 | -18.16 | 0.27 | 0.24 | 750 | 6533.15 |
| final_boosting | CISO | 3.04 | 2.70 | -2.12 | -2.72 | 0.45 | -18.66 | 0.43 | 0.18 | 737 | 25196.91 |
| final_boosting | DUK | 3.58 | 3.12 | -0.42 | -2.27 | 1.50 | -16.82 | 0.33 | 0.27 | 750 | 12129.97 |
| final_boosting | ERCO | 3.13 | 2.72 | -2.27 | -2.98 | 1.29 | -15.00 | 0.35 | 0.18 | 746 | 46782.53 |
| final_boosting | FPL | 6.29 | 5.93 | -6.96 | -7.30 | 1.39 | -52.25 | 0.20 | 0.27 | 700 | 15274.07 |
| final_boosting | ISNE | 3.67 | 3.34 | -0.81 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 752 | 13392.81 |
| final_boosting | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| final_boosting | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.74 | -14.02 | 0.51 | 0.66 | 752 | 17400.75 |
| final_boosting | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.75 | 0.57 | 744 | 91927.69 |
| final_boosting | SWPP | 2.73 | 2.19 | -0.89 | -1.99 | 1.69 | -28.44 | 0.68 | 0.08 | 747 | 31342.11 |
| final_boosting | TVA | 3.28 | 2.85 | -0.22 | -1.84 | 1.54 | -15.24 | 0.24 | 0.30 | 739 | 18562.62 |
| final_ensemble | BPAT | 2.59 | 2.27 | -0.66 | -1.61 | 1.83 | -18.29 | 0.32 | 0.23 | 750 | 6533.15 |
| final_ensemble | CISO | 3.09 | 2.64 | -2.46 | -3.12 | 0.38 | -18.43 | 0.43 | 0.16 | 737 | 25196.91 |
| final_ensemble | DUK | 3.43 | 2.97 | -0.56 | -2.26 | 1.33 | -15.64 | 0.37 | 0.27 | 750 | 12129.97 |
| final_ensemble | ERCO | 3.13 | 2.70 | -2.25 | -2.89 | 1.07 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| final_ensemble | FPL | 6.05 | 5.68 | -6.70 | -7.08 | 1.17 | -53.35 | 0.26 | 0.27 | 700 | 15274.07 |
| final_ensemble | ISNE | 3.53 | 3.16 | -0.96 | -2.20 | 0.53 | -19.48 | 0.26 | 0.16 | 752 | 13392.81 |
| final_ensemble | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| final_ensemble | NYIS | 2.49 | 2.14 | -0.64 | -1.71 | 0.56 | -13.90 | 0.56 | 0.65 | 752 | 17400.75 |
| final_ensemble | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.79 | 0.55 | 744 | 91927.69 |
| final_ensemble | SWPP | 2.51 | 1.99 | -0.56 | -1.70 | 1.51 | -21.47 | 0.71 | 0.09 | 747 | 31342.11 |
| final_ensemble | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |
| final_nn40 | BPAT | 2.54 | 2.20 | -0.87 | -1.79 | 1.81 | -18.21 | 0.37 | 0.22 | 750 | 6533.15 |
| final_nn40 | CISO | 2.62 | 2.34 | -0.37 | -1.56 | 0.36 | -13.71 | 0.53 | 0.26 | 737 | 25196.91 |
| final_nn40 | DUK | 3.32 | 2.95 | -0.84 | -2.32 | 1.41 | -16.92 | 0.39 | 0.28 | 750 | 12129.97 |
| final_nn40 | ERCO | 2.76 | 2.37 | -0.66 | -1.89 | 1.13 | -15.20 | 0.44 | 0.24 | 746 | 46782.53 |
| final_nn40 | FPL | 3.74 | 3.27 | -2.13 | -3.50 | 1.19 | -48.85 | 0.61 | 0.60 | 700 | 15274.07 |
| final_nn40 | ISNE | 3.41 | 2.94 | -0.21 | -1.72 | 0.53 | -17.43 | 0.32 | 0.18 | 752 | 13392.81 |
| final_nn40 | MISO | 2.08 | 1.86 | -0.49 | -1.34 | 1.51 | -8.64 | 0.61 | 0.05 | 746 | 73788.38 |
| final_nn40 | NYIS | 2.47 | 2.09 | -0.53 | -1.68 | 0.56 | -12.93 | 0.58 | 0.65 | 752 | 17400.75 |
| final_nn40 | PJM | 2.27 | 1.99 | -0.62 | -1.65 | 1.61 | -11.26 | 0.86 | 0.52 | 744 | 91927.69 |
| final_nn40 | SWPP | 2.43 | 1.95 | -0.65 | -1.68 | 1.47 | -20.96 | 0.73 | 0.09 | 747 | 31342.11 |
| final_nn40 | TVA | 2.98 | 2.57 | -0.53 | -1.98 | 1.43 | -16.61 | 0.30 | 0.27 | 739 | 18562.62 |
| final_nn40_tail | BPAT | 2.54 | 2.20 | -0.87 | -1.79 | 1.81 | -18.21 | 0.37 | 0.22 | 750 | 6533.15 |
| final_nn40_tail | CISO | 2.62 | 2.34 | -0.37 | -1.56 | 0.36 | -13.71 | 0.53 | 0.26 | 737 | 25196.91 |
| final_nn40_tail | DUK | 3.32 | 2.95 | -0.84 | -2.32 | 1.41 | -16.92 | 0.39 | 0.28 | 750 | 12129.97 |
| final_nn40_tail | ERCO | 2.76 | 2.37 | -0.66 | -1.89 | 1.13 | -15.20 | 0.44 | 0.24 | 746 | 46782.53 |
| final_nn40_tail | FPL | 3.74 | 3.27 | -2.13 | -3.50 | 1.19 | -48.85 | 0.61 | 0.60 | 700 | 15274.07 |
| final_nn40_tail | ISNE | 3.41 | 2.94 | -0.21 | -1.72 | 0.53 | -17.43 | 0.32 | 0.18 | 752 | 13392.81 |
| final_nn40_tail | MISO | 2.08 | 1.86 | -0.49 | -1.34 | 1.51 | -8.64 | 0.61 | 0.05 | 746 | 73788.38 |
| final_nn40_tail | NYIS | 2.47 | 2.09 | -0.53 | -1.68 | 0.56 | -12.93 | 0.58 | 0.65 | 752 | 17400.75 |
| final_nn40_tail | PJM | 2.27 | 1.99 | -0.62 | -1.65 | 1.61 | -11.26 | 0.86 | 0.52 | 744 | 91927.69 |
| final_nn40_tail | SWPP | 2.43 | 1.95 | -0.65 | -1.68 | 1.47 | -20.96 | 0.73 | 0.09 | 747 | 31342.11 |
| final_nn40_tail | TVA | 2.98 | 2.57 | -0.53 | -1.98 | 1.43 | -16.61 | 0.30 | 0.27 | 739 | 18562.62 |
| final_nn60 | BPAT | 2.53 | 2.20 | -0.94 | -1.82 | 1.84 | -18.57 | 0.38 | 0.22 | 750 | 6533.15 |
| final_nn60 | CISO | 2.61 | 2.34 | -0.44 | -1.59 | 0.36 | -13.39 | 0.54 | 0.24 | 737 | 25196.91 |
| final_nn60 | DUK | 3.31 | 2.98 | -0.94 | -2.40 | 1.34 | -16.41 | 0.39 | 0.27 | 750 | 12129.97 |
| final_nn60 | ERCO | 2.77 | 2.32 | -0.64 | -1.88 | 1.11 | -15.34 | 0.43 | 0.23 | 746 | 46782.53 |
| final_nn60 | FPL | 3.76 | 3.31 | -2.12 | -3.50 | 1.18 | -48.85 | 0.60 | 0.60 | 700 | 15274.07 |
| final_nn60 | ISNE | 3.40 | 2.94 | -0.26 | -1.75 | 0.50 | -18.12 | 0.32 | 0.18 | 752 | 13392.81 |
| final_nn60 | MISO | 2.07 | 1.83 | -0.57 | -1.39 | 1.47 | -8.38 | 0.62 | 0.05 | 746 | 73788.38 |
| final_nn60 | NYIS | 2.45 | 2.06 | -0.54 | -1.68 | 0.54 | -12.93 | 0.59 | 0.65 | 752 | 17400.75 |
| final_nn60 | PJM | 2.28 | 1.99 | -0.68 | -1.68 | 1.59 | -11.26 | 0.85 | 0.52 | 744 | 91927.69 |
| final_nn60 | SWPP | 2.42 | 1.95 | -0.69 | -1.70 | 1.49 | -20.96 | 0.73 | 0.09 | 747 | 31342.11 |
| final_nn60 | TVA | 2.98 | 2.60 | -0.58 | -2.01 | 1.41 | -16.39 | 0.31 | 0.26 | 739 | 18562.62 |
| final_tail | BPAT | 2.52 | 2.20 | -1.00 | -1.87 | 1.87 | -18.57 | 0.37 | 0.22 | 750 | 6533.15 |
| final_tail | CISO | 2.64 | 2.37 | -0.74 | -1.78 | 0.39 | -14.13 | 0.53 | 0.23 | 737 | 25196.91 |
| final_tail | DUK | 3.31 | 2.95 | -1.14 | -2.53 | 1.35 | -16.31 | 0.40 | 0.27 | 750 | 12129.97 |
| final_tail | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| final_tail | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| final_tail | ISNE | 3.43 | 2.95 | -0.27 | -1.80 | 0.52 | -18.28 | 0.31 | 0.17 | 752 | 13392.81 |
| final_tail | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| final_tail | NYIS | 2.45 | 2.05 | -0.52 | -1.67 | 0.55 | -13.12 | 0.58 | 0.66 | 752 | 17400.75 |
| final_tail | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| final_tail | SWPP | 2.42 | 1.94 | -0.75 | -1.74 | 1.53 | -21.32 | 0.72 | 0.09 | 747 | 31342.11 |
| final_tail | TVA | 3.04 | 2.63 | -0.72 | -2.10 | 1.51 | -15.93 | 0.28 | 0.26 | 739 | 18562.62 |

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
| DF | PJM | uri | 2.82 | -1.01 | -1.14 | -2.03 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| final | CISO | uri | 1.74 | -0.55 | -0.92 | -1.78 | 6 |
| final | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| final | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| final | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| final | ISNE | uri | 2.71 | 1.07 | -0.50 | -2.56 | 6 |
| final | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| final | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| final | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| final | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| final | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
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
| final_nn40 | BPAT | uri | 2.86 | -0.42 | -1.10 | -4.38 | 6 |
| final_nn40 | CISO | uri | 1.82 | -0.50 | -0.98 | -2.28 | 6 |
| final_nn40 | DUK | uri | 3.50 | -2.19 | -2.50 | -4.37 | 6 |
| final_nn40 | ERCO | uri | 7.36 | -10.21 | -10.21 | -11.22 | 2 |
| final_nn40 | FPL | uri | 8.47 | -9.80 | -9.80 | -12.97 | 6 |
| final_nn40 | ISNE | uri | 2.69 | 1.19 | -0.44 | -2.10 | 6 |
| final_nn40 | MISO | uri | 3.52 | -2.96 | -3.25 | -6.49 | 5 |
| final_nn40 | NYIS | uri | 1.96 | 1.60 | -0.25 | -1.52 | 6 |
| final_nn40 | PJM | uri | 1.81 | -0.48 | -0.90 | -2.83 | 6 |
| final_nn40 | SWPP | uri | 6.38 | 0.32 | -2.77 | -6.51 | 4 |
| final_nn40 | TVA | uri | 3.02 | -2.44 | -3.10 | -6.07 | 6 |
| final_nn40_tail | BPAT | uri | 2.86 | -0.42 | -1.10 | -4.38 | 6 |
| final_nn40_tail | CISO | uri | 1.82 | -0.50 | -0.98 | -2.28 | 6 |
| final_nn40_tail | DUK | uri | 3.50 | -2.19 | -2.50 | -4.37 | 6 |
| final_nn40_tail | ERCO | uri | 7.36 | -10.21 | -10.21 | -11.22 | 2 |
| final_nn40_tail | FPL | uri | 8.47 | -9.80 | -9.80 | -12.97 | 6 |
| final_nn40_tail | ISNE | uri | 2.69 | 1.19 | -0.44 | -2.10 | 6 |
| final_nn40_tail | MISO | uri | 3.52 | -2.96 | -3.25 | -6.49 | 5 |
| final_nn40_tail | NYIS | uri | 1.96 | 1.60 | -0.25 | -1.52 | 6 |
| final_nn40_tail | PJM | uri | 1.81 | -0.48 | -0.90 | -2.83 | 6 |
| final_nn40_tail | SWPP | uri | 6.38 | 0.32 | -2.77 | -6.51 | 4 |
| final_nn40_tail | TVA | uri | 3.02 | -2.44 | -3.10 | -6.07 | 6 |
| final_nn60 | BPAT | uri | 2.78 | -1.16 | -1.50 | -5.07 | 6 |
| final_nn60 | CISO | uri | 1.78 | -0.39 | -0.87 | -1.79 | 6 |
| final_nn60 | DUK | uri | 3.45 | -2.73 | -2.80 | -5.08 | 6 |
| final_nn60 | ERCO | uri | 6.97 | -9.89 | -9.89 | -10.48 | 2 |
| final_nn60 | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| final_nn60 | ISNE | uri | 2.71 | 1.11 | -0.50 | -2.26 | 6 |
| final_nn60 | MISO | uri | 3.50 | -3.07 | -3.22 | -6.39 | 5 |
| final_nn60 | NYIS | uri | 1.95 | 1.56 | -0.23 | -1.40 | 6 |
| final_nn60 | PJM | uri | 1.84 | -0.34 | -0.85 | -3.05 | 6 |
| final_nn60 | SWPP | uri | 6.13 | 0.77 | -2.61 | -6.52 | 4 |
| final_nn60 | TVA | uri | 2.94 | -2.61 | -3.16 | -5.92 | 6 |
| final_tail | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| final_tail | CISO | uri | 1.74 | -0.55 | -0.92 | -1.78 | 6 |
| final_tail | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| final_tail | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| final_tail | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| final_tail | ISNE | uri | 2.71 | 1.07 | -0.50 | -2.56 | 6 |
| final_tail | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| final_tail | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| final_tail | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| final_tail | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| final_tail | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 4.02 | -3.14 | -3.14 | -5.88 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final | BPAT | elliott | 4.33 | -3.84 | -4.19 | -8.42 | 5 |
| final | CISO | elliott | 3.28 | 1.03 | -0.92 | -4.25 | 5 |
| final | DUK | elliott | 3.38 | -3.22 | -3.22 | -5.20 | 4 |
| final | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| final | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| final | ISNE | elliott | 3.31 | 1.20 | -0.77 | -1.98 | 5 |
| final | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| final | NYIS | elliott | 2.77 | -0.78 | -1.63 | -3.23 | 5 |
| final | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| final | SWPP | elliott | 4.17 | -1.47 | -2.82 | -6.59 | 5 |
| final | TVA | elliott | 6.17 | 1.48 | -0.79 | -1.40 | 3 |
| final_additive | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| final_additive | CISO | elliott | 3.76 | 2.62 | -0.56 | -2.81 | 5 |
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
| final_boosting | CISO | elliott | 3.86 | 1.39 | -0.79 | -3.74 | 5 |
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
| final_ensemble | CISO | elliott | 3.49 | 1.95 | -0.66 | -3.32 | 5 |
| final_ensemble | DUK | elliott | 3.71 | -3.00 | -3.00 | -3.88 | 4 |
| final_ensemble | ERCO | elliott | 6.73 | -4.28 | -5.36 | -12.60 | 5 |
| final_ensemble | FPL | elliott | 8.81 | -10.29 | -10.53 | -14.82 | 5 |
| final_ensemble | ISNE | elliott | 3.39 | 2.09 | -0.44 | -1.16 | 5 |
| final_ensemble | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| final_ensemble | NYIS | elliott | 2.73 | -1.04 | -1.83 | -3.53 | 5 |
| final_ensemble | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| final_ensemble | SWPP | elliott | 4.12 | -2.20 | -3.22 | -7.26 | 5 |
| final_ensemble | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |
| final_nn40 | BPAT | elliott | 3.75 | -3.37 | -3.68 | -7.52 | 5 |
| final_nn40 | CISO | elliott | 3.09 | 0.96 | -0.97 | -4.36 | 5 |
| final_nn40 | DUK | elliott | 3.19 | -1.98 | -2.07 | -5.21 | 4 |
| final_nn40 | ERCO | elliott | 6.87 | -1.96 | -4.23 | -9.87 | 5 |
| final_nn40 | FPL | elliott | 7.99 | -9.17 | -9.41 | -14.82 | 5 |
| final_nn40 | ISNE | elliott | 3.45 | 1.01 | -0.95 | -2.75 | 5 |
| final_nn40 | MISO | elliott | 3.40 | -2.09 | -3.04 | -4.39 | 5 |
| final_nn40 | NYIS | elliott | 2.87 | -1.55 | -2.17 | -4.05 | 5 |
| final_nn40 | PJM | elliott | 4.25 | -3.07 | -3.35 | -6.86 | 5 |
| final_nn40 | SWPP | elliott | 4.57 | -0.24 | -2.15 | -5.66 | 5 |
| final_nn40 | TVA | elliott | 6.44 | 3.16 | 0.00 | 0.00 | 3 |
| final_nn40_tail | BPAT | elliott | 3.75 | -3.37 | -3.68 | -7.52 | 5 |
| final_nn40_tail | CISO | elliott | 3.09 | 0.96 | -0.97 | -4.36 | 5 |
| final_nn40_tail | DUK | elliott | 3.19 | -1.98 | -2.07 | -5.21 | 4 |
| final_nn40_tail | ERCO | elliott | 6.87 | -1.96 | -4.23 | -9.87 | 5 |
| final_nn40_tail | FPL | elliott | 7.99 | -9.17 | -9.41 | -14.82 | 5 |
| final_nn40_tail | ISNE | elliott | 3.45 | 1.01 | -0.95 | -2.75 | 5 |
| final_nn40_tail | MISO | elliott | 3.40 | -2.09 | -3.04 | -4.39 | 5 |
| final_nn40_tail | NYIS | elliott | 2.87 | -1.55 | -2.17 | -4.05 | 5 |
| final_nn40_tail | PJM | elliott | 4.25 | -3.07 | -3.35 | -6.86 | 5 |
| final_nn40_tail | SWPP | elliott | 4.57 | -0.24 | -2.15 | -5.66 | 5 |
| final_nn40_tail | TVA | elliott | 6.44 | 3.16 | 0.00 | 0.00 | 3 |
| final_nn60 | BPAT | elliott | 3.84 | -3.37 | -3.66 | -7.52 | 5 |
| final_nn60 | CISO | elliott | 3.15 | 1.01 | -0.94 | -4.44 | 5 |
| final_nn60 | DUK | elliott | 3.16 | -2.21 | -2.21 | -5.04 | 4 |
| final_nn60 | ERCO | elliott | 6.79 | -2.98 | -4.81 | -11.06 | 5 |
| final_nn60 | FPL | elliott | 7.99 | -9.24 | -9.48 | -14.82 | 5 |
| final_nn60 | ISNE | elliott | 3.70 | 1.10 | -0.96 | -2.91 | 5 |
| final_nn60 | MISO | elliott | 3.45 | -1.94 | -2.94 | -4.37 | 5 |
| final_nn60 | NYIS | elliott | 2.89 | -1.58 | -2.22 | -4.23 | 5 |
| final_nn60 | PJM | elliott | 4.27 | -3.08 | -3.45 | -6.85 | 5 |
| final_nn60 | SWPP | elliott | 4.41 | -0.61 | -2.44 | -6.17 | 5 |
| final_nn60 | TVA | elliott | 6.31 | 3.08 | 0.00 | 0.00 | 3 |
| final_tail | BPAT | elliott | 4.33 | -3.84 | -4.19 | -8.42 | 5 |
| final_tail | CISO | elliott | 3.28 | 1.03 | -0.92 | -4.25 | 5 |
| final_tail | DUK | elliott | 3.38 | -3.22 | -3.22 | -5.20 | 4 |
| final_tail | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| final_tail | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| final_tail | ISNE | elliott | 3.31 | 1.20 | -0.77 | -1.98 | 5 |
| final_tail | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| final_tail | NYIS | elliott | 2.77 | -0.78 | -1.63 | -3.23 | 5 |
| final_tail | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| final_tail | SWPP | elliott | 4.17 | -1.47 | -2.82 | -6.59 | 5 |
| final_tail | TVA | elliott | 6.17 | 1.48 | -0.79 | -1.40 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | final_nn60 | eve | 3.46 | 0.38 | -1.72 | 0.48 | 268 |
| 9 | DF | eve | 3.47 | 0.40 | -1.41 |  | 268 |
| 14 | final_nn40 | eve | 3.47 | 0.36 | -1.73 | 0.48 | 268 |
| 15 | final_nn40_tail | eve | 3.47 | 0.36 | -1.73 | 0.48 | 268 |
| 10 | final | eve | 3.52 | 0.34 | -1.77 | 0.47 | 268 |
| 17 | final_tail | eve | 3.52 | 0.34 | -1.77 | 0.47 | 268 |
| 13 | final_ensemble | eve | 3.62 | -0.13 | -2.04 | 0.46 | 268 |
| 11 | final_additive | eve | 3.83 | -0.16 | -2.20 | 0.43 | 268 |
| 12 | final_boosting | eve | 3.86 | -0.09 | -2.12 | 0.43 | 268 |
| 1 | final | special | 3.40 | -1.33 | -2.53 | 0.53 | 270 |
| 8 | final_tail | special | 3.40 | -1.33 | -2.53 | 0.53 | 270 |
| 7 | final_nn60 | special | 3.40 | -1.23 | -2.48 | 0.54 | 270 |
| 5 | final_nn40 | special | 3.41 | -1.24 | -2.49 | 0.54 | 270 |
| 6 | final_nn40_tail | special | 3.41 | -1.24 | -2.49 | 0.54 | 270 |
| 4 | final_ensemble | special | 3.61 | -1.76 | -2.90 | 0.53 | 270 |
| 0 | DF | special | 3.80 | -0.17 | -1.78 |  | 270 |
| 2 | final_additive | special | 3.84 | -1.88 | -3.09 | 0.48 | 270 |
| 3 | final_boosting | special | 3.93 | -1.61 | -2.93 | 0.44 | 270 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final | all | 0.403 | 1.405 | 0.410 | 0.895 | 12.221 | 0.888 | 7921 |
| final_nn40 | all | 0.405 | 1.390 | 0.417 | 0.890 | 12.171 | 0.884 | 7921 |
| final_nn40_tail | all | 0.405 | 1.390 | 0.416 | 0.893 | 12.322 | 0.886 | 7921 |
| final_nn60 | all | 0.399 | 1.389 | 0.411 | 0.893 | 12.130 | 0.888 | 7921 |
| final_tail | all | 0.403 | 1.405 | 0.410 | 0.896 | 12.260 | 0.886 | 7921 |
| final | events | 0.493 | 1.914 | 0.621 | 0.769 | 11.765 | 0.785 | 107 |
| final_nn40 | events | 0.501 | 1.931 | 0.591 | 0.780 | 12.435 | 0.785 | 107 |
| final_nn40_tail | events | 0.497 | 1.931 | 0.578 | 0.787 | 12.539 | 0.785 | 107 |
| final_nn60 | events | 0.483 | 1.924 | 0.595 | 0.786 | 12.129 | 0.794 | 107 |
| final_tail | events | 0.491 | 1.914 | 0.619 | 0.771 | 11.814 | 0.776 | 107 |
| final | cold_mornings | 0.460 | 1.728 | 0.530 | 0.807 | 12.005 | 0.773 | 330 |
| final_nn40 | cold_mornings | 0.468 | 1.689 | 0.496 | 0.843 | 13.107 | 0.803 | 330 |
| final_nn40_tail | cold_mornings | 0.473 | 1.689 | 0.492 | 0.846 | 13.243 | 0.812 | 330 |
| final_nn60 | cold_mornings | 0.459 | 1.692 | 0.500 | 0.836 | 12.807 | 0.803 | 330 |
| final_tail | cold_mornings | 0.464 | 1.728 | 0.532 | 0.811 | 12.135 | 0.779 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 20078 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 20073 | DUK | 2022-12-24 | final | 9.09 | -14.17 | -14.17 |
| 20070 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 20071 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 20072 | DUK | 2022-12-24 | final_ensemble | 8.26 | -14.16 | -14.16 |
| 20074 | DUK | 2022-12-24 | final_nn40 | 8.55 | -12.48 | -12.48 |
| 20077 | DUK | 2022-12-24 | final_nn40_tail | 8.55 | -12.48 | -12.48 |
| 20075 | DUK | 2022-12-24 | final_nn60 | 9.01 | -13.15 | -13.15 |
| 20076 | DUK | 2022-12-24 | final_tail | 9.09 | -14.17 | -14.17 |
| 20816 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 20811 | ERCO | 2021-02-15 | final | 33.61 | -10.86 | -10.86 |
| 20808 | ERCO | 2021-02-15 | final_additive | 41.72 | -4.24 | -4.24 |
| 20809 | ERCO | 2021-02-15 | final_boosting | 27.39 | -16.57 | -16.57 |
| 20810 | ERCO | 2021-02-15 | final_ensemble | 34.57 | -10.39 | -10.39 |
| 20812 | ERCO | 2021-02-15 | final_nn40 | 33.10 | -10.91 | -10.91 |
| 20815 | ERCO | 2021-02-15 | final_nn40_tail | 33.10 | -10.91 | -10.91 |
| 20813 | ERCO | 2021-02-15 | final_nn60 | 33.45 | -10.91 | -10.91 |
| 20814 | ERCO | 2021-02-15 | final_tail | 33.61 | -10.86 | -10.86 |
| 20825 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 20820 | ERCO | 2021-02-16 | final | 39.49 | 37.58 | 0.00 |
| 20817 | ERCO | 2021-02-16 | final_additive | 47.08 | 43.33 | 0.00 |
| 20818 | ERCO | 2021-02-16 | final_boosting | 33.46 | 31.10 | 0.00 |
| 20819 | ERCO | 2021-02-16 | final_ensemble | 40.43 | 37.36 | 0.00 |
| 20821 | ERCO | 2021-02-16 | final_nn40 | 39.00 | 37.98 | 0.00 |
| 20824 | ERCO | 2021-02-16 | final_nn40_tail | 39.00 | 37.98 | 0.00 |
| 20822 | ERCO | 2021-02-16 | final_nn60 | 39.29 | 37.58 | 0.00 |
| 20823 | ERCO | 2021-02-16 | final_tail | 39.49 | 37.58 | 0.00 |
| 20834 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 20829 | ERCO | 2021-02-17 | final | 29.39 | 23.92 | 0.00 |
| 20826 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 20827 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 20828 | ERCO | 2021-02-17 | final_ensemble | 30.28 | 26.83 | 0.00 |
| 20830 | ERCO | 2021-02-17 | final_nn40 | 28.94 | 23.46 | 0.00 |
| 20833 | ERCO | 2021-02-17 | final_nn40_tail | 28.94 | 23.46 | 0.00 |
| 20831 | ERCO | 2021-02-17 | final_nn60 | 29.21 | 23.61 | 0.00 |
| 20832 | ERCO | 2021-02-17 | final_tail | 29.39 | 23.92 | 0.00 |
| 20843 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 20838 | ERCO | 2021-02-18 | final | 6.89 | 4.76 | 0.00 |
| 20835 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 20836 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 20837 | ERCO | 2021-02-18 | final_ensemble | 7.68 | 4.44 | 0.00 |
| 20839 | ERCO | 2021-02-18 | final_nn40 | 6.60 | 5.01 | 0.00 |
| 20842 | ERCO | 2021-02-18 | final_nn40_tail | 6.60 | 5.01 | 0.00 |
| 20840 | ERCO | 2021-02-18 | final_nn60 | 6.67 | 4.45 | 0.00 |
| 20841 | ERCO | 2021-02-18 | final_tail | 6.89 | 4.76 | 0.00 |
| 40643 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 40638 | MISO | 2021-02-16 | final | 2.07 | 1.67 | 0.00 |
| 40635 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 40636 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 40637 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 40639 | MISO | 2021-02-16 | final_nn40 | 2.27 | 2.53 | 0.00 |
| 40642 | MISO | 2021-02-16 | final_nn40_tail | 2.27 | 2.53 | 0.00 |
| 40640 | MISO | 2021-02-16 | final_nn60 | 2.14 | 1.79 | 0.00 |
| 40641 | MISO | 2021-02-16 | final_tail | 2.07 | 1.67 | 0.00 |
| 60821 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 60816 | SWPP | 2021-02-15 | final | 2.08 | -2.08 | -2.08 |
| 60813 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 60814 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 60815 | SWPP | 2021-02-15 | final_ensemble | 2.21 | -3.25 | -3.25 |
| 60817 | SWPP | 2021-02-15 | final_nn40 | 1.95 | -2.08 | -2.08 |
| 60820 | SWPP | 2021-02-15 | final_nn40_tail | 1.95 | -2.08 | -2.08 |
| 60818 | SWPP | 2021-02-15 | final_nn60 | 2.01 | -1.88 | -1.88 |
| 60819 | SWPP | 2021-02-15 | final_tail | 2.08 | -2.08 | -2.08 |
| 60830 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 60825 | SWPP | 2021-02-16 | final | 5.52 | -1.24 | -1.24 |
| 60822 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 60823 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 60824 | SWPP | 2021-02-16 | final_ensemble | 5.49 | -1.39 | -1.39 |
| 60826 | SWPP | 2021-02-16 | final_nn40 | 5.91 | -1.86 | -1.86 |
| 60829 | SWPP | 2021-02-16 | final_nn40_tail | 5.91 | -1.86 | -1.86 |
| 60827 | SWPP | 2021-02-16 | final_nn60 | 5.51 | -0.59 | -0.59 |
| 60828 | SWPP | 2021-02-16 | final_tail | 5.52 | -1.24 | -1.24 |
| 73484 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 73479 | TVA | 2022-12-23 | final | 10.85 | -12.10 | -12.10 |
| 73476 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 73477 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 73478 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 73480 | TVA | 2022-12-23 | final_nn40 | 10.45 | -12.10 | -12.10 |
| 73483 | TVA | 2022-12-23 | final_nn40_tail | 10.45 | -12.10 | -12.10 |
| 73481 | TVA | 2022-12-23 | final_nn60 | 10.69 | -12.28 | -12.28 |
| 73482 | TVA | 2022-12-23 | final_tail | 10.85 | -12.10 | -12.10 |
| 73493 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 73488 | TVA | 2022-12-24 | final | 4.93 | -11.86 | -11.86 |
| 73485 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 73486 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 73487 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |
| 73489 | TVA | 2022-12-24 | final_nn40 | 4.58 | -11.23 | -11.23 |
| 73492 | TVA | 2022-12-24 | final_nn40_tail | 4.58 | -11.23 | -11.23 |
| 73490 | TVA | 2022-12-24 | final_nn60 | 4.68 | -11.29 | -11.29 |
| 73491 | TVA | 2022-12-24 | final_tail | 4.93 | -11.86 | -11.86 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final | BPAT | mape | 8.324 | 0.000 | 750 |
| final | CISO | mape | -2.368 | 0.018 | 737 |
| final | DUK | mape | 6.960 | 0.000 | 750 |
| final | ERCO | mape | 2.542 | 0.011 | 746 |
| final | FPL | mape | -0.133 | 0.895 | 700 |
| final | ISNE | mape | 15.485 | 0.000 | 752 |
| final | MISO | mape | -8.669 | 0.000 | 746 |
| final | NYIS | mape | -3.388 | 0.001 | 752 |
| final | PJM | mape | -25.615 | 0.000 | 744 |
| final | SWPP | mape | -16.212 | 0.000 | 747 |
| final | TVA | mape | 14.282 | 0.000 | 739 |
| final_additive | BPAT | mape | 12.541 | 0.000 | 750 |
| final_additive | CISO | mape | 12.049 | 0.000 | 737 |
| final_additive | DUK | mape | 10.152 | 0.000 | 750 |
| final_additive | ERCO | mape | 11.907 | 0.000 | 746 |
| final_additive | FPL | mape | 17.271 | 0.000 | 700 |
| final_additive | ISNE | mape | 21.098 | 0.000 | 752 |
| final_additive | MISO | mape | -2.885 | 0.004 | 746 |
| final_additive | NYIS | mape | 0.771 | 0.441 | 752 |
| final_additive | PJM | mape | -14.911 | 0.000 | 744 |
| final_additive | SWPP | mape | -14.397 | 0.000 | 747 |
| final_additive | TVA | mape | 17.307 | 0.000 | 739 |
| final_boosting | BPAT | mape | 12.457 | 0.000 | 750 |
| final_boosting | CISO | mape | 3.470 | 0.001 | 737 |
| final_boosting | DUK | mape | 10.290 | 0.000 | 750 |
| final_boosting | ERCO | mape | 6.704 | 0.000 | 746 |
| final_boosting | FPL | mape | 21.017 | 0.000 | 700 |
| final_boosting | ISNE | mape | 19.009 | 0.000 | 752 |
| final_boosting | MISO | mape | -3.438 | 0.001 | 746 |
| final_boosting | NYIS | mape | 0.532 | 0.595 | 752 |
| final_boosting | PJM | mape | -14.855 | 0.000 | 744 |
| final_boosting | SWPP | mape | -11.406 | 0.000 | 747 |
| final_boosting | TVA | mape | 16.453 | 0.000 | 739 |
| final_ensemble | BPAT | mape | 9.782 | 0.000 | 750 |
| final_ensemble | CISO | mape | 4.079 | 0.000 | 737 |
| final_ensemble | DUK | mape | 8.508 | 0.000 | 750 |
| final_ensemble | ERCO | mape | 6.848 | 0.000 | 746 |
| final_ensemble | FPL | mape | 18.299 | 0.000 | 700 |
| final_ensemble | ISNE | mape | 17.396 | 0.000 | 752 |
| final_ensemble | MISO | mape | -6.116 | 0.000 | 746 |
| final_ensemble | NYIS | mape | -2.860 | 0.004 | 752 |
| final_ensemble | PJM | mape | -19.327 | 0.000 | 744 |
| final_ensemble | SWPP | mape | -15.215 | 0.000 | 747 |
| final_ensemble | TVA | mape | 14.766 | 0.000 | 739 |
| final_nn40 | BPAT | mape | 8.591 | 0.000 | 750 |
| final_nn40 | CISO | mape | -2.737 | 0.006 | 737 |
| final_nn40 | DUK | mape | 7.297 | 0.000 | 750 |
| final_nn40 | ERCO | mape | 2.014 | 0.044 | 746 |
| final_nn40 | FPL | mape | -2.208 | 0.027 | 700 |
| final_nn40 | ISNE | mape | 15.297 | 0.000 | 752 |
| final_nn40 | MISO | mape | -9.074 | 0.000 | 746 |
| final_nn40 | NYIS | mape | -3.060 | 0.002 | 752 |
| final_nn40 | PJM | mape | -26.955 | 0.000 | 744 |
| final_nn40 | SWPP | mape | -16.107 | 0.000 | 747 |
| final_nn40 | TVA | mape | 13.310 | 0.000 | 739 |
| final_nn40_tail | BPAT | mape | 8.591 | 0.000 | 750 |
| final_nn40_tail | CISO | mape | -2.737 | 0.006 | 737 |
| final_nn40_tail | DUK | mape | 7.297 | 0.000 | 750 |
| final_nn40_tail | ERCO | mape | 2.014 | 0.044 | 746 |
| final_nn40_tail | FPL | mape | -2.208 | 0.027 | 700 |
| final_nn40_tail | ISNE | mape | 15.297 | 0.000 | 752 |
| final_nn40_tail | MISO | mape | -9.074 | 0.000 | 746 |
| final_nn40_tail | NYIS | mape | -3.060 | 0.002 | 752 |
| final_nn40_tail | PJM | mape | -26.955 | 0.000 | 744 |
| final_nn40_tail | SWPP | mape | -16.107 | 0.000 | 747 |
| final_nn40_tail | TVA | mape | 13.310 | 0.000 | 739 |
| final_nn60 | BPAT | mape | 8.495 | 0.000 | 750 |
| final_nn60 | CISO | mape | -2.806 | 0.005 | 737 |
| final_nn60 | DUK | mape | 7.109 | 0.000 | 750 |
| final_nn60 | ERCO | mape | 2.261 | 0.024 | 746 |
| final_nn60 | FPL | mape | -2.036 | 0.042 | 700 |
| final_nn60 | ISNE | mape | 15.291 | 0.000 | 752 |
| final_nn60 | MISO | mape | -9.055 | 0.000 | 746 |
| final_nn60 | NYIS | mape | -3.330 | 0.001 | 752 |
| final_nn60 | PJM | mape | -26.854 | 0.000 | 744 |
| final_nn60 | SWPP | mape | -16.264 | 0.000 | 747 |
| final_nn60 | TVA | mape | 13.346 | 0.000 | 739 |
| final_tail | BPAT | mape | 8.324 | 0.000 | 750 |
| final_tail | CISO | mape | -2.368 | 0.018 | 737 |
| final_tail | DUK | mape | 6.960 | 0.000 | 750 |
| final_tail | ERCO | mape | 2.542 | 0.011 | 746 |
| final_tail | FPL | mape | -0.133 | 0.895 | 700 |
| final_tail | ISNE | mape | 15.485 | 0.000 | 752 |
| final_tail | MISO | mape | -8.669 | 0.000 | 746 |
| final_tail | NYIS | mape | -3.388 | 0.001 | 752 |
| final_tail | PJM | mape | -25.615 | 0.000 | 744 |
| final_tail | SWPP | mape | -16.212 | 0.000 | 747 |
| final_tail | TVA | mape | 14.282 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final | 0.992 |
| final_additive | 0.981 |
| final_boosting | 0.992 |
| final_ensemble | 0.992 |
| final_nn40 | 0.992 |
| final_nn40_tail | 0.992 |
| final_nn60 | 0.992 |
| final_tail | 0.992 |
