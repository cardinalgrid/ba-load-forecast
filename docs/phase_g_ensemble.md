# Phase G: ensemble and correction

Development BAs: BPAT, CISO, DUK, ERCO, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `ens_hourly` weights the members per hour of the day; `ens_three` adds the recency regression; `ens_ratio` uses a boosting trained on the load divided by the last known 24 h mean; `final2_*` are the corrected versions with the recipe's correction; `final2_nn30` and `final2_nn50` change the size of the nearest-temperature pool.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2_three | 2.44 | 2.10 | 0.06 | -1.31 | 1.27 | 0.54 | 0.28 | -20.52 | 7461 | 10.00 |
| final2_hourly | 2.48 | 2.16 | 0.16 | -1.29 | 1.30 | 0.53 | 0.28 | -20.94 | 7461 | 10.00 |
| final2_nn50 | 2.48 | 2.15 | 0.13 | -1.30 | 1.31 | 0.53 | 0.28 | -20.88 | 7461 | 10.00 |
| final2 | 2.48 | 2.16 | 0.16 | -1.29 | 1.33 | 0.52 | 0.28 | -20.96 | 7461 | 10.00 |
| final2_nn30 | 2.49 | 2.15 | 0.18 | -1.29 | 1.33 | 0.52 | 0.28 | -20.82 | 7461 | 10.00 |
| final2_ratio | 2.52 | 2.17 | 0.19 | -1.29 | 1.29 | 0.52 | 0.27 | -22.18 | 7461 | 10.00 |
| DF | 2.64 | 2.34 | 0.53 | -0.93 | 0.90 | 0.00 | 0.00 | -19.98 | 7461 | 10.00 |
| ens_hourly | 2.70 | 2.34 | -0.97 | -1.96 | 1.29 | 0.48 | 0.23 | -21.45 | 7461 | 10.00 |
| final_ensemble | 2.71 | 2.35 | -0.96 | -1.96 | 1.29 | 0.47 | 0.23 | -21.47 | 7461 | 10.00 |
| ens_three | 2.72 | 2.36 | -1.08 | -2.00 | 1.31 | 0.47 | 0.23 | -20.44 | 7461 | 10.00 |
| ens_ratio | 2.73 | 2.35 | -0.94 | -1.95 | 1.33 | 0.47 | 0.23 | -22.06 | 7461 | 10.00 |
| final_boosting | 2.85 | 2.50 | -0.72 | -1.88 | 1.50 | 0.43 | 0.24 | -28.44 | 7461 | 10.00 |
| boosting_ratio | 2.92 | 2.52 | -0.68 | -1.88 | 1.48 | 0.43 | 0.24 | -25.22 | 7461 | 10.00 |
| final_additive | 2.97 | 2.61 | -1.23 | -2.24 | 1.43 | 0.42 | 0.22 | -20.55 | 7461 | 10.00 |
| recency_ml | 3.48 | 3.12 | -1.39 | -2.44 | 1.62 | 0.33 | 0.22 | -20.32 | 7461 | 10.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.38 | 2.15 | 0.39 | -0.65 | 0.24 | -6.72 |  |  | 737 | 25196.34 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 2.45 | 2.23 | -0.60 | -1.27 | 1.04 | -8.98 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.21 | -19.98 |  |  | 745 | 31350.31 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| boosting_ratio | BPAT | 2.81 | 2.46 | -0.32 | -1.51 | 1.84 | -18.02 | 0.28 | 0.24 | 750 | 6533.15 |
| boosting_ratio | CISO | 3.08 | 2.72 | -1.97 | -2.68 | 0.53 | -20.53 | 0.30 | 0.15 | 737 | 25196.34 |
| boosting_ratio | DUK | 3.62 | 3.09 | -0.50 | -2.27 | 1.48 | -16.83 | 0.35 | 0.29 | 750 | 12129.97 |
| boosting_ratio | ERCO | 3.28 | 2.74 | -2.13 | -2.90 | 1.28 | -16.24 | 0.34 | 0.17 | 746 | 46782.53 |
| boosting_ratio | ISNE | 3.69 | 3.33 | -0.72 | -2.05 | 0.61 | -17.56 | 0.26 | 0.16 | 752 | 13392.81 |
| boosting_ratio | MISO | 2.39 | 2.08 | -0.56 | -1.50 | 1.58 | -10.19 | 0.55 | 0.06 | 746 | 73788.38 |
| boosting_ratio | NYIS | 2.79 | 2.45 | -0.45 | -1.65 | 0.79 | -16.02 | 0.51 | 0.66 | 752 | 17400.75 |
| boosting_ratio | PJM | 2.92 | 2.56 | 0.14 | -1.42 | 1.95 | -11.43 | 0.42 | 0.42 | 744 | 91927.69 |
| boosting_ratio | SWPP | 2.77 | 2.26 | -0.73 | -1.93 | 1.59 | -25.22 | 0.65 | 0.09 | 745 | 31350.31 |
| boosting_ratio | TVA | 3.34 | 2.91 | -0.20 | -1.93 | 1.56 | -13.73 | 0.24 | 0.29 | 739 | 18562.62 |
| ens_hourly | BPAT | 2.58 | 2.25 | -0.67 | -1.61 | 1.81 | -18.30 | 0.32 | 0.23 | 750 | 6533.15 |
| ens_hourly | CISO | 3.06 | 2.58 | -2.39 | -3.03 | 0.36 | -18.44 | 0.38 | 0.14 | 737 | 25196.34 |
| ens_hourly | DUK | 3.43 | 2.97 | -0.56 | -2.26 | 1.32 | -15.68 | 0.38 | 0.27 | 750 | 12129.97 |
| ens_hourly | ERCO | 3.13 | 2.69 | -2.26 | -2.90 | 1.09 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| ens_hourly | ISNE | 3.52 | 3.13 | -0.96 | -2.19 | 0.51 | -19.51 | 0.27 | 0.17 | 752 | 13392.81 |
| ens_hourly | MISO | 2.22 | 1.91 | -0.94 | -1.60 | 1.52 | -8.21 | 0.57 | 0.05 | 746 | 73788.38 |
| ens_hourly | NYIS | 2.47 | 2.13 | -0.60 | -1.68 | 0.54 | -13.90 | 0.57 | 0.65 | 752 | 17400.75 |
| ens_hourly | PJM | 2.60 | 2.34 | -0.29 | -1.54 | 1.56 | -10.97 | 0.47 | 0.39 | 744 | 91927.69 |
| ens_hourly | SWPP | 2.43 | 1.98 | -0.61 | -1.72 | 1.47 | -21.45 | 0.72 | 0.09 | 745 | 31350.31 |
| ens_hourly | TVA | 3.13 | 2.73 | -0.63 | -2.02 | 1.49 | -14.26 | 0.28 | 0.28 | 739 | 18562.62 |
| ens_ratio | BPAT | 2.61 | 2.29 | -0.60 | -1.58 | 1.82 | -18.22 | 0.32 | 0.23 | 750 | 6533.15 |
| ens_ratio | CISO | 3.10 | 2.64 | -2.33 | -3.05 | 0.40 | -19.51 | 0.36 | 0.14 | 737 | 25196.34 |
| ens_ratio | DUK | 3.44 | 3.00 | -0.61 | -2.25 | 1.43 | -15.65 | 0.39 | 0.27 | 750 | 12129.97 |
| ens_ratio | ERCO | 3.19 | 2.72 | -2.17 | -2.86 | 1.00 | -15.01 | 0.36 | 0.16 | 746 | 46782.53 |
| ens_ratio | ISNE | 3.53 | 3.12 | -0.92 | -2.16 | 0.53 | -18.19 | 0.28 | 0.16 | 752 | 13392.81 |
| ens_ratio | MISO | 2.23 | 1.94 | -0.96 | -1.63 | 1.63 | -8.57 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_ratio | NYIS | 2.52 | 2.10 | -0.63 | -1.74 | 0.59 | -14.83 | 0.58 | 0.66 | 752 | 17400.75 |
| ens_ratio | PJM | 2.65 | 2.32 | -0.26 | -1.50 | 1.65 | -11.00 | 0.46 | 0.40 | 744 | 91927.69 |
| ens_ratio | SWPP | 2.47 | 2.01 | -0.50 | -1.67 | 1.44 | -22.06 | 0.70 | 0.09 | 745 | 31350.31 |
| ens_ratio | TVA | 3.16 | 2.73 | -0.62 | -2.06 | 1.46 | -12.80 | 0.28 | 0.27 | 739 | 18562.62 |
| ens_three | BPAT | 2.56 | 2.29 | -0.87 | -1.70 | 1.75 | -18.52 | 0.35 | 0.23 | 750 | 6533.15 |
| ens_three | CISO | 3.36 | 2.82 | -2.85 | -3.38 | 0.36 | -17.95 | 0.32 | 0.13 | 737 | 25196.34 |
| ens_three | DUK | 3.41 | 3.03 | -0.54 | -2.25 | 1.45 | -14.53 | 0.40 | 0.27 | 750 | 12129.97 |
| ens_three | ERCO | 3.16 | 2.71 | -2.40 | -3.00 | 1.03 | -15.07 | 0.36 | 0.17 | 746 | 46782.53 |
| ens_three | ISNE | 3.65 | 3.27 | -1.42 | -2.40 | 0.52 | -18.19 | 0.25 | 0.14 | 752 | 13392.81 |
| ens_three | MISO | 2.25 | 1.92 | -1.02 | -1.63 | 1.70 | -8.77 | 0.57 | 0.05 | 746 | 73788.38 |
| ens_three | NYIS | 2.48 | 2.12 | -0.60 | -1.66 | 0.61 | -14.95 | 0.57 | 0.65 | 752 | 17400.75 |
| ens_three | PJM | 2.58 | 2.29 | -0.37 | -1.53 | 1.54 | -11.08 | 0.48 | 0.41 | 744 | 91927.69 |
| ens_three | SWPP | 2.35 | 1.95 | -0.46 | -1.57 | 1.43 | -20.44 | 0.71 | 0.09 | 745 | 31350.31 |
| ens_three | TVA | 3.10 | 2.71 | -0.77 | -2.11 | 1.38 | -14.95 | 0.29 | 0.26 | 739 | 18562.62 |
| final2 | BPAT | 2.55 | 2.21 | -0.24 | -1.41 | 1.81 | -18.21 | 0.37 | 0.26 | 750 | 6533.15 |
| final2 | CISO | 2.58 | 2.24 | 0.55 | -1.12 | 0.33 | -12.29 | 0.47 | 0.26 | 737 | 25196.34 |
| final2 | DUK | 3.36 | 3.03 | 0.11 | -1.85 | 1.32 | -15.78 | 0.39 | 0.32 | 750 | 12129.97 |
| final2 | ERCO | 2.79 | 2.38 | 0.20 | -1.47 | 1.12 | -13.56 | 0.44 | 0.28 | 746 | 46782.53 |
| final2 | ISNE | 3.43 | 2.98 | 0.64 | -1.35 | 0.51 | -17.43 | 0.30 | 0.22 | 752 | 13392.81 |
| final2 | MISO | 2.10 | 1.87 | 0.11 | -1.03 | 1.63 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2 | NYIS | 2.48 | 2.10 | 0.19 | -1.30 | 0.58 | -12.50 | 0.57 | 0.71 | 752 | 17400.75 |
| final2 | PJM | 2.29 | 1.98 | 0.05 | -1.31 | 1.64 | -10.41 | 0.56 | 0.42 | 744 | 91927.69 |
| final2 | SWPP | 2.37 | 1.98 | -0.08 | -1.35 | 1.46 | -20.96 | 0.72 | 0.11 | 745 | 31350.31 |
| final2 | TVA | 3.02 | 2.63 | 0.40 | -1.52 | 1.36 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final2_hourly | BPAT | 2.55 | 2.19 | -0.25 | -1.42 | 1.85 | -18.20 | 0.37 | 0.26 | 750 | 6533.15 |
| final2_hourly | CISO | 2.56 | 2.23 | 0.52 | -1.11 | 0.33 | -12.32 | 0.47 | 0.26 | 737 | 25196.34 |
| final2_hourly | DUK | 3.35 | 3.03 | 0.12 | -1.84 | 1.32 | -15.80 | 0.39 | 0.32 | 750 | 12129.97 |
| final2_hourly | ERCO | 2.79 | 2.38 | 0.20 | -1.47 | 1.10 | -13.41 | 0.44 | 0.29 | 746 | 46782.53 |
| final2_hourly | ISNE | 3.43 | 2.97 | 0.64 | -1.34 | 0.52 | -17.45 | 0.30 | 0.22 | 752 | 13392.81 |
| final2_hourly | MISO | 2.10 | 1.87 | 0.11 | -1.02 | 1.59 | -7.97 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_hourly | NYIS | 2.47 | 2.08 | 0.20 | -1.28 | 0.57 | -12.47 | 0.58 | 0.72 | 752 | 17400.75 |
| final2_hourly | PJM | 2.28 | 1.99 | 0.07 | -1.30 | 1.59 | -10.48 | 0.56 | 0.42 | 744 | 91927.69 |
| final2_hourly | SWPP | 2.36 | 1.97 | -0.07 | -1.35 | 1.44 | -20.94 | 0.73 | 0.11 | 745 | 31350.31 |
| final2_hourly | TVA | 3.02 | 2.64 | 0.39 | -1.52 | 1.36 | -15.98 | 0.29 | 0.33 | 739 | 18562.62 |
| final2_nn30 | BPAT | 2.56 | 2.21 | -0.23 | -1.41 | 1.81 | -18.15 | 0.36 | 0.27 | 750 | 6533.15 |
| final2_nn30 | CISO | 2.58 | 2.24 | 0.53 | -1.14 | 0.33 | -11.97 | 0.46 | 0.26 | 737 | 25196.34 |
| final2_nn30 | DUK | 3.37 | 3.04 | 0.15 | -1.83 | 1.39 | -17.51 | 0.38 | 0.33 | 750 | 12129.97 |
| final2_nn30 | ERCO | 2.79 | 2.40 | 0.25 | -1.44 | 1.13 | -14.09 | 0.43 | 0.28 | 746 | 46782.53 |
| final2_nn30 | ISNE | 3.46 | 3.03 | 0.73 | -1.32 | 0.53 | -17.99 | 0.30 | 0.22 | 752 | 13392.81 |
| final2_nn30 | MISO | 2.10 | 1.84 | 0.13 | -1.03 | 1.61 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_nn30 | NYIS | 2.50 | 2.10 | 0.20 | -1.30 | 0.58 | -12.57 | 0.58 | 0.71 | 752 | 17400.75 |
| final2_nn30 | PJM | 2.29 | 1.98 | 0.09 | -1.31 | 1.63 | -9.94 | 0.55 | 0.42 | 744 | 91927.69 |
| final2_nn30 | SWPP | 2.38 | 1.96 | -0.07 | -1.35 | 1.50 | -20.82 | 0.73 | 0.11 | 745 | 31350.31 |
| final2_nn30 | TVA | 3.03 | 2.64 | 0.41 | -1.51 | 1.34 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final2_nn50 | BPAT | 2.54 | 2.23 | -0.27 | -1.43 | 1.84 | -18.21 | 0.37 | 0.26 | 750 | 6533.15 |
| final2_nn50 | CISO | 2.58 | 2.24 | 0.51 | -1.14 | 0.33 | -12.55 | 0.47 | 0.27 | 737 | 25196.34 |
| final2_nn50 | DUK | 3.34 | 3.04 | 0.05 | -1.88 | 1.30 | -15.78 | 0.40 | 0.32 | 750 | 12129.97 |
| final2_nn50 | ERCO | 2.80 | 2.36 | 0.19 | -1.47 | 1.14 | -14.04 | 0.43 | 0.28 | 746 | 46782.53 |
| final2_nn50 | ISNE | 3.43 | 2.99 | 0.61 | -1.36 | 0.50 | -17.99 | 0.31 | 0.22 | 752 | 13392.81 |
| final2_nn50 | MISO | 2.09 | 1.85 | 0.07 | -1.04 | 1.58 | -7.44 | 0.61 | 0.06 | 746 | 73788.38 |
| final2_nn50 | NYIS | 2.47 | 2.09 | 0.16 | -1.31 | 0.56 | -12.57 | 0.57 | 0.70 | 752 | 17400.75 |
| final2_nn50 | PJM | 2.29 | 1.99 | 0.03 | -1.32 | 1.60 | -10.78 | 0.55 | 0.42 | 744 | 91927.69 |
| final2_nn50 | SWPP | 2.36 | 1.95 | -0.10 | -1.36 | 1.46 | -20.88 | 0.72 | 0.10 | 745 | 31350.31 |
| final2_nn50 | TVA | 3.02 | 2.65 | 0.37 | -1.53 | 1.37 | -15.18 | 0.28 | 0.32 | 739 | 18562.62 |
| final2_ratio | BPAT | 2.55 | 2.22 | -0.38 | -1.48 | 1.78 | -17.97 | 0.37 | 0.25 | 750 | 6533.15 |
| final2_ratio | CISO | 2.61 | 2.20 | 0.54 | -1.15 | 0.36 | -13.91 | 0.47 | 0.26 | 737 | 25196.34 |
| final2_ratio | DUK | 3.37 | 3.04 | 0.10 | -1.85 | 1.40 | -15.27 | 0.38 | 0.32 | 750 | 12129.97 |
| final2_ratio | ERCO | 2.88 | 2.40 | 0.29 | -1.44 | 1.07 | -13.75 | 0.41 | 0.27 | 746 | 46782.53 |
| final2_ratio | ISNE | 3.46 | 3.00 | 0.72 | -1.33 | 0.53 | -15.86 | 0.31 | 0.21 | 752 | 13392.81 |
| final2_ratio | MISO | 2.11 | 1.83 | 0.13 | -1.04 | 1.58 | -8.54 | 0.61 | 0.07 | 746 | 73788.38 |
| final2_ratio | NYIS | 2.52 | 2.10 | 0.19 | -1.33 | 0.56 | -13.31 | 0.59 | 0.72 | 752 | 17400.75 |
| final2_ratio | PJM | 2.34 | 2.07 | 0.08 | -1.31 | 1.56 | -10.24 | 0.53 | 0.41 | 744 | 91927.69 |
| final2_ratio | SWPP | 2.40 | 1.97 | -0.00 | -1.34 | 1.40 | -22.18 | 0.72 | 0.12 | 745 | 31350.31 |
| final2_ratio | TVA | 3.05 | 2.64 | 0.50 | -1.51 | 1.45 | -14.28 | 0.28 | 0.32 | 739 | 18562.62 |
| final2_three | BPAT | 2.51 | 2.18 | -0.45 | -1.49 | 1.72 | -18.75 | 0.36 | 0.25 | 750 | 6533.15 |
| final2_three | CISO | 2.49 | 2.23 | 0.41 | -1.11 | 0.34 | -12.39 | 0.48 | 0.27 | 737 | 25196.34 |
| final2_three | DUK | 3.32 | 2.99 | 0.00 | -1.89 | 1.39 | -16.47 | 0.38 | 0.31 | 750 | 12129.97 |
| final2_three | ERCO | 2.74 | 2.29 | 0.12 | -1.50 | 1.03 | -14.46 | 0.45 | 0.28 | 746 | 46782.53 |
| final2_three | ISNE | 3.45 | 3.03 | 0.42 | -1.40 | 0.51 | -16.85 | 0.30 | 0.21 | 752 | 13392.81 |
| final2_three | MISO | 2.07 | 1.83 | 0.02 | -1.06 | 1.68 | -8.33 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_three | NYIS | 2.42 | 2.02 | 0.07 | -1.33 | 0.56 | -13.74 | 0.59 | 0.71 | 752 | 17400.75 |
| final2_three | PJM | 2.26 | 1.93 | 0.01 | -1.29 | 1.42 | -11.39 | 0.59 | 0.42 | 744 | 91927.69 |
| final2_three | SWPP | 2.26 | 1.89 | -0.27 | -1.38 | 1.50 | -20.52 | 0.74 | 0.11 | 745 | 31350.31 |
| final2_three | TVA | 2.99 | 2.59 | 0.37 | -1.55 | 1.37 | -16.38 | 0.30 | 0.32 | 739 | 18562.62 |
| final_additive | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| final_additive | CISO | 3.78 | 3.16 | -2.87 | -3.82 | 0.42 | -18.17 | 0.25 | 0.13 | 737 | 25196.34 |
| final_additive | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| final_additive | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
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
| final_ensemble | ISNE | 3.53 | 3.16 | -0.96 | -2.20 | 0.53 | -19.48 | 0.26 | 0.16 | 752 | 13392.81 |
| final_ensemble | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| final_ensemble | NYIS | 2.49 | 2.14 | -0.64 | -1.71 | 0.56 | -13.90 | 0.56 | 0.65 | 752 | 17400.75 |
| final_ensemble | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.46 | 0.39 | 744 | 91927.69 |
| final_ensemble | SWPP | 2.44 | 1.98 | -0.59 | -1.71 | 1.47 | -21.47 | 0.71 | 0.09 | 745 | 31350.31 |
| final_ensemble | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |
| recency_ml | BPAT | 3.20 | 2.83 | -1.37 | -2.22 | 1.97 | -18.92 | 0.22 | 0.20 | 750 | 6533.15 |
| recency_ml | CISO | 5.67 | 5.37 | -4.56 | -5.02 | 0.58 | -19.79 | 0.06 | 0.08 | 737 | 25196.34 |
| recency_ml | DUK | 3.91 | 3.52 | -0.50 | -2.47 | 1.62 | -15.94 | 0.29 | 0.26 | 750 | 12129.97 |
| recency_ml | ERCO | 3.72 | 3.28 | -2.73 | -3.46 | 1.17 | -19.79 | 0.29 | 0.18 | 746 | 46782.53 |
| recency_ml | ISNE | 5.23 | 4.91 | -2.67 | -3.43 | 0.68 | -20.32 | 0.06 | 0.11 | 752 | 13392.81 |
| recency_ml | MISO | 2.92 | 2.60 | -1.20 | -1.97 | 2.15 | -14.05 | 0.42 | 0.05 | 746 | 73788.38 |
| recency_ml | NYIS | 3.45 | 3.05 | -0.47 | -1.82 | 0.84 | -18.20 | 0.36 | 0.64 | 752 | 17400.75 |
| recency_ml | PJM | 3.09 | 2.76 | -0.58 | -1.85 | 1.94 | -19.85 | 0.32 | 0.37 | 744 | 91927.69 |
| recency_ml | SWPP | 2.90 | 2.48 | -0.16 | -1.61 | 1.70 | -17.99 | 0.60 | 0.10 | 745 | 31350.31 |
| recency_ml | TVA | 3.58 | 3.27 | -1.05 | -2.58 | 1.52 | -16.84 | 0.20 | 0.24 | 739 | 18562.62 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | uri | 2.77 | -0.21 | -1.69 | -6.97 | 6 |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| boosting_ratio | BPAT | uri | 3.92 | 2.48 | -0.99 | -5.96 | 6 |
| boosting_ratio | CISO | uri | 1.94 | -0.81 | -1.05 | -2.40 | 6 |
| boosting_ratio | DUK | uri | 3.80 | -2.66 | -2.66 | -5.22 | 6 |
| boosting_ratio | ERCO | uri | 4.28 | -8.34 | -8.34 | -10.37 | 2 |
| boosting_ratio | ISNE | uri | 3.19 | 1.36 | -0.40 | -2.37 | 6 |
| boosting_ratio | MISO | uri | 2.93 | -2.56 | -2.82 | -6.40 | 5 |
| boosting_ratio | NYIS | uri | 1.97 | 1.00 | -0.35 | -2.13 | 6 |
| boosting_ratio | PJM | uri | 2.05 | -1.41 | -2.04 | -4.03 | 6 |
| boosting_ratio | SWPP | uri | 6.49 | 0.83 | -2.71 | -7.36 | 4 |
| boosting_ratio | TVA | uri | 4.70 | -3.36 | -4.53 | -9.47 | 6 |
| ens_hourly | BPAT | uri | 2.93 | 0.31 | -0.67 | -3.37 | 6 |
| ens_hourly | CISO | uri | 1.59 | 0.41 | -0.23 | -0.80 | 6 |
| ens_hourly | DUK | uri | 3.41 | -2.78 | -2.78 | -5.99 | 6 |
| ens_hourly | ERCO | uri | 6.26 | -9.21 | -9.21 | -9.49 | 2 |
| ens_hourly | ISNE | uri | 2.79 | 1.29 | -0.41 | -2.28 | 6 |
| ens_hourly | MISO | uri | 3.35 | -3.08 | -3.19 | -6.26 | 5 |
| ens_hourly | NYIS | uri | 2.13 | 1.45 | -0.25 | -1.49 | 6 |
| ens_hourly | PJM | uri | 2.22 | 0.41 | -0.71 | -3.29 | 6 |
| ens_hourly | SWPP | uri | 6.08 | -0.32 | -2.95 | -6.24 | 4 |
| ens_hourly | TVA | uri | 2.70 | -1.12 | -1.74 | -3.38 | 6 |
| ens_ratio | BPAT | uri | 3.04 | 0.97 | -0.74 | -3.91 | 6 |
| ens_ratio | CISO | uri | 1.61 | 0.70 | -0.13 | -0.74 | 6 |
| ens_ratio | DUK | uri | 3.51 | -2.70 | -2.70 | -5.16 | 6 |
| ens_ratio | ERCO | uri | 4.33 | -6.98 | -6.98 | -7.19 | 2 |
| ens_ratio | ISNE | uri | 2.71 | 1.45 | -0.19 | -0.59 | 6 |
| ens_ratio | MISO | uri | 3.18 | -2.43 | -2.73 | -5.84 | 5 |
| ens_ratio | NYIS | uri | 2.01 | 1.58 | -0.17 | -1.02 | 6 |
| ens_ratio | PJM | uri | 2.20 | 0.36 | -0.86 | -3.13 | 6 |
| ens_ratio | SWPP | uri | 6.51 | 1.30 | -2.30 | -4.89 | 4 |
| ens_ratio | TVA | uri | 3.67 | -1.72 | -2.86 | -5.58 | 6 |
| ens_three | BPAT | uri | 2.83 | 0.08 | -0.74 | -3.82 | 6 |
| ens_three | CISO | uri | 1.88 | 0.11 | -0.35 | -0.70 | 6 |
| ens_three | DUK | uri | 3.58 | -2.98 | -2.98 | -6.40 | 6 |
| ens_three | ERCO | uri | 5.48 | -7.70 | -7.70 | -9.22 | 2 |
| ens_three | ISNE | uri | 2.50 | 0.38 | -0.56 | -2.72 | 6 |
| ens_three | MISO | uri | 3.98 | -3.94 | -3.94 | -7.27 | 5 |
| ens_three | NYIS | uri | 2.00 | 1.75 | -0.11 | -0.66 | 6 |
| ens_three | PJM | uri | 2.32 | 0.71 | -0.71 | -3.60 | 6 |
| ens_three | SWPP | uri | 6.28 | -1.13 | -3.49 | -7.59 | 4 |
| ens_three | TVA | uri | 2.97 | -0.93 | -1.77 | -3.40 | 6 |
| final2 | BPAT | uri | 2.87 | 0.04 | -0.92 | -4.38 | 6 |
| final2 | CISO | uri | 1.79 | 0.24 | -0.41 | -1.10 | 6 |
| final2 | DUK | uri | 3.51 | -1.08 | -1.67 | -4.03 | 6 |
| final2 | ERCO | uri | 7.11 | -9.52 | -9.52 | -10.27 | 2 |
| final2 | ISNE | uri | 2.76 | 2.18 | -0.15 | -0.87 | 6 |
| final2 | MISO | uri | 3.44 | -2.39 | -2.82 | -5.84 | 5 |
| final2 | NYIS | uri | 2.03 | 2.22 | -0.14 | -0.82 | 6 |
| final2 | PJM | uri | 1.86 | 0.07 | -0.65 | -2.07 | 6 |
| final2 | SWPP | uri | 6.41 | 1.17 | -2.28 | -5.30 | 4 |
| final2 | TVA | uri | 3.04 | -1.89 | -2.67 | -5.67 | 6 |
| final2_hourly | BPAT | uri | 2.87 | 0.10 | -0.91 | -4.29 | 6 |
| final2_hourly | CISO | uri | 1.77 | 0.14 | -0.50 | -1.26 | 6 |
| final2_hourly | DUK | uri | 3.51 | -1.06 | -1.65 | -4.08 | 6 |
| final2_hourly | ERCO | uri | 7.09 | -9.46 | -9.46 | -10.11 | 2 |
| final2_hourly | ISNE | uri | 2.73 | 2.13 | -0.18 | -1.07 | 6 |
| final2_hourly | MISO | uri | 3.43 | -2.34 | -2.83 | -5.82 | 5 |
| final2_hourly | NYIS | uri | 2.02 | 2.03 | -0.19 | -1.15 | 6 |
| final2_hourly | PJM | uri | 1.85 | 0.01 | -0.62 | -2.08 | 6 |
| final2_hourly | SWPP | uri | 6.42 | 1.23 | -2.29 | -5.29 | 4 |
| final2_hourly | TVA | uri | 3.03 | -1.91 | -2.70 | -5.69 | 6 |
| final2_nn30 | BPAT | uri | 3.07 | 0.66 | -0.72 | -3.81 | 6 |
| final2_nn30 | CISO | uri | 1.79 | -0.02 | -0.66 | -1.50 | 6 |
| final2_nn30 | DUK | uri | 3.35 | -0.61 | -1.33 | -3.82 | 6 |
| final2_nn30 | ERCO | uri | 7.33 | -9.92 | -9.92 | -11.22 | 2 |
| final2_nn30 | ISNE | uri | 2.74 | 2.20 | -0.14 | -0.84 | 6 |
| final2_nn30 | MISO | uri | 3.48 | -2.47 | -2.80 | -5.84 | 5 |
| final2_nn30 | NYIS | uri | 1.99 | 2.19 | -0.16 | -0.94 | 6 |
| final2_nn30 | PJM | uri | 1.88 | -0.07 | -0.70 | -2.27 | 6 |
| final2_nn30 | SWPP | uri | 6.35 | 1.45 | -2.04 | -4.43 | 4 |
| final2_nn30 | TVA | uri | 3.02 | -1.78 | -2.59 | -5.32 | 6 |
| final2_nn50 | BPAT | uri | 2.80 | -0.28 | -1.07 | -4.89 | 6 |
| final2_nn50 | CISO | uri | 1.75 | 0.40 | -0.24 | -1.04 | 6 |
| final2_nn50 | DUK | uri | 3.45 | -1.71 | -2.09 | -4.32 | 6 |
| final2_nn50 | ERCO | uri | 6.98 | -9.52 | -9.52 | -10.27 | 2 |
| final2_nn50 | ISNE | uri | 2.83 | 2.34 | -0.15 | -0.88 | 6 |
| final2_nn50 | MISO | uri | 3.44 | -2.52 | -2.86 | -5.93 | 5 |
| final2_nn50 | NYIS | uri | 2.02 | 2.06 | -0.14 | -0.82 | 6 |
| final2_nn50 | PJM | uri | 1.86 | 0.08 | -0.63 | -2.27 | 6 |
| final2_nn50 | SWPP | uri | 6.16 | 1.21 | -2.28 | -5.37 | 4 |
| final2_nn50 | TVA | uri | 3.08 | -2.02 | -2.80 | -5.47 | 6 |
| final2_ratio | BPAT | uri | 2.91 | 0.62 | -0.95 | -4.82 | 6 |
| final2_ratio | CISO | uri | 1.81 | 0.34 | -0.39 | -1.21 | 6 |
| final2_ratio | DUK | uri | 3.55 | -1.25 | -1.62 | -4.44 | 6 |
| final2_ratio | ERCO | uri | 5.03 | -7.15 | -7.15 | -8.17 | 2 |
| final2_ratio | ISNE | uri | 2.62 | 2.02 | -0.03 | -0.21 | 6 |
| final2_ratio | MISO | uri | 3.10 | -1.16 | -2.07 | -4.87 | 5 |
| final2_ratio | NYIS | uri | 1.92 | 1.91 | -0.14 | -0.84 | 6 |
| final2_ratio | PJM | uri | 1.87 | -0.06 | -0.77 | -2.67 | 6 |
| final2_ratio | SWPP | uri | 6.83 | 2.92 | -1.66 | -4.29 | 4 |
| final2_ratio | TVA | uri | 4.23 | -2.24 | -3.65 | -7.49 | 6 |
| final2_three | BPAT | uri | 2.66 | -0.54 | -1.13 | -4.99 | 6 |
| final2_three | CISO | uri | 1.93 | -0.07 | -0.54 | -0.95 | 6 |
| final2_three | DUK | uri | 3.62 | -1.63 | -2.01 | -4.49 | 6 |
| final2_three | ERCO | uri | 6.54 | -8.52 | -8.52 | -8.75 | 2 |
| final2_three | ISNE | uri | 2.61 | 1.78 | -0.13 | -0.76 | 6 |
| final2_three | MISO | uri | 4.05 | -3.32 | -3.55 | -7.08 | 5 |
| final2_three | NYIS | uri | 1.95 | 1.95 | -0.08 | -0.50 | 6 |
| final2_three | PJM | uri | 1.99 | -0.05 | -0.78 | -2.89 | 6 |
| final2_three | SWPP | uri | 6.67 | -0.03 | -3.10 | -7.20 | 4 |
| final2_three | TVA | uri | 3.44 | -2.08 | -3.01 | -5.89 | 6 |
| final_additive | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| final_additive | CISO | uri | 2.40 | 2.19 | 0.00 | 0.00 | 6 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
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
| final_ensemble | ISNE | uri | 2.81 | 1.32 | -0.38 | -2.20 | 6 |
| final_ensemble | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| final_ensemble | NYIS | uri | 2.11 | 1.50 | -0.23 | -1.35 | 6 |
| final_ensemble | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| final_ensemble | SWPP | uri | 6.08 | -0.39 | -2.96 | -6.25 | 4 |
| final_ensemble | TVA | uri | 2.71 | -1.06 | -1.72 | -3.36 | 6 |
| recency_ml | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| recency_ml | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| recency_ml | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| recency_ml | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| recency_ml | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| recency_ml | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| recency_ml | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| recency_ml | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| recency_ml | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| recency_ml | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | CISO | elliott | 3.38 | 1.96 | -0.88 | -4.40 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| boosting_ratio | BPAT | elliott | 7.12 | 0.43 | -2.31 | -7.90 | 5 |
| boosting_ratio | CISO | elliott | 4.01 | 1.05 | -1.26 | -6.13 | 5 |
| boosting_ratio | DUK | elliott | 7.75 | -1.59 | -3.20 | -9.62 | 4 |
| boosting_ratio | ERCO | elliott | 7.44 | -2.16 | -5.31 | -14.17 | 5 |
| boosting_ratio | ISNE | elliott | 3.50 | 2.91 | -0.27 | -1.35 | 5 |
| boosting_ratio | MISO | elliott | 4.18 | -1.29 | -2.55 | -5.39 | 5 |
| boosting_ratio | NYIS | elliott | 2.86 | -1.27 | -2.05 | -4.69 | 5 |
| boosting_ratio | PJM | elliott | 5.89 | -2.68 | -4.19 | -11.43 | 5 |
| boosting_ratio | SWPP | elliott | 7.61 | -0.42 | -3.65 | -11.56 | 5 |
| boosting_ratio | TVA | elliott | 11.08 | 10.45 | 0.00 | 0.00 | 3 |
| ens_hourly | BPAT | elliott | 4.21 | -3.42 | -3.88 | -8.30 | 5 |
| ens_hourly | CISO | elliott | 3.44 | 2.60 | -0.48 | -2.42 | 5 |
| ens_hourly | DUK | elliott | 3.65 | -2.88 | -2.88 | -3.86 | 4 |
| ens_hourly | ERCO | elliott | 6.72 | -4.23 | -5.32 | -12.60 | 5 |
| ens_hourly | ISNE | elliott | 3.40 | 2.15 | -0.43 | -1.24 | 5 |
| ens_hourly | MISO | elliott | 3.45 | -2.05 | -2.83 | -4.91 | 5 |
| ens_hourly | NYIS | elliott | 2.73 | -0.80 | -1.68 | -3.55 | 5 |
| ens_hourly | PJM | elliott | 4.24 | -1.95 | -2.88 | -6.29 | 5 |
| ens_hourly | SWPP | elliott | 4.14 | -2.21 | -3.25 | -7.42 | 5 |
| ens_hourly | TVA | elliott | 6.81 | 2.92 | -0.40 | -0.76 | 3 |
| ens_ratio | BPAT | elliott | 5.19 | -0.49 | -1.94 | -5.60 | 5 |
| ens_ratio | CISO | elliott | 3.59 | 2.45 | -0.71 | -3.53 | 5 |
| ens_ratio | DUK | elliott | 5.13 | -2.16 | -2.16 | -5.04 | 4 |
| ens_ratio | ERCO | elliott | 7.01 | -3.56 | -4.83 | -13.41 | 5 |
| ens_ratio | ISNE | elliott | 3.40 | 2.36 | -0.43 | -1.13 | 5 |
| ens_ratio | MISO | elliott | 3.60 | -2.11 | -2.98 | -4.76 | 5 |
| ens_ratio | NYIS | elliott | 2.84 | -1.58 | -2.21 | -4.10 | 5 |
| ens_ratio | PJM | elliott | 4.52 | -2.32 | -3.34 | -8.72 | 5 |
| ens_ratio | SWPP | elliott | 5.26 | -1.50 | -3.21 | -7.46 | 5 |
| ens_ratio | TVA | elliott | 9.40 | 7.91 | 0.00 | 0.00 | 3 |
| ens_three | BPAT | elliott | 3.91 | -3.37 | -3.69 | -8.85 | 5 |
| ens_three | CISO | elliott | 3.37 | 3.43 | -0.33 | -1.64 | 5 |
| ens_three | DUK | elliott | 3.42 | -3.78 | -3.78 | -5.59 | 4 |
| ens_three | ERCO | elliott | 5.65 | -3.51 | -4.37 | -7.74 | 5 |
| ens_three | ISNE | elliott | 3.42 | 2.55 | -0.56 | -1.72 | 5 |
| ens_three | MISO | elliott | 3.51 | -2.89 | -3.45 | -6.43 | 5 |
| ens_three | NYIS | elliott | 2.78 | -1.25 | -1.99 | -4.01 | 5 |
| ens_three | PJM | elliott | 4.59 | -4.24 | -4.63 | -10.18 | 5 |
| ens_three | SWPP | elliott | 3.70 | -2.65 | -3.38 | -7.95 | 5 |
| ens_three | TVA | elliott | 6.02 | 2.93 | -1.03 | -1.64 | 3 |
| final2 | BPAT | elliott | 3.70 | -2.63 | -3.01 | -6.46 | 5 |
| final2 | CISO | elliott | 3.19 | 2.15 | -0.43 | -2.17 | 5 |
| final2 | DUK | elliott | 3.14 | -1.01 | -1.49 | -4.41 | 4 |
| final2 | ERCO | elliott | 6.82 | -1.38 | -3.86 | -9.30 | 5 |
| final2 | ISNE | elliott | 3.51 | 1.63 | -0.72 | -2.23 | 5 |
| final2 | MISO | elliott | 3.42 | -1.58 | -2.69 | -4.10 | 5 |
| final2 | NYIS | elliott | 2.78 | -0.62 | -1.45 | -3.18 | 5 |
| final2 | PJM | elliott | 4.26 | -2.70 | -3.11 | -6.29 | 5 |
| final2 | SWPP | elliott | 4.56 | 0.73 | -1.68 | -4.76 | 5 |
| final2 | TVA | elliott | 6.70 | 4.69 | 0.00 | 0.00 | 3 |
| final2_hourly | BPAT | elliott | 3.70 | -2.56 | -2.98 | -6.43 | 5 |
| final2_hourly | CISO | elliott | 3.18 | 1.88 | -0.53 | -2.65 | 5 |
| final2_hourly | DUK | elliott | 3.10 | -0.86 | -1.36 | -3.95 | 4 |
| final2_hourly | ERCO | elliott | 6.80 | -1.28 | -3.81 | -9.26 | 5 |
| final2_hourly | ISNE | elliott | 3.49 | 1.77 | -0.69 | -2.23 | 5 |
| final2_hourly | MISO | elliott | 3.44 | -1.75 | -2.72 | -4.03 | 5 |
| final2_hourly | NYIS | elliott | 2.80 | -0.41 | -1.35 | -3.22 | 5 |
| final2_hourly | PJM | elliott | 4.22 | -2.91 | -3.25 | -6.23 | 5 |
| final2_hourly | SWPP | elliott | 4.58 | 0.66 | -1.73 | -4.91 | 5 |
| final2_hourly | TVA | elliott | 6.66 | 4.67 | 0.00 | 0.00 | 3 |
| final2_nn30 | BPAT | elliott | 3.75 | -2.94 | -3.29 | -6.76 | 5 |
| final2_nn30 | CISO | elliott | 3.15 | 2.17 | -0.46 | -2.29 | 5 |
| final2_nn30 | DUK | elliott | 3.10 | -1.04 | -1.34 | -3.84 | 4 |
| final2_nn30 | ERCO | elliott | 6.95 | -0.61 | -3.50 | -8.62 | 5 |
| final2_nn30 | ISNE | elliott | 3.55 | 1.77 | -0.63 | -1.87 | 5 |
| final2_nn30 | MISO | elliott | 3.43 | -1.58 | -2.73 | -4.20 | 5 |
| final2_nn30 | NYIS | elliott | 2.75 | -0.47 | -1.37 | -3.18 | 5 |
| final2_nn30 | PJM | elliott | 4.32 | -2.87 | -3.16 | -6.39 | 5 |
| final2_nn30 | SWPP | elliott | 4.55 | 0.65 | -1.68 | -4.42 | 5 |
| final2_nn30 | TVA | elliott | 6.79 | 4.59 | 0.00 | 0.00 | 3 |
| final2_nn50 | BPAT | elliott | 3.79 | -2.61 | -2.97 | -6.76 | 5 |
| final2_nn50 | CISO | elliott | 3.17 | 2.14 | -0.44 | -2.21 | 5 |
| final2_nn50 | DUK | elliott | 3.09 | -1.24 | -1.51 | -4.41 | 4 |
| final2_nn50 | ERCO | elliott | 6.81 | -1.80 | -4.15 | -9.85 | 5 |
| final2_nn50 | ISNE | elliott | 3.56 | 1.72 | -0.67 | -2.16 | 5 |
| final2_nn50 | MISO | elliott | 3.44 | -1.45 | -2.57 | -4.04 | 5 |
| final2_nn50 | NYIS | elliott | 2.83 | -0.73 | -1.60 | -3.18 | 5 |
| final2_nn50 | PJM | elliott | 4.25 | -2.61 | -3.12 | -6.29 | 5 |
| final2_nn50 | SWPP | elliott | 4.40 | 0.21 | -1.86 | -5.23 | 5 |
| final2_nn50 | TVA | elliott | 6.69 | 4.72 | 0.00 | 0.00 | 3 |
| final2_ratio | BPAT | elliott | 4.87 | 0.55 | -1.59 | -4.04 | 5 |
| final2_ratio | CISO | elliott | 3.34 | 1.77 | -0.72 | -3.59 | 5 |
| final2_ratio | DUK | elliott | 4.67 | 0.09 | -1.75 | -4.98 | 4 |
| final2_ratio | ERCO | elliott | 7.11 | -0.85 | -3.77 | -10.21 | 5 |
| final2_ratio | ISNE | elliott | 3.53 | 1.94 | -0.70 | -1.84 | 5 |
| final2_ratio | MISO | elliott | 3.64 | -1.86 | -2.90 | -4.83 | 5 |
| final2_ratio | NYIS | elliott | 2.87 | -1.00 | -1.72 | -3.60 | 5 |
| final2_ratio | PJM | elliott | 4.63 | -2.84 | -3.63 | -8.43 | 5 |
| final2_ratio | SWPP | elliott | 6.29 | 1.75 | -1.61 | -4.34 | 5 |
| final2_ratio | TVA | elliott | 9.63 | 9.71 | 0.00 | 0.00 | 3 |
| final2_three | BPAT | elliott | 3.28 | -2.36 | -2.80 | -6.40 | 5 |
| final2_three | CISO | elliott | 3.53 | 3.08 | -0.28 | -1.41 | 5 |
| final2_three | DUK | elliott | 2.88 | -1.32 | -1.38 | -3.25 | 4 |
| final2_three | ERCO | elliott | 5.56 | -0.13 | -2.23 | -6.48 | 5 |
| final2_three | ISNE | elliott | 3.41 | 2.41 | -0.68 | -2.24 | 5 |
| final2_three | MISO | elliott | 3.63 | -2.61 | -3.39 | -6.72 | 5 |
| final2_three | NYIS | elliott | 2.82 | -1.12 | -1.78 | -4.13 | 5 |
| final2_three | PJM | elliott | 4.85 | -5.06 | -5.21 | -11.39 | 5 |
| final2_three | SWPP | elliott | 4.10 | 0.07 | -1.97 | -5.80 | 5 |
| final2_three | TVA | elliott | 5.82 | 4.86 | 0.00 | 0.00 | 3 |
| final_additive | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| final_additive | CISO | elliott | 3.53 | 4.14 | -0.08 | -0.41 | 5 |
| final_additive | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| final_additive | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
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
| final_ensemble | ISNE | elliott | 3.39 | 2.09 | -0.44 | -1.16 | 5 |
| final_ensemble | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| final_ensemble | NYIS | elliott | 2.73 | -1.04 | -1.83 | -3.53 | 5 |
| final_ensemble | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| final_ensemble | SWPP | elliott | 4.12 | -2.20 | -3.22 | -7.26 | 5 |
| final_ensemble | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |
| recency_ml | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| recency_ml | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| recency_ml | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| recency_ml | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| recency_ml | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| recency_ml | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| recency_ml | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| recency_ml | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| recency_ml | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| recency_ml | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | DF | eve | 3.27 | 0.98 | -1.10 |  | 245 |
| 25 | final2_three | eve | 3.30 | 1.03 | -1.35 | 0.44 | 245 |
| 19 | ens_three | eve | 3.31 | -0.01 | -1.81 | 0.45 | 245 |
| 17 | ens_hourly | eve | 3.43 | 0.38 | -1.66 | 0.44 | 245 |
| 23 | final2_nn50 | eve | 3.44 | 1.37 | -1.27 | 0.41 | 245 |
| 28 | final_ensemble | eve | 3.44 | 0.39 | -1.67 | 0.43 | 245 |
| 21 | final2_hourly | eve | 3.44 | 1.36 | -1.26 | 0.41 | 245 |
| 20 | final2 | eve | 3.44 | 1.37 | -1.27 | 0.41 | 245 |
| 22 | final2_nn30 | eve | 3.45 | 1.36 | -1.26 | 0.42 | 245 |
| 24 | final2_ratio | eve | 3.50 | 1.65 | -1.11 | 0.47 | 245 |
| 18 | ens_ratio | eve | 3.51 | 0.63 | -1.49 | 0.48 | 245 |
| 26 | final_additive | eve | 3.57 | 0.22 | -1.85 | 0.42 | 245 |
| 27 | final_boosting | eve | 3.69 | 0.55 | -1.66 | 0.41 | 245 |
| 16 | boosting_ratio | eve | 3.92 | 1.03 | -1.41 | 0.40 | 245 |
| 29 | recency_ml | eve | 3.97 | -0.95 | -2.48 | 0.33 | 245 |
| 7 | final2_nn30 | special | 3.31 | -0.10 | -1.79 | 0.50 | 247 |
| 5 | final2 | special | 3.31 | -0.13 | -1.81 | 0.49 | 247 |
| 6 | final2_hourly | special | 3.31 | -0.16 | -1.82 | 0.49 | 247 |
| 8 | final2_nn50 | special | 3.31 | -0.15 | -1.81 | 0.49 | 247 |
| 10 | final2_three | special | 3.32 | -0.26 | -1.92 | 0.49 | 247 |
| 2 | ens_hourly | special | 3.36 | -1.15 | -2.40 | 0.49 | 247 |
| 13 | final_ensemble | special | 3.37 | -1.15 | -2.40 | 0.50 | 247 |
| 4 | ens_three | special | 3.39 | -1.30 | -2.57 | 0.50 | 247 |
| 9 | final2_ratio | special | 3.45 | -0.07 | -1.82 | 0.49 | 247 |
| 3 | ens_ratio | special | 3.52 | -1.09 | -2.39 | 0.51 | 247 |
| 11 | final_additive | special | 3.55 | -1.44 | -2.69 | 0.46 | 247 |
| 0 | DF | special | 3.57 | 0.31 | -1.46 |  | 247 |
| 12 | final_boosting | special | 3.67 | -0.87 | -2.31 | 0.43 | 247 |
| 1 | boosting_ratio | special | 4.01 | -0.78 | -2.41 | 0.43 | 247 |
| 14 | recency_ml | special | 4.20 | -1.70 | -3.15 | 0.38 | 247 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.391 | 1.353 | 0.401 | 0.889 | 11.801 | 0.888 | 7248 |
| final2_hourly | all | 0.390 | 1.350 | 0.400 | 0.889 | 11.783 | 0.889 | 7248 |
| final2_nn30 | all | 0.396 | 1.358 | 0.403 | 0.886 | 11.800 | 0.886 | 7248 |
| final2_nn50 | all | 0.386 | 1.351 | 0.398 | 0.891 | 11.776 | 0.891 | 7248 |
| final2_ratio | all | 0.401 | 1.370 | 0.400 | 0.889 | 11.895 | 0.893 | 7248 |
| final2_three | all | 0.382 | 1.330 | 0.394 | 0.888 | 11.586 | 0.889 | 7248 |
| final2 | events | 0.496 | 1.790 | 0.521 | 0.807 | 12.313 | 0.840 | 100 |
| final2_hourly | events | 0.496 | 1.786 | 0.521 | 0.808 | 12.289 | 0.830 | 100 |
| final2_nn30 | events | 0.492 | 1.797 | 0.509 | 0.813 | 12.472 | 0.850 | 100 |
| final2_nn50 | events | 0.477 | 1.781 | 0.534 | 0.811 | 12.194 | 0.830 | 100 |
| final2_ratio | events | 0.691 | 1.976 | 0.546 | 0.772 | 12.268 | 0.800 | 100 |
| final2_three | events | 0.447 | 1.770 | 0.567 | 0.795 | 12.073 | 0.790 | 100 |
| final2 | cold_mornings | 0.457 | 1.630 | 0.477 | 0.844 | 12.709 | 0.807 | 300 |
| final2_hourly | cold_mornings | 0.455 | 1.627 | 0.475 | 0.845 | 12.685 | 0.813 | 300 |
| final2_nn30 | cold_mornings | 0.463 | 1.618 | 0.479 | 0.845 | 12.877 | 0.823 | 300 |
| final2_nn50 | cold_mornings | 0.445 | 1.628 | 0.479 | 0.840 | 12.442 | 0.800 | 300 |
| final2_ratio | cold_mornings | 0.528 | 1.717 | 0.505 | 0.836 | 12.954 | 0.810 | 300 |
| final2_three | cold_mornings | 0.440 | 1.611 | 0.504 | 0.841 | 12.673 | 0.807 | 300 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 33464 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 33452 | DUK | 2022-12-24 | boosting_ratio | 12.17 | -19.04 | -19.04 |
| 33455 | DUK | 2022-12-24 | ens_hourly | 8.30 | -14.27 | -14.27 |
| 33457 | DUK | 2022-12-24 | ens_ratio | 9.59 | -15.69 | -15.69 |
| 33456 | DUK | 2022-12-24 | ens_three | 8.58 | -12.82 | -12.82 |
| 33458 | DUK | 2022-12-24 | final2 | 8.29 | -11.33 | -11.33 |
| 33459 | DUK | 2022-12-24 | final2_hourly | 8.31 | -11.45 | -11.45 |
| 33462 | DUK | 2022-12-24 | final2_nn30 | 8.54 | -12.39 | -12.39 |
| 33463 | DUK | 2022-12-24 | final2_nn50 | 8.53 | -11.67 | -11.67 |
| 33461 | DUK | 2022-12-24 | final2_ratio | 9.75 | -12.90 | -12.90 |
| 33460 | DUK | 2022-12-24 | final2_three | 8.42 | -9.33 | -9.33 |
| 33450 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 33451 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 33454 | DUK | 2022-12-24 | final_ensemble | 8.26 | -14.16 | -14.16 |
| 33453 | DUK | 2022-12-24 | recency_ml | 9.27 | -9.99 | -9.99 |
| 34694 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 34682 | ERCO | 2021-02-17 | boosting_ratio | 24.56 | 21.74 | 0.00 |
| 34685 | ERCO | 2021-02-17 | ens_hourly | 30.26 | 26.94 | 0.00 |
| 34687 | ERCO | 2021-02-17 | ens_ratio | 27.89 | 25.49 | 0.00 |
| 34686 | ERCO | 2021-02-17 | ens_three | 33.18 | 29.45 | 0.00 |
| 34688 | ERCO | 2021-02-17 | final2 | 29.35 | 23.99 | 0.00 |
| 34689 | ERCO | 2021-02-17 | final2_hourly | 29.33 | 24.10 | 0.00 |
| 34692 | ERCO | 2021-02-17 | final2_nn30 | 29.10 | 23.90 | 0.00 |
| 34693 | ERCO | 2021-02-17 | final2_nn50 | 29.36 | 24.31 | 0.00 |
| 34691 | ERCO | 2021-02-17 | final2_ratio | 27.31 | 22.95 | 0.00 |
| 34690 | ERCO | 2021-02-17 | final2_three | 32.00 | 26.01 | 0.00 |
| 34680 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 34681 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 34684 | ERCO | 2021-02-17 | final_ensemble | 30.28 | 26.83 | 0.00 |
| 34683 | ERCO | 2021-02-17 | recency_ml | 41.20 | 36.68 | 0.00 |
| 34709 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 34697 | ERCO | 2021-02-18 | boosting_ratio | 8.32 | 3.26 | 0.00 |
| 34700 | ERCO | 2021-02-18 | ens_hourly | 7.68 | 4.17 | 0.00 |
| 34702 | ERCO | 2021-02-18 | ens_ratio | 10.67 | 7.68 | 0.00 |
| 34701 | ERCO | 2021-02-18 | ens_three | 7.02 | 3.89 | 0.00 |
| 34703 | ERCO | 2021-02-18 | final2 | 7.05 | 5.55 | 0.00 |
| 34704 | ERCO | 2021-02-18 | final2_hourly | 7.00 | 5.25 | 0.00 |
| 34707 | ERCO | 2021-02-18 | final2_nn30 | 6.76 | 5.53 | 0.00 |
| 34708 | ERCO | 2021-02-18 | final2_nn50 | 6.81 | 5.24 | 0.00 |
| 34706 | ERCO | 2021-02-18 | final2_ratio | 10.27 | 9.25 | 0.00 |
| 34705 | ERCO | 2021-02-18 | final2_three | 6.09 | 4.64 | 0.00 |
| 34695 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 34696 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 34699 | ERCO | 2021-02-18 | final_ensemble | 7.68 | 4.44 | 0.00 |
| 34698 | ERCO | 2021-02-18 | recency_ml | 5.36 | 2.19 | 0.00 |
| 57209 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 57197 | MISO | 2021-02-16 | boosting_ratio | 1.35 | -1.49 | -1.49 |
| 57200 | MISO | 2021-02-16 | ens_hourly | 2.19 | 1.54 | 0.00 |
| 57202 | MISO | 2021-02-16 | ens_ratio | 1.73 | 0.20 | 0.00 |
| 57201 | MISO | 2021-02-16 | ens_three | 1.67 | 0.50 | 0.00 |
| 57203 | MISO | 2021-02-16 | final2 | 2.57 | 2.89 | 0.00 |
| 57204 | MISO | 2021-02-16 | final2_hourly | 2.55 | 3.00 | 0.00 |
| 57207 | MISO | 2021-02-16 | final2_nn30 | 2.42 | 2.69 | 0.00 |
| 57208 | MISO | 2021-02-16 | final2_nn50 | 2.40 | 2.77 | 0.00 |
| 57206 | MISO | 2021-02-16 | final2_ratio | 2.46 | 2.13 | 0.00 |
| 57205 | MISO | 2021-02-16 | final2_three | 1.88 | 2.37 | 0.00 |
| 57195 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 57196 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 57199 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 57198 | MISO | 2021-02-16 | recency_ml | 3.61 | -2.07 | -2.07 |
| 90839 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 90827 | SWPP | 2021-02-15 | boosting_ratio | 3.66 | -5.10 | -5.10 |
| 90830 | SWPP | 2021-02-15 | ens_hourly | 2.18 | -3.13 | -3.13 |
| 90832 | SWPP | 2021-02-15 | ens_ratio | 1.98 | -1.99 | -1.99 |
| 90831 | SWPP | 2021-02-15 | ens_three | 2.87 | -3.86 | -3.86 |
| 90833 | SWPP | 2021-02-15 | final2 | 1.83 | -1.71 | -1.71 |
| 90834 | SWPP | 2021-02-15 | final2_hourly | 1.80 | -1.60 | -1.60 |
| 90837 | SWPP | 2021-02-15 | final2_nn30 | 2.15 | -1.88 | -1.88 |
| 90838 | SWPP | 2021-02-15 | final2_nn50 | 1.81 | -1.57 | -1.57 |
| 90836 | SWPP | 2021-02-15 | final2_ratio | 1.85 | -0.30 | -0.30 |
| 90835 | SWPP | 2021-02-15 | final2_three | 2.87 | -2.68 | -2.68 |
| 90825 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 90826 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 90829 | SWPP | 2021-02-15 | final_ensemble | 2.21 | -3.25 | -3.25 |
| 90828 | SWPP | 2021-02-15 | recency_ml | 4.81 | -5.28 | -5.28 |
| 90854 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 90842 | SWPP | 2021-02-16 | boosting_ratio | 6.71 | 0.43 | 0.00 |
| 90845 | SWPP | 2021-02-16 | ens_hourly | 5.60 | -1.84 | -1.84 |
| 90847 | SWPP | 2021-02-16 | ens_ratio | 7.15 | 1.88 | 0.00 |
| 90846 | SWPP | 2021-02-16 | ens_three | 4.30 | -1.01 | -1.01 |
| 90848 | SWPP | 2021-02-16 | final2 | 6.21 | -0.62 | -0.62 |
| 90849 | SWPP | 2021-02-16 | final2_hourly | 6.31 | -1.09 | -1.09 |
| 90852 | SWPP | 2021-02-16 | final2_nn30 | 6.90 | -0.60 | -0.60 |
| 90853 | SWPP | 2021-02-16 | final2_nn50 | 5.97 | -0.03 | -0.03 |
| 90851 | SWPP | 2021-02-16 | final2_ratio | 7.84 | 3.01 | 0.00 |
| 90850 | SWPP | 2021-02-16 | final2_three | 4.50 | -0.41 | -0.41 |
| 90840 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 90841 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 90844 | SWPP | 2021-02-16 | final_ensemble | 5.49 | -1.39 | -1.39 |
| 90843 | SWPP | 2021-02-16 | recency_ml | 2.57 | -0.10 | -0.10 |
| 111914 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 111902 | TVA | 2022-12-23 | boosting_ratio | 13.51 | -16.88 | -16.88 |
| 111905 | TVA | 2022-12-23 | ens_hourly | 9.59 | -10.09 | -10.09 |
| 111907 | TVA | 2022-12-23 | ens_ratio | 9.54 | -11.02 | -11.02 |
| 111906 | TVA | 2022-12-23 | ens_three | 8.36 | -10.13 | -10.13 |
| 111908 | TVA | 2022-12-23 | final2 | 10.26 | -11.56 | -11.56 |
| 111909 | TVA | 2022-12-23 | final2_hourly | 10.30 | -11.56 | -11.56 |
| 111912 | TVA | 2022-12-23 | final2_nn30 | 9.94 | -11.25 | -11.25 |
| 111913 | TVA | 2022-12-23 | final2_nn50 | 10.29 | -11.61 | -11.61 |
| 111911 | TVA | 2022-12-23 | final2_ratio | 9.90 | -12.17 | -12.17 |
| 111910 | TVA | 2022-12-23 | final2_three | 8.86 | -11.81 | -11.81 |
| 111900 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 111901 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 111904 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 111903 | TVA | 2022-12-23 | recency_ml | 11.83 | -10.22 | -10.22 |
| 111929 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 111917 | TVA | 2022-12-24 | boosting_ratio | 5.92 | -15.66 | -15.66 |
| 111920 | TVA | 2022-12-24 | ens_hourly | 4.68 | -10.60 | -10.60 |
| 111922 | TVA | 2022-12-24 | ens_ratio | 4.53 | -12.13 | -12.13 |
| 111921 | TVA | 2022-12-24 | ens_three | 5.34 | -10.90 | -10.90 |
| 111923 | TVA | 2022-12-24 | final2 | 4.45 | -11.23 | -11.23 |
| 111924 | TVA | 2022-12-24 | final2_hourly | 4.45 | -11.15 | -11.15 |
| 111927 | TVA | 2022-12-24 | final2_nn30 | 4.25 | -11.23 | -11.23 |
| 111928 | TVA | 2022-12-24 | final2_nn50 | 4.54 | -11.29 | -11.29 |
| 111926 | TVA | 2022-12-24 | final2_ratio | 4.18 | -13.29 | -13.29 |
| 111925 | TVA | 2022-12-24 | final2_three | 5.12 | -10.46 | -10.46 |
| 111915 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 111916 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 111919 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |
| 111918 | TVA | 2022-12-24 | recency_ml | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| boosting_ratio | BPAT | mape | 12.863 | 0.000 | 750 |
| boosting_ratio | CISO | mape | 10.773 | 0.000 | 737 |
| boosting_ratio | DUK | mape | 10.506 | 0.000 | 750 |
| boosting_ratio | ERCO | mape | 8.720 | 0.000 | 746 |
| boosting_ratio | ISNE | mape | 19.017 | 0.000 | 752 |
| boosting_ratio | MISO | mape | -3.785 | 0.000 | 746 |
| boosting_ratio | NYIS | mape | 1.677 | 0.094 | 752 |
| boosting_ratio | PJM | mape | 7.508 | 0.000 | 744 |
| boosting_ratio | SWPP | mape | -10.594 | 0.000 | 745 |
| boosting_ratio | TVA | mape | 16.651 | 0.000 | 739 |
| ens_hourly | BPAT | mape | 9.664 | 0.000 | 750 |
| ens_hourly | CISO | mape | 9.729 | 0.000 | 737 |
| ens_hourly | DUK | mape | 8.414 | 0.000 | 750 |
| ens_hourly | ERCO | mape | 6.776 | 0.000 | 746 |
| ens_hourly | ISNE | mape | 17.242 | 0.000 | 752 |
| ens_hourly | MISO | mape | -6.211 | 0.000 | 746 |
| ens_hourly | NYIS | mape | -3.041 | 0.002 | 752 |
| ens_hourly | PJM | mape | 2.510 | 0.012 | 744 |
| ens_hourly | SWPP | mape | -15.337 | 0.000 | 745 |
| ens_hourly | TVA | mape | 14.640 | 0.000 | 739 |
| ens_ratio | BPAT | mape | 10.140 | 0.000 | 750 |
| ens_ratio | CISO | mape | 10.398 | 0.000 | 737 |
| ens_ratio | DUK | mape | 8.529 | 0.000 | 750 |
| ens_ratio | ERCO | mape | 7.735 | 0.000 | 746 |
| ens_ratio | ISNE | mape | 17.362 | 0.000 | 752 |
| ens_ratio | MISO | mape | -6.126 | 0.000 | 746 |
| ens_ratio | NYIS | mape | -2.193 | 0.028 | 752 |
| ens_ratio | PJM | mape | 3.382 | 0.001 | 744 |
| ens_ratio | SWPP | mape | -15.086 | 0.000 | 745 |
| ens_ratio | TVA | mape | 14.950 | 0.000 | 739 |
| ens_three | BPAT | mape | 9.293 | 0.000 | 750 |
| ens_three | CISO | mape | 13.381 | 0.000 | 737 |
| ens_three | DUK | mape | 8.240 | 0.000 | 750 |
| ens_three | ERCO | mape | 7.086 | 0.000 | 746 |
| ens_three | ISNE | mape | 19.301 | 0.000 | 752 |
| ens_three | MISO | mape | -5.746 | 0.000 | 746 |
| ens_three | NYIS | mape | -2.885 | 0.004 | 752 |
| ens_three | PJM | mape | 2.281 | 0.023 | 744 |
| ens_three | SWPP | mape | -16.634 | 0.000 | 745 |
| ens_three | TVA | mape | 14.569 | 0.000 | 739 |
| final2 | BPAT | mape | 8.954 | 0.000 | 750 |
| final2 | CISO | mape | 3.258 | 0.001 | 737 |
| final2 | DUK | mape | 7.740 | 0.000 | 750 |
| final2 | ERCO | mape | 2.537 | 0.011 | 746 |
| final2 | ISNE | mape | 15.636 | 0.000 | 752 |
| final2 | MISO | mape | -8.862 | 0.000 | 746 |
| final2 | NYIS | mape | -2.877 | 0.004 | 752 |
| final2 | PJM | mape | -3.041 | 0.002 | 744 |
| final2 | SWPP | mape | -16.355 | 0.000 | 745 |
| final2 | TVA | mape | 13.923 | 0.000 | 739 |
| final2_hourly | BPAT | mape | 8.933 | 0.000 | 750 |
| final2_hourly | CISO | mape | 3.028 | 0.002 | 737 |
| final2_hourly | DUK | mape | 7.667 | 0.000 | 750 |
| final2_hourly | ERCO | mape | 2.507 | 0.012 | 746 |
| final2_hourly | ISNE | mape | 15.515 | 0.000 | 752 |
| final2_hourly | MISO | mape | -8.923 | 0.000 | 746 |
| final2_hourly | NYIS | mape | -2.972 | 0.003 | 752 |
| final2_hourly | PJM | mape | -3.118 | 0.002 | 744 |
| final2_hourly | SWPP | mape | -16.413 | 0.000 | 745 |
| final2_hourly | TVA | mape | 13.858 | 0.000 | 739 |
| final2_nn30 | BPAT | mape | 9.046 | 0.000 | 750 |
| final2_nn30 | CISO | mape | 3.341 | 0.001 | 737 |
| final2_nn30 | DUK | mape | 7.794 | 0.000 | 750 |
| final2_nn30 | ERCO | mape | 2.522 | 0.012 | 746 |
| final2_nn30 | ISNE | mape | 15.768 | 0.000 | 752 |
| final2_nn30 | MISO | mape | -8.862 | 0.000 | 746 |
| final2_nn30 | NYIS | mape | -2.619 | 0.009 | 752 |
| final2_nn30 | PJM | mape | -2.925 | 0.003 | 744 |
| final2_nn30 | SWPP | mape | -16.292 | 0.000 | 745 |
| final2_nn30 | TVA | mape | 14.117 | 0.000 | 739 |
| final2_nn50 | BPAT | mape | 8.887 | 0.000 | 750 |
| final2_nn50 | CISO | mape | 3.260 | 0.001 | 737 |
| final2_nn50 | DUK | mape | 7.416 | 0.000 | 750 |
| final2_nn50 | ERCO | mape | 2.705 | 0.007 | 746 |
| final2_nn50 | ISNE | mape | 15.710 | 0.000 | 752 |
| final2_nn50 | MISO | mape | -9.041 | 0.000 | 746 |
| final2_nn50 | NYIS | mape | -3.108 | 0.002 | 752 |
| final2_nn50 | PJM | mape | -2.918 | 0.004 | 744 |
| final2_nn50 | SWPP | mape | -16.459 | 0.000 | 745 |
| final2_nn50 | TVA | mape | 13.943 | 0.000 | 739 |
| final2_ratio | BPAT | mape | 8.931 | 0.000 | 750 |
| final2_ratio | CISO | mape | 3.708 | 0.000 | 737 |
| final2_ratio | DUK | mape | 7.923 | 0.000 | 750 |
| final2_ratio | ERCO | mape | 4.041 | 0.000 | 746 |
| final2_ratio | ISNE | mape | 15.794 | 0.000 | 752 |
| final2_ratio | MISO | mape | -8.700 | 0.000 | 746 |
| final2_ratio | NYIS | mape | -2.256 | 0.024 | 752 |
| final2_ratio | PJM | mape | -2.046 | 0.041 | 744 |
| final2_ratio | SWPP | mape | -16.102 | 0.000 | 745 |
| final2_ratio | TVA | mape | 14.024 | 0.000 | 739 |
| final2_three | BPAT | mape | 8.205 | 0.000 | 750 |
| final2_three | CISO | mape | 1.894 | 0.058 | 737 |
| final2_three | DUK | mape | 7.331 | 0.000 | 750 |
| final2_three | ERCO | mape | 1.778 | 0.075 | 746 |
| final2_three | ISNE | mape | 15.645 | 0.000 | 752 |
| final2_three | MISO | mape | -9.285 | 0.000 | 746 |
| final2_three | NYIS | mape | -3.764 | 0.000 | 752 |
| final2_three | PJM | mape | -3.577 | 0.000 | 744 |
| final2_three | SWPP | mape | -17.705 | 0.000 | 745 |
| final2_three | TVA | mape | 13.397 | 0.000 | 739 |
| final_additive | BPAT | mape | 12.541 | 0.000 | 750 |
| final_additive | CISO | mape | 17.909 | 0.000 | 737 |
| final_additive | DUK | mape | 10.152 | 0.000 | 750 |
| final_additive | ERCO | mape | 11.907 | 0.000 | 746 |
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
| final_ensemble | ISNE | mape | 17.396 | 0.000 | 752 |
| final_ensemble | MISO | mape | -6.116 | 0.000 | 746 |
| final_ensemble | NYIS | mape | -2.860 | 0.004 | 752 |
| final_ensemble | PJM | mape | 2.785 | 0.005 | 744 |
| final_ensemble | SWPP | mape | -15.252 | 0.000 | 745 |
| final_ensemble | TVA | mape | 14.766 | 0.000 | 739 |
| recency_ml | BPAT | mape | 17.478 | 0.000 | 750 |
| recency_ml | CISO | mape | 37.390 | 0.000 | 737 |
| recency_ml | DUK | mape | 14.132 | 0.000 | 750 |
| recency_ml | ERCO | mape | 13.167 | 0.000 | 746 |
| recency_ml | ISNE | mape | 36.416 | 0.000 | 752 |
| recency_ml | MISO | mape | 3.503 | 0.000 | 746 |
| recency_ml | NYIS | mape | 10.210 | 0.000 | 752 |
| recency_ml | PJM | mape | 10.791 | 0.000 | 744 |
| recency_ml | SWPP | mape | -9.681 | 0.000 | 745 |
| recency_ml | TVA | mape | 20.636 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.996 |
| boosting_ratio | 0.992 |
| ens_hourly | 0.992 |
| ens_ratio | 0.992 |
| ens_three | 0.992 |
| final2 | 0.992 |
| final2_hourly | 0.992 |
| final2_nn30 | 0.992 |
| final2_nn50 | 0.992 |
| final2_ratio | 0.992 |
| final2_three | 0.992 |
| final_additive | 0.983 |
| final_boosting | 0.992 |
| final_ensemble | 0.992 |
| recency_ml | 0.992 |
