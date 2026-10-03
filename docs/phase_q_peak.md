# Phase Q: a second stage for the daily peak

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final10s` is the recipe after phase P. `final11m`, `final11r` and `final11x` multiply its whole band by a bump centred on the hour of the forecast peak (Gaussian, 2.5 h), so that the forecast maximum is scaled by a ratio and the hours far from the peak do not move: `final11m` by the mean of the members' own daily maxima over the issued maximum (never below 1); `final11r` by a ridge regression of log(actual / issued) at the hour of the actual peak on the known days (features: the members' flattening and disagreement at the peak, excess of the forecast maximum and minimum over the station's known extremes, NBM spread, day type, special day, the median ratio of the last 14 known days); `final11x` is `final11r` only on days of extreme forecast temperature (above the 90th or below the 10th percentile of the known daily extremes). See `src/ba_load_forecast/forecasters/peak.py`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final11r | 2.25 | 1.92 | -0.11 | -1.23 | 1.13 | 0.61 | 0.29 | -46.59 | 8079 | 11.00 |
| final11x | 2.26 | 1.93 | -0.09 | -1.24 | 1.13 | 0.61 | 0.29 | -46.62 | 8079 | 11.00 |
| final10s | 2.26 | 1.94 | -0.04 | -1.22 | 1.12 | 0.61 | 0.29 | -46.62 | 8079 | 11.00 |
| final11m | 2.26 | 1.93 | 0.00 | -1.19 | 1.12 | 0.60 | 0.30 | -46.62 | 8079 | 11.00 |
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
| final10s_ensemble | NYIS | 2.26 | 2.00 | -1.13 | -1.82 | 0.54 | -15.25 | 0.61 | 0.64 | 749 | 17417.19 |
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
| final11m | BPAT | 2.29 | 2.03 | -0.15 | -1.21 | 1.60 | -17.41 | 0.44 | 0.27 | 749 | 6537.56 |
| final11m | CISO | 2.27 | 1.97 | 0.28 | -0.99 | 0.34 | -11.04 | 0.56 | 0.27 | 722 | 25198.48 |
| final11m | DUK | 2.81 | 2.51 | 0.04 | -1.48 | 1.18 | -13.20 | 0.50 | 0.32 | 747 | 12145.43 |
| final11m | ERCO | 2.45 | 1.96 | -0.08 | -1.32 | 0.88 | -17.51 | 0.54 | 0.27 | 745 | 46853.29 |
| final11m | FPL | 3.37 | 2.81 | -0.16 | -1.90 | 0.97 | -46.62 | 0.64 | 0.70 | 666 | 15342.04 |
| final11m | ISNE | 3.00 | 2.70 | 0.21 | -1.24 | 0.49 | -13.56 | 0.39 | 0.20 | 749 | 13405.84 |
| final11m | MISO | 1.95 | 1.69 | 0.09 | -0.97 | 1.47 | -6.98 | 0.65 | 0.06 | 741 | 73714.43 |
| final11m | NYIS | 2.20 | 1.90 | 0.00 | -1.22 | 0.53 | -14.02 | 0.65 | 0.74 | 749 | 17417.19 |
| final11m | PJM | 2.00 | 1.75 | -0.15 | -1.15 | 1.30 | -10.45 | 0.65 | 0.43 | 735 | 92099.88 |
| final11m | SWPP | 2.22 | 1.83 | -0.04 | -1.25 | 1.30 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final11m | TVA | 2.58 | 2.24 | 0.31 | -1.29 | 1.13 | -11.14 | 0.39 | 0.32 | 732 | 18589.75 |
| final11r | BPAT | 2.27 | 1.99 | -0.39 | -1.29 | 1.59 | -17.21 | 0.44 | 0.25 | 749 | 6537.56 |
| final11r | CISO | 2.25 | 1.98 | 0.01 | -1.11 | 0.34 | -11.61 | 0.57 | 0.25 | 722 | 25198.48 |
| final11r | DUK | 2.80 | 2.48 | -0.07 | -1.52 | 1.16 | -13.46 | 0.51 | 0.32 | 747 | 12145.43 |
| final11r | ERCO | 2.48 | 1.97 | -0.23 | -1.43 | 0.91 | -17.51 | 0.54 | 0.26 | 745 | 46853.29 |
| final11r | FPL | 3.37 | 2.80 | 0.30 | -1.70 | 0.98 | -46.59 | 0.63 | 0.73 | 666 | 15342.04 |
| final11r | ISNE | 3.00 | 2.70 | 0.24 | -1.21 | 0.49 | -13.56 | 0.38 | 0.20 | 749 | 13405.84 |
| final11r | MISO | 1.93 | 1.66 | -0.14 | -1.04 | 1.50 | -7.14 | 0.66 | 0.06 | 741 | 73714.43 |
| final11r | NYIS | 2.18 | 1.88 | -0.12 | -1.25 | 0.52 | -13.50 | 0.66 | 0.73 | 749 | 17417.19 |
| final11r | PJM | 2.00 | 1.73 | -0.14 | -1.14 | 1.31 | -10.45 | 0.65 | 0.43 | 735 | 92099.88 |
| final11r | SWPP | 2.18 | 1.77 | -0.27 | -1.31 | 1.28 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final11r | TVA | 2.56 | 2.21 | 0.04 | -1.39 | 1.14 | -11.14 | 0.41 | 0.30 | 732 | 18589.75 |
| final11x | BPAT | 2.29 | 2.01 | -0.47 | -1.38 | 1.58 | -17.41 | 0.45 | 0.25 | 749 | 6537.56 |
| final11x | CISO | 2.26 | 1.98 | 0.21 | -1.03 | 0.34 | -11.32 | 0.56 | 0.27 | 722 | 25198.48 |
| final11x | DUK | 2.80 | 2.50 | -0.13 | -1.57 | 1.18 | -13.46 | 0.51 | 0.31 | 747 | 12145.43 |
| final11x | ERCO | 2.46 | 1.96 | -0.26 | -1.44 | 0.91 | -17.51 | 0.54 | 0.26 | 745 | 46853.29 |
| final11x | FPL | 3.36 | 2.81 | -0.17 | -1.91 | 0.98 | -46.62 | 0.64 | 0.70 | 666 | 15342.04 |
| final11x | ISNE | 3.00 | 2.70 | 0.21 | -1.24 | 0.49 | -13.56 | 0.38 | 0.21 | 749 | 13405.84 |
| final11x | MISO | 1.95 | 1.67 | 0.03 | -1.00 | 1.47 | -7.14 | 0.66 | 0.06 | 741 | 73714.43 |
| final11x | NYIS | 2.19 | 1.88 | -0.11 | -1.27 | 0.53 | -14.02 | 0.65 | 0.73 | 749 | 17417.19 |
| final11x | PJM | 2.00 | 1.76 | -0.19 | -1.18 | 1.30 | -10.45 | 0.65 | 0.42 | 735 | 92099.88 |
| final11x | SWPP | 2.20 | 1.81 | -0.18 | -1.31 | 1.31 | -19.15 | 0.74 | 0.09 | 744 | 31394.87 |
| final11x | TVA | 2.57 | 2.24 | 0.15 | -1.36 | 1.13 | -11.14 | 0.40 | 0.31 | 732 | 18589.75 |

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
| final11m | BPAT | uri | 2.33 | 0.01 | -0.64 | -3.40 | 6 |
| final11m | CISO | uri | 1.95 | -0.20 | -0.88 | -2.03 | 6 |
| final11m | DUK | uri | 4.18 | -3.36 | -3.69 | -8.80 | 6 |
| final11m | ERCO | uri | 6.19 | -7.28 | -7.28 | -9.15 | 2 |
| final11m | FPL | uri | 7.46 | -7.59 | -7.59 | -10.72 | 6 |
| final11m | ISNE | uri | 2.53 | 1.67 | 0.00 | 0.00 | 6 |
| final11m | MISO | uri | 3.88 | -3.26 | -3.42 | -6.98 | 5 |
| final11m | NYIS | uri | 2.17 | 2.25 | -0.08 | -0.46 | 6 |
| final11m | PJM | uri | 1.78 | 0.59 | -0.43 | -2.32 | 6 |
| final11m | SWPP | uri | 6.14 | 0.40 | -2.66 | -5.96 | 4 |
| final11m | TVA | uri | 3.84 | -1.40 | -2.47 | -6.54 | 6 |
| final11r | BPAT | uri | 2.32 | -0.29 | -0.81 | -3.40 | 6 |
| final11r | CISO | uri | 1.95 | -0.21 | -0.90 | -2.04 | 6 |
| final11r | DUK | uri | 4.19 | -3.36 | -3.69 | -8.80 | 6 |
| final11r | ERCO | uri | 6.59 | -8.80 | -8.80 | -9.80 | 2 |
| final11r | FPL | uri | 7.46 | -7.59 | -7.59 | -10.72 | 6 |
| final11r | ISNE | uri | 2.53 | 1.67 | 0.00 | 0.00 | 6 |
| final11r | MISO | uri | 3.90 | -3.34 | -3.50 | -7.14 | 5 |
| final11r | NYIS | uri | 2.17 | 2.25 | -0.08 | -0.46 | 6 |
| final11r | PJM | uri | 1.73 | 0.04 | -0.57 | -2.63 | 6 |
| final11r | SWPP | uri | 6.14 | 0.40 | -2.66 | -5.96 | 4 |
| final11r | TVA | uri | 3.87 | -1.52 | -2.59 | -6.68 | 6 |
| final11x | BPAT | uri | 2.32 | -0.29 | -0.81 | -3.40 | 6 |
| final11x | CISO | uri | 1.95 | -0.21 | -0.90 | -2.04 | 6 |
| final11x | DUK | uri | 4.19 | -3.36 | -3.69 | -8.80 | 6 |
| final11x | ERCO | uri | 6.59 | -8.80 | -8.80 | -9.80 | 2 |
| final11x | FPL | uri | 7.46 | -7.59 | -7.59 | -10.72 | 6 |
| final11x | ISNE | uri | 2.53 | 1.67 | 0.00 | 0.00 | 6 |
| final11x | MISO | uri | 3.90 | -3.34 | -3.50 | -7.14 | 5 |
| final11x | NYIS | uri | 2.17 | 2.25 | -0.08 | -0.46 | 6 |
| final11x | PJM | uri | 1.73 | 0.04 | -0.57 | -2.63 | 6 |
| final11x | SWPP | uri | 6.14 | 0.40 | -2.66 | -5.96 | 4 |
| final11x | TVA | uri | 3.87 | -1.52 | -2.59 | -6.68 | 6 |
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
| final11m | BPAT | elliott | 2.91 | -1.93 | -2.27 | -6.75 | 5 |
| final11m | CISO | elliott | 3.32 | 1.86 | -0.79 | -3.94 | 5 |
| final11m | DUK | elliott | 3.08 | -1.69 | -1.93 | -4.84 | 4 |
| final11m | ERCO | elliott | 5.82 | -2.75 | -3.66 | -8.78 | 5 |
| final11m | FPL | elliott | 5.51 | -5.52 | -5.52 | -9.51 | 5 |
| final11m | ISNE | elliott | 3.31 | 2.54 | -0.40 | -1.26 | 5 |
| final11m | MISO | elliott | 3.62 | -2.85 | -3.51 | -6.72 | 5 |
| final11m | NYIS | elliott | 2.75 | -0.23 | -1.23 | -3.39 | 5 |
| final11m | PJM | elliott | 4.32 | -4.26 | -4.26 | -8.66 | 5 |
| final11m | SWPP | elliott | 4.08 | -0.81 | -2.38 | -7.63 | 5 |
| final11m | TVA | elliott | 4.07 | 0.43 | -0.33 | -1.00 | 3 |
| final11r | BPAT | elliott | 2.95 | -1.99 | -2.55 | -5.50 | 5 |
| final11r | CISO | elliott | 3.34 | 1.29 | -1.23 | -4.98 | 5 |
| final11r | DUK | elliott | 2.80 | 1.02 | -0.45 | -1.80 | 4 |
| final11r | ERCO | elliott | 6.26 | -5.31 | -6.03 | -11.65 | 5 |
| final11r | FPL | elliott | 5.91 | -7.45 | -7.45 | -10.11 | 5 |
| final11r | ISNE | elliott | 3.40 | 3.56 | -0.10 | -0.29 | 5 |
| final11r | MISO | elliott | 3.57 | -2.51 | -3.26 | -6.33 | 5 |
| final11r | NYIS | elliott | 2.81 | -0.43 | -1.34 | -3.27 | 5 |
| final11r | PJM | elliott | 4.50 | -4.26 | -4.26 | -8.66 | 5 |
| final11r | SWPP | elliott | 4.04 | -0.97 | -2.38 | -7.14 | 5 |
| final11r | TVA | elliott | 4.15 | 1.27 | -0.16 | -0.47 | 3 |
| final11x | BPAT | elliott | 2.89 | -2.50 | -2.80 | -6.75 | 5 |
| final11x | CISO | elliott | 3.32 | 1.72 | -0.88 | -4.11 | 5 |
| final11x | DUK | elliott | 2.79 | 0.90 | -0.57 | -2.28 | 4 |
| final11x | ERCO | elliott | 6.26 | -5.31 | -6.03 | -11.65 | 5 |
| final11x | FPL | elliott | 5.87 | -7.19 | -7.19 | -10.11 | 5 |
| final11x | ISNE | elliott | 3.43 | 3.46 | -0.21 | -0.75 | 5 |
| final11x | MISO | elliott | 3.57 | -2.51 | -3.26 | -6.33 | 5 |
| final11x | NYIS | elliott | 2.76 | -0.22 | -1.13 | -3.27 | 5 |
| final11x | PJM | elliott | 4.48 | -4.26 | -4.26 | -8.66 | 5 |
| final11x | SWPP | elliott | 4.04 | -0.97 | -2.38 | -7.14 | 5 |
| final11x | TVA | elliott | 4.15 | 1.27 | -0.16 | -0.47 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | final10s_ensemble | eve | 3.07 | -1.00 | -2.18 | 0.54 | 265 |
| 15 | final11m | eve | 3.21 | 0.89 | -1.30 | 0.49 | 265 |
| 10 | final10s | eve | 3.21 | 0.84 | -1.33 | 0.49 | 265 |
| 17 | final11x | eve | 3.22 | 0.76 | -1.39 | 0.49 | 265 |
| 16 | final11r | eve | 3.23 | 0.97 | -1.30 | 0.48 | 265 |
| 11 | final10s_additive | eve | 3.29 | -0.80 | -2.19 | 0.50 | 265 |
| 9 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 12 | final10s_boosting | eve | 3.38 | -0.55 | -2.11 | 0.48 | 265 |
| 14 | final10s_recency | eve | 3.91 | -2.00 | -3.00 | 0.37 | 265 |
| 1 | final10s | special | 3.16 | -0.49 | -1.89 | 0.58 | 267 |
| 6 | final11m | special | 3.16 | -0.44 | -1.86 | 0.57 | 267 |
| 8 | final11x | special | 3.17 | -0.55 | -1.95 | 0.58 | 267 |
| 4 | final10s_ensemble | special | 3.18 | -2.39 | -3.07 | 0.58 | 267 |
| 7 | final11r | special | 3.20 | -0.34 | -1.86 | 0.60 | 267 |
| 2 | final10s_additive | special | 3.39 | -2.49 | -3.21 | 0.52 | 267 |
| 3 | final10s_boosting | special | 3.44 | -2.02 | -2.86 | 0.54 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 5 | final10s_recency | special | 4.14 | -2.94 | -3.86 | 0.45 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10s | all | 0.365 | 1.231 | 0.361 | 0.889 | 10.973 | 0.891 | 14.532 | 1.595 | 7848 |
| final11m | all | 0.365 | 1.231 | 0.361 | 0.889 | 10.968 | 0.892 | 14.532 | 1.595 | 7848 |
| final11r | all | 0.364 | 1.226 | 0.361 | 0.889 | 10.975 | 0.889 | 14.508 | 1.589 | 7848 |
| final11x | all | 0.366 | 1.230 | 0.361 | 0.889 | 10.976 | 0.890 | 14.539 | 1.594 | 7848 |
| final10s | events | 0.449 | 1.881 | 0.576 | 0.815 | 13.474 | 0.802 | 20.485 | 2.412 | 111 |
| final11m | events | 0.448 | 1.876 | 0.577 | 0.814 | 13.451 | 0.802 | 20.495 | 2.405 | 111 |
| final11r | events | 0.456 | 1.901 | 0.582 | 0.810 | 13.520 | 0.784 | 20.761 | 2.439 | 111 |
| final11x | events | 0.454 | 1.897 | 0.581 | 0.810 | 13.531 | 0.784 | 20.696 | 2.436 | 111 |
| final10s | cold_mornings | 0.448 | 1.559 | 0.485 | 0.880 | 14.226 | 0.861 | 18.654 | 2.035 | 330 |
| final11m | cold_mornings | 0.449 | 1.556 | 0.483 | 0.881 | 14.214 | 0.867 | 18.636 | 2.031 | 330 |
| final11r | cold_mornings | 0.451 | 1.586 | 0.490 | 0.876 | 14.202 | 0.845 | 18.820 | 2.067 | 330 |
| final11x | cold_mornings | 0.453 | 1.586 | 0.490 | 0.876 | 14.268 | 0.852 | 18.860 | 2.067 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 19907 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 19903 | DUK | 2022-12-24 | final10s | 9.66 | -11.22 | -11.22 |
| 19899 | DUK | 2022-12-24 | final10s_additive | 8.92 | -12.68 | -12.68 |
| 19900 | DUK | 2022-12-24 | final10s_boosting | 10.90 | -17.09 | -17.09 |
| 19902 | DUK | 2022-12-24 | final10s_ensemble | 10.08 | -13.84 | -13.84 |
| 19901 | DUK | 2022-12-24 | final10s_recency | 10.63 | -11.43 | -11.43 |
| 19904 | DUK | 2022-12-24 | final11m | 9.66 | -11.22 | -11.22 |
| 19905 | DUK | 2022-12-24 | final11r | 8.51 | -8.03 | -8.03 |
| 19906 | DUK | 2022-12-24 | final11x | 8.51 | -8.03 | -8.03 |
| 20645 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 20641 | ERCO | 2021-02-17 | final10s | 31.81 | 25.11 | 0.00 |
| 20637 | ERCO | 2021-02-17 | final10s_additive | 29.56 | 25.22 | 0.00 |
| 20638 | ERCO | 2021-02-17 | final10s_boosting | 28.85 | 23.03 | 0.00 |
| 20640 | ERCO | 2021-02-17 | final10s_ensemble | 31.76 | 26.20 | 0.00 |
| 20639 | ERCO | 2021-02-17 | final10s_recency | 38.48 | 31.79 | 0.00 |
| 20642 | ERCO | 2021-02-17 | final11m | 31.81 | 25.11 | 0.00 |
| 20643 | ERCO | 2021-02-17 | final11r | 31.81 | 25.11 | 0.00 |
| 20644 | ERCO | 2021-02-17 | final11x | 31.81 | 25.11 | 0.00 |
| 20654 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 20650 | ERCO | 2021-02-18 | final10s | 4.22 | 2.65 | 0.00 |
| 20646 | ERCO | 2021-02-18 | final10s_additive | 13.29 | 11.84 | 0.00 |
| 20647 | ERCO | 2021-02-18 | final10s_boosting | 4.23 | -7.71 | -7.71 |
| 20649 | ERCO | 2021-02-18 | final10s_ensemble | 4.31 | 1.50 | 0.00 |
| 20648 | ERCO | 2021-02-18 | final10s_recency | 5.36 | 2.19 | 0.00 |
| 20651 | ERCO | 2021-02-18 | final11m | 4.53 | 2.66 | 0.00 |
| 20652 | ERCO | 2021-02-18 | final11r | 4.22 | 2.65 | 0.00 |
| 20653 | ERCO | 2021-02-18 | final11x | 4.22 | 2.65 | 0.00 |
| 40112 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 40108 | MISO | 2021-02-16 | final10s | 1.65 | 1.40 | 0.00 |
| 40104 | MISO | 2021-02-16 | final10s_additive | 2.24 | 2.04 | 0.00 |
| 40105 | MISO | 2021-02-16 | final10s_boosting | 1.52 | 0.96 | 0.00 |
| 40107 | MISO | 2021-02-16 | final10s_ensemble | 1.56 | 0.51 | 0.00 |
| 40106 | MISO | 2021-02-16 | final10s_recency | 3.83 | -2.20 | -2.20 |
| 40109 | MISO | 2021-02-16 | final11m | 1.65 | 1.40 | 0.00 |
| 40110 | MISO | 2021-02-16 | final11r | 1.65 | 1.40 | 0.00 |
| 40111 | MISO | 2021-02-16 | final11x | 1.65 | 1.40 | 0.00 |
| 60137 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 60133 | SWPP | 2021-02-15 | final10s | 2.48 | -2.09 | -2.09 |
| 60129 | SWPP | 2021-02-15 | final10s_additive | 2.57 | 1.33 | 0.00 |
| 60130 | SWPP | 2021-02-15 | final10s_boosting | 6.68 | -8.01 | -8.01 |
| 60132 | SWPP | 2021-02-15 | final10s_ensemble | 2.87 | -3.68 | -3.68 |
| 60131 | SWPP | 2021-02-15 | final10s_recency | 4.67 | -4.95 | -4.95 |
| 60134 | SWPP | 2021-02-15 | final11m | 2.48 | -2.09 | -2.09 |
| 60135 | SWPP | 2021-02-15 | final11r | 2.48 | -2.09 | -2.09 |
| 60136 | SWPP | 2021-02-15 | final11x | 2.48 | -2.09 | -2.09 |
| 60146 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 60142 | SWPP | 2021-02-16 | final10s | 4.01 | 0.22 | 0.00 |
| 60138 | SWPP | 2021-02-16 | final10s_additive | 7.69 | 3.65 | 0.00 |
| 60139 | SWPP | 2021-02-16 | final10s_boosting | 3.28 | -6.32 | -6.32 |
| 60141 | SWPP | 2021-02-16 | final10s_ensemble | 3.80 | -0.84 | -0.84 |
| 60140 | SWPP | 2021-02-16 | final10s_recency | 2.38 | -0.44 | -0.44 |
| 60143 | SWPP | 2021-02-16 | final11m | 4.01 | 0.22 | 0.00 |
| 60144 | SWPP | 2021-02-16 | final11r | 4.01 | 0.22 | 0.00 |
| 60145 | SWPP | 2021-02-16 | final11x | 4.01 | 0.22 | 0.00 |
| 72710 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 72706 | TVA | 2022-12-23 | final10s | 9.58 | -11.20 | -11.20 |
| 72702 | TVA | 2022-12-23 | final10s_additive | 6.10 | -4.61 | -4.61 |
| 72703 | TVA | 2022-12-23 | final10s_boosting | 15.03 | -15.47 | -15.47 |
| 72705 | TVA | 2022-12-23 | final10s_ensemble | 9.72 | -10.91 | -10.91 |
| 72704 | TVA | 2022-12-23 | final10s_recency | 10.25 | -13.32 | -13.32 |
| 72707 | TVA | 2022-12-23 | final11m | 9.08 | -11.20 | -11.20 |
| 72708 | TVA | 2022-12-23 | final11r | 9.91 | -11.20 | -11.20 |
| 72709 | TVA | 2022-12-23 | final11x | 9.91 | -11.20 | -11.20 |
| 72719 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 72715 | TVA | 2022-12-24 | final10s | 6.03 | -13.09 | -13.09 |
| 72711 | TVA | 2022-12-24 | final10s_additive | 4.10 | -10.03 | -10.03 |
| 72712 | TVA | 2022-12-24 | final10s_boosting | 7.18 | -15.19 | -15.19 |
| 72714 | TVA | 2022-12-24 | final10s_ensemble | 6.22 | -12.64 | -12.64 |
| 72713 | TVA | 2022-12-24 | final10s_recency | 7.90 | -12.89 | -12.89 |
| 72716 | TVA | 2022-12-24 | final11m | 6.03 | -13.09 | -13.09 |
| 72717 | TVA | 2022-12-24 | final11r | 6.45 | -13.12 | -13.12 |
| 72718 | TVA | 2022-12-24 | final11x | 6.45 | -13.12 | -13.12 |

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
| final10s | NYIS | mape | -7.768 | 0.000 | 749 |
| final10s | PJM | mape | -9.313 | 0.000 | 735 |
| final10s | SWPP | mape | -18.283 | 0.000 | 744 |
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
| final10s_boosting | NYIS | mape | -5.860 | 0.000 | 749 |
| final10s_boosting | PJM | mape | -2.017 | 0.044 | 735 |
| final10s_boosting | SWPP | mape | -13.743 | 0.000 | 744 |
| final10s_boosting | TVA | mape | 11.467 | 0.000 | 732 |
| final10s_ensemble | BPAT | mape | 4.486 | 0.000 | 749 |
| final10s_ensemble | CISO | mape | 2.125 | 0.034 | 722 |
| final10s_ensemble | DUK | mape | 0.134 | 0.894 | 747 |
| final10s_ensemble | ERCO | mape | 1.360 | 0.174 | 745 |
| final10s_ensemble | FPL | mape | 4.828 | 0.000 | 666 |
| final10s_ensemble | ISNE | mape | 17.085 | 0.000 | 749 |
| final10s_ensemble | MISO | mape | -7.559 | 0.000 | 741 |
| final10s_ensemble | NYIS | mape | -7.275 | 0.000 | 749 |
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
| final11m | BPAT | mape | 4.599 | 0.000 | 749 |
| final11m | CISO | mape | -2.513 | 0.012 | 722 |
| final11m | DUK | mape | -0.575 | 0.565 | 747 |
| final11m | ERCO | mape | -3.056 | 0.002 | 745 |
| final11m | FPL | mape | -5.835 | 0.000 | 666 |
| final11m | ISNE | mape | 11.747 | 0.000 | 749 |
| final11m | MISO | mape | -11.832 | 0.000 | 741 |
| final11m | NYIS | mape | -7.757 | 0.000 | 749 |
| final11m | PJM | mape | -9.246 | 0.000 | 735 |
| final11m | SWPP | mape | -18.291 | 0.000 | 744 |
| final11m | TVA | mape | 7.551 | 0.000 | 732 |
| final11r | BPAT | mape | 4.229 | 0.000 | 749 |
| final11r | CISO | mape | -2.733 | 0.006 | 722 |
| final11r | DUK | mape | -0.764 | 0.445 | 747 |
| final11r | ERCO | mape | -2.684 | 0.007 | 745 |
| final11r | FPL | mape | -5.811 | 0.000 | 666 |
| final11r | ISNE | mape | 11.796 | 0.000 | 749 |
| final11r | MISO | mape | -12.161 | 0.000 | 741 |
| final11r | NYIS | mape | -8.223 | 0.000 | 749 |
| final11r | PJM | mape | -9.269 | 0.000 | 735 |
| final11r | SWPP | mape | -18.813 | 0.000 | 744 |
| final11r | TVA | mape | 7.153 | 0.000 | 732 |
| final11x | BPAT | mape | 4.550 | 0.000 | 749 |
| final11x | CISO | mape | -2.538 | 0.011 | 722 |
| final11x | DUK | mape | -0.639 | 0.523 | 747 |
| final11x | ERCO | mape | -2.877 | 0.004 | 745 |
| final11x | FPL | mape | -5.873 | 0.000 | 666 |
| final11x | ISNE | mape | 11.770 | 0.000 | 749 |
| final11x | MISO | mape | -11.901 | 0.000 | 741 |
| final11x | NYIS | mape | -7.903 | 0.000 | 749 |
| final11x | PJM | mape | -9.189 | 0.000 | 735 |
| final11x | SWPP | mape | -18.390 | 0.000 | 744 |
| final11x | TVA | mape | 7.385 | 0.000 | 732 |

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
| final11m | 0.990 |
| final11r | 0.990 |
| final11x | 0.990 |
