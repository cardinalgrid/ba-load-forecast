# Phase E: regime-conditional errors with an adaptive level

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `ens_bc_regime` reads the 5th and 95th percentiles of the corrected ensemble's errors on the known days of the same temperature regime over the last year; `ens_bc_adaptive` reads them on the last 120 days at a level that adapts to the coverage achieved (adaptive conformal inference); `ens_bc_regime_aci` combines the two (regime pool, one adaptive level); `ens_bc_regime_aci2` tracks one adaptive level per regime.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_bc_regime | 2.58 | 2.25 | -0.81 | -1.86 | 1.32 | 0.60 | 0.28 | -49.03 | 8163 | 11.00 |
| ens_bc_regime_aci | 2.58 | 2.25 | -0.81 | -1.86 | 1.32 | 0.60 | 0.28 | -49.03 | 8163 | 11.00 |
| ens_bc_regime_aci2 | 2.58 | 2.25 | -0.81 | -1.86 | 1.32 | 0.60 | 0.28 | -49.03 | 8163 | 11.00 |
| ens_bc_adaptive | 2.74 | 2.40 | -0.81 | -1.91 | 1.38 | 0.57 | 0.29 | -49.77 | 8163 | 11.00 |
| ens_recent | 2.88 | 2.52 | -1.24 | -2.20 | 1.29 | 0.55 | 0.27 | -53.35 | 8163 | 11.00 |
| boosting_ml | 3.03 | 2.67 | -1.02 | -2.14 | 1.50 | 0.52 | 0.28 | -52.25 | 8163 | 11.00 |
| DF | 3.04 | 2.74 | 0.09 | -1.26 | 1.08 | 0.00 | 0.00 | -53.60 | 8163 | 11.00 |
| additive_ml_special | 3.14 | 2.77 | -1.49 | -2.48 | 1.41 | 0.50 | 0.26 | -54.20 | 8163 | 11.00 |

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
| additive_ml_special | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| additive_ml_special | CISO | 3.86 | 3.50 | -3.12 | -3.96 | 0.37 | -18.80 | 0.29 | 0.14 | 737 | 25196.91 |
| additive_ml_special | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| additive_ml_special | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
| additive_ml_special | FPL | 6.20 | 5.63 | -6.55 | -7.12 | 1.15 | -54.20 | 0.29 | 0.28 | 700 | 15274.07 |
| additive_ml_special | ISNE | 4.22 | 3.71 | -1.60 | -2.79 | 0.53 | -22.39 | 0.17 | 0.15 | 752 | 13392.81 |
| additive_ml_special | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_ml_special | NYIS | 2.72 | 2.37 | -0.86 | -2.08 | 0.60 | -15.67 | 0.51 | 0.60 | 752 | 17400.75 |
| additive_ml_special | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.75 | 0.51 | 744 | 91927.69 |
| additive_ml_special | SWPP | 2.61 | 2.11 | -0.25 | -1.59 | 1.54 | -20.36 | 0.70 | 0.10 | 747 | 31342.11 |
| additive_ml_special | TVA | 3.35 | 2.97 | -1.05 | -2.35 | 1.42 | -14.12 | 0.25 | 0.26 | 739 | 18562.62 |
| boosting_ml | BPAT | 2.73 | 2.43 | -0.43 | -1.57 | 2.00 | -18.16 | 0.27 | 0.24 | 750 | 6533.15 |
| boosting_ml | CISO | 3.11 | 2.78 | -2.24 | -2.82 | 0.49 | -18.95 | 0.41 | 0.17 | 737 | 25196.91 |
| boosting_ml | DUK | 3.58 | 3.12 | -0.42 | -2.27 | 1.50 | -16.82 | 0.33 | 0.27 | 750 | 12129.97 |
| boosting_ml | ERCO | 3.13 | 2.72 | -2.27 | -2.98 | 1.29 | -15.00 | 0.35 | 0.18 | 746 | 46782.53 |
| boosting_ml | FPL | 6.29 | 5.93 | -6.96 | -7.30 | 1.39 | -52.25 | 0.20 | 0.27 | 700 | 15274.07 |
| boosting_ml | ISNE | 3.93 | 3.56 | -1.18 | -2.30 | 0.63 | -21.45 | 0.22 | 0.16 | 752 | 13392.81 |
| boosting_ml | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| boosting_ml | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.74 | -14.02 | 0.51 | 0.66 | 752 | 17400.75 |
| boosting_ml | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.75 | 0.57 | 744 | 91927.69 |
| boosting_ml | SWPP | 2.73 | 2.19 | -0.89 | -1.99 | 1.69 | -28.44 | 0.68 | 0.08 | 747 | 31342.11 |
| boosting_ml | TVA | 3.28 | 2.85 | -0.22 | -1.84 | 1.54 | -15.24 | 0.24 | 0.30 | 739 | 18562.62 |
| ens_bc_adaptive | BPAT | 2.58 | 2.29 | -1.14 | -1.96 | 1.91 | -19.43 | 0.35 | 0.21 | 750 | 6533.15 |
| ens_bc_adaptive | CISO | 2.96 | 2.63 | -0.52 | -2.00 | 0.36 | -16.77 | 0.43 | 0.23 | 737 | 25196.91 |
| ens_bc_adaptive | DUK | 3.40 | 3.11 | -1.07 | -2.53 | 1.49 | -15.96 | 0.36 | 0.27 | 750 | 12129.97 |
| ens_bc_adaptive | ERCO | 2.93 | 2.50 | -1.05 | -2.14 | 1.16 | -14.76 | 0.40 | 0.22 | 746 | 46782.53 |
| ens_bc_adaptive | FPL | 4.14 | 3.67 | -2.30 | -3.70 | 1.16 | -49.77 | 0.52 | 0.57 | 700 | 15274.07 |
| ens_bc_adaptive | ISNE | 3.84 | 3.46 | -0.75 | -2.12 | 0.51 | -22.94 | 0.24 | 0.16 | 752 | 13392.81 |
| ens_bc_adaptive | MISO | 2.20 | 1.89 | -0.61 | -1.43 | 1.61 | -8.52 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_bc_adaptive | NYIS | 2.48 | 2.12 | -0.62 | -1.70 | 0.59 | -14.78 | 0.55 | 0.66 | 752 | 17400.75 |
| ens_bc_adaptive | PJM | 2.59 | 2.36 | -0.61 | -1.73 | 1.73 | -12.31 | 0.78 | 0.52 | 744 | 91927.69 |
| ens_bc_adaptive | SWPP | 2.52 | 2.08 | -0.79 | -1.82 | 1.61 | -21.32 | 0.71 | 0.09 | 747 | 31342.11 |
| ens_bc_adaptive | TVA | 3.10 | 2.69 | -1.05 | -2.31 | 1.58 | -13.65 | 0.30 | 0.26 | 739 | 18562.62 |
| ens_bc_regime | BPAT | 2.52 | 2.20 | -1.00 | -1.87 | 1.87 | -18.57 | 0.37 | 0.22 | 750 | 6533.15 |
| ens_bc_regime | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime | DUK | 3.31 | 2.95 | -1.14 | -2.53 | 1.35 | -16.31 | 0.40 | 0.27 | 750 | 12129.97 |
| ens_bc_regime | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| ens_bc_regime | ISNE | 3.74 | 3.31 | -0.51 | -1.95 | 0.50 | -21.57 | 0.26 | 0.16 | 752 | 13392.81 |
| ens_bc_regime | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime | NYIS | 2.45 | 2.05 | -0.52 | -1.67 | 0.55 | -13.12 | 0.58 | 0.66 | 752 | 17400.75 |
| ens_bc_regime | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_bc_regime | SWPP | 2.42 | 1.94 | -0.75 | -1.74 | 1.53 | -21.32 | 0.72 | 0.09 | 747 | 31342.11 |
| ens_bc_regime | TVA | 3.04 | 2.63 | -0.72 | -2.10 | 1.51 | -15.93 | 0.28 | 0.26 | 739 | 18562.62 |
| ens_bc_regime_aci | BPAT | 2.52 | 2.20 | -1.00 | -1.87 | 1.87 | -18.57 | 0.37 | 0.22 | 750 | 6533.15 |
| ens_bc_regime_aci | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime_aci | DUK | 3.31 | 2.95 | -1.14 | -2.53 | 1.35 | -16.31 | 0.40 | 0.27 | 750 | 12129.97 |
| ens_bc_regime_aci | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime_aci | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| ens_bc_regime_aci | ISNE | 3.74 | 3.31 | -0.51 | -1.95 | 0.50 | -21.57 | 0.26 | 0.16 | 752 | 13392.81 |
| ens_bc_regime_aci | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime_aci | NYIS | 2.45 | 2.05 | -0.52 | -1.67 | 0.55 | -13.12 | 0.58 | 0.66 | 752 | 17400.75 |
| ens_bc_regime_aci | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_bc_regime_aci | SWPP | 2.42 | 1.94 | -0.75 | -1.74 | 1.53 | -21.32 | 0.72 | 0.09 | 747 | 31342.11 |
| ens_bc_regime_aci | TVA | 3.04 | 2.63 | -0.72 | -2.10 | 1.51 | -15.93 | 0.28 | 0.26 | 739 | 18562.62 |
| ens_bc_regime_aci2 | BPAT | 2.52 | 2.20 | -1.00 | -1.87 | 1.87 | -18.57 | 0.37 | 0.22 | 750 | 6533.15 |
| ens_bc_regime_aci2 | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime_aci2 | DUK | 3.31 | 2.95 | -1.14 | -2.53 | 1.35 | -16.31 | 0.40 | 0.27 | 750 | 12129.97 |
| ens_bc_regime_aci2 | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime_aci2 | FPL | 3.91 | 3.46 | -2.53 | -3.79 | 1.18 | -49.03 | 0.57 | 0.56 | 700 | 15274.07 |
| ens_bc_regime_aci2 | ISNE | 3.74 | 3.31 | -0.51 | -1.95 | 0.50 | -21.57 | 0.26 | 0.16 | 752 | 13392.81 |
| ens_bc_regime_aci2 | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime_aci2 | NYIS | 2.45 | 2.05 | -0.52 | -1.67 | 0.55 | -13.12 | 0.58 | 0.66 | 752 | 17400.75 |
| ens_bc_regime_aci2 | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_bc_regime_aci2 | SWPP | 2.42 | 1.94 | -0.75 | -1.74 | 1.53 | -21.32 | 0.72 | 0.09 | 747 | 31342.11 |
| ens_bc_regime_aci2 | TVA | 3.04 | 2.63 | -0.72 | -2.10 | 1.51 | -15.93 | 0.28 | 0.26 | 739 | 18562.62 |
| ens_recent | BPAT | 2.59 | 2.27 | -0.66 | -1.61 | 1.83 | -18.29 | 0.32 | 0.23 | 750 | 6533.15 |
| ens_recent | CISO | 3.16 | 2.78 | -2.58 | -3.21 | 0.39 | -18.88 | 0.42 | 0.15 | 737 | 25196.91 |
| ens_recent | DUK | 3.43 | 2.97 | -0.56 | -2.26 | 1.33 | -15.64 | 0.37 | 0.27 | 750 | 12129.97 |
| ens_recent | ERCO | 3.13 | 2.70 | -2.25 | -2.89 | 1.07 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| ens_recent | FPL | 6.05 | 5.68 | -6.70 | -7.08 | 1.17 | -53.35 | 0.26 | 0.27 | 700 | 15274.07 |
| ens_recent | ISNE | 3.83 | 3.46 | -1.36 | -2.42 | 0.52 | -21.88 | 0.22 | 0.14 | 752 | 13392.81 |
| ens_recent | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_recent | NYIS | 2.49 | 2.14 | -0.64 | -1.71 | 0.56 | -13.90 | 0.56 | 0.65 | 752 | 17400.75 |
| ens_recent | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.79 | 0.55 | 744 | 91927.69 |
| ens_recent | SWPP | 2.51 | 1.99 | -0.56 | -1.70 | 1.51 | -21.47 | 0.71 | 0.09 | 747 | 31342.11 |
| ens_recent | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |

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
| additive_ml_special | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| additive_ml_special | CISO | uri | 2.30 | 1.97 | 0.00 | 0.00 | 6 |
| additive_ml_special | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| additive_ml_special | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| additive_ml_special | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| additive_ml_special | ISNE | uri | 3.16 | 0.95 | -0.46 | -2.03 | 6 |
| additive_ml_special | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| additive_ml_special | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| additive_ml_special | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_ml_special | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_ml_special | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| boosting_ml | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| boosting_ml | CISO | uri | 1.94 | -1.22 | -1.32 | -3.36 | 6 |
| boosting_ml | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_ml | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| boosting_ml | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| boosting_ml | ISNE | uri | 3.45 | 1.14 | -0.75 | -3.08 | 6 |
| boosting_ml | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_ml | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| boosting_ml | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_ml | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_ml | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| ens_bc_adaptive | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| ens_bc_adaptive | CISO | uri | 1.96 | -0.77 | -1.09 | -2.59 | 6 |
| ens_bc_adaptive | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| ens_bc_adaptive | ERCO | uri | 6.75 | -9.60 | -9.60 | -9.98 | 2 |
| ens_bc_adaptive | FPL | uri | 10.00 | -11.78 | -11.78 | -14.33 | 6 |
| ens_bc_adaptive | ISNE | uri | 3.06 | 1.67 | -0.35 | -2.09 | 6 |
| ens_bc_adaptive | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_adaptive | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| ens_bc_adaptive | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_adaptive | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| ens_bc_adaptive | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
| ens_bc_regime | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| ens_bc_regime | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| ens_bc_regime | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| ens_bc_regime | ISNE | uri | 3.06 | 1.67 | -0.35 | -2.09 | 6 |
| ens_bc_regime | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| ens_bc_regime | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| ens_bc_regime | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
| ens_bc_regime_aci | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| ens_bc_regime_aci | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime_aci | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| ens_bc_regime_aci | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime_aci | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| ens_bc_regime_aci | ISNE | uri | 3.06 | 1.67 | -0.35 | -2.09 | 6 |
| ens_bc_regime_aci | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime_aci | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| ens_bc_regime_aci | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime_aci | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| ens_bc_regime_aci | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
| ens_bc_regime_aci2 | BPAT | uri | 2.75 | -1.34 | -1.60 | -5.19 | 6 |
| ens_bc_regime_aci2 | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime_aci2 | DUK | uri | 3.41 | -2.74 | -2.75 | -5.53 | 6 |
| ens_bc_regime_aci2 | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime_aci2 | FPL | uri | 8.60 | -9.96 | -9.96 | -11.99 | 6 |
| ens_bc_regime_aci2 | ISNE | uri | 3.06 | 1.67 | -0.35 | -2.09 | 6 |
| ens_bc_regime_aci2 | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime_aci2 | NYIS | uri | 1.97 | 1.43 | -0.25 | -1.49 | 6 |
| ens_bc_regime_aci2 | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime_aci2 | SWPP | uri | 6.15 | 0.41 | -2.72 | -6.47 | 4 |
| ens_bc_regime_aci2 | TVA | uri | 2.89 | -2.67 | -3.16 | -5.91 | 6 |
| ens_recent | BPAT | uri | 2.95 | 0.23 | -0.68 | -3.44 | 6 |
| ens_recent | CISO | uri | 1.78 | 0.44 | -0.28 | -1.40 | 6 |
| ens_recent | DUK | uri | 3.42 | -2.79 | -2.79 | -6.10 | 6 |
| ens_recent | ERCO | uri | 6.28 | -9.24 | -9.24 | -9.46 | 2 |
| ens_recent | FPL | uri | 9.92 | -12.91 | -12.91 | -15.50 | 6 |
| ens_recent | ISNE | uri | 3.16 | 1.04 | -0.49 | -2.53 | 6 |
| ens_recent | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| ens_recent | NYIS | uri | 2.11 | 1.50 | -0.23 | -1.35 | 6 |
| ens_recent | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| ens_recent | SWPP | uri | 6.08 | -0.39 | -2.96 | -6.25 | 4 |
| ens_recent | TVA | uri | 2.71 | -1.06 | -1.72 | -3.36 | 6 |
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
| additive_ml_special | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| additive_ml_special | CISO | elliott | 3.89 | 2.67 | -0.55 | -2.75 | 5 |
| additive_ml_special | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| additive_ml_special | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| additive_ml_special | FPL | elliott | 11.83 | -1.71 | -7.55 | -19.18 | 5 |
| additive_ml_special | ISNE | elliott | 4.53 | 0.92 | -0.90 | -3.30 | 5 |
| additive_ml_special | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| additive_ml_special | NYIS | elliott | 3.27 | -1.91 | -2.37 | -3.71 | 5 |
| additive_ml_special | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| additive_ml_special | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| additive_ml_special | TVA | elliott | 7.91 | 5.47 | 0.00 | 0.00 | 3 |
| boosting_ml | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| boosting_ml | CISO | elliott | 3.66 | 1.13 | -0.69 | -3.11 | 5 |
| boosting_ml | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| boosting_ml | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| boosting_ml | FPL | elliott | 9.68 | -16.11 | -16.11 | -23.65 | 5 |
| boosting_ml | ISNE | elliott | 3.61 | 2.38 | -0.33 | -1.12 | 5 |
| boosting_ml | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| boosting_ml | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| boosting_ml | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| boosting_ml | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| boosting_ml | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |
| ens_bc_adaptive | BPAT | elliott | 4.42 | -4.31 | -4.56 | -9.04 | 5 |
| ens_bc_adaptive | CISO | elliott | 4.09 | 2.82 | -0.44 | -2.20 | 5 |
| ens_bc_adaptive | DUK | elliott | 3.54 | -2.63 | -2.63 | -4.59 | 4 |
| ens_bc_adaptive | ERCO | elliott | 6.93 | -2.86 | -4.49 | -11.30 | 5 |
| ens_bc_adaptive | FPL | elliott | 5.96 | -3.28 | -4.98 | -8.68 | 5 |
| ens_bc_adaptive | ISNE | elliott | 3.83 | 2.52 | -0.27 | -1.14 | 5 |
| ens_bc_adaptive | MISO | elliott | 3.58 | -1.17 | -2.16 | -4.06 | 5 |
| ens_bc_adaptive | NYIS | elliott | 2.62 | 0.48 | -0.63 | -2.04 | 5 |
| ens_bc_adaptive | PJM | elliott | 4.36 | -1.15 | -2.39 | -5.75 | 5 |
| ens_bc_adaptive | SWPP | elliott | 4.16 | -1.94 | -3.11 | -7.24 | 5 |
| ens_bc_adaptive | TVA | elliott | 6.51 | 2.43 | -0.53 | -0.88 | 3 |
| ens_bc_regime | BPAT | elliott | 4.33 | -3.84 | -4.19 | -8.42 | 5 |
| ens_bc_regime | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime | DUK | elliott | 3.38 | -3.22 | -3.22 | -5.20 | 4 |
| ens_bc_regime | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| ens_bc_regime | ISNE | elliott | 3.65 | 0.91 | -0.90 | -2.60 | 5 |
| ens_bc_regime | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime | NYIS | elliott | 2.77 | -0.78 | -1.63 | -3.23 | 5 |
| ens_bc_regime | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_bc_regime | SWPP | elliott | 4.17 | -1.47 | -2.82 | -6.59 | 5 |
| ens_bc_regime | TVA | elliott | 6.17 | 1.48 | -0.79 | -1.40 | 3 |
| ens_bc_regime_aci | BPAT | elliott | 4.33 | -3.84 | -4.19 | -8.42 | 5 |
| ens_bc_regime_aci | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime_aci | DUK | elliott | 3.38 | -3.22 | -3.22 | -5.20 | 4 |
| ens_bc_regime_aci | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime_aci | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| ens_bc_regime_aci | ISNE | elliott | 3.65 | 0.91 | -0.90 | -2.60 | 5 |
| ens_bc_regime_aci | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime_aci | NYIS | elliott | 2.77 | -0.78 | -1.63 | -3.23 | 5 |
| ens_bc_regime_aci | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_bc_regime_aci | SWPP | elliott | 4.17 | -1.47 | -2.82 | -6.59 | 5 |
| ens_bc_regime_aci | TVA | elliott | 6.17 | 1.48 | -0.79 | -1.40 | 3 |
| ens_bc_regime_aci2 | BPAT | elliott | 4.33 | -3.84 | -4.19 | -8.42 | 5 |
| ens_bc_regime_aci2 | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime_aci2 | DUK | elliott | 3.38 | -3.22 | -3.22 | -5.20 | 4 |
| ens_bc_regime_aci2 | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime_aci2 | FPL | elliott | 8.02 | -9.31 | -9.55 | -14.82 | 5 |
| ens_bc_regime_aci2 | ISNE | elliott | 3.65 | 0.91 | -0.90 | -2.60 | 5 |
| ens_bc_regime_aci2 | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime_aci2 | NYIS | elliott | 2.77 | -0.78 | -1.63 | -3.23 | 5 |
| ens_bc_regime_aci2 | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_bc_regime_aci2 | SWPP | elliott | 4.17 | -1.47 | -2.82 | -6.59 | 5 |
| ens_bc_regime_aci2 | TVA | elliott | 6.17 | 1.48 | -0.79 | -1.40 | 3 |
| ens_recent | BPAT | elliott | 4.21 | -3.47 | -3.90 | -8.35 | 5 |
| ens_recent | CISO | elliott | 3.27 | 1.77 | -0.59 | -2.96 | 5 |
| ens_recent | DUK | elliott | 3.71 | -3.00 | -3.00 | -3.88 | 4 |
| ens_recent | ERCO | elliott | 6.73 | -4.28 | -5.36 | -12.60 | 5 |
| ens_recent | FPL | elliott | 8.81 | -10.29 | -10.53 | -14.82 | 5 |
| ens_recent | ISNE | elliott | 3.77 | 1.69 | -0.60 | -1.85 | 5 |
| ens_recent | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| ens_recent | NYIS | elliott | 2.73 | -1.04 | -1.83 | -3.53 | 5 |
| ens_recent | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| ens_recent | SWPP | elliott | 4.12 | -2.20 | -3.22 | -7.26 | 5 |
| ens_recent | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | DF | eve | 3.47 | 0.40 | -1.41 |  | 268 |
| 12 | ens_bc_regime | eve | 3.56 | 0.34 | -1.77 | 0.47 | 268 |
| 13 | ens_bc_regime_aci | eve | 3.56 | 0.34 | -1.77 | 0.47 | 268 |
| 14 | ens_bc_regime_aci2 | eve | 3.56 | 0.34 | -1.77 | 0.47 | 268 |
| 15 | ens_recent | eve | 3.66 | -0.17 | -2.07 | 0.47 | 268 |
| 11 | ens_bc_adaptive | eve | 3.72 | 0.64 | -1.64 | 0.43 | 268 |
| 9 | additive_ml_special | eve | 3.87 | -0.26 | -2.27 | 0.43 | 268 |
| 10 | boosting_ml | eve | 3.89 | -0.08 | -2.13 | 0.42 | 268 |
| 4 | ens_bc_regime | special | 3.43 | -1.33 | -2.53 | 0.52 | 270 |
| 5 | ens_bc_regime_aci | special | 3.43 | -1.33 | -2.53 | 0.52 | 270 |
| 6 | ens_bc_regime_aci2 | special | 3.43 | -1.33 | -2.53 | 0.52 | 270 |
| 3 | ens_bc_adaptive | special | 3.61 | -1.08 | -2.46 | 0.51 | 270 |
| 7 | ens_recent | special | 3.64 | -1.80 | -2.94 | 0.52 | 270 |
| 0 | DF | special | 3.80 | -0.17 | -1.78 |  | 270 |
| 1 | additive_ml_special | special | 3.88 | -1.97 | -3.18 | 0.47 | 270 |
| 2 | boosting_ml | special | 3.95 | -1.61 | -2.93 | 0.43 | 270 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_bc_adaptive | all | 0.426 | 1.491 | 0.427 | 0.897 | 12.925 | 0.890 | 7933 |
| ens_bc_regime | all | 0.408 | 1.425 | 0.413 | 0.869 | 11.175 | 0.860 | 7921 |
| ens_bc_regime_aci | all | 0.412 | 1.425 | 0.413 | 0.898 | 12.554 | 0.891 | 7921 |
| ens_bc_regime_aci2 | all | 0.408 | 1.425 | 0.416 | 0.895 | 12.410 | 0.888 | 7921 |
| ens_bc_adaptive | events | 0.547 | 2.055 | 0.622 | 0.777 | 12.696 | 0.793 | 111 |
| ens_bc_regime | events | 0.531 | 1.933 | 0.639 | 0.734 | 10.840 | 0.738 | 107 |
| ens_bc_regime_aci | events | 0.513 | 1.933 | 0.624 | 0.766 | 11.907 | 0.757 | 107 |
| ens_bc_regime_aci2 | events | 0.503 | 1.933 | 0.626 | 0.770 | 12.000 | 0.785 | 107 |
| ens_bc_adaptive | cold_mornings | 0.498 | 1.793 | 0.538 | 0.814 | 12.453 | 0.782 | 330 |
| ens_bc_regime | cold_mornings | 0.492 | 1.730 | 0.546 | 0.781 | 11.256 | 0.750 | 324 |
| ens_bc_regime_aci | cold_mornings | 0.472 | 1.730 | 0.531 | 0.811 | 12.176 | 0.775 | 324 |
| ens_bc_regime_aci2 | cold_mornings | 0.459 | 1.730 | 0.536 | 0.809 | 12.130 | 0.778 | 324 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 17847 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 17840 | DUK | 2022-12-24 | additive_ml_special | 7.26 | -12.67 | -12.67 |
| 17841 | DUK | 2022-12-24 | boosting_ml | 9.36 | -15.80 | -15.80 |
| 17844 | DUK | 2022-12-24 | ens_bc_adaptive | 8.40 | -12.59 | -12.59 |
| 17843 | DUK | 2022-12-24 | ens_bc_regime | 9.09 | -14.17 | -14.17 |
| 17845 | DUK | 2022-12-24 | ens_bc_regime_aci | 9.09 | -14.17 | -14.17 |
| 17846 | DUK | 2022-12-24 | ens_bc_regime_aci2 | 9.09 | -14.17 | -14.17 |
| 17842 | DUK | 2022-12-24 | ens_recent | 8.26 | -14.16 | -14.16 |
| 18503 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 18496 | ERCO | 2021-02-15 | additive_ml_special | 41.72 | -4.24 | -4.24 |
| 18497 | ERCO | 2021-02-15 | boosting_ml | 27.39 | -16.57 | -16.57 |
| 18500 | ERCO | 2021-02-15 | ens_bc_adaptive | 33.89 | -10.66 | -10.66 |
| 18499 | ERCO | 2021-02-15 | ens_bc_regime | 33.61 | -10.86 | -10.86 |
| 18501 | ERCO | 2021-02-15 | ens_bc_regime_aci | 33.61 | -10.86 | -10.86 |
| 18502 | ERCO | 2021-02-15 | ens_bc_regime_aci2 | 33.61 | -10.86 | -10.86 |
| 18498 | ERCO | 2021-02-15 | ens_recent | 34.57 | -10.39 | -10.39 |
| 18511 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 18504 | ERCO | 2021-02-16 | additive_ml_special | 47.08 | 43.33 | 0.00 |
| 18505 | ERCO | 2021-02-16 | boosting_ml | 33.46 | 31.10 | 0.00 |
| 18508 | ERCO | 2021-02-16 | ens_bc_adaptive | 39.79 | 37.44 | 0.00 |
| 18507 | ERCO | 2021-02-16 | ens_bc_regime | 39.49 | 37.58 | 0.00 |
| 18509 | ERCO | 2021-02-16 | ens_bc_regime_aci | 39.49 | 37.58 | 0.00 |
| 18510 | ERCO | 2021-02-16 | ens_bc_regime_aci2 | 39.49 | 37.58 | 0.00 |
| 18506 | ERCO | 2021-02-16 | ens_recent | 40.43 | 37.36 | 0.00 |
| 18519 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 18512 | ERCO | 2021-02-17 | additive_ml_special | 31.74 | 29.84 | 0.00 |
| 18513 | ERCO | 2021-02-17 | boosting_ml | 28.91 | 24.01 | 0.00 |
| 18516 | ERCO | 2021-02-17 | ens_bc_adaptive | 29.65 | 24.44 | 0.00 |
| 18515 | ERCO | 2021-02-17 | ens_bc_regime | 29.39 | 23.92 | 0.00 |
| 18517 | ERCO | 2021-02-17 | ens_bc_regime_aci | 29.39 | 23.92 | 0.00 |
| 18518 | ERCO | 2021-02-17 | ens_bc_regime_aci2 | 29.39 | 23.92 | 0.00 |
| 18514 | ERCO | 2021-02-17 | ens_recent | 30.28 | 26.83 | 0.00 |
| 18527 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 18520 | ERCO | 2021-02-18 | additive_ml_special | 13.46 | 12.91 | 0.00 |
| 18521 | ERCO | 2021-02-18 | boosting_ml | 3.58 | -2.96 | -2.96 |
| 18524 | ERCO | 2021-02-18 | ens_bc_adaptive | 7.10 | 4.76 | 0.00 |
| 18523 | ERCO | 2021-02-18 | ens_bc_regime | 6.89 | 4.76 | 0.00 |
| 18525 | ERCO | 2021-02-18 | ens_bc_regime_aci | 6.89 | 4.76 | 0.00 |
| 18526 | ERCO | 2021-02-18 | ens_bc_regime_aci2 | 6.89 | 4.76 | 0.00 |
| 18522 | ERCO | 2021-02-18 | ens_recent | 7.68 | 4.44 | 0.00 |
| 36127 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 36120 | MISO | 2021-02-16 | additive_ml_special | 2.38 | 1.99 | 0.00 |
| 36121 | MISO | 2021-02-16 | boosting_ml | 2.11 | 0.99 | 0.00 |
| 36124 | MISO | 2021-02-16 | ens_bc_adaptive | 2.07 | 1.67 | 0.00 |
| 36123 | MISO | 2021-02-16 | ens_bc_regime | 2.07 | 1.67 | 0.00 |
| 36125 | MISO | 2021-02-16 | ens_bc_regime_aci | 2.07 | 1.67 | 0.00 |
| 36126 | MISO | 2021-02-16 | ens_bc_regime_aci2 | 2.07 | 1.67 | 0.00 |
| 36122 | MISO | 2021-02-16 | ens_recent | 2.17 | 1.51 | 0.00 |
| 54063 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 54056 | SWPP | 2021-02-15 | additive_ml_special | 2.66 | 1.09 | 0.00 |
| 54057 | SWPP | 2021-02-15 | boosting_ml | 5.58 | -7.79 | -7.79 |
| 54060 | SWPP | 2021-02-15 | ens_bc_adaptive | 2.08 | -2.08 | -2.08 |
| 54059 | SWPP | 2021-02-15 | ens_bc_regime | 2.08 | -2.08 | -2.08 |
| 54061 | SWPP | 2021-02-15 | ens_bc_regime_aci | 2.08 | -2.08 | -2.08 |
| 54062 | SWPP | 2021-02-15 | ens_bc_regime_aci2 | 2.08 | -2.08 | -2.08 |
| 54058 | SWPP | 2021-02-15 | ens_recent | 2.21 | -3.25 | -3.25 |
| 54071 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 54064 | SWPP | 2021-02-16 | additive_ml_special | 8.09 | 3.29 | 0.00 |
| 54065 | SWPP | 2021-02-16 | boosting_ml | 3.72 | -6.44 | -6.44 |
| 54068 | SWPP | 2021-02-16 | ens_bc_adaptive | 5.52 | -1.24 | -1.24 |
| 54067 | SWPP | 2021-02-16 | ens_bc_regime | 5.52 | -1.24 | -1.24 |
| 54069 | SWPP | 2021-02-16 | ens_bc_regime_aci | 5.52 | -1.24 | -1.24 |
| 54070 | SWPP | 2021-02-16 | ens_bc_regime_aci2 | 5.52 | -1.24 | -1.24 |
| 54066 | SWPP | 2021-02-16 | ens_recent | 5.49 | -1.39 | -1.39 |
| 65319 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 65312 | TVA | 2022-12-23 | additive_ml_special | 6.61 | -5.25 | -5.25 |
| 65313 | TVA | 2022-12-23 | boosting_ml | 13.98 | -15.00 | -15.00 |
| 65316 | TVA | 2022-12-23 | ens_bc_adaptive | 10.24 | -10.83 | -10.83 |
| 65315 | TVA | 2022-12-23 | ens_bc_regime | 10.85 | -12.10 | -12.10 |
| 65317 | TVA | 2022-12-23 | ens_bc_regime_aci | 10.85 | -12.10 | -12.10 |
| 65318 | TVA | 2022-12-23 | ens_bc_regime_aci2 | 10.85 | -12.10 | -12.10 |
| 65314 | TVA | 2022-12-23 | ens_recent | 9.54 | -10.08 | -10.08 |
| 65327 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 65320 | TVA | 2022-12-24 | additive_ml_special | 3.65 | -8.48 | -8.48 |
| 65321 | TVA | 2022-12-24 | boosting_ml | 6.04 | -12.78 | -12.78 |
| 65324 | TVA | 2022-12-24 | ens_bc_adaptive | 4.77 | -10.60 | -10.60 |
| 65323 | TVA | 2022-12-24 | ens_bc_regime | 4.93 | -11.86 | -11.86 |
| 65325 | TVA | 2022-12-24 | ens_bc_regime_aci | 4.93 | -11.86 | -11.86 |
| 65326 | TVA | 2022-12-24 | ens_bc_regime_aci2 | 4.93 | -11.86 | -11.86 |
| 65322 | TVA | 2022-12-24 | ens_recent | 4.68 | -10.66 | -10.66 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_ml_special | BPAT | mape | 12.541 | 0.000 | 750 |
| additive_ml_special | CISO | mape | 13.851 | 0.000 | 737 |
| additive_ml_special | DUK | mape | 10.152 | 0.000 | 750 |
| additive_ml_special | ERCO | mape | 11.907 | 0.000 | 746 |
| additive_ml_special | FPL | mape | 17.271 | 0.000 | 700 |
| additive_ml_special | ISNE | mape | 24.101 | 0.000 | 752 |
| additive_ml_special | MISO | mape | -2.885 | 0.004 | 746 |
| additive_ml_special | NYIS | mape | 0.771 | 0.441 | 752 |
| additive_ml_special | PJM | mape | -14.911 | 0.000 | 744 |
| additive_ml_special | SWPP | mape | -14.397 | 0.000 | 747 |
| additive_ml_special | TVA | mape | 17.307 | 0.000 | 739 |
| boosting_ml | BPAT | mape | 12.457 | 0.000 | 750 |
| boosting_ml | CISO | mape | 4.432 | 0.000 | 737 |
| boosting_ml | DUK | mape | 10.290 | 0.000 | 750 |
| boosting_ml | ERCO | mape | 6.704 | 0.000 | 746 |
| boosting_ml | FPL | mape | 21.017 | 0.000 | 700 |
| boosting_ml | ISNE | mape | 21.959 | 0.000 | 752 |
| boosting_ml | MISO | mape | -3.438 | 0.001 | 746 |
| boosting_ml | NYIS | mape | 0.532 | 0.595 | 752 |
| boosting_ml | PJM | mape | -14.855 | 0.000 | 744 |
| boosting_ml | SWPP | mape | -11.406 | 0.000 | 747 |
| boosting_ml | TVA | mape | 16.453 | 0.000 | 739 |
| ens_bc_adaptive | BPAT | mape | 9.403 | 0.000 | 750 |
| ens_bc_adaptive | CISO | mape | 2.411 | 0.016 | 737 |
| ens_bc_adaptive | DUK | mape | 8.259 | 0.000 | 750 |
| ens_bc_adaptive | ERCO | mape | 4.599 | 0.000 | 746 |
| ens_bc_adaptive | FPL | mape | 2.487 | 0.013 | 700 |
| ens_bc_adaptive | ISNE | mape | 20.603 | 0.000 | 752 |
| ens_bc_adaptive | MISO | mape | -6.867 | 0.000 | 746 |
| ens_bc_adaptive | NYIS | mape | -2.956 | 0.003 | 752 |
| ens_bc_adaptive | PJM | mape | -19.397 | 0.000 | 744 |
| ens_bc_adaptive | SWPP | mape | -14.932 | 0.000 | 747 |
| ens_bc_adaptive | TVA | mape | 14.826 | 0.000 | 739 |
| ens_bc_regime | BPAT | mape | 8.324 | 0.000 | 750 |
| ens_bc_regime | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime | DUK | mape | 6.960 | 0.000 | 750 |
| ens_bc_regime | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime | FPL | mape | -0.133 | 0.895 | 700 |
| ens_bc_regime | ISNE | mape | 18.609 | 0.000 | 752 |
| ens_bc_regime | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime | NYIS | mape | -3.388 | 0.001 | 752 |
| ens_bc_regime | PJM | mape | -25.615 | 0.000 | 744 |
| ens_bc_regime | SWPP | mape | -16.212 | 0.000 | 747 |
| ens_bc_regime | TVA | mape | 14.282 | 0.000 | 739 |
| ens_bc_regime_aci | BPAT | mape | 8.324 | 0.000 | 750 |
| ens_bc_regime_aci | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime_aci | DUK | mape | 6.960 | 0.000 | 750 |
| ens_bc_regime_aci | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime_aci | FPL | mape | -0.133 | 0.895 | 700 |
| ens_bc_regime_aci | ISNE | mape | 18.609 | 0.000 | 752 |
| ens_bc_regime_aci | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime_aci | NYIS | mape | -3.388 | 0.001 | 752 |
| ens_bc_regime_aci | PJM | mape | -25.615 | 0.000 | 744 |
| ens_bc_regime_aci | SWPP | mape | -16.212 | 0.000 | 747 |
| ens_bc_regime_aci | TVA | mape | 14.282 | 0.000 | 739 |
| ens_bc_regime_aci2 | BPAT | mape | 8.324 | 0.000 | 750 |
| ens_bc_regime_aci2 | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime_aci2 | DUK | mape | 6.960 | 0.000 | 750 |
| ens_bc_regime_aci2 | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime_aci2 | FPL | mape | -0.133 | 0.895 | 700 |
| ens_bc_regime_aci2 | ISNE | mape | 18.609 | 0.000 | 752 |
| ens_bc_regime_aci2 | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime_aci2 | NYIS | mape | -3.388 | 0.001 | 752 |
| ens_bc_regime_aci2 | PJM | mape | -25.615 | 0.000 | 744 |
| ens_bc_regime_aci2 | SWPP | mape | -16.212 | 0.000 | 747 |
| ens_bc_regime_aci2 | TVA | mape | 14.282 | 0.000 | 739 |
| ens_recent | BPAT | mape | 9.782 | 0.000 | 750 |
| ens_recent | CISO | mape | 4.977 | 0.000 | 737 |
| ens_recent | DUK | mape | 8.508 | 0.000 | 750 |
| ens_recent | ERCO | mape | 6.848 | 0.000 | 746 |
| ens_recent | FPL | mape | 18.299 | 0.000 | 700 |
| ens_recent | ISNE | mape | 20.729 | 0.000 | 752 |
| ens_recent | MISO | mape | -6.116 | 0.000 | 746 |
| ens_recent | NYIS | mape | -2.860 | 0.004 | 752 |
| ens_recent | PJM | mape | -19.327 | 0.000 | 744 |
| ens_recent | SWPP | mape | -15.215 | 0.000 | 747 |
| ens_recent | TVA | mape | 14.766 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| additive_ml_special | 0.981 |
| boosting_ml | 0.992 |
| ens_bc_adaptive | 0.992 |
| ens_bc_regime | 0.992 |
| ens_bc_regime_aci | 0.992 |
| ens_bc_regime_aci2 | 0.992 |
| ens_recent | 0.992 |
