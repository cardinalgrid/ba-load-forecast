# Phase G: the temperature forecast corrected by its own recent bias

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). The phase F recipe with the HRRR 2 m temperature path of every station moved by the median of the forecast's own error at that local hour over the last 30 known days (forecast as seen at the cut-off against the airport observation). Compare with `docs/phase_g_protocol.md` (same recipe, no correction).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final_ensemble | 2.51 | 2.18 | -1.44 | -2.21 | 1.26 | 0.54 | 0.21 | -46.15 | 8154 | 11.00 |
| final2 | 2.52 | 2.18 | -0.11 | -1.46 | 1.28 | 0.54 | 0.28 | -45.07 | 8154 | 11.00 |
| final_boosting | 2.64 | 2.28 | -1.20 | -2.12 | 1.41 | 0.51 | 0.23 | -44.30 | 8154 | 11.00 |
| DF | 2.69 | 2.40 | 0.35 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8154 | 11.00 |
| final_additive | 2.81 | 2.47 | -1.71 | -2.51 | 1.36 | 0.47 | 0.19 | -48.08 | 8154 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.38 | 2.15 | 0.39 | -0.65 | 0.24 | -6.72 |  |  | 737 | 25196.34 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | FPL | 3.89 | 3.60 | -3.63 | -4.02 | 1.17 | -47.43 |  |  | 693 | 15271.72 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 2.45 | 2.23 | -0.60 | -1.27 | 1.04 | -8.98 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.21 | -19.98 |  |  | 745 | 31350.31 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| final2 | BPAT | 2.53 | 2.19 | -0.36 | -1.46 | 1.75 | -19.06 | 0.38 | 0.25 | 750 | 6533.15 |
| final2 | CISO | 2.48 | 2.21 | 0.38 | -1.12 | 0.36 | -11.37 | 0.48 | 0.26 | 737 | 25196.34 |
| final2 | DUK | 3.41 | 3.03 | -0.30 | -2.14 | 1.32 | -15.54 | 0.38 | 0.30 | 750 | 12129.97 |
| final2 | ERCO | 2.73 | 2.28 | -0.02 | -1.57 | 1.05 | -14.39 | 0.46 | 0.26 | 746 | 46782.53 |
| final2 | FPL | 3.61 | 3.09 | -0.43 | -2.45 | 1.14 | -45.07 | 0.60 | 0.66 | 693 | 15271.72 |
| final2 | ISNE | 3.38 | 2.96 | 0.34 | -1.42 | 0.55 | -17.93 | 0.31 | 0.22 | 752 | 13392.81 |
| final2 | MISO | 2.07 | 1.82 | -0.19 | -1.16 | 1.70 | -9.02 | 0.62 | 0.06 | 746 | 73788.38 |
| final2 | NYIS | 2.54 | 2.17 | 0.04 | -1.42 | 0.62 | -12.74 | 0.56 | 0.70 | 752 | 17400.75 |
| final2 | PJM | 2.32 | 2.03 | -0.16 | -1.43 | 1.42 | -9.78 | 0.57 | 0.40 | 744 | 91927.69 |
| final2 | SWPP | 2.35 | 1.95 | -0.36 | -1.48 | 1.53 | -21.35 | 0.73 | 0.10 | 745 | 31350.31 |
| final2 | TVA | 3.05 | 2.61 | 0.04 | -1.75 | 1.38 | -14.76 | 0.29 | 0.30 | 739 | 18562.62 |
| final_additive | BPAT | 2.72 | 2.34 | -1.27 | -2.00 | 1.81 | -18.99 | 0.33 | 0.20 | 750 | 6533.15 |
| final_additive | CISO | 2.88 | 2.56 | -1.56 | -2.44 | 0.41 | -13.21 | 0.36 | 0.15 | 737 | 25196.34 |
| final_additive | DUK | 3.55 | 3.20 | -2.03 | -3.23 | 1.44 | -18.91 | 0.35 | 0.21 | 750 | 12129.97 |
| final_additive | ERCO | 3.14 | 2.70 | -2.07 | -2.93 | 1.05 | -17.14 | 0.39 | 0.15 | 746 | 46782.53 |
| final_additive | FPL | 4.19 | 3.69 | -2.32 | -3.73 | 1.10 | -48.08 | 0.52 | 0.54 | 693 | 15271.72 |
| final_additive | ISNE | 3.70 | 3.35 | -1.31 | -2.40 | 0.54 | -18.59 | 0.23 | 0.15 | 752 | 13392.81 |
| final_additive | MISO | 2.33 | 2.07 | -1.76 | -2.22 | 1.81 | -10.21 | 0.56 | 0.05 | 746 | 73788.38 |
| final_additive | NYIS | 2.87 | 2.45 | -1.42 | -2.44 | 0.58 | -15.56 | 0.48 | 0.55 | 752 | 17400.75 |
| final_additive | PJM | 2.59 | 2.28 | -1.62 | -2.38 | 1.61 | -12.76 | 0.48 | 0.25 | 744 | 91927.69 |
| final_additive | SWPP | 2.47 | 2.11 | -1.10 | -2.00 | 1.50 | -20.27 | 0.70 | 0.08 | 745 | 31350.31 |
| final_additive | TVA | 3.25 | 2.83 | -2.23 | -3.10 | 1.53 | -16.38 | 0.27 | 0.18 | 739 | 18562.62 |
| final_boosting | BPAT | 2.54 | 2.24 | -1.16 | -1.94 | 1.79 | -19.71 | 0.34 | 0.20 | 750 | 6533.15 |
| final_boosting | CISO | 2.56 | 2.23 | -0.40 | -1.42 | 0.38 | -14.60 | 0.46 | 0.23 | 737 | 25196.34 |
| final_boosting | DUK | 3.42 | 3.08 | -1.76 | -2.97 | 1.41 | -18.17 | 0.38 | 0.22 | 750 | 12129.97 |
| final_boosting | ERCO | 2.88 | 2.50 | -2.06 | -2.82 | 1.28 | -16.00 | 0.39 | 0.19 | 746 | 46782.53 |
| final_boosting | FPL | 3.67 | 3.23 | -2.16 | -3.44 | 1.29 | -44.30 | 0.58 | 0.57 | 693 | 15271.72 |
| final_boosting | ISNE | 3.49 | 3.11 | -0.68 | -1.89 | 0.61 | -18.27 | 0.28 | 0.16 | 752 | 13392.81 |
| final_boosting | MISO | 2.20 | 1.88 | -0.90 | -1.65 | 1.77 | -11.02 | 0.60 | 0.05 | 746 | 73788.38 |
| final_boosting | NYIS | 2.63 | 2.30 | -0.86 | -1.83 | 0.72 | -13.31 | 0.54 | 0.63 | 752 | 17400.75 |
| final_boosting | PJM | 2.44 | 2.12 | -0.96 | -1.94 | 1.60 | -11.01 | 0.53 | 0.33 | 744 | 91927.69 |
| final_boosting | SWPP | 2.52 | 2.02 | -1.71 | -2.38 | 1.71 | -30.63 | 0.71 | 0.06 | 745 | 31350.31 |
| final_boosting | TVA | 3.06 | 2.70 | -1.26 | -2.44 | 1.52 | -16.84 | 0.27 | 0.22 | 739 | 18562.62 |
| final_ensemble | BPAT | 2.46 | 2.10 | -1.20 | -1.90 | 1.71 | -19.35 | 0.40 | 0.21 | 750 | 6533.15 |
| final_ensemble | CISO | 2.44 | 2.13 | -0.92 | -1.75 | 0.35 | -12.66 | 0.49 | 0.18 | 737 | 25196.34 |
| final_ensemble | DUK | 3.35 | 2.93 | -1.89 | -3.04 | 1.34 | -18.53 | 0.39 | 0.21 | 750 | 12129.97 |
| final_ensemble | ERCO | 2.78 | 2.38 | -2.09 | -2.78 | 1.08 | -15.34 | 0.44 | 0.17 | 746 | 46782.53 |
| final_ensemble | FPL | 3.60 | 3.21 | -2.20 | -3.42 | 1.13 | -46.15 | 0.60 | 0.57 | 693 | 15271.72 |
| final_ensemble | ISNE | 3.34 | 2.91 | -0.98 | -2.03 | 0.52 | -17.29 | 0.31 | 0.15 | 752 | 13392.81 |
| final_ensemble | MISO | 2.05 | 1.80 | -1.30 | -1.82 | 1.55 | -9.80 | 0.62 | 0.04 | 746 | 73788.38 |
| final_ensemble | NYIS | 2.50 | 2.13 | -1.08 | -1.98 | 0.60 | -13.64 | 0.56 | 0.61 | 752 | 17400.75 |
| final_ensemble | PJM | 2.31 | 2.03 | -1.28 | -2.07 | 1.46 | -10.81 | 0.59 | 0.28 | 744 | 91927.69 |
| final_ensemble | SWPP | 2.34 | 1.89 | -1.40 | -2.11 | 1.53 | -21.46 | 0.73 | 0.07 | 745 | 31350.31 |
| final_ensemble | TVA | 2.98 | 2.61 | -1.72 | -2.68 | 1.43 | -16.61 | 0.31 | 0.19 | 739 | 18562.62 |

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
| final2 | BPAT | uri | 2.92 | 0.07 | -1.13 | -5.35 | 6 |
| final2 | CISO | uri | 2.23 | -0.21 | -0.74 | -2.00 | 6 |
| final2 | DUK | uri | 3.91 | -1.24 | -1.80 | -4.34 | 6 |
| final2 | ERCO | uri | 7.05 | -9.12 | -9.12 | -9.99 | 2 |
| final2 | FPL | uri | 6.09 | -7.07 | -7.07 | -14.06 | 6 |
| final2 | ISNE | uri | 2.57 | 1.79 | -0.24 | -1.43 | 6 |
| final2 | MISO | uri | 3.20 | -2.23 | -2.57 | -5.65 | 5 |
| final2 | NYIS | uri | 1.90 | 1.83 | -0.15 | -0.90 | 6 |
| final2 | PJM | uri | 1.87 | 0.36 | -0.74 | -2.79 | 6 |
| final2 | SWPP | uri | 6.74 | 2.06 | -2.06 | -4.73 | 4 |
| final2 | TVA | uri | 3.64 | -0.79 | -2.16 | -5.38 | 6 |
| final_additive | BPAT | uri | 3.14 | -0.87 | -1.70 | -3.78 | 6 |
| final_additive | CISO | uri | 2.22 | -0.46 | -0.99 | -2.12 | 6 |
| final_additive | DUK | uri | 3.70 | -3.86 | -3.86 | -6.96 | 6 |
| final_additive | ERCO | uri | 6.79 | -7.87 | -7.87 | -9.87 | 2 |
| final_additive | FPL | uri | 7.85 | -10.61 | -10.61 | -15.24 | 6 |
| final_additive | ISNE | uri | 2.25 | 0.10 | -0.85 | -3.10 | 6 |
| final_additive | MISO | uri | 3.67 | -2.79 | -3.11 | -6.02 | 5 |
| final_additive | NYIS | uri | 1.96 | 1.15 | -0.33 | -1.02 | 6 |
| final_additive | PJM | uri | 2.27 | 0.52 | -0.93 | -3.50 | 6 |
| final_additive | SWPP | uri | 6.78 | 2.07 | -1.90 | -4.93 | 4 |
| final_additive | TVA | uri | 3.68 | -1.96 | -2.95 | -6.54 | 6 |
| final_boosting | BPAT | uri | 3.14 | -0.59 | -1.62 | -7.08 | 6 |
| final_boosting | CISO | uri | 2.35 | -1.51 | -1.59 | -2.61 | 6 |
| final_boosting | DUK | uri | 3.80 | -3.75 | -3.75 | -5.45 | 6 |
| final_boosting | ERCO | uri | 8.82 | -12.97 | -12.97 | -15.12 | 2 |
| final_boosting | FPL | uri | 4.96 | -6.19 | -6.26 | -16.14 | 6 |
| final_boosting | ISNE | uri | 3.15 | 0.16 | -1.30 | -3.49 | 6 |
| final_boosting | MISO | uri | 4.13 | -5.39 | -5.39 | -8.41 | 5 |
| final_boosting | NYIS | uri | 1.83 | -0.44 | -1.11 | -3.49 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.93 | -1.95 | -5.16 | 6 |
| final_boosting | SWPP | uri | 6.00 | -2.11 | -4.10 | -10.32 | 4 |
| final_boosting | TVA | uri | 3.37 | -3.62 | -4.25 | -7.03 | 6 |
| final_ensemble | BPAT | uri | 2.79 | -0.74 | -1.38 | -4.99 | 6 |
| final_ensemble | CISO | uri | 1.96 | -0.99 | -1.30 | -2.22 | 6 |
| final_ensemble | DUK | uri | 3.69 | -3.81 | -3.81 | -5.75 | 6 |
| final_ensemble | ERCO | uri | 7.71 | -10.57 | -10.57 | -10.77 | 2 |
| final_ensemble | FPL | uri | 6.24 | -8.27 | -8.27 | -15.73 | 6 |
| final_ensemble | ISNE | uri | 2.53 | 0.13 | -0.84 | -3.27 | 6 |
| final_ensemble | MISO | uri | 3.73 | -4.12 | -4.12 | -7.14 | 5 |
| final_ensemble | NYIS | uri | 1.78 | 0.43 | -0.57 | -2.11 | 6 |
| final_ensemble | PJM | uri | 1.85 | -0.85 | -1.27 | -4.43 | 6 |
| final_ensemble | SWPP | uri | 6.42 | 0.08 | -2.96 | -6.34 | 4 |
| final_ensemble | TVA | uri | 3.24 | -2.85 | -3.38 | -6.69 | 6 |
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
| final2 | BPAT | elliott | 4.06 | -2.72 | -3.18 | -7.77 | 5 |
| final2 | CISO | elliott | 3.27 | 1.67 | -0.72 | -3.60 | 5 |
| final2 | DUK | elliott | 3.20 | -0.95 | -1.23 | -2.87 | 4 |
| final2 | ERCO | elliott | 6.22 | -0.23 | -2.73 | -6.93 | 5 |
| final2 | FPL | elliott | 7.65 | -8.51 | -8.51 | -14.30 | 5 |
| final2 | ISNE | elliott | 3.44 | 1.31 | -0.98 | -2.82 | 5 |
| final2 | MISO | elliott | 3.26 | -1.24 | -2.35 | -3.24 | 5 |
| final2 | NYIS | elliott | 2.75 | -0.36 | -1.37 | -2.86 | 5 |
| final2 | PJM | elliott | 4.05 | -2.30 | -2.86 | -5.67 | 5 |
| final2 | SWPP | elliott | 4.63 | 0.18 | -2.11 | -5.49 | 5 |
| final2 | TVA | elliott | 6.46 | 4.31 | 0.00 | 0.00 | 3 |
| final_additive | BPAT | elliott | 4.33 | -1.68 | -2.68 | -5.65 | 5 |
| final_additive | CISO | elliott | 3.08 | 0.93 | -0.98 | -4.84 | 5 |
| final_additive | DUK | elliott | 3.59 | -3.89 | -3.89 | -4.88 | 4 |
| final_additive | ERCO | elliott | 7.20 | -5.08 | -5.83 | -11.19 | 5 |
| final_additive | FPL | elliott | 8.95 | -2.85 | -6.68 | -15.29 | 5 |
| final_additive | ISNE | elliott | 4.12 | -1.20 | -1.97 | -5.00 | 5 |
| final_additive | MISO | elliott | 3.42 | -3.89 | -4.09 | -6.93 | 5 |
| final_additive | NYIS | elliott | 3.87 | -3.27 | -3.51 | -5.07 | 5 |
| final_additive | PJM | elliott | 3.95 | -3.84 | -3.94 | -7.57 | 5 |
| final_additive | SWPP | elliott | 3.68 | -3.14 | -3.55 | -7.20 | 5 |
| final_additive | TVA | elliott | 6.75 | 3.51 | -0.45 | -1.36 | 3 |
| final_boosting | BPAT | elliott | 4.74 | -5.65 | -5.65 | -12.28 | 5 |
| final_boosting | CISO | elliott | 3.35 | 1.15 | -0.97 | -4.10 | 5 |
| final_boosting | DUK | elliott | 3.55 | -4.27 | -4.27 | -7.00 | 4 |
| final_boosting | ERCO | elliott | 5.35 | -4.92 | -5.73 | -12.29 | 5 |
| final_boosting | FPL | elliott | 9.98 | -15.53 | -15.53 | -23.96 | 5 |
| final_boosting | ISNE | elliott | 3.28 | 0.49 | -1.38 | -4.05 | 5 |
| final_boosting | MISO | elliott | 3.56 | -1.67 | -2.82 | -4.05 | 5 |
| final_boosting | NYIS | elliott | 2.82 | -1.21 | -2.17 | -4.14 | 5 |
| final_boosting | PJM | elliott | 4.05 | -4.14 | -4.15 | -6.73 | 5 |
| final_boosting | SWPP | elliott | 4.98 | -2.53 | -4.39 | -11.56 | 5 |
| final_boosting | TVA | elliott | 5.28 | -1.39 | -2.05 | -4.48 | 3 |
| final_ensemble | BPAT | elliott | 4.45 | -3.76 | -4.11 | -8.46 | 5 |
| final_ensemble | CISO | elliott | 3.07 | 1.06 | -0.88 | -4.41 | 5 |
| final_ensemble | DUK | elliott | 3.45 | -4.09 | -4.09 | -5.70 | 4 |
| final_ensemble | ERCO | elliott | 6.06 | -4.99 | -5.77 | -11.76 | 5 |
| final_ensemble | FPL | elliott | 8.64 | -10.56 | -10.56 | -16.40 | 5 |
| final_ensemble | ISNE | elliott | 3.34 | -0.23 | -1.56 | -4.12 | 5 |
| final_ensemble | MISO | elliott | 3.23 | -2.58 | -3.34 | -4.58 | 5 |
| final_ensemble | NYIS | elliott | 2.97 | -2.06 | -2.72 | -4.53 | 5 |
| final_ensemble | PJM | elliott | 3.94 | -4.02 | -4.06 | -6.96 | 5 |
| final_ensemble | SWPP | elliott | 4.18 | -2.84 | -3.88 | -8.41 | 5 |
| final_ensemble | TVA | elliott | 5.79 | 1.04 | -1.09 | -1.77 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | final_ensemble | eve | 3.35 | -0.63 | -2.19 | 0.50 | 268 |
| 5 | DF | eve | 3.37 | 0.49 | -1.42 |  | 268 |
| 6 | final2 | eve | 3.50 | 0.73 | -1.63 | 0.45 | 268 |
| 7 | final_additive | eve | 3.53 | -0.82 | -2.38 | 0.45 | 268 |
| 8 | final_boosting | eve | 3.59 | -0.50 | -2.28 | 0.44 | 268 |
| 4 | final_ensemble | special | 3.39 | -2.24 | -3.15 | 0.52 | 270 |
| 1 | final2 | special | 3.42 | -0.86 | -2.29 | 0.53 | 270 |
| 3 | final_boosting | special | 3.61 | -2.05 | -3.14 | 0.48 | 270 |
| 2 | final_additive | special | 3.68 | -2.50 | -3.46 | 0.47 | 270 |
| 0 | DF | special | 3.70 | -0.13 | -1.77 |  | 270 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.401 | 1.386 | 0.414 | 0.890 | 12.169 | 0.893 | 7923 |
| final2 | events | 0.521 | 1.967 | 0.543 | 0.803 | 12.440 | 0.820 | 111 |
| final2 | cold_mornings | 0.470 | 1.686 | 0.493 | 0.844 | 12.910 | 0.827 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 11154 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 11153 | DUK | 2022-12-24 | final2 | 8.02 | -10.61 | -10.61 |
| 11150 | DUK | 2022-12-24 | final_additive | 8.91 | -11.63 | -11.63 |
| 11151 | DUK | 2022-12-24 | final_boosting | 10.68 | -15.80 | -15.80 |
| 11152 | DUK | 2022-12-24 | final_ensemble | 9.81 | -13.75 | -13.75 |
| 11564 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 11563 | ERCO | 2021-02-17 | final2 | 30.65 | 25.49 | 0.00 |
| 11560 | ERCO | 2021-02-17 | final_additive | 29.74 | 26.66 | 0.00 |
| 11561 | ERCO | 2021-02-17 | final_boosting | 28.57 | 22.90 | 0.00 |
| 11562 | ERCO | 2021-02-17 | final_ensemble | 29.11 | 24.63 | 0.00 |
| 11569 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 11568 | ERCO | 2021-02-18 | final2 | 8.50 | 6.49 | 0.00 |
| 11565 | ERCO | 2021-02-18 | final_additive | 12.74 | 12.12 | 0.00 |
| 11566 | ERCO | 2021-02-18 | final_boosting | 3.65 | -3.15 | -3.15 |
| 11567 | ERCO | 2021-02-18 | final_ensemble | 7.13 | 3.71 | 0.00 |
| 22534 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 22533 | MISO | 2021-02-16 | final2 | 2.64 | 2.76 | 0.00 |
| 22530 | MISO | 2021-02-16 | final_additive | 2.14 | 1.90 | 0.00 |
| 22531 | MISO | 2021-02-16 | final_boosting | 1.41 | -0.89 | -0.89 |
| 22532 | MISO | 2021-02-16 | final_ensemble | 1.67 | 0.49 | 0.00 |
| 33744 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 33743 | SWPP | 2021-02-15 | final2 | 1.91 | -1.38 | -1.38 |
| 33740 | SWPP | 2021-02-15 | final_additive | 2.64 | 1.09 | 0.00 |
| 33741 | SWPP | 2021-02-15 | final_boosting | 5.66 | -7.79 | -7.79 |
| 33742 | SWPP | 2021-02-15 | final_ensemble | 2.13 | -3.18 | -3.18 |
| 33749 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 33748 | SWPP | 2021-02-16 | final2 | 6.59 | -0.09 | -0.09 |
| 33745 | SWPP | 2021-02-16 | final_additive | 8.18 | 3.31 | 0.00 |
| 33746 | SWPP | 2021-02-16 | final_boosting | 3.71 | -6.44 | -6.44 |
| 33747 | SWPP | 2021-02-16 | final_ensemble | 5.51 | -1.30 | -1.30 |
| 40769 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 40768 | TVA | 2022-12-23 | final2 | 8.62 | -8.62 | -8.62 |
| 40765 | TVA | 2022-12-23 | final_additive | 6.49 | -5.25 | -5.25 |
| 40766 | TVA | 2022-12-23 | final_boosting | 14.12 | -15.00 | -15.00 |
| 40767 | TVA | 2022-12-23 | final_ensemble | 9.77 | -10.17 | -10.17 |
| 40774 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 40773 | TVA | 2022-12-24 | final2 | 4.43 | -10.00 | -10.00 |
| 40770 | TVA | 2022-12-24 | final_additive | 3.35 | -8.15 | -8.15 |
| 40771 | TVA | 2022-12-24 | final_boosting | 6.53 | -12.78 | -12.78 |
| 40772 | TVA | 2022-12-24 | final_ensemble | 4.85 | -10.55 | -10.55 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | BPAT | mape | 8.399 | 0.000 | 750 |
| final2 | CISO | mape | 1.725 | 0.085 | 737 |
| final2 | DUK | mape | 8.348 | 0.000 | 750 |
| final2 | ERCO | mape | 1.743 | 0.081 | 746 |
| final2 | FPL | mape | -3.395 | 0.001 | 693 |
| final2 | ISNE | mape | 15.696 | 0.000 | 752 |
| final2 | MISO | mape | -9.403 | 0.000 | 746 |
| final2 | NYIS | mape | -1.910 | 0.056 | 752 |
| final2 | PJM | mape | -2.298 | 0.022 | 744 |
| final2 | SWPP | mape | -16.090 | 0.000 | 745 |
| final2 | TVA | mape | 14.738 | 0.000 | 739 |
| final_additive | BPAT | mape | 10.916 | 0.000 | 750 |
| final_additive | CISO | mape | 9.002 | 0.000 | 737 |
| final_additive | DUK | mape | 9.810 | 0.000 | 750 |
| final_additive | ERCO | mape | 7.416 | 0.000 | 746 |
| final_additive | FPL | mape | 3.113 | 0.002 | 693 |
| final_additive | ISNE | mape | 20.361 | 0.000 | 752 |
| final_additive | MISO | mape | -4.561 | 0.000 | 746 |
| final_additive | NYIS | mape | 2.838 | 0.005 | 752 |
| final_additive | PJM | mape | 2.381 | 0.017 | 744 |
| final_additive | SWPP | mape | -14.675 | 0.000 | 745 |
| final_additive | TVA | mape | 15.875 | 0.000 | 739 |
| final_boosting | BPAT | mape | 9.176 | 0.000 | 750 |
| final_boosting | CISO | mape | 2.948 | 0.003 | 737 |
| final_boosting | DUK | mape | 8.480 | 0.000 | 750 |
| final_boosting | ERCO | mape | 3.641 | 0.000 | 746 |
| final_boosting | FPL | mape | -2.754 | 0.006 | 693 |
| final_boosting | ISNE | mape | 16.832 | 0.000 | 752 |
| final_boosting | MISO | mape | -6.765 | 0.000 | 746 |
| final_boosting | NYIS | mape | -0.578 | 0.564 | 752 |
| final_boosting | PJM | mape | -0.212 | 0.832 | 744 |
| final_boosting | SWPP | mape | -12.816 | 0.000 | 745 |
| final_boosting | TVA | mape | 15.196 | 0.000 | 739 |
| final_ensemble | BPAT | mape | 7.315 | 0.000 | 750 |
| final_ensemble | CISO | mape | 1.032 | 0.302 | 737 |
| final_ensemble | DUK | mape | 7.443 | 0.000 | 750 |
| final_ensemble | ERCO | mape | 2.266 | 0.023 | 746 |
| final_ensemble | FPL | mape | -3.619 | 0.000 | 693 |
| final_ensemble | ISNE | mape | 15.635 | 0.000 | 752 |
| final_ensemble | MISO | mape | -9.078 | 0.000 | 746 |
| final_ensemble | NYIS | mape | -2.628 | 0.009 | 752 |
| final_ensemble | PJM | mape | -2.680 | 0.007 | 744 |
| final_ensemble | SWPP | mape | -15.979 | 0.000 | 745 |
| final_ensemble | TVA | mape | 13.301 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final2 | 0.987 |
| final_additive | 0.976 |
| final_boosting | 0.987 |
| final_ensemble | 0.987 |
