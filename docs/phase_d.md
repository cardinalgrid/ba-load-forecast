# Phase D: closing the development of the model

Development BAs (BPAT, CISO, DUK, ERCO, ISNE, MISO, NYIS, PJM, SWPP, TVA), 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at four to five stations per BA, six years of training (`_ml`). Variants: explicit cold and heat extreme terms (`_ext`), ensembles of the direct models (`ens_`), the special-day treatments (`_special`, `_separate`), quantile forecasts (`qboost_`, `emp_`). Three phase C variants are kept as references (`_multi`: several stations with two years; `additive_long`: one station with six years). Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_recent | 2.76 | 2.40 | -0.98 | -1.99 | 1.30 | 0.56 | 0.27 | -22.26 | 7253 | 10.00 |
| ens_mean | 2.77 | 2.40 | -1.00 | -2.00 | 1.29 | 0.56 | 0.27 | -22.29 | 7253 | 10.00 |
| ens_mean3 | 2.78 | 2.41 | -0.88 | -1.95 | 1.30 | 0.56 | 0.27 | -19.83 | 7253 | 10.00 |
| emp_additive_ml | 2.80 | 2.41 | -0.58 | -1.84 | 1.36 | 0.55 | 0.28 | -23.56 | 7253 | 10.00 |
| boosting_ml_ext | 2.89 | 2.53 | -0.74 | -1.91 | 1.48 | 0.53 | 0.28 | -28.68 | 7253 | 10.00 |
| boosting_ml | 2.90 | 2.54 | -0.75 | -1.92 | 1.50 | 0.53 | 0.28 | -28.44 | 7253 | 10.00 |
| qboost_ml | 2.92 | 2.52 | -0.79 | -1.95 | 1.47 | 0.53 | 0.28 | -22.59 | 7253 | 10.00 |
| DF | 3.01 | 2.70 | 0.30 | -1.10 | 1.07 | 0.00 | 0.00 | -19.98 | 7253 | 10.00 |
| additive_ml_ext_special | 3.03 | 2.65 | -1.26 | -2.28 | 1.43 | 0.51 | 0.25 | -22.51 | 7253 | 10.00 |
| additive_ml | 3.03 | 2.66 | -1.26 | -2.28 | 1.41 | 0.51 | 0.25 | -22.52 | 7253 | 10.00 |
| additive_ml_ext | 3.04 | 2.66 | -1.26 | -2.28 | 1.44 | 0.51 | 0.25 | -22.64 | 7253 | 10.00 |
| additive_ml_ext_separate | 3.04 | 2.66 | -1.26 | -2.28 | 1.44 | 0.51 | 0.25 | -22.64 | 7253 | 10.00 |
| boosting_multi | 3.08 | 2.66 | -0.82 | -2.05 | 1.53 | 0.50 | 0.27 | -31.26 | 7253 | 10.00 |
| additive_multi | 3.15 | 2.71 | -0.49 | -1.95 | 1.45 | 0.50 | 0.28 | -22.77 | 7253 | 10.00 |
| additive_long | 3.57 | 3.03 | -0.89 | -2.47 | 1.61 | 0.43 | 0.26 | -26.57 | 7253 | 10.00 |
| recency_ml | 3.66 | 3.19 | -0.64 | -2.23 | 1.58 | 0.41 | 0.27 | -30.94 | 7253 | 10.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.44 | -19.35 |  |  | 729 | 6521.82 |
| DF | CISO | 2.84 | 2.39 | 0.10 | -0.83 | 0.42 | -6.84 |  |  | 716 | 25235.45 |
| DF | DUK | 2.84 | 2.52 | -0.05 | -1.47 | 1.18 | -13.32 |  |  | 729 | 12124.38 |
| DF | ERCO | 2.65 | 2.13 | 0.53 | -1.11 | 0.81 | -14.36 |  |  | 725 | 46952.76 |
| DF | ISNE | 2.36 | 2.31 | 0.52 | -0.46 | 0.35 | -6.96 |  |  | 731 | 13367.24 |
| DF | MISO | 2.64 | 2.30 | 2.14 | -0.19 | 0.96 | -6.70 |  |  | 725 | 73818.42 |
| DF | NYIS | 2.66 | 2.49 | -2.46 | -2.65 | 0.41 | -12.87 |  |  | 731 | 17396.47 |
| DF | PJM | 3.65 | 3.47 | -1.42 | -1.87 | 1.62 | -10.72 |  |  | 723 | 91872.73 |
| DF | SWPP | 3.88 | 3.52 | 2.65 | -0.42 | 1.24 | -19.98 |  |  | 726 | 31381.35 |
| DF | TVA | 2.22 | 1.92 | -0.13 | -1.24 | 0.97 | -16.93 |  |  | 718 | 18548.22 |
| additive_long | BPAT | 3.13 | 2.69 | -0.66 | -1.94 | 1.68 | -17.50 | 0.25 | 0.24 | 729 | 6521.82 |
| additive_long | CISO | 4.33 | 3.83 | -0.87 | -3.03 | 0.58 | -26.57 | 0.28 | 0.26 | 716 | 25235.45 |
| additive_long | DUK | 3.77 | 3.31 | -0.88 | -2.56 | 1.37 | -17.37 | 0.33 | 0.27 | 729 | 12124.38 |
| additive_long | ERCO | 3.64 | 3.07 | -1.33 | -2.72 | 1.17 | -19.57 | 0.33 | 0.21 | 725 | 46952.76 |
| additive_long | ISNE | 4.77 | 4.22 | -2.17 | -3.35 | 0.62 | -25.28 | 0.12 | 0.14 | 731 | 13367.24 |
| additive_long | MISO | 2.88 | 2.33 | -1.10 | -2.23 | 1.94 | -16.14 | 0.47 | 0.04 | 725 | 73818.42 |
| additive_long | NYIS | 3.52 | 2.90 | -0.92 | -2.57 | 0.75 | -25.13 | 0.41 | 0.58 | 731 | 17396.47 |
| additive_long | PJM | 3.73 | 3.21 | -0.39 | -2.31 | 2.17 | -16.84 | 0.56 | 0.49 | 723 | 91872.73 |
| additive_long | SWPP | 3.45 | 2.71 | -0.16 | -2.05 | 1.54 | -20.79 | 0.57 | 0.07 | 726 | 31381.35 |
| additive_long | TVA | 3.83 | 3.43 | -1.79 | -3.03 | 1.68 | -16.92 | 0.21 | 0.19 | 718 | 18548.22 |
| additive_ml | BPAT | 2.80 | 2.44 | -0.96 | -1.85 | 1.75 | -18.41 | 0.29 | 0.22 | 729 | 6521.82 |
| additive_ml | CISO | 3.91 | 3.55 | -3.30 | -4.09 | 0.38 | -18.80 | 0.29 | 0.13 | 716 | 25235.45 |
| additive_ml | DUK | 3.58 | 3.16 | -0.67 | -2.37 | 1.37 | -14.83 | 0.34 | 0.27 | 729 | 12124.38 |
| additive_ml | ERCO | 3.60 | 3.17 | -2.25 | -3.08 | 1.11 | -16.35 | 0.30 | 0.15 | 725 | 46952.76 |
| additive_ml | ISNE | 4.24 | 3.70 | -1.56 | -2.77 | 0.55 | -22.52 | 0.17 | 0.15 | 731 | 13367.24 |
| additive_ml | MISO | 2.47 | 2.17 | -1.37 | -1.96 | 1.78 | -9.51 | 0.53 | 0.05 | 725 | 73818.42 |
| additive_ml | NYIS | 2.74 | 2.38 | -0.80 | -2.05 | 0.61 | -15.67 | 0.50 | 0.60 | 731 | 17396.47 |
| additive_ml | PJM | 2.84 | 2.50 | -0.66 | -1.84 | 1.75 | -12.07 | 0.75 | 0.50 | 723 | 91872.73 |
| additive_ml | SWPP | 2.64 | 2.14 | -0.22 | -1.59 | 1.53 | -20.37 | 0.71 | 0.09 | 726 | 31381.35 |
| additive_ml | TVA | 3.37 | 2.98 | -1.04 | -2.37 | 1.41 | -14.25 | 0.24 | 0.24 | 718 | 18548.22 |
| additive_ml_ext | BPAT | 2.82 | 2.47 | -0.96 | -1.86 | 1.83 | -18.44 | 0.29 | 0.22 | 729 | 6521.82 |
| additive_ml_ext | CISO | 3.92 | 3.56 | -3.31 | -4.11 | 0.37 | -19.22 | 0.30 | 0.13 | 716 | 25235.45 |
| additive_ml_ext | DUK | 3.62 | 3.16 | -0.69 | -2.40 | 1.41 | -15.17 | 0.34 | 0.27 | 729 | 12124.38 |
| additive_ml_ext | ERCO | 3.60 | 3.17 | -2.25 | -3.07 | 1.11 | -19.08 | 0.30 | 0.15 | 725 | 46952.76 |
| additive_ml_ext | ISNE | 4.25 | 3.74 | -1.56 | -2.79 | 0.56 | -22.64 | 0.17 | 0.15 | 731 | 13367.24 |
| additive_ml_ext | MISO | 2.48 | 2.19 | -1.37 | -1.96 | 1.87 | -9.54 | 0.53 | 0.05 | 725 | 73818.42 |
| additive_ml_ext | NYIS | 2.75 | 2.38 | -0.79 | -2.05 | 0.62 | -15.60 | 0.50 | 0.60 | 731 | 17396.47 |
| additive_ml_ext | PJM | 2.85 | 2.51 | -0.64 | -1.84 | 1.78 | -12.22 | 0.74 | 0.50 | 723 | 91872.73 |
| additive_ml_ext | SWPP | 2.64 | 2.13 | -0.20 | -1.58 | 1.56 | -20.28 | 0.70 | 0.09 | 726 | 31381.35 |
| additive_ml_ext | TVA | 3.37 | 2.94 | -1.04 | -2.38 | 1.44 | -15.67 | 0.25 | 0.24 | 718 | 18548.22 |
| additive_ml_ext_separate | BPAT | 2.82 | 2.47 | -0.96 | -1.86 | 1.83 | -18.44 | 0.29 | 0.22 | 729 | 6521.82 |
| additive_ml_ext_separate | CISO | 3.92 | 3.56 | -3.31 | -4.11 | 0.37 | -19.22 | 0.30 | 0.13 | 716 | 25235.45 |
| additive_ml_ext_separate | DUK | 3.62 | 3.16 | -0.69 | -2.40 | 1.41 | -15.17 | 0.34 | 0.27 | 729 | 12124.38 |
| additive_ml_ext_separate | ERCO | 3.60 | 3.17 | -2.25 | -3.07 | 1.11 | -19.08 | 0.30 | 0.15 | 725 | 46952.76 |
| additive_ml_ext_separate | ISNE | 4.25 | 3.74 | -1.56 | -2.79 | 0.56 | -22.64 | 0.17 | 0.15 | 731 | 13367.24 |
| additive_ml_ext_separate | MISO | 2.48 | 2.19 | -1.37 | -1.96 | 1.87 | -9.54 | 0.53 | 0.05 | 725 | 73818.42 |
| additive_ml_ext_separate | NYIS | 2.75 | 2.38 | -0.79 | -2.05 | 0.62 | -15.60 | 0.50 | 0.60 | 731 | 17396.47 |
| additive_ml_ext_separate | PJM | 2.85 | 2.51 | -0.64 | -1.84 | 1.78 | -12.22 | 0.74 | 0.50 | 723 | 91872.73 |
| additive_ml_ext_separate | SWPP | 2.64 | 2.13 | -0.20 | -1.58 | 1.56 | -20.28 | 0.70 | 0.09 | 726 | 31381.35 |
| additive_ml_ext_separate | TVA | 3.37 | 2.94 | -1.04 | -2.38 | 1.44 | -15.67 | 0.25 | 0.24 | 718 | 18548.22 |
| additive_ml_ext_special | BPAT | 2.82 | 2.45 | -0.96 | -1.85 | 1.88 | -18.44 | 0.29 | 0.22 | 729 | 6521.82 |
| additive_ml_ext_special | CISO | 3.90 | 3.52 | -3.27 | -4.07 | 0.37 | -19.22 | 0.30 | 0.13 | 716 | 25235.45 |
| additive_ml_ext_special | DUK | 3.61 | 3.13 | -0.70 | -2.40 | 1.43 | -15.08 | 0.34 | 0.26 | 729 | 12124.38 |
| additive_ml_ext_special | ERCO | 3.60 | 3.15 | -2.25 | -3.08 | 1.10 | -19.19 | 0.30 | 0.15 | 725 | 46952.76 |
| additive_ml_ext_special | ISNE | 4.24 | 3.76 | -1.53 | -2.77 | 0.55 | -22.51 | 0.17 | 0.15 | 731 | 13367.24 |
| additive_ml_ext_special | MISO | 2.46 | 2.18 | -1.41 | -1.98 | 1.84 | -9.51 | 0.53 | 0.05 | 725 | 73818.42 |
| additive_ml_ext_special | NYIS | 2.74 | 2.37 | -0.77 | -2.04 | 0.60 | -15.59 | 0.50 | 0.59 | 731 | 17396.47 |
| additive_ml_ext_special | PJM | 2.84 | 2.49 | -0.64 | -1.84 | 1.76 | -12.25 | 0.75 | 0.50 | 723 | 91872.73 |
| additive_ml_ext_special | SWPP | 2.63 | 2.11 | -0.20 | -1.58 | 1.57 | -20.26 | 0.70 | 0.09 | 726 | 31381.35 |
| additive_ml_ext_special | TVA | 3.36 | 2.98 | -1.07 | -2.37 | 1.45 | -15.55 | 0.24 | 0.25 | 718 | 18548.22 |
| additive_multi | BPAT | 2.87 | 2.45 | -0.93 | -1.89 | 1.98 | -18.56 | 0.30 | 0.21 | 729 | 6521.82 |
| additive_multi | CISO | 3.97 | 3.55 | -2.24 | -3.51 | 0.38 | -18.55 | 0.31 | 0.18 | 716 | 25235.45 |
| additive_multi | DUK | 3.76 | 3.29 | -0.15 | -2.10 | 1.44 | -14.72 | 0.35 | 0.30 | 729 | 12124.38 |
| additive_multi | ERCO | 3.51 | 2.91 | -1.47 | -2.66 | 1.06 | -17.26 | 0.35 | 0.18 | 725 | 46952.76 |
| additive_multi | ISNE | 4.37 | 3.77 | -0.27 | -2.26 | 0.61 | -22.77 | 0.18 | 0.18 | 731 | 13367.24 |
| additive_multi | MISO | 2.71 | 2.45 | -0.53 | -1.65 | 1.87 | -9.36 | 0.47 | 0.06 | 725 | 73818.42 |
| additive_multi | NYIS | 2.94 | 2.39 | -0.20 | -1.84 | 0.67 | -16.20 | 0.48 | 0.63 | 731 | 17396.47 |
| additive_multi | PJM | 2.91 | 2.50 | 0.15 | -1.52 | 1.79 | -11.89 | 0.73 | 0.56 | 723 | 91872.73 |
| additive_multi | SWPP | 2.76 | 2.27 | -0.20 | -1.62 | 1.57 | -20.05 | 0.68 | 0.09 | 726 | 31381.35 |
| additive_multi | TVA | 3.71 | 3.21 | 0.40 | -1.70 | 1.45 | -11.78 | 0.21 | 0.31 | 718 | 18548.22 |
| boosting_ml | BPAT | 2.72 | 2.42 | -0.47 | -1.58 | 2.02 | -18.16 | 0.28 | 0.24 | 729 | 6521.82 |
| boosting_ml | CISO | 3.14 | 2.81 | -2.30 | -2.89 | 0.50 | -18.95 | 0.41 | 0.17 | 716 | 25235.45 |
| boosting_ml | DUK | 3.59 | 3.13 | -0.35 | -2.24 | 1.49 | -16.82 | 0.33 | 0.27 | 729 | 12124.38 |
| boosting_ml | ERCO | 3.15 | 2.73 | -2.32 | -3.02 | 1.28 | -15.00 | 0.35 | 0.17 | 725 | 46952.76 |
| boosting_ml | ISNE | 3.96 | 3.58 | -1.19 | -2.33 | 0.65 | -21.45 | 0.21 | 0.15 | 731 | 13367.24 |
| boosting_ml | MISO | 2.43 | 2.10 | -0.52 | -1.47 | 1.78 | -11.84 | 0.53 | 0.06 | 725 | 73818.42 |
| boosting_ml | NYIS | 2.73 | 2.41 | -0.47 | -1.63 | 0.76 | -14.02 | 0.50 | 0.66 | 731 | 17396.47 |
| boosting_ml | PJM | 2.85 | 2.57 | 0.15 | -1.44 | 1.82 | -11.75 | 0.75 | 0.56 | 723 | 91872.73 |
| boosting_ml | SWPP | 2.75 | 2.19 | -0.84 | -1.98 | 1.68 | -28.44 | 0.68 | 0.08 | 726 | 31381.35 |
| boosting_ml | TVA | 3.28 | 2.85 | -0.20 | -1.85 | 1.57 | -15.24 | 0.24 | 0.29 | 718 | 18548.22 |
| boosting_ml_ext | BPAT | 2.72 | 2.42 | -0.47 | -1.58 | 1.94 | -18.08 | 0.28 | 0.23 | 729 | 6521.82 |
| boosting_ml_ext | CISO | 3.13 | 2.78 | -2.37 | -2.94 | 0.51 | -18.97 | 0.43 | 0.16 | 716 | 25235.45 |
| boosting_ml_ext | DUK | 3.59 | 3.16 | -0.31 | -2.20 | 1.49 | -17.16 | 0.33 | 0.27 | 729 | 12124.38 |
| boosting_ml_ext | ERCO | 3.19 | 2.68 | -2.27 | -3.00 | 1.31 | -15.30 | 0.35 | 0.17 | 725 | 46952.76 |
| boosting_ml_ext | ISNE | 3.95 | 3.61 | -1.18 | -2.33 | 0.64 | -21.93 | 0.22 | 0.15 | 731 | 13367.24 |
| boosting_ml_ext | MISO | 2.40 | 2.10 | -0.46 | -1.43 | 1.72 | -11.41 | 0.55 | 0.06 | 725 | 73818.42 |
| boosting_ml_ext | NYIS | 2.74 | 2.40 | -0.43 | -1.62 | 0.77 | -15.02 | 0.50 | 0.65 | 731 | 17396.47 |
| boosting_ml_ext | PJM | 2.84 | 2.58 | 0.09 | -1.45 | 1.80 | -11.46 | 0.75 | 0.56 | 723 | 91872.73 |
| boosting_ml_ext | SWPP | 2.74 | 2.17 | -0.76 | -1.95 | 1.62 | -28.68 | 0.68 | 0.08 | 726 | 31381.35 |
| boosting_ml_ext | TVA | 3.29 | 2.84 | -0.22 | -1.85 | 1.58 | -14.90 | 0.24 | 0.29 | 718 | 18548.22 |
| boosting_multi | BPAT | 2.85 | 2.56 | -0.58 | -1.73 | 1.89 | -19.81 | 0.28 | 0.24 | 729 | 6521.82 |
| boosting_multi | CISO | 3.28 | 2.90 | -2.58 | -3.12 | 0.49 | -19.56 | 0.39 | 0.15 | 716 | 25235.45 |
| boosting_multi | DUK | 3.80 | 3.27 | -0.36 | -2.35 | 1.55 | -15.26 | 0.30 | 0.28 | 729 | 12124.38 |
| boosting_multi | ERCO | 3.20 | 2.68 | -2.13 | -2.91 | 1.29 | -17.98 | 0.36 | 0.19 | 725 | 46952.76 |
| boosting_multi | ISNE | 4.11 | 3.67 | -1.11 | -2.34 | 0.66 | -19.55 | 0.19 | 0.15 | 731 | 13367.24 |
| boosting_multi | MISO | 2.65 | 2.26 | -0.72 | -1.69 | 1.84 | -12.42 | 0.51 | 0.06 | 725 | 73818.42 |
| boosting_multi | NYIS | 2.87 | 2.51 | -0.39 | -1.70 | 0.69 | -15.69 | 0.48 | 0.66 | 731 | 17396.47 |
| boosting_multi | PJM | 3.09 | 2.76 | -0.02 | -1.66 | 1.89 | -12.72 | 0.69 | 0.52 | 723 | 91872.73 |
| boosting_multi | SWPP | 2.91 | 2.31 | -0.74 | -2.03 | 1.74 | -31.26 | 0.66 | 0.08 | 726 | 31381.35 |
| boosting_multi | TVA | 3.51 | 2.96 | -0.14 | -1.89 | 1.48 | -15.85 | 0.22 | 0.29 | 718 | 18548.22 |
| emp_additive_ml | BPAT | 2.75 | 2.39 | -0.97 | -1.92 | 1.93 | -19.56 | 0.31 | 0.21 | 729 | 6521.82 |
| emp_additive_ml | CISO | 3.09 | 2.75 | -0.23 | -1.88 | 0.36 | -14.57 | 0.44 | 0.24 | 716 | 25235.45 |
| emp_additive_ml | DUK | 3.55 | 3.13 | -0.97 | -2.53 | 1.40 | -16.55 | 0.35 | 0.27 | 729 | 12124.38 |
| emp_additive_ml | ERCO | 3.17 | 2.60 | -0.87 | -2.17 | 1.16 | -18.31 | 0.37 | 0.20 | 725 | 46952.76 |
| emp_additive_ml | ISNE | 4.05 | 3.61 | -0.42 | -2.21 | 0.55 | -23.56 | 0.22 | 0.17 | 731 | 13367.24 |
| emp_additive_ml | MISO | 2.33 | 2.04 | -0.49 | -1.44 | 1.74 | -8.84 | 0.56 | 0.06 | 725 | 73818.42 |
| emp_additive_ml | NYIS | 2.65 | 2.19 | -0.40 | -1.79 | 0.60 | -16.94 | 0.53 | 0.64 | 731 | 17396.47 |
| emp_additive_ml | PJM | 2.64 | 2.30 | -0.47 | -1.76 | 1.54 | -11.99 | 0.77 | 0.52 | 723 | 91872.73 |
| emp_additive_ml | SWPP | 2.55 | 2.10 | -0.68 | -1.77 | 1.57 | -20.58 | 0.72 | 0.09 | 726 | 31381.35 |
| emp_additive_ml | TVA | 3.27 | 2.83 | -0.94 | -2.35 | 1.46 | -15.27 | 0.26 | 0.25 | 718 | 18548.22 |
| ens_mean | BPAT | 2.59 | 2.28 | -0.71 | -1.64 | 1.77 | -18.26 | 0.32 | 0.22 | 729 | 6521.82 |
| ens_mean | CISO | 3.26 | 2.81 | -2.84 | -3.43 | 0.40 | -19.10 | 0.42 | 0.14 | 716 | 25235.45 |
| ens_mean | DUK | 3.46 | 2.98 | -0.50 | -2.23 | 1.29 | -15.95 | 0.37 | 0.28 | 729 | 12124.38 |
| ens_mean | ERCO | 3.20 | 2.68 | -2.26 | -2.94 | 1.06 | -14.96 | 0.36 | 0.17 | 725 | 46952.76 |
| ens_mean | ISNE | 3.87 | 3.47 | -1.37 | -2.46 | 0.52 | -22.29 | 0.23 | 0.14 | 731 | 13367.24 |
| ens_mean | MISO | 2.26 | 1.98 | -0.92 | -1.60 | 1.58 | -8.41 | 0.58 | 0.06 | 725 | 73818.42 |
| ens_mean | NYIS | 2.51 | 2.16 | -0.61 | -1.71 | 0.58 | -13.62 | 0.56 | 0.65 | 731 | 17396.47 |
| ens_mean | PJM | 2.64 | 2.40 | -0.27 | -1.55 | 1.54 | -11.14 | 0.78 | 0.54 | 723 | 91872.73 |
| ens_mean | SWPP | 2.53 | 1.97 | -0.48 | -1.69 | 1.47 | -20.93 | 0.71 | 0.08 | 726 | 31381.35 |
| ens_mean | TVA | 3.16 | 2.69 | -0.63 | -2.04 | 1.47 | -13.87 | 0.29 | 0.27 | 718 | 18548.22 |
| ens_mean3 | BPAT | 2.56 | 2.27 | -0.85 | -1.68 | 1.85 | -18.48 | 0.33 | 0.22 | 729 | 6521.82 |
| ens_mean3 | CISO | 3.46 | 3.14 | -2.66 | -3.40 | 0.43 | -17.46 | 0.35 | 0.15 | 716 | 25235.45 |
| ens_mean3 | DUK | 3.50 | 3.03 | -0.33 | -2.18 | 1.37 | -14.22 | 0.38 | 0.27 | 729 | 12124.38 |
| ens_mean3 | ERCO | 3.13 | 2.56 | -2.09 | -2.83 | 1.06 | -15.58 | 0.38 | 0.18 | 725 | 46952.76 |
| ens_mean3 | ISNE | 3.89 | 3.46 | -1.05 | -2.23 | 0.53 | -18.57 | 0.22 | 0.15 | 731 | 13367.24 |
| ens_mean3 | MISO | 2.35 | 2.08 | -0.91 | -1.65 | 1.64 | -8.83 | 0.55 | 0.04 | 725 | 73818.42 |
| ens_mean3 | NYIS | 2.50 | 2.11 | -0.46 | -1.61 | 0.60 | -14.69 | 0.57 | 0.67 | 731 | 17396.47 |
| ens_mean3 | PJM | 2.58 | 2.27 | -0.16 | -1.47 | 1.50 | -13.82 | 0.80 | 0.55 | 723 | 91872.73 |
| ens_mean3 | SWPP | 2.49 | 2.03 | -0.48 | -1.65 | 1.47 | -19.83 | 0.70 | 0.09 | 726 | 31381.35 |
| ens_mean3 | TVA | 3.27 | 2.85 | -0.22 | -1.90 | 1.40 | -14.40 | 0.27 | 0.29 | 718 | 18548.22 |
| ens_recent | BPAT | 2.58 | 2.27 | -0.72 | -1.63 | 1.81 | -18.28 | 0.32 | 0.22 | 729 | 6521.82 |
| ens_recent | CISO | 3.20 | 2.79 | -2.74 | -3.33 | 0.41 | -19.09 | 0.42 | 0.15 | 716 | 25235.45 |
| ens_recent | DUK | 3.46 | 2.98 | -0.50 | -2.23 | 1.30 | -16.02 | 0.37 | 0.28 | 729 | 12124.38 |
| ens_recent | ERCO | 3.18 | 2.68 | -2.24 | -2.92 | 1.05 | -14.75 | 0.36 | 0.17 | 725 | 46952.76 |
| ens_recent | ISNE | 3.86 | 3.47 | -1.35 | -2.44 | 0.52 | -22.26 | 0.23 | 0.14 | 731 | 13367.24 |
| ens_recent | MISO | 2.25 | 1.96 | -0.90 | -1.59 | 1.59 | -8.52 | 0.58 | 0.05 | 725 | 73818.42 |
| ens_recent | NYIS | 2.51 | 2.15 | -0.59 | -1.70 | 0.59 | -13.63 | 0.56 | 0.65 | 731 | 17396.47 |
| ens_recent | PJM | 2.64 | 2.40 | -0.28 | -1.55 | 1.54 | -11.05 | 0.78 | 0.53 | 723 | 91872.73 |
| ens_recent | SWPP | 2.53 | 1.97 | -0.47 | -1.68 | 1.52 | -20.88 | 0.71 | 0.08 | 726 | 31381.35 |
| ens_recent | TVA | 3.15 | 2.70 | -0.62 | -2.03 | 1.46 | -13.90 | 0.30 | 0.27 | 718 | 18548.22 |
| qboost_ml | BPAT | 2.71 | 2.47 | -0.53 | -1.62 | 1.84 | -19.39 | 0.28 | 0.24 | 729 | 6521.82 |
| qboost_ml | CISO | 3.18 | 2.81 | -2.39 | -2.99 | 0.55 | -17.73 | 0.40 | 0.15 | 716 | 25235.45 |
| qboost_ml | DUK | 3.55 | 3.09 | -0.49 | -2.28 | 1.45 | -15.82 | 0.36 | 0.27 | 729 | 12124.38 |
| qboost_ml | ERCO | 3.24 | 2.71 | -2.57 | -3.22 | 1.36 | -20.49 | 0.35 | 0.16 | 725 | 46952.76 |
| qboost_ml | ISNE | 4.00 | 3.65 | -1.20 | -2.35 | 0.67 | -19.80 | 0.20 | 0.15 | 731 | 13367.24 |
| qboost_ml | MISO | 2.46 | 2.12 | -0.38 | -1.44 | 1.80 | -11.82 | 0.54 | 0.07 | 725 | 73818.42 |
| qboost_ml | NYIS | 2.81 | 2.45 | -0.36 | -1.61 | 0.73 | -16.27 | 0.49 | 0.65 | 731 | 17396.47 |
| qboost_ml | PJM | 2.85 | 2.51 | -0.02 | -1.46 | 1.67 | -11.57 | 0.75 | 0.56 | 723 | 91872.73 |
| qboost_ml | SWPP | 2.68 | 2.17 | -0.59 | -1.80 | 1.66 | -22.59 | 0.68 | 0.09 | 726 | 31381.35 |
| qboost_ml | TVA | 3.28 | 2.82 | -0.31 | -1.92 | 1.55 | -14.58 | 0.24 | 0.28 | 718 | 18548.22 |
| recency_ml | BPAT | 3.37 | 2.88 | -1.13 | -2.18 | 1.90 | -18.92 | 0.23 | 0.22 | 729 | 6521.82 |
| recency_ml | CISO | 4.73 | 4.48 | -2.29 | -3.73 | 0.65 | -17.83 | 0.19 | 0.17 | 716 | 25235.45 |
| recency_ml | DUK | 4.29 | 3.82 | -0.00 | -2.41 | 1.52 | -18.13 | 0.26 | 0.26 | 729 | 12124.38 |
| recency_ml | ERCO | 3.71 | 3.04 | -1.76 | -2.98 | 1.14 | -17.32 | 0.32 | 0.20 | 725 | 46952.76 |
| recency_ml | ISNE | 4.78 | 4.33 | -0.40 | -2.16 | 0.63 | -18.65 | 0.13 | 0.17 | 731 | 13367.24 |
| recency_ml | MISO | 3.38 | 2.92 | -0.88 | -2.07 | 2.12 | -16.19 | 0.38 | 0.05 | 725 | 73818.42 |
| recency_ml | NYIS | 3.63 | 3.19 | -0.15 | -1.85 | 0.72 | -16.83 | 0.34 | 0.63 | 731 | 17396.47 |
| recency_ml | PJM | 3.40 | 2.95 | 0.08 | -1.76 | 1.87 | -30.94 | 0.63 | 0.51 | 723 | 91872.73 |
| recency_ml | SWPP | 3.20 | 2.66 | -0.47 | -1.98 | 1.72 | -17.64 | 0.58 | 0.09 | 726 | 31381.35 |
| recency_ml | TVA | 4.23 | 3.82 | 0.61 | -1.97 | 1.56 | -15.46 | 0.15 | 0.30 | 718 | 18548.22 |

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
| DF | PJM | uri | 2.82 | -1.01 | -1.14 | -2.03 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| additive_long | BPAT | uri | 3.05 | 0.66 | -0.79 | -3.92 | 6 |
| additive_long | CISO | uri | 2.75 | 1.20 | -0.23 | -0.94 | 6 |
| additive_long | DUK | uri | 3.74 | -1.42 | -1.85 | -6.75 | 6 |
| additive_long | ERCO | uri | 4.44 | -3.11 | -3.54 | -7.09 | 2 |
| additive_long | ISNE | uri | 3.52 | 0.97 | -0.35 | -1.13 | 6 |
| additive_long | MISO | uri | 5.35 | -3.73 | -4.49 | -8.36 | 5 |
| additive_long | NYIS | uri | 2.03 | 1.51 | -0.24 | -1.27 | 6 |
| additive_long | PJM | uri | 2.30 | -0.71 | -0.89 | -2.83 | 6 |
| additive_long | SWPP | uri | 7.99 | 4.17 | -1.10 | -4.40 | 4 |
| additive_long | TVA | uri | 5.12 | 1.67 | -1.24 | -3.99 | 6 |
| additive_ml | BPAT | uri | 3.12 | -0.34 | -1.37 | -3.10 | 6 |
| additive_ml | CISO | uri | 2.27 | 1.84 | 0.00 | 0.00 | 6 |
| additive_ml | DUK | uri | 3.49 | -2.75 | -2.75 | -7.66 | 6 |
| additive_ml | ERCO | uri | 4.96 | -5.47 | -5.47 | -8.10 | 2 |
| additive_ml | ISNE | uri | 3.14 | 0.91 | -0.50 | -2.09 | 6 |
| additive_ml | MISO | uri | 3.77 | -2.72 | -3.18 | -6.16 | 5 |
| additive_ml | NYIS | uri | 2.22 | 2.03 | -0.05 | -0.19 | 6 |
| additive_ml | PJM | uri | 2.91 | 2.19 | -0.45 | -2.56 | 6 |
| additive_ml | SWPP | uri | 6.62 | 1.73 | -1.91 | -5.32 | 4 |
| additive_ml | TVA | uri | 3.39 | -0.25 | -1.44 | -3.88 | 6 |
| additive_ml_ext | BPAT | uri | 2.94 | -0.21 | -1.22 | -2.63 | 6 |
| additive_ml_ext | CISO | uri | 2.27 | 1.83 | 0.00 | 0.00 | 6 |
| additive_ml_ext | DUK | uri | 3.50 | -2.65 | -2.65 | -7.89 | 6 |
| additive_ml_ext | ERCO | uri | 4.64 | -5.78 | -5.78 | -6.84 | 2 |
| additive_ml_ext | ISNE | uri | 3.19 | 1.79 | -0.33 | -1.98 | 6 |
| additive_ml_ext | MISO | uri | 4.43 | -2.11 | -2.91 | -5.96 | 5 |
| additive_ml_ext | NYIS | uri | 2.43 | 2.70 | -0.00 | -0.01 | 6 |
| additive_ml_ext | PJM | uri | 3.99 | 4.27 | -0.30 | -1.80 | 6 |
| additive_ml_ext | SWPP | uri | 6.67 | 1.11 | -1.90 | -5.74 | 4 |
| additive_ml_ext | TVA | uri | 3.43 | -1.22 | -2.01 | -4.40 | 6 |
| additive_ml_ext_separate | BPAT | uri | 2.94 | -0.21 | -1.22 | -2.63 | 6 |
| additive_ml_ext_separate | CISO | uri | 2.27 | 1.83 | 0.00 | 0.00 | 6 |
| additive_ml_ext_separate | DUK | uri | 3.50 | -2.65 | -2.65 | -7.89 | 6 |
| additive_ml_ext_separate | ERCO | uri | 4.64 | -5.78 | -5.78 | -6.84 | 2 |
| additive_ml_ext_separate | ISNE | uri | 3.19 | 1.79 | -0.33 | -1.98 | 6 |
| additive_ml_ext_separate | MISO | uri | 4.43 | -2.11 | -2.91 | -5.96 | 5 |
| additive_ml_ext_separate | NYIS | uri | 2.43 | 2.70 | -0.00 | -0.01 | 6 |
| additive_ml_ext_separate | PJM | uri | 3.99 | 4.27 | -0.30 | -1.80 | 6 |
| additive_ml_ext_separate | SWPP | uri | 6.67 | 1.11 | -1.90 | -5.74 | 4 |
| additive_ml_ext_separate | TVA | uri | 3.43 | -1.22 | -2.01 | -4.40 | 6 |
| additive_ml_ext_special | BPAT | uri | 3.09 | -0.28 | -1.26 | -2.91 | 6 |
| additive_ml_ext_special | CISO | uri | 2.30 | 1.97 | 0.00 | 0.00 | 6 |
| additive_ml_ext_special | DUK | uri | 3.46 | -2.63 | -2.63 | -7.85 | 6 |
| additive_ml_ext_special | ERCO | uri | 4.64 | -5.89 | -5.89 | -6.84 | 2 |
| additive_ml_ext_special | ISNE | uri | 3.22 | 1.82 | -0.32 | -1.92 | 6 |
| additive_ml_ext_special | MISO | uri | 4.17 | -2.01 | -2.76 | -5.50 | 5 |
| additive_ml_ext_special | NYIS | uri | 2.45 | 2.71 | -0.00 | -0.01 | 6 |
| additive_ml_ext_special | PJM | uri | 4.17 | 4.38 | -0.30 | -1.81 | 6 |
| additive_ml_ext_special | SWPP | uri | 6.63 | 1.18 | -1.85 | -5.53 | 4 |
| additive_ml_ext_special | TVA | uri | 3.30 | -0.73 | -1.62 | -3.28 | 6 |
| additive_multi | BPAT | uri | 2.78 | 0.35 | -0.45 | -1.97 | 6 |
| additive_multi | CISO | uri | 2.73 | 2.54 | -0.04 | -0.25 | 6 |
| additive_multi | DUK | uri | 3.42 | -1.61 | -1.70 | -7.45 | 6 |
| additive_multi | ERCO | uri | 5.16 | -6.62 | -6.62 | -7.27 | 2 |
| additive_multi | ISNE | uri | 3.79 | 3.65 | -0.11 | -0.67 | 6 |
| additive_multi | MISO | uri | 5.04 | -3.68 | -4.12 | -7.03 | 5 |
| additive_multi | NYIS | uri | 2.15 | 2.84 | -0.03 | -0.19 | 6 |
| additive_multi | PJM | uri | 2.34 | 1.19 | -0.41 | -2.45 | 6 |
| additive_multi | SWPP | uri | 6.87 | 1.42 | -2.10 | -4.69 | 4 |
| additive_multi | TVA | uri | 3.29 | 0.17 | -0.98 | -2.71 | 6 |
| boosting_ml | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| boosting_ml | CISO | uri | 1.94 | -1.22 | -1.32 | -3.36 | 6 |
| boosting_ml | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_ml | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| boosting_ml | ISNE | uri | 3.45 | 1.14 | -0.75 | -3.08 | 6 |
| boosting_ml | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_ml | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| boosting_ml | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_ml | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_ml | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| boosting_ml_ext | BPAT | uri | 3.55 | 0.84 | -1.09 | -5.22 | 6 |
| boosting_ml_ext | CISO | uri | 1.90 | -1.16 | -1.24 | -3.07 | 6 |
| boosting_ml_ext | DUK | uri | 3.60 | -1.97 | -2.06 | -4.15 | 6 |
| boosting_ml_ext | ERCO | uri | 9.48 | -13.16 | -13.16 | -15.30 | 2 |
| boosting_ml_ext | ISNE | uri | 3.53 | 1.05 | -0.87 | -3.94 | 6 |
| boosting_ml_ext | MISO | uri | 2.88 | -3.12 | -3.19 | -6.57 | 5 |
| boosting_ml_ext | NYIS | uri | 2.28 | 0.63 | -0.75 | -2.46 | 6 |
| boosting_ml_ext | PJM | uri | 2.06 | -1.42 | -1.44 | -3.69 | 6 |
| boosting_ml_ext | SWPP | uri | 5.39 | -1.87 | -3.73 | -9.50 | 4 |
| boosting_ml_ext | TVA | uri | 3.03 | -3.34 | -3.74 | -7.27 | 6 |
| boosting_multi | BPAT | uri | 3.19 | -0.44 | -1.39 | -3.52 | 6 |
| boosting_multi | CISO | uri | 1.86 | 0.14 | -0.65 | -2.17 | 6 |
| boosting_multi | DUK | uri | 4.08 | -3.14 | -3.14 | -5.91 | 6 |
| boosting_multi | ERCO | uri | 10.29 | -15.83 | -15.83 | -17.59 | 2 |
| boosting_multi | ISNE | uri | 3.74 | 0.94 | -0.56 | -3.12 | 6 |
| boosting_multi | MISO | uri | 6.70 | -7.12 | -7.12 | -12.42 | 5 |
| boosting_multi | NYIS | uri | 2.12 | 1.02 | -0.39 | -0.90 | 6 |
| boosting_multi | PJM | uri | 2.99 | -1.75 | -2.43 | -4.42 | 6 |
| boosting_multi | SWPP | uri | 6.73 | -3.47 | -4.61 | -11.41 | 4 |
| boosting_multi | TVA | uri | 4.22 | -5.52 | -5.75 | -8.77 | 6 |
| emp_additive_ml | BPAT | uri | 2.99 | -1.46 | -1.99 | -3.98 | 6 |
| emp_additive_ml | CISO | uri | 2.28 | -0.27 | -0.85 | -1.82 | 6 |
| emp_additive_ml | DUK | uri | 3.66 | -2.85 | -2.85 | -7.62 | 6 |
| emp_additive_ml | ERCO | uri | 4.95 | -6.08 | -6.08 | -6.22 | 2 |
| emp_additive_ml | ISNE | uri | 3.62 | 2.98 | -0.16 | -0.97 | 6 |
| emp_additive_ml | MISO | uri | 4.36 | -1.96 | -2.94 | -6.00 | 5 |
| emp_additive_ml | NYIS | uri | 2.55 | 2.89 | -0.00 | -0.01 | 6 |
| emp_additive_ml | PJM | uri | 3.54 | 3.33 | -0.21 | -1.22 | 6 |
| emp_additive_ml | SWPP | uri | 6.60 | 1.52 | -1.89 | -4.62 | 4 |
| emp_additive_ml | TVA | uri | 3.43 | -2.37 | -3.03 | -6.69 | 6 |
| ens_mean | BPAT | uri | 2.86 | 0.31 | -0.69 | -3.66 | 6 |
| ens_mean | CISO | uri | 1.78 | 0.34 | -0.28 | -1.00 | 6 |
| ens_mean | DUK | uri | 3.41 | -2.31 | -2.31 | -5.08 | 6 |
| ens_mean | ERCO | uri | 6.44 | -9.47 | -9.47 | -10.01 | 2 |
| ens_mean | ISNE | uri | 3.26 | 1.42 | -0.55 | -2.96 | 6 |
| ens_mean | MISO | uri | 3.62 | -2.62 | -3.01 | -6.00 | 5 |
| ens_mean | NYIS | uri | 2.24 | 1.67 | -0.22 | -1.23 | 6 |
| ens_mean | PJM | uri | 2.66 | 1.43 | -0.58 | -2.75 | 6 |
| ens_mean | SWPP | uri | 6.03 | -0.38 | -2.82 | -5.68 | 4 |
| ens_mean | TVA | uri | 2.86 | -2.28 | -2.79 | -5.34 | 6 |
| ens_mean3 | BPAT | uri | 2.65 | -0.28 | -0.91 | -4.25 | 6 |
| ens_mean3 | CISO | uri | 1.70 | 0.26 | -0.25 | -0.84 | 6 |
| ens_mean3 | DUK | uri | 3.58 | -3.00 | -3.00 | -5.76 | 6 |
| ens_mean3 | ERCO | uri | 5.45 | -7.54 | -7.54 | -9.58 | 2 |
| ens_mean3 | ISNE | uri | 2.91 | 0.73 | -0.51 | -2.90 | 6 |
| ens_mean3 | MISO | uri | 4.55 | -4.37 | -4.37 | -7.79 | 5 |
| ens_mean3 | NYIS | uri | 1.91 | 0.87 | -0.29 | -1.41 | 6 |
| ens_mean3 | PJM | uri | 2.28 | 0.05 | -1.00 | -4.02 | 6 |
| ens_mean3 | SWPP | uri | 6.20 | -2.04 | -3.82 | -8.07 | 4 |
| ens_mean3 | TVA | uri | 2.96 | -2.21 | -2.83 | -5.39 | 6 |
| ens_recent | BPAT | uri | 2.85 | 0.29 | -0.67 | -3.60 | 6 |
| ens_recent | CISO | uri | 1.79 | 0.38 | -0.26 | -0.97 | 6 |
| ens_recent | DUK | uri | 3.41 | -2.32 | -2.32 | -5.14 | 6 |
| ens_recent | ERCO | uri | 6.44 | -9.47 | -9.47 | -10.01 | 2 |
| ens_recent | ISNE | uri | 3.26 | 1.44 | -0.54 | -2.92 | 6 |
| ens_recent | MISO | uri | 3.63 | -2.63 | -3.00 | -6.00 | 5 |
| ens_recent | NYIS | uri | 2.25 | 1.79 | -0.18 | -1.09 | 6 |
| ens_recent | PJM | uri | 2.55 | 1.15 | -0.63 | -2.87 | 6 |
| ens_recent | SWPP | uri | 6.06 | -0.31 | -2.79 | -5.59 | 4 |
| ens_recent | TVA | uri | 2.86 | -2.26 | -2.77 | -5.30 | 6 |
| qboost_ml | BPAT | uri | 3.52 | 0.97 | -1.10 | -6.34 | 6 |
| qboost_ml | CISO | uri | 1.89 | -0.96 | -1.24 | -2.80 | 6 |
| qboost_ml | DUK | uri | 3.58 | -3.94 | -3.94 | -5.49 | 6 |
| qboost_ml | ERCO | uri | 13.59 | -18.23 | -18.23 | -20.49 | 2 |
| qboost_ml | ISNE | uri | 3.45 | 0.69 | -0.57 | -2.57 | 6 |
| qboost_ml | MISO | uri | 3.80 | -3.75 | -3.98 | -8.76 | 5 |
| qboost_ml | NYIS | uri | 2.31 | 0.70 | -0.70 | -1.99 | 6 |
| qboost_ml | PJM | uri | 2.08 | -0.71 | -1.08 | -3.43 | 6 |
| qboost_ml | SWPP | uri | 6.19 | -3.50 | -4.80 | -10.88 | 4 |
| qboost_ml | TVA | uri | 2.89 | -2.95 | -3.34 | -6.49 | 6 |
| recency_ml | BPAT | uri | 2.83 | -1.46 | -1.97 | -5.41 | 6 |
| recency_ml | CISO | uri | 1.79 | 0.11 | -0.29 | -0.73 | 6 |
| recency_ml | DUK | uri | 4.12 | -4.38 | -4.38 | -7.13 | 6 |
| recency_ml | ERCO | uri | 6.30 | -3.70 | -5.44 | -10.88 | 2 |
| recency_ml | ISNE | uri | 2.86 | -0.65 | -0.87 | -2.78 | 6 |
| recency_ml | MISO | uri | 8.12 | -7.89 | -7.89 | -11.39 | 5 |
| recency_ml | NYIS | uri | 3.15 | -0.74 | -1.01 | -3.82 | 6 |
| recency_ml | PJM | uri | 3.13 | -2.70 | -2.70 | -6.56 | 6 |
| recency_ml | SWPP | uri | 6.56 | -5.37 | -5.84 | -12.85 | 4 |
| recency_ml | TVA | uri | 3.93 | -2.05 | -2.92 | -5.50 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 4.02 | -3.14 | -3.14 | -5.88 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| additive_long | BPAT | elliott | 4.86 | -1.46 | -3.10 | -6.26 | 5 |
| additive_long | CISO | elliott | 5.25 | 5.88 | -0.27 | -1.35 | 5 |
| additive_long | DUK | elliott | 6.21 | 0.68 | -1.16 | -3.17 | 4 |
| additive_long | ERCO | elliott | 9.48 | -6.92 | -6.93 | -19.57 | 5 |
| additive_long | ISNE | elliott | 3.83 | 1.57 | -0.94 | -2.84 | 5 |
| additive_long | MISO | elliott | 5.29 | -2.58 | -3.59 | -7.59 | 5 |
| additive_long | NYIS | elliott | 3.31 | 0.45 | -1.55 | -6.98 | 5 |
| additive_long | PJM | elliott | 4.47 | -1.42 | -2.19 | -7.20 | 5 |
| additive_long | SWPP | elliott | 4.52 | -4.75 | -4.75 | -9.71 | 5 |
| additive_long | TVA | elliott | 8.31 | 5.63 | 0.00 | 0.00 | 3 |
| additive_ml | BPAT | elliott | 4.56 | -0.92 | -2.54 | -4.95 | 5 |
| additive_ml | CISO | elliott | 4.35 | 4.24 | -0.06 | -0.29 | 5 |
| additive_ml | DUK | elliott | 4.35 | -2.16 | -2.16 | -3.28 | 4 |
| additive_ml | ERCO | elliott | 8.00 | -4.71 | -5.80 | -12.54 | 5 |
| additive_ml | ISNE | elliott | 4.29 | 1.36 | -0.76 | -2.56 | 5 |
| additive_ml | MISO | elliott | 3.98 | -1.49 | -2.44 | -4.99 | 5 |
| additive_ml | NYIS | elliott | 3.06 | -2.29 | -2.61 | -4.34 | 5 |
| additive_ml | PJM | elliott | 4.16 | -1.15 | -2.44 | -5.36 | 5 |
| additive_ml | SWPP | elliott | 3.99 | -1.82 | -2.27 | -6.75 | 5 |
| additive_ml | TVA | elliott | 8.53 | 6.71 | 0.00 | 0.00 | 3 |
| additive_ml_ext | BPAT | elliott | 4.48 | -1.08 | -2.71 | -5.65 | 5 |
| additive_ml_ext | CISO | elliott | 4.34 | 4.24 | -0.06 | -0.30 | 5 |
| additive_ml_ext | DUK | elliott | 4.68 | -3.49 | -3.49 | -7.21 | 4 |
| additive_ml_ext | ERCO | elliott | 8.09 | -4.89 | -5.87 | -19.08 | 5 |
| additive_ml_ext | ISNE | elliott | 4.14 | 1.33 | -0.66 | -2.13 | 5 |
| additive_ml_ext | MISO | elliott | 4.00 | -1.63 | -2.53 | -4.84 | 5 |
| additive_ml_ext | NYIS | elliott | 3.05 | -2.25 | -2.59 | -4.26 | 5 |
| additive_ml_ext | PJM | elliott | 4.11 | -0.88 | -2.25 | -5.07 | 5 |
| additive_ml_ext | SWPP | elliott | 3.91 | -1.22 | -2.03 | -4.79 | 5 |
| additive_ml_ext | TVA | elliott | 7.89 | 5.54 | -0.20 | -0.60 | 3 |
| additive_ml_ext_separate | BPAT | elliott | 4.48 | -1.08 | -2.71 | -5.65 | 5 |
| additive_ml_ext_separate | CISO | elliott | 4.34 | 4.24 | -0.06 | -0.30 | 5 |
| additive_ml_ext_separate | DUK | elliott | 4.68 | -3.49 | -3.49 | -7.21 | 4 |
| additive_ml_ext_separate | ERCO | elliott | 8.09 | -4.89 | -5.87 | -19.08 | 5 |
| additive_ml_ext_separate | ISNE | elliott | 4.14 | 1.33 | -0.66 | -2.13 | 5 |
| additive_ml_ext_separate | MISO | elliott | 4.00 | -1.63 | -2.53 | -4.84 | 5 |
| additive_ml_ext_separate | NYIS | elliott | 3.05 | -2.25 | -2.59 | -4.26 | 5 |
| additive_ml_ext_separate | PJM | elliott | 4.11 | -0.88 | -2.25 | -5.07 | 5 |
| additive_ml_ext_separate | SWPP | elliott | 3.91 | -1.22 | -2.03 | -4.79 | 5 |
| additive_ml_ext_separate | TVA | elliott | 7.89 | 5.54 | -0.20 | -0.60 | 3 |
| additive_ml_ext_special | BPAT | elliott | 4.19 | -1.63 | -2.63 | -5.64 | 5 |
| additive_ml_ext_special | CISO | elliott | 3.89 | 2.67 | -0.55 | -2.76 | 5 |
| additive_ml_ext_special | DUK | elliott | 4.50 | -4.19 | -4.19 | -6.16 | 4 |
| additive_ml_ext_special | ERCO | elliott | 7.96 | -5.32 | -6.15 | -19.19 | 5 |
| additive_ml_ext_special | ISNE | elliott | 4.42 | 0.92 | -0.79 | -2.82 | 5 |
| additive_ml_ext_special | MISO | elliott | 3.44 | -3.33 | -3.69 | -6.36 | 5 |
| additive_ml_ext_special | NYIS | elliott | 3.26 | -1.86 | -2.34 | -3.61 | 5 |
| additive_ml_ext_special | PJM | elliott | 3.63 | -1.72 | -2.44 | -6.20 | 5 |
| additive_ml_ext_special | SWPP | elliott | 3.57 | -1.91 | -2.59 | -5.57 | 5 |
| additive_ml_ext_special | TVA | elliott | 7.47 | 4.34 | -0.84 | -2.53 | 3 |
| additive_multi | BPAT | elliott | 4.80 | -2.32 | -3.79 | -7.97 | 5 |
| additive_multi | CISO | elliott | 4.22 | 4.21 | -0.02 | -0.11 | 5 |
| additive_multi | DUK | elliott | 6.39 | -5.00 | -5.17 | -9.17 | 4 |
| additive_multi | ERCO | elliott | 9.68 | -7.85 | -9.04 | -17.26 | 5 |
| additive_multi | ISNE | elliott | 4.80 | 4.05 | -0.46 | -1.28 | 5 |
| additive_multi | MISO | elliott | 5.16 | 6.10 | -0.34 | -1.69 | 5 |
| additive_multi | NYIS | elliott | 2.59 | -0.97 | -1.67 | -2.56 | 5 |
| additive_multi | PJM | elliott | 5.62 | -0.11 | -2.30 | -7.15 | 5 |
| additive_multi | SWPP | elliott | 4.61 | -2.06 | -3.18 | -8.59 | 5 |
| additive_multi | TVA | elliott | 6.15 | 1.51 | -0.46 | -1.37 | 3 |
| boosting_ml | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| boosting_ml | CISO | elliott | 3.66 | 1.13 | -0.69 | -3.11 | 5 |
| boosting_ml | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| boosting_ml | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| boosting_ml | ISNE | elliott | 3.61 | 2.38 | -0.33 | -1.12 | 5 |
| boosting_ml | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| boosting_ml | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| boosting_ml | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| boosting_ml | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| boosting_ml | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |
| boosting_ml_ext | BPAT | elliott | 4.32 | -5.38 | -5.38 | -11.84 | 5 |
| boosting_ml_ext | CISO | elliott | 3.70 | 1.18 | -0.79 | -3.49 | 5 |
| boosting_ml_ext | DUK | elliott | 4.19 | -3.34 | -3.34 | -5.88 | 4 |
| boosting_ml_ext | ERCO | elliott | 6.22 | -5.61 | -6.14 | -11.82 | 5 |
| boosting_ml_ext | ISNE | elliott | 3.56 | 2.30 | -0.35 | -0.98 | 5 |
| boosting_ml_ext | MISO | elliott | 3.57 | -0.91 | -2.12 | -3.60 | 5 |
| boosting_ml_ext | NYIS | elliott | 2.80 | -0.16 | -1.26 | -3.26 | 5 |
| boosting_ml_ext | PJM | elliott | 4.83 | -2.21 | -3.12 | -6.04 | 5 |
| boosting_ml_ext | SWPP | elliott | 4.62 | -1.65 | -3.73 | -11.08 | 5 |
| boosting_ml_ext | TVA | elliott | 6.21 | -0.58 | -1.88 | -4.28 | 3 |
| boosting_multi | BPAT | elliott | 4.18 | -5.04 | -5.47 | -10.51 | 5 |
| boosting_multi | CISO | elliott | 3.44 | 0.56 | -1.07 | -4.18 | 5 |
| boosting_multi | DUK | elliott | 5.60 | -8.96 | -8.96 | -13.16 | 4 |
| boosting_multi | ERCO | elliott | 7.00 | -3.83 | -5.63 | -12.32 | 5 |
| boosting_multi | ISNE | elliott | 4.07 | 3.71 | -0.09 | -0.45 | 5 |
| boosting_multi | MISO | elliott | 5.19 | -0.71 | -2.80 | -5.40 | 5 |
| boosting_multi | NYIS | elliott | 3.30 | -0.21 | -1.50 | -2.86 | 5 |
| boosting_multi | PJM | elliott | 4.77 | -6.53 | -6.53 | -12.72 | 5 |
| boosting_multi | SWPP | elliott | 4.79 | -1.38 | -3.35 | -10.76 | 5 |
| boosting_multi | TVA | elliott | 5.39 | -1.74 | -1.94 | -5.52 | 3 |
| emp_additive_ml | BPAT | elliott | 4.37 | -0.73 | -2.42 | -5.22 | 5 |
| emp_additive_ml | CISO | elliott | 4.42 | 4.77 | -0.01 | -0.03 | 5 |
| emp_additive_ml | DUK | elliott | 4.78 | -2.34 | -2.62 | -7.42 | 4 |
| emp_additive_ml | ERCO | elliott | 8.24 | -4.04 | -5.33 | -18.31 | 5 |
| emp_additive_ml | ISNE | elliott | 4.06 | 2.31 | -0.31 | -1.44 | 5 |
| emp_additive_ml | MISO | elliott | 4.52 | -0.18 | -1.68 | -3.76 | 5 |
| emp_additive_ml | NYIS | elliott | 2.52 | 0.76 | -0.46 | -1.23 | 5 |
| emp_additive_ml | PJM | elliott | 4.41 | 1.03 | -1.17 | -3.71 | 5 |
| emp_additive_ml | SWPP | elliott | 4.27 | 0.21 | -1.28 | -3.24 | 5 |
| emp_additive_ml | TVA | elliott | 7.61 | 5.07 | -0.32 | -0.96 | 3 |
| ens_mean | BPAT | elliott | 4.19 | -3.23 | -3.72 | -8.44 | 5 |
| ens_mean | CISO | elliott | 3.53 | 2.71 | -0.38 | -1.90 | 5 |
| ens_mean | DUK | elliott | 4.30 | -3.42 | -3.42 | -6.54 | 4 |
| ens_mean | ERCO | elliott | 6.89 | -5.25 | -6.00 | -14.96 | 5 |
| ens_mean | ISNE | elliott | 3.48 | 1.82 | -0.51 | -1.56 | 5 |
| ens_mean | MISO | elliott | 3.70 | -1.27 | -2.27 | -4.22 | 5 |
| ens_mean | NYIS | elliott | 2.59 | -1.21 | -1.93 | -3.73 | 5 |
| ens_mean | PJM | elliott | 4.34 | -1.54 | -2.68 | -5.56 | 5 |
| ens_mean | SWPP | elliott | 3.98 | -1.44 | -2.88 | -6.74 | 5 |
| ens_mean | TVA | elliott | 6.60 | 2.48 | -0.46 | -0.99 | 3 |
| ens_mean3 | BPAT | elliott | 3.36 | -1.58 | -2.32 | -8.22 | 5 |
| ens_mean3 | CISO | elliott | 4.11 | 4.82 | 0.00 | 0.00 | 5 |
| ens_mean3 | DUK | elliott | 3.73 | -3.01 | -3.01 | -4.13 | 4 |
| ens_mean3 | ERCO | elliott | 5.70 | -4.24 | -4.82 | -7.49 | 5 |
| ens_mean3 | ISNE | elliott | 3.42 | 3.11 | -0.39 | -1.24 | 5 |
| ens_mean3 | MISO | elliott | 4.22 | -1.55 | -2.76 | -7.92 | 5 |
| ens_mean3 | NYIS | elliott | 2.50 | -0.91 | -1.70 | -3.94 | 5 |
| ens_mean3 | PJM | elliott | 5.40 | -6.25 | -6.55 | -13.82 | 5 |
| ens_mean3 | SWPP | elliott | 3.30 | -1.08 | -2.34 | -5.59 | 5 |
| ens_mean3 | TVA | elliott | 5.84 | 2.00 | -1.06 | -1.74 | 3 |
| ens_recent | BPAT | elliott | 4.19 | -3.37 | -3.80 | -8.69 | 5 |
| ens_recent | CISO | elliott | 3.45 | 2.43 | -0.44 | -2.18 | 5 |
| ens_recent | DUK | elliott | 4.31 | -3.41 | -3.41 | -6.56 | 4 |
| ens_recent | ERCO | elliott | 6.84 | -5.28 | -6.02 | -14.73 | 5 |
| ens_recent | ISNE | elliott | 3.47 | 1.84 | -0.50 | -1.52 | 5 |
| ens_recent | MISO | elliott | 3.67 | -1.22 | -2.25 | -4.14 | 5 |
| ens_recent | NYIS | elliott | 2.60 | -1.18 | -1.91 | -3.73 | 5 |
| ens_recent | PJM | elliott | 4.31 | -1.51 | -2.66 | -5.53 | 5 |
| ens_recent | SWPP | elliott | 4.00 | -1.47 | -2.93 | -6.99 | 5 |
| ens_recent | TVA | elliott | 6.58 | 2.45 | -0.45 | -0.98 | 3 |
| qboost_ml | BPAT | elliott | 4.26 | -5.57 | -5.89 | -12.50 | 5 |
| qboost_ml | CISO | elliott | 3.71 | 0.96 | -1.53 | -7.67 | 5 |
| qboost_ml | DUK | elliott | 5.04 | -6.89 | -6.89 | -10.02 | 4 |
| qboost_ml | ERCO | elliott | 6.73 | -7.86 | -8.54 | -14.06 | 5 |
| qboost_ml | ISNE | elliott | 3.72 | 3.80 | -0.25 | -1.25 | 5 |
| qboost_ml | MISO | elliott | 3.89 | -0.46 | -1.47 | -4.38 | 5 |
| qboost_ml | NYIS | elliott | 2.79 | 0.14 | -0.91 | -2.24 | 5 |
| qboost_ml | PJM | elliott | 4.31 | -2.06 | -3.02 | -5.59 | 5 |
| qboost_ml | SWPP | elliott | 4.53 | -3.43 | -3.91 | -11.43 | 5 |
| qboost_ml | TVA | elliott | 5.42 | -0.65 | -1.71 | -4.76 | 3 |
| recency_ml | BPAT | elliott | 4.02 | 1.73 | -1.56 | -7.79 | 5 |
| recency_ml | CISO | elliott | 5.97 | 9.03 | 0.00 | 0.00 | 5 |
| recency_ml | DUK | elliott | 3.33 | -2.21 | -3.00 | -5.50 | 4 |
| recency_ml | ERCO | elliott | 6.39 | -2.22 | -4.70 | -9.53 | 5 |
| recency_ml | ISNE | elliott | 4.18 | 5.70 | -0.36 | -1.79 | 5 |
| recency_ml | MISO | elliott | 5.61 | -2.12 | -4.13 | -16.19 | 5 |
| recency_ml | NYIS | elliott | 3.00 | -0.33 | -1.68 | -4.37 | 5 |
| recency_ml | PJM | elliott | 11.18 | -15.67 | -15.67 | -30.94 | 5 |
| recency_ml | SWPP | elliott | 2.86 | -0.38 | -1.53 | -5.61 | 5 |
| recency_ml | TVA | elliott | 4.75 | 1.03 | -2.26 | -3.53 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | DF | eve | 3.43 | 0.94 | -1.08 |  | 235 |
| 29 | ens_recent | eve | 3.55 | 0.56 | -1.62 | 0.49 | 235 |
| 27 | ens_mean | eve | 3.55 | 0.56 | -1.63 | 0.48 | 235 |
| 28 | ens_mean3 | eve | 3.57 | 0.54 | -1.67 | 0.47 | 235 |
| 21 | additive_ml_ext_special | eve | 3.66 | 0.10 | -1.97 | 0.44 | 235 |
| 24 | boosting_ml_ext | eve | 3.73 | 0.63 | -1.67 | 0.44 | 235 |
| 18 | additive_ml | eve | 3.75 | 0.47 | -1.73 | 0.44 | 235 |
| 19 | additive_ml_ext | eve | 3.76 | 0.48 | -1.73 | 0.44 | 235 |
| 20 | additive_ml_ext_separate | eve | 3.76 | 0.48 | -1.73 | 0.44 | 235 |
| 23 | boosting_ml | eve | 3.76 | 0.64 | -1.65 | 0.43 | 235 |
| 30 | qboost_ml | eve | 3.86 | 0.58 | -1.68 | 0.41 | 235 |
| 26 | emp_additive_ml | eve | 3.90 | 1.43 | -1.28 | 0.39 | 235 |
| 25 | boosting_multi | eve | 4.14 | 1.10 | -1.63 | 0.39 | 235 |
| 22 | additive_multi | eve | 4.20 | 1.85 | -1.32 | 0.38 | 235 |
| 17 | additive_long | eve | 4.42 | 0.44 | -2.20 | 0.34 | 235 |
| 31 | recency_ml | eve | 4.43 | 0.50 | -2.13 | 0.34 | 235 |
| 13 | ens_recent | special | 3.57 | -0.74 | -2.23 | 0.50 | 247 |
| 11 | ens_mean | special | 3.58 | -0.74 | -2.23 | 0.50 | 247 |
| 5 | additive_ml_ext_special | special | 3.59 | -1.58 | -2.78 | 0.49 | 247 |
| 12 | ens_mean3 | special | 3.65 | -0.52 | -2.23 | 0.49 | 247 |
| 8 | boosting_ml_ext | special | 3.67 | -0.90 | -2.33 | 0.47 | 247 |
| 0 | DF | special | 3.69 | 0.26 | -1.48 |  | 247 |
| 7 | boosting_ml | special | 3.70 | -0.88 | -2.32 | 0.45 | 247 |
| 14 | qboost_ml | special | 3.86 | -0.92 | -2.40 | 0.45 | 247 |
| 2 | additive_ml | special | 3.92 | -0.59 | -2.35 | 0.44 | 247 |
| 3 | additive_ml_ext | special | 3.92 | -0.58 | -2.34 | 0.45 | 247 |
| 4 | additive_ml_ext_separate | special | 3.92 | -0.58 | -2.34 | 0.45 | 247 |
| 10 | emp_additive_ml | special | 3.96 | 0.24 | -1.89 | 0.45 | 247 |
| 9 | boosting_multi | special | 4.17 | -0.50 | -2.34 | 0.42 | 247 |
| 6 | additive_multi | special | 4.28 | 0.71 | -1.77 | 0.40 | 247 |
| 1 | additive_long | special | 4.57 | -1.10 | -2.96 | 0.37 | 247 |
| 15 | recency_ml | special | 4.69 | -0.07 | -2.58 | 0.34 | 247 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| emp_additive_ml | all | 0.439 | 1.502 | 0.434 | 0.848 | 11.199 | 0.847 | 7253 |
| qboost_ml | all | 0.511 | 1.538 | 0.540 | 0.728 | 8.963 | 0.699 | 7253 |
| emp_additive_ml | events | 0.739 | 2.083 | 0.650 | 0.723 | 11.199 | 0.800 | 100 |
| qboost_ml | events | 0.623 | 1.977 | 0.725 | 0.695 | 11.238 | 0.700 | 100 |
| emp_additive_ml | cold_mornings | 0.577 | 1.839 | 0.584 | 0.763 | 11.046 | 0.790 | 300 |
| qboost_ml | cold_mornings | 0.565 | 1.789 | 0.713 | 0.713 | 10.771 | 0.640 | 300 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 34675 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 34685 | DUK | 2022-12-24 | additive_long | 6.42 | -10.46 | -10.46 |
| 34672 | DUK | 2022-12-24 | additive_ml | 5.40 | -10.83 | -10.83 |
| 34679 | DUK | 2022-12-24 | additive_ml_ext | 5.26 | -10.73 | -10.73 |
| 34684 | DUK | 2022-12-24 | additive_ml_ext_separate | 5.26 | -10.73 | -10.73 |
| 34683 | DUK | 2022-12-24 | additive_ml_ext_special | 7.19 | -12.60 | -12.60 |
| 34686 | DUK | 2022-12-24 | additive_multi | 10.74 | -19.81 | -19.81 |
| 34673 | DUK | 2022-12-24 | boosting_ml | 9.36 | -15.80 | -15.80 |
| 34680 | DUK | 2022-12-24 | boosting_ml_ext | 9.41 | -16.37 | -16.37 |
| 34687 | DUK | 2022-12-24 | boosting_multi | 11.99 | -20.52 | -20.52 |
| 34682 | DUK | 2022-12-24 | emp_additive_ml | 4.88 | -8.73 | -8.73 |
| 34676 | DUK | 2022-12-24 | ens_mean | 7.32 | -13.55 | -13.55 |
| 34678 | DUK | 2022-12-24 | ens_mean3 | 7.02 | -10.01 | -10.01 |
| 34677 | DUK | 2022-12-24 | ens_recent | 7.29 | -13.50 | -13.50 |
| 34681 | DUK | 2022-12-24 | qboost_ml | 10.87 | -17.71 | -17.71 |
| 34674 | DUK | 2022-12-24 | recency_ml | 6.41 | -2.92 | -2.92 |
| 35651 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 35661 | ERCO | 2021-02-15 | additive_long | 41.10 | -1.69 | -1.69 |
| 35648 | ERCO | 2021-02-15 | additive_ml | 41.73 | -4.19 | -4.19 |
| 35655 | ERCO | 2021-02-15 | additive_ml_ext | 29.46 | -7.20 | -7.20 |
| 35660 | ERCO | 2021-02-15 | additive_ml_ext_separate | 29.46 | -7.20 | -7.20 |
| 35659 | ERCO | 2021-02-15 | additive_ml_ext_special | 29.55 | -7.22 | -7.22 |
| 35662 | ERCO | 2021-02-15 | additive_multi | 26.51 | -13.89 | -13.89 |
| 35649 | ERCO | 2021-02-15 | boosting_ml | 27.39 | -16.57 | -16.57 |
| 35656 | ERCO | 2021-02-15 | boosting_ml_ext | 26.52 | -16.47 | -16.47 |
| 35663 | ERCO | 2021-02-15 | boosting_multi | 21.27 | -17.98 | -17.98 |
| 35658 | ERCO | 2021-02-15 | emp_additive_ml | 29.19 | -7.55 | -7.55 |
| 35652 | ERCO | 2021-02-15 | ens_mean | 27.99 | -11.83 | -11.83 |
| 35654 | ERCO | 2021-02-15 | ens_mean3 | 43.30 | -1.47 | -1.47 |
| 35653 | ERCO | 2021-02-15 | ens_recent | 28.02 | -11.74 | -11.74 |
| 35657 | ERCO | 2021-02-15 | qboost_ml | 22.06 | -18.64 | -18.64 |
| 35650 | ERCO | 2021-02-15 | recency_ml | 76.77 | 19.26 | 0.00 |
| 35667 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 35677 | ERCO | 2021-02-16 | additive_long | 52.45 | 46.85 | 0.00 |
| 35664 | ERCO | 2021-02-16 | additive_ml | 47.11 | 43.31 | 0.00 |
| 35671 | ERCO | 2021-02-16 | additive_ml_ext | 29.65 | 27.49 | 0.00 |
| 35676 | ERCO | 2021-02-16 | additive_ml_ext_separate | 29.65 | 27.49 | 0.00 |
| 35675 | ERCO | 2021-02-16 | additive_ml_ext_special | 29.77 | 26.95 | 0.00 |
| 35678 | ERCO | 2021-02-16 | additive_multi | 34.99 | 36.46 | 0.00 |
| 35665 | ERCO | 2021-02-16 | boosting_ml | 33.46 | 31.10 | 0.00 |
| 35672 | ERCO | 2021-02-16 | boosting_ml_ext | 32.49 | 31.35 | 0.00 |
| 35679 | ERCO | 2021-02-16 | boosting_multi | 26.88 | 23.64 | 0.00 |
| 35674 | ERCO | 2021-02-16 | emp_additive_ml | 29.36 | 27.39 | 0.00 |
| 35668 | ERCO | 2021-02-16 | ens_mean | 31.07 | 29.42 | 0.00 |
| 35670 | ERCO | 2021-02-16 | ens_mean3 | 48.40 | 52.95 | 0.00 |
| 35669 | ERCO | 2021-02-16 | ens_recent | 31.01 | 29.34 | 0.00 |
| 35673 | ERCO | 2021-02-16 | qboost_ml | 26.32 | 24.65 | 0.00 |
| 35666 | ERCO | 2021-02-16 | recency_ml | 83.08 | 100.02 | 0.00 |
| 35683 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 35693 | ERCO | 2021-02-17 | additive_long | 35.15 | 33.44 | 0.00 |
| 35680 | ERCO | 2021-02-17 | additive_ml | 31.71 | 29.79 | 0.00 |
| 35687 | ERCO | 2021-02-17 | additive_ml_ext | 30.52 | 26.67 | 0.00 |
| 35692 | ERCO | 2021-02-17 | additive_ml_ext_separate | 30.52 | 26.67 | 0.00 |
| 35691 | ERCO | 2021-02-17 | additive_ml_ext_special | 30.56 | 26.67 | 0.00 |
| 35694 | ERCO | 2021-02-17 | additive_multi | 31.70 | 32.07 | 0.00 |
| 35681 | ERCO | 2021-02-17 | boosting_ml | 28.91 | 24.01 | 0.00 |
| 35688 | ERCO | 2021-02-17 | boosting_ml_ext | 28.70 | 22.57 | 0.00 |
| 35695 | ERCO | 2021-02-17 | boosting_multi | 24.61 | 18.29 | 0.00 |
| 35690 | ERCO | 2021-02-17 | emp_additive_ml | 30.26 | 24.59 | 0.00 |
| 35684 | ERCO | 2021-02-17 | ens_mean | 29.61 | 24.62 | 0.00 |
| 35686 | ERCO | 2021-02-17 | ens_mean3 | 33.63 | 29.45 | 0.00 |
| 35685 | ERCO | 2021-02-17 | ens_recent | 29.63 | 24.67 | 0.00 |
| 35689 | ERCO | 2021-02-17 | qboost_ml | 23.26 | 17.16 | 0.00 |
| 35682 | ERCO | 2021-02-17 | recency_ml | 41.67 | 39.12 | 0.00 |
| 35699 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 35709 | ERCO | 2021-02-18 | additive_long | 8.08 | 5.87 | 0.00 |
| 35696 | ERCO | 2021-02-18 | additive_ml | 13.42 | 12.91 | 0.00 |
| 35703 | ERCO | 2021-02-18 | additive_ml_ext | 13.61 | 14.19 | 0.00 |
| 35708 | ERCO | 2021-02-18 | additive_ml_ext_separate | 13.61 | 14.19 | 0.00 |
| 35707 | ERCO | 2021-02-18 | additive_ml_ext_special | 13.66 | 14.18 | 0.00 |
| 35710 | ERCO | 2021-02-18 | additive_multi | 12.43 | 10.18 | 0.00 |
| 35697 | ERCO | 2021-02-18 | boosting_ml | 3.58 | -2.96 | -2.96 |
| 35704 | ERCO | 2021-02-18 | boosting_ml_ext | 13.04 | 7.25 | 0.00 |
| 35711 | ERCO | 2021-02-18 | boosting_multi | 4.42 | -3.21 | -3.21 |
| 35706 | ERCO | 2021-02-18 | emp_additive_ml | 13.27 | 15.10 | 0.00 |
| 35700 | ERCO | 2021-02-18 | ens_mean | 13.33 | 10.72 | 0.00 |
| 35702 | ERCO | 2021-02-18 | ens_mean3 | 11.12 | 8.57 | 0.00 |
| 35701 | ERCO | 2021-02-18 | ens_recent | 13.33 | 10.81 | 0.00 |
| 35705 | ERCO | 2021-02-18 | qboost_ml | 8.70 | 4.37 | 0.00 |
| 35698 | ERCO | 2021-02-18 | recency_ml | 6.71 | 4.27 | 0.00 |
| 59027 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 59037 | MISO | 2021-02-16 | additive_long | 2.23 | -1.57 | -1.57 |
| 59024 | MISO | 2021-02-16 | additive_ml | 2.23 | 1.64 | 0.00 |
| 59031 | MISO | 2021-02-16 | additive_ml_ext | 1.75 | 1.21 | 0.00 |
| 59036 | MISO | 2021-02-16 | additive_ml_ext_separate | 1.75 | 1.21 | 0.00 |
| 59035 | MISO | 2021-02-16 | additive_ml_ext_special | 1.82 | 1.67 | 0.00 |
| 59038 | MISO | 2021-02-16 | additive_multi | 2.85 | -2.38 | -2.38 |
| 59025 | MISO | 2021-02-16 | boosting_ml | 2.11 | 0.99 | 0.00 |
| 59032 | MISO | 2021-02-16 | boosting_ml_ext | 2.56 | 1.68 | 0.00 |
| 59039 | MISO | 2021-02-16 | boosting_multi | 4.02 | -4.78 | -4.78 |
| 59034 | MISO | 2021-02-16 | emp_additive_ml | 2.01 | 2.03 | 0.00 |
| 59028 | MISO | 2021-02-16 | ens_mean | 2.02 | 1.45 | 0.00 |
| 59030 | MISO | 2021-02-16 | ens_mean3 | 1.41 | -0.72 | -0.72 |
| 59029 | MISO | 2021-02-16 | ens_recent | 2.03 | 1.45 | 0.00 |
| 59033 | MISO | 2021-02-16 | qboost_ml | 2.99 | 1.79 | 0.00 |
| 59026 | MISO | 2021-02-16 | recency_ml | 6.15 | -5.04 | -5.04 |
| 93891 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 93901 | SWPP | 2021-02-15 | additive_long | 4.52 | 2.27 | 0.00 |
| 93888 | SWPP | 2021-02-15 | additive_ml | 2.70 | 1.05 | 0.00 |
| 93895 | SWPP | 2021-02-15 | additive_ml_ext | 2.81 | 0.69 | 0.00 |
| 93900 | SWPP | 2021-02-15 | additive_ml_ext_separate | 2.81 | 0.69 | 0.00 |
| 93899 | SWPP | 2021-02-15 | additive_ml_ext_special | 2.81 | 0.72 | 0.00 |
| 93902 | SWPP | 2021-02-15 | additive_multi | 2.27 | -3.16 | -3.16 |
| 93889 | SWPP | 2021-02-15 | boosting_ml | 5.58 | -7.79 | -7.79 |
| 93896 | SWPP | 2021-02-15 | boosting_ml_ext | 5.34 | -7.86 | -7.86 |
| 93903 | SWPP | 2021-02-15 | boosting_multi | 6.63 | -9.64 | -9.64 |
| 93898 | SWPP | 2021-02-15 | emp_additive_ml | 2.44 | 1.66 | 0.00 |
| 93892 | SWPP | 2021-02-15 | ens_mean | 2.29 | -3.59 | -3.59 |
| 93894 | SWPP | 2021-02-15 | ens_mean3 | 3.68 | -4.67 | -4.67 |
| 93893 | SWPP | 2021-02-15 | ens_recent | 2.26 | -3.46 | -3.46 |
| 93897 | SWPP | 2021-02-15 | qboost_ml | 3.91 | -7.17 | -7.17 |
| 93890 | SWPP | 2021-02-15 | recency_ml | 7.32 | -6.84 | -6.84 |
| 93907 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 93917 | SWPP | 2021-02-16 | additive_long | 9.32 | 6.48 | 0.00 |
| 93904 | SWPP | 2021-02-16 | additive_ml | 8.08 | 3.24 | 0.00 |
| 93911 | SWPP | 2021-02-16 | additive_ml_ext | 8.57 | 4.05 | 0.00 |
| 93916 | SWPP | 2021-02-16 | additive_ml_ext_separate | 8.57 | 4.05 | 0.00 |
| 93915 | SWPP | 2021-02-16 | additive_ml_ext_special | 8.63 | 4.10 | 0.00 |
| 93918 | SWPP | 2021-02-16 | additive_multi | 6.69 | 0.04 | 0.00 |
| 93905 | SWPP | 2021-02-16 | boosting_ml | 3.72 | -6.44 | -6.44 |
| 93912 | SWPP | 2021-02-16 | boosting_ml_ext | 4.44 | -6.87 | -6.87 |
| 93919 | SWPP | 2021-02-16 | boosting_multi | 3.60 | -8.83 | -8.83 |
| 93914 | SWPP | 2021-02-16 | emp_additive_ml | 8.05 | 4.04 | 0.00 |
| 93908 | SWPP | 2021-02-16 | ens_mean | 5.72 | -1.41 | -1.41 |
| 93910 | SWPP | 2021-02-16 | ens_mean3 | 3.78 | -1.14 | -1.14 |
| 93909 | SWPP | 2021-02-16 | ens_recent | 5.77 | -1.21 | -1.21 |
| 93913 | SWPP | 2021-02-16 | qboost_ml | 4.14 | -6.16 | -6.16 |
| 93906 | SWPP | 2021-02-16 | recency_ml | 4.08 | -0.60 | -0.60 |
| 116067 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 116077 | TVA | 2022-12-23 | additive_long | 7.93 | -6.77 | -6.77 |
| 116064 | TVA | 2022-12-23 | additive_ml | 6.64 | -5.03 | -5.03 |
| 116071 | TVA | 2022-12-23 | additive_ml_ext | 6.20 | -5.20 | -5.20 |
| 116076 | TVA | 2022-12-23 | additive_ml_ext_separate | 6.20 | -5.20 | -5.20 |
| 116075 | TVA | 2022-12-23 | additive_ml_ext_special | 6.11 | -5.40 | -5.40 |
| 116078 | TVA | 2022-12-23 | additive_multi | 14.19 | -15.37 | -15.37 |
| 116065 | TVA | 2022-12-23 | boosting_ml | 13.98 | -15.00 | -15.00 |
| 116072 | TVA | 2022-12-23 | boosting_ml_ext | 13.35 | -14.63 | -14.63 |
| 116079 | TVA | 2022-12-23 | boosting_multi | 16.93 | -18.92 | -18.92 |
| 116074 | TVA | 2022-12-23 | emp_additive_ml | 6.85 | -6.69 | -6.69 |
| 116068 | TVA | 2022-12-23 | ens_mean | 9.17 | -9.92 | -9.92 |
| 116070 | TVA | 2022-12-23 | ens_mean3 | 10.46 | -13.35 | -13.35 |
| 116069 | TVA | 2022-12-23 | ens_recent | 9.25 | -10.02 | -10.02 |
| 116073 | TVA | 2022-12-23 | qboost_ml | 12.65 | -15.80 | -15.80 |
| 116066 | TVA | 2022-12-23 | recency_ml | 15.95 | -20.21 | -20.21 |
| 116083 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 116093 | TVA | 2022-12-24 | additive_long | 3.98 | -9.72 | -9.72 |
| 116080 | TVA | 2022-12-24 | additive_ml | 4.47 | -7.00 | -7.00 |
| 116087 | TVA | 2022-12-24 | additive_ml_ext | 4.52 | -6.80 | -6.80 |
| 116092 | TVA | 2022-12-24 | additive_ml_ext_separate | 4.52 | -6.80 | -6.80 |
| 116091 | TVA | 2022-12-24 | additive_ml_ext_special | 3.35 | -8.26 | -8.26 |
| 116094 | TVA | 2022-12-24 | additive_multi | 7.38 | -16.89 | -16.89 |
| 116081 | TVA | 2022-12-24 | boosting_ml | 6.04 | -12.78 | -12.78 |
| 116088 | TVA | 2022-12-24 | boosting_ml_ext | 6.20 | -12.49 | -12.49 |
| 116095 | TVA | 2022-12-24 | boosting_multi | 8.24 | -17.45 | -17.45 |
| 116090 | TVA | 2022-12-24 | emp_additive_ml | 3.71 | -6.68 | -6.68 |
| 116084 | TVA | 2022-12-24 | ens_mean | 4.17 | -9.65 | -9.65 |
| 116086 | TVA | 2022-12-24 | ens_mean3 | 5.05 | -10.59 | -10.59 |
| 116085 | TVA | 2022-12-24 | ens_recent | 4.23 | -9.74 | -9.74 |
| 116089 | TVA | 2022-12-24 | qboost_ml | 5.56 | -15.55 | -15.55 |
| 116082 | TVA | 2022-12-24 | recency_ml | 8.62 | -12.48 | -12.48 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_long | BPAT | mape | 15.538 | 0.000 | 729 |
| additive_long | CISO | mape | 15.317 | 0.000 | 716 |
| additive_long | DUK | mape | 11.890 | 0.000 | 729 |
| additive_long | ERCO | mape | 11.698 | 0.000 | 725 |
| additive_long | ISNE | mape | 26.298 | 0.000 | 731 |
| additive_long | MISO | mape | 2.968 | 0.003 | 725 |
| additive_long | NYIS | mape | 9.410 | 0.000 | 731 |
| additive_long | PJM | mape | 0.955 | 0.340 | 723 |
| additive_long | SWPP | mape | -3.928 | 0.000 | 726 |
| additive_long | TVA | mape | 19.344 | 0.000 | 718 |
| additive_ml | BPAT | mape | 12.273 | 0.000 | 729 |
| additive_ml | CISO | mape | 13.797 | 0.000 | 716 |
| additive_ml | DUK | mape | 9.977 | 0.000 | 729 |
| additive_ml | ERCO | mape | 11.747 | 0.000 | 725 |
| additive_ml | ISNE | mape | 23.917 | 0.000 | 731 |
| additive_ml | MISO | mape | -2.391 | 0.017 | 725 |
| additive_ml | NYIS | mape | 1.213 | 0.225 | 731 |
| additive_ml | PJM | mape | -14.102 | 0.000 | 723 |
| additive_ml | SWPP | mape | -14.238 | 0.000 | 726 |
| additive_ml | TVA | mape | 17.048 | 0.000 | 718 |
| additive_ml_ext | BPAT | mape | 12.363 | 0.000 | 729 |
| additive_ml_ext | CISO | mape | 13.831 | 0.000 | 716 |
| additive_ml_ext | DUK | mape | 10.156 | 0.000 | 729 |
| additive_ml_ext | ERCO | mape | 11.688 | 0.000 | 725 |
| additive_ml_ext | ISNE | mape | 24.093 | 0.000 | 731 |
| additive_ml_ext | MISO | mape | -2.199 | 0.028 | 725 |
| additive_ml_ext | NYIS | mape | 1.282 | 0.200 | 731 |
| additive_ml_ext | PJM | mape | -13.707 | 0.000 | 723 |
| additive_ml_ext | SWPP | mape | -14.314 | 0.000 | 726 |
| additive_ml_ext | TVA | mape | 17.075 | 0.000 | 718 |
| additive_ml_ext_separate | BPAT | mape | 12.363 | 0.000 | 729 |
| additive_ml_ext_separate | CISO | mape | 13.831 | 0.000 | 716 |
| additive_ml_ext_separate | DUK | mape | 10.156 | 0.000 | 729 |
| additive_ml_ext_separate | ERCO | mape | 11.688 | 0.000 | 725 |
| additive_ml_ext_separate | ISNE | mape | 24.093 | 0.000 | 731 |
| additive_ml_ext_separate | MISO | mape | -2.199 | 0.028 | 725 |
| additive_ml_ext_separate | NYIS | mape | 1.282 | 0.200 | 731 |
| additive_ml_ext_separate | PJM | mape | -13.707 | 0.000 | 723 |
| additive_ml_ext_separate | SWPP | mape | -14.314 | 0.000 | 726 |
| additive_ml_ext_separate | TVA | mape | 17.075 | 0.000 | 718 |
| additive_ml_ext_special | BPAT | mape | 12.386 | 0.000 | 729 |
| additive_ml_ext_special | CISO | mape | 13.565 | 0.000 | 716 |
| additive_ml_ext_special | DUK | mape | 10.144 | 0.000 | 729 |
| additive_ml_ext_special | ERCO | mape | 11.685 | 0.000 | 725 |
| additive_ml_ext_special | ISNE | mape | 24.044 | 0.000 | 731 |
| additive_ml_ext_special | MISO | mape | -2.423 | 0.015 | 725 |
| additive_ml_ext_special | NYIS | mape | 1.224 | 0.221 | 731 |
| additive_ml_ext_special | PJM | mape | -13.803 | 0.000 | 723 |
| additive_ml_ext_special | SWPP | mape | -14.369 | 0.000 | 726 |
| additive_ml_ext_special | TVA | mape | 17.199 | 0.000 | 718 |
| additive_multi | BPAT | mape | 13.054 | 0.000 | 729 |
| additive_multi | CISO | mape | 12.979 | 0.000 | 716 |
| additive_multi | DUK | mape | 11.241 | 0.000 | 729 |
| additive_multi | ERCO | mape | 10.386 | 0.000 | 725 |
| additive_multi | ISNE | mape | 23.690 | 0.000 | 731 |
| additive_multi | MISO | mape | 0.892 | 0.372 | 725 |
| additive_multi | NYIS | mape | 3.632 | 0.000 | 731 |
| additive_multi | PJM | mape | -11.309 | 0.000 | 723 |
| additive_multi | SWPP | mape | -12.547 | 0.000 | 726 |
| additive_multi | TVA | mape | 19.646 | 0.000 | 718 |
| boosting_ml | BPAT | mape | 12.134 | 0.000 | 729 |
| boosting_ml | CISO | mape | 4.197 | 0.000 | 716 |
| boosting_ml | DUK | mape | 10.116 | 0.000 | 729 |
| boosting_ml | ERCO | mape | 6.427 | 0.000 | 725 |
| boosting_ml | ISNE | mape | 21.913 | 0.000 | 731 |
| boosting_ml | MISO | mape | -3.022 | 0.003 | 725 |
| boosting_ml | NYIS | mape | 1.018 | 0.308 | 731 |
| boosting_ml | PJM | mape | -14.253 | 0.000 | 723 |
| boosting_ml | SWPP | mape | -11.352 | 0.000 | 726 |
| boosting_ml | TVA | mape | 16.249 | 0.000 | 718 |
| boosting_ml_ext | BPAT | mape | 12.327 | 0.000 | 729 |
| boosting_ml_ext | CISO | mape | 3.974 | 0.000 | 716 |
| boosting_ml_ext | DUK | mape | 10.175 | 0.000 | 729 |
| boosting_ml_ext | ERCO | mape | 7.446 | 0.000 | 725 |
| boosting_ml_ext | ISNE | mape | 21.801 | 0.000 | 731 |
| boosting_ml_ext | MISO | mape | -3.393 | 0.001 | 725 |
| boosting_ml_ext | NYIS | mape | 1.187 | 0.235 | 731 |
| boosting_ml_ext | PJM | mape | -14.523 | 0.000 | 723 |
| boosting_ml_ext | SWPP | mape | -11.421 | 0.000 | 726 |
| boosting_ml_ext | TVA | mape | 16.303 | 0.000 | 718 |
| boosting_multi | BPAT | mape | 14.162 | 0.000 | 729 |
| boosting_multi | CISO | mape | 5.799 | 0.000 | 716 |
| boosting_multi | DUK | mape | 12.167 | 0.000 | 729 |
| boosting_multi | ERCO | mape | 7.260 | 0.000 | 725 |
| boosting_multi | ISNE | mape | 22.292 | 0.000 | 731 |
| boosting_multi | MISO | mape | 0.079 | 0.937 | 725 |
| boosting_multi | NYIS | mape | 3.084 | 0.002 | 731 |
| boosting_multi | PJM | mape | -9.040 | 0.000 | 723 |
| boosting_multi | SWPP | mape | -9.392 | 0.000 | 726 |
| boosting_multi | TVA | mape | 18.571 | 0.000 | 718 |
| emp_additive_ml | BPAT | mape | 11.320 | 0.000 | 729 |
| emp_additive_ml | CISO | mape | 3.382 | 0.001 | 716 |
| emp_additive_ml | DUK | mape | 9.341 | 0.000 | 729 |
| emp_additive_ml | ERCO | mape | 7.591 | 0.000 | 725 |
| emp_additive_ml | ISNE | mape | 21.807 | 0.000 | 731 |
| emp_additive_ml | MISO | mape | -4.747 | 0.000 | 725 |
| emp_additive_ml | NYIS | mape | -0.123 | 0.902 | 731 |
| emp_additive_ml | PJM | mape | -16.625 | 0.000 | 723 |
| emp_additive_ml | SWPP | mape | -15.297 | 0.000 | 726 |
| emp_additive_ml | TVA | mape | 16.426 | 0.000 | 718 |
| ens_mean | BPAT | mape | 9.655 | 0.000 | 729 |
| ens_mean | CISO | mape | 5.713 | 0.000 | 716 |
| ens_mean | DUK | mape | 8.516 | 0.000 | 729 |
| ens_mean | ERCO | mape | 7.420 | 0.000 | 725 |
| ens_mean | ISNE | mape | 20.815 | 0.000 | 731 |
| ens_mean | MISO | mape | -5.501 | 0.000 | 725 |
| ens_mean | NYIS | mape | -2.230 | 0.026 | 731 |
| ens_mean | PJM | mape | -18.465 | 0.000 | 723 |
| ens_mean | SWPP | mape | -15.055 | 0.000 | 726 |
| ens_mean | TVA | mape | 14.642 | 0.000 | 718 |
| ens_mean3 | BPAT | mape | 9.234 | 0.000 | 729 |
| ens_mean3 | CISO | mape | 8.684 | 0.000 | 716 |
| ens_mean3 | DUK | mape | 8.859 | 0.000 | 729 |
| ens_mean3 | ERCO | mape | 6.363 | 0.000 | 725 |
| ens_mean3 | ISNE | mape | 21.279 | 0.000 | 731 |
| ens_mean3 | MISO | mape | -4.027 | 0.000 | 725 |
| ens_mean3 | NYIS | mape | -2.401 | 0.016 | 731 |
| ens_mean3 | PJM | mape | -19.498 | 0.000 | 723 |
| ens_mean3 | SWPP | mape | -15.950 | 0.000 | 726 |
| ens_mean3 | TVA | mape | 16.591 | 0.000 | 718 |
| ens_recent | BPAT | mape | 9.570 | 0.000 | 729 |
| ens_recent | CISO | mape | 4.899 | 0.000 | 716 |
| ens_recent | DUK | mape | 8.496 | 0.000 | 729 |
| ens_recent | ERCO | mape | 7.235 | 0.000 | 725 |
| ens_recent | ISNE | mape | 20.717 | 0.000 | 731 |
| ens_recent | MISO | mape | -5.627 | 0.000 | 725 |
| ens_recent | NYIS | mape | -2.245 | 0.025 | 731 |
| ens_recent | PJM | mape | -18.532 | 0.000 | 723 |
| ens_recent | SWPP | mape | -15.205 | 0.000 | 726 |
| ens_recent | TVA | mape | 14.561 | 0.000 | 718 |
| qboost_ml | BPAT | mape | 12.089 | 0.000 | 729 |
| qboost_ml | CISO | mape | 4.672 | 0.000 | 716 |
| qboost_ml | DUK | mape | 9.584 | 0.000 | 729 |
| qboost_ml | ERCO | mape | 7.832 | 0.000 | 725 |
| qboost_ml | ISNE | mape | 22.746 | 0.000 | 731 |
| qboost_ml | MISO | mape | -2.591 | 0.010 | 725 |
| qboost_ml | NYIS | mape | 2.245 | 0.025 | 731 |
| qboost_ml | PJM | mape | -14.118 | 0.000 | 723 |
| qboost_ml | SWPP | mape | -13.074 | 0.000 | 726 |
| qboost_ml | TVA | mape | 16.474 | 0.000 | 718 |
| recency_ml | BPAT | mape | 18.386 | 0.000 | 729 |
| recency_ml | CISO | mape | 22.530 | 0.000 | 716 |
| recency_ml | DUK | mape | 16.148 | 0.000 | 729 |
| recency_ml | ERCO | mape | 12.369 | 0.000 | 725 |
| recency_ml | ISNE | mape | 28.186 | 0.000 | 731 |
| recency_ml | MISO | mape | 8.199 | 0.000 | 725 |
| recency_ml | NYIS | mape | 11.830 | 0.000 | 731 |
| recency_ml | PJM | mape | -3.128 | 0.002 | 723 |
| recency_ml | SWPP | mape | -6.995 | 0.000 | 726 |
| recency_ml | TVA | mape | 25.161 | 0.000 | 718 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| additive_long | 0.986 |
| additive_ml | 0.986 |
| additive_ml_ext | 0.986 |
| additive_ml_ext_separate | 0.986 |
| additive_ml_ext_special | 0.986 |
| additive_multi | 0.986 |
| boosting_ml | 0.995 |
| boosting_ml_ext | 0.995 |
| boosting_multi | 0.995 |
| emp_additive_ml | 0.958 |
| ens_mean | 0.995 |
| ens_mean3 | 0.995 |
| ens_recent | 0.995 |
| qboost_ml | 0.995 |
| recency_ml | 0.995 |
