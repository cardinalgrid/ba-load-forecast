# Phase R (A29): the recipe with the observed temperature, a diagnostic

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final10so` is `final10s` with every hour of each station's temperature path, from the cut-off to the end of the target day, replaced by the temperature observed at that station: what the recipe would do with a perfect temperature forecast. Dew point, wind and the NBM spread stay forecast. Not a forecast; compare with `peak_q:final10s` (same days) to split the error into its weather and its model parts.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10so | 2.00 | 1.74 | -0.02 | -1.07 | 1.08 | 0.66 | 0.32 | -44.49 | 8088 | 11.00 |
| final10so_ensemble | 2.12 | 1.88 | -1.71 | -2.10 | 1.10 | 0.63 | 0.22 | -45.29 | 8088 | 11.00 |
| final10so_boosting | 2.15 | 1.89 | -1.36 | -1.90 | 1.25 | 0.62 | 0.24 | -44.06 | 8088 | 11.00 |
| final10so_additive | 2.51 | 2.19 | -1.94 | -2.46 | 1.13 | 0.53 | 0.21 | -45.40 | 8088 | 11.00 |
| DF | 2.69 | 2.40 | 0.35 | -1.07 | 0.91 | 0.00 | 0.00 | -47.43 | 8088 | 11.00 |
| final10so_recency | 3.10 | 2.75 | -2.12 | -2.66 | 1.34 | 0.41 | 0.20 | -46.82 | 8088 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.20 | -0.95 | 1.45 | -19.35 |  |  | 750 | 6538.39 |
| DF | CISO | 2.39 | 2.17 | 0.40 | -0.65 | 0.25 | -6.72 |  |  | 723 | 25197.20 |
| DF | DUK | 2.84 | 2.51 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 748 | 12147.45 |
| DF | ERCO | 2.63 | 2.11 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46845.44 |
| DF | FPL | 3.89 | 3.60 | -3.67 | -4.06 | 1.18 | -47.43 |  |  | 667 | 15337.27 |
| DF | ISNE | 2.36 | 2.30 | 0.50 | -0.48 | 0.34 | -6.96 |  |  | 750 | 13405.84 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 749 | 17417.19 |
| DF | PJM | 2.46 | 2.23 | -0.60 | -1.28 | 1.05 | -8.98 |  |  | 736 | 92104.26 |
| DF | SWPP | 3.75 | 3.47 | 2.56 | -0.43 | 1.21 | -19.98 |  |  | 745 | 31394.24 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 733 | 18594.02 |
| final10so | BPAT | 2.10 | 1.88 | -0.35 | -1.21 | 1.60 | -18.12 | 0.48 | 0.28 | 750 | 6538.39 |
| final10so | CISO | 2.31 | 2.04 | 0.49 | -0.93 | 0.35 | -11.36 | 0.51 | 0.29 | 723 | 25197.20 |
| final10so | DUK | 1.99 | 1.80 | -0.12 | -1.09 | 1.04 | -9.10 | 0.71 | 0.38 | 748 | 12147.45 |
| final10so | ERCO | 2.07 | 1.71 | 0.13 | -1.09 | 0.95 | -10.39 | 0.64 | 0.33 | 746 | 46845.44 |
| final10so | FPL | 2.68 | 2.32 | -0.25 | -1.72 | 0.92 | -44.49 | 0.77 | 0.70 | 667 | 15337.27 |
| final10so | ISNE | 2.77 | 2.52 | 0.08 | -1.17 | 0.44 | -14.94 | 0.44 | 0.22 | 750 | 13405.84 |
| final10so | MISO | 1.78 | 1.57 | -0.05 | -0.92 | 1.42 | -6.68 | 0.68 | 0.08 | 741 | 73714.43 |
| final10so | NYIS | 2.11 | 1.84 | -0.15 | -1.24 | 0.56 | -12.32 | 0.67 | 0.70 | 749 | 17417.19 |
| final10so | PJM | 1.82 | 1.59 | -0.11 | -1.05 | 1.18 | -11.14 | 0.71 | 0.46 | 736 | 92104.26 |
| final10so | SWPP | 1.95 | 1.67 | -0.16 | -1.13 | 1.37 | -18.53 | 0.78 | 0.12 | 745 | 31394.24 |
| final10so | TVA | 2.04 | 1.75 | 0.22 | -0.93 | 1.08 | -7.22 | 0.55 | 0.41 | 733 | 18594.02 |
| final10so_additive | BPAT | 2.36 | 2.04 | -1.14 | -1.78 | 1.53 | -17.48 | 0.42 | 0.21 | 750 | 6538.39 |
| final10so_additive | CISO | 2.70 | 2.47 | -1.61 | -2.31 | 0.42 | -12.44 | 0.40 | 0.16 | 723 | 25197.20 |
| final10so_additive | DUK | 2.63 | 2.39 | -2.49 | -2.92 | 1.03 | -14.58 | 0.54 | 0.24 | 748 | 12147.45 |
| final10so_additive | ERCO | 2.90 | 2.50 | -2.30 | -2.90 | 1.04 | -13.60 | 0.42 | 0.20 | 746 | 46845.44 |
| final10so_additive | FPL | 3.54 | 3.05 | -2.95 | -3.71 | 0.94 | -45.40 | 0.63 | 0.51 | 667 | 15337.27 |
| final10so_additive | ISNE | 3.22 | 2.89 | -1.57 | -2.31 | 0.52 | -19.70 | 0.31 | 0.15 | 750 | 13405.84 |
| final10so_additive | MISO | 2.08 | 1.82 | -1.65 | -2.03 | 1.52 | -9.15 | 0.60 | 0.05 | 741 | 73714.43 |
| final10so_additive | NYIS | 2.54 | 2.18 | -1.59 | -2.30 | 0.55 | -14.75 | 0.55 | 0.57 | 749 | 17417.19 |
| final10so_additive | PJM | 2.29 | 1.98 | -1.85 | -2.32 | 1.19 | -12.97 | 0.56 | 0.29 | 736 | 92104.26 |
| final10so_additive | SWPP | 2.44 | 2.02 | -1.91 | -2.47 | 1.31 | -21.77 | 0.71 | 0.07 | 745 | 31394.24 |
| final10so_additive | TVA | 2.75 | 2.54 | -2.74 | -3.13 | 1.16 | -13.26 | 0.36 | 0.18 | 733 | 18594.02 |
| final10so_boosting | BPAT | 2.11 | 1.90 | -1.35 | -1.85 | 1.69 | -18.40 | 0.46 | 0.21 | 750 | 6538.39 |
| final10so_boosting | CISO | 2.41 | 2.10 | -0.56 | -1.39 | 0.39 | -16.53 | 0.49 | 0.25 | 723 | 25197.20 |
| final10so_boosting | DUK | 2.27 | 2.13 | -1.80 | -2.26 | 1.09 | -11.48 | 0.59 | 0.28 | 748 | 12147.45 |
| final10so_boosting | ERCO | 2.25 | 1.91 | -1.87 | -2.35 | 1.18 | -18.16 | 0.55 | 0.22 | 746 | 46845.44 |
| final10so_boosting | FPL | 2.62 | 2.23 | -1.82 | -2.53 | 1.04 | -44.06 | 0.83 | 0.65 | 667 | 15337.27 |
| final10so_boosting | ISNE | 2.87 | 2.66 | -0.66 | -1.50 | 0.55 | -13.66 | 0.39 | 0.19 | 750 | 13405.84 |
| final10so_boosting | MISO | 1.92 | 1.69 | -1.04 | -1.56 | 1.62 | -7.91 | 0.65 | 0.05 | 741 | 73714.43 |
| final10so_boosting | NYIS | 2.21 | 1.91 | -0.85 | -1.58 | 0.71 | -15.28 | 0.62 | 0.68 | 749 | 17417.19 |
| final10so_boosting | PJM | 1.97 | 1.79 | -1.43 | -1.89 | 1.39 | -10.10 | 0.66 | 0.33 | 736 | 92104.26 |
| final10so_boosting | SWPP | 2.24 | 1.84 | -1.89 | -2.35 | 1.48 | -20.68 | 0.72 | 0.07 | 745 | 31394.24 |
| final10so_boosting | TVA | 2.19 | 1.97 | -1.53 | -2.01 | 1.24 | -8.48 | 0.48 | 0.26 | 733 | 18594.02 |
| final10so_ensemble | BPAT | 2.08 | 1.82 | -1.38 | -1.83 | 1.47 | -18.24 | 0.50 | 0.20 | 750 | 6538.39 |
| final10so_ensemble | CISO | 2.47 | 2.25 | -1.50 | -2.02 | 0.36 | -13.76 | 0.46 | 0.16 | 723 | 25197.20 |
| final10so_ensemble | DUK | 2.13 | 1.94 | -1.96 | -2.32 | 1.09 | -10.91 | 0.64 | 0.27 | 748 | 12147.45 |
| final10so_ensemble | ERCO | 2.25 | 1.92 | -2.04 | -2.44 | 0.98 | -13.48 | 0.58 | 0.20 | 746 | 46845.44 |
| final10so_ensemble | FPL | 2.84 | 2.44 | -2.67 | -3.19 | 0.93 | -45.29 | 0.76 | 0.57 | 667 | 15337.27 |
| final10so_ensemble | ISNE | 2.90 | 2.71 | -1.63 | -2.13 | 0.47 | -16.06 | 0.35 | 0.13 | 750 | 13405.84 |
| final10so_ensemble | MISO | 1.85 | 1.63 | -1.45 | -1.77 | 1.50 | -7.53 | 0.66 | 0.04 | 741 | 73714.43 |
| final10so_ensemble | NYIS | 2.17 | 1.93 | -1.22 | -1.80 | 0.56 | -12.64 | 0.63 | 0.63 | 749 | 17417.19 |
| final10so_ensemble | PJM | 1.94 | 1.76 | -1.71 | -2.03 | 1.18 | -11.69 | 0.68 | 0.31 | 736 | 92104.26 |
| final10so_ensemble | SWPP | 2.03 | 1.69 | -1.61 | -2.03 | 1.38 | -19.36 | 0.75 | 0.08 | 745 | 31394.24 |
| final10so_ensemble | TVA | 2.20 | 2.01 | -2.11 | -2.41 | 1.02 | -9.05 | 0.48 | 0.22 | 733 | 18594.02 |
| final10so_recency | BPAT | 2.93 | 2.61 | -1.79 | -2.37 | 1.64 | -19.02 | 0.28 | 0.20 | 750 | 6538.39 |
| final10so_recency | CISO | 4.60 | 4.47 | -3.23 | -3.62 | 0.58 | -12.74 | 0.11 | 0.10 | 723 | 25197.20 |
| final10so_recency | DUK | 2.71 | 2.47 | -1.68 | -2.34 | 1.23 | -12.81 | 0.49 | 0.27 | 748 | 12147.45 |
| final10so_recency | ERCO | 3.05 | 2.66 | -2.20 | -2.86 | 1.16 | -18.43 | 0.38 | 0.21 | 746 | 46845.44 |
| final10so_recency | FPL | 4.29 | 3.55 | -4.09 | -4.71 | 1.06 | -46.82 | 0.53 | 0.46 | 667 | 15337.27 |
| final10so_recency | ISNE | 4.91 | 4.60 | -3.39 | -3.85 | 0.69 | -23.75 | 0.07 | 0.07 | 750 | 13405.84 |
| final10so_recency | MISO | 2.76 | 2.39 | -1.88 | -2.27 | 1.80 | -16.18 | 0.44 | 0.05 | 741 | 73714.43 |
| final10so_recency | NYIS | 3.42 | 3.16 | -1.47 | -2.27 | 0.90 | -18.24 | 0.34 | 0.55 | 749 | 17417.19 |
| final10so_recency | PJM | 2.73 | 2.44 | -1.97 | -2.43 | 1.43 | -16.66 | 0.45 | 0.28 | 736 | 92104.26 |
| final10so_recency | SWPP | 2.64 | 2.17 | -1.12 | -1.94 | 1.62 | -18.46 | 0.68 | 0.10 | 745 | 31394.24 |
| final10so_recency | TVA | 2.89 | 2.57 | -2.29 | -2.80 | 1.21 | -11.76 | 0.34 | 0.21 | 733 | 18594.02 |

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
| final10so | BPAT | uri | 2.39 | 0.61 | -0.96 | -2.92 | 6 |
| final10so | CISO | uri | 1.95 | -0.54 | -0.93 | -1.83 | 6 |
| final10so | DUK | uri | 1.97 | -0.62 | -0.86 | -2.17 | 6 |
| final10so | ERCO | uri | 2.77 | -3.41 | -3.41 | -4.81 | 2 |
| final10so | FPL | uri | 5.52 | -5.03 | -5.03 | -7.42 | 6 |
| final10so | ISNE | uri | 2.18 | 1.58 | 0.00 | 0.00 | 6 |
| final10so | MISO | uri | 3.08 | -2.37 | -2.45 | -5.79 | 5 |
| final10so | NYIS | uri | 2.12 | 2.21 | -0.11 | -0.69 | 6 |
| final10so | PJM | uri | 1.78 | 0.53 | -0.38 | -2.26 | 6 |
| final10so | SWPP | uri | 5.96 | 1.85 | -2.25 | -5.86 | 4 |
| final10so | TVA | uri | 4.06 | 2.95 | 0.00 | 0.00 | 6 |
| final10so_additive | BPAT | uri | 2.17 | -0.24 | -0.40 | -1.38 | 6 |
| final10so_additive | CISO | uri | 2.12 | -0.71 | -1.08 | -1.88 | 6 |
| final10so_additive | DUK | uri | 2.02 | -1.58 | -1.89 | -3.62 | 6 |
| final10so_additive | ERCO | uri | 2.59 | -2.62 | -2.94 | -5.87 | 2 |
| final10so_additive | FPL | uri | 6.93 | -9.08 | -9.08 | -11.72 | 6 |
| final10so_additive | ISNE | uri | 2.03 | 0.77 | -0.05 | -0.32 | 6 |
| final10so_additive | MISO | uri | 3.41 | -2.40 | -2.88 | -6.22 | 5 |
| final10so_additive | NYIS | uri | 2.36 | 2.33 | -0.09 | -0.51 | 6 |
| final10so_additive | PJM | uri | 2.15 | 1.94 | -0.43 | -2.59 | 6 |
| final10so_additive | SWPP | uri | 5.60 | 3.52 | -0.71 | -2.16 | 4 |
| final10so_additive | TVA | uri | 3.59 | 2.25 | -0.03 | -0.19 | 6 |
| final10so_boosting | BPAT | uri | 3.14 | 0.98 | -1.22 | -4.05 | 6 |
| final10so_boosting | CISO | uri | 2.40 | -2.07 | -2.27 | -4.50 | 6 |
| final10so_boosting | DUK | uri | 2.19 | -2.39 | -2.39 | -4.30 | 6 |
| final10so_boosting | ERCO | uri | 7.58 | -11.92 | -11.92 | -14.57 | 2 |
| final10so_boosting | FPL | uri | 2.47 | -2.92 | -2.92 | -6.37 | 6 |
| final10so_boosting | ISNE | uri | 2.61 | 0.55 | -0.29 | -1.29 | 6 |
| final10so_boosting | MISO | uri | 2.09 | -2.74 | -2.74 | -5.07 | 5 |
| final10so_boosting | NYIS | uri | 2.41 | 0.76 | -0.50 | -3.00 | 6 |
| final10so_boosting | PJM | uri | 1.71 | -1.39 | -1.39 | -2.23 | 6 |
| final10so_boosting | SWPP | uri | 5.92 | -0.73 | -3.36 | -8.53 | 4 |
| final10so_boosting | TVA | uri | 3.35 | 1.17 | -0.07 | -0.40 | 6 |
| final10so_ensemble | BPAT | uri | 2.37 | 0.50 | -0.79 | -2.61 | 6 |
| final10so_ensemble | CISO | uri | 2.34 | -2.13 | -2.24 | -3.40 | 6 |
| final10so_ensemble | DUK | uri | 2.07 | -2.36 | -2.39 | -4.18 | 6 |
| final10so_ensemble | ERCO | uri | 3.50 | -4.85 | -4.85 | -6.82 | 2 |
| final10so_ensemble | FPL | uri | 5.59 | -7.29 | -7.29 | -10.19 | 6 |
| final10so_ensemble | ISNE | uri | 1.73 | -0.37 | -0.44 | -1.01 | 6 |
| final10so_ensemble | MISO | uri | 3.32 | -3.44 | -3.44 | -6.74 | 5 |
| final10so_ensemble | NYIS | uri | 2.06 | 1.41 | -0.25 | -1.49 | 6 |
| final10so_ensemble | PJM | uri | 1.65 | 0.09 | -0.50 | -2.89 | 6 |
| final10so_ensemble | SWPP | uri | 5.87 | 0.76 | -2.62 | -6.06 | 4 |
| final10so_ensemble | TVA | uri | 3.13 | 1.38 | -0.03 | -0.18 | 6 |
| final10so_recency | BPAT | uri | 2.33 | 0.64 | -0.76 | -2.29 | 6 |
| final10so_recency | CISO | uri | 4.20 | -4.00 | -4.00 | -5.14 | 6 |
| final10so_recency | DUK | uri | 2.55 | -3.13 | -3.13 | -5.73 | 6 |
| final10so_recency | ERCO | uri | 4.40 | 1.70 | -2.39 | -4.78 | 2 |
| final10so_recency | FPL | uri | 8.77 | -10.82 | -10.82 | -13.74 | 6 |
| final10so_recency | ISNE | uri | 4.06 | -3.81 | -3.81 | -5.28 | 6 |
| final10so_recency | MISO | uri | 6.48 | -5.93 | -5.93 | -9.94 | 5 |
| final10so_recency | NYIS | uri | 2.29 | 1.19 | -0.17 | -0.58 | 6 |
| final10so_recency | PJM | uri | 2.08 | 0.03 | -0.85 | -4.66 | 6 |
| final10so_recency | SWPP | uri | 6.38 | -1.20 | -4.29 | -10.26 | 4 |
| final10so_recency | TVA | uri | 3.17 | 0.62 | -0.12 | -0.44 | 6 |
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
| final10so | BPAT | elliott | 4.28 | 2.86 | -0.12 | -0.35 | 5 |
| final10so | CISO | elliott | 3.97 | 3.94 | -0.32 | -1.62 | 5 |
| final10so | DUK | elliott | 2.35 | -2.67 | -2.67 | -5.88 | 4 |
| final10so | ERCO | elliott | 4.98 | -2.52 | -2.91 | -7.50 | 5 |
| final10so | FPL | elliott | 5.69 | -6.73 | -6.73 | -9.19 | 5 |
| final10so | ISNE | elliott | 2.94 | 3.12 | -0.17 | -0.85 | 5 |
| final10so | MISO | elliott | 3.42 | -2.18 | -2.75 | -6.28 | 5 |
| final10so | NYIS | elliott | 2.50 | 0.83 | -0.82 | -2.38 | 5 |
| final10so | PJM | elliott | 3.74 | -2.84 | -3.01 | -7.57 | 5 |
| final10so | SWPP | elliott | 3.39 | -1.89 | -2.86 | -7.10 | 5 |
| final10so | TVA | elliott | 3.08 | -2.09 | -2.09 | -3.19 | 3 |
| final10so_additive | BPAT | elliott | 4.93 | 2.26 | -0.61 | -2.43 | 5 |
| final10so_additive | CISO | elliott | 3.12 | 0.81 | -1.25 | -5.18 | 5 |
| final10so_additive | DUK | elliott | 3.20 | -6.50 | -6.50 | -8.76 | 4 |
| final10so_additive | ERCO | elliott | 7.01 | -4.85 | -4.85 | -13.60 | 5 |
| final10so_additive | FPL | elliott | 7.03 | -3.30 | -4.05 | -8.47 | 5 |
| final10so_additive | ISNE | elliott | 3.56 | -0.75 | -1.43 | -4.05 | 5 |
| final10so_additive | MISO | elliott | 3.43 | -3.36 | -3.42 | -6.03 | 5 |
| final10so_additive | NYIS | elliott | 3.12 | -1.91 | -2.19 | -5.53 | 5 |
| final10so_additive | PJM | elliott | 3.21 | -2.38 | -2.66 | -6.86 | 5 |
| final10so_additive | SWPP | elliott | 3.07 | -2.30 | -2.55 | -6.83 | 5 |
| final10so_additive | TVA | elliott | 3.81 | -3.61 | -3.61 | -4.68 | 3 |
| final10so_boosting | BPAT | elliott | 3.83 | -1.36 | -2.22 | -5.69 | 5 |
| final10so_boosting | CISO | elliott | 3.72 | 2.32 | -0.57 | -1.90 | 5 |
| final10so_boosting | DUK | elliott | 2.97 | -3.24 | -3.24 | -7.38 | 4 |
| final10so_boosting | ERCO | elliott | 7.31 | -12.16 | -12.16 | -18.16 | 5 |
| final10so_boosting | FPL | elliott | 8.41 | -12.47 | -12.47 | -18.87 | 5 |
| final10so_boosting | ISNE | elliott | 2.67 | 1.47 | -0.51 | -2.56 | 5 |
| final10so_boosting | MISO | elliott | 3.23 | -2.34 | -3.08 | -5.35 | 5 |
| final10so_boosting | NYIS | elliott | 2.47 | -0.03 | -1.02 | -2.98 | 5 |
| final10so_boosting | PJM | elliott | 3.63 | -4.16 | -4.16 | -7.82 | 5 |
| final10so_boosting | SWPP | elliott | 4.22 | -5.25 | -5.69 | -13.25 | 5 |
| final10so_boosting | TVA | elliott | 2.80 | -3.40 | -3.40 | -5.25 | 3 |
| final10so_ensemble | BPAT | elliott | 3.69 | 0.82 | -0.71 | -2.59 | 5 |
| final10so_ensemble | CISO | elliott | 3.21 | 1.96 | -0.74 | -3.05 | 5 |
| final10so_ensemble | DUK | elliott | 2.70 | -5.49 | -5.49 | -7.94 | 4 |
| final10so_ensemble | ERCO | elliott | 5.67 | -7.03 | -7.03 | -11.99 | 5 |
| final10so_ensemble | FPL | elliott | 6.82 | -9.20 | -9.20 | -12.07 | 5 |
| final10so_ensemble | ISNE | elliott | 2.82 | 0.64 | -0.88 | -3.36 | 5 |
| final10so_ensemble | MISO | elliott | 3.66 | -3.90 | -4.03 | -7.53 | 5 |
| final10so_ensemble | NYIS | elliott | 2.66 | -1.17 | -1.79 | -4.17 | 5 |
| final10so_ensemble | PJM | elliott | 4.01 | -4.78 | -4.78 | -9.28 | 5 |
| final10so_ensemble | SWPP | elliott | 3.71 | -4.86 | -4.95 | -9.89 | 5 |
| final10so_ensemble | TVA | elliott | 3.33 | -4.41 | -4.41 | -5.62 | 3 |
| final10so_recency | BPAT | elliott | 3.58 | 2.58 | -0.05 | -0.27 | 5 |
| final10so_recency | CISO | elliott | 3.92 | 2.74 | -0.49 | -2.43 | 5 |
| final10so_recency | DUK | elliott | 4.44 | -7.52 | -7.52 | -8.71 | 4 |
| final10so_recency | ERCO | elliott | 4.73 | -2.76 | -2.76 | -6.70 | 5 |
| final10so_recency | FPL | elliott | 10.02 | -12.12 | -12.12 | -17.83 | 5 |
| final10so_recency | ISNE | elliott | 4.19 | 0.99 | -1.27 | -3.79 | 5 |
| final10so_recency | MISO | elliott | 6.80 | -7.63 | -7.63 | -16.18 | 5 |
| final10so_recency | NYIS | elliott | 4.18 | -2.41 | -2.81 | -6.26 | 5 |
| final10so_recency | PJM | elliott | 6.24 | -8.15 | -8.15 | -16.66 | 5 |
| final10so_recency | SWPP | elliott | 5.41 | -7.54 | -7.54 | -13.07 | 5 |
| final10so_recency | TVA | elliott | 4.05 | -6.59 | -6.59 | -7.77 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final10so_ensemble | eve | 2.76 | -0.85 | -1.90 | 0.60 | 265 |
| 7 | final10so | eve | 2.97 | 1.02 | -1.11 | 0.55 | 265 |
| 9 | final10so_boosting | eve | 3.06 | -0.28 | -1.73 | 0.55 | 265 |
| 8 | final10so_additive | eve | 3.10 | -0.83 | -2.09 | 0.54 | 265 |
| 6 | DF | eve | 3.36 | 0.49 | -1.42 |  | 265 |
| 11 | final10so_recency | eve | 3.75 | -1.94 | -2.89 | 0.42 | 265 |
| 4 | final10so_ensemble | special | 2.84 | -2.15 | -2.76 | 0.64 | 267 |
| 1 | final10so | special | 2.89 | -0.26 | -1.59 | 0.66 | 267 |
| 3 | final10so_boosting | special | 3.13 | -1.69 | -2.52 | 0.59 | 267 |
| 2 | final10so_additive | special | 3.18 | -2.36 | -3.08 | 0.51 | 267 |
| 0 | DF | special | 3.71 | -0.12 | -1.77 |  | 267 |
| 5 | final10so_recency | special | 3.86 | -2.81 | -3.59 | 0.45 | 267 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10so | all | 0.326 | 1.074 | 0.316 | 0.890 | 9.665 | 0.896 | 12.829 | 1.395 | 7857 |
| final10so | events | 0.455 | 1.665 | 0.520 | 0.787 | 10.950 | 0.820 | 19.508 | 2.163 | 111 |
| final10so | cold_mornings | 0.400 | 1.287 | 0.398 | 0.888 | 12.009 | 0.888 | 15.969 | 1.689 | 330 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13289 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13288 | DUK | 2022-12-24 | final10so | 8.48 | -10.16 | -10.16 |
| 13284 | DUK | 2022-12-24 | final10so_additive | 9.14 | -11.37 | -11.37 |
| 13285 | DUK | 2022-12-24 | final10so_boosting | 9.27 | -16.03 | -16.03 |
| 13287 | DUK | 2022-12-24 | final10so_ensemble | 9.58 | -12.87 | -12.87 |
| 13286 | DUK | 2022-12-24 | final10so_recency | 11.03 | -10.02 | -10.02 |
| 13787 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13786 | ERCO | 2021-02-17 | final10so | 27.84 | 20.85 | 0.00 |
| 13782 | ERCO | 2021-02-17 | final10so_additive | 28.50 | 20.50 | 0.00 |
| 13783 | ERCO | 2021-02-17 | final10so_boosting | 26.22 | 18.64 | 0.00 |
| 13785 | ERCO | 2021-02-17 | final10so_ensemble | 26.27 | 19.55 | 0.00 |
| 13784 | ERCO | 2021-02-17 | final10so_recency | 23.63 | 19.71 | 0.00 |
| 13793 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13792 | ERCO | 2021-02-18 | final10so | 11.03 | 10.14 | 0.00 |
| 13788 | ERCO | 2021-02-18 | final10so_additive | 12.09 | 11.73 | 0.00 |
| 13789 | ERCO | 2021-02-18 | final10so_boosting | 10.15 | 5.99 | 0.00 |
| 13791 | ERCO | 2021-02-18 | final10so_ensemble | 9.81 | 7.47 | 0.00 |
| 13790 | ERCO | 2021-02-18 | final10so_recency | 6.27 | 4.24 | 0.00 |
| 26777 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 26776 | MISO | 2021-02-16 | final10so | 1.96 | 2.06 | 0.00 |
| 26772 | MISO | 2021-02-16 | final10so_additive | 2.25 | 2.52 | 0.00 |
| 26773 | MISO | 2021-02-16 | final10so_boosting | 1.71 | 1.23 | 0.00 |
| 26775 | MISO | 2021-02-16 | final10so_ensemble | 1.67 | 0.94 | 0.00 |
| 26774 | MISO | 2021-02-16 | final10so_recency | 3.95 | -1.82 | -1.82 |
| 40139 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 40138 | SWPP | 2021-02-15 | final10so | 2.28 | -2.14 | -2.14 |
| 40134 | SWPP | 2021-02-15 | final10so_additive | 3.01 | 1.61 | 0.00 |
| 40135 | SWPP | 2021-02-15 | final10so_boosting | 5.35 | -8.08 | -8.08 |
| 40137 | SWPP | 2021-02-15 | final10so_ensemble | 2.32 | -3.24 | -3.24 |
| 40136 | SWPP | 2021-02-15 | final10so_recency | 4.52 | -3.99 | -3.99 |
| 40145 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 40144 | SWPP | 2021-02-16 | final10so | 4.45 | 0.07 | 0.00 |
| 40140 | SWPP | 2021-02-16 | final10so_additive | 8.02 | 4.01 | 0.00 |
| 40141 | SWPP | 2021-02-16 | final10so_boosting | 3.60 | -5.49 | -5.49 |
| 40143 | SWPP | 2021-02-16 | final10so_ensemble | 4.23 | -0.24 | -0.24 |
| 40142 | SWPP | 2021-02-16 | final10so_recency | 2.44 | 0.23 | 0.00 |
| 48527 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 48526 | TVA | 2022-12-23 | final10so | 8.66 | -8.74 | -8.74 |
| 48522 | TVA | 2022-12-23 | final10so_additive | 5.78 | -3.20 | -3.20 |
| 48523 | TVA | 2022-12-23 | final10so_boosting | 14.86 | -16.20 | -16.20 |
| 48525 | TVA | 2022-12-23 | final10so_ensemble | 9.85 | -10.66 | -10.66 |
| 48524 | TVA | 2022-12-23 | final10so_recency | 10.40 | -12.84 | -12.84 |
| 48533 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 48532 | TVA | 2022-12-24 | final10so | 5.91 | -10.06 | -10.06 |
| 48528 | TVA | 2022-12-24 | final10so_additive | 4.95 | -7.83 | -7.83 |
| 48529 | TVA | 2022-12-24 | final10so_boosting | 8.06 | -14.25 | -14.25 |
| 48531 | TVA | 2022-12-24 | final10so_ensemble | 7.24 | -11.35 | -11.35 |
| 48530 | TVA | 2022-12-24 | final10so_recency | 8.93 | -11.93 | -11.93 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final10so | BPAT | mape | 0.793 | 0.428 | 750 |
| final10so | CISO | mape | -1.600 | 0.110 | 723 |
| final10so | DUK | mape | -13.671 | 0.000 | 748 |
| final10so | ERCO | mape | -9.282 | 0.000 | 746 |
| final10so | FPL | mape | -16.588 | 0.000 | 667 |
| final10so | ISNE | mape | 8.100 | 0.000 | 750 |
| final10so | MISO | mape | -14.598 | 0.000 | 741 |
| final10so | NYIS | mape | -9.642 | 0.000 | 749 |
| final10so | PJM | mape | -12.908 | 0.000 | 736 |
| final10so | SWPP | mape | -21.832 | 0.000 | 745 |
| final10so | TVA | mape | -3.529 | 0.000 | 733 |
| final10so_additive | BPAT | mape | 5.621 | 0.000 | 750 |
| final10so_additive | CISO | mape | 5.637 | 0.000 | 723 |
| final10so_additive | DUK | mape | -2.866 | 0.004 | 748 |
| final10so_additive | ERCO | mape | 3.532 | 0.000 | 746 |
| final10so_additive | FPL | mape | -3.982 | 0.000 | 667 |
| final10so_additive | ISNE | mape | 15.522 | 0.000 | 750 |
| final10so_additive | MISO | mape | -8.577 | 0.000 | 741 |
| final10so_additive | NYIS | mape | -2.156 | 0.031 | 749 |
| final10so_additive | PJM | mape | -3.241 | 0.001 | 736 |
| final10so_additive | SWPP | mape | -14.147 | 0.000 | 745 |
| final10so_additive | TVA | mape | 8.165 | 0.000 | 733 |
| final10so_boosting | BPAT | mape | 0.981 | 0.327 | 750 |
| final10so_boosting | CISO | mape | 0.303 | 0.762 | 723 |
| final10so_boosting | DUK | mape | -8.807 | 0.000 | 748 |
| final10so_boosting | ERCO | mape | -5.799 | 0.000 | 746 |
| final10so_boosting | FPL | mape | -18.464 | 0.000 | 667 |
| final10so_boosting | ISNE | mape | 10.105 | 0.000 | 750 |
| final10so_boosting | MISO | mape | -11.887 | 0.000 | 741 |
| final10so_boosting | NYIS | mape | -8.242 | 0.000 | 749 |
| final10so_boosting | PJM | mape | -10.090 | 0.000 | 736 |
| final10so_boosting | SWPP | mape | -16.783 | 0.000 | 745 |
| final10so_boosting | TVA | mape | -0.711 | 0.477 | 733 |
| final10so_ensemble | BPAT | mape | 0.344 | 0.731 | 750 |
| final10so_ensemble | CISO | mape | 1.582 | 0.114 | 723 |
| final10so_ensemble | DUK | mape | -11.014 | 0.000 | 748 |
| final10so_ensemble | ERCO | mape | -5.671 | 0.000 | 746 |
| final10so_ensemble | FPL | mape | -13.965 | 0.000 | 667 |
| final10so_ensemble | ISNE | mape | 11.293 | 0.000 | 750 |
| final10so_ensemble | MISO | mape | -12.454 | 0.000 | 741 |
| final10so_ensemble | NYIS | mape | -9.099 | 0.000 | 749 |
| final10so_ensemble | PJM | mape | -10.973 | 0.000 | 736 |
| final10so_ensemble | SWPP | mape | -19.882 | 0.000 | 745 |
| final10so_ensemble | TVA | mape | -0.464 | 0.643 | 733 |
| final10so_recency | BPAT | mape | 13.614 | 0.000 | 750 |
| final10so_recency | CISO | mape | 32.094 | 0.000 | 723 |
| final10so_recency | DUK | mape | -1.721 | 0.085 | 748 |
| final10so_recency | ERCO | mape | 5.668 | 0.000 | 746 |
| final10so_recency | FPL | mape | 3.354 | 0.001 | 667 |
| final10so_recency | ISNE | mape | 34.973 | 0.000 | 750 |
| final10so_recency | MISO | mape | 1.417 | 0.157 | 741 |
| final10so_recency | NYIS | mape | 10.622 | 0.000 | 749 |
| final10so_recency | PJM | mape | 4.649 | 0.000 | 736 |
| final10so_recency | SWPP | mape | -12.491 | 0.000 | 745 |
| final10so_recency | TVA | mape | 10.068 | 0.000 | 733 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.991 |
| final10so | 0.991 |
| final10so_additive | 0.968 |
| final10so_boosting | 0.991 |
| final10so_ensemble | 0.991 |
| final10so_recency | 0.991 |
