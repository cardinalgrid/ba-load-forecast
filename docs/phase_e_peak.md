# Phase E: the under-forecast at the daily peak

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `final` is the recipe; `final_peak_lift` replaces the hourly median correction, at the hours within 3 % of the forecast maximum, by the median of the errors measured at the actual peak hour of the pool days; `final_peak_q55` and `final_peak_q60` read the point at the 55th or 60th percentile of the errors at those hours instead of the median. The 90 % band moves with the point.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final | 2.56 | 2.23 | -0.79 | -1.85 | 1.32 | 0.61 | 0.28 | -49.03 | 8163 | 11.00 |
| final_peak_q55 | 2.57 | 2.24 | -0.42 | -1.64 | 1.32 | 0.61 | 0.31 | -49.03 | 8163 | 11.00 |
| final_peak_q60 | 2.58 | 2.24 | -0.03 | -1.44 | 1.32 | 0.60 | 0.33 | -49.03 | 8163 | 11.00 |
| final_peak_lift | 2.58 | 2.24 | -0.10 | -1.46 | 1.29 | 0.60 | 0.33 | -49.03 | 8163 | 11.00 |
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
| final_peak_lift | BPAT | 2.55 | 2.21 | -0.24 | -1.42 | 1.84 | -18.57 | 0.35 | 0.26 | 750 | 6533.15 |
| final_peak_lift | CISO | 2.65 | 2.36 | -0.47 | -1.64 | 0.39 | -14.13 | 0.53 | 0.24 | 737 | 25196.91 |
| final_peak_lift | DUK | 3.35 | 2.97 | 0.03 | -1.92 | 1.33 | -16.13 | 0.39 | 0.31 | 750 | 12129.97 |
| final_peak_lift | ERCO | 2.82 | 2.42 | 0.05 | -1.51 | 1.07 | -13.33 | 0.43 | 0.27 | 746 | 46782.53 |
| final_peak_lift | FPL | 3.93 | 3.48 | -1.41 | -3.17 | 1.15 | -49.03 | 0.57 | 0.62 | 700 | 15274.07 |
| final_peak_lift | ISNE | 3.44 | 2.97 | 0.19 | -1.58 | 0.52 | -18.28 | 0.31 | 0.20 | 752 | 13392.81 |
| final_peak_lift | MISO | 2.11 | 1.83 | 0.00 | -1.06 | 1.56 | -8.39 | 0.60 | 0.07 | 746 | 73788.38 |
| final_peak_lift | NYIS | 2.47 | 2.08 | 0.09 | -1.35 | 0.56 | -12.37 | 0.57 | 0.71 | 752 | 17400.75 |
| final_peak_lift | PJM | 2.35 | 2.07 | -0.15 | -1.42 | 1.56 | -11.20 | 0.84 | 0.56 | 744 | 91927.69 |
| final_peak_lift | SWPP | 2.45 | 1.97 | 0.05 | -1.28 | 1.52 | -21.32 | 0.73 | 0.11 | 747 | 31342.11 |
| final_peak_lift | TVA | 3.08 | 2.70 | 0.24 | -1.55 | 1.45 | -13.83 | 0.27 | 0.33 | 739 | 18562.62 |
| final_peak_q55 | BPAT | 2.52 | 2.21 | -0.69 | -1.67 | 1.80 | -18.57 | 0.37 | 0.24 | 750 | 6533.15 |
| final_peak_q55 | CISO | 2.64 | 2.35 | -0.36 | -1.59 | 0.39 | -13.79 | 0.53 | 0.25 | 737 | 25196.91 |
| final_peak_q55 | DUK | 3.32 | 2.97 | -0.63 | -2.26 | 1.37 | -15.96 | 0.40 | 0.28 | 750 | 12129.97 |
| final_peak_q55 | ERCO | 2.80 | 2.45 | -0.32 | -1.73 | 1.10 | -14.85 | 0.43 | 0.25 | 746 | 46782.53 |
| final_peak_q55 | FPL | 3.91 | 3.50 | -1.90 | -3.42 | 1.16 | -49.03 | 0.57 | 0.61 | 700 | 15274.07 |
| final_peak_q55 | ISNE | 3.44 | 2.97 | 0.15 | -1.61 | 0.52 | -18.28 | 0.31 | 0.20 | 752 | 13392.81 |
| final_peak_q55 | MISO | 2.09 | 1.84 | -0.31 | -1.24 | 1.58 | -8.29 | 0.61 | 0.06 | 746 | 73788.38 |
| final_peak_q55 | NYIS | 2.45 | 2.06 | -0.19 | -1.48 | 0.57 | -12.84 | 0.58 | 0.68 | 752 | 17400.75 |
| final_peak_q55 | PJM | 2.34 | 2.07 | -0.43 | -1.57 | 1.59 | -10.98 | 0.84 | 0.53 | 744 | 91927.69 |
| final_peak_q55 | SWPP | 2.42 | 1.93 | -0.41 | -1.54 | 1.54 | -21.32 | 0.73 | 0.10 | 747 | 31342.11 |
| final_peak_q55 | TVA | 3.06 | 2.67 | -0.28 | -1.87 | 1.57 | -15.60 | 0.27 | 0.29 | 739 | 18562.62 |
| final_peak_q60 | BPAT | 2.53 | 2.20 | -0.39 | -1.50 | 1.86 | -18.57 | 0.36 | 0.25 | 750 | 6533.15 |
| final_peak_q60 | CISO | 2.65 | 2.37 | 0.05 | -1.39 | 0.38 | -13.30 | 0.53 | 0.28 | 737 | 25196.91 |
| final_peak_q60 | DUK | 3.33 | 2.99 | -0.08 | -1.98 | 1.35 | -14.83 | 0.40 | 0.30 | 750 | 12129.97 |
| final_peak_q60 | ERCO | 2.82 | 2.43 | 0.11 | -1.53 | 1.14 | -14.45 | 0.43 | 0.27 | 746 | 46782.53 |
| final_peak_q60 | FPL | 3.92 | 3.46 | -1.21 | -3.06 | 1.13 | -49.03 | 0.57 | 0.64 | 700 | 15274.07 |
| final_peak_q60 | ISNE | 3.46 | 2.99 | 0.60 | -1.42 | 0.51 | -18.28 | 0.30 | 0.21 | 752 | 13392.81 |
| final_peak_q60 | MISO | 2.10 | 1.83 | 0.00 | -1.07 | 1.61 | -7.93 | 0.61 | 0.06 | 746 | 73788.38 |
| final_peak_q60 | NYIS | 2.46 | 2.08 | 0.13 | -1.32 | 0.61 | -12.56 | 0.58 | 0.71 | 752 | 17400.75 |
| final_peak_q60 | PJM | 2.34 | 2.06 | -0.07 | -1.38 | 1.58 | -10.77 | 0.84 | 0.57 | 744 | 91927.69 |
| final_peak_q60 | SWPP | 2.43 | 1.95 | -0.06 | -1.36 | 1.52 | -21.32 | 0.72 | 0.11 | 747 | 31342.11 |
| final_peak_q60 | TVA | 3.08 | 2.68 | 0.21 | -1.63 | 1.52 | -15.09 | 0.26 | 0.31 | 739 | 18562.62 |

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
| final_peak_lift | BPAT | uri | 2.71 | -0.59 | -1.23 | -5.19 | 6 |
| final_peak_lift | CISO | uri | 1.74 | -0.55 | -0.92 | -1.78 | 6 |
| final_peak_lift | DUK | uri | 3.41 | -1.14 | -1.21 | -4.42 | 6 |
| final_peak_lift | ERCO | uri | 6.30 | -8.64 | -8.64 | -8.86 | 2 |
| final_peak_lift | FPL | uri | 8.55 | -9.91 | -9.91 | -11.99 | 6 |
| final_peak_lift | ISNE | uri | 2.74 | 1.50 | -0.34 | -2.05 | 6 |
| final_peak_lift | MISO | uri | 3.39 | -2.53 | -2.78 | -5.80 | 5 |
| final_peak_lift | NYIS | uri | 2.07 | 2.05 | -0.15 | -0.88 | 6 |
| final_peak_lift | PJM | uri | 1.93 | 0.37 | -0.68 | -2.97 | 6 |
| final_peak_lift | SWPP | uri | 6.05 | 1.22 | -2.23 | -4.79 | 4 |
| final_peak_lift | TVA | uri | 2.96 | 0.09 | -1.16 | -2.60 | 6 |
| final_peak_q55 | BPAT | uri | 2.73 | -1.04 | -1.43 | -5.19 | 6 |
| final_peak_q55 | CISO | uri | 1.72 | 0.07 | -0.41 | -1.13 | 6 |
| final_peak_q55 | DUK | uri | 3.39 | -2.49 | -2.53 | -5.32 | 6 |
| final_peak_q55 | ERCO | uri | 6.81 | -9.59 | -9.59 | -10.08 | 2 |
| final_peak_q55 | FPL | uri | 8.34 | -9.21 | -9.21 | -11.22 | 6 |
| final_peak_q55 | ISNE | uri | 2.75 | 1.56 | -0.34 | -2.06 | 6 |
| final_peak_q55 | MISO | uri | 3.47 | -2.98 | -3.14 | -6.26 | 5 |
| final_peak_q55 | NYIS | uri | 2.00 | 1.81 | -0.18 | -1.09 | 6 |
| final_peak_q55 | PJM | uri | 1.86 | -0.03 | -0.69 | -2.54 | 6 |
| final_peak_q55 | SWPP | uri | 6.18 | 0.83 | -2.55 | -6.10 | 4 |
| final_peak_q55 | TVA | uri | 2.90 | -2.28 | -2.85 | -5.64 | 6 |
| final_peak_q60 | BPAT | uri | 2.72 | -0.73 | -1.25 | -5.19 | 6 |
| final_peak_q60 | CISO | uri | 1.72 | 0.23 | -0.31 | -1.04 | 6 |
| final_peak_q60 | DUK | uri | 3.40 | -1.99 | -2.07 | -4.75 | 6 |
| final_peak_q60 | ERCO | uri | 6.67 | -9.22 | -9.22 | -9.61 | 2 |
| final_peak_q60 | FPL | uri | 8.04 | -8.22 | -8.22 | -10.41 | 6 |
| final_peak_q60 | ISNE | uri | 2.81 | 2.50 | -0.18 | -1.08 | 6 |
| final_peak_q60 | MISO | uri | 3.44 | -2.63 | -2.90 | -6.00 | 5 |
| final_peak_q60 | NYIS | uri | 2.05 | 2.10 | -0.15 | -0.89 | 6 |
| final_peak_q60 | PJM | uri | 1.87 | 0.27 | -0.58 | -2.33 | 6 |
| final_peak_q60 | SWPP | uri | 6.16 | 1.20 | -2.39 | -5.76 | 4 |
| final_peak_q60 | TVA | uri | 2.91 | -1.88 | -2.54 | -5.18 | 6 |
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
| final_peak_lift | BPAT | elliott | 4.33 | -2.81 | -3.38 | -7.72 | 5 |
| final_peak_lift | CISO | elliott | 3.31 | 1.44 | -0.76 | -3.81 | 5 |
| final_peak_lift | DUK | elliott | 3.14 | -1.24 | -1.40 | -2.26 | 4 |
| final_peak_lift | ERCO | elliott | 6.62 | -2.65 | -4.40 | -11.17 | 5 |
| final_peak_lift | FPL | elliott | 7.92 | -9.18 | -9.41 | -14.82 | 5 |
| final_peak_lift | ISNE | elliott | 3.33 | 1.65 | -0.62 | -1.58 | 5 |
| final_peak_lift | MISO | elliott | 3.48 | -1.07 | -2.16 | -3.67 | 5 |
| final_peak_lift | NYIS | elliott | 2.72 | -0.23 | -1.19 | -2.75 | 5 |
| final_peak_lift | PJM | elliott | 4.19 | -1.81 | -2.71 | -6.00 | 5 |
| final_peak_lift | SWPP | elliott | 4.11 | -0.39 | -2.17 | -5.57 | 5 |
| final_peak_lift | TVA | elliott | 6.32 | 2.98 | -0.28 | -0.51 | 3 |
| final_peak_q55 | BPAT | elliott | 4.34 | -3.56 | -3.96 | -8.11 | 5 |
| final_peak_q55 | CISO | elliott | 3.30 | 1.22 | -0.85 | -4.09 | 5 |
| final_peak_q55 | DUK | elliott | 3.33 | -2.85 | -2.85 | -4.83 | 4 |
| final_peak_q55 | ERCO | elliott | 6.71 | -3.28 | -4.88 | -11.38 | 5 |
| final_peak_q55 | FPL | elliott | 7.98 | -9.20 | -9.43 | -14.82 | 5 |
| final_peak_q55 | ISNE | elliott | 3.35 | 1.73 | -0.58 | -1.49 | 5 |
| final_peak_q55 | MISO | elliott | 3.40 | -1.77 | -2.72 | -4.28 | 5 |
| final_peak_q55 | NYIS | elliott | 2.74 | -0.49 | -1.40 | -2.97 | 5 |
| final_peak_q55 | PJM | elliott | 4.18 | -2.31 | -3.01 | -6.73 | 5 |
| final_peak_q55 | SWPP | elliott | 4.15 | -1.18 | -2.65 | -6.26 | 5 |
| final_peak_q55 | TVA | elliott | 6.18 | 2.34 | -0.08 | -0.20 | 3 |
| final_peak_q60 | BPAT | elliott | 4.35 | -2.97 | -3.54 | -7.54 | 5 |
| final_peak_q60 | CISO | elliott | 3.32 | 1.58 | -0.75 | -3.74 | 5 |
| final_peak_q60 | DUK | elliott | 3.27 | -2.17 | -2.17 | -4.39 | 4 |
| final_peak_q60 | ERCO | elliott | 6.69 | -3.02 | -4.75 | -11.11 | 5 |
| final_peak_q60 | FPL | elliott | 7.93 | -9.03 | -9.26 | -14.82 | 5 |
| final_peak_q60 | ISNE | elliott | 3.38 | 2.18 | -0.41 | -1.07 | 5 |
| final_peak_q60 | MISO | elliott | 3.41 | -1.52 | -2.50 | -4.11 | 5 |
| final_peak_q60 | NYIS | elliott | 2.71 | -0.09 | -1.09 | -2.61 | 5 |
| final_peak_q60 | PJM | elliott | 4.19 | -2.00 | -2.81 | -6.29 | 5 |
| final_peak_q60 | SWPP | elliott | 4.12 | -0.83 | -2.44 | -5.95 | 5 |
| final_peak_q60 | TVA | elliott | 6.25 | 2.86 | 0.00 | 0.00 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | DF | eve | 3.47 | 0.40 | -1.41 |  | 268 |
| 9 | final | eve | 3.52 | 0.34 | -1.77 | 0.47 | 268 |
| 14 | final_peak_q55 | eve | 3.55 | 0.70 | -1.63 | 0.47 | 268 |
| 15 | final_peak_q60 | eve | 3.59 | 1.10 | -1.50 | 0.46 | 268 |
| 13 | final_peak_lift | eve | 3.59 | 1.02 | -1.50 | 0.46 | 268 |
| 12 | final_ensemble | eve | 3.62 | -0.13 | -2.04 | 0.46 | 268 |
| 10 | final_additive | eve | 3.83 | -0.16 | -2.20 | 0.43 | 268 |
| 11 | final_boosting | eve | 3.86 | -0.09 | -2.12 | 0.43 | 268 |
| 1 | final | special | 3.40 | -1.33 | -2.53 | 0.53 | 270 |
| 6 | final_peak_q55 | special | 3.41 | -0.95 | -2.31 | 0.52 | 270 |
| 7 | final_peak_q60 | special | 3.42 | -0.53 | -2.09 | 0.52 | 270 |
| 5 | final_peak_lift | special | 3.43 | -0.58 | -2.09 | 0.50 | 270 |
| 4 | final_ensemble | special | 3.61 | -1.76 | -2.90 | 0.53 | 270 |
| 0 | DF | special | 3.80 | -0.17 | -1.78 |  | 270 |
| 2 | final_additive | special | 3.84 | -1.88 | -3.09 | 0.48 | 270 |
| 3 | final_boosting | special | 3.93 | -1.61 | -2.93 | 0.44 | 270 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final | all | 0.403 | 1.405 | 0.410 | 0.895 | 12.221 | 0.888 | 7921 |
| final_peak_lift | all | 0.409 | 1.417 | 0.414 | 0.895 | 12.301 | 0.896 | 7921 |
| final_peak_q55 | all | 0.404 | 1.407 | 0.411 | 0.895 | 12.226 | 0.893 | 7921 |
| final_peak_q60 | all | 0.406 | 1.414 | 0.413 | 0.895 | 12.271 | 0.893 | 7921 |
| final | events | 0.493 | 1.914 | 0.621 | 0.769 | 11.765 | 0.785 | 107 |
| final_peak_lift | events | 0.504 | 1.903 | 0.611 | 0.776 | 11.917 | 0.785 | 107 |
| final_peak_q55 | events | 0.498 | 1.905 | 0.610 | 0.771 | 11.795 | 0.785 | 107 |
| final_peak_q60 | events | 0.501 | 1.897 | 0.599 | 0.777 | 11.863 | 0.776 | 107 |
| final | cold_mornings | 0.460 | 1.728 | 0.530 | 0.807 | 12.005 | 0.773 | 330 |
| final_peak_lift | cold_mornings | 0.475 | 1.715 | 0.509 | 0.818 | 12.090 | 0.803 | 330 |
| final_peak_q55 | cold_mornings | 0.464 | 1.723 | 0.523 | 0.807 | 12.005 | 0.776 | 330 |
| final_peak_q60 | cold_mornings | 0.469 | 1.720 | 0.518 | 0.810 | 12.042 | 0.785 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 17847 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 17843 | DUK | 2022-12-24 | final | 9.09 | -14.17 | -14.17 |
| 17840 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 17841 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 17842 | DUK | 2022-12-24 | final_ensemble | 8.26 | -14.16 | -14.16 |
| 17844 | DUK | 2022-12-24 | final_peak_lift | 8.83 | -13.48 | -13.48 |
| 17845 | DUK | 2022-12-24 | final_peak_q55 | 9.03 | -13.90 | -13.90 |
| 17846 | DUK | 2022-12-24 | final_peak_q60 | 8.95 | -13.59 | -13.59 |
| 18503 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 18499 | ERCO | 2021-02-15 | final | 33.61 | -10.86 | -10.86 |
| 18496 | ERCO | 2021-02-15 | final_additive | 41.72 | -4.24 | -4.24 |
| 18497 | ERCO | 2021-02-15 | final_boosting | 27.39 | -16.57 | -16.57 |
| 18498 | ERCO | 2021-02-15 | final_ensemble | 34.57 | -10.39 | -10.39 |
| 18500 | ERCO | 2021-02-15 | final_peak_lift | 34.31 | -10.86 | -10.86 |
| 18501 | ERCO | 2021-02-15 | final_peak_q55 | 33.76 | -10.86 | -10.86 |
| 18502 | ERCO | 2021-02-15 | final_peak_q60 | 33.95 | -10.86 | -10.86 |
| 18511 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 18507 | ERCO | 2021-02-16 | final | 39.49 | 37.58 | 0.00 |
| 18504 | ERCO | 2021-02-16 | final_additive | 47.08 | 43.33 | 0.00 |
| 18505 | ERCO | 2021-02-16 | final_boosting | 33.46 | 31.10 | 0.00 |
| 18506 | ERCO | 2021-02-16 | final_ensemble | 40.43 | 37.36 | 0.00 |
| 18508 | ERCO | 2021-02-16 | final_peak_lift | 40.17 | 37.58 | 0.00 |
| 18509 | ERCO | 2021-02-16 | final_peak_q55 | 39.67 | 37.58 | 0.00 |
| 18510 | ERCO | 2021-02-16 | final_peak_q60 | 39.95 | 37.58 | 0.00 |
| 18519 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 18515 | ERCO | 2021-02-17 | final | 29.39 | 23.92 | 0.00 |
| 18512 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 18513 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 18514 | ERCO | 2021-02-17 | final_ensemble | 30.28 | 26.83 | 0.00 |
| 18516 | ERCO | 2021-02-17 | final_peak_lift | 30.27 | 27.90 | 0.00 |
| 18517 | ERCO | 2021-02-17 | final_peak_q55 | 29.58 | 24.52 | 0.00 |
| 18518 | ERCO | 2021-02-17 | final_peak_q60 | 29.79 | 25.16 | 0.00 |
| 18527 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 18523 | ERCO | 2021-02-18 | final | 6.89 | 4.76 | 0.00 |
| 18520 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 18521 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 18522 | ERCO | 2021-02-18 | final_ensemble | 7.68 | 4.44 | 0.00 |
| 18524 | ERCO | 2021-02-18 | final_peak_lift | 7.72 | 5.24 | 0.00 |
| 18525 | ERCO | 2021-02-18 | final_peak_q55 | 7.07 | 5.08 | 0.00 |
| 18526 | ERCO | 2021-02-18 | final_peak_q60 | 7.29 | 5.31 | 0.00 |
| 36127 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 36123 | MISO | 2021-02-16 | final | 2.07 | 1.67 | 0.00 |
| 36120 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 36121 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 36122 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 36124 | MISO | 2021-02-16 | final_peak_lift | 2.41 | 2.19 | 0.00 |
| 36125 | MISO | 2021-02-16 | final_peak_q55 | 2.17 | 1.84 | 0.00 |
| 36126 | MISO | 2021-02-16 | final_peak_q60 | 2.30 | 2.40 | 0.00 |
| 54063 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 54059 | SWPP | 2021-02-15 | final | 2.08 | -2.08 | -2.08 |
| 54056 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 54057 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 54058 | SWPP | 2021-02-15 | final_ensemble | 2.21 | -3.25 | -3.25 |
| 54060 | SWPP | 2021-02-15 | final_peak_lift | 2.12 | -1.73 | -1.73 |
| 54061 | SWPP | 2021-02-15 | final_peak_q55 | 1.94 | -1.87 | -1.87 |
| 54062 | SWPP | 2021-02-15 | final_peak_q60 | 1.86 | -1.48 | -1.48 |
| 54071 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 54067 | SWPP | 2021-02-16 | final | 5.52 | -1.24 | -1.24 |
| 54064 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 54065 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 54066 | SWPP | 2021-02-16 | final_ensemble | 5.49 | -1.39 | -1.39 |
| 54068 | SWPP | 2021-02-16 | final_peak_lift | 5.92 | 0.22 | 0.00 |
| 54069 | SWPP | 2021-02-16 | final_peak_q55 | 5.64 | -0.43 | -0.43 |
| 54070 | SWPP | 2021-02-16 | final_peak_q60 | 5.76 | -0.02 | -0.02 |
| 65319 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 65315 | TVA | 2022-12-23 | final | 10.85 | -12.10 | -12.10 |
| 65312 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 65313 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 65314 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 65316 | TVA | 2022-12-23 | final_peak_lift | 10.39 | -10.13 | -10.13 |
| 65317 | TVA | 2022-12-23 | final_peak_q55 | 10.73 | -11.57 | -11.57 |
| 65318 | TVA | 2022-12-23 | final_peak_q60 | 10.62 | -11.27 | -11.27 |
| 65327 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 65323 | TVA | 2022-12-24 | final | 4.93 | -11.86 | -11.86 |
| 65320 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 65321 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 65322 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |
| 65324 | TVA | 2022-12-24 | final_peak_lift | 4.82 | -11.86 | -11.86 |
| 65325 | TVA | 2022-12-24 | final_peak_q55 | 4.83 | -11.86 | -11.86 |
| 65326 | TVA | 2022-12-24 | final_peak_q60 | 4.75 | -11.86 | -11.86 |

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
| final_peak_lift | BPAT | mape | 9.077 | 0.000 | 750 |
| final_peak_lift | CISO | mape | -2.272 | 0.023 | 737 |
| final_peak_lift | DUK | mape | 7.584 | 0.000 | 750 |
| final_peak_lift | ERCO | mape | 2.940 | 0.003 | 746 |
| final_peak_lift | FPL | mape | 0.082 | 0.935 | 700 |
| final_peak_lift | ISNE | mape | 15.664 | 0.000 | 752 |
| final_peak_lift | MISO | mape | -8.575 | 0.000 | 746 |
| final_peak_lift | NYIS | mape | -3.046 | 0.002 | 752 |
| final_peak_lift | PJM | mape | -25.119 | 0.000 | 744 |
| final_peak_lift | SWPP | mape | -16.224 | 0.000 | 747 |
| final_peak_lift | TVA | mape | 14.891 | 0.000 | 739 |
| final_peak_q55 | BPAT | mape | 8.400 | 0.000 | 750 |
| final_peak_q55 | CISO | mape | -2.354 | 0.019 | 737 |
| final_peak_q55 | DUK | mape | 7.070 | 0.000 | 750 |
| final_peak_q55 | ERCO | mape | 2.734 | 0.006 | 746 |
| final_peak_q55 | FPL | mape | -0.186 | 0.852 | 700 |
| final_peak_q55 | ISNE | mape | 15.614 | 0.000 | 752 |
| final_peak_q55 | MISO | mape | -8.734 | 0.000 | 746 |
| final_peak_q55 | NYIS | mape | -3.348 | 0.001 | 752 |
| final_peak_q55 | PJM | mape | -25.550 | 0.000 | 744 |
| final_peak_q55 | SWPP | mape | -16.357 | 0.000 | 747 |
| final_peak_q55 | TVA | mape | 14.518 | 0.000 | 739 |
| final_peak_q60 | BPAT | mape | 8.607 | 0.000 | 750 |
| final_peak_q60 | CISO | mape | -2.267 | 0.023 | 737 |
| final_peak_q60 | DUK | mape | 7.296 | 0.000 | 750 |
| final_peak_q60 | ERCO | mape | 3.066 | 0.002 | 746 |
| final_peak_q60 | FPL | mape | -0.004 | 0.996 | 700 |
| final_peak_q60 | ISNE | mape | 15.830 | 0.000 | 752 |
| final_peak_q60 | MISO | mape | -8.647 | 0.000 | 746 |
| final_peak_q60 | NYIS | mape | -3.184 | 0.001 | 752 |
| final_peak_q60 | PJM | mape | -25.303 | 0.000 | 744 |
| final_peak_q60 | SWPP | mape | -16.374 | 0.000 | 747 |
| final_peak_q60 | TVA | mape | 14.918 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final | 0.992 |
| final_additive | 0.981 |
| final_boosting | 0.992 |
| final_ensemble | 0.992 |
| final_peak_lift | 0.992 |
| final_peak_q55 | 0.992 |
| final_peak_q60 | 0.992 |
