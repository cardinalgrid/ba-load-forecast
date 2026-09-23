# Phase G: parameters

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Boosting: `deep` 800 iterations at rate 0.03 with 63 leaves; `shallow` 300 iterations, 15 leaves, 50 samples per leaf; `l2` regularisation 1.0; `refit3` refitted every 3 days; `7y` trained on 2555 days. Additive: 8 and 10 knots; 90 validation days; a penalty grid from 0.001 to 1000; 2555 training days.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8151 | 11.00 |
| boosting_deep | 2.95 | 2.58 | -0.85 | -2.01 | 1.40 | 0.44 | 0.25 | -51.84 | 8151 | 11.00 |
| boosting_refit3 | 2.98 | 2.64 | -1.00 | -2.10 | 1.45 | 0.43 | 0.24 | -50.67 | 8151 | 11.00 |
| boosting_l2 | 2.99 | 2.62 | -0.97 | -2.10 | 1.44 | 0.43 | 0.25 | -52.05 | 8151 | 11.00 |
| boosting_7y | 2.99 | 2.63 | -0.98 | -2.09 | 1.47 | 0.43 | 0.25 | -52.85 | 8151 | 11.00 |
| final_boosting | 3.00 | 2.65 | -0.97 | -2.10 | 1.49 | 0.42 | 0.24 | -51.98 | 8151 | 11.00 |
| boosting_shallow | 3.10 | 2.74 | -1.28 | -2.29 | 1.49 | 0.41 | 0.23 | -51.19 | 8151 | 11.00 |
| additive_7y | 3.11 | 2.73 | -1.46 | -2.45 | 1.40 | 0.42 | 0.22 | -50.89 | 8151 | 11.00 |
| final_additive | 3.11 | 2.74 | -1.44 | -2.44 | 1.41 | 0.42 | 0.22 | -50.91 | 8151 | 11.00 |
| additive_val90 | 3.12 | 2.73 | -1.43 | -2.43 | 1.41 | 0.41 | 0.22 | -50.91 | 8151 | 11.00 |
| additive_k8 | 3.12 | 2.74 | -1.45 | -2.45 | 1.43 | 0.41 | 0.22 | -50.93 | 8151 | 11.00 |
| additive_lam | 3.12 | 2.73 | -1.48 | -2.46 | 1.42 | 0.42 | 0.22 | -50.91 | 8151 | 11.00 |
| additive_k10 | 3.12 | 2.73 | -1.47 | -2.46 | 1.41 | 0.41 | 0.22 | -50.86 | 8151 | 11.00 |

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
| additive_7y | BPAT | 2.81 | 2.46 | -0.90 | -1.81 | 1.88 | -18.47 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_7y | CISO | 3.77 | 3.15 | -2.87 | -3.81 | 0.42 | -18.19 | 0.25 | 0.13 | 737 | 25196.34 |
| additive_7y | DUK | 3.56 | 3.15 | -0.71 | -2.38 | 1.39 | -14.80 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_7y | ERCO | 3.56 | 3.14 | -2.24 | -3.05 | 1.11 | -16.22 | 0.30 | 0.15 | 746 | 46782.53 |
| additive_7y | FPL | 6.18 | 5.59 | -6.19 | -6.75 | 1.10 | -50.89 | 0.29 | 0.27 | 690 | 15275.13 |
| additive_7y | ISNE | 3.86 | 3.46 | -1.17 | -2.52 | 0.55 | -20.54 | 0.20 | 0.16 | 752 | 13392.81 |
| additive_7y | MISO | 2.44 | 2.18 | -1.44 | -2.00 | 1.81 | -9.65 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_7y | NYIS | 2.72 | 2.35 | -0.86 | -2.09 | 0.59 | -15.52 | 0.51 | 0.59 | 752 | 17400.75 |
| additive_7y | PJM | 2.80 | 2.47 | -0.67 | -1.83 | 1.74 | -12.08 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_7y | SWPP | 2.52 | 2.10 | -0.29 | -1.59 | 1.50 | -20.30 | 0.70 | 0.10 | 745 | 31350.31 |
| additive_7y | TVA | 3.34 | 2.96 | -1.07 | -2.35 | 1.42 | -14.12 | 0.24 | 0.25 | 739 | 18562.62 |
| additive_k10 | BPAT | 2.84 | 2.47 | -0.89 | -1.81 | 1.86 | -18.28 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_k10 | CISO | 3.79 | 3.16 | -2.92 | -3.83 | 0.43 | -18.70 | 0.25 | 0.13 | 737 | 25196.34 |
| additive_k10 | DUK | 3.58 | 3.12 | -0.68 | -2.38 | 1.46 | -14.79 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_k10 | ERCO | 3.57 | 3.16 | -2.24 | -3.04 | 1.08 | -16.22 | 0.30 | 0.16 | 746 | 46782.53 |
| additive_k10 | FPL | 6.21 | 5.52 | -6.13 | -6.74 | 1.12 | -50.86 | 0.28 | 0.27 | 690 | 15275.13 |
| additive_k10 | ISNE | 3.87 | 3.48 | -1.16 | -2.52 | 0.54 | -20.37 | 0.21 | 0.16 | 752 | 13392.81 |
| additive_k10 | MISO | 2.45 | 2.17 | -1.42 | -2.00 | 1.80 | -11.33 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_k10 | NYIS | 2.73 | 2.36 | -0.87 | -2.09 | 0.59 | -15.41 | 0.51 | 0.60 | 752 | 17400.75 |
| additive_k10 | PJM | 2.81 | 2.47 | -0.74 | -1.88 | 1.76 | -12.34 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_k10 | SWPP | 2.54 | 2.11 | -0.31 | -1.61 | 1.57 | -21.53 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_k10 | TVA | 3.35 | 2.97 | -1.02 | -2.33 | 1.47 | -13.95 | 0.24 | 0.26 | 739 | 18562.62 |
| additive_k8 | BPAT | 2.84 | 2.47 | -0.87 | -1.80 | 1.86 | -18.11 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_k8 | CISO | 3.79 | 3.16 | -2.90 | -3.83 | 0.43 | -18.60 | 0.26 | 0.13 | 737 | 25196.34 |
| additive_k8 | DUK | 3.57 | 3.13 | -0.69 | -2.38 | 1.42 | -14.72 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_k8 | ERCO | 3.58 | 3.16 | -2.24 | -3.05 | 1.12 | -16.07 | 0.29 | 0.16 | 746 | 46782.53 |
| additive_k8 | FPL | 6.19 | 5.56 | -6.14 | -6.74 | 1.12 | -50.93 | 0.29 | 0.27 | 690 | 15275.13 |
| additive_k8 | ISNE | 3.87 | 3.48 | -1.12 | -2.50 | 0.55 | -20.86 | 0.20 | 0.16 | 752 | 13392.81 |
| additive_k8 | MISO | 2.45 | 2.19 | -1.40 | -1.98 | 1.87 | -9.37 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_k8 | NYIS | 2.73 | 2.36 | -0.87 | -2.09 | 0.58 | -15.41 | 0.51 | 0.59 | 752 | 17400.75 |
| additive_k8 | PJM | 2.81 | 2.48 | -0.68 | -1.84 | 1.78 | -12.39 | 0.41 | 0.37 | 744 | 91927.69 |
| additive_k8 | SWPP | 2.52 | 2.10 | -0.32 | -1.61 | 1.55 | -21.08 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_k8 | TVA | 3.36 | 3.00 | -1.05 | -2.35 | 1.47 | -13.95 | 0.24 | 0.26 | 739 | 18562.62 |
| additive_lam | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_lam | CISO | 3.79 | 3.16 | -2.88 | -3.82 | 0.42 | -18.17 | 0.25 | 0.13 | 737 | 25196.34 |
| additive_lam | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| additive_lam | ERCO | 3.59 | 3.14 | -2.29 | -3.08 | 1.11 | -16.37 | 0.29 | 0.15 | 746 | 46782.53 |
| additive_lam | FPL | 6.18 | 5.61 | -6.17 | -6.74 | 1.08 | -50.91 | 0.29 | 0.27 | 690 | 15275.13 |
| additive_lam | ISNE | 3.87 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 752 | 13392.81 |
| additive_lam | MISO | 2.44 | 2.13 | -1.46 | -2.03 | 1.89 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_lam | NYIS | 2.72 | 2.39 | -0.84 | -2.06 | 0.64 | -15.67 | 0.52 | 0.59 | 752 | 17400.75 |
| additive_lam | PJM | 2.82 | 2.48 | -0.70 | -1.85 | 1.76 | -12.10 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_lam | SWPP | 2.54 | 2.14 | -0.30 | -1.61 | 1.51 | -20.36 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_lam | TVA | 3.36 | 3.01 | -1.07 | -2.37 | 1.42 | -14.12 | 0.24 | 0.25 | 739 | 18562.62 |
| additive_val90 | BPAT | 2.80 | 2.45 | -0.89 | -1.80 | 1.88 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_val90 | CISO | 3.80 | 3.16 | -2.87 | -3.83 | 0.43 | -18.18 | 0.25 | 0.13 | 737 | 25196.34 |
| additive_val90 | DUK | 3.57 | 3.15 | -0.67 | -2.36 | 1.44 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| additive_val90 | ERCO | 3.57 | 3.13 | -2.21 | -3.04 | 1.11 | -16.37 | 0.30 | 0.16 | 746 | 46782.53 |
| additive_val90 | FPL | 6.19 | 5.56 | -6.16 | -6.74 | 1.07 | -50.91 | 0.29 | 0.27 | 690 | 15275.13 |
| additive_val90 | ISNE | 3.88 | 3.45 | -1.07 | -2.49 | 0.56 | -20.75 | 0.20 | 0.16 | 752 | 13392.81 |
| additive_val90 | MISO | 2.45 | 2.16 | -1.40 | -1.97 | 1.79 | -10.34 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_val90 | NYIS | 2.73 | 2.36 | -0.83 | -2.06 | 0.63 | -15.66 | 0.51 | 0.60 | 752 | 17400.75 |
| additive_val90 | PJM | 2.81 | 2.47 | -0.63 | -1.80 | 1.79 | -12.13 | 0.42 | 0.38 | 744 | 91927.69 |
| additive_val90 | SWPP | 2.53 | 2.11 | -0.30 | -1.60 | 1.50 | -20.36 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_val90 | TVA | 3.35 | 2.99 | -1.04 | -2.34 | 1.44 | -14.12 | 0.25 | 0.25 | 739 | 18562.62 |
| boosting_7y | BPAT | 2.74 | 2.45 | -0.42 | -1.57 | 2.03 | -17.58 | 0.28 | 0.25 | 750 | 6533.15 |
| boosting_7y | CISO | 3.02 | 2.66 | -2.07 | -2.66 | 0.40 | -19.33 | 0.35 | 0.15 | 737 | 25196.34 |
| boosting_7y | DUK | 3.57 | 3.09 | -0.38 | -2.24 | 1.47 | -15.99 | 0.34 | 0.28 | 750 | 12129.97 |
| boosting_7y | ERCO | 3.14 | 2.70 | -2.24 | -2.96 | 1.30 | -15.00 | 0.34 | 0.18 | 746 | 46782.53 |
| boosting_7y | FPL | 6.24 | 5.87 | -6.57 | -6.89 | 1.25 | -52.85 | 0.21 | 0.27 | 690 | 15275.13 |
| boosting_7y | ISNE | 3.65 | 3.28 | -0.80 | -2.05 | 0.57 | -19.10 | 0.26 | 0.16 | 752 | 13392.81 |
| boosting_7y | MISO | 2.41 | 2.05 | -0.52 | -1.46 | 1.78 | -12.64 | 0.54 | 0.06 | 746 | 73788.38 |
| boosting_7y | NYIS | 2.70 | 2.36 | -0.45 | -1.58 | 0.73 | -13.58 | 0.52 | 0.66 | 752 | 17400.75 |
| boosting_7y | PJM | 2.82 | 2.54 | 0.07 | -1.43 | 1.81 | -11.43 | 0.41 | 0.43 | 744 | 91927.69 |
| boosting_7y | SWPP | 2.65 | 2.19 | -0.85 | -1.94 | 1.64 | -28.75 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_7y | TVA | 3.26 | 2.79 | -0.23 | -1.82 | 1.54 | -15.07 | 0.26 | 0.30 | 739 | 18562.62 |
| boosting_deep | BPAT | 2.69 | 2.42 | -0.38 | -1.52 | 1.96 | -20.05 | 0.29 | 0.24 | 750 | 6533.15 |
| boosting_deep | CISO | 2.94 | 2.56 | -2.02 | -2.62 | 0.38 | -19.08 | 0.37 | 0.15 | 737 | 25196.34 |
| boosting_deep | DUK | 3.52 | 3.07 | -0.27 | -2.16 | 1.39 | -18.31 | 0.36 | 0.29 | 750 | 12129.97 |
| boosting_deep | ERCO | 3.05 | 2.61 | -2.16 | -2.85 | 1.30 | -14.60 | 0.38 | 0.18 | 746 | 46782.53 |
| boosting_deep | FPL | 6.23 | 5.83 | -6.39 | -6.75 | 1.20 | -51.84 | 0.19 | 0.27 | 690 | 15275.13 |
| boosting_deep | ISNE | 3.61 | 3.22 | -0.57 | -1.94 | 0.52 | -22.39 | 0.25 | 0.19 | 752 | 13392.81 |
| boosting_deep | MISO | 2.37 | 2.06 | -0.52 | -1.43 | 1.62 | -12.44 | 0.56 | 0.06 | 746 | 73788.38 |
| boosting_deep | NYIS | 2.65 | 2.28 | -0.15 | -1.46 | 0.70 | -15.02 | 0.53 | 0.70 | 752 | 17400.75 |
| boosting_deep | PJM | 2.79 | 2.49 | 0.28 | -1.34 | 1.74 | -12.43 | 0.43 | 0.44 | 744 | 91927.69 |
| boosting_deep | SWPP | 2.60 | 2.11 | -0.64 | -1.84 | 1.51 | -28.42 | 0.68 | 0.09 | 745 | 31350.31 |
| boosting_deep | TVA | 3.22 | 2.76 | -0.14 | -1.77 | 1.50 | -16.53 | 0.25 | 0.30 | 739 | 18562.62 |
| boosting_l2 | BPAT | 2.73 | 2.44 | -0.48 | -1.59 | 1.97 | -18.40 | 0.27 | 0.24 | 750 | 6533.15 |
| boosting_l2 | CISO | 3.01 | 2.66 | -2.07 | -2.67 | 0.40 | -19.21 | 0.36 | 0.16 | 737 | 25196.34 |
| boosting_l2 | DUK | 3.56 | 3.10 | -0.40 | -2.24 | 1.52 | -17.15 | 0.34 | 0.28 | 750 | 12129.97 |
| boosting_l2 | ERCO | 3.11 | 2.69 | -2.30 | -2.99 | 1.32 | -15.60 | 0.36 | 0.17 | 746 | 46782.53 |
| boosting_l2 | FPL | 6.27 | 5.89 | -6.53 | -6.88 | 1.30 | -52.05 | 0.19 | 0.27 | 690 | 15275.13 |
| boosting_l2 | ISNE | 3.66 | 3.30 | -0.82 | -2.09 | 0.61 | -21.28 | 0.26 | 0.17 | 752 | 13392.81 |
| boosting_l2 | MISO | 2.40 | 2.05 | -0.47 | -1.42 | 1.72 | -11.42 | 0.55 | 0.06 | 746 | 73788.38 |
| boosting_l2 | NYIS | 2.70 | 2.37 | -0.44 | -1.59 | 0.69 | -13.70 | 0.51 | 0.66 | 752 | 17400.75 |
| boosting_l2 | PJM | 2.83 | 2.51 | 0.12 | -1.43 | 1.71 | -11.30 | 0.40 | 0.43 | 744 | 91927.69 |
| boosting_l2 | SWPP | 2.64 | 2.14 | -0.89 | -2.00 | 1.58 | -27.46 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_l2 | TVA | 3.27 | 2.77 | -0.23 | -1.85 | 1.57 | -15.50 | 0.26 | 0.29 | 739 | 18562.62 |
| boosting_refit3 | BPAT | 2.70 | 2.43 | -0.49 | -1.61 | 1.95 | -18.35 | 0.28 | 0.24 | 750 | 6533.15 |
| boosting_refit3 | CISO | 3.02 | 2.65 | -2.15 | -2.70 | 0.40 | -18.88 | 0.35 | 0.15 | 737 | 25196.34 |
| boosting_refit3 | DUK | 3.53 | 3.04 | -0.44 | -2.25 | 1.43 | -16.41 | 0.36 | 0.27 | 750 | 12129.97 |
| boosting_refit3 | ERCO | 3.08 | 2.68 | -2.16 | -2.86 | 1.32 | -14.94 | 0.36 | 0.18 | 746 | 46782.53 |
| boosting_refit3 | FPL | 6.31 | 5.98 | -6.57 | -6.92 | 1.32 | -50.67 | 0.19 | 0.27 | 690 | 15275.13 |
| boosting_refit3 | ISNE | 3.69 | 3.27 | -0.88 | -2.12 | 0.57 | -18.56 | 0.25 | 0.17 | 752 | 13392.81 |
| boosting_refit3 | MISO | 2.39 | 2.08 | -0.56 | -1.47 | 1.74 | -12.88 | 0.55 | 0.06 | 746 | 73788.38 |
| boosting_refit3 | NYIS | 2.73 | 2.40 | -0.49 | -1.63 | 0.71 | -13.52 | 0.50 | 0.65 | 752 | 17400.75 |
| boosting_refit3 | PJM | 2.82 | 2.53 | 0.04 | -1.48 | 1.79 | -10.57 | 0.41 | 0.41 | 744 | 91927.69 |
| boosting_refit3 | SWPP | 2.59 | 2.18 | -0.75 | -1.85 | 1.54 | -21.10 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_refit3 | TVA | 3.23 | 2.86 | -0.33 | -1.89 | 1.57 | -16.13 | 0.25 | 0.29 | 739 | 18562.62 |
| boosting_shallow | BPAT | 2.74 | 2.49 | -0.61 | -1.70 | 2.05 | -18.18 | 0.27 | 0.24 | 750 | 6533.15 |
| boosting_shallow | CISO | 3.16 | 2.74 | -2.39 | -2.96 | 0.44 | -18.54 | 0.31 | 0.15 | 737 | 25196.34 |
| boosting_shallow | DUK | 3.67 | 3.19 | -0.83 | -2.52 | 1.58 | -15.68 | 0.31 | 0.26 | 750 | 12129.97 |
| boosting_shallow | ERCO | 3.33 | 2.85 | -2.52 | -3.20 | 1.36 | -16.61 | 0.32 | 0.17 | 746 | 46782.53 |
| boosting_shallow | FPL | 6.31 | 6.05 | -6.66 | -6.99 | 1.32 | -51.19 | 0.19 | 0.27 | 690 | 15275.13 |
| boosting_shallow | ISNE | 3.79 | 3.48 | -1.20 | -2.28 | 0.63 | -20.91 | 0.24 | 0.15 | 752 | 13392.81 |
| boosting_shallow | MISO | 2.47 | 2.16 | -0.70 | -1.56 | 1.72 | -12.17 | 0.54 | 0.06 | 746 | 73788.38 |
| boosting_shallow | NYIS | 2.88 | 2.53 | -0.86 | -1.86 | 0.78 | -14.28 | 0.47 | 0.62 | 752 | 17400.75 |
| boosting_shallow | PJM | 2.89 | 2.60 | -0.30 | -1.62 | 1.76 | -12.08 | 0.40 | 0.39 | 744 | 91927.69 |
| boosting_shallow | SWPP | 2.75 | 2.29 | -1.12 | -2.18 | 1.80 | -27.40 | 0.66 | 0.08 | 745 | 31350.31 |
| boosting_shallow | TVA | 3.38 | 2.94 | -0.58 | -2.10 | 1.65 | -16.11 | 0.22 | 0.28 | 739 | 18562.62 |
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
| additive_7y | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| additive_7y | CISO | uri | 2.40 | 2.19 | 0.00 | 0.00 | 6 |
| additive_7y | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| additive_7y | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| additive_7y | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| additive_7y | ISNE | uri | 2.56 | 1.52 | -0.29 | -1.49 | 6 |
| additive_7y | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| additive_7y | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| additive_7y | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_7y | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_7y | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| additive_k10 | BPAT | uri | 3.00 | -0.20 | -1.27 | -2.80 | 6 |
| additive_k10 | CISO | uri | 2.49 | 2.14 | 0.00 | 0.00 | 6 |
| additive_k10 | DUK | uri | 3.43 | -2.65 | -2.65 | -8.06 | 6 |
| additive_k10 | ERCO | uri | 5.10 | -6.38 | -6.38 | -8.36 | 2 |
| additive_k10 | FPL | uri | 10.35 | -14.74 | -14.74 | -18.57 | 6 |
| additive_k10 | ISNE | uri | 2.55 | 1.54 | -0.30 | -1.48 | 6 |
| additive_k10 | MISO | uri | 3.38 | -2.07 | -2.56 | -5.58 | 5 |
| additive_k10 | NYIS | uri | 2.19 | 1.94 | -0.09 | -0.36 | 6 |
| additive_k10 | PJM | uri | 2.85 | 2.13 | -0.51 | -2.87 | 6 |
| additive_k10 | SWPP | uri | 6.39 | 2.32 | -1.42 | -4.79 | 4 |
| additive_k10 | TVA | uri | 3.41 | 0.07 | -1.35 | -3.17 | 6 |
| additive_k8 | BPAT | uri | 3.18 | -0.31 | -1.38 | -3.29 | 6 |
| additive_k8 | CISO | uri | 2.50 | 2.28 | 0.00 | 0.00 | 6 |
| additive_k8 | DUK | uri | 3.44 | -2.69 | -2.69 | -8.13 | 6 |
| additive_k8 | ERCO | uri | 5.28 | -6.78 | -6.78 | -8.31 | 2 |
| additive_k8 | FPL | uri | 10.30 | -14.62 | -14.62 | -18.18 | 6 |
| additive_k8 | ISNE | uri | 2.54 | 1.47 | -0.31 | -1.53 | 6 |
| additive_k8 | MISO | uri | 3.49 | -2.22 | -2.72 | -5.58 | 5 |
| additive_k8 | NYIS | uri | 2.20 | 1.96 | -0.08 | -0.27 | 6 |
| additive_k8 | PJM | uri | 2.91 | 2.14 | -0.51 | -2.73 | 6 |
| additive_k8 | SWPP | uri | 6.41 | 2.12 | -1.59 | -4.88 | 4 |
| additive_k8 | TVA | uri | 3.33 | 0.15 | -1.25 | -3.07 | 6 |
| additive_lam | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| additive_lam | CISO | uri | 2.35 | 2.03 | 0.00 | 0.00 | 6 |
| additive_lam | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| additive_lam | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| additive_lam | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| additive_lam | ISNE | uri | 2.56 | 1.52 | -0.29 | -1.49 | 6 |
| additive_lam | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| additive_lam | NYIS | uri | 2.08 | 2.29 | -0.12 | -0.71 | 6 |
| additive_lam | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_lam | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_lam | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| additive_val90 | BPAT | uri | 3.20 | -0.38 | -1.43 | -3.22 | 6 |
| additive_val90 | CISO | uri | 2.18 | 2.30 | 0.00 | 0.00 | 6 |
| additive_val90 | DUK | uri | 3.46 | -2.66 | -2.66 | -8.00 | 6 |
| additive_val90 | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| additive_val90 | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| additive_val90 | ISNE | uri | 2.56 | 1.45 | -0.35 | -1.18 | 6 |
| additive_val90 | MISO | uri | 3.59 | -2.58 | -2.94 | -5.40 | 5 |
| additive_val90 | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| additive_val90 | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_val90 | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_val90 | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| boosting_7y | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| boosting_7y | CISO | uri | 1.85 | -0.83 | -0.99 | -2.55 | 6 |
| boosting_7y | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_7y | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| boosting_7y | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| boosting_7y | ISNE | uri | 3.32 | 1.07 | -0.73 | -3.06 | 6 |
| boosting_7y | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_7y | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| boosting_7y | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_7y | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_7y | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| boosting_deep | BPAT | uri | 3.38 | 1.25 | -0.77 | -4.62 | 6 |
| boosting_deep | CISO | uri | 1.98 | -0.06 | -0.56 | -2.28 | 6 |
| boosting_deep | DUK | uri | 3.37 | -2.88 | -2.88 | -6.14 | 6 |
| boosting_deep | ERCO | uri | 7.24 | -11.31 | -11.31 | -13.82 | 2 |
| boosting_deep | FPL | uri | 9.49 | -11.41 | -11.41 | -16.83 | 6 |
| boosting_deep | ISNE | uri | 3.20 | 2.02 | -0.53 | -3.16 | 6 |
| boosting_deep | MISO | uri | 2.71 | -3.35 | -3.49 | -7.15 | 5 |
| boosting_deep | NYIS | uri | 1.96 | 0.73 | -0.66 | -2.81 | 6 |
| boosting_deep | PJM | uri | 2.08 | -0.26 | -0.96 | -3.04 | 6 |
| boosting_deep | SWPP | uri | 5.67 | -2.01 | -3.75 | -9.43 | 4 |
| boosting_deep | TVA | uri | 2.83 | -3.47 | -3.77 | -7.19 | 6 |
| boosting_l2 | BPAT | uri | 3.64 | 0.87 | -1.00 | -5.26 | 6 |
| boosting_l2 | CISO | uri | 1.79 | -0.61 | -0.79 | -2.05 | 6 |
| boosting_l2 | DUK | uri | 3.54 | -2.85 | -2.85 | -4.87 | 6 |
| boosting_l2 | ERCO | uri | 9.25 | -13.43 | -13.43 | -15.60 | 2 |
| boosting_l2 | FPL | uri | 9.39 | -11.41 | -11.41 | -16.43 | 6 |
| boosting_l2 | ISNE | uri | 3.28 | 0.99 | -0.70 | -3.34 | 6 |
| boosting_l2 | MISO | uri | 2.96 | -3.59 | -3.59 | -7.01 | 5 |
| boosting_l2 | NYIS | uri | 2.34 | 1.03 | -0.61 | -2.66 | 6 |
| boosting_l2 | PJM | uri | 1.91 | -1.27 | -1.33 | -3.21 | 6 |
| boosting_l2 | SWPP | uri | 5.60 | -2.32 | -3.99 | -9.71 | 4 |
| boosting_l2 | TVA | uri | 2.91 | -2.95 | -3.33 | -6.19 | 6 |
| boosting_refit3 | BPAT | uri | 3.63 | 0.92 | -1.07 | -5.44 | 6 |
| boosting_refit3 | CISO | uri | 2.01 | -1.26 | -1.38 | -3.67 | 6 |
| boosting_refit3 | DUK | uri | 3.49 | -3.13 | -3.13 | -6.25 | 6 |
| boosting_refit3 | ERCO | uri | 7.96 | -12.67 | -12.67 | -14.94 | 2 |
| boosting_refit3 | FPL | uri | 9.62 | -11.83 | -11.83 | -15.65 | 6 |
| boosting_refit3 | ISNE | uri | 3.22 | 0.57 | -0.81 | -3.21 | 6 |
| boosting_refit3 | MISO | uri | 3.27 | -3.35 | -3.74 | -8.30 | 5 |
| boosting_refit3 | NYIS | uri | 1.97 | 0.41 | -0.57 | -2.39 | 6 |
| boosting_refit3 | PJM | uri | 2.15 | -1.25 | -1.47 | -3.84 | 6 |
| boosting_refit3 | SWPP | uri | 6.27 | -1.08 | -3.58 | -9.16 | 4 |
| boosting_refit3 | TVA | uri | 3.04 | -3.02 | -3.48 | -7.14 | 6 |
| boosting_shallow | BPAT | uri | 3.44 | 0.48 | -1.09 | -5.94 | 6 |
| boosting_shallow | CISO | uri | 2.22 | -1.24 | -1.55 | -3.57 | 6 |
| boosting_shallow | DUK | uri | 4.01 | -4.47 | -4.47 | -6.52 | 6 |
| boosting_shallow | ERCO | uri | 8.91 | -14.48 | -14.48 | -16.61 | 2 |
| boosting_shallow | FPL | uri | 9.09 | -11.59 | -11.59 | -15.73 | 6 |
| boosting_shallow | ISNE | uri | 3.65 | 0.74 | -0.68 | -2.36 | 6 |
| boosting_shallow | MISO | uri | 2.72 | -2.35 | -2.52 | -5.93 | 5 |
| boosting_shallow | NYIS | uri | 2.39 | 0.62 | -0.83 | -3.16 | 6 |
| boosting_shallow | PJM | uri | 1.97 | -1.81 | -1.81 | -4.72 | 6 |
| boosting_shallow | SWPP | uri | 6.20 | -4.19 | -5.14 | -11.42 | 4 |
| boosting_shallow | TVA | uri | 3.41 | -3.05 | -3.42 | -8.12 | 6 |
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
| additive_7y | BPAT | elliott | 4.25 | -1.35 | -2.31 | -4.68 | 5 |
| additive_7y | CISO | elliott | 3.50 | 4.10 | -0.07 | -0.35 | 5 |
| additive_7y | DUK | elliott | 4.21 | -2.34 | -2.58 | -5.69 | 4 |
| additive_7y | ERCO | elliott | 7.89 | -4.98 | -5.94 | -12.21 | 5 |
| additive_7y | FPL | elliott | 11.79 | -1.90 | -7.58 | -19.32 | 5 |
| additive_7y | ISNE | elliott | 3.98 | 1.48 | -0.70 | -2.74 | 5 |
| additive_7y | MISO | elliott | 3.36 | -3.19 | -3.57 | -6.14 | 5 |
| additive_7y | NYIS | elliott | 3.32 | -2.08 | -2.48 | -4.04 | 5 |
| additive_7y | PJM | elliott | 3.63 | -1.97 | -2.52 | -6.73 | 5 |
| additive_7y | SWPP | elliott | 3.61 | -2.38 | -2.94 | -6.77 | 5 |
| additive_7y | TVA | elliott | 7.86 | 5.44 | 0.00 | 0.00 | 3 |
| additive_k10 | BPAT | elliott | 4.23 | -1.31 | -2.34 | -5.14 | 5 |
| additive_k10 | CISO | elliott | 3.65 | 4.00 | -0.14 | -0.69 | 5 |
| additive_k10 | DUK | elliott | 3.90 | -1.20 | -2.17 | -4.37 | 4 |
| additive_k10 | ERCO | elliott | 7.50 | -3.99 | -4.94 | -9.53 | 5 |
| additive_k10 | FPL | elliott | 12.90 | 0.02 | -7.88 | -20.63 | 5 |
| additive_k10 | ISNE | elliott | 3.94 | 2.06 | -0.62 | -2.22 | 5 |
| additive_k10 | MISO | elliott | 3.75 | -4.64 | -4.99 | -11.33 | 5 |
| additive_k10 | NYIS | elliott | 3.33 | -2.09 | -2.53 | -3.82 | 5 |
| additive_k10 | PJM | elliott | 3.79 | -2.24 | -2.88 | -7.38 | 5 |
| additive_k10 | SWPP | elliott | 3.96 | -2.96 | -3.46 | -6.99 | 5 |
| additive_k10 | TVA | elliott | 6.68 | 4.61 | 0.00 | 0.00 | 3 |
| additive_k8 | BPAT | elliott | 4.27 | -1.30 | -2.34 | -5.07 | 5 |
| additive_k8 | CISO | elliott | 3.51 | 4.07 | -0.06 | -0.28 | 5 |
| additive_k8 | DUK | elliott | 3.96 | -2.07 | -2.41 | -5.23 | 4 |
| additive_k8 | ERCO | elliott | 7.68 | -4.48 | -5.45 | -10.19 | 5 |
| additive_k8 | FPL | elliott | 12.37 | 0.29 | -7.34 | -19.36 | 5 |
| additive_k8 | ISNE | elliott | 3.94 | 1.63 | -0.64 | -2.29 | 5 |
| additive_k8 | MISO | elliott | 3.60 | -3.80 | -4.15 | -6.83 | 5 |
| additive_k8 | NYIS | elliott | 3.27 | -1.96 | -2.40 | -3.82 | 5 |
| additive_k8 | PJM | elliott | 3.74 | -2.15 | -2.77 | -7.12 | 5 |
| additive_k8 | SWPP | elliott | 3.78 | -2.73 | -3.18 | -6.73 | 5 |
| additive_k8 | TVA | elliott | 7.94 | 5.39 | 0.00 | 0.00 | 3 |
| additive_lam | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| additive_lam | CISO | elliott | 3.53 | 4.14 | -0.08 | -0.41 | 5 |
| additive_lam | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| additive_lam | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| additive_lam | FPL | elliott | 11.83 | -1.71 | -7.55 | -19.18 | 5 |
| additive_lam | ISNE | elliott | 3.99 | 1.75 | -0.62 | -2.38 | 5 |
| additive_lam | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| additive_lam | NYIS | elliott | 3.04 | -1.83 | -2.47 | -3.33 | 5 |
| additive_lam | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| additive_lam | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| additive_lam | TVA | elliott | 7.91 | 5.47 | 0.00 | 0.00 | 3 |
| additive_val90 | BPAT | elliott | 4.30 | -1.55 | -2.54 | -5.00 | 5 |
| additive_val90 | CISO | elliott | 3.53 | 4.14 | -0.08 | -0.41 | 5 |
| additive_val90 | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| additive_val90 | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| additive_val90 | FPL | elliott | 11.98 | -1.71 | -7.57 | -19.26 | 5 |
| additive_val90 | ISNE | elliott | 3.99 | 1.75 | -0.62 | -2.38 | 5 |
| additive_val90 | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| additive_val90 | NYIS | elliott | 3.27 | -1.91 | -2.37 | -3.71 | 5 |
| additive_val90 | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| additive_val90 | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| additive_val90 | TVA | elliott | 6.62 | 4.76 | 0.00 | 0.00 | 3 |
| boosting_7y | BPAT | elliott | 4.52 | -5.50 | -5.63 | -12.41 | 5 |
| boosting_7y | CISO | elliott | 3.51 | 1.50 | -1.12 | -4.39 | 5 |
| boosting_7y | DUK | elliott | 4.13 | -3.57 | -3.57 | -6.38 | 4 |
| boosting_7y | ERCO | elliott | 6.12 | -3.24 | -5.06 | -13.29 | 5 |
| boosting_7y | FPL | elliott | 12.12 | -17.05 | -17.05 | -23.35 | 5 |
| boosting_7y | ISNE | elliott | 3.53 | 3.23 | -0.41 | -1.69 | 5 |
| boosting_7y | MISO | elliott | 3.63 | -0.75 | -1.95 | -3.33 | 5 |
| boosting_7y | NYIS | elliott | 2.85 | 0.03 | -0.98 | -2.66 | 5 |
| boosting_7y | PJM | elliott | 5.02 | -2.24 | -3.07 | -6.54 | 5 |
| boosting_7y | SWPP | elliott | 4.76 | -1.16 | -3.31 | -10.61 | 5 |
| boosting_7y | TVA | elliott | 5.92 | 0.40 | -1.38 | -4.01 | 3 |
| boosting_deep | BPAT | elliott | 4.24 | -4.79 | -4.91 | -10.52 | 5 |
| boosting_deep | CISO | elliott | 3.21 | 1.51 | -0.75 | -3.76 | 5 |
| boosting_deep | DUK | elliott | 4.22 | -3.42 | -3.45 | -7.78 | 4 |
| boosting_deep | ERCO | elliott | 6.08 | -3.77 | -5.43 | -13.71 | 5 |
| boosting_deep | FPL | elliott | 8.19 | -13.53 | -13.53 | -21.03 | 5 |
| boosting_deep | ISNE | elliott | 3.29 | 3.07 | -0.22 | -0.62 | 5 |
| boosting_deep | MISO | elliott | 4.06 | -0.76 | -2.18 | -3.94 | 5 |
| boosting_deep | NYIS | elliott | 2.79 | 0.10 | -1.03 | -3.31 | 5 |
| boosting_deep | PJM | elliott | 5.10 | -1.06 | -2.74 | -5.99 | 5 |
| boosting_deep | SWPP | elliott | 5.34 | -0.91 | -3.63 | -11.08 | 5 |
| boosting_deep | TVA | elliott | 6.14 | 2.19 | -0.08 | -0.25 | 3 |
| boosting_l2 | BPAT | elliott | 4.54 | -5.55 | -5.57 | -12.97 | 5 |
| boosting_l2 | CISO | elliott | 3.75 | 1.75 | -0.67 | -3.05 | 5 |
| boosting_l2 | DUK | elliott | 4.43 | -3.90 | -3.90 | -7.25 | 4 |
| boosting_l2 | ERCO | elliott | 6.04 | -3.00 | -4.83 | -12.59 | 5 |
| boosting_l2 | FPL | elliott | 8.92 | -14.52 | -14.52 | -20.57 | 5 |
| boosting_l2 | ISNE | elliott | 3.53 | 2.65 | -0.33 | -1.19 | 5 |
| boosting_l2 | MISO | elliott | 3.74 | -0.80 | -2.06 | -3.60 | 5 |
| boosting_l2 | NYIS | elliott | 2.77 | -0.55 | -1.38 | -4.22 | 5 |
| boosting_l2 | PJM | elliott | 5.30 | -1.73 | -3.05 | -5.70 | 5 |
| boosting_l2 | SWPP | elliott | 4.88 | -1.91 | -3.82 | -10.98 | 5 |
| boosting_l2 | TVA | elliott | 5.85 | 0.52 | -1.12 | -3.12 | 3 |
| boosting_refit3 | BPAT | elliott | 4.17 | -5.57 | -5.57 | -12.18 | 5 |
| boosting_refit3 | CISO | elliott | 3.62 | 1.14 | -1.15 | -5.15 | 5 |
| boosting_refit3 | DUK | elliott | 4.02 | -2.66 | -2.66 | -7.02 | 4 |
| boosting_refit3 | ERCO | elliott | 5.38 | -5.18 | -5.89 | -13.09 | 5 |
| boosting_refit3 | FPL | elliott | 9.24 | -13.95 | -13.95 | -19.69 | 5 |
| boosting_refit3 | ISNE | elliott | 3.29 | 2.19 | -0.50 | -2.02 | 5 |
| boosting_refit3 | MISO | elliott | 3.80 | -0.36 | -1.81 | -2.89 | 5 |
| boosting_refit3 | NYIS | elliott | 2.82 | 0.27 | -0.80 | -2.79 | 5 |
| boosting_refit3 | PJM | elliott | 5.29 | -2.34 | -3.28 | -6.65 | 5 |
| boosting_refit3 | SWPP | elliott | 4.14 | -3.53 | -4.21 | -10.54 | 5 |
| boosting_refit3 | TVA | elliott | 5.65 | -0.08 | -1.30 | -3.90 | 3 |
| boosting_shallow | BPAT | elliott | 4.33 | -6.04 | -6.07 | -13.54 | 5 |
| boosting_shallow | CISO | elliott | 3.96 | 1.90 | -0.81 | -3.74 | 5 |
| boosting_shallow | DUK | elliott | 4.27 | -5.59 | -5.59 | -9.46 | 4 |
| boosting_shallow | ERCO | elliott | 5.87 | -5.17 | -5.91 | -13.34 | 5 |
| boosting_shallow | FPL | elliott | 9.87 | -15.49 | -15.49 | -21.98 | 5 |
| boosting_shallow | ISNE | elliott | 3.60 | 2.88 | -0.31 | -1.54 | 5 |
| boosting_shallow | MISO | elliott | 3.59 | -1.16 | -2.28 | -3.45 | 5 |
| boosting_shallow | NYIS | elliott | 3.32 | -0.05 | -1.20 | -2.32 | 5 |
| boosting_shallow | PJM | elliott | 4.92 | -3.07 | -3.66 | -8.09 | 5 |
| boosting_shallow | SWPP | elliott | 4.44 | -2.13 | -3.52 | -10.33 | 5 |
| boosting_shallow | TVA | elliott | 5.78 | 0.60 | -1.96 | -5.87 | 3 |
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

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | DF | eve | 3.37 | 0.49 | -1.42 |  | 268 |
| 22 | boosting_refit3 | eve | 3.77 | -0.10 | -2.06 | 0.40 | 268 |
| 20 | boosting_deep | eve | 3.81 | 0.16 | -1.96 | 0.42 | 268 |
| 14 | additive_7y | eve | 3.82 | -0.16 | -2.21 | 0.40 | 268 |
| 24 | final_additive | eve | 3.83 | -0.12 | -2.19 | 0.40 | 268 |
| 18 | additive_val90 | eve | 3.84 | -0.13 | -2.21 | 0.40 | 268 |
| 16 | additive_k8 | eve | 3.84 | -0.14 | -2.22 | 0.40 | 268 |
| 21 | boosting_l2 | eve | 3.85 | -0.07 | -2.09 | 0.38 | 268 |
| 17 | additive_lam | eve | 3.85 | -0.11 | -2.19 | 0.41 | 268 |
| 25 | final_boosting | eve | 3.86 | -0.07 | -2.12 | 0.40 | 268 |
| 15 | additive_k10 | eve | 3.87 | -0.14 | -2.25 | 0.41 | 268 |
| 19 | boosting_7y | eve | 3.88 | 0.00 | -2.07 | 0.37 | 268 |
| 23 | boosting_shallow | eve | 3.93 | -0.39 | -2.30 | 0.40 | 268 |
| 0 | DF | special | 3.70 | -0.13 | -1.77 |  | 270 |
| 4 | additive_lam | special | 3.83 | -1.73 | -3.01 | 0.46 | 270 |
| 1 | additive_7y | special | 3.84 | -1.92 | -3.13 | 0.46 | 270 |
| 11 | final_additive | special | 3.84 | -1.83 | -3.08 | 0.46 | 270 |
| 5 | additive_val90 | special | 3.85 | -1.86 | -3.11 | 0.46 | 270 |
| 7 | boosting_deep | special | 3.86 | -1.38 | -2.75 | 0.46 | 270 |
| 3 | additive_k8 | special | 3.87 | -1.83 | -3.11 | 0.46 | 270 |
| 2 | additive_k10 | special | 3.87 | -1.83 | -3.13 | 0.45 | 270 |
| 9 | boosting_refit3 | special | 3.91 | -1.62 | -2.90 | 0.43 | 270 |
| 8 | boosting_l2 | special | 3.91 | -1.61 | -2.88 | 0.44 | 270 |
| 12 | final_boosting | special | 3.93 | -1.60 | -2.93 | 0.42 | 270 |
| 6 | boosting_7y | special | 3.94 | -1.60 | -2.88 | 0.42 | 270 |
| 10 | boosting_shallow | special | 4.13 | -2.00 | -3.26 | 0.39 | 270 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 29002 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 29001 | DUK | 2022-12-24 | additive_7y | 7.30 | -12.87 | -12.87 |
| 28998 | DUK | 2022-12-24 | additive_k10 | 7.69 | -13.17 | -13.17 |
| 28997 | DUK | 2022-12-24 | additive_k8 | 7.68 | -13.38 | -13.38 |
| 29000 | DUK | 2022-12-24 | additive_lam | 7.26 | -12.67 | -12.67 |
| 28999 | DUK | 2022-12-24 | additive_val90 | 7.26 | -12.67 | -12.67 |
| 28996 | DUK | 2022-12-24 | boosting_7y | 9.86 | -16.76 | -16.76 |
| 28992 | DUK | 2022-12-24 | boosting_deep | 9.55 | -18.81 | -18.81 |
| 28994 | DUK | 2022-12-24 | boosting_l2 | 9.53 | -16.92 | -16.92 |
| 28995 | DUK | 2022-12-24 | boosting_refit3 | 9.53 | -16.59 | -16.59 |
| 28993 | DUK | 2022-12-24 | boosting_shallow | 11.57 | -20.37 | -20.37 |
| 28990 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 28991 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 30068 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 30067 | ERCO | 2021-02-17 | additive_7y | 31.74 | 29.84 | 0.00 |
| 30064 | ERCO | 2021-02-17 | additive_k10 | 30.08 | 29.13 | 0.00 |
| 30063 | ERCO | 2021-02-17 | additive_k8 | 30.79 | 29.83 | 0.00 |
| 30066 | ERCO | 2021-02-17 | additive_lam | 31.74 | 29.84 | 0.00 |
| 30065 | ERCO | 2021-02-17 | additive_val90 | 31.74 | 29.84 | 0.00 |
| 30062 | ERCO | 2021-02-17 | boosting_7y | 28.91 | 24.01 | 0.00 |
| 30058 | ERCO | 2021-02-17 | boosting_deep | 30.10 | 23.52 | 0.00 |
| 30060 | ERCO | 2021-02-17 | boosting_l2 | 29.12 | 24.75 | 0.00 |
| 30061 | ERCO | 2021-02-17 | boosting_refit3 | 31.02 | 24.43 | 0.00 |
| 30059 | ERCO | 2021-02-17 | boosting_shallow | 26.16 | 20.61 | 0.00 |
| 30056 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 30057 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 30081 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 30080 | ERCO | 2021-02-18 | additive_7y | 13.46 | 12.91 | 0.00 |
| 30077 | ERCO | 2021-02-18 | additive_k10 | 15.10 | 13.99 | 0.00 |
| 30076 | ERCO | 2021-02-18 | additive_k8 | 14.59 | 13.74 | 0.00 |
| 30079 | ERCO | 2021-02-18 | additive_lam | 13.46 | 12.91 | 0.00 |
| 30078 | ERCO | 2021-02-18 | additive_val90 | 13.46 | 12.91 | 0.00 |
| 30075 | ERCO | 2021-02-18 | boosting_7y | 3.58 | -2.96 | -2.96 |
| 30071 | ERCO | 2021-02-18 | boosting_deep | 4.54 | 0.22 | 0.00 |
| 30073 | ERCO | 2021-02-18 | boosting_l2 | 3.13 | -5.43 | -5.43 |
| 30074 | ERCO | 2021-02-18 | boosting_refit3 | 14.49 | 10.03 | 0.00 |
| 30072 | ERCO | 2021-02-18 | boosting_shallow | 5.69 | 0.20 | 0.00 |
| 30069 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 30070 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 58551 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 58550 | MISO | 2021-02-16 | additive_7y | 2.38 | 1.99 | 0.00 |
| 58547 | MISO | 2021-02-16 | additive_k10 | 2.65 | 2.11 | 0.00 |
| 58546 | MISO | 2021-02-16 | additive_k8 | 2.47 | 1.98 | 0.00 |
| 58549 | MISO | 2021-02-16 | additive_lam | 2.38 | 1.99 | 0.00 |
| 58548 | MISO | 2021-02-16 | additive_val90 | 2.48 | 2.09 | 0.00 |
| 58545 | MISO | 2021-02-16 | boosting_7y | 2.11 | 0.99 | 0.00 |
| 58541 | MISO | 2021-02-16 | boosting_deep | 1.99 | 0.87 | 0.00 |
| 58543 | MISO | 2021-02-16 | boosting_l2 | 2.66 | 1.86 | 0.00 |
| 58544 | MISO | 2021-02-16 | boosting_refit3 | 4.03 | 2.56 | 0.00 |
| 58542 | MISO | 2021-02-16 | boosting_shallow | 3.86 | 1.36 | 0.00 |
| 58539 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 58540 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 87697 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 87696 | SWPP | 2021-02-15 | additive_7y | 2.66 | 1.09 | 0.00 |
| 87693 | SWPP | 2021-02-15 | additive_k10 | 3.99 | 2.82 | 0.00 |
| 87692 | SWPP | 2021-02-15 | additive_k8 | 3.66 | 2.48 | 0.00 |
| 87695 | SWPP | 2021-02-15 | additive_lam | 2.66 | 1.09 | 0.00 |
| 87694 | SWPP | 2021-02-15 | additive_val90 | 2.66 | 1.09 | 0.00 |
| 87691 | SWPP | 2021-02-15 | boosting_7y | 5.58 | -7.79 | -7.79 |
| 87687 | SWPP | 2021-02-15 | boosting_deep | 5.50 | -7.96 | -7.96 |
| 87689 | SWPP | 2021-02-15 | boosting_l2 | 5.02 | -7.10 | -7.10 |
| 87690 | SWPP | 2021-02-15 | boosting_refit3 | 4.26 | -6.83 | -6.83 |
| 87688 | SWPP | 2021-02-15 | boosting_shallow | 5.04 | -7.81 | -7.81 |
| 87685 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 87686 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 87710 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 87709 | SWPP | 2021-02-16 | additive_7y | 8.09 | 3.29 | 0.00 |
| 87706 | SWPP | 2021-02-16 | additive_k10 | 9.53 | 4.85 | 0.00 |
| 87705 | SWPP | 2021-02-16 | additive_k8 | 9.20 | 4.60 | 0.00 |
| 87708 | SWPP | 2021-02-16 | additive_lam | 8.09 | 3.29 | 0.00 |
| 87707 | SWPP | 2021-02-16 | additive_val90 | 8.09 | 3.29 | 0.00 |
| 87704 | SWPP | 2021-02-16 | boosting_7y | 3.72 | -6.44 | -6.44 |
| 87700 | SWPP | 2021-02-16 | boosting_deep | 3.62 | -6.58 | -6.58 |
| 87702 | SWPP | 2021-02-16 | boosting_l2 | 3.61 | -5.96 | -5.96 |
| 87703 | SWPP | 2021-02-16 | boosting_refit3 | 5.59 | -3.82 | -3.82 |
| 87701 | SWPP | 2021-02-16 | boosting_shallow | 3.49 | -6.14 | -6.14 |
| 87698 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 87699 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 105962 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 105961 | TVA | 2022-12-23 | additive_7y | 6.55 | -5.17 | -5.17 |
| 105958 | TVA | 2022-12-23 | additive_k10 | 6.56 | 1.79 | 0.00 |
| 105957 | TVA | 2022-12-23 | additive_k8 | 7.27 | -4.86 | -4.86 |
| 105960 | TVA | 2022-12-23 | additive_lam | 6.61 | -5.25 | -5.25 |
| 105959 | TVA | 2022-12-23 | additive_val90 | 6.06 | -1.17 | -1.17 |
| 105956 | TVA | 2022-12-23 | boosting_7y | 12.62 | -14.77 | -14.77 |
| 105952 | TVA | 2022-12-23 | boosting_deep | 14.31 | -14.79 | -14.79 |
| 105954 | TVA | 2022-12-23 | boosting_l2 | 13.73 | -14.81 | -14.81 |
| 105955 | TVA | 2022-12-23 | boosting_refit3 | 12.83 | -14.05 | -14.05 |
| 105953 | TVA | 2022-12-23 | boosting_shallow | 13.62 | -15.06 | -15.06 |
| 105950 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 105951 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 105975 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 105974 | TVA | 2022-12-24 | additive_7y | 3.64 | -8.58 | -8.58 |
| 105971 | TVA | 2022-12-24 | additive_k10 | 4.47 | -8.67 | -8.67 |
| 105970 | TVA | 2022-12-24 | additive_k8 | 4.05 | -9.50 | -9.50 |
| 105973 | TVA | 2022-12-24 | additive_lam | 3.65 | -8.48 | -8.48 |
| 105972 | TVA | 2022-12-24 | additive_val90 | 3.52 | -8.50 | -8.50 |
| 105969 | TVA | 2022-12-24 | boosting_7y | 5.93 | -12.91 | -12.91 |
| 105965 | TVA | 2022-12-24 | boosting_deep | 6.09 | -11.84 | -11.84 |
| 105967 | TVA | 2022-12-24 | boosting_l2 | 5.95 | -12.24 | -12.24 |
| 105968 | TVA | 2022-12-24 | boosting_refit3 | 6.31 | -12.68 | -12.68 |
| 105966 | TVA | 2022-12-24 | boosting_shallow | 8.04 | -16.15 | -16.15 |
| 105963 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 105964 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_7y | BPAT | mape | 12.536 | 0.000 | 750 |
| additive_7y | CISO | mape | 17.794 | 0.000 | 737 |
| additive_7y | DUK | mape | 10.089 | 0.000 | 750 |
| additive_7y | ERCO | mape | 11.875 | 0.000 | 746 |
| additive_7y | FPL | mape | 17.264 | 0.000 | 690 |
| additive_7y | ISNE | mape | 21.048 | 0.000 | 752 |
| additive_7y | MISO | mape | -2.902 | 0.004 | 746 |
| additive_7y | NYIS | mape | 0.794 | 0.427 | 752 |
| additive_7y | PJM | mape | 5.949 | 0.000 | 744 |
| additive_7y | SWPP | mape | -14.449 | 0.000 | 745 |
| additive_7y | TVA | mape | 17.260 | 0.000 | 739 |
| additive_k10 | BPAT | mape | 11.369 | 0.000 | 750 |
| additive_k10 | CISO | mape | 17.876 | 0.000 | 737 |
| additive_k10 | DUK | mape | 10.383 | 0.000 | 750 |
| additive_k10 | ERCO | mape | 12.037 | 0.000 | 746 |
| additive_k10 | FPL | mape | 17.371 | 0.000 | 690 |
| additive_k10 | ISNE | mape | 21.202 | 0.000 | 752 |
| additive_k10 | MISO | mape | -2.660 | 0.008 | 746 |
| additive_k10 | NYIS | mape | 0.868 | 0.386 | 752 |
| additive_k10 | PJM | mape | 6.049 | 0.000 | 744 |
| additive_k10 | SWPP | mape | -14.169 | 0.000 | 745 |
| additive_k10 | TVA | mape | 17.573 | 0.000 | 739 |
| additive_k8 | BPAT | mape | 11.587 | 0.000 | 750 |
| additive_k8 | CISO | mape | 17.868 | 0.000 | 737 |
| additive_k8 | DUK | mape | 10.224 | 0.000 | 750 |
| additive_k8 | ERCO | mape | 12.089 | 0.000 | 746 |
| additive_k8 | FPL | mape | 17.302 | 0.000 | 690 |
| additive_k8 | ISNE | mape | 21.386 | 0.000 | 752 |
| additive_k8 | MISO | mape | -2.732 | 0.006 | 746 |
| additive_k8 | NYIS | mape | 0.889 | 0.374 | 752 |
| additive_k8 | PJM | mape | 6.075 | 0.000 | 744 |
| additive_k8 | SWPP | mape | -14.390 | 0.000 | 745 |
| additive_k8 | TVA | mape | 17.454 | 0.000 | 739 |
| additive_lam | BPAT | mape | 12.542 | 0.000 | 750 |
| additive_lam | CISO | mape | 17.955 | 0.000 | 737 |
| additive_lam | DUK | mape | 10.153 | 0.000 | 750 |
| additive_lam | ERCO | mape | 12.242 | 0.000 | 746 |
| additive_lam | FPL | mape | 17.251 | 0.000 | 690 |
| additive_lam | ISNE | mape | 21.187 | 0.000 | 752 |
| additive_lam | MISO | mape | -2.892 | 0.004 | 746 |
| additive_lam | NYIS | mape | 0.765 | 0.444 | 752 |
| additive_lam | PJM | mape | 6.145 | 0.000 | 744 |
| additive_lam | SWPP | mape | -14.201 | 0.000 | 745 |
| additive_lam | TVA | mape | 17.343 | 0.000 | 739 |
| additive_val90 | BPAT | mape | 12.956 | 0.000 | 750 |
| additive_val90 | CISO | mape | 18.040 | 0.000 | 737 |
| additive_val90 | DUK | mape | 10.191 | 0.000 | 750 |
| additive_val90 | ERCO | mape | 11.950 | 0.000 | 746 |
| additive_val90 | FPL | mape | 17.312 | 0.000 | 690 |
| additive_val90 | ISNE | mape | 21.273 | 0.000 | 752 |
| additive_val90 | MISO | mape | -2.804 | 0.005 | 746 |
| additive_val90 | NYIS | mape | 0.919 | 0.358 | 752 |
| additive_val90 | PJM | mape | 6.067 | 0.000 | 744 |
| additive_val90 | SWPP | mape | -14.282 | 0.000 | 745 |
| additive_val90 | TVA | mape | 17.413 | 0.000 | 739 |
| boosting_7y | BPAT | mape | 12.593 | 0.000 | 750 |
| boosting_7y | CISO | mape | 9.591 | 0.000 | 737 |
| boosting_7y | DUK | mape | 10.150 | 0.000 | 750 |
| boosting_7y | ERCO | mape | 6.726 | 0.000 | 746 |
| boosting_7y | FPL | mape | 20.845 | 0.000 | 690 |
| boosting_7y | ISNE | mape | 18.667 | 0.000 | 752 |
| boosting_7y | MISO | mape | -3.535 | 0.000 | 746 |
| boosting_7y | NYIS | mape | 0.423 | 0.672 | 752 |
| boosting_7y | PJM | mape | 6.187 | 0.000 | 744 |
| boosting_7y | SWPP | mape | -11.927 | 0.000 | 745 |
| boosting_7y | TVA | mape | 16.245 | 0.000 | 739 |
| boosting_deep | BPAT | mape | 11.802 | 0.000 | 750 |
| boosting_deep | CISO | mape | 8.339 | 0.000 | 737 |
| boosting_deep | DUK | mape | 9.444 | 0.000 | 750 |
| boosting_deep | ERCO | mape | 5.856 | 0.000 | 746 |
| boosting_deep | FPL | mape | 21.155 | 0.000 | 690 |
| boosting_deep | ISNE | mape | 18.019 | 0.000 | 752 |
| boosting_deep | MISO | mape | -4.086 | 0.000 | 746 |
| boosting_deep | NYIS | mape | -0.251 | 0.802 | 752 |
| boosting_deep | PJM | mape | 5.707 | 0.000 | 744 |
| boosting_deep | SWPP | mape | -12.387 | 0.000 | 745 |
| boosting_deep | TVA | mape | 15.836 | 0.000 | 739 |
| boosting_l2 | BPAT | mape | 12.492 | 0.000 | 750 |
| boosting_l2 | CISO | mape | 9.316 | 0.000 | 737 |
| boosting_l2 | DUK | mape | 10.128 | 0.000 | 750 |
| boosting_l2 | ERCO | mape | 6.489 | 0.000 | 746 |
| boosting_l2 | FPL | mape | 20.899 | 0.000 | 690 |
| boosting_l2 | ISNE | mape | 18.981 | 0.000 | 752 |
| boosting_l2 | MISO | mape | -3.622 | 0.000 | 746 |
| boosting_l2 | NYIS | mape | 0.408 | 0.683 | 752 |
| boosting_l2 | PJM | mape | 6.273 | 0.000 | 744 |
| boosting_l2 | SWPP | mape | -11.939 | 0.000 | 745 |
| boosting_l2 | TVA | mape | 16.348 | 0.000 | 739 |
| boosting_refit3 | BPAT | mape | 11.923 | 0.000 | 750 |
| boosting_refit3 | CISO | mape | 9.495 | 0.000 | 737 |
| boosting_refit3 | DUK | mape | 9.418 | 0.000 | 750 |
| boosting_refit3 | ERCO | mape | 6.141 | 0.000 | 746 |
| boosting_refit3 | FPL | mape | 20.831 | 0.000 | 690 |
| boosting_refit3 | ISNE | mape | 19.047 | 0.000 | 752 |
| boosting_refit3 | MISO | mape | -3.673 | 0.000 | 746 |
| boosting_refit3 | NYIS | mape | 0.991 | 0.322 | 752 |
| boosting_refit3 | PJM | mape | 6.235 | 0.000 | 744 |
| boosting_refit3 | SWPP | mape | -13.442 | 0.000 | 745 |
| boosting_refit3 | TVA | mape | 15.771 | 0.000 | 739 |
| boosting_shallow | BPAT | mape | 12.955 | 0.000 | 750 |
| boosting_shallow | CISO | mape | 11.443 | 0.000 | 737 |
| boosting_shallow | DUK | mape | 11.676 | 0.000 | 750 |
| boosting_shallow | ERCO | mape | 9.776 | 0.000 | 746 |
| boosting_shallow | FPL | mape | 21.799 | 0.000 | 690 |
| boosting_shallow | ISNE | mape | 20.823 | 0.000 | 752 |
| boosting_shallow | MISO | mape | -2.598 | 0.009 | 746 |
| boosting_shallow | NYIS | mape | 3.130 | 0.002 | 752 |
| boosting_shallow | PJM | mape | 7.309 | 0.000 | 744 |
| boosting_shallow | SWPP | mape | -11.142 | 0.000 | 745 |
| boosting_shallow | TVA | mape | 18.479 | 0.000 | 739 |
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

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| additive_7y | 0.976 |
| additive_k10 | 0.976 |
| additive_k8 | 0.976 |
| additive_lam | 0.976 |
| additive_val90 | 0.976 |
| boosting_7y | 0.987 |
| boosting_deep | 0.987 |
| boosting_l2 | 0.987 |
| boosting_refit3 | 0.987 |
| boosting_shallow | 0.987 |
| final_additive | 0.976 |
| final_boosting | 0.987 |
