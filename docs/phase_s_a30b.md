# Phase S (A30b): a linear recalibration of the ensemble per hour of the day

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final12l` is the band of `final10s` on top of `final12l_recal`: for each hour of the day, the load that occurred regressed on the ensemble over the last 365 known days of the target day's regime (slope clipped to 0.8-1.5, at least 60 days), to undo the members' shrinkage toward the mean on the highest days.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10s | 2.26 | 1.94 | -0.04 | -1.22 | 1.12 | 0.61 | 0.29 | -46.62 | 8079 | 11.00 |
| final12l_recal | 2.31 | 2.00 | -0.99 | -1.78 | 1.10 | 0.60 | 0.23 | -46.31 | 8079 | 11.00 |
| final12l | 2.39 | 2.05 | 0.29 | -1.13 | 1.16 | 0.57 | 0.30 | -46.13 | 8079 | 11.00 |
| final10s_ensemble | 2.50 | 2.19 | -1.80 | -2.29 | 1.11 | 0.54 | 0.18 | -49.12 | 8079 | 11.00 |
| final10s_boosting | 2.52 | 2.24 | -1.43 | -2.11 | 1.30 | 0.53 | 0.21 | -48.89 | 8079 | 11.00 |
| DF | 2.69 | 2.40 | 0.35 | -1.06 | 0.91 | 0.00 | 0.00 | -47.43 | 8079 | 11.00 |
| final10s_additive | 2.79 | 2.47 | -2.01 | -2.59 | 1.19 | 0.47 | 0.18 | -48.25 | 8079 | 11.00 |
| final10s_recency | 3.38 | 3.01 | -2.18 | -2.79 | 1.43 | 0.35 | 0.18 | -50.47 | 8079 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.21 | -0.95 | 1.45 | -19.35 |  |  | 749 | 6537.56 |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.25 | -6.72 |  |  | 722 | 25198.48 |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | ERCO | 2.63 | 2.11 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 745 | 46853.29 |
| DF | FPL | 3.89 | 3.59 | -3.66 | -4.05 | 1.16 | -47.43 |  |  | 666 | 15342.04 |
| DF | ISNE | 2.36 | 2.31 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 749 | 13405.84 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 749 | 17417.19 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final10s | BPAT | 2.30 | 2.02 | -0.40 | -1.35 | 1.60 | -17.41 | 0.44 | 0.25 | 749 | 6537.56 |
| final10s | CISO | 2.27 | 1.97 | 0.27 | -1.00 | 0.34 | -11.04 | 0.56 | 0.27 | 722 | 25198.48 |
| final10s | DUK | 2.81 | 2.50 | -0.00 | -1.50 | 1.18 | -13.20 | 0.50 | 0.32 | 747 | 12145.43 |
| final10s | ERCO | 2.45 | 1.95 | -0.11 | -1.34 | 0.88 | -17.51 | 0.54 | 0.27 | 745 | 46853.29 |
| final10s | FPL | 3.37 | 2.81 | -0.17 | -1.91 | 0.97 | -46.62 | 0.64 | 0.70 | 666 | 15342.04 |
| final10s | ISNE | 3.00 | 2.70 | 0.20 | -1.24 | 0.49 | -13.56 | 0.39 | 0.20 | 749 | 13405.84 |
| final10s | MISO | 1.95 | 1.69 | 0.07 | -0.99 | 1.47 | -7.14 | 0.66 | 0.06 | 741 | 73714.43 |
| final10s | NYIS | 2.20 | 1.90 | -0.04 | -1.24 | 0.53 | -14.02 | 0.65 | 0.73 | 749 | 17417.19 |
| final10s | PJM | 2.00 | 1.76 | -0.22 | -1.19 | 1.30 | -10.45 | 0.65 | 0.42 | 735 | 92099.88 |
| final10s | SWPP | 2.22 | 1.82 | -0.07 | -1.27 | 1.30 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final10s | TVA | 2.58 | 2.24 | 0.27 | -1.32 | 1.13 | -11.14 | 0.39 | 0.32 | 732 | 18589.75 |
| final10s_additive | BPAT | 2.52 | 2.21 | -0.94 | -1.71 | 1.70 | -16.81 | 0.36 | 0.20 | 749 | 6537.56 |
| final10s_additive | CISO | 2.70 | 2.44 | -1.63 | -2.34 | 0.39 | -12.70 | 0.41 | 0.14 | 722 | 25198.48 |
| final10s_additive | DUK | 3.14 | 2.84 | -2.31 | -3.01 | 1.20 | -16.21 | 0.42 | 0.19 | 747 | 12145.43 |
| final10s_additive | ERCO | 3.29 | 2.87 | -2.65 | -3.23 | 0.97 | -18.25 | 0.34 | 0.11 | 745 | 46853.29 |
| final10s_additive | FPL | 4.61 | 4.09 | -4.70 | -5.25 | 0.99 | -48.25 | 0.45 | 0.35 | 666 | 15342.04 |
| final10s_additive | ISNE | 3.55 | 3.25 | -1.84 | -2.59 | 0.53 | -16.84 | 0.25 | 0.13 | 749 | 13405.84 |
| final10s_additive | MISO | 2.29 | 2.00 | -1.69 | -2.12 | 1.48 | -10.13 | 0.56 | 0.04 | 741 | 73714.43 |
| final10s_additive | NYIS | 2.59 | 2.25 | -1.65 | -2.42 | 0.54 | -16.88 | 0.54 | 0.55 | 749 | 17417.19 |
| final10s_additive | PJM | 2.58 | 2.29 | -1.69 | -2.26 | 1.41 | -12.60 | 0.48 | 0.30 | 735 | 92099.88 |
| final10s_additive | SWPP | 2.48 | 2.06 | -1.70 | -2.35 | 1.38 | -21.65 | 0.69 | 0.07 | 744 | 31394.87 |
| final10s_additive | TVA | 3.27 | 3.04 | -2.62 | -3.25 | 1.36 | -14.44 | 0.27 | 0.13 | 732 | 18589.75 |
| final10s_boosting | BPAT | 2.33 | 2.06 | -0.98 | -1.74 | 1.80 | -17.05 | 0.39 | 0.22 | 749 | 6537.56 |
| final10s_boosting | CISO | 2.50 | 2.23 | -0.56 | -1.44 | 0.43 | -15.05 | 0.47 | 0.21 | 722 | 25198.48 |
| final10s_boosting | DUK | 2.96 | 2.67 | -1.62 | -2.47 | 1.30 | -14.77 | 0.42 | 0.22 | 747 | 12145.43 |
| final10s_boosting | ERCO | 2.70 | 2.28 | -2.30 | -2.82 | 1.16 | -17.43 | 0.44 | 0.15 | 745 | 46853.29 |
| final10s_boosting | FPL | 3.93 | 3.61 | -4.53 | -4.96 | 1.14 | -48.89 | 0.53 | 0.36 | 666 | 15342.04 |
| final10s_boosting | ISNE | 3.23 | 2.94 | -0.87 | -1.78 | 0.53 | -15.59 | 0.33 | 0.16 | 749 | 13405.84 |
| final10s_boosting | MISO | 2.16 | 1.87 | -1.07 | -1.67 | 1.58 | -9.57 | 0.60 | 0.04 | 741 | 73714.43 |
| final10s_boosting | NYIS | 2.32 | 2.06 | -0.64 | -1.48 | 0.74 | -12.56 | 0.60 | 0.70 | 749 | 17417.19 |
| final10s_boosting | PJM | 2.36 | 2.19 | -1.11 | -1.81 | 1.49 | -12.20 | 0.54 | 0.34 | 735 | 92099.88 |
| final10s_boosting | SWPP | 2.46 | 2.03 | -1.69 | -2.42 | 1.59 | -29.38 | 0.69 | 0.06 | 744 | 31394.87 |
| final10s_boosting | TVA | 2.80 | 2.47 | -1.56 | -2.32 | 1.35 | -12.55 | 0.33 | 0.18 | 732 | 18589.75 |
| final10s_ensemble | BPAT | 2.28 | 2.02 | -1.10 | -1.73 | 1.69 | -17.50 | 0.42 | 0.20 | 749 | 6537.56 |
| final10s_ensemble | CISO | 2.50 | 2.26 | -1.50 | -2.01 | 0.38 | -13.33 | 0.49 | 0.13 | 722 | 25198.48 |
| final10s_ensemble | DUK | 2.85 | 2.52 | -1.81 | -2.55 | 1.24 | -13.97 | 0.46 | 0.19 | 747 | 12145.43 |
| final10s_ensemble | ERCO | 2.71 | 2.27 | -2.47 | -2.87 | 0.86 | -17.48 | 0.45 | 0.11 | 745 | 46853.29 |
| final10s_ensemble | FPL | 4.32 | 3.91 | -5.03 | -5.41 | 0.98 | -49.12 | 0.50 | 0.33 | 666 | 15342.04 |
| final10s_ensemble | ISNE | 3.28 | 3.04 | -1.88 | -2.39 | 0.51 | -16.50 | 0.28 | 0.10 | 749 | 13405.84 |
| final10s_ensemble | MISO | 2.13 | 1.86 | -1.49 | -1.87 | 1.49 | -9.36 | 0.60 | 0.03 | 741 | 73714.43 |
| final10s_ensemble | NYIS | 2.26 | 2.00 | -1.14 | -1.82 | 0.54 | -15.25 | 0.62 | 0.64 | 749 | 17417.19 |
| final10s_ensemble | PJM | 2.31 | 2.05 | -1.49 | -1.98 | 1.23 | -11.61 | 0.57 | 0.32 | 735 | 92099.88 |
| final10s_ensemble | SWPP | 2.20 | 1.81 | -1.42 | -2.04 | 1.27 | -20.14 | 0.72 | 0.06 | 744 | 31394.87 |
| final10s_ensemble | TVA | 2.84 | 2.53 | -2.11 | -2.71 | 1.18 | -12.60 | 0.31 | 0.11 | 732 | 18589.75 |
| final10s_recency | BPAT | 3.01 | 2.67 | -1.52 | -2.21 | 1.79 | -18.78 | 0.26 | 0.20 | 749 | 6537.56 |
| final10s_recency | CISO | 4.74 | 4.61 | -3.16 | -3.50 | 0.66 | -12.84 | 0.08 | 0.08 | 722 | 25198.48 |
| final10s_recency | DUK | 3.40 | 3.10 | -1.49 | -2.64 | 1.50 | -15.26 | 0.35 | 0.21 | 747 | 12145.43 |
| final10s_recency | ERCO | 3.29 | 2.74 | -2.58 | -3.16 | 1.09 | -19.04 | 0.32 | 0.14 | 745 | 46853.29 |
| final10s_recency | FPL | 5.63 | 4.90 | -6.42 | -6.82 | 1.14 | -50.47 | 0.36 | 0.27 | 666 | 15342.04 |
| final10s_recency | ISNE | 5.23 | 5.02 | -3.56 | -3.96 | 0.72 | -18.24 | 0.05 | 0.07 | 749 | 13405.84 |
| final10s_recency | MISO | 2.95 | 2.59 | -1.88 | -2.32 | 1.98 | -15.59 | 0.42 | 0.04 | 741 | 73714.43 |
| final10s_recency | NYIS | 3.44 | 3.16 | -1.29 | -2.19 | 0.79 | -20.11 | 0.36 | 0.57 | 749 | 17417.19 |
| final10s_recency | PJM | 2.98 | 2.64 | -1.75 | -2.35 | 1.58 | -16.39 | 0.37 | 0.29 | 735 | 92099.88 |
| final10s_recency | SWPP | 2.81 | 2.40 | -0.86 | -1.91 | 1.64 | -18.61 | 0.65 | 0.08 | 744 | 31394.87 |
| final10s_recency | TVA | 3.35 | 2.99 | -2.31 | -3.08 | 1.22 | -15.37 | 0.22 | 0.15 | 732 | 18589.75 |
| final12l | BPAT | 2.37 | 2.08 | 0.08 | -1.14 | 1.62 | -17.55 | 0.40 | 0.29 | 749 | 6537.56 |
| final12l | CISO | 2.35 | 2.04 | 0.64 | -0.88 | 0.31 | -10.02 | 0.53 | 0.28 | 722 | 25198.48 |
| final12l | DUK | 2.91 | 2.54 | 0.37 | -1.36 | 1.22 | -14.08 | 0.47 | 0.34 | 747 | 12145.43 |
| final12l | ERCO | 2.86 | 2.27 | 0.60 | -1.27 | 0.95 | -17.78 | 0.46 | 0.27 | 745 | 46853.29 |
| final12l | FPL | 3.51 | 3.01 | -0.06 | -2.02 | 0.99 | -46.13 | 0.60 | 0.71 | 666 | 15342.04 |
| final12l | ISNE | 3.02 | 2.71 | 0.55 | -1.10 | 0.44 | -11.13 | 0.38 | 0.22 | 749 | 13405.84 |
| final12l | MISO | 2.03 | 1.73 | 0.23 | -0.92 | 1.58 | -6.96 | 0.63 | 0.07 | 741 | 73714.43 |
| final12l | NYIS | 2.23 | 1.91 | 0.17 | -1.15 | 0.51 | -14.44 | 0.66 | 0.76 | 749 | 17417.19 |
| final12l | PJM | 2.10 | 1.88 | 0.05 | -1.13 | 1.33 | -10.30 | 0.60 | 0.43 | 735 | 92099.88 |
| final12l | SWPP | 2.30 | 1.88 | 0.31 | -1.09 | 1.29 | -19.03 | 0.73 | 0.11 | 744 | 31394.87 |
| final12l | TVA | 2.73 | 2.38 | 0.66 | -1.22 | 1.18 | -12.18 | 0.35 | 0.35 | 732 | 18589.75 |
| final12l_recal | BPAT | 2.29 | 2.02 | -1.27 | -1.89 | 1.69 | -17.64 | 0.44 | 0.19 | 749 | 6537.56 |
| final12l_recal | CISO | 2.27 | 1.97 | -0.40 | -1.34 | 0.34 | -11.58 | 0.55 | 0.22 | 722 | 25198.48 |
| final12l_recal | DUK | 2.81 | 2.51 | -1.30 | -2.21 | 1.27 | -13.99 | 0.49 | 0.24 | 747 | 12145.43 |
| final12l_recal | ERCO | 2.73 | 2.17 | -1.41 | -2.24 | 0.87 | -17.76 | 0.49 | 0.18 | 745 | 46853.29 |
| final12l_recal | FPL | 3.36 | 2.90 | -1.21 | -2.51 | 0.95 | -46.31 | 0.65 | 0.64 | 666 | 15342.04 |
| final12l_recal | ISNE | 2.96 | 2.64 | -0.72 | -1.69 | 0.45 | -15.25 | 0.40 | 0.15 | 749 | 13405.84 |
| final12l_recal | MISO | 1.95 | 1.72 | -0.77 | -1.43 | 1.50 | -7.42 | 0.65 | 0.04 | 741 | 73714.43 |
| final12l_recal | NYIS | 2.16 | 1.89 | -0.75 | -1.59 | 0.52 | -15.04 | 0.68 | 0.67 | 749 | 17417.19 |
| final12l_recal | PJM | 2.06 | 1.83 | -1.11 | -1.75 | 1.17 | -10.73 | 0.65 | 0.33 | 735 | 92099.88 |
| final12l_recal | SWPP | 2.20 | 1.84 | -0.93 | -1.74 | 1.34 | -19.40 | 0.73 | 0.08 | 744 | 31394.87 |
| final12l_recal | TVA | 2.64 | 2.32 | -1.09 | -2.08 | 1.18 | -11.59 | 0.38 | 0.20 | 732 | 18589.75 |

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
| final10s | BPAT | uri | 2.32 | -0.29 | -0.81 | -3.40 | 6 |
| final10s | CISO | uri | 1.95 | -0.21 | -0.90 | -2.04 | 6 |
| final10s | DUK | uri | 4.19 | -3.36 | -3.69 | -8.80 | 6 |
| final10s | ERCO | uri | 6.59 | -8.80 | -8.80 | -9.80 | 2 |
| final10s | FPL | uri | 7.46 | -7.59 | -7.59 | -10.72 | 6 |
| final10s | ISNE | uri | 2.53 | 1.67 | 0.00 | 0.00 | 6 |
| final10s | MISO | uri | 3.90 | -3.34 | -3.50 | -7.14 | 5 |
| final10s | NYIS | uri | 2.17 | 2.25 | -0.08 | -0.46 | 6 |
| final10s | PJM | uri | 1.73 | 0.04 | -0.57 | -2.63 | 6 |
| final10s | SWPP | uri | 6.14 | 0.40 | -2.66 | -5.96 | 4 |
| final10s | TVA | uri | 3.87 | -1.52 | -2.59 | -6.68 | 6 |
| final10s_additive | BPAT | uri | 2.76 | -0.68 | -1.06 | -2.05 | 6 |
| final10s_additive | CISO | uri | 2.15 | 1.10 | -0.12 | -0.66 | 6 |
| final10s_additive | DUK | uri | 3.91 | -3.97 | -3.97 | -6.69 | 6 |
| final10s_additive | ERCO | uri | 5.26 | -6.89 | -6.89 | -9.48 | 2 |
| final10s_additive | FPL | uri | 9.22 | -13.46 | -13.46 | -16.61 | 6 |
| final10s_additive | ISNE | uri | 2.53 | 1.29 | -0.18 | -1.08 | 6 |
| final10s_additive | MISO | uri | 3.65 | -2.66 | -3.20 | -6.58 | 5 |
| final10s_additive | NYIS | uri | 2.58 | 2.75 | 0.00 | 0.00 | 6 |
| final10s_additive | PJM | uri | 2.82 | 2.27 | -0.40 | -2.43 | 6 |
| final10s_additive | SWPP | uri | 6.11 | 2.05 | -1.66 | -4.46 | 4 |
| final10s_additive | TVA | uri | 3.94 | -0.58 | -1.99 | -5.82 | 6 |
| final10s_boosting | BPAT | uri | 2.68 | 0.31 | -1.21 | -5.05 | 6 |
| final10s_boosting | CISO | uri | 1.98 | -0.99 | -1.39 | -3.74 | 6 |
| final10s_boosting | DUK | uri | 3.88 | -5.03 | -5.03 | -9.61 | 6 |
| final10s_boosting | ERCO | uri | 8.66 | -13.62 | -13.62 | -15.74 | 2 |
| final10s_boosting | FPL | uri | 6.80 | -9.32 | -9.32 | -13.79 | 6 |
| final10s_boosting | ISNE | uri | 3.64 | 1.52 | -0.33 | -1.79 | 6 |
| final10s_boosting | MISO | uri | 2.65 | -2.90 | -2.95 | -5.31 | 5 |
| final10s_boosting | NYIS | uri | 2.67 | 1.20 | -0.44 | -2.67 | 6 |
| final10s_boosting | PJM | uri | 1.57 | -0.86 | -1.04 | -2.57 | 6 |
| final10s_boosting | SWPP | uri | 4.88 | -3.23 | -3.99 | -9.76 | 4 |
| final10s_boosting | TVA | uri | 3.13 | -2.41 | -2.41 | -5.95 | 6 |
| final10s_ensemble | BPAT | uri | 2.38 | -0.17 | -0.66 | -3.09 | 6 |
| final10s_ensemble | CISO | uri | 1.88 | -0.52 | -1.07 | -2.07 | 6 |
| final10s_ensemble | DUK | uri | 4.11 | -4.86 | -4.86 | -8.07 | 6 |
| final10s_ensemble | ERCO | uri | 6.37 | -8.91 | -8.91 | -10.45 | 2 |
| final10s_ensemble | FPL | uri | 8.97 | -12.33 | -12.33 | -15.74 | 6 |
| final10s_ensemble | ISNE | uri | 2.29 | 0.31 | -0.38 | -1.68 | 6 |
| final10s_ensemble | MISO | uri | 3.79 | -3.71 | -3.71 | -7.06 | 5 |
| final10s_ensemble | NYIS | uri | 2.21 | 2.01 | -0.09 | -0.56 | 6 |
| final10s_ensemble | PJM | uri | 2.00 | 0.55 | -0.56 | -3.05 | 6 |
| final10s_ensemble | SWPP | uri | 5.84 | -1.15 | -3.33 | -7.30 | 4 |
| final10s_ensemble | TVA | uri | 3.56 | -1.63 | -2.30 | -5.75 | 6 |
| final10s_recency | BPAT | uri | 2.66 | -0.21 | -0.69 | -2.99 | 6 |
| final10s_recency | CISO | uri | 3.72 | -1.78 | -2.10 | -3.69 | 6 |
| final10s_recency | DUK | uri | 4.82 | -5.61 | -5.61 | -8.14 | 6 |
| final10s_recency | ERCO | uri | 6.07 | -5.61 | -5.61 | -10.26 | 2 |
| final10s_recency | FPL | uri | 11.43 | -14.78 | -14.78 | -17.35 | 6 |
| final10s_recency | ISNE | uri | 3.72 | -2.60 | -2.60 | -4.34 | 6 |
| final10s_recency | MISO | uri | 6.74 | -6.06 | -6.06 | -9.68 | 5 |
| final10s_recency | NYIS | uri | 2.47 | 2.02 | -0.03 | -0.17 | 6 |
| final10s_recency | PJM | uri | 2.45 | 0.50 | -0.84 | -4.36 | 6 |
| final10s_recency | SWPP | uri | 6.47 | -2.75 | -4.55 | -10.56 | 4 |
| final10s_recency | TVA | uri | 4.24 | -1.89 | -2.86 | -6.14 | 6 |
| final12l | BPAT | uri | 2.55 | -0.18 | -1.07 | -3.78 | 6 |
| final12l | CISO | uri | 1.85 | 0.23 | -0.53 | -1.92 | 6 |
| final12l | DUK | uri | 4.39 | -2.86 | -3.78 | -10.92 | 6 |
| final12l | ERCO | uri | 3.95 | -5.58 | -5.58 | -7.73 | 2 |
| final12l | FPL | uri | 6.86 | -3.92 | -3.92 | -9.05 | 6 |
| final12l | ISNE | uri | 2.59 | 2.24 | 0.00 | 0.00 | 6 |
| final12l | MISO | uri | 4.17 | -2.75 | -3.37 | -6.96 | 5 |
| final12l | NYIS | uri | 2.04 | 1.93 | -0.21 | -1.28 | 6 |
| final12l | PJM | uri | 1.84 | -1.24 | -1.33 | -2.97 | 6 |
| final12l | SWPP | uri | 6.37 | 3.13 | -1.07 | -2.70 | 4 |
| final12l | TVA | uri | 4.39 | -0.88 | -2.66 | -7.18 | 6 |
| final12l_recal | BPAT | uri | 2.49 | -0.02 | -0.93 | -3.64 | 6 |
| final12l_recal | CISO | uri | 1.73 | 0.01 | -0.61 | -1.80 | 6 |
| final12l_recal | DUK | uri | 4.12 | -4.08 | -4.08 | -9.15 | 6 |
| final12l_recal | ERCO | uri | 3.63 | -5.69 | -5.69 | -8.39 | 2 |
| final12l_recal | FPL | uri | 8.28 | -8.22 | -8.22 | -11.94 | 6 |
| final12l_recal | ISNE | uri | 2.32 | 0.96 | -0.14 | -0.47 | 6 |
| final12l_recal | MISO | uri | 4.14 | -3.41 | -3.64 | -7.40 | 5 |
| final12l_recal | NYIS | uri | 1.95 | 1.60 | -0.23 | -1.38 | 6 |
| final12l_recal | PJM | uri | 1.62 | -0.96 | -1.12 | -3.39 | 6 |
| final12l_recal | SWPP | uri | 6.15 | 1.89 | -1.69 | -3.77 | 4 |
| final12l_recal | TVA | uri | 4.10 | -1.19 | -2.29 | -6.63 | 6 |
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
| final10s | BPAT | elliott | 2.91 | -1.93 | -2.27 | -6.75 | 5 |
| final10s | CISO | elliott | 3.32 | 1.72 | -0.88 | -4.11 | 5 |
| final10s | DUK | elliott | 3.11 | -1.87 | -2.11 | -5.56 | 4 |
| final10s | ERCO | elliott | 5.82 | -2.75 | -3.66 | -8.78 | 5 |
| final10s | FPL | elliott | 5.52 | -5.69 | -5.69 | -9.51 | 5 |
| final10s | ISNE | elliott | 3.31 | 2.54 | -0.40 | -1.26 | 5 |
| final10s | MISO | elliott | 3.64 | -2.86 | -3.52 | -6.79 | 5 |
| final10s | NYIS | elliott | 2.75 | -0.23 | -1.23 | -3.39 | 5 |
| final10s | PJM | elliott | 4.32 | -4.26 | -4.26 | -8.66 | 5 |
| final10s | SWPP | elliott | 4.08 | -0.81 | -2.38 | -7.63 | 5 |
| final10s | TVA | elliott | 4.08 | 0.30 | -0.47 | -1.40 | 3 |
| final10s_additive | BPAT | elliott | 3.92 | -1.21 | -2.06 | -4.69 | 5 |
| final10s_additive | CISO | elliott | 3.01 | 0.82 | -1.16 | -5.50 | 5 |
| final10s_additive | DUK | elliott | 3.89 | -4.32 | -4.32 | -6.30 | 4 |
| final10s_additive | ERCO | elliott | 7.53 | -5.95 | -6.29 | -12.74 | 5 |
| final10s_additive | FPL | elliott | 7.43 | -3.39 | -4.83 | -11.76 | 5 |
| final10s_additive | ISNE | elliott | 3.63 | -0.40 | -1.38 | -4.68 | 5 |
| final10s_additive | MISO | elliott | 3.51 | -3.79 | -4.00 | -6.60 | 5 |
| final10s_additive | NYIS | elliott | 3.50 | -2.55 | -2.60 | -5.35 | 5 |
| final10s_additive | PJM | elliott | 3.37 | -2.64 | -2.64 | -7.54 | 5 |
| final10s_additive | SWPP | elliott | 3.44 | -2.75 | -3.00 | -6.28 | 5 |
| final10s_additive | TVA | elliott | 4.73 | -0.54 | -0.59 | -1.27 | 3 |
| final10s_boosting | BPAT | elliott | 3.59 | -4.87 | -4.87 | -11.14 | 5 |
| final10s_boosting | CISO | elliott | 3.43 | 0.88 | -1.31 | -4.81 | 5 |
| final10s_boosting | DUK | elliott | 4.03 | -3.08 | -3.08 | -6.28 | 4 |
| final10s_boosting | ERCO | elliott | 7.22 | -11.93 | -11.93 | -17.43 | 5 |
| final10s_boosting | FPL | elliott | 8.75 | -13.82 | -13.82 | -20.04 | 5 |
| final10s_boosting | ISNE | elliott | 3.28 | 1.80 | -0.43 | -1.24 | 5 |
| final10s_boosting | MISO | elliott | 3.52 | -2.09 | -3.12 | -4.27 | 5 |
| final10s_boosting | NYIS | elliott | 2.66 | -0.26 | -1.25 | -3.17 | 5 |
| final10s_boosting | PJM | elliott | 3.88 | -4.52 | -4.52 | -7.50 | 5 |
| final10s_boosting | SWPP | elliott | 4.60 | -3.35 | -4.18 | -12.42 | 5 |
| final10s_boosting | TVA | elliott | 4.33 | -2.05 | -2.05 | -3.07 | 3 |
| final10s_ensemble | BPAT | elliott | 3.13 | -2.81 | -3.10 | -7.64 | 5 |
| final10s_ensemble | CISO | elliott | 2.99 | 1.14 | -1.08 | -4.72 | 5 |
| final10s_ensemble | DUK | elliott | 3.60 | -4.60 | -4.60 | -5.80 | 4 |
| final10s_ensemble | ERCO | elliott | 6.43 | -7.92 | -7.92 | -12.26 | 5 |
| final10s_ensemble | FPL | elliott | 7.12 | -9.55 | -9.55 | -13.65 | 5 |
| final10s_ensemble | ISNE | elliott | 3.27 | 0.83 | -0.97 | -3.16 | 5 |
| final10s_ensemble | MISO | elliott | 3.69 | -4.03 | -4.30 | -7.76 | 5 |
| final10s_ensemble | NYIS | elliott | 3.03 | -1.72 | -2.20 | -4.44 | 5 |
| final10s_ensemble | PJM | elliott | 4.16 | -4.98 | -4.98 | -9.90 | 5 |
| final10s_ensemble | SWPP | elliott | 3.99 | -4.19 | -4.46 | -10.42 | 5 |
| final10s_ensemble | TVA | elliott | 4.07 | -2.07 | -2.07 | -2.63 | 3 |
| final10s_recency | BPAT | elliott | 3.69 | -1.70 | -2.65 | -9.33 | 5 |
| final10s_recency | CISO | elliott | 3.75 | 2.01 | -0.71 | -3.54 | 5 |
| final10s_recency | DUK | elliott | 4.08 | -6.68 | -6.68 | -9.35 | 4 |
| final10s_recency | ERCO | elliott | 5.48 | -4.79 | -4.79 | -11.25 | 5 |
| final10s_recency | FPL | elliott | 9.67 | -11.11 | -11.11 | -16.78 | 5 |
| final10s_recency | ISNE | elliott | 4.50 | 1.02 | -1.64 | -3.99 | 5 |
| final10s_recency | MISO | elliott | 6.72 | -7.67 | -7.67 | -15.59 | 5 |
| final10s_recency | NYIS | elliott | 4.46 | -2.95 | -3.31 | -5.91 | 5 |
| final10s_recency | PJM | elliott | 5.96 | -8.01 | -8.01 | -16.39 | 5 |
| final10s_recency | SWPP | elliott | 4.79 | -6.95 | -6.95 | -13.10 | 5 |
| final10s_recency | TVA | elliott | 3.83 | -3.80 | -3.80 | -4.81 | 3 |
| final12l | BPAT | elliott | 2.90 | -1.86 | -2.21 | -6.75 | 5 |
| final12l | CISO | elliott | 3.20 | 1.15 | -1.21 | -4.61 | 5 |
| final12l | DUK | elliott | 3.04 | -0.95 | -1.78 | -5.03 | 4 |
| final12l | ERCO | elliott | 7.68 | 5.40 | -0.23 | -1.17 | 5 |
| final12l | FPL | elliott | 4.23 | -2.58 | -2.65 | -7.23 | 5 |
| final12l | ISNE | elliott | 3.30 | 2.53 | -0.37 | -1.18 | 5 |
| final12l | MISO | elliott | 3.68 | -2.58 | -3.34 | -6.59 | 5 |
| final12l | NYIS | elliott | 2.69 | 0.12 | -1.00 | -2.84 | 5 |
| final12l | PJM | elliott | 4.28 | -3.52 | -3.52 | -8.30 | 5 |
| final12l | SWPP | elliott | 4.66 | 1.07 | -1.48 | -4.79 | 5 |
| final12l | TVA | elliott | 4.08 | 0.68 | -0.60 | -1.79 | 3 |
| final12l_recal | BPAT | elliott | 2.89 | -2.38 | -2.75 | -6.95 | 5 |
| final12l_recal | CISO | elliott | 3.38 | 1.22 | -1.16 | -4.95 | 5 |
| final12l_recal | DUK | elliott | 3.20 | -2.91 | -2.91 | -6.67 | 4 |
| final12l_recal | ERCO | elliott | 5.90 | -2.01 | -2.81 | -6.35 | 5 |
| final12l_recal | FPL | elliott | 4.65 | -4.69 | -4.69 | -9.24 | 5 |
| final12l_recal | ISNE | elliott | 2.98 | 1.34 | -0.78 | -2.70 | 5 |
| final12l_recal | MISO | elliott | 3.73 | -3.47 | -3.99 | -7.30 | 5 |
| final12l_recal | NYIS | elliott | 2.84 | -1.19 | -1.79 | -3.85 | 5 |
| final12l_recal | PJM | elliott | 4.35 | -5.19 | -5.19 | -9.82 | 5 |
| final12l_recal | SWPP | elliott | 4.01 | -1.16 | -2.35 | -7.06 | 5 |
| final12l_recal | TVA | elliott | 3.92 | -0.99 | -0.99 | -2.51 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | final10s_ensemble | eve | 3.07 | -1.00 | -2.18 | 0.54 | 265 |
| 15 | final12l_recal | eve | 3.11 | -0.07 | -1.69 | 0.51 | 265 |
| 9 | final10s | eve | 3.21 | 0.84 | -1.33 | 0.49 | 265 |
| 10 | final10s_additive | eve | 3.29 | -0.80 | -2.19 | 0.50 | 265 |
| 8 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 11 | final10s_boosting | eve | 3.38 | -0.55 | -2.11 | 0.48 | 265 |
| 14 | final12l | eve | 3.41 | 1.31 | -1.19 | 0.46 | 265 |
| 13 | final10s_recency | eve | 3.91 | -2.00 | -3.00 | 0.37 | 265 |
| 7 | final12l_recal | special | 3.11 | -1.50 | -2.43 | 0.58 | 267 |
| 1 | final10s | special | 3.16 | -0.49 | -1.89 | 0.58 | 267 |
| 4 | final10s_ensemble | special | 3.18 | -2.39 | -3.07 | 0.58 | 267 |
| 6 | final12l | special | 3.34 | -0.02 | -1.73 | 0.54 | 267 |
| 2 | final10s_additive | special | 3.39 | -2.49 | -3.21 | 0.52 | 267 |
| 3 | final10s_boosting | special | 3.44 | -2.02 | -2.86 | 0.54 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 5 | final10s_recency | special | 4.14 | -2.94 | -3.86 | 0.45 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10s | all | 0.365 | 1.231 | 0.361 | 0.889 | 10.973 | 0.891 | 14.532 | 1.595 | 7848 |
| final12l | all | 0.381 | 1.291 | 0.383 | 0.888 | 11.518 | 0.892 | 15.286 | 1.674 | 7848 |
| final10s | events | 0.449 | 1.881 | 0.576 | 0.815 | 13.474 | 0.802 | 20.485 | 2.412 | 111 |
| final12l | events | 0.556 | 1.895 | 0.608 | 0.815 | 14.074 | 0.838 | 23.289 | 2.492 | 111 |
| final10s | cold_mornings | 0.448 | 1.559 | 0.485 | 0.880 | 14.226 | 0.861 | 18.654 | 2.035 | 330 |
| final12l | cold_mornings | 0.507 | 1.601 | 0.521 | 0.876 | 15.018 | 0.855 | 20.554 | 2.115 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 17695 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 17692 | DUK | 2022-12-24 | final10s | 9.66 | -11.22 | -11.22 |
| 17688 | DUK | 2022-12-24 | final10s_additive | 8.92 | -12.68 | -12.68 |
| 17689 | DUK | 2022-12-24 | final10s_boosting | 10.90 | -17.09 | -17.09 |
| 17691 | DUK | 2022-12-24 | final10s_ensemble | 10.08 | -13.84 | -13.84 |
| 17690 | DUK | 2022-12-24 | final10s_recency | 10.63 | -11.43 | -11.43 |
| 17694 | DUK | 2022-12-24 | final12l | 9.57 | -10.16 | -10.16 |
| 17693 | DUK | 2022-12-24 | final12l_recal | 9.77 | -11.36 | -11.36 |
| 18351 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 18348 | ERCO | 2021-02-17 | final10s | 31.81 | 25.11 | 0.00 |
| 18344 | ERCO | 2021-02-17 | final10s_additive | 29.56 | 25.22 | 0.00 |
| 18345 | ERCO | 2021-02-17 | final10s_boosting | 28.85 | 23.03 | 0.00 |
| 18347 | ERCO | 2021-02-17 | final10s_ensemble | 31.76 | 26.20 | 0.00 |
| 18346 | ERCO | 2021-02-17 | final10s_recency | 38.48 | 31.79 | 0.00 |
| 18350 | ERCO | 2021-02-17 | final12l | 26.82 | 16.72 | 0.00 |
| 18349 | ERCO | 2021-02-17 | final12l_recal | 26.90 | 18.43 | 0.00 |
| 18359 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 18356 | ERCO | 2021-02-18 | final10s | 4.22 | 2.65 | 0.00 |
| 18352 | ERCO | 2021-02-18 | final10s_additive | 13.29 | 11.84 | 0.00 |
| 18353 | ERCO | 2021-02-18 | final10s_boosting | 4.23 | -7.71 | -7.71 |
| 18355 | ERCO | 2021-02-18 | final10s_ensemble | 4.31 | 1.50 | 0.00 |
| 18354 | ERCO | 2021-02-18 | final10s_recency | 5.36 | 2.19 | 0.00 |
| 18358 | ERCO | 2021-02-18 | final12l | 1.90 | -1.46 | -1.46 |
| 18357 | ERCO | 2021-02-18 | final12l_recal | 1.79 | -2.57 | -2.57 |
| 35655 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 35652 | MISO | 2021-02-16 | final10s | 1.65 | 1.40 | 0.00 |
| 35648 | MISO | 2021-02-16 | final10s_additive | 2.24 | 2.04 | 0.00 |
| 35649 | MISO | 2021-02-16 | final10s_boosting | 1.52 | 0.96 | 0.00 |
| 35651 | MISO | 2021-02-16 | final10s_ensemble | 1.56 | 0.51 | 0.00 |
| 35650 | MISO | 2021-02-16 | final10s_recency | 3.83 | -2.20 | -2.20 |
| 35654 | MISO | 2021-02-16 | final12l | 2.01 | 2.59 | 0.00 |
| 35653 | MISO | 2021-02-16 | final12l_recal | 1.74 | 1.81 | 0.00 |
| 53455 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 53452 | SWPP | 2021-02-15 | final10s | 2.48 | -2.09 | -2.09 |
| 53448 | SWPP | 2021-02-15 | final10s_additive | 2.57 | 1.33 | 0.00 |
| 53449 | SWPP | 2021-02-15 | final10s_boosting | 6.68 | -8.01 | -8.01 |
| 53451 | SWPP | 2021-02-15 | final10s_ensemble | 2.87 | -3.68 | -3.68 |
| 53450 | SWPP | 2021-02-15 | final10s_recency | 4.67 | -4.95 | -4.95 |
| 53454 | SWPP | 2021-02-15 | final12l | 3.03 | 1.17 | 0.00 |
| 53453 | SWPP | 2021-02-15 | final12l_recal | 2.48 | -0.11 | -0.11 |
| 53463 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 53460 | SWPP | 2021-02-16 | final10s | 4.01 | 0.22 | 0.00 |
| 53456 | SWPP | 2021-02-16 | final10s_additive | 7.69 | 3.65 | 0.00 |
| 53457 | SWPP | 2021-02-16 | final10s_boosting | 3.28 | -6.32 | -6.32 |
| 53459 | SWPP | 2021-02-16 | final10s_ensemble | 3.80 | -0.84 | -0.84 |
| 53458 | SWPP | 2021-02-16 | final10s_recency | 2.38 | -0.44 | -0.44 |
| 53462 | SWPP | 2021-02-16 | final12l | 8.10 | 3.72 | 0.00 |
| 53461 | SWPP | 2021-02-16 | final12l_recal | 7.52 | 2.62 | 0.00 |
| 64631 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 64628 | TVA | 2022-12-23 | final10s | 9.58 | -11.20 | -11.20 |
| 64624 | TVA | 2022-12-23 | final10s_additive | 6.10 | -4.61 | -4.61 |
| 64625 | TVA | 2022-12-23 | final10s_boosting | 15.03 | -15.47 | -15.47 |
| 64627 | TVA | 2022-12-23 | final10s_ensemble | 9.72 | -10.91 | -10.91 |
| 64626 | TVA | 2022-12-23 | final10s_recency | 10.25 | -13.32 | -13.32 |
| 64630 | TVA | 2022-12-23 | final12l | 9.81 | -12.32 | -12.32 |
| 64629 | TVA | 2022-12-23 | final12l_recal | 9.68 | -12.10 | -12.10 |
| 64639 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 64636 | TVA | 2022-12-24 | final10s | 6.03 | -13.09 | -13.09 |
| 64632 | TVA | 2022-12-24 | final10s_additive | 4.10 | -10.03 | -10.03 |
| 64633 | TVA | 2022-12-24 | final10s_boosting | 7.18 | -15.19 | -15.19 |
| 64635 | TVA | 2022-12-24 | final10s_ensemble | 6.22 | -12.64 | -12.64 |
| 64634 | TVA | 2022-12-24 | final10s_recency | 7.90 | -12.89 | -12.89 |
| 64638 | TVA | 2022-12-24 | final12l | 6.38 | -13.48 | -13.48 |
| 64637 | TVA | 2022-12-24 | final12l_recal | 6.15 | -13.22 | -13.22 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final10s | BPAT | mape | 4.683 | 0.000 | 749 |
| final10s | CISO | mape | -2.500 | 0.012 | 722 |
| final10s | DUK | mape | -0.608 | 0.543 | 747 |
| final10s | ERCO | mape | -3.057 | 0.002 | 745 |
| final10s | FPL | mape | -5.835 | 0.000 | 666 |
| final10s | ISNE | mape | 11.742 | 0.000 | 749 |
| final10s | MISO | mape | -11.797 | 0.000 | 741 |
| final10s | NYIS | mape | -7.764 | 0.000 | 749 |
| final10s | PJM | mape | -9.313 | 0.000 | 735 |
| final10s | SWPP | mape | -18.282 | 0.000 | 744 |
| final10s | TVA | mape | 7.568 | 0.000 | 732 |
| final10s_additive | BPAT | mape | 8.822 | 0.000 | 749 |
| final10s_additive | CISO | mape | 5.631 | 0.000 | 722 |
| final10s_additive | DUK | mape | 4.810 | 0.000 | 747 |
| final10s_additive | ERCO | mape | 9.376 | 0.000 | 745 |
| final10s_additive | FPL | mape | 7.146 | 0.000 | 666 |
| final10s_additive | ISNE | mape | 19.698 | 0.000 | 749 |
| final10s_additive | MISO | mape | -4.992 | 0.000 | 741 |
| final10s_additive | NYIS | mape | -1.257 | 0.209 | 749 |
| final10s_additive | PJM | mape | 2.180 | 0.029 | 735 |
| final10s_additive | SWPP | mape | -13.905 | 0.000 | 744 |
| final10s_additive | TVA | mape | 16.869 | 0.000 | 732 |
| final10s_boosting | BPAT | mape | 5.846 | 0.000 | 749 |
| final10s_boosting | CISO | mape | 1.834 | 0.067 | 722 |
| final10s_boosting | DUK | mape | 2.126 | 0.033 | 747 |
| final10s_boosting | ERCO | mape | 1.164 | 0.245 | 745 |
| final10s_boosting | FPL | mape | 0.612 | 0.541 | 666 |
| final10s_boosting | ISNE | mape | 15.349 | 0.000 | 749 |
| final10s_boosting | MISO | mape | -7.443 | 0.000 | 741 |
| final10s_boosting | NYIS | mape | -5.863 | 0.000 | 749 |
| final10s_boosting | PJM | mape | -2.017 | 0.044 | 735 |
| final10s_boosting | SWPP | mape | -13.744 | 0.000 | 744 |
| final10s_boosting | TVA | mape | 11.467 | 0.000 | 732 |
| final10s_ensemble | BPAT | mape | 4.486 | 0.000 | 749 |
| final10s_ensemble | CISO | mape | 2.125 | 0.034 | 722 |
| final10s_ensemble | DUK | mape | 0.134 | 0.894 | 747 |
| final10s_ensemble | ERCO | mape | 1.360 | 0.174 | 745 |
| final10s_ensemble | FPL | mape | 4.828 | 0.000 | 666 |
| final10s_ensemble | ISNE | mape | 17.085 | 0.000 | 749 |
| final10s_ensemble | MISO | mape | -7.559 | 0.000 | 741 |
| final10s_ensemble | NYIS | mape | -7.274 | 0.000 | 749 |
| final10s_ensemble | PJM | mape | -3.125 | 0.002 | 735 |
| final10s_ensemble | SWPP | mape | -17.687 | 0.000 | 744 |
| final10s_ensemble | TVA | mape | 11.683 | 0.000 | 732 |
| final10s_recency | BPAT | mape | 15.098 | 0.000 | 749 |
| final10s_recency | CISO | mape | 35.747 | 0.000 | 722 |
| final10s_recency | DUK | mape | 9.074 | 0.000 | 747 |
| final10s_recency | ERCO | mape | 8.848 | 0.000 | 745 |
| final10s_recency | FPL | mape | 13.371 | 0.000 | 666 |
| final10s_recency | ISNE | mape | 38.674 | 0.000 | 749 |
| final10s_recency | MISO | mape | 3.697 | 0.000 | 741 |
| final10s_recency | NYIS | mape | 10.823 | 0.000 | 749 |
| final10s_recency | PJM | mape | 9.266 | 0.000 | 735 |
| final10s_recency | SWPP | mape | -10.439 | 0.000 | 744 |
| final10s_recency | TVA | mape | 17.916 | 0.000 | 732 |
| final12l | BPAT | mape | 6.286 | 0.000 | 749 |
| final12l | CISO | mape | -0.855 | 0.393 | 722 |
| final12l | DUK | mape | 1.272 | 0.203 | 747 |
| final12l | ERCO | mape | 3.610 | 0.000 | 745 |
| final12l | FPL | mape | -4.405 | 0.000 | 666 |
| final12l | ISNE | mape | 11.977 | 0.000 | 749 |
| final12l | MISO | mape | -10.412 | 0.000 | 741 |
| final12l | NYIS | mape | -7.044 | 0.000 | 749 |
| final12l | PJM | mape | -7.069 | 0.000 | 735 |
| final12l | SWPP | mape | -17.686 | 0.000 | 744 |
| final12l | TVA | mape | 10.138 | 0.000 | 732 |
| final12l_recal | BPAT | mape | 4.690 | 0.000 | 749 |
| final12l_recal | CISO | mape | -2.348 | 0.019 | 722 |
| final12l_recal | DUK | mape | -0.514 | 0.607 | 747 |
| final12l_recal | ERCO | mape | 1.525 | 0.127 | 745 |
| final12l_recal | FPL | mape | -6.203 | 0.000 | 666 |
| final12l_recal | ISNE | mape | 11.034 | 0.000 | 749 |
| final12l_recal | MISO | mape | -11.072 | 0.000 | 741 |
| final12l_recal | NYIS | mape | -8.788 | 0.000 | 749 |
| final12l_recal | PJM | mape | -8.348 | 0.000 | 735 |
| final12l_recal | SWPP | mape | -18.310 | 0.000 | 744 |
| final12l_recal | TVA | mape | 8.546 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final10s | 0.990 |
| final10s_additive | 0.967 |
| final10s_boosting | 0.990 |
| final10s_ensemble | 0.990 |
| final10s_recency | 0.990 |
| final12l | 0.990 |
| final12l_recal | 0.990 |
