# Phase K: the NBM temperature in place of the HRRR

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final6n` averages the NBM 2 m temperature at the stations with the HRRR path hour by hour; `final6r` uses the NBM where it has the hour and the HRRR elsewhere; `final6p` keeps the HRRR path and reads the cold-day peak rule from the NBM 5th-percentile 18-hour minimum. NBM files: one GeoTIFF per element and forecast hour in the public archive, hourly to 36 h and three-hourly beyond (interpolated). Compare with `docs/phase_i_final.md` (same days).

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6r | 2.33 | 1.97 | -0.02 | -1.27 | 1.12 | 0.59 | 0.28 | -45.60 | 8067 | 11.00 |
| final6r_ensemble | 2.50 | 2.18 | -1.97 | -2.46 | 1.10 | 0.54 | 0.17 | -49.30 | 8067 | 11.00 |
| final6r_boosting | 2.53 | 2.19 | -1.58 | -2.26 | 1.31 | 0.53 | 0.20 | -48.63 | 8067 | 11.00 |
| DF | 2.69 | 2.40 | 0.35 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8067 | 11.00 |
| final6r_additive | 2.80 | 2.46 | -2.20 | -2.77 | 1.18 | 0.48 | 0.17 | -48.55 | 8067 | 11.00 |
| final6r_recency | 3.36 | 2.97 | -2.31 | -2.94 | 1.39 | 0.37 | 0.17 | -50.91 | 8067 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.20 | -0.95 | 1.45 | -19.35 |  |  | 747 | 6537.86 |
| DF | CISO | 2.40 | 2.17 | 0.40 | -0.65 | 0.25 | -6.72 |  |  | 720 | 25192.90 |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | ERCO | 2.63 | 2.11 | 0.51 | -1.10 | 0.81 | -14.36 |  |  | 743 | 46838.99 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 749 | 13405.84 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 739 | 73717.29 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 749 | 17417.19 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 742 | 31388.55 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.23 | 0.97 | -11.24 |  |  | 730 | 18590.46 |
| final6r | BPAT | 2.28 | 2.02 | -0.47 | -1.39 | 1.75 | -17.50 | 0.43 | 0.24 | 747 | 6537.86 |
| final6r | CISO | 2.40 | 2.09 | 0.12 | -1.16 | 0.36 | -11.50 | 0.51 | 0.24 | 720 | 25192.90 |
| final6r | DUK | 2.81 | 2.39 | -0.02 | -1.55 | 1.28 | -14.47 | 0.53 | 0.31 | 747 | 12145.43 |
| final6r | ERCO | 2.50 | 1.90 | -0.05 | -1.37 | 0.80 | -19.66 | 0.53 | 0.26 | 743 | 46838.99 |
| final6r | FPL | 3.78 | 3.09 | -0.21 | -2.14 | 0.96 | -45.60 | 0.58 | 0.69 | 666 | 15342.04 |
| final6r | ISNE | 3.11 | 2.79 | 0.32 | -1.26 | 0.48 | -14.42 | 0.36 | 0.20 | 749 | 13405.84 |
| final6r | MISO | 1.98 | 1.73 | 0.06 | -1.03 | 1.44 | -6.84 | 0.64 | 0.06 | 739 | 73717.29 |
| final6r | NYIS | 2.27 | 1.94 | 0.09 | -1.25 | 0.53 | -14.83 | 0.63 | 0.74 | 749 | 17417.19 |
| final6r | PJM | 2.06 | 1.79 | -0.16 | -1.25 | 1.31 | -10.19 | 0.64 | 0.40 | 735 | 92099.88 |
| final6r | SWPP | 2.20 | 1.81 | -0.13 | -1.28 | 1.32 | -20.08 | 0.74 | 0.10 | 742 | 31388.55 |
| final6r | TVA | 2.67 | 2.30 | 0.40 | -1.29 | 1.20 | -11.17 | 0.38 | 0.33 | 730 | 18590.46 |
| final6r_additive | BPAT | 2.47 | 2.15 | -1.28 | -1.94 | 1.75 | -16.57 | 0.37 | 0.18 | 747 | 6537.86 |
| final6r_additive | CISO | 3.04 | 2.56 | -2.73 | -3.20 | 0.44 | -16.18 | 0.36 | 0.10 | 720 | 25192.90 |
| final6r_additive | DUK | 3.12 | 2.81 | -2.38 | -3.12 | 1.28 | -17.43 | 0.43 | 0.20 | 747 | 12145.43 |
| final6r_additive | ERCO | 3.37 | 2.99 | -2.78 | -3.40 | 0.87 | -21.74 | 0.34 | 0.11 | 743 | 46838.99 |
| final6r_additive | FPL | 4.94 | 4.28 | -5.29 | -5.81 | 0.99 | -48.55 | 0.44 | 0.31 | 666 | 15342.04 |
| final6r_additive | ISNE | 3.55 | 3.27 | -2.21 | -2.82 | 0.53 | -16.38 | 0.25 | 0.11 | 749 | 13405.84 |
| final6r_additive | MISO | 2.27 | 1.98 | -1.76 | -2.20 | 1.55 | -10.36 | 0.56 | 0.04 | 739 | 73717.29 |
| final6r_additive | NYIS | 2.66 | 2.28 | -1.80 | -2.56 | 0.56 | -15.96 | 0.52 | 0.54 | 749 | 17417.19 |
| final6r_additive | PJM | 2.46 | 2.20 | -1.76 | -2.33 | 1.37 | -13.11 | 0.52 | 0.27 | 735 | 92099.88 |
| final6r_additive | SWPP | 2.48 | 2.04 | -1.93 | -2.52 | 1.31 | -22.21 | 0.69 | 0.06 | 742 | 31388.55 |
| final6r_additive | TVA | 3.08 | 2.79 | -2.43 | -3.12 | 1.30 | -13.21 | 0.29 | 0.12 | 730 | 18590.46 |
| final6r_boosting | BPAT | 2.27 | 2.01 | -1.36 | -1.95 | 1.79 | -16.73 | 0.38 | 0.18 | 747 | 6537.86 |
| final6r_boosting | CISO | 2.64 | 2.28 | -1.22 | -1.91 | 0.40 | -15.30 | 0.45 | 0.18 | 720 | 25192.90 |
| final6r_boosting | DUK | 2.96 | 2.64 | -1.77 | -2.63 | 1.30 | -12.64 | 0.45 | 0.21 | 747 | 12145.43 |
| final6r_boosting | ERCO | 2.76 | 2.31 | -2.46 | -2.98 | 1.13 | -20.45 | 0.43 | 0.15 | 743 | 46838.99 |
| final6r_boosting | FPL | 4.40 | 3.82 | -4.89 | -5.38 | 1.20 | -48.63 | 0.53 | 0.35 | 666 | 15342.04 |
| final6r_boosting | ISNE | 3.19 | 2.92 | -1.14 | -1.96 | 0.55 | -16.33 | 0.33 | 0.14 | 749 | 13405.84 |
| final6r_boosting | MISO | 2.12 | 1.82 | -1.12 | -1.74 | 1.66 | -10.55 | 0.60 | 0.04 | 739 | 73717.29 |
| final6r_boosting | NYIS | 2.40 | 2.13 | -0.88 | -1.68 | 0.72 | -12.19 | 0.60 | 0.66 | 749 | 17417.19 |
| final6r_boosting | PJM | 2.27 | 2.02 | -1.20 | -1.92 | 1.46 | -11.95 | 0.57 | 0.31 | 735 | 92099.88 |
| final6r_boosting | SWPP | 2.47 | 2.02 | -1.88 | -2.52 | 1.53 | -28.35 | 0.69 | 0.05 | 742 | 31388.55 |
| final6r_boosting | TVA | 2.74 | 2.39 | -1.28 | -2.21 | 1.48 | -12.55 | 0.32 | 0.20 | 730 | 18590.46 |
| final6r_ensemble | BPAT | 2.24 | 1.99 | -1.44 | -1.96 | 1.72 | -17.10 | 0.43 | 0.18 | 747 | 6537.86 |
| final6r_ensemble | CISO | 2.80 | 2.40 | -2.41 | -2.76 | 0.41 | -14.64 | 0.42 | 0.09 | 720 | 25192.90 |
| final6r_ensemble | DUK | 2.82 | 2.42 | -1.91 | -2.68 | 1.22 | -15.27 | 0.49 | 0.20 | 747 | 12145.43 |
| final6r_ensemble | ERCO | 2.79 | 2.37 | -2.61 | -3.04 | 0.80 | -20.00 | 0.45 | 0.11 | 743 | 46838.99 |
| final6r_ensemble | FPL | 4.75 | 4.06 | -5.61 | -6.01 | 1.09 | -49.30 | 0.50 | 0.31 | 666 | 15342.04 |
| final6r_ensemble | ISNE | 3.29 | 3.03 | -2.25 | -2.70 | 0.52 | -14.73 | 0.28 | 0.09 | 749 | 13405.84 |
| final6r_ensemble | MISO | 2.08 | 1.85 | -1.53 | -1.95 | 1.48 | -10.03 | 0.61 | 0.03 | 739 | 73717.29 |
| final6r_ensemble | NYIS | 2.34 | 2.08 | -1.31 | -1.99 | 0.55 | -14.48 | 0.59 | 0.60 | 749 | 17417.19 |
| final6r_ensemble | PJM | 2.19 | 1.95 | -1.52 | -2.05 | 1.20 | -12.22 | 0.60 | 0.29 | 735 | 92099.88 |
| final6r_ensemble | SWPP | 2.19 | 1.79 | -1.61 | -2.15 | 1.25 | -20.38 | 0.72 | 0.06 | 742 | 31388.55 |
| final6r_ensemble | TVA | 2.70 | 2.43 | -1.86 | -2.57 | 1.19 | -12.81 | 0.35 | 0.12 | 730 | 18590.46 |
| final6r_recency | BPAT | 3.00 | 2.62 | -1.81 | -2.44 | 1.85 | -18.26 | 0.25 | 0.17 | 747 | 6537.86 |
| final6r_recency | CISO | 5.05 | 4.82 | -4.28 | -4.50 | 0.81 | -14.28 | 0.07 | 0.05 | 720 | 25192.90 |
| final6r_recency | DUK | 3.33 | 2.98 | -1.58 | -2.69 | 1.38 | -16.23 | 0.37 | 0.21 | 747 | 12145.43 |
| final6r_recency | ERCO | 3.35 | 2.81 | -2.69 | -3.30 | 1.01 | -20.67 | 0.33 | 0.14 | 743 | 46838.99 |
| final6r_recency | FPL | 5.97 | 4.89 | -7.15 | -7.57 | 1.18 | -50.91 | 0.35 | 0.24 | 666 | 15342.04 |
| final6r_recency | ISNE | 5.22 | 4.83 | -4.17 | -4.52 | 0.75 | -19.16 | 0.05 | 0.06 | 749 | 13405.84 |
| final6r_recency | MISO | 2.85 | 2.55 | -1.88 | -2.35 | 1.90 | -12.92 | 0.44 | 0.04 | 739 | 73717.29 |
| final6r_recency | NYIS | 3.49 | 3.21 | -1.41 | -2.36 | 0.80 | -18.20 | 0.34 | 0.53 | 749 | 17417.19 |
| final6r_recency | PJM | 2.83 | 2.52 | -1.66 | -2.33 | 1.48 | -15.27 | 0.40 | 0.27 | 735 | 92099.88 |
| final6r_recency | SWPP | 2.76 | 2.31 | -1.01 | -1.94 | 1.61 | -18.99 | 0.64 | 0.08 | 742 | 31388.55 |
| final6r_recency | TVA | 3.22 | 2.90 | -1.98 | -2.91 | 1.31 | -15.53 | 0.24 | 0.14 | 730 | 18590.46 |

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
| final6r | BPAT | uri | 2.55 | -1.11 | -1.70 | -4.42 | 6 |
| final6r | CISO | uri | 1.97 | 0.26 | -0.49 | -1.28 | 6 |
| final6r | DUK | uri | 4.22 | -3.45 | -3.88 | -8.77 | 6 |
| final6r | ERCO | uri | 7.18 | -9.42 | -9.42 | -11.23 | 2 |
| final6r | FPL | uri | 7.10 | -7.00 | -7.00 | -10.85 | 6 |
| final6r | ISNE | uri | 2.49 | 1.26 | -0.01 | -0.08 | 6 |
| final6r | MISO | uri | 3.82 | -3.49 | -3.49 | -6.84 | 5 |
| final6r | NYIS | uri | 2.13 | 2.47 | 0.00 | 0.00 | 6 |
| final6r | PJM | uri | 1.61 | -0.19 | -0.67 | -2.46 | 6 |
| final6r | SWPP | uri | 5.81 | 0.55 | -2.32 | -5.00 | 4 |
| final6r | TVA | uri | 4.27 | -1.19 | -2.34 | -7.21 | 6 |
| final6r_additive | BPAT | uri | 2.65 | -1.37 | -1.37 | -2.50 | 6 |
| final6r_additive | CISO | uri | 2.13 | 0.95 | -0.20 | -0.66 | 6 |
| final6r_additive | DUK | uri | 3.87 | -3.89 | -3.89 | -6.93 | 6 |
| final6r_additive | ERCO | uri | 6.20 | -7.89 | -7.89 | -11.03 | 2 |
| final6r_additive | FPL | uri | 9.37 | -13.18 | -13.18 | -17.55 | 6 |
| final6r_additive | ISNE | uri | 2.13 | 0.56 | -0.22 | -1.08 | 6 |
| final6r_additive | MISO | uri | 3.68 | -2.89 | -3.32 | -6.68 | 5 |
| final6r_additive | NYIS | uri | 2.45 | 2.48 | 0.00 | 0.00 | 6 |
| final6r_additive | PJM | uri | 2.53 | 1.61 | -0.42 | -2.43 | 6 |
| final6r_additive | SWPP | uri | 5.72 | 2.39 | -1.22 | -3.75 | 4 |
| final6r_additive | TVA | uri | 4.48 | -1.61 | -2.81 | -8.43 | 6 |
| final6r_boosting | BPAT | uri | 2.65 | -0.63 | -2.12 | -5.67 | 6 |
| final6r_boosting | CISO | uri | 2.25 | -1.16 | -1.56 | -3.70 | 6 |
| final6r_boosting | DUK | uri | 4.06 | -5.37 | -5.37 | -9.81 | 6 |
| final6r_boosting | ERCO | uri | 8.91 | -14.35 | -14.35 | -15.78 | 2 |
| final6r_boosting | FPL | uri | 6.81 | -8.40 | -8.40 | -13.08 | 6 |
| final6r_boosting | ISNE | uri | 2.90 | 0.39 | -0.66 | -1.79 | 6 |
| final6r_boosting | MISO | uri | 2.96 | -3.67 | -3.67 | -6.39 | 5 |
| final6r_boosting | NYIS | uri | 2.53 | 0.90 | -0.44 | -2.67 | 6 |
| final6r_boosting | PJM | uri | 1.47 | -1.55 | -1.61 | -3.03 | 6 |
| final6r_boosting | SWPP | uri | 4.58 | -3.09 | -3.85 | -9.78 | 4 |
| final6r_boosting | TVA | uri | 3.93 | -4.05 | -4.05 | -8.58 | 6 |
| final6r_ensemble | BPAT | uri | 2.33 | -0.95 | -1.43 | -4.21 | 6 |
| final6r_ensemble | CISO | uri | 2.02 | -0.80 | -1.30 | -2.20 | 6 |
| final6r_ensemble | DUK | uri | 4.11 | -4.88 | -4.88 | -8.45 | 6 |
| final6r_ensemble | ERCO | uri | 7.23 | -10.04 | -10.04 | -11.96 | 2 |
| final6r_ensemble | FPL | uri | 9.10 | -11.87 | -11.87 | -16.14 | 6 |
| final6r_ensemble | ISNE | uri | 2.15 | -0.51 | -0.76 | -1.92 | 6 |
| final6r_ensemble | MISO | uri | 3.89 | -4.08 | -4.08 | -7.30 | 5 |
| final6r_ensemble | NYIS | uri | 2.12 | 1.68 | -0.10 | -0.60 | 6 |
| final6r_ensemble | PJM | uri | 1.76 | -0.16 | -0.71 | -3.04 | 6 |
| final6r_ensemble | SWPP | uri | 5.50 | -0.94 | -3.07 | -6.87 | 4 |
| final6r_ensemble | TVA | uri | 4.20 | -2.86 | -3.39 | -8.46 | 6 |
| final6r_recency | BPAT | uri | 2.63 | -0.93 | -1.05 | -4.69 | 6 |
| final6r_recency | CISO | uri | 3.74 | -2.33 | -2.56 | -4.33 | 6 |
| final6r_recency | DUK | uri | 4.70 | -5.41 | -5.41 | -8.64 | 6 |
| final6r_recency | ERCO | uri | 7.22 | -7.12 | -7.12 | -11.83 | 2 |
| final6r_recency | FPL | uri | 11.56 | -14.56 | -14.56 | -18.55 | 6 |
| final6r_recency | ISNE | uri | 4.12 | -3.33 | -3.33 | -4.83 | 6 |
| final6r_recency | MISO | uri | 6.76 | -6.22 | -6.22 | -9.97 | 5 |
| final6r_recency | NYIS | uri | 2.33 | 1.63 | -0.01 | -0.08 | 6 |
| final6r_recency | PJM | uri | 2.23 | -0.23 | -0.94 | -4.36 | 6 |
| final6r_recency | SWPP | uri | 6.22 | -2.68 | -4.41 | -10.52 | 4 |
| final6r_recency | TVA | uri | 4.73 | -2.90 | -3.65 | -8.37 | 6 |
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
| final6r | BPAT | elliott | 2.84 | -1.98 | -2.18 | -5.46 | 5 |
| final6r | CISO | elliott | 3.27 | 1.37 | -1.06 | -4.53 | 5 |
| final6r | DUK | elliott | 3.02 | -2.94 | -2.98 | -6.76 | 4 |
| final6r | ERCO | elliott | 6.37 | -2.42 | -3.52 | -11.38 | 5 |
| final6r | FPL | elliott | 5.49 | -5.43 | -5.67 | -9.72 | 5 |
| final6r | ISNE | elliott | 3.18 | 1.65 | -0.59 | -1.57 | 5 |
| final6r | MISO | elliott | 3.52 | -2.62 | -3.40 | -5.55 | 5 |
| final6r | NYIS | elliott | 2.87 | -0.75 | -1.41 | -4.08 | 5 |
| final6r | PJM | elliott | 4.25 | -4.19 | -4.19 | -8.32 | 5 |
| final6r | SWPP | elliott | 4.78 | 0.31 | -2.24 | -7.19 | 5 |
| final6r | TVA | elliott | 4.08 | -2.51 | -2.71 | -7.81 | 3 |
| final6r_additive | BPAT | elliott | 3.71 | -1.63 | -2.12 | -4.50 | 5 |
| final6r_additive | CISO | elliott | 3.00 | -1.15 | -2.25 | -7.85 | 5 |
| final6r_additive | DUK | elliott | 3.56 | -5.07 | -5.07 | -7.58 | 4 |
| final6r_additive | ERCO | elliott | 7.66 | -6.42 | -6.56 | -11.70 | 5 |
| final6r_additive | FPL | elliott | 6.60 | -4.04 | -4.65 | -10.64 | 5 |
| final6r_additive | ISNE | elliott | 4.15 | -2.00 | -2.42 | -5.70 | 5 |
| final6r_additive | MISO | elliott | 3.65 | -4.45 | -4.60 | -6.84 | 5 |
| final6r_additive | NYIS | elliott | 3.89 | -3.44 | -3.44 | -6.02 | 5 |
| final6r_additive | PJM | elliott | 3.66 | -3.53 | -3.53 | -8.02 | 5 |
| final6r_additive | SWPP | elliott | 3.77 | -2.96 | -3.23 | -6.69 | 5 |
| final6r_additive | TVA | elliott | 4.46 | -3.20 | -3.20 | -6.54 | 3 |
| final6r_boosting | BPAT | elliott | 3.40 | -4.56 | -4.56 | -9.18 | 5 |
| final6r_boosting | CISO | elliott | 3.31 | 1.12 | -1.08 | -4.36 | 5 |
| final6r_boosting | DUK | elliott | 3.57 | -3.94 | -3.94 | -7.46 | 4 |
| final6r_boosting | ERCO | elliott | 7.97 | -12.11 | -12.11 | -20.45 | 5 |
| final6r_boosting | FPL | elliott | 8.84 | -13.85 | -13.85 | -20.28 | 5 |
| final6r_boosting | ISNE | elliott | 3.19 | 0.10 | -1.10 | -2.71 | 5 |
| final6r_boosting | MISO | elliott | 3.58 | -2.88 | -3.79 | -5.40 | 5 |
| final6r_boosting | NYIS | elliott | 2.74 | -1.01 | -1.63 | -3.96 | 5 |
| final6r_boosting | PJM | elliott | 4.01 | -5.58 | -5.58 | -8.55 | 5 |
| final6r_boosting | SWPP | elliott | 5.92 | -2.46 | -4.26 | -12.51 | 5 |
| final6r_boosting | TVA | elliott | 4.45 | -4.24 | -4.24 | -8.03 | 3 |
| final6r_ensemble | BPAT | elliott | 2.92 | -3.07 | -3.11 | -6.31 | 5 |
| final6r_ensemble | CISO | elliott | 2.95 | 0.34 | -1.41 | -5.52 | 5 |
| final6r_ensemble | DUK | elliott | 3.44 | -5.45 | -5.45 | -7.31 | 4 |
| final6r_ensemble | ERCO | elliott | 6.78 | -8.06 | -8.06 | -14.71 | 5 |
| final6r_ensemble | FPL | elliott | 7.36 | -10.01 | -10.01 | -14.11 | 5 |
| final6r_ensemble | ISNE | elliott | 3.56 | -0.78 | -1.91 | -4.19 | 5 |
| final6r_ensemble | MISO | elliott | 3.76 | -4.23 | -4.55 | -7.08 | 5 |
| final6r_ensemble | NYIS | elliott | 3.34 | -2.45 | -2.74 | -5.22 | 5 |
| final6r_ensemble | PJM | elliott | 4.31 | -5.71 | -5.71 | -10.17 | 5 |
| final6r_ensemble | SWPP | elliott | 4.38 | -3.15 | -3.80 | -10.04 | 5 |
| final6r_ensemble | TVA | elliott | 4.13 | -4.60 | -4.60 | -7.86 | 3 |
| final6r_recency | BPAT | elliott | 3.79 | -2.78 | -3.39 | -9.12 | 5 |
| final6r_recency | CISO | elliott | 3.83 | 0.77 | -1.29 | -4.69 | 5 |
| final6r_recency | DUK | elliott | 4.23 | -7.60 | -7.60 | -9.48 | 4 |
| final6r_recency | ERCO | elliott | 5.63 | -4.75 | -4.75 | -13.72 | 5 |
| final6r_recency | FPL | elliott | 10.07 | -12.10 | -12.10 | -17.00 | 5 |
| final6r_recency | ISNE | elliott | 4.67 | -0.66 | -2.57 | -5.30 | 5 |
| final6r_recency | MISO | elliott | 5.65 | -6.22 | -6.22 | -12.92 | 5 |
| final6r_recency | NYIS | elliott | 4.78 | -3.71 | -3.91 | -6.62 | 5 |
| final6r_recency | PJM | elliott | 5.96 | -8.00 | -8.00 | -15.27 | 5 |
| final6r_recency | SWPP | elliott | 4.03 | -4.16 | -4.67 | -11.16 | 5 |
| final6r_recency | TVA | elliott | 4.15 | -6.53 | -6.53 | -9.14 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final6r_ensemble | eve | 3.10 | -1.13 | -2.26 | 0.56 | 265 |
| 7 | final6r | eve | 3.25 | 0.96 | -1.26 | 0.50 | 265 |
| 8 | final6r_additive | eve | 3.31 | -1.03 | -2.33 | 0.50 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 9 | final6r_boosting | eve | 3.44 | -0.67 | -2.19 | 0.47 | 265 |
| 11 | final6r_recency | eve | 3.88 | -2.08 | -3.04 | 0.37 | 265 |
| 1 | final6r | special | 3.14 | -0.37 | -1.80 | 0.58 | 267 |
| 4 | final6r_ensemble | special | 3.20 | -2.61 | -3.25 | 0.60 | 267 |
| 2 | final6r_additive | special | 3.43 | -2.82 | -3.45 | 0.51 | 267 |
| 3 | final6r_boosting | special | 3.44 | -2.18 | -3.01 | 0.53 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 5 | final6r_recency | special | 4.12 | -3.15 | -4.01 | 0.44 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final6r | all | 0.381 | 1.274 | 0.371 | 0.887 | 11.036 | 0.886 | 15.049 | 1.653 | 7837 |
| final6r | events | 0.467 | 1.900 | 0.652 | 0.752 | 11.525 | 0.685 | 22.377 | 2.513 | 111 |
| final6r | cold_mornings | 0.434 | 1.542 | 0.555 | 0.843 | 12.197 | 0.830 | 19.788 | 2.068 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13247 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13246 | DUK | 2022-12-24 | final6r | 10.67 | -11.40 | -11.40 |
| 13242 | DUK | 2022-12-24 | final6r_additive | 10.09 | -12.69 | -12.69 |
| 13243 | DUK | 2022-12-24 | final6r_boosting | 11.47 | -17.16 | -17.16 |
| 13245 | DUK | 2022-12-24 | final6r_ensemble | 10.97 | -14.09 | -14.09 |
| 13244 | DUK | 2022-12-24 | final6r_recency | 11.49 | -12.30 | -12.30 |
| 13739 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13738 | ERCO | 2021-02-17 | final6r | 29.73 | 21.41 | 0.00 |
| 13734 | ERCO | 2021-02-17 | final6r_additive | 27.13 | 21.57 | 0.00 |
| 13735 | ERCO | 2021-02-17 | final6r_boosting | 26.94 | 18.79 | 0.00 |
| 13737 | ERCO | 2021-02-17 | final6r_ensemble | 29.44 | 22.01 | 0.00 |
| 13736 | ERCO | 2021-02-17 | final6r_recency | 35.86 | 27.15 | 0.00 |
| 13745 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13744 | ERCO | 2021-02-18 | final6r | 4.59 | 2.48 | 0.00 |
| 13740 | ERCO | 2021-02-18 | final6r_additive | 13.29 | 11.84 | 0.00 |
| 13741 | ERCO | 2021-02-18 | final6r_boosting | 4.23 | -7.71 | -7.71 |
| 13743 | ERCO | 2021-02-18 | final6r_ensemble | 4.25 | 1.44 | 0.00 |
| 13742 | ERCO | 2021-02-18 | final6r_recency | 5.36 | 2.19 | 0.00 |
| 26705 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26704 | MISO | 2021-02-16 | final6r | 1.75 | 1.24 | 0.00 |
| 26700 | MISO | 2021-02-16 | final6r_additive | 2.11 | 1.89 | 0.00 |
| 26701 | MISO | 2021-02-16 | final6r_boosting | 1.43 | 0.92 | 0.00 |
| 26703 | MISO | 2021-02-16 | final6r_ensemble | 1.53 | 0.42 | 0.00 |
| 26702 | MISO | 2021-02-16 | final6r_recency | 4.05 | -2.35 | -2.35 |
| 40043 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 40042 | SWPP | 2021-02-15 | final6r | 2.58 | -2.33 | -2.33 |
| 40038 | SWPP | 2021-02-15 | final6r_additive | 2.85 | 1.37 | 0.00 |
| 40039 | SWPP | 2021-02-15 | final6r_boosting | 6.58 | -8.08 | -8.08 |
| 40041 | SWPP | 2021-02-15 | final6r_ensemble | 2.72 | -3.59 | -3.59 |
| 40040 | SWPP | 2021-02-15 | final6r_recency | 4.69 | -4.66 | -4.66 |
| 40049 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 40048 | SWPP | 2021-02-16 | final6r | 4.01 | -0.39 | -0.39 |
| 40044 | SWPP | 2021-02-16 | final6r_additive | 7.63 | 3.62 | 0.00 |
| 40045 | SWPP | 2021-02-16 | final6r_boosting | 3.41 | -6.32 | -6.32 |
| 40047 | SWPP | 2021-02-16 | final6r_ensemble | 3.71 | -0.95 | -0.95 |
| 40046 | SWPP | 2021-02-16 | final6r_recency | 2.23 | -0.78 | -0.78 |
| 48401 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48400 | TVA | 2022-12-23 | final6r | 10.89 | -12.64 | -12.64 |
| 48396 | TVA | 2022-12-23 | final6r_additive | 7.48 | -8.91 | -8.91 |
| 48397 | TVA | 2022-12-23 | final6r_boosting | 16.51 | -17.28 | -17.28 |
| 48399 | TVA | 2022-12-23 | final6r_ensemble | 11.15 | -12.91 | -12.91 |
| 48398 | TVA | 2022-12-23 | final6r_recency | 9.85 | -12.89 | -12.89 |
| 48407 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48406 | TVA | 2022-12-24 | final6r | 7.00 | -14.09 | -14.09 |
| 48402 | TVA | 2022-12-24 | final6r_additive | 5.19 | -11.52 | -11.52 |
| 48403 | TVA | 2022-12-24 | final6r_boosting | 8.31 | -15.36 | -15.36 |
| 48405 | TVA | 2022-12-24 | final6r_ensemble | 7.20 | -13.35 | -13.35 |
| 48404 | TVA | 2022-12-24 | final6r_recency | 8.47 | -13.29 | -13.29 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final6r | BPAT | mape | 4.488 | 0.000 | 747 |
| final6r | CISO | mape | 0.056 | 0.955 | 720 |
| final6r | DUK | mape | -0.506 | 0.613 | 747 |
| final6r | ERCO | mape | -2.089 | 0.037 | 743 |
| final6r | FPL | mape | -0.979 | 0.328 | 666 |
| final6r | ISNE | mape | 13.065 | 0.000 | 749 |
| final6r | MISO | mape | -11.186 | 0.000 | 739 |
| final6r | NYIS | mape | -6.394 | 0.000 | 749 |
| final6r | PJM | mape | -7.981 | 0.000 | 735 |
| final6r | SWPP | mape | -18.416 | 0.000 | 742 |
| final6r | TVA | mape | 8.979 | 0.000 | 730 |
| final6r_additive | BPAT | mape | 7.884 | 0.000 | 747 |
| final6r_additive | CISO | mape | 9.864 | 0.000 | 720 |
| final6r_additive | DUK | mape | 4.336 | 0.000 | 747 |
| final6r_additive | ERCO | mape | 9.651 | 0.000 | 743 |
| final6r_additive | FPL | mape | 8.549 | 0.000 | 666 |
| final6r_additive | ISNE | mape | 19.634 | 0.000 | 749 |
| final6r_additive | MISO | mape | -5.294 | 0.000 | 739 |
| final6r_additive | NYIS | mape | -0.181 | 0.856 | 749 |
| final6r_additive | PJM | mape | -0.013 | 0.989 | 735 |
| final6r_additive | SWPP | mape | -13.715 | 0.000 | 742 |
| final6r_additive | TVA | mape | 14.821 | 0.000 | 730 |
| final6r_boosting | BPAT | mape | 4.631 | 0.000 | 747 |
| final6r_boosting | CISO | mape | 4.117 | 0.000 | 720 |
| final6r_boosting | DUK | mape | 2.127 | 0.033 | 747 |
| final6r_boosting | ERCO | mape | 1.926 | 0.054 | 743 |
| final6r_boosting | FPL | mape | 4.728 | 0.000 | 666 |
| final6r_boosting | ISNE | mape | 14.766 | 0.000 | 749 |
| final6r_boosting | MISO | mape | -8.233 | 0.000 | 739 |
| final6r_boosting | NYIS | mape | -4.492 | 0.000 | 749 |
| final6r_boosting | PJM | mape | -3.839 | 0.000 | 735 |
| final6r_boosting | SWPP | mape | -13.557 | 0.000 | 742 |
| final6r_boosting | TVA | mape | 11.091 | 0.000 | 730 |
| final6r_ensemble | BPAT | mape | 3.635 | 0.000 | 747 |
| final6r_ensemble | CISO | mape | 6.576 | 0.000 | 720 |
| final6r_ensemble | DUK | mape | -0.259 | 0.796 | 747 |
| final6r_ensemble | ERCO | mape | 2.402 | 0.016 | 743 |
| final6r_ensemble | FPL | mape | 7.070 | 0.000 | 666 |
| final6r_ensemble | ISNE | mape | 16.880 | 0.000 | 749 |
| final6r_ensemble | MISO | mape | -8.474 | 0.000 | 739 |
| final6r_ensemble | NYIS | mape | -6.000 | 0.000 | 749 |
| final6r_ensemble | PJM | mape | -5.729 | 0.000 | 735 |
| final6r_ensemble | SWPP | mape | -17.745 | 0.000 | 742 |
| final6r_ensemble | TVA | mape | 9.969 | 0.000 | 730 |
| final6r_recency | BPAT | mape | 14.788 | 0.000 | 747 |
| final6r_recency | CISO | mape | 34.822 | 0.000 | 720 |
| final6r_recency | DUK | mape | 7.929 | 0.000 | 747 |
| final6r_recency | ERCO | mape | 8.977 | 0.000 | 743 |
| final6r_recency | FPL | mape | 13.277 | 0.000 | 666 |
| final6r_recency | ISNE | mape | 37.335 | 0.000 | 749 |
| final6r_recency | MISO | mape | 2.603 | 0.009 | 739 |
| final6r_recency | NYIS | mape | 11.672 | 0.000 | 749 |
| final6r_recency | PJM | mape | 6.765 | 0.000 | 735 |
| final6r_recency | SWPP | mape | -11.049 | 0.000 | 742 |
| final6r_recency | TVA | mape | 16.607 | 0.000 | 730 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final6r | 0.989 |
| final6r_additive | 0.966 |
| final6r_boosting | 0.989 |
| final6r_ensemble | 0.989 |
| final6r_recency | 0.989 |
