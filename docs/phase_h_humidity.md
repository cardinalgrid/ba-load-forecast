# Phase H: humidity and wind

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final3_hw` is the phase G recipe with the dew point, dew-point depression, relative humidity, heat index, wind speed and wind chill (NWS formulas) as features of the boosting and the apparent temperature as the input of the additive model's smooth response; `h_boosting` and `w_boosting` add one block at a time to the phase G boosting. Observed dew point and wind from ISD-Lite and the supplements, forecasts from the HRRR archive. Compare with `docs/phase_g_final.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_hw | 2.40 | 2.08 | -0.02 | -1.32 | 1.24 | 0.57 | 0.30 | -46.49 | 8056 | 11.00 |
| DF | 2.69 | 2.40 | 0.36 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8056 | 11.00 |
| final3_hw_ensemble | 2.74 | 2.42 | -1.45 | -2.22 | 1.27 | 0.50 | 0.23 | -50.91 | 8056 | 11.00 |
| final3_hw_boosting | 2.83 | 2.50 | -1.00 | -2.01 | 1.40 | 0.46 | 0.25 | -51.31 | 8056 | 11.00 |
| h_boosting | 2.83 | 2.49 | -0.97 | -2.00 | 1.42 | 0.45 | 0.25 | -51.51 | 8056 | 11.00 |
| w_boosting | 2.91 | 2.57 | -1.00 | -2.07 | 1.39 | 0.44 | 0.25 | -52.14 | 8056 | 11.00 |
| final3_hw_additive | 3.01 | 2.65 | -1.76 | -2.57 | 1.32 | 0.43 | 0.20 | -49.24 | 8056 | 11.00 |
| final3_hw_recency | 3.66 | 3.29 | -1.71 | -2.74 | 1.60 | 0.32 | 0.22 | -52.57 | 8056 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.06 | 1.80 | 0.20 | -0.95 | 1.45 | -19.35 |  |  | 746 | 6536.52 |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.24 | -6.72 |  |  | 719 | 25193.76 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | ERCO | 2.62 | 2.11 | 0.51 | -1.11 | 0.81 | -14.36 |  |  | 742 | 46834.59 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.04 | 1.17 | -47.43 |  |  | 665 | 15346.05 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 748 | 13403.92 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 738 | 73700.16 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.67 | 0.40 | -12.87 |  |  | 748 | 17415.28 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| DF | TVA | 2.23 | 1.92 | -0.14 | -1.23 | 0.98 | -11.24 |  |  | 729 | 18581.23 |
| final3_hw | BPAT | 2.48 | 2.14 | -0.47 | -1.50 | 1.76 | -17.80 | 0.38 | 0.25 | 746 | 6536.52 |
| final3_hw | CISO | 2.44 | 2.13 | 0.34 | -1.13 | 0.34 | -12.72 | 0.50 | 0.26 | 719 | 25193.76 |
| final3_hw | DUK | 3.22 | 2.94 | -0.02 | -1.78 | 1.37 | -15.23 | 0.40 | 0.31 | 746 | 12143.29 |
| final3_hw | ERCO | 2.60 | 2.19 | -0.00 | -1.42 | 1.02 | -13.73 | 0.49 | 0.29 | 742 | 46834.59 |
| final3_hw | FPL | 3.64 | 3.18 | -0.81 | -2.57 | 1.02 | -46.49 | 0.59 | 0.65 | 665 | 15346.05 |
| final3_hw | ISNE | 3.21 | 2.83 | 0.37 | -1.29 | 0.52 | -15.56 | 0.34 | 0.21 | 748 | 13403.92 |
| final3_hw | MISO | 2.02 | 1.76 | 0.07 | -1.03 | 1.63 | -7.40 | 0.63 | 0.07 | 738 | 73700.16 |
| final3_hw | NYIS | 2.26 | 1.94 | -0.01 | -1.29 | 0.57 | -12.61 | 0.62 | 0.72 | 748 | 17415.28 |
| final3_hw | PJM | 2.16 | 1.90 | -0.06 | -1.24 | 1.45 | -11.03 | 0.61 | 0.43 | 734 | 92076.14 |
| final3_hw | SWPP | 2.17 | 1.82 | -0.24 | -1.32 | 1.35 | -20.04 | 0.75 | 0.11 | 741 | 31382.01 |
| final3_hw | TVA | 2.84 | 2.45 | 0.28 | -1.44 | 1.33 | -13.85 | 0.33 | 0.33 | 729 | 18581.23 |
| final3_hw_additive | BPAT | 2.79 | 2.48 | -0.83 | -1.83 | 1.92 | -15.83 | 0.29 | 0.22 | 746 | 6536.52 |
| final3_hw_additive | CISO | 3.64 | 3.06 | -2.98 | -3.84 | 0.46 | -18.34 | 0.27 | 0.13 | 719 | 25193.76 |
| final3_hw_additive | DUK | 3.59 | 3.05 | -0.99 | -2.46 | 1.41 | -16.06 | 0.36 | 0.27 | 746 | 12143.29 |
| final3_hw_additive | ERCO | 3.62 | 3.23 | -2.58 | -3.32 | 1.06 | -16.22 | 0.29 | 0.15 | 742 | 46834.59 |
| final3_hw_additive | FPL | 6.16 | 5.69 | -6.19 | -6.70 | 1.07 | -49.24 | 0.27 | 0.25 | 665 | 15346.05 |
| final3_hw_additive | ISNE | 3.72 | 3.31 | -1.53 | -2.57 | 0.55 | -21.21 | 0.24 | 0.15 | 748 | 13403.92 |
| final3_hw_additive | MISO | 2.33 | 2.03 | -1.26 | -1.87 | 1.64 | -8.53 | 0.54 | 0.05 | 738 | 73700.16 |
| final3_hw_additive | NYIS | 2.60 | 2.22 | -1.01 | -2.06 | 0.54 | -15.44 | 0.56 | 0.59 | 748 | 17415.28 |
| final3_hw_additive | PJM | 2.64 | 2.36 | -1.19 | -2.04 | 1.58 | -12.12 | 0.45 | 0.32 | 734 | 92076.14 |
| final3_hw_additive | SWPP | 2.39 | 2.00 | -1.29 | -2.04 | 1.41 | -21.15 | 0.71 | 0.07 | 741 | 31382.01 |
| final3_hw_additive | TVA | 3.29 | 2.88 | -1.64 | -2.66 | 1.63 | -17.38 | 0.26 | 0.22 | 729 | 18581.23 |
| final3_hw_boosting | BPAT | 2.64 | 2.38 | -0.57 | -1.65 | 1.95 | -17.45 | 0.30 | 0.24 | 746 | 6536.52 |
| final3_hw_boosting | CISO | 2.89 | 2.58 | -1.99 | -2.57 | 0.42 | -16.56 | 0.37 | 0.16 | 719 | 25193.76 |
| final3_hw_boosting | DUK | 3.35 | 2.93 | -0.89 | -2.32 | 1.46 | -18.54 | 0.36 | 0.27 | 746 | 12143.29 |
| final3_hw_boosting | ERCO | 2.96 | 2.56 | -2.35 | -2.94 | 1.28 | -19.79 | 0.38 | 0.17 | 742 | 46834.59 |
| final3_hw_boosting | FPL | 6.07 | 5.69 | -6.47 | -6.84 | 1.28 | -51.31 | 0.21 | 0.27 | 665 | 15346.05 |
| final3_hw_boosting | ISNE | 3.45 | 3.12 | -0.27 | -1.57 | 0.54 | -17.19 | 0.30 | 0.19 | 748 | 13403.92 |
| final3_hw_boosting | MISO | 2.25 | 1.96 | -0.50 | -1.37 | 1.61 | -9.73 | 0.57 | 0.06 | 738 | 73700.16 |
| final3_hw_boosting | NYIS | 2.52 | 2.22 | -0.17 | -1.32 | 0.69 | -10.62 | 0.54 | 0.72 | 748 | 17415.28 |
| final3_hw_boosting | PJM | 2.64 | 2.39 | 0.13 | -1.29 | 1.71 | -11.82 | 0.45 | 0.44 | 734 | 92076.14 |
| final3_hw_boosting | SWPP | 2.49 | 2.10 | -1.14 | -2.08 | 1.52 | -29.02 | 0.70 | 0.07 | 741 | 31382.01 |
| final3_hw_boosting | TVA | 3.08 | 2.61 | -0.58 | -1.88 | 1.59 | -13.00 | 0.29 | 0.27 | 729 | 18581.23 |
| final3_hw_ensemble | BPAT | 2.50 | 2.23 | -0.87 | -1.72 | 1.78 | -17.43 | 0.37 | 0.23 | 746 | 6536.52 |
| final3_hw_ensemble | CISO | 3.23 | 2.76 | -2.85 | -3.33 | 0.36 | -17.03 | 0.35 | 0.12 | 719 | 25193.76 |
| final3_hw_ensemble | DUK | 3.25 | 2.81 | -0.85 | -2.24 | 1.35 | -15.23 | 0.42 | 0.26 | 746 | 12143.29 |
| final3_hw_ensemble | ERCO | 3.07 | 2.63 | -2.52 | -3.05 | 1.09 | -14.54 | 0.38 | 0.16 | 742 | 46834.59 |
| final3_hw_ensemble | FPL | 6.35 | 5.99 | -7.01 | -7.32 | 1.07 | -50.91 | 0.22 | 0.23 | 665 | 15346.05 |
| final3_hw_ensemble | ISNE | 3.40 | 3.08 | -1.33 | -2.18 | 0.51 | -17.60 | 0.27 | 0.14 | 748 | 13403.92 |
| final3_hw_ensemble | MISO | 2.15 | 1.89 | -0.96 | -1.57 | 1.65 | -8.12 | 0.60 | 0.05 | 738 | 73700.16 |
| final3_hw_ensemble | NYIS | 2.32 | 2.03 | -0.54 | -1.53 | 0.54 | -13.64 | 0.59 | 0.68 | 748 | 17415.28 |
| final3_hw_ensemble | PJM | 2.40 | 2.18 | -0.55 | -1.52 | 1.50 | -10.50 | 0.55 | 0.40 | 734 | 92076.14 |
| final3_hw_ensemble | SWPP | 2.16 | 1.77 | -0.91 | -1.70 | 1.36 | -20.07 | 0.74 | 0.08 | 741 | 31382.01 |
| final3_hw_ensemble | TVA | 2.95 | 2.52 | -1.09 | -2.15 | 1.40 | -14.10 | 0.31 | 0.25 | 729 | 18581.23 |
| final3_hw_recency | BPAT | 3.19 | 2.83 | -1.37 | -2.22 | 1.96 | -18.92 | 0.22 | 0.20 | 746 | 6536.52 |
| final3_hw_recency | CISO | 5.63 | 5.36 | -4.46 | -4.93 | 0.59 | -18.26 | 0.06 | 0.08 | 719 | 25193.76 |
| final3_hw_recency | DUK | 3.90 | 3.51 | -0.50 | -2.47 | 1.63 | -15.94 | 0.29 | 0.26 | 746 | 12143.29 |
| final3_hw_recency | ERCO | 3.72 | 3.28 | -2.74 | -3.47 | 1.17 | -19.79 | 0.29 | 0.18 | 742 | 46834.59 |
| final3_hw_recency | FPL | 7.72 | 7.07 | -8.87 | -9.18 | 1.26 | -52.57 | 0.17 | 0.18 | 665 | 15346.05 |
| final3_hw_recency | ISNE | 5.23 | 4.92 | -2.67 | -3.42 | 0.68 | -20.32 | 0.06 | 0.10 | 748 | 13403.92 |
| final3_hw_recency | MISO | 2.93 | 2.60 | -1.23 | -1.99 | 2.17 | -14.05 | 0.42 | 0.05 | 738 | 73700.16 |
| final3_hw_recency | NYIS | 3.44 | 3.04 | -0.48 | -1.83 | 0.84 | -18.20 | 0.36 | 0.64 | 748 | 17415.28 |
| final3_hw_recency | PJM | 3.09 | 2.74 | -0.59 | -1.85 | 1.93 | -19.85 | 0.32 | 0.37 | 734 | 92076.14 |
| final3_hw_recency | SWPP | 2.90 | 2.47 | -0.16 | -1.61 | 1.71 | -17.99 | 0.60 | 0.10 | 741 | 31382.01 |
| final3_hw_recency | TVA | 3.57 | 3.27 | -1.01 | -2.54 | 1.52 | -15.53 | 0.20 | 0.24 | 729 | 18581.23 |
| h_boosting | BPAT | 2.66 | 2.41 | -0.52 | -1.60 | 1.99 | -17.63 | 0.30 | 0.25 | 746 | 6536.52 |
| h_boosting | CISO | 2.89 | 2.58 | -1.91 | -2.52 | 0.44 | -16.09 | 0.37 | 0.15 | 719 | 25193.76 |
| h_boosting | DUK | 3.32 | 2.90 | -0.97 | -2.34 | 1.40 | -18.14 | 0.37 | 0.26 | 746 | 12143.29 |
| h_boosting | ERCO | 2.96 | 2.55 | -2.43 | -2.97 | 1.33 | -19.98 | 0.36 | 0.16 | 742 | 46834.59 |
| h_boosting | FPL | 6.03 | 5.61 | -6.48 | -6.83 | 1.30 | -51.51 | 0.21 | 0.28 | 665 | 15346.05 |
| h_boosting | ISNE | 3.44 | 3.09 | -0.22 | -1.52 | 0.53 | -16.39 | 0.29 | 0.19 | 748 | 13403.92 |
| h_boosting | MISO | 2.24 | 1.92 | -0.45 | -1.33 | 1.64 | -9.61 | 0.57 | 0.06 | 738 | 73700.16 |
| h_boosting | NYIS | 2.56 | 2.27 | -0.12 | -1.32 | 0.74 | -11.42 | 0.53 | 0.73 | 748 | 17415.28 |
| h_boosting | PJM | 2.66 | 2.40 | 0.19 | -1.28 | 1.72 | -13.24 | 0.44 | 0.43 | 734 | 92076.14 |
| h_boosting | SWPP | 2.52 | 2.05 | -1.10 | -2.04 | 1.59 | -29.46 | 0.70 | 0.08 | 741 | 31382.01 |
| h_boosting | TVA | 3.08 | 2.64 | -0.60 | -1.91 | 1.50 | -12.10 | 0.30 | 0.27 | 729 | 18581.23 |
| w_boosting | BPAT | 2.65 | 2.42 | -0.49 | -1.61 | 2.01 | -18.10 | 0.29 | 0.24 | 746 | 6536.52 |
| w_boosting | CISO | 2.95 | 2.65 | -2.04 | -2.66 | 0.42 | -17.31 | 0.36 | 0.15 | 719 | 25193.76 |
| w_boosting | DUK | 3.49 | 3.06 | -0.48 | -2.23 | 1.41 | -17.41 | 0.36 | 0.28 | 746 | 12143.29 |
| w_boosting | ERCO | 3.08 | 2.64 | -2.30 | -2.99 | 1.29 | -19.40 | 0.35 | 0.18 | 742 | 46834.59 |
| w_boosting | FPL | 6.25 | 5.90 | -6.58 | -6.95 | 1.32 | -52.14 | 0.18 | 0.27 | 665 | 15346.05 |
| w_boosting | ISNE | 3.69 | 3.32 | -0.66 | -1.98 | 0.59 | -18.34 | 0.24 | 0.17 | 748 | 13403.92 |
| w_boosting | MISO | 2.31 | 1.99 | -0.50 | -1.40 | 1.62 | -10.38 | 0.55 | 0.06 | 738 | 73700.16 |
| w_boosting | NYIS | 2.63 | 2.29 | -0.43 | -1.50 | 0.78 | -11.45 | 0.53 | 0.68 | 748 | 17415.28 |
| w_boosting | PJM | 2.69 | 2.44 | 0.04 | -1.38 | 1.63 | -10.86 | 0.44 | 0.42 | 734 | 92076.14 |
| w_boosting | SWPP | 2.58 | 2.16 | -0.87 | -1.92 | 1.55 | -29.06 | 0.67 | 0.08 | 741 | 31382.01 |
| w_boosting | TVA | 3.19 | 2.69 | -0.38 | -1.88 | 1.51 | -12.80 | 0.26 | 0.29 | 729 | 18581.23 |

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
| final3_hw | BPAT | uri | 2.41 | 0.16 | -0.88 | -5.26 | 6 |
| final3_hw | CISO | uri | 1.96 | -0.56 | -1.04 | -2.30 | 6 |
| final3_hw | DUK | uri | 3.69 | -1.43 | -1.95 | -3.80 | 6 |
| final3_hw | ERCO | uri | 6.53 | -7.89 | -7.89 | -8.65 | 2 |
| final3_hw | FPL | uri | 8.35 | -7.47 | -7.47 | -10.54 | 6 |
| final3_hw | ISNE | uri | 2.49 | 1.29 | -0.17 | -0.58 | 6 |
| final3_hw | MISO | uri | 4.38 | -3.83 | -3.96 | -7.40 | 5 |
| final3_hw | NYIS | uri | 2.02 | 1.92 | -0.15 | -0.90 | 6 |
| final3_hw | PJM | uri | 1.98 | 0.16 | -0.79 | -2.81 | 6 |
| final3_hw | SWPP | uri | 6.30 | -0.22 | -3.26 | -7.59 | 4 |
| final3_hw | TVA | uri | 3.72 | -0.93 | -2.47 | -4.98 | 6 |
| final3_hw_additive | BPAT | uri | 2.50 | 0.05 | -0.74 | -2.27 | 6 |
| final3_hw_additive | CISO | uri | 2.17 | 1.55 | -0.11 | -0.64 | 6 |
| final3_hw_additive | DUK | uri | 4.37 | -0.45 | -1.19 | -6.02 | 6 |
| final3_hw_additive | ERCO | uri | 4.50 | -4.43 | -4.43 | -7.08 | 2 |
| final3_hw_additive | FPL | uri | 10.39 | -14.93 | -14.93 | -17.51 | 6 |
| final3_hw_additive | ISNE | uri | 2.25 | 0.33 | -0.66 | -2.06 | 6 |
| final3_hw_additive | MISO | uri | 4.72 | -4.14 | -4.27 | -8.48 | 5 |
| final3_hw_additive | NYIS | uri | 2.22 | 2.37 | -0.02 | -0.11 | 6 |
| final3_hw_additive | PJM | uri | 2.44 | 0.76 | -0.93 | -4.39 | 6 |
| final3_hw_additive | SWPP | uri | 5.75 | 1.24 | -1.99 | -4.77 | 4 |
| final3_hw_additive | TVA | uri | 3.85 | 1.08 | -1.16 | -2.43 | 6 |
| final3_hw_boosting | BPAT | uri | 2.92 | 0.83 | -0.94 | -5.67 | 6 |
| final3_hw_boosting | CISO | uri | 2.06 | -1.00 | -1.38 | -3.88 | 6 |
| final3_hw_boosting | DUK | uri | 3.61 | -2.41 | -2.49 | -4.95 | 6 |
| final3_hw_boosting | ERCO | uri | 8.51 | -13.40 | -13.40 | -15.36 | 2 |
| final3_hw_boosting | FPL | uri | 8.60 | -10.26 | -10.26 | -13.08 | 6 |
| final3_hw_boosting | ISNE | uri | 3.87 | 2.07 | -0.42 | -1.79 | 6 |
| final3_hw_boosting | MISO | uri | 2.45 | -2.58 | -2.68 | -4.81 | 5 |
| final3_hw_boosting | NYIS | uri | 2.76 | 1.53 | -0.44 | -2.67 | 6 |
| final3_hw_boosting | PJM | uri | 1.95 | -0.50 | -0.92 | -2.57 | 6 |
| final3_hw_boosting | SWPP | uri | 5.08 | -3.51 | -4.28 | -9.79 | 4 |
| final3_hw_boosting | TVA | uri | 3.17 | -1.16 | -1.79 | -3.71 | 6 |
| final3_hw_ensemble | BPAT | uri | 2.51 | 0.26 | -0.75 | -4.19 | 6 |
| final3_hw_ensemble | CISO | uri | 1.78 | -0.18 | -0.67 | -1.90 | 6 |
| final3_hw_ensemble | DUK | uri | 3.71 | -2.13 | -2.13 | -5.99 | 6 |
| final3_hw_ensemble | ERCO | uri | 5.69 | -7.54 | -7.54 | -9.11 | 2 |
| final3_hw_ensemble | FPL | uri | 10.34 | -13.54 | -13.54 | -16.14 | 6 |
| final3_hw_ensemble | ISNE | uri | 2.36 | 0.27 | -0.55 | -2.18 | 6 |
| final3_hw_ensemble | MISO | uri | 4.23 | -4.11 | -4.11 | -7.45 | 5 |
| final3_hw_ensemble | NYIS | uri | 2.20 | 2.09 | -0.10 | -0.61 | 6 |
| final3_hw_ensemble | PJM | uri | 2.24 | 0.46 | -0.75 | -3.75 | 6 |
| final3_hw_ensemble | SWPP | uri | 5.83 | -1.57 | -3.59 | -7.69 | 4 |
| final3_hw_ensemble | TVA | uri | 3.45 | -0.24 | -1.60 | -3.00 | 6 |
| final3_hw_recency | BPAT | uri | 2.91 | -0.26 | -1.29 | -4.69 | 6 |
| final3_hw_recency | CISO | uri | 3.56 | -0.94 | -1.18 | -2.44 | 6 |
| final3_hw_recency | DUK | uri | 3.96 | -3.34 | -3.34 | -6.98 | 6 |
| final3_hw_recency | ERCO | uri | 5.16 | -4.08 | -4.32 | -8.65 | 2 |
| final3_hw_recency | FPL | uri | 12.52 | -16.13 | -16.13 | -18.76 | 6 |
| final3_hw_recency | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| final3_hw_recency | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| final3_hw_recency | NYIS | uri | 2.58 | 2.31 | -0.05 | -0.28 | 6 |
| final3_hw_recency | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| final3_hw_recency | SWPP | uri | 6.71 | -2.83 | -4.69 | -10.65 | 4 |
| final3_hw_recency | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| h_boosting | BPAT | uri | 3.02 | 0.67 | -0.94 | -4.88 | 6 |
| h_boosting | CISO | uri | 2.48 | -1.79 | -2.03 | -4.80 | 6 |
| h_boosting | DUK | uri | 3.71 | -2.23 | -2.39 | -5.90 | 6 |
| h_boosting | ERCO | uri | 8.50 | -12.13 | -12.13 | -14.13 | 2 |
| h_boosting | FPL | uri | 8.44 | -10.23 | -10.23 | -13.90 | 6 |
| h_boosting | ISNE | uri | 3.92 | 2.28 | -0.13 | -0.71 | 6 |
| h_boosting | MISO | uri | 2.32 | -2.46 | -2.59 | -5.34 | 5 |
| h_boosting | NYIS | uri | 2.85 | 1.95 | -0.35 | -2.12 | 6 |
| h_boosting | PJM | uri | 2.09 | -0.31 | -0.82 | -2.01 | 6 |
| h_boosting | SWPP | uri | 5.35 | -3.53 | -4.41 | -10.11 | 4 |
| h_boosting | TVA | uri | 3.19 | -0.94 | -1.79 | -4.74 | 6 |
| w_boosting | BPAT | uri | 2.92 | 0.61 | -1.09 | -5.88 | 6 |
| w_boosting | CISO | uri | 1.95 | -0.98 | -1.39 | -3.98 | 6 |
| w_boosting | DUK | uri | 3.56 | -2.43 | -2.43 | -4.99 | 6 |
| w_boosting | ERCO | uri | 8.25 | -12.83 | -12.83 | -15.13 | 2 |
| w_boosting | FPL | uri | 8.62 | -10.50 | -10.50 | -13.69 | 6 |
| w_boosting | ISNE | uri | 3.69 | 2.07 | -0.59 | -2.56 | 6 |
| w_boosting | MISO | uri | 3.14 | -3.15 | -3.15 | -5.90 | 5 |
| w_boosting | NYIS | uri | 2.49 | 0.75 | -0.77 | -3.57 | 6 |
| w_boosting | PJM | uri | 1.90 | -0.79 | -0.83 | -2.45 | 6 |
| w_boosting | SWPP | uri | 5.02 | -3.79 | -4.21 | -9.67 | 4 |
| w_boosting | TVA | uri | 2.75 | -1.27 | -1.92 | -4.25 | 6 |
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
| final3_hw | BPAT | elliott | 2.91 | -2.72 | -2.85 | -6.48 | 5 |
| final3_hw | CISO | elliott | 3.68 | 3.21 | -0.38 | -1.88 | 5 |
| final3_hw | DUK | elliott | 4.22 | -1.22 | -1.25 | -2.46 | 4 |
| final3_hw | ERCO | elliott | 5.50 | -2.31 | -3.56 | -7.80 | 5 |
| final3_hw | FPL | elliott | 7.50 | -8.27 | -8.27 | -12.86 | 5 |
| final3_hw | ISNE | elliott | 3.82 | 2.88 | -0.84 | -2.57 | 5 |
| final3_hw | MISO | elliott | 3.31 | -2.03 | -2.60 | -4.94 | 5 |
| final3_hw | NYIS | elliott | 2.83 | -0.35 | -1.52 | -3.51 | 5 |
| final3_hw | PJM | elliott | 4.60 | -4.25 | -4.25 | -11.03 | 5 |
| final3_hw | SWPP | elliott | 4.40 | -0.14 | -2.32 | -6.85 | 5 |
| final3_hw | TVA | elliott | 5.73 | 2.58 | 0.00 | 0.00 | 3 |
| final3_hw_additive | BPAT | elliott | 3.23 | -2.00 | -2.22 | -4.35 | 5 |
| final3_hw_additive | CISO | elliott | 3.57 | 4.39 | -0.13 | -0.63 | 5 |
| final3_hw_additive | DUK | elliott | 8.21 | -1.38 | -2.33 | -6.73 | 4 |
| final3_hw_additive | ERCO | elliott | 7.87 | -3.65 | -4.53 | -14.16 | 5 |
| final3_hw_additive | FPL | elliott | 13.29 | -4.31 | -7.25 | -18.03 | 5 |
| final3_hw_additive | ISNE | elliott | 4.27 | 2.10 | -1.57 | -3.94 | 5 |
| final3_hw_additive | MISO | elliott | 2.88 | -1.86 | -2.33 | -6.47 | 5 |
| final3_hw_additive | NYIS | elliott | 3.15 | 0.41 | -1.55 | -3.37 | 5 |
| final3_hw_additive | PJM | elliott | 3.76 | -1.20 | -1.80 | -4.89 | 5 |
| final3_hw_additive | SWPP | elliott | 3.39 | -4.02 | -4.15 | -8.71 | 5 |
| final3_hw_additive | TVA | elliott | 7.33 | -0.63 | -1.05 | -3.15 | 3 |
| final3_hw_boosting | BPAT | elliott | 4.23 | -5.34 | -5.34 | -11.66 | 5 |
| final3_hw_boosting | CISO | elliott | 4.04 | 1.93 | -0.82 | -3.86 | 5 |
| final3_hw_boosting | DUK | elliott | 4.68 | -3.05 | -3.05 | -6.31 | 4 |
| final3_hw_boosting | ERCO | elliott | 6.96 | -9.55 | -9.58 | -19.79 | 5 |
| final3_hw_boosting | FPL | elliott | 8.94 | -14.59 | -14.59 | -19.67 | 5 |
| final3_hw_boosting | ISNE | elliott | 3.95 | 3.32 | -0.22 | -1.12 | 5 |
| final3_hw_boosting | MISO | elliott | 3.41 | -1.13 | -2.26 | -4.00 | 5 |
| final3_hw_boosting | NYIS | elliott | 3.11 | 0.61 | -0.73 | -2.96 | 5 |
| final3_hw_boosting | PJM | elliott | 4.64 | -2.47 | -3.04 | -6.44 | 5 |
| final3_hw_boosting | SWPP | elliott | 5.45 | -1.84 | -3.83 | -11.88 | 5 |
| final3_hw_boosting | TVA | elliott | 6.16 | 0.77 | -1.10 | -3.31 | 3 |
| final3_hw_ensemble | BPAT | elliott | 3.55 | -3.60 | -3.66 | -8.15 | 5 |
| final3_hw_ensemble | CISO | elliott | 3.58 | 3.53 | -0.38 | -1.89 | 5 |
| final3_hw_ensemble | DUK | elliott | 4.89 | -3.28 | -3.28 | -6.06 | 4 |
| final3_hw_ensemble | ERCO | elliott | 5.82 | -5.29 | -5.73 | -11.31 | 5 |
| final3_hw_ensemble | FPL | elliott | 8.46 | -9.72 | -9.72 | -12.86 | 5 |
| final3_hw_ensemble | ISNE | elliott | 3.76 | 3.01 | -0.80 | -2.74 | 5 |
| final3_hw_ensemble | MISO | elliott | 3.19 | -2.51 | -2.82 | -6.11 | 5 |
| final3_hw_ensemble | NYIS | elliott | 2.91 | -0.14 | -1.51 | -3.01 | 5 |
| final3_hw_ensemble | PJM | elliott | 4.33 | -4.17 | -4.23 | -10.49 | 5 |
| final3_hw_ensemble | SWPP | elliott | 3.76 | -3.16 | -3.76 | -9.26 | 5 |
| final3_hw_ensemble | TVA | elliott | 5.85 | 0.95 | -0.94 | -2.03 | 3 |
| final3_hw_recency | BPAT | elliott | 4.21 | -3.09 | -3.09 | -10.23 | 5 |
| final3_hw_recency | CISO | elliott | 4.14 | 5.22 | -0.03 | -0.17 | 5 |
| final3_hw_recency | DUK | elliott | 3.96 | -5.35 | -5.35 | -9.06 | 4 |
| final3_hw_recency | ERCO | elliott | 4.32 | -1.45 | -2.67 | -6.25 | 5 |
| final3_hw_recency | FPL | elliott | 10.04 | -8.90 | -9.31 | -16.17 | 5 |
| final3_hw_recency | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| final3_hw_recency | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| final3_hw_recency | NYIS | elliott | 3.97 | -1.73 | -2.46 | -5.07 | 5 |
| final3_hw_recency | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| final3_hw_recency | SWPP | elliott | 3.28 | -3.64 | -3.98 | -9.50 | 5 |
| final3_hw_recency | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |
| h_boosting | BPAT | elliott | 4.31 | -4.47 | -4.63 | -10.92 | 5 |
| h_boosting | CISO | elliott | 4.05 | 1.78 | -0.93 | -4.24 | 5 |
| h_boosting | DUK | elliott | 4.61 | -3.06 | -3.06 | -6.88 | 4 |
| h_boosting | ERCO | elliott | 7.14 | -9.31 | -9.31 | -19.98 | 5 |
| h_boosting | FPL | elliott | 8.80 | -14.67 | -14.67 | -20.48 | 5 |
| h_boosting | ISNE | elliott | 3.75 | 3.12 | -0.14 | -0.69 | 5 |
| h_boosting | MISO | elliott | 3.53 | -1.28 | -2.27 | -4.18 | 5 |
| h_boosting | NYIS | elliott | 3.13 | 0.26 | -0.90 | -3.64 | 5 |
| h_boosting | PJM | elliott | 5.00 | -2.32 | -3.08 | -6.22 | 5 |
| h_boosting | SWPP | elliott | 5.72 | -1.57 | -4.02 | -12.13 | 5 |
| h_boosting | TVA | elliott | 6.28 | 1.24 | -0.93 | -2.78 | 3 |
| w_boosting | BPAT | elliott | 4.16 | -4.56 | -4.70 | -11.05 | 5 |
| w_boosting | CISO | elliott | 4.17 | 1.62 | -0.96 | -4.34 | 5 |
| w_boosting | DUK | elliott | 4.82 | -3.06 | -3.06 | -5.62 | 4 |
| w_boosting | ERCO | elliott | 6.56 | -9.84 | -9.84 | -19.40 | 5 |
| w_boosting | FPL | elliott | 9.41 | -15.50 | -15.50 | -19.83 | 5 |
| w_boosting | ISNE | elliott | 3.93 | 3.94 | -0.31 | -1.55 | 5 |
| w_boosting | MISO | elliott | 3.81 | -1.22 | -2.38 | -4.50 | 5 |
| w_boosting | NYIS | elliott | 2.97 | -0.05 | -1.16 | -3.46 | 5 |
| w_boosting | PJM | elliott | 5.06 | -2.51 | -3.53 | -7.17 | 5 |
| w_boosting | SWPP | elliott | 4.41 | -2.18 | -3.87 | -11.36 | 5 |
| w_boosting | TVA | elliott | 5.97 | 0.65 | -0.79 | -2.37 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | final3_hw | eve | 3.33 | 0.81 | -1.44 | 0.44 | 265 |
| 8 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 12 | final3_hw_ensemble | eve | 3.41 | -0.56 | -2.13 | 0.47 | 265 |
| 10 | final3_hw_additive | eve | 3.69 | -0.26 | -2.13 | 0.45 | 265 |
| 11 | final3_hw_boosting | eve | 3.73 | -0.16 | -2.05 | 0.40 | 265 |
| 15 | w_boosting | eve | 3.75 | -0.11 | -2.11 | 0.39 | 265 |
| 14 | h_boosting | eve | 3.77 | -0.12 | -2.03 | 0.38 | 265 |
| 13 | final3_hw_recency | eve | 4.25 | -1.47 | -2.94 | 0.32 | 265 |
| 1 | final3_hw | special | 3.36 | -0.67 | -2.15 | 0.52 | 267 |
| 4 | final3_hw_ensemble | special | 3.55 | -2.03 | -3.09 | 0.52 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 3 | final3_hw_boosting | special | 3.79 | -1.67 | -2.84 | 0.46 | 267 |
| 2 | final3_hw_additive | special | 3.79 | -2.08 | -3.19 | 0.48 | 267 |
| 6 | h_boosting | special | 3.83 | -1.57 | -2.79 | 0.46 | 267 |
| 7 | w_boosting | special | 3.88 | -1.63 | -2.91 | 0.46 | 267 |
| 5 | final3_hw_recency | special | 4.54 | -2.50 | -3.85 | 0.37 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3_hw | all | 0.387 | 1.315 | 0.392 | 0.889 | 11.587 | 0.891 | 7815 |
| final3_hw | events | 0.480 | 1.932 | 0.643 | 0.769 | 11.917 | 0.822 | 107 |
| final3_hw | cold_mornings | 0.453 | 1.665 | 0.522 | 0.833 | 12.905 | 0.812 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 17639 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 17638 | DUK | 2022-12-24 | final3_hw | 9.12 | -11.79 | -11.79 |
| 17634 | DUK | 2022-12-24 | final3_hw_additive | 8.68 | -16.68 | -16.68 |
| 17635 | DUK | 2022-12-24 | final3_hw_boosting | 9.91 | -17.04 | -17.04 |
| 17637 | DUK | 2022-12-24 | final3_hw_ensemble | 9.04 | -14.62 | -14.62 |
| 17636 | DUK | 2022-12-24 | final3_hw_recency | 9.27 | -9.99 | -9.99 |
| 17632 | DUK | 2022-12-24 | h_boosting | 9.96 | -18.19 | -18.19 |
| 17633 | DUK | 2022-12-24 | w_boosting | 9.88 | -18.19 | -18.19 |
| 18295 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 18294 | ERCO | 2021-02-17 | final3_hw | 32.61 | 26.66 | 0.00 |
| 18290 | ERCO | 2021-02-17 | final3_hw_additive | 31.23 | 30.11 | 0.00 |
| 18291 | ERCO | 2021-02-17 | final3_hw_boosting | 29.91 | 24.19 | 0.00 |
| 18293 | ERCO | 2021-02-17 | final3_hw_ensemble | 33.36 | 29.57 | 0.00 |
| 18292 | ERCO | 2021-02-17 | final3_hw_recency | 41.20 | 36.68 | 0.00 |
| 18288 | ERCO | 2021-02-17 | h_boosting | 29.50 | 23.26 | 0.00 |
| 18289 | ERCO | 2021-02-17 | w_boosting | 29.37 | 24.71 | 0.00 |
| 18303 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 18302 | ERCO | 2021-02-18 | final3_hw | 3.49 | 1.97 | 0.00 |
| 18298 | ERCO | 2021-02-18 | final3_hw_additive | 11.87 | 10.29 | 0.00 |
| 18299 | ERCO | 2021-02-18 | final3_hw_boosting | 4.23 | -7.71 | -7.71 |
| 18301 | ERCO | 2021-02-18 | final3_hw_ensemble | 3.82 | 0.96 | 0.00 |
| 18300 | ERCO | 2021-02-18 | final3_hw_recency | 5.36 | 2.19 | 0.00 |
| 18296 | ERCO | 2021-02-18 | h_boosting | 2.92 | -4.68 | -4.68 |
| 18297 | ERCO | 2021-02-18 | w_boosting | 2.98 | -6.73 | -6.73 |
| 35559 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 35558 | MISO | 2021-02-16 | final3_hw | 1.43 | 1.84 | 0.00 |
| 35554 | MISO | 2021-02-16 | final3_hw_additive | 1.55 | 1.66 | 0.00 |
| 35555 | MISO | 2021-02-16 | final3_hw_boosting | 1.96 | 1.33 | 0.00 |
| 35557 | MISO | 2021-02-16 | final3_hw_ensemble | 1.33 | 0.45 | 0.00 |
| 35556 | MISO | 2021-02-16 | final3_hw_recency | 3.61 | -2.07 | -2.07 |
| 35552 | MISO | 2021-02-16 | h_boosting | 3.03 | 1.40 | 0.00 |
| 35553 | MISO | 2021-02-16 | w_boosting | 1.92 | 0.81 | 0.00 |
| 53319 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 53318 | SWPP | 2021-02-15 | final3_hw | 3.80 | -3.27 | -3.27 |
| 53314 | SWPP | 2021-02-15 | final3_hw_additive | 1.17 | -1.01 | -1.01 |
| 53315 | SWPP | 2021-02-15 | final3_hw_boosting | 6.97 | -8.54 | -8.54 |
| 53317 | SWPP | 2021-02-15 | final3_hw_ensemble | 3.90 | -4.84 | -4.84 |
| 53316 | SWPP | 2021-02-15 | final3_hw_recency | 4.81 | -5.28 | -5.28 |
| 53312 | SWPP | 2021-02-15 | h_boosting | 6.23 | -8.01 | -8.01 |
| 53313 | SWPP | 2021-02-15 | w_boosting | 6.61 | -8.34 | -8.34 |
| 53327 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 53326 | SWPP | 2021-02-16 | final3_hw | 3.29 | -0.31 | -0.31 |
| 53322 | SWPP | 2021-02-16 | final3_hw_additive | 6.09 | 2.55 | 0.00 |
| 53323 | SWPP | 2021-02-16 | final3_hw_boosting | 3.27 | -6.32 | -6.32 |
| 53325 | SWPP | 2021-02-16 | final3_hw_ensemble | 3.38 | -1.22 | -1.22 |
| 53324 | SWPP | 2021-02-16 | final3_hw_recency | 2.57 | -0.10 | -0.10 |
| 53320 | SWPP | 2021-02-16 | h_boosting | 3.13 | -5.72 | -5.72 |
| 53321 | SWPP | 2021-02-16 | w_boosting | 3.84 | -6.28 | -6.28 |
| 64447 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 64446 | TVA | 2022-12-23 | final3_hw | 11.09 | -12.47 | -12.47 |
| 64442 | TVA | 2022-12-23 | final3_hw_additive | 12.58 | -8.20 | -8.20 |
| 64443 | TVA | 2022-12-23 | final3_hw_boosting | 15.23 | -16.37 | -16.37 |
| 64445 | TVA | 2022-12-23 | final3_hw_ensemble | 10.88 | -11.59 | -11.59 |
| 64444 | TVA | 2022-12-23 | final3_hw_recency | 11.83 | -10.22 | -10.22 |
| 64440 | TVA | 2022-12-23 | h_boosting | 14.01 | -15.52 | -15.52 |
| 64441 | TVA | 2022-12-23 | w_boosting | 14.25 | -15.40 | -15.40 |
| 64455 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 64454 | TVA | 2022-12-24 | final3_hw | 6.01 | -12.13 | -12.13 |
| 64450 | TVA | 2022-12-24 | final3_hw_additive | 3.70 | -9.02 | -9.02 |
| 64451 | TVA | 2022-12-24 | final3_hw_boosting | 7.15 | -15.20 | -15.20 |
| 64453 | TVA | 2022-12-24 | final3_hw_ensemble | 6.00 | -11.87 | -11.87 |
| 64452 | TVA | 2022-12-24 | final3_hw_recency | 7.21 | -11.36 | -11.36 |
| 64448 | TVA | 2022-12-24 | h_boosting | 7.32 | -15.52 | -15.52 |
| 64449 | TVA | 2022-12-24 | w_boosting | 6.54 | -15.14 | -15.14 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3_hw | BPAT | mape | 7.779 | 0.000 | 746 |
| final3_hw | CISO | mape | 0.879 | 0.379 | 719 |
| final3_hw | DUK | mape | 5.933 | 0.000 | 746 |
| final3_hw | ERCO | mape | -0.426 | 0.670 | 742 |
| final3_hw | FPL | mape | -2.886 | 0.004 | 665 |
| final3_hw | ISNE | mape | 13.856 | 0.000 | 748 |
| final3_hw | MISO | mape | -10.343 | 0.000 | 738 |
| final3_hw | NYIS | mape | -6.426 | 0.000 | 748 |
| final3_hw | PJM | mape | -5.793 | 0.000 | 734 |
| final3_hw | SWPP | mape | -18.902 | 0.000 | 741 |
| final3_hw | TVA | mape | 11.285 | 0.000 | 729 |
| final3_hw_additive | BPAT | mape | 12.841 | 0.000 | 746 |
| final3_hw_additive | CISO | mape | 16.272 | 0.000 | 719 |
| final3_hw_additive | DUK | mape | 9.667 | 0.000 | 746 |
| final3_hw_additive | ERCO | mape | 12.636 | 0.000 | 742 |
| final3_hw_additive | FPL | mape | 17.545 | 0.000 | 665 |
| final3_hw_additive | ISNE | mape | 19.841 | 0.000 | 748 |
| final3_hw_additive | MISO | mape | -4.624 | 0.000 | 738 |
| final3_hw_additive | NYIS | mape | -1.052 | 0.293 | 748 |
| final3_hw_additive | PJM | mape | 3.307 | 0.001 | 734 |
| final3_hw_additive | SWPP | mape | -15.629 | 0.000 | 741 |
| final3_hw_additive | TVA | mape | 15.912 | 0.000 | 729 |
| final3_hw_boosting | BPAT | mape | 11.385 | 0.000 | 746 |
| final3_hw_boosting | CISO | mape | 7.873 | 0.000 | 719 |
| final3_hw_boosting | DUK | mape | 7.523 | 0.000 | 746 |
| final3_hw_boosting | ERCO | mape | 4.791 | 0.000 | 742 |
| final3_hw_boosting | FPL | mape | 19.104 | 0.000 | 665 |
| final3_hw_boosting | ISNE | mape | 17.407 | 0.000 | 748 |
| final3_hw_boosting | MISO | mape | -6.182 | 0.000 | 738 |
| final3_hw_boosting | NYIS | mape | -2.270 | 0.023 | 748 |
| final3_hw_boosting | PJM | mape | 3.149 | 0.002 | 734 |
| final3_hw_boosting | SWPP | mape | -13.824 | 0.000 | 741 |
| final3_hw_boosting | TVA | mape | 13.850 | 0.000 | 729 |
| final3_hw_ensemble | BPAT | mape | 8.420 | 0.000 | 746 |
| final3_hw_ensemble | CISO | mape | 11.924 | 0.000 | 719 |
| final3_hw_ensemble | DUK | mape | 5.993 | 0.000 | 746 |
| final3_hw_ensemble | ERCO | mape | 6.167 | 0.000 | 742 |
| final3_hw_ensemble | FPL | mape | 19.564 | 0.000 | 665 |
| final3_hw_ensemble | ISNE | mape | 17.603 | 0.000 | 748 |
| final3_hw_ensemble | MISO | mape | -7.489 | 0.000 | 738 |
| final3_hw_ensemble | NYIS | mape | -5.606 | 0.000 | 748 |
| final3_hw_ensemble | PJM | mape | -1.269 | 0.204 | 734 |
| final3_hw_ensemble | SWPP | mape | -18.982 | 0.000 | 741 |
| final3_hw_ensemble | TVA | mape | 12.219 | 0.000 | 729 |
| final3_hw_recency | BPAT | mape | 17.471 | 0.000 | 746 |
| final3_hw_recency | CISO | mape | 37.528 | 0.000 | 719 |
| final3_hw_recency | DUK | mape | 14.008 | 0.000 | 746 |
| final3_hw_recency | ERCO | mape | 13.195 | 0.000 | 742 |
| final3_hw_recency | FPL | mape | 23.568 | 0.000 | 665 |
| final3_hw_recency | ISNE | mape | 36.381 | 0.000 | 748 |
| final3_hw_recency | MISO | mape | 3.545 | 0.000 | 738 |
| final3_hw_recency | NYIS | mape | 10.129 | 0.000 | 748 |
| final3_hw_recency | PJM | mape | 10.506 | 0.000 | 734 |
| final3_hw_recency | SWPP | mape | -9.646 | 0.000 | 741 |
| final3_hw_recency | TVA | mape | 20.369 | 0.000 | 729 |
| h_boosting | BPAT | mape | 11.635 | 0.000 | 746 |
| h_boosting | CISO | mape | 7.964 | 0.000 | 719 |
| h_boosting | DUK | mape | 7.113 | 0.000 | 746 |
| h_boosting | ERCO | mape | 4.778 | 0.000 | 742 |
| h_boosting | FPL | mape | 19.065 | 0.000 | 665 |
| h_boosting | ISNE | mape | 17.090 | 0.000 | 748 |
| h_boosting | MISO | mape | -6.295 | 0.000 | 738 |
| h_boosting | NYIS | mape | -1.698 | 0.089 | 748 |
| h_boosting | PJM | mape | 3.537 | 0.000 | 734 |
| h_boosting | SWPP | mape | -13.466 | 0.000 | 741 |
| h_boosting | TVA | mape | 13.792 | 0.000 | 729 |
| w_boosting | BPAT | mape | 11.762 | 0.000 | 746 |
| w_boosting | CISO | mape | 8.908 | 0.000 | 719 |
| w_boosting | DUK | mape | 9.102 | 0.000 | 746 |
| w_boosting | ERCO | mape | 6.193 | 0.000 | 742 |
| w_boosting | FPL | mape | 20.562 | 0.000 | 665 |
| w_boosting | ISNE | mape | 19.396 | 0.000 | 748 |
| w_boosting | MISO | mape | -5.133 | 0.000 | 738 |
| w_boosting | NYIS | mape | -0.580 | 0.562 | 748 |
| w_boosting | PJM | mape | 4.026 | 0.000 | 734 |
| w_boosting | SWPP | mape | -12.607 | 0.000 | 741 |
| w_boosting | TVA | mape | 15.589 | 0.000 | 729 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final3_hw | 0.987 |
| final3_hw_additive | 0.965 |
| final3_hw_boosting | 0.987 |
| final3_hw_ensemble | 0.987 |
| final3_hw_recency | 0.987 |
| h_boosting | 0.987 |
| w_boosting | 0.987 |
