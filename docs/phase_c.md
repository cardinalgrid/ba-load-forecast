# Phase C: model families and data options against the BA's forecast

Development BAs (BPAT, CISO, DUK, ERCO, ISNE, MISO, NYIS, PJM, SWPP, TVA), 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature. Groups: one station with the gross-fault guard (`single`: recency regression, additive with and without special-day indicators, with the shape-cluster label and as a separate special-day model, boosting with and without indicators and with the cluster label); several stations per BA (`_multi`); history cleaned by grid-data-sentinel (`_sentinel`); six years of training (`_long`). Two floors of phase B are kept as references. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 3.00 | 2.70 | 0.27 | -1.12 | 1.07 | 0.00 | 0.00 | -19.98 | 7457 | 10.00 |
| additive_long | 3.55 | 3.00 | -0.89 | -2.46 | 1.62 | 0.43 | 0.26 | -26.57 | 7457 | 10.00 |
| boosting_long | 3.70 | 3.08 | -0.89 | -2.45 | 1.70 | 0.41 | 0.27 | -27.80 | 7457 | 10.00 |
| additive_sentinel | 3.73 | 3.12 | -0.38 | -2.26 | 1.69 | 0.41 | 0.28 | -26.29 | 7457 | 10.00 |
| additive_special | 3.74 | 3.14 | -0.42 | -2.29 | 1.68 | 0.41 | 0.28 | -26.30 | 7457 | 10.00 |
| additive | 3.74 | 3.12 | -0.43 | -2.28 | 1.68 | 0.41 | 0.28 | -26.35 | 7457 | 10.00 |
| additive_separate | 3.74 | 3.12 | -0.43 | -2.28 | 1.68 | 0.41 | 0.28 | -26.35 | 7457 | 10.00 |
| boosting_sentinel | 3.89 | 3.18 | -0.94 | -2.56 | 1.74 | 0.39 | 0.27 | -30.61 | 7457 | 10.00 |
| boosting | 3.91 | 3.19 | -1.01 | -2.61 | 1.78 | 0.38 | 0.26 | -28.98 | 7457 | 10.00 |
| boosting_nospecial | 3.91 | 3.22 | -1.01 | -2.62 | 1.80 | 0.38 | 0.26 | -29.93 | 7457 | 10.00 |
| recency_regression | 4.27 | 3.64 | -0.60 | -2.49 | 1.84 | 0.33 | 0.28 | -26.14 | 7457 | 10.00 |
| recency_regression_sentinel | 4.28 | 3.64 | -0.59 | -2.48 | 1.83 | 0.33 | 0.27 | -26.20 | 7457 | 10.00 |
| additive_cluster | 4.60 | 3.83 | -0.56 | -2.86 | 2.11 | 0.32 | 0.26 | -32.54 | 7457 | 10.00 |
| boosting_cluster | 4.71 | 3.79 | -1.17 | -3.12 | 1.99 | 0.31 | 0.24 | -33.73 | 7457 | 10.00 |
| profile | 6.86 | 5.29 | -1.48 | -4.34 | 2.13 | 0.21 | 0.23 | -44.25 | 7457 | 10.00 |
| last_known_day | 6.95 | 5.82 | -0.91 | -4.23 | 2.55 | 0.19 | 0.24 | -44.26 | 7457 | 10.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 3.65 | 3.48 | -1.47 | -1.91 | 1.63 | -10.72 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.78 | 3.49 | 2.58 | -0.43 | 1.22 | -19.98 |  |  | 741 | 31300.49 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| additive | BPAT | 3.22 | 2.78 | -0.45 | -1.87 | 2.02 | -18.01 | 0.26 | 0.24 | 750 | 6533.15 |
| additive | CISO | 4.59 | 4.02 | -0.09 | -2.75 | 0.64 | -26.35 | 0.27 | 0.26 | 737 | 25196.91 |
| additive | DUK | 4.06 | 3.53 | -0.34 | -2.32 | 1.48 | -17.12 | 0.28 | 0.30 | 750 | 12129.97 |
| additive | ERCO | 3.64 | 3.10 | -1.45 | -2.81 | 1.19 | -19.26 | 0.29 | 0.20 | 746 | 46782.53 |
| additive | ISNE | 5.05 | 4.49 | -1.48 | -3.18 | 0.64 | -25.75 | 0.12 | 0.17 | 752 | 13392.81 |
| additive | MISO | 3.04 | 2.50 | -0.42 | -1.90 | 2.24 | -15.42 | 0.44 | 0.06 | 746 | 73788.38 |
| additive | NYIS | 3.55 | 2.93 | -0.72 | -2.43 | 0.77 | -25.84 | 0.39 | 0.61 | 752 | 17400.75 |
| additive | PJM | 3.90 | 3.22 | 0.06 | -2.15 | 2.08 | -17.44 | 0.57 | 0.52 | 744 | 91927.69 |
| additive | SWPP | 3.64 | 2.80 | -0.06 | -2.05 | 1.62 | -21.66 | 0.54 | 0.07 | 741 | 31300.49 |
| additive | TVA | 4.13 | 3.53 | -0.36 | -2.27 | 1.77 | -16.13 | 0.20 | 0.28 | 739 | 18562.62 |
| additive_cluster | BPAT | 3.75 | 3.14 | -0.78 | -2.34 | 2.11 | -18.55 | 0.21 | 0.23 | 750 | 6533.15 |
| additive_cluster | CISO | 6.00 | 5.09 | -2.44 | -5.00 | 0.66 | -32.54 | 0.16 | 0.25 | 737 | 25196.91 |
| additive_cluster | DUK | 5.23 | 4.58 | -0.55 | -3.00 | 1.69 | -19.63 | 0.17 | 0.27 | 750 | 12129.97 |
| additive_cluster | ERCO | 4.18 | 3.58 | -1.76 | -3.28 | 1.50 | -20.46 | 0.23 | 0.18 | 746 | 46782.53 |
| additive_cluster | ISNE | 5.52 | 4.80 | -0.78 | -2.92 | 0.68 | -24.65 | 0.09 | 0.19 | 752 | 13392.81 |
| additive_cluster | MISO | 3.94 | 3.24 | 0.30 | -2.02 | 2.68 | -17.72 | 0.35 | 0.07 | 746 | 73788.38 |
| additive_cluster | NYIS | 3.82 | 3.15 | 0.35 | -1.88 | 0.78 | -23.70 | 0.36 | 0.67 | 752 | 17400.75 |
| additive_cluster | PJM | 4.88 | 3.97 | -0.68 | -3.13 | 2.93 | -25.64 | 0.42 | 0.46 | 744 | 91927.69 |
| additive_cluster | SWPP | 4.60 | 3.63 | 1.04 | -2.12 | 1.99 | -21.72 | 0.46 | 0.08 | 741 | 31300.49 |
| additive_cluster | TVA | 5.00 | 4.38 | -1.10 | -3.12 | 2.06 | -20.25 | 0.13 | 0.25 | 739 | 18562.62 |
| additive_long | BPAT | 3.12 | 2.69 | -0.64 | -1.92 | 1.73 | -17.50 | 0.25 | 0.25 | 750 | 6533.15 |
| additive_long | CISO | 4.31 | 3.78 | -0.76 | -2.94 | 0.57 | -26.57 | 0.28 | 0.27 | 737 | 25196.91 |
| additive_long | DUK | 3.77 | 3.32 | -0.88 | -2.54 | 1.39 | -17.37 | 0.32 | 0.27 | 750 | 12129.97 |
| additive_long | ERCO | 3.60 | 3.02 | -1.30 | -2.68 | 1.21 | -19.57 | 0.33 | 0.22 | 746 | 46782.53 |
| additive_long | ISNE | 4.75 | 4.20 | -2.23 | -3.38 | 0.61 | -25.28 | 0.12 | 0.14 | 752 | 13392.81 |
| additive_long | MISO | 2.87 | 2.32 | -1.17 | -2.27 | 1.98 | -16.14 | 0.47 | 0.04 | 746 | 73788.38 |
| additive_long | NYIS | 3.49 | 2.86 | -0.94 | -2.56 | 0.75 | -25.13 | 0.41 | 0.59 | 752 | 17400.75 |
| additive_long | PJM | 3.72 | 3.20 | -0.36 | -2.27 | 2.18 | -16.84 | 0.56 | 0.50 | 744 | 91927.69 |
| additive_long | SWPP | 3.37 | 2.66 | -0.18 | -2.00 | 1.52 | -20.79 | 0.57 | 0.08 | 741 | 31300.49 |
| additive_long | TVA | 3.81 | 3.37 | -1.81 | -3.03 | 1.70 | -16.92 | 0.21 | 0.20 | 739 | 18562.62 |
| additive_sentinel | BPAT | 3.21 | 2.77 | -0.41 | -1.84 | 2.01 | -17.93 | 0.26 | 0.24 | 750 | 6533.15 |
| additive_sentinel | CISO | 4.59 | 3.99 | -0.09 | -2.76 | 0.65 | -26.29 | 0.26 | 0.26 | 737 | 25196.91 |
| additive_sentinel | DUK | 4.06 | 3.53 | -0.34 | -2.32 | 1.48 | -17.12 | 0.28 | 0.30 | 750 | 12129.97 |
| additive_sentinel | ERCO | 3.64 | 3.10 | -1.45 | -2.81 | 1.19 | -19.26 | 0.29 | 0.20 | 746 | 46782.53 |
| additive_sentinel | ISNE | 5.05 | 4.49 | -1.49 | -3.18 | 0.64 | -25.75 | 0.12 | 0.17 | 752 | 13392.81 |
| additive_sentinel | MISO | 3.04 | 2.50 | -0.43 | -1.90 | 2.24 | -15.42 | 0.44 | 0.06 | 746 | 73788.38 |
| additive_sentinel | NYIS | 3.55 | 2.92 | -0.74 | -2.44 | 0.77 | -26.04 | 0.39 | 0.61 | 752 | 17400.75 |
| additive_sentinel | PJM | 3.87 | 3.21 | 0.18 | -2.10 | 2.10 | -16.81 | 0.57 | 0.53 | 744 | 91927.69 |
| additive_sentinel | SWPP | 3.64 | 2.86 | 0.07 | -1.96 | 1.64 | -20.17 | 0.54 | 0.08 | 741 | 31300.49 |
| additive_sentinel | TVA | 4.13 | 3.50 | -0.36 | -2.26 | 1.77 | -16.06 | 0.20 | 0.28 | 739 | 18562.62 |
| additive_separate | BPAT | 3.22 | 2.78 | -0.45 | -1.87 | 2.02 | -18.01 | 0.26 | 0.24 | 750 | 6533.15 |
| additive_separate | CISO | 4.59 | 4.02 | -0.09 | -2.75 | 0.64 | -26.35 | 0.27 | 0.26 | 737 | 25196.91 |
| additive_separate | DUK | 4.06 | 3.53 | -0.34 | -2.32 | 1.48 | -17.12 | 0.28 | 0.30 | 750 | 12129.97 |
| additive_separate | ERCO | 3.64 | 3.10 | -1.45 | -2.81 | 1.19 | -19.26 | 0.29 | 0.20 | 746 | 46782.53 |
| additive_separate | ISNE | 5.05 | 4.49 | -1.48 | -3.18 | 0.64 | -25.75 | 0.12 | 0.17 | 752 | 13392.81 |
| additive_separate | MISO | 3.04 | 2.50 | -0.42 | -1.90 | 2.24 | -15.42 | 0.44 | 0.06 | 746 | 73788.38 |
| additive_separate | NYIS | 3.55 | 2.93 | -0.72 | -2.43 | 0.77 | -25.84 | 0.39 | 0.61 | 752 | 17400.75 |
| additive_separate | PJM | 3.90 | 3.22 | 0.06 | -2.15 | 2.08 | -17.44 | 0.57 | 0.52 | 744 | 91927.69 |
| additive_separate | SWPP | 3.64 | 2.80 | -0.06 | -2.05 | 1.62 | -21.66 | 0.54 | 0.07 | 741 | 31300.49 |
| additive_separate | TVA | 4.13 | 3.53 | -0.36 | -2.27 | 1.77 | -16.13 | 0.20 | 0.28 | 739 | 18562.62 |
| additive_special | BPAT | 3.22 | 2.78 | -0.45 | -1.85 | 2.05 | -18.01 | 0.26 | 0.25 | 750 | 6533.15 |
| additive_special | CISO | 4.61 | 4.04 | -0.02 | -2.73 | 0.64 | -26.30 | 0.26 | 0.26 | 737 | 25196.91 |
| additive_special | DUK | 4.05 | 3.54 | -0.34 | -2.33 | 1.51 | -17.12 | 0.28 | 0.29 | 750 | 12129.97 |
| additive_special | ERCO | 3.65 | 3.11 | -1.44 | -2.81 | 1.22 | -19.26 | 0.30 | 0.20 | 746 | 46782.53 |
| additive_special | ISNE | 5.04 | 4.38 | -1.46 | -3.16 | 0.63 | -25.39 | 0.12 | 0.18 | 752 | 13392.81 |
| additive_special | MISO | 3.02 | 2.54 | -0.42 | -1.90 | 2.22 | -17.01 | 0.44 | 0.06 | 746 | 73788.38 |
| additive_special | NYIS | 3.54 | 2.90 | -0.70 | -2.42 | 0.76 | -25.64 | 0.40 | 0.61 | 752 | 17400.75 |
| additive_special | PJM | 3.91 | 3.25 | 0.07 | -2.16 | 2.08 | -17.44 | 0.56 | 0.52 | 744 | 91927.69 |
| additive_special | SWPP | 3.65 | 2.81 | -0.08 | -2.07 | 1.65 | -21.64 | 0.54 | 0.07 | 741 | 31300.49 |
| additive_special | TVA | 4.12 | 3.54 | -0.39 | -2.27 | 1.77 | -16.07 | 0.19 | 0.29 | 739 | 18562.62 |
| boosting | BPAT | 3.27 | 2.88 | -0.69 | -2.06 | 2.02 | -18.03 | 0.23 | 0.24 | 750 | 6533.15 |
| boosting | CISO | 4.16 | 3.22 | -0.51 | -2.46 | 0.62 | -25.39 | 0.31 | 0.28 | 737 | 25196.91 |
| boosting | DUK | 4.28 | 3.76 | -0.33 | -2.47 | 1.67 | -16.67 | 0.24 | 0.28 | 750 | 12129.97 |
| boosting | ERCO | 3.88 | 3.17 | -2.05 | -3.31 | 1.55 | -19.56 | 0.27 | 0.21 | 746 | 46782.53 |
| boosting | ISNE | 5.00 | 4.38 | -1.48 | -2.86 | 0.63 | -23.51 | 0.14 | 0.17 | 752 | 13392.81 |
| boosting | MISO | 3.34 | 2.70 | -0.93 | -2.37 | 2.21 | -19.49 | 0.39 | 0.05 | 746 | 73788.38 |
| boosting | NYIS | 3.74 | 2.95 | -1.03 | -2.46 | 0.81 | -28.98 | 0.39 | 0.62 | 752 | 17400.75 |
| boosting | PJM | 4.23 | 3.51 | -0.71 | -2.57 | 2.21 | -20.32 | 0.50 | 0.47 | 744 | 91927.69 |
| boosting | SWPP | 3.72 | 2.79 | -1.14 | -2.63 | 1.79 | -27.57 | 0.55 | 0.07 | 741 | 31300.49 |
| boosting | TVA | 4.02 | 3.42 | -0.83 | -2.47 | 1.89 | -16.48 | 0.17 | 0.26 | 739 | 18562.62 |
| boosting_cluster | BPAT | 3.78 | 3.24 | -0.92 | -2.47 | 2.35 | -21.38 | 0.19 | 0.22 | 750 | 6533.15 |
| boosting_cluster | CISO | 5.60 | 4.35 | -3.48 | -4.86 | 0.59 | -33.73 | 0.19 | 0.21 | 737 | 25196.91 |
| boosting_cluster | DUK | 5.21 | 4.50 | -0.67 | -3.14 | 1.82 | -17.47 | 0.16 | 0.25 | 750 | 12129.97 |
| boosting_cluster | ERCO | 4.30 | 3.52 | -1.95 | -3.48 | 1.60 | -24.76 | 0.21 | 0.19 | 746 | 46782.53 |
| boosting_cluster | ISNE | 5.78 | 5.08 | -0.98 | -2.85 | 0.67 | -24.61 | 0.09 | 0.20 | 752 | 13392.81 |
| boosting_cluster | MISO | 4.21 | 3.30 | -0.65 | -2.64 | 2.56 | -18.69 | 0.32 | 0.06 | 746 | 73788.38 |
| boosting_cluster | NYIS | 4.01 | 3.26 | -0.47 | -2.21 | 0.81 | -31.53 | 0.35 | 0.64 | 752 | 17400.75 |
| boosting_cluster | PJM | 5.10 | 4.09 | -1.13 | -3.33 | 2.55 | -25.66 | 0.43 | 0.42 | 744 | 91927.69 |
| boosting_cluster | SWPP | 4.50 | 3.42 | -0.19 | -2.49 | 1.88 | -20.63 | 0.46 | 0.08 | 741 | 31300.49 |
| boosting_cluster | TVA | 4.80 | 4.16 | -1.11 | -3.02 | 1.99 | -21.04 | 0.13 | 0.24 | 739 | 18562.62 |
| boosting_long | BPAT | 3.10 | 2.78 | -0.52 | -1.89 | 2.05 | -17.75 | 0.24 | 0.24 | 750 | 6533.15 |
| boosting_long | CISO | 3.97 | 3.29 | -0.19 | -2.14 | 0.58 | -24.19 | 0.36 | 0.30 | 737 | 25196.91 |
| boosting_long | DUK | 4.05 | 3.57 | -0.25 | -2.33 | 1.61 | -17.83 | 0.26 | 0.29 | 750 | 12129.97 |
| boosting_long | ERCO | 3.68 | 3.09 | -2.16 | -3.28 | 1.41 | -20.99 | 0.29 | 0.20 | 746 | 46782.53 |
| boosting_long | ISNE | 4.75 | 4.12 | -1.55 | -2.80 | 0.64 | -24.69 | 0.16 | 0.16 | 752 | 13392.81 |
| boosting_long | MISO | 3.12 | 2.55 | -0.87 | -2.23 | 1.99 | -16.72 | 0.42 | 0.05 | 746 | 73788.38 |
| boosting_long | NYIS | 3.58 | 2.90 | -1.16 | -2.48 | 0.84 | -27.80 | 0.41 | 0.61 | 752 | 17400.75 |
| boosting_long | PJM | 4.02 | 3.37 | -0.36 | -2.32 | 2.20 | -18.28 | 0.52 | 0.50 | 744 | 91927.69 |
| boosting_long | SWPP | 3.46 | 2.65 | -1.14 | -2.48 | 1.73 | -23.76 | 0.58 | 0.06 | 741 | 31300.49 |
| boosting_long | TVA | 3.83 | 3.29 | -0.73 | -2.33 | 1.76 | -18.42 | 0.19 | 0.26 | 739 | 18562.62 |
| boosting_nospecial | BPAT | 3.27 | 2.92 | -0.69 | -2.07 | 2.08 | -18.81 | 0.24 | 0.24 | 750 | 6533.15 |
| boosting_nospecial | CISO | 4.17 | 3.28 | -0.60 | -2.50 | 0.59 | -26.37 | 0.32 | 0.28 | 737 | 25196.91 |
| boosting_nospecial | DUK | 4.30 | 3.79 | -0.35 | -2.50 | 1.80 | -17.07 | 0.25 | 0.28 | 750 | 12129.97 |
| boosting_nospecial | ERCO | 3.87 | 3.16 | -1.99 | -3.27 | 1.52 | -19.57 | 0.27 | 0.21 | 746 | 46782.53 |
| boosting_nospecial | ISNE | 5.00 | 4.37 | -1.49 | -2.88 | 0.59 | -22.92 | 0.14 | 0.17 | 752 | 13392.81 |
| boosting_nospecial | MISO | 3.38 | 2.76 | -0.96 | -2.40 | 2.16 | -19.86 | 0.40 | 0.05 | 746 | 73788.38 |
| boosting_nospecial | NYIS | 3.74 | 2.93 | -1.05 | -2.49 | 0.86 | -29.93 | 0.39 | 0.62 | 752 | 17400.75 |
| boosting_nospecial | PJM | 4.21 | 3.55 | -0.70 | -2.56 | 2.28 | -19.95 | 0.50 | 0.47 | 744 | 91927.69 |
| boosting_nospecial | SWPP | 3.73 | 2.74 | -1.11 | -2.61 | 1.88 | -27.84 | 0.55 | 0.07 | 741 | 31300.49 |
| boosting_nospecial | TVA | 4.01 | 3.40 | -0.82 | -2.47 | 1.85 | -17.62 | 0.17 | 0.26 | 739 | 18562.62 |
| boosting_sentinel | BPAT | 3.24 | 2.84 | -0.68 | -2.04 | 1.96 | -17.49 | 0.23 | 0.23 | 750 | 6533.15 |
| boosting_sentinel | CISO | 4.17 | 3.27 | -0.64 | -2.54 | 0.60 | -27.70 | 0.31 | 0.27 | 737 | 25196.91 |
| boosting_sentinel | DUK | 4.30 | 3.76 | -0.31 | -2.47 | 1.79 | -18.59 | 0.24 | 0.29 | 750 | 12129.97 |
| boosting_sentinel | ERCO | 3.88 | 3.17 | -2.03 | -3.30 | 1.48 | -19.49 | 0.26 | 0.21 | 746 | 46782.53 |
| boosting_sentinel | ISNE | 5.03 | 4.35 | -1.51 | -2.91 | 0.63 | -22.84 | 0.13 | 0.18 | 752 | 13392.81 |
| boosting_sentinel | MISO | 3.35 | 2.69 | -0.93 | -2.37 | 2.21 | -19.32 | 0.40 | 0.05 | 746 | 73788.38 |
| boosting_sentinel | NYIS | 3.73 | 3.02 | -1.08 | -2.48 | 0.84 | -30.61 | 0.38 | 0.62 | 752 | 17400.75 |
| boosting_sentinel | PJM | 4.15 | 3.48 | -0.58 | -2.46 | 2.14 | -21.49 | 0.52 | 0.49 | 744 | 91927.69 |
| boosting_sentinel | SWPP | 3.66 | 2.74 | -0.73 | -2.36 | 1.68 | -18.73 | 0.56 | 0.07 | 741 | 31300.49 |
| boosting_sentinel | TVA | 4.03 | 3.41 | -0.78 | -2.41 | 1.79 | -17.12 | 0.18 | 0.26 | 739 | 18562.62 |
| last_known_day | BPAT | 5.26 | 4.53 | -0.78 | -3.31 | 2.51 | -27.64 | 0.11 | 0.22 | 750 | 6533.15 |
| last_known_day | CISO | 6.99 | 6.67 | 0.07 | -3.46 | 0.62 | -33.31 | 0.19 | 0.26 | 737 | 25196.91 |
| last_known_day | DUK | 9.21 | 8.24 | -1.61 | -5.91 | 2.57 | -39.52 | 0.09 | 0.25 | 750 | 12129.97 |
| last_known_day | ERCO | 6.79 | 5.34 | -1.59 | -4.58 | 2.30 | -38.07 | 0.11 | 0.18 | 746 | 46782.53 |
| last_known_day | ISNE | 8.69 | 7.30 | -0.16 | -4.35 | 0.79 | -44.26 | 0.05 | 0.19 | 752 | 13392.81 |
| last_known_day | MISO | 5.95 | 4.99 | -0.83 | -3.63 | 3.08 | -24.61 | 0.21 | 0.07 | 746 | 73788.38 |
| last_known_day | NYIS | 7.19 | 5.86 | -0.29 | -4.13 | 1.16 | -37.87 | 0.14 | 0.51 | 752 | 17400.75 |
| last_known_day | PJM | 7.31 | 6.06 | -0.85 | -4.46 | 3.20 | -33.75 | 0.25 | 0.42 | 744 | 91927.69 |
| last_known_day | SWPP | 6.08 | 4.89 | -1.09 | -3.91 | 2.70 | -28.08 | 0.32 | 0.07 | 741 | 31300.49 |
| last_known_day | TVA | 8.60 | 7.33 | -1.46 | -5.40 | 2.74 | -36.52 | 0.04 | 0.27 | 739 | 18562.62 |
| profile | BPAT | 5.78 | 4.50 | -1.71 | -3.83 | 2.36 | -30.43 | 0.13 | 0.21 | 750 | 6533.15 |
| profile | CISO | 5.54 | 4.37 | -0.44 | -3.01 | 0.54 | -27.55 | 0.20 | 0.24 | 737 | 25196.91 |
| profile | DUK | 8.60 | 6.76 | -1.99 | -5.57 | 2.30 | -37.55 | 0.11 | 0.21 | 750 | 12129.97 |
| profile | ERCO | 7.58 | 5.84 | -2.50 | -5.32 | 2.14 | -41.15 | 0.11 | 0.19 | 746 | 46782.53 |
| profile | ISNE | 7.93 | 6.34 | -1.33 | -4.28 | 0.54 | -36.25 | 0.07 | 0.15 | 752 | 13392.81 |
| profile | MISO | 5.57 | 4.29 | -0.88 | -3.35 | 2.41 | -24.75 | 0.25 | 0.06 | 746 | 73788.38 |
| profile | NYIS | 6.18 | 4.75 | -0.87 | -3.58 | 0.61 | -36.24 | 0.22 | 0.54 | 752 | 17400.75 |
| profile | PJM | 7.30 | 5.65 | -1.77 | -4.79 | 2.70 | -33.55 | 0.27 | 0.38 | 744 | 91927.69 |
| profile | SWPP | 6.67 | 4.66 | -1.06 | -4.01 | 2.10 | -28.84 | 0.35 | 0.07 | 741 | 31300.49 |
| profile | TVA | 9.29 | 7.38 | -2.21 | -6.02 | 2.83 | -44.25 | 0.05 | 0.23 | 739 | 18562.62 |
| recency_regression | BPAT | 3.80 | 3.27 | -0.70 | -2.22 | 2.06 | -18.62 | 0.20 | 0.25 | 750 | 6533.15 |
| recency_regression | CISO | 5.72 | 4.92 | -1.51 | -3.18 | 0.84 | -24.61 | 0.14 | 0.24 | 737 | 25196.91 |
| recency_regression | DUK | 4.58 | 4.16 | -0.04 | -2.43 | 1.72 | -20.27 | 0.21 | 0.29 | 750 | 12129.97 |
| recency_regression | ERCO | 4.13 | 3.46 | -1.45 | -3.06 | 1.43 | -24.41 | 0.24 | 0.23 | 746 | 46782.53 |
| recency_regression | ISNE | 5.24 | 4.72 | -0.81 | -2.55 | 0.72 | -20.97 | 0.09 | 0.17 | 752 | 13392.81 |
| recency_regression | MISO | 3.75 | 3.15 | -0.88 | -2.42 | 2.49 | -24.00 | 0.33 | 0.05 | 746 | 73788.38 |
| recency_regression | NYIS | 3.90 | 3.24 | -0.48 | -2.13 | 0.95 | -26.14 | 0.33 | 0.63 | 752 | 17400.75 |
| recency_regression | PJM | 4.36 | 3.75 | 0.15 | -2.21 | 2.19 | -22.47 | 0.46 | 0.50 | 744 | 91927.69 |
| recency_regression | SWPP | 3.81 | 3.00 | -0.36 | -2.25 | 1.65 | -18.84 | 0.49 | 0.08 | 741 | 31300.49 |
| recency_regression | TVA | 4.65 | 4.17 | -0.53 | -2.69 | 1.79 | -19.34 | 0.14 | 0.26 | 739 | 18562.62 |
| recency_regression_sentinel | BPAT | 3.80 | 3.28 | -0.71 | -2.23 | 2.05 | -18.73 | 0.20 | 0.25 | 750 | 6533.15 |
| recency_regression_sentinel | CISO | 5.71 | 4.89 | -1.54 | -3.20 | 0.84 | -24.70 | 0.14 | 0.24 | 737 | 25196.91 |
| recency_regression_sentinel | DUK | 4.58 | 4.16 | -0.04 | -2.42 | 1.72 | -20.27 | 0.21 | 0.29 | 750 | 12129.97 |
| recency_regression_sentinel | ERCO | 4.13 | 3.46 | -1.45 | -3.06 | 1.43 | -24.41 | 0.24 | 0.23 | 746 | 46782.53 |
| recency_regression_sentinel | ISNE | 5.24 | 4.71 | -0.82 | -2.55 | 0.73 | -20.98 | 0.09 | 0.17 | 752 | 13392.81 |
| recency_regression_sentinel | MISO | 3.75 | 3.15 | -0.88 | -2.42 | 2.49 | -23.99 | 0.33 | 0.05 | 746 | 73788.38 |
| recency_regression_sentinel | NYIS | 3.90 | 3.25 | -0.50 | -2.14 | 0.95 | -26.20 | 0.33 | 0.62 | 752 | 17400.75 |
| recency_regression_sentinel | PJM | 4.37 | 3.77 | 0.14 | -2.21 | 2.16 | -22.34 | 0.45 | 0.50 | 744 | 91927.69 |
| recency_regression_sentinel | SWPP | 3.85 | 2.98 | -0.13 | -2.11 | 1.66 | -19.74 | 0.51 | 0.08 | 741 | 31300.49 |
| recency_regression_sentinel | TVA | 4.66 | 4.16 | -0.53 | -2.69 | 1.80 | -19.31 | 0.14 | 0.26 | 739 | 18562.62 |

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
| additive | BPAT | uri | 3.11 | -0.51 | -1.61 | -4.29 | 6 |
| additive | CISO | uri | 2.64 | 1.16 | -0.38 | -1.97 | 6 |
| additive | DUK | uri | 3.80 | -0.99 | -1.71 | -7.28 | 6 |
| additive | ERCO | uri | 8.04 | -9.91 | -9.91 | -10.99 | 2 |
| additive | ISNE | uri | 3.66 | 3.48 | 0.00 | 0.00 | 6 |
| additive | MISO | uri | 5.42 | -3.30 | -4.08 | -7.25 | 5 |
| additive | NYIS | uri | 1.98 | 2.15 | -0.26 | -1.54 | 6 |
| additive | PJM | uri | 2.25 | -0.71 | -1.29 | -3.07 | 6 |
| additive | SWPP | uri | 8.11 | 3.42 | -1.48 | -4.11 | 4 |
| additive | TVA | uri | 4.28 | 1.66 | -1.20 | -7.21 | 6 |
| additive_cluster | BPAT | uri | 3.56 | 0.38 | -0.96 | -3.77 | 6 |
| additive_cluster | CISO | uri | 3.32 | 3.03 | -0.07 | -0.43 | 6 |
| additive_cluster | DUK | uri | 4.70 | -1.24 | -3.04 | -10.46 | 6 |
| additive_cluster | ERCO | uri | 6.45 | -9.10 | -9.10 | -10.52 | 2 |
| additive_cluster | ISNE | uri | 4.09 | 3.80 | 0.00 | 0.00 | 6 |
| additive_cluster | MISO | uri | 4.86 | -3.10 | -3.95 | -8.75 | 5 |
| additive_cluster | NYIS | uri | 2.07 | 2.28 | -0.27 | -1.61 | 6 |
| additive_cluster | PJM | uri | 2.83 | 1.29 | -1.48 | -4.53 | 6 |
| additive_cluster | SWPP | uri | 8.42 | 5.12 | -0.45 | -1.42 | 4 |
| additive_cluster | TVA | uri | 4.23 | 1.35 | -1.28 | -6.28 | 6 |
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
| additive_sentinel | BPAT | uri | 3.11 | -0.50 | -1.60 | -4.36 | 6 |
| additive_sentinel | CISO | uri | 2.61 | 1.11 | -0.40 | -1.92 | 6 |
| additive_sentinel | DUK | uri | 3.80 | -0.99 | -1.71 | -7.28 | 6 |
| additive_sentinel | ERCO | uri | 8.04 | -9.91 | -9.91 | -10.99 | 2 |
| additive_sentinel | ISNE | uri | 3.66 | 3.47 | 0.00 | 0.00 | 6 |
| additive_sentinel | MISO | uri | 5.42 | -3.30 | -4.08 | -7.25 | 5 |
| additive_sentinel | NYIS | uri | 1.98 | 2.15 | -0.26 | -1.54 | 6 |
| additive_sentinel | PJM | uri | 2.10 | 0.31 | -0.44 | -1.62 | 6 |
| additive_sentinel | SWPP | uri | 8.14 | 2.64 | -2.05 | -4.93 | 4 |
| additive_sentinel | TVA | uri | 4.27 | 1.67 | -1.20 | -7.20 | 6 |
| additive_separate | BPAT | uri | 3.11 | -0.51 | -1.61 | -4.29 | 6 |
| additive_separate | CISO | uri | 2.64 | 1.16 | -0.38 | -1.97 | 6 |
| additive_separate | DUK | uri | 3.80 | -0.99 | -1.71 | -7.28 | 6 |
| additive_separate | ERCO | uri | 8.04 | -9.91 | -9.91 | -10.99 | 2 |
| additive_separate | ISNE | uri | 3.66 | 3.48 | 0.00 | 0.00 | 6 |
| additive_separate | MISO | uri | 5.42 | -3.30 | -4.08 | -7.25 | 5 |
| additive_separate | NYIS | uri | 1.98 | 2.15 | -0.26 | -1.54 | 6 |
| additive_separate | PJM | uri | 2.25 | -0.71 | -1.29 | -3.07 | 6 |
| additive_separate | SWPP | uri | 8.11 | 3.42 | -1.48 | -4.11 | 4 |
| additive_separate | TVA | uri | 4.28 | 1.66 | -1.20 | -7.21 | 6 |
| additive_special | BPAT | uri | 3.12 | -0.48 | -1.59 | -4.22 | 6 |
| additive_special | CISO | uri | 2.66 | 1.31 | -0.34 | -1.83 | 6 |
| additive_special | DUK | uri | 3.82 | -0.95 | -1.67 | -7.25 | 6 |
| additive_special | ERCO | uri | 8.02 | -9.90 | -9.90 | -10.99 | 2 |
| additive_special | ISNE | uri | 3.69 | 3.48 | 0.00 | 0.00 | 6 |
| additive_special | MISO | uri | 5.16 | -2.52 | -3.38 | -5.67 | 5 |
| additive_special | NYIS | uri | 1.99 | 2.16 | -0.25 | -1.52 | 6 |
| additive_special | PJM | uri | 2.23 | -0.64 | -1.24 | -3.06 | 6 |
| additive_special | SWPP | uri | 8.11 | 3.40 | -1.50 | -4.14 | 4 |
| additive_special | TVA | uri | 4.41 | 2.51 | -0.48 | -2.87 | 6 |
| boosting | BPAT | uri | 3.38 | -1.04 | -2.27 | -5.76 | 6 |
| boosting | CISO | uri | 2.35 | 0.16 | -0.58 | -1.86 | 6 |
| boosting | DUK | uri | 4.22 | -2.85 | -2.85 | -5.36 | 6 |
| boosting | ERCO | uri | 12.44 | -17.12 | -17.12 | -19.11 | 2 |
| boosting | ISNE | uri | 4.00 | 0.52 | -0.70 | -2.94 | 6 |
| boosting | MISO | uri | 7.04 | -8.34 | -8.34 | -13.40 | 5 |
| boosting | NYIS | uri | 2.24 | 0.08 | -0.99 | -3.67 | 6 |
| boosting | PJM | uri | 2.74 | -3.07 | -3.07 | -4.08 | 6 |
| boosting | SWPP | uri | 8.47 | -2.38 | -4.79 | -11.00 | 4 |
| boosting | TVA | uri | 4.64 | -4.72 | -5.19 | -8.25 | 6 |
| boosting_cluster | BPAT | uri | 3.70 | -0.09 | -1.29 | -4.90 | 6 |
| boosting_cluster | CISO | uri | 2.40 | 0.83 | -0.26 | -1.46 | 6 |
| boosting_cluster | DUK | uri | 5.22 | -3.36 | -4.09 | -7.87 | 6 |
| boosting_cluster | ERCO | uri | 9.74 | -14.33 | -14.33 | -15.64 | 2 |
| boosting_cluster | ISNE | uri | 4.52 | 0.43 | -1.15 | -4.74 | 6 |
| boosting_cluster | MISO | uri | 6.68 | -8.14 | -8.34 | -12.64 | 5 |
| boosting_cluster | NYIS | uri | 2.54 | 0.22 | -0.99 | -4.71 | 6 |
| boosting_cluster | PJM | uri | 3.30 | -3.53 | -3.95 | -7.20 | 6 |
| boosting_cluster | SWPP | uri | 6.44 | -0.28 | -2.60 | -7.06 | 4 |
| boosting_cluster | TVA | uri | 3.34 | -2.42 | -3.03 | -6.79 | 6 |
| boosting_long | BPAT | uri | 4.22 | 0.73 | -1.12 | -5.94 | 6 |
| boosting_long | CISO | uri | 2.42 | -1.20 | -1.42 | -4.15 | 6 |
| boosting_long | DUK | uri | 3.84 | -2.36 | -2.36 | -3.60 | 6 |
| boosting_long | ERCO | uri | 11.61 | -17.14 | -17.14 | -17.86 | 2 |
| boosting_long | ISNE | uri | 3.59 | 0.04 | -1.06 | -2.45 | 6 |
| boosting_long | MISO | uri | 6.47 | -7.11 | -7.11 | -12.41 | 5 |
| boosting_long | NYIS | uri | 2.48 | -0.19 | -1.10 | -4.60 | 6 |
| boosting_long | PJM | uri | 2.87 | -3.63 | -3.63 | -4.52 | 6 |
| boosting_long | SWPP | uri | 6.48 | -0.84 | -3.39 | -9.72 | 4 |
| boosting_long | TVA | uri | 4.75 | -1.29 | -2.47 | -6.68 | 6 |
| boosting_nospecial | BPAT | uri | 3.38 | -1.46 | -2.63 | -6.20 | 6 |
| boosting_nospecial | CISO | uri | 2.27 | 0.21 | -0.52 | -1.58 | 6 |
| boosting_nospecial | DUK | uri | 4.27 | -3.16 | -3.16 | -6.28 | 6 |
| boosting_nospecial | ERCO | uri | 13.40 | -18.01 | -18.01 | -19.57 | 2 |
| boosting_nospecial | ISNE | uri | 4.07 | 0.59 | -0.78 | -3.24 | 6 |
| boosting_nospecial | MISO | uri | 6.73 | -7.64 | -7.64 | -11.98 | 5 |
| boosting_nospecial | NYIS | uri | 2.38 | -0.27 | -1.23 | -4.37 | 6 |
| boosting_nospecial | PJM | uri | 2.77 | -2.95 | -2.95 | -4.22 | 6 |
| boosting_nospecial | SWPP | uri | 8.25 | -2.62 | -4.75 | -11.25 | 4 |
| boosting_nospecial | TVA | uri | 4.69 | -4.47 | -5.00 | -7.97 | 6 |
| boosting_sentinel | BPAT | uri | 3.16 | -0.60 | -1.77 | -5.58 | 6 |
| boosting_sentinel | CISO | uri | 2.77 | -1.45 | -1.74 | -3.77 | 6 |
| boosting_sentinel | DUK | uri | 4.34 | -2.66 | -2.66 | -5.51 | 6 |
| boosting_sentinel | ERCO | uri | 13.24 | -17.62 | -17.62 | -19.46 | 2 |
| boosting_sentinel | ISNE | uri | 4.00 | 0.19 | -0.74 | -2.83 | 6 |
| boosting_sentinel | MISO | uri | 6.68 | -8.21 | -8.21 | -12.28 | 5 |
| boosting_sentinel | NYIS | uri | 2.24 | -0.16 | -1.10 | -4.43 | 6 |
| boosting_sentinel | PJM | uri | 2.79 | -3.02 | -3.02 | -4.15 | 6 |
| boosting_sentinel | SWPP | uri | 8.79 | -2.58 | -5.10 | -12.68 | 4 |
| boosting_sentinel | TVA | uri | 5.19 | -4.63 | -5.28 | -8.37 | 6 |
| last_known_day | BPAT | uri | 5.56 | 1.23 | -1.49 | -4.90 | 6 |
| last_known_day | CISO | uri | 6.30 | -0.04 | -2.90 | -8.63 | 6 |
| last_known_day | DUK | uri | 8.80 | -6.01 | -8.05 | -15.89 | 6 |
| last_known_day | ERCO | uri | 3.71 | -8.02 | -8.02 | -9.38 | 2 |
| last_known_day | ISNE | uri | 5.40 | 0.10 | -2.20 | -6.56 | 6 |
| last_known_day | MISO | uri | 4.42 | -0.72 | -2.17 | -8.13 | 5 |
| last_known_day | NYIS | uri | 4.15 | 0.12 | -2.12 | -5.89 | 6 |
| last_known_day | PJM | uri | 4.16 | -3.17 | -4.91 | -11.49 | 6 |
| last_known_day | SWPP | uri | 6.51 | 0.17 | -0.92 | -3.69 | 4 |
| last_known_day | TVA | uri | 8.03 | -1.72 | -4.70 | -9.64 | 6 |
| profile | BPAT | uri | 9.21 | -5.26 | -7.00 | -21.28 | 6 |
| profile | CISO | uri | 2.76 | 0.39 | -0.79 | -2.24 | 6 |
| profile | DUK | uri | 11.34 | -12.81 | -12.81 | -21.53 | 6 |
| profile | ERCO | uri | 37.38 | -38.02 | -38.02 | -41.15 | 2 |
| profile | ISNE | uri | 5.94 | 3.16 | -0.80 | -4.80 | 6 |
| profile | MISO | uri | 11.57 | -9.74 | -10.54 | -21.58 | 5 |
| profile | NYIS | uri | 3.72 | 2.13 | -0.73 | -2.87 | 6 |
| profile | PJM | uri | 3.41 | -2.51 | -2.99 | -6.23 | 6 |
| profile | SWPP | uri | 17.18 | -6.75 | -11.94 | -27.71 | 4 |
| profile | TVA | uri | 16.63 | -17.66 | -17.72 | -27.35 | 6 |
| recency_regression | BPAT | uri | 3.29 | -0.43 | -1.94 | -8.29 | 6 |
| recency_regression | CISO | uri | 3.90 | -1.40 | -1.59 | -2.98 | 6 |
| recency_regression | DUK | uri | 3.90 | -2.84 | -2.84 | -6.00 | 6 |
| recency_regression | ERCO | uri | 8.42 | -8.70 | -8.70 | -15.68 | 2 |
| recency_regression | ISNE | uri | 2.87 | 0.46 | -0.47 | -1.82 | 6 |
| recency_regression | MISO | uri | 9.57 | -8.37 | -8.37 | -12.59 | 5 |
| recency_regression | NYIS | uri | 3.00 | 0.01 | -0.53 | -2.78 | 6 |
| recency_regression | PJM | uri | 5.32 | -3.87 | -3.87 | -4.74 | 6 |
| recency_regression | SWPP | uri | 8.37 | -5.92 | -7.38 | -18.84 | 4 |
| recency_regression | TVA | uri | 5.36 | -1.90 | -3.22 | -6.55 | 6 |
| recency_regression_sentinel | BPAT | uri | 3.30 | -0.43 | -1.96 | -8.40 | 6 |
| recency_regression_sentinel | CISO | uri | 3.89 | -1.41 | -1.59 | -3.03 | 6 |
| recency_regression_sentinel | DUK | uri | 3.90 | -2.84 | -2.84 | -6.00 | 6 |
| recency_regression_sentinel | ERCO | uri | 8.42 | -8.70 | -8.70 | -15.68 | 2 |
| recency_regression_sentinel | ISNE | uri | 2.87 | 0.46 | -0.47 | -1.82 | 6 |
| recency_regression_sentinel | MISO | uri | 9.57 | -8.36 | -8.36 | -12.59 | 5 |
| recency_regression_sentinel | NYIS | uri | 3.01 | 0.01 | -0.53 | -2.78 | 6 |
| recency_regression_sentinel | PJM | uri | 5.25 | -3.69 | -3.69 | -4.83 | 6 |
| recency_regression_sentinel | SWPP | uri | 8.49 | -6.33 | -7.75 | -19.74 | 4 |
| recency_regression_sentinel | TVA | uri | 5.36 | -1.90 | -3.23 | -6.56 | 6 |
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
| additive | BPAT | elliott | 5.63 | -0.71 | -2.51 | -6.85 | 5 |
| additive | CISO | elliott | 4.41 | 2.19 | -1.10 | -5.50 | 5 |
| additive | DUK | elliott | 7.47 | -2.76 | -3.87 | -7.41 | 4 |
| additive | ERCO | elliott | 10.25 | -8.91 | -9.41 | -19.26 | 5 |
| additive | ISNE | elliott | 4.99 | 5.77 | 0.00 | 0.00 | 5 |
| additive | MISO | elliott | 6.69 | -1.95 | -2.78 | -6.29 | 5 |
| additive | NYIS | elliott | 4.22 | 0.69 | -1.48 | -7.38 | 5 |
| additive | PJM | elliott | 6.44 | -5.40 | -6.39 | -13.76 | 5 |
| additive | SWPP | elliott | 4.53 | -5.25 | -5.25 | -10.26 | 5 |
| additive | TVA | elliott | 5.85 | -3.53 | -3.99 | -8.09 | 3 |
| additive_cluster | BPAT | elliott | 7.91 | 0.07 | -2.97 | -11.41 | 5 |
| additive_cluster | CISO | elliott | 6.04 | 7.76 | 0.00 | 0.00 | 5 |
| additive_cluster | DUK | elliott | 6.50 | -6.81 | -7.59 | -13.53 | 4 |
| additive_cluster | ERCO | elliott | 11.23 | -4.80 | -6.02 | -20.46 | 5 |
| additive_cluster | ISNE | elliott | 4.77 | 6.93 | 0.00 | 0.00 | 5 |
| additive_cluster | MISO | elliott | 11.46 | -2.48 | -6.21 | -17.72 | 5 |
| additive_cluster | NYIS | elliott | 4.74 | 1.97 | -0.90 | -4.34 | 5 |
| additive_cluster | PJM | elliott | 8.83 | -8.15 | -9.17 | -25.64 | 5 |
| additive_cluster | SWPP | elliott | 4.68 | -3.27 | -3.49 | -7.27 | 5 |
| additive_cluster | TVA | elliott | 5.69 | -1.08 | -2.33 | -5.40 | 3 |
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
| additive_sentinel | BPAT | elliott | 5.63 | -0.71 | -2.51 | -6.85 | 5 |
| additive_sentinel | CISO | elliott | 4.41 | 2.33 | -1.03 | -5.15 | 5 |
| additive_sentinel | DUK | elliott | 7.47 | -2.76 | -3.87 | -7.41 | 4 |
| additive_sentinel | ERCO | elliott | 10.25 | -8.91 | -9.41 | -19.26 | 5 |
| additive_sentinel | ISNE | elliott | 4.99 | 5.77 | 0.00 | 0.00 | 5 |
| additive_sentinel | MISO | elliott | 6.69 | -1.95 | -2.78 | -6.29 | 5 |
| additive_sentinel | NYIS | elliott | 4.22 | 0.70 | -1.47 | -7.34 | 5 |
| additive_sentinel | PJM | elliott | 6.44 | -5.40 | -6.39 | -13.76 | 5 |
| additive_sentinel | SWPP | elliott | 4.53 | -5.28 | -5.28 | -9.98 | 5 |
| additive_sentinel | TVA | elliott | 5.85 | -3.63 | -4.09 | -8.40 | 3 |
| additive_separate | BPAT | elliott | 5.63 | -0.71 | -2.51 | -6.85 | 5 |
| additive_separate | CISO | elliott | 4.41 | 2.19 | -1.10 | -5.50 | 5 |
| additive_separate | DUK | elliott | 7.47 | -2.76 | -3.87 | -7.41 | 4 |
| additive_separate | ERCO | elliott | 10.25 | -8.91 | -9.41 | -19.26 | 5 |
| additive_separate | ISNE | elliott | 4.99 | 5.77 | 0.00 | 0.00 | 5 |
| additive_separate | MISO | elliott | 6.69 | -1.95 | -2.78 | -6.29 | 5 |
| additive_separate | NYIS | elliott | 4.22 | 0.69 | -1.48 | -7.38 | 5 |
| additive_separate | PJM | elliott | 6.44 | -5.40 | -6.39 | -13.76 | 5 |
| additive_separate | SWPP | elliott | 4.53 | -5.25 | -5.25 | -10.26 | 5 |
| additive_separate | TVA | elliott | 5.85 | -3.53 | -3.99 | -8.09 | 3 |
| additive_special | BPAT | elliott | 5.32 | -0.99 | -2.39 | -6.85 | 5 |
| additive_special | CISO | elliott | 4.27 | -0.02 | -2.17 | -9.09 | 5 |
| additive_special | DUK | elliott | 7.03 | -3.35 | -4.93 | -10.39 | 4 |
| additive_special | ERCO | elliott | 9.93 | -8.11 | -8.89 | -19.26 | 5 |
| additive_special | ISNE | elliott | 6.70 | 6.42 | 0.00 | 0.00 | 5 |
| additive_special | MISO | elliott | 5.50 | -0.97 | -3.49 | -7.04 | 5 |
| additive_special | NYIS | elliott | 4.65 | 1.59 | -1.49 | -7.43 | 5 |
| additive_special | PJM | elliott | 6.48 | -6.18 | -6.81 | -13.78 | 5 |
| additive_special | SWPP | elliott | 4.57 | -5.56 | -5.56 | -10.26 | 5 |
| additive_special | TVA | elliott | 5.41 | -5.12 | -5.12 | -7.88 | 3 |
| boosting | BPAT | elliott | 5.89 | -1.69 | -3.79 | -7.94 | 5 |
| boosting | CISO | elliott | 3.24 | 0.72 | -1.16 | -3.31 | 5 |
| boosting | DUK | elliott | 6.78 | -7.27 | -7.98 | -14.21 | 4 |
| boosting | ERCO | elliott | 8.85 | -8.14 | -8.63 | -18.42 | 5 |
| boosting | ISNE | elliott | 4.83 | 5.06 | 0.00 | 0.00 | 5 |
| boosting | MISO | elliott | 6.81 | -2.54 | -4.50 | -8.73 | 5 |
| boosting | NYIS | elliott | 3.72 | 0.17 | -1.14 | -3.51 | 5 |
| boosting | PJM | elliott | 6.28 | -8.65 | -8.65 | -17.21 | 5 |
| boosting | SWPP | elliott | 4.59 | -4.60 | -5.27 | -14.87 | 5 |
| boosting | TVA | elliott | 5.73 | 0.02 | -1.22 | -3.02 | 3 |
| boosting_cluster | BPAT | elliott | 6.45 | -2.19 | -4.55 | -9.98 | 5 |
| boosting_cluster | CISO | elliott | 3.05 | 0.37 | -0.77 | -1.81 | 5 |
| boosting_cluster | DUK | elliott | 6.40 | -9.79 | -9.79 | -15.02 | 4 |
| boosting_cluster | ERCO | elliott | 8.63 | -9.67 | -9.67 | -18.39 | 5 |
| boosting_cluster | ISNE | elliott | 3.03 | 3.47 | 0.00 | 0.00 | 5 |
| boosting_cluster | MISO | elliott | 7.63 | -3.08 | -4.54 | -8.61 | 5 |
| boosting_cluster | NYIS | elliott | 3.97 | -0.57 | -1.60 | -4.22 | 5 |
| boosting_cluster | PJM | elliott | 8.24 | -9.71 | -10.14 | -19.56 | 5 |
| boosting_cluster | SWPP | elliott | 5.10 | -2.81 | -4.20 | -14.89 | 5 |
| boosting_cluster | TVA | elliott | 5.92 | -1.52 | -2.03 | -6.09 | 3 |
| boosting_long | BPAT | elliott | 5.98 | -1.28 | -3.28 | -7.12 | 5 |
| boosting_long | CISO | elliott | 4.08 | 2.06 | -0.49 | -2.43 | 5 |
| boosting_long | DUK | elliott | 5.63 | -2.85 | -3.25 | -7.64 | 4 |
| boosting_long | ERCO | elliott | 5.99 | -6.47 | -6.77 | -13.98 | 5 |
| boosting_long | ISNE | elliott | 3.12 | 2.75 | -0.22 | -1.09 | 5 |
| boosting_long | MISO | elliott | 4.89 | -1.41 | -2.73 | -4.69 | 5 |
| boosting_long | NYIS | elliott | 3.49 | 0.81 | -0.58 | -1.83 | 5 |
| boosting_long | PJM | elliott | 6.02 | -4.79 | -5.24 | -10.58 | 5 |
| boosting_long | SWPP | elliott | 5.22 | -5.38 | -5.64 | -14.19 | 5 |
| boosting_long | TVA | elliott | 6.31 | 1.58 | -0.24 | -0.72 | 3 |
| boosting_nospecial | BPAT | elliott | 5.95 | -1.81 | -4.01 | -8.74 | 5 |
| boosting_nospecial | CISO | elliott | 3.83 | 1.37 | -0.69 | -2.11 | 5 |
| boosting_nospecial | DUK | elliott | 6.74 | -7.01 | -7.64 | -13.56 | 4 |
| boosting_nospecial | ERCO | elliott | 8.56 | -8.16 | -8.58 | -18.08 | 5 |
| boosting_nospecial | ISNE | elliott | 4.86 | 6.23 | 0.00 | 0.00 | 5 |
| boosting_nospecial | MISO | elliott | 6.94 | -1.67 | -3.95 | -7.91 | 5 |
| boosting_nospecial | NYIS | elliott | 3.90 | 1.06 | -0.87 | -2.28 | 5 |
| boosting_nospecial | PJM | elliott | 6.45 | -8.95 | -8.95 | -17.06 | 5 |
| boosting_nospecial | SWPP | elliott | 4.65 | -4.66 | -5.41 | -15.11 | 5 |
| boosting_nospecial | TVA | elliott | 5.93 | -0.07 | -1.09 | -3.28 | 3 |
| boosting_sentinel | BPAT | elliott | 5.89 | -1.69 | -3.79 | -7.94 | 5 |
| boosting_sentinel | CISO | elliott | 3.34 | 0.70 | -1.18 | -3.76 | 5 |
| boosting_sentinel | DUK | elliott | 6.84 | -7.28 | -8.11 | -14.18 | 4 |
| boosting_sentinel | ERCO | elliott | 8.76 | -7.78 | -8.74 | -19.49 | 5 |
| boosting_sentinel | ISNE | elliott | 4.23 | 4.54 | 0.00 | 0.00 | 5 |
| boosting_sentinel | MISO | elliott | 6.96 | -2.14 | -4.39 | -8.42 | 5 |
| boosting_sentinel | NYIS | elliott | 3.83 | 0.54 | -1.02 | -2.69 | 5 |
| boosting_sentinel | PJM | elliott | 6.14 | -8.48 | -8.48 | -16.70 | 5 |
| boosting_sentinel | SWPP | elliott | 4.66 | -4.48 | -5.25 | -15.37 | 5 |
| boosting_sentinel | TVA | elliott | 5.80 | -0.98 | -1.73 | -4.11 | 3 |
| last_known_day | BPAT | elliott | 16.65 | 9.54 | -3.69 | -12.35 | 5 |
| last_known_day | CISO | elliott | 7.28 | 5.67 | -0.65 | -3.27 | 5 |
| last_known_day | DUK | elliott | 12.98 | -4.91 | -7.71 | -30.82 | 4 |
| last_known_day | ERCO | elliott | 22.52 | -6.55 | -12.98 | -33.14 | 5 |
| last_known_day | ISNE | elliott | 5.75 | 1.27 | -1.62 | -5.04 | 5 |
| last_known_day | MISO | elliott | 10.19 | -2.25 | -6.65 | -15.11 | 5 |
| last_known_day | NYIS | elliott | 5.81 | 0.58 | -2.12 | -6.27 | 5 |
| last_known_day | PJM | elliott | 11.75 | -3.11 | -7.30 | -19.23 | 5 |
| last_known_day | SWPP | elliott | 15.08 | -1.66 | -5.68 | -20.35 | 5 |
| last_known_day | TVA | elliott | 16.30 | -0.58 | -5.25 | -15.74 | 3 |
| profile | BPAT | elliott | 11.57 | -3.84 | -7.72 | -15.77 | 5 |
| profile | CISO | elliott | 6.73 | 6.86 | -0.06 | -0.30 | 5 |
| profile | DUK | elliott | 20.01 | -23.96 | -24.41 | -37.55 | 4 |
| profile | ERCO | elliott | 22.24 | -32.34 | -32.34 | -40.42 | 5 |
| profile | ISNE | elliott | 8.88 | -3.16 | -6.30 | -15.14 | 5 |
| profile | MISO | elliott | 14.08 | -15.53 | -15.53 | -24.75 | 5 |
| profile | NYIS | elliott | 9.18 | -7.26 | -7.84 | -17.00 | 5 |
| profile | PJM | elliott | 16.64 | -17.72 | -18.05 | -33.55 | 5 |
| profile | SWPP | elliott | 15.89 | -19.05 | -19.05 | -25.25 | 5 |
| profile | TVA | elliott | 23.76 | -32.17 | -32.17 | -44.25 | 3 |
| recency_regression | BPAT | elliott | 4.54 | -0.44 | -2.10 | -6.58 | 5 |
| recency_regression | CISO | elliott | 7.39 | 5.61 | 0.00 | 0.00 | 5 |
| recency_regression | DUK | elliott | 4.28 | -2.72 | -3.08 | -6.52 | 4 |
| recency_regression | ERCO | elliott | 10.81 | 5.82 | -5.94 | -14.70 | 5 |
| recency_regression | ISNE | elliott | 4.23 | 6.39 | -0.23 | -1.17 | 5 |
| recency_regression | MISO | elliott | 6.79 | -7.47 | -7.80 | -24.00 | 5 |
| recency_regression | NYIS | elliott | 3.41 | -0.50 | -2.15 | -4.65 | 5 |
| recency_regression | PJM | elliott | 7.05 | -8.07 | -8.11 | -16.86 | 5 |
| recency_regression | SWPP | elliott | 4.46 | -4.82 | -4.82 | -7.33 | 5 |
| recency_regression | TVA | elliott | 4.73 | 4.04 | -1.49 | -3.36 | 3 |
| recency_regression_sentinel | BPAT | elliott | 4.54 | -0.44 | -2.10 | -6.58 | 5 |
| recency_regression_sentinel | CISO | elliott | 7.40 | 5.63 | 0.00 | 0.00 | 5 |
| recency_regression_sentinel | DUK | elliott | 4.28 | -2.72 | -3.08 | -6.52 | 4 |
| recency_regression_sentinel | ERCO | elliott | 10.81 | 5.83 | -5.93 | -14.70 | 5 |
| recency_regression_sentinel | ISNE | elliott | 4.23 | 6.42 | -0.24 | -1.18 | 5 |
| recency_regression_sentinel | MISO | elliott | 6.79 | -7.47 | -7.79 | -23.99 | 5 |
| recency_regression_sentinel | NYIS | elliott | 3.41 | -0.51 | -2.16 | -4.65 | 5 |
| recency_regression_sentinel | PJM | elliott | 7.05 | -8.07 | -8.11 | -16.86 | 5 |
| recency_regression_sentinel | SWPP | elliott | 4.58 | -4.97 | -4.97 | -7.85 | 5 |
| recency_regression_sentinel | TVA | elliott | 4.73 | 4.07 | -1.49 | -3.36 | 3 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 35682 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 35687 | DUK | 2022-12-24 | additive | 10.06 | -18.74 | -18.74 |
| 35689 | DUK | 2022-12-24 | additive_cluster | 13.15 | -24.17 | -24.17 |
| 35680 | DUK | 2022-12-24 | additive_long | 6.42 | -10.46 | -10.46 |
| 35684 | DUK | 2022-12-24 | additive_sentinel | 10.06 | -18.76 | -18.76 |
| 35690 | DUK | 2022-12-24 | additive_separate | 10.06 | -18.74 | -18.74 |
| 35688 | DUK | 2022-12-24 | additive_special | 11.31 | -22.03 | -22.03 |
| 35691 | DUK | 2022-12-24 | boosting | 10.84 | -20.01 | -20.01 |
| 35693 | DUK | 2022-12-24 | boosting_cluster | 14.52 | -23.13 | -23.13 |
| 35681 | DUK | 2022-12-24 | boosting_long | 9.83 | -16.18 | -16.18 |
| 35692 | DUK | 2022-12-24 | boosting_nospecial | 10.79 | -20.26 | -20.26 |
| 35685 | DUK | 2022-12-24 | boosting_sentinel | 10.76 | -20.02 | -20.02 |
| 35694 | DUK | 2022-12-24 | last_known_day | 29.05 | -39.03 | -39.03 |
| 35695 | DUK | 2022-12-24 | profile | 42.59 | -45.59 | -45.59 |
| 35686 | DUK | 2022-12-24 | recency_regression | 10.06 | -9.81 | -9.81 |
| 35683 | DUK | 2022-12-24 | recency_regression_sentinel | 10.06 | -9.78 | -9.78 |
| 36994 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 36999 | ERCO | 2021-02-15 | additive | 23.31 | -16.98 | -16.98 |
| 37001 | ERCO | 2021-02-15 | additive_cluster | 21.98 | -18.89 | -18.89 |
| 36992 | ERCO | 2021-02-15 | additive_long | 41.10 | -1.69 | -1.69 |
| 36996 | ERCO | 2021-02-15 | additive_sentinel | 23.31 | -16.98 | -16.98 |
| 37002 | ERCO | 2021-02-15 | additive_separate | 23.31 | -16.98 | -16.98 |
| 37000 | ERCO | 2021-02-15 | additive_special | 23.58 | -16.93 | -16.93 |
| 37003 | ERCO | 2021-02-15 | boosting | 16.80 | -17.21 | -17.21 |
| 37005 | ERCO | 2021-02-15 | boosting_cluster | 19.13 | -19.11 | -19.11 |
| 36993 | ERCO | 2021-02-15 | boosting_long | 22.14 | -14.57 | -14.57 |
| 37004 | ERCO | 2021-02-15 | boosting_nospecial | 16.54 | -17.64 | -17.64 |
| 36997 | ERCO | 2021-02-15 | boosting_sentinel | 17.42 | -16.97 | -16.97 |
| 37006 | ERCO | 2021-02-15 | last_known_day | 22.77 | -15.91 | -15.91 |
| 37007 | ERCO | 2021-02-15 | profile | 12.39 | -34.83 | -34.83 |
| 36998 | ERCO | 2021-02-15 | recency_regression | 59.63 | 3.38 | 0.00 |
| 36995 | ERCO | 2021-02-15 | recency_regression_sentinel | 59.64 | 3.38 | 0.00 |
| 37010 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 37015 | ERCO | 2021-02-16 | additive | 30.79 | 26.54 | 0.00 |
| 37017 | ERCO | 2021-02-16 | additive_cluster | 29.57 | 26.54 | 0.00 |
| 37008 | ERCO | 2021-02-16 | additive_long | 52.45 | 46.85 | 0.00 |
| 37012 | ERCO | 2021-02-16 | additive_sentinel | 30.79 | 26.54 | 0.00 |
| 37018 | ERCO | 2021-02-16 | additive_separate | 30.79 | 26.54 | 0.00 |
| 37016 | ERCO | 2021-02-16 | additive_special | 31.04 | 26.41 | 0.00 |
| 37019 | ERCO | 2021-02-16 | boosting | 22.33 | 19.90 | 0.00 |
| 37021 | ERCO | 2021-02-16 | boosting_cluster | 23.20 | 16.91 | 0.00 |
| 37009 | ERCO | 2021-02-16 | boosting_long | 28.06 | 26.11 | 0.00 |
| 37020 | ERCO | 2021-02-16 | boosting_nospecial | 21.29 | 18.82 | 0.00 |
| 37013 | ERCO | 2021-02-16 | boosting_sentinel | 22.04 | 18.43 | 0.00 |
| 37022 | ERCO | 2021-02-16 | last_known_day | 37.95 | 9.73 | 0.00 |
| 37023 | ERCO | 2021-02-16 | profile | 10.35 | 12.52 | 0.00 |
| 37014 | ERCO | 2021-02-16 | recency_regression | 81.77 | 86.34 | 0.00 |
| 37011 | ERCO | 2021-02-16 | recency_regression_sentinel | 81.78 | 86.35 | 0.00 |
| 37026 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 37031 | ERCO | 2021-02-17 | additive | 25.55 | 21.54 | 0.00 |
| 37033 | ERCO | 2021-02-17 | additive_cluster | 25.24 | 21.73 | 0.00 |
| 37024 | ERCO | 2021-02-17 | additive_long | 35.15 | 33.44 | 0.00 |
| 37028 | ERCO | 2021-02-17 | additive_sentinel | 25.55 | 21.54 | 0.00 |
| 37034 | ERCO | 2021-02-17 | additive_separate | 25.55 | 21.54 | 0.00 |
| 37032 | ERCO | 2021-02-17 | additive_special | 25.69 | 21.66 | 0.00 |
| 37035 | ERCO | 2021-02-17 | boosting | 17.89 | 11.98 | 0.00 |
| 37037 | ERCO | 2021-02-17 | boosting_cluster | 18.52 | 11.99 | 0.00 |
| 37025 | ERCO | 2021-02-17 | boosting_long | 23.41 | 15.65 | 0.00 |
| 37036 | ERCO | 2021-02-17 | boosting_nospecial | 17.15 | 11.61 | 0.00 |
| 37029 | ERCO | 2021-02-17 | boosting_sentinel | 17.59 | 11.20 | 0.00 |
| 37038 | ERCO | 2021-02-17 | last_known_day | 5.67 | -9.74 | -9.74 |
| 37039 | ERCO | 2021-02-17 | profile | 8.92 | 6.34 | 0.00 |
| 37030 | ERCO | 2021-02-17 | recency_regression | 47.01 | 36.53 | 0.00 |
| 37027 | ERCO | 2021-02-17 | recency_regression_sentinel | 47.01 | 36.53 | 0.00 |
| 37042 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 37047 | ERCO | 2021-02-18 | additive | 7.46 | 5.66 | 0.00 |
| 37049 | ERCO | 2021-02-18 | additive_cluster | 7.64 | 6.52 | 0.00 |
| 37040 | ERCO | 2021-02-18 | additive_long | 8.08 | 5.87 | 0.00 |
| 37044 | ERCO | 2021-02-18 | additive_sentinel | 7.46 | 5.66 | 0.00 |
| 37050 | ERCO | 2021-02-18 | additive_separate | 7.46 | 5.66 | 0.00 |
| 37048 | ERCO | 2021-02-18 | additive_special | 7.45 | 5.64 | 0.00 |
| 37051 | ERCO | 2021-02-18 | boosting | 7.56 | 1.88 | 0.00 |
| 37053 | ERCO | 2021-02-18 | boosting_cluster | 6.06 | 1.36 | 0.00 |
| 37041 | ERCO | 2021-02-18 | boosting_long | 3.87 | -1.15 | -1.15 |
| 37052 | ERCO | 2021-02-18 | boosting_nospecial | 7.85 | 2.76 | 0.00 |
| 37045 | ERCO | 2021-02-18 | boosting_sentinel | 8.70 | 3.13 | 0.00 |
| 37054 | ERCO | 2021-02-18 | last_known_day | 14.79 | -20.49 | -20.49 |
| 37055 | ERCO | 2021-02-18 | profile | 5.37 | -5.70 | -5.70 |
| 37046 | ERCO | 2021-02-18 | recency_regression | 2.73 | -0.95 | -0.95 |
| 37043 | ERCO | 2021-02-18 | recency_regression_sentinel | 2.73 | -0.95 | -0.95 |
| 61042 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 61047 | MISO | 2021-02-16 | additive | 2.63 | -1.97 | -1.97 |
| 61049 | MISO | 2021-02-16 | additive_cluster | 2.51 | -1.90 | -1.90 |
| 61040 | MISO | 2021-02-16 | additive_long | 2.23 | -1.57 | -1.57 |
| 61044 | MISO | 2021-02-16 | additive_sentinel | 2.63 | -1.97 | -1.97 |
| 61050 | MISO | 2021-02-16 | additive_separate | 2.63 | -1.97 | -1.97 |
| 61048 | MISO | 2021-02-16 | additive_special | 2.52 | -1.46 | -1.46 |
| 61051 | MISO | 2021-02-16 | boosting | 5.65 | -6.63 | -6.63 |
| 61053 | MISO | 2021-02-16 | boosting_cluster | 6.52 | -7.16 | -7.16 |
| 61041 | MISO | 2021-02-16 | boosting_long | 3.96 | -3.77 | -3.77 |
| 61052 | MISO | 2021-02-16 | boosting_nospecial | 4.90 | -5.90 | -5.90 |
| 61045 | MISO | 2021-02-16 | boosting_sentinel | 4.79 | -6.23 | -6.23 |
| 61054 | MISO | 2021-02-16 | last_known_day | 1.83 | -5.59 | -5.59 |
| 61055 | MISO | 2021-02-16 | profile | 8.70 | -7.19 | -7.19 |
| 61046 | MISO | 2021-02-16 | recency_regression | 7.40 | -6.85 | -6.85 |
| 61043 | MISO | 2021-02-16 | recency_regression_sentinel | 7.40 | -6.85 | -6.85 |
| 96914 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 96919 | SWPP | 2021-02-15 | additive | 2.19 | -2.44 | -2.44 |
| 96921 | SWPP | 2021-02-15 | additive_cluster | 3.06 | -0.86 | -0.86 |
| 96912 | SWPP | 2021-02-15 | additive_long | 4.52 | 2.27 | 0.00 |
| 96916 | SWPP | 2021-02-15 | additive_sentinel | 1.90 | -2.68 | -2.68 |
| 96922 | SWPP | 2021-02-15 | additive_separate | 2.19 | -2.44 | -2.44 |
| 96920 | SWPP | 2021-02-15 | additive_special | 2.15 | -2.43 | -2.43 |
| 96923 | SWPP | 2021-02-15 | boosting | 5.52 | -7.82 | -7.82 |
| 96925 | SWPP | 2021-02-15 | boosting_cluster | 6.27 | -9.94 | -9.94 |
| 96913 | SWPP | 2021-02-15 | boosting_long | 5.21 | -7.70 | -7.70 |
| 96924 | SWPP | 2021-02-15 | boosting_nospecial | 5.74 | -8.32 | -8.32 |
| 96917 | SWPP | 2021-02-15 | boosting_sentinel | 5.79 | -8.58 | -8.58 |
| 96926 | SWPP | 2021-02-15 | last_known_day | 5.65 | -6.47 | -6.47 |
| 96927 | SWPP | 2021-02-15 | profile | 9.92 | -7.53 | -7.53 |
| 96918 | SWPP | 2021-02-15 | recency_regression | 8.24 | -3.68 | -3.68 |
| 96915 | SWPP | 2021-02-15 | recency_regression_sentinel | 9.43 | -4.96 | -4.96 |
| 96930 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 96935 | SWPP | 2021-02-16 | additive | 6.90 | 1.66 | 0.00 |
| 96937 | SWPP | 2021-02-16 | additive_cluster | 7.72 | 2.47 | 0.00 |
| 96928 | SWPP | 2021-02-16 | additive_long | 9.32 | 6.48 | 0.00 |
| 96932 | SWPP | 2021-02-16 | additive_sentinel | 6.45 | 1.74 | 0.00 |
| 96938 | SWPP | 2021-02-16 | additive_separate | 6.90 | 1.66 | 0.00 |
| 96936 | SWPP | 2021-02-16 | additive_special | 6.93 | 1.72 | 0.00 |
| 96939 | SWPP | 2021-02-16 | boosting | 3.45 | -6.93 | -6.93 |
| 96941 | SWPP | 2021-02-16 | boosting_cluster | 3.31 | -7.95 | -7.95 |
| 96929 | SWPP | 2021-02-16 | boosting_long | 3.41 | -6.94 | -6.94 |
| 96940 | SWPP | 2021-02-16 | boosting_nospecial | 3.31 | -7.05 | -7.05 |
| 96933 | SWPP | 2021-02-16 | boosting_sentinel | 3.44 | -7.30 | -7.30 |
| 96942 | SWPP | 2021-02-16 | last_known_day | 6.45 | -0.45 | -0.45 |
| 96943 | SWPP | 2021-02-16 | profile | 5.00 | -8.76 | -8.76 |
| 96934 | SWPP | 2021-02-16 | recency_regression | 7.20 | 7.97 | 0.00 |
| 96931 | SWPP | 2021-02-16 | recency_regression_sentinel | 8.80 | 6.65 | 0.00 |
| 119330 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 119335 | TVA | 2022-12-23 | additive | 14.64 | -15.51 | -15.51 |
| 119337 | TVA | 2022-12-23 | additive_cluster | 16.39 | -17.79 | -17.79 |
| 119328 | TVA | 2022-12-23 | additive_long | 7.93 | -6.77 | -6.77 |
| 119332 | TVA | 2022-12-23 | additive_sentinel | 14.65 | -15.51 | -15.51 |
| 119338 | TVA | 2022-12-23 | additive_separate | 14.64 | -15.51 | -15.51 |
| 119336 | TVA | 2022-12-23 | additive_special | 13.99 | -13.76 | -13.76 |
| 119339 | TVA | 2022-12-23 | boosting | 17.29 | -18.74 | -18.74 |
| 119341 | TVA | 2022-12-23 | boosting_cluster | 17.43 | -18.08 | -18.08 |
| 119329 | TVA | 2022-12-23 | boosting_long | 14.28 | -14.32 | -14.32 |
| 119340 | TVA | 2022-12-23 | boosting_nospecial | 17.34 | -18.46 | -18.46 |
| 119333 | TVA | 2022-12-23 | boosting_sentinel | 16.89 | -18.42 | -18.42 |
| 119342 | TVA | 2022-12-23 | last_known_day | 38.49 | -39.75 | -39.75 |
| 119343 | TVA | 2022-12-23 | profile | 33.41 | -35.97 | -35.97 |
| 119334 | TVA | 2022-12-23 | recency_regression | 17.85 | -19.05 | -19.05 |
| 119331 | TVA | 2022-12-23 | recency_regression_sentinel | 17.86 | -19.06 | -19.06 |
| 119346 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 119351 | TVA | 2022-12-24 | additive | 8.68 | -20.29 | -20.29 |
| 119353 | TVA | 2022-12-24 | additive_cluster | 6.02 | -20.53 | -20.53 |
| 119344 | TVA | 2022-12-24 | additive_long | 3.98 | -9.72 | -9.72 |
| 119348 | TVA | 2022-12-24 | additive_sentinel | 8.68 | -20.29 | -20.29 |
| 119354 | TVA | 2022-12-24 | additive_separate | 8.68 | -20.29 | -20.29 |
| 119352 | TVA | 2022-12-24 | additive_special | 10.64 | -22.51 | -22.51 |
| 119355 | TVA | 2022-12-24 | boosting | 7.61 | -16.53 | -16.53 |
| 119357 | TVA | 2022-12-24 | boosting_cluster | 9.63 | -20.74 | -20.74 |
| 119345 | TVA | 2022-12-24 | boosting_long | 5.76 | -12.55 | -12.55 |
| 119356 | TVA | 2022-12-24 | boosting_nospecial | 7.07 | -15.92 | -15.92 |
| 119349 | TVA | 2022-12-24 | boosting_sentinel | 8.18 | -18.64 | -18.64 |
| 119358 | TVA | 2022-12-24 | last_known_day | 18.57 | -22.60 | -22.60 |
| 119359 | TVA | 2022-12-24 | profile | 43.83 | -54.16 | -54.16 |
| 119350 | TVA | 2022-12-24 | recency_regression | 6.63 | -13.17 | -13.17 |
| 119347 | TVA | 2022-12-24 | recency_regression_sentinel | 6.63 | -13.17 | -13.17 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive | BPAT | mape | 16.508 | 0.000 | 750 |
| additive | CISO | mape | 17.309 | 0.000 | 737 |
| additive | DUK | mape | 14.555 | 0.000 | 750 |
| additive | ERCO | mape | 12.327 | 0.000 | 746 |
| additive | ISNE | mape | 28.207 | 0.000 | 752 |
| additive | MISO | mape | 4.885 | 0.000 | 746 |
| additive | NYIS | mape | 9.681 | 0.000 | 752 |
| additive | PJM | mape | 2.788 | 0.005 | 744 |
| additive | SWPP | mape | -1.241 | 0.214 | 741 |
| additive | TVA | mape | 21.030 | 0.000 | 739 |
| additive_cluster | BPAT | mape | 19.551 | 0.000 | 750 |
| additive_cluster | CISO | mape | 23.342 | 0.000 | 737 |
| additive_cluster | DUK | mape | 22.357 | 0.000 | 750 |
| additive_cluster | ERCO | mape | 17.750 | 0.000 | 746 |
| additive_cluster | ISNE | mape | 30.216 | 0.000 | 752 |
| additive_cluster | MISO | mape | 13.075 | 0.000 | 746 |
| additive_cluster | NYIS | mape | 12.070 | 0.000 | 752 |
| additive_cluster | PJM | mape | 10.800 | 0.000 | 744 |
| additive_cluster | SWPP | mape | 6.252 | 0.000 | 741 |
| additive_cluster | TVA | mape | 25.394 | 0.000 | 739 |
| additive_long | BPAT | mape | 15.554 | 0.000 | 750 |
| additive_long | CISO | mape | 15.776 | 0.000 | 737 |
| additive_long | DUK | mape | 12.186 | 0.000 | 750 |
| additive_long | ERCO | mape | 11.844 | 0.000 | 746 |
| additive_long | ISNE | mape | 26.504 | 0.000 | 752 |
| additive_long | MISO | mape | 2.795 | 0.005 | 746 |
| additive_long | NYIS | mape | 9.145 | 0.000 | 752 |
| additive_long | PJM | mape | 0.853 | 0.394 | 744 |
| additive_long | SWPP | mape | -3.961 | 0.000 | 741 |
| additive_long | TVA | mape | 19.568 | 0.000 | 739 |
| additive_sentinel | BPAT | mape | 16.378 | 0.000 | 750 |
| additive_sentinel | CISO | mape | 17.295 | 0.000 | 737 |
| additive_sentinel | DUK | mape | 14.555 | 0.000 | 750 |
| additive_sentinel | ERCO | mape | 12.327 | 0.000 | 746 |
| additive_sentinel | ISNE | mape | 28.203 | 0.000 | 752 |
| additive_sentinel | MISO | mape | 4.886 | 0.000 | 746 |
| additive_sentinel | NYIS | mape | 9.658 | 0.000 | 752 |
| additive_sentinel | PJM | mape | 2.401 | 0.016 | 744 |
| additive_sentinel | SWPP | mape | -1.278 | 0.201 | 741 |
| additive_sentinel | TVA | mape | 20.986 | 0.000 | 739 |
| additive_separate | BPAT | mape | 16.508 | 0.000 | 750 |
| additive_separate | CISO | mape | 17.309 | 0.000 | 737 |
| additive_separate | DUK | mape | 14.555 | 0.000 | 750 |
| additive_separate | ERCO | mape | 12.327 | 0.000 | 746 |
| additive_separate | ISNE | mape | 28.207 | 0.000 | 752 |
| additive_separate | MISO | mape | 4.885 | 0.000 | 746 |
| additive_separate | NYIS | mape | 9.681 | 0.000 | 752 |
| additive_separate | PJM | mape | 2.788 | 0.005 | 744 |
| additive_separate | SWPP | mape | -1.241 | 0.214 | 741 |
| additive_separate | TVA | mape | 21.030 | 0.000 | 739 |
| additive_special | BPAT | mape | 16.499 | 0.000 | 750 |
| additive_special | CISO | mape | 17.389 | 0.000 | 737 |
| additive_special | DUK | mape | 14.659 | 0.000 | 750 |
| additive_special | ERCO | mape | 12.340 | 0.000 | 746 |
| additive_special | ISNE | mape | 27.901 | 0.000 | 752 |
| additive_special | MISO | mape | 4.718 | 0.000 | 746 |
| additive_special | NYIS | mape | 9.596 | 0.000 | 752 |
| additive_special | PJM | mape | 2.890 | 0.004 | 744 |
| additive_special | SWPP | mape | -1.169 | 0.243 | 741 |
| additive_special | TVA | mape | 21.130 | 0.000 | 739 |
| boosting | BPAT | mape | 18.683 | 0.000 | 750 |
| boosting | CISO | mape | 11.979 | 0.000 | 737 |
| boosting | DUK | mape | 16.956 | 0.000 | 750 |
| boosting | ERCO | mape | 14.105 | 0.000 | 746 |
| boosting | ISNE | mape | 27.258 | 0.000 | 752 |
| boosting | MISO | mape | 7.844 | 0.000 | 746 |
| boosting | NYIS | mape | 10.859 | 0.000 | 752 |
| boosting | PJM | mape | 6.085 | 0.000 | 744 |
| boosting | SWPP | mape | -0.557 | 0.577 | 741 |
| boosting | TVA | mape | 21.853 | 0.000 | 739 |
| boosting_cluster | BPAT | mape | 21.539 | 0.000 | 750 |
| boosting_cluster | CISO | mape | 19.284 | 0.000 | 737 |
| boosting_cluster | DUK | mape | 21.761 | 0.000 | 750 |
| boosting_cluster | ERCO | mape | 17.730 | 0.000 | 746 |
| boosting_cluster | ISNE | mape | 30.604 | 0.000 | 752 |
| boosting_cluster | MISO | mape | 14.313 | 0.000 | 746 |
| boosting_cluster | NYIS | mape | 13.097 | 0.000 | 752 |
| boosting_cluster | PJM | mape | 11.489 | 0.000 | 744 |
| boosting_cluster | SWPP | mape | 5.450 | 0.000 | 741 |
| boosting_cluster | TVA | mape | 25.172 | 0.000 | 739 |
| boosting_long | BPAT | mape | 16.754 | 0.000 | 750 |
| boosting_long | CISO | mape | 11.277 | 0.000 | 737 |
| boosting_long | DUK | mape | 15.011 | 0.000 | 750 |
| boosting_long | ERCO | mape | 12.499 | 0.000 | 746 |
| boosting_long | ISNE | mape | 25.557 | 0.000 | 752 |
| boosting_long | MISO | mape | 5.769 | 0.000 | 746 |
| boosting_long | NYIS | mape | 9.647 | 0.000 | 752 |
| boosting_long | PJM | mape | 4.135 | 0.000 | 744 |
| boosting_long | SWPP | mape | -2.992 | 0.003 | 741 |
| boosting_long | TVA | mape | 20.301 | 0.000 | 739 |
| boosting_nospecial | BPAT | mape | 18.566 | 0.000 | 750 |
| boosting_nospecial | CISO | mape | 12.075 | 0.000 | 737 |
| boosting_nospecial | DUK | mape | 16.905 | 0.000 | 750 |
| boosting_nospecial | ERCO | mape | 13.977 | 0.000 | 746 |
| boosting_nospecial | ISNE | mape | 26.981 | 0.000 | 752 |
| boosting_nospecial | MISO | mape | 8.196 | 0.000 | 746 |
| boosting_nospecial | NYIS | mape | 10.835 | 0.000 | 752 |
| boosting_nospecial | PJM | mape | 5.941 | 0.000 | 744 |
| boosting_nospecial | SWPP | mape | -0.505 | 0.613 | 741 |
| boosting_nospecial | TVA | mape | 21.620 | 0.000 | 739 |
| boosting_sentinel | BPAT | mape | 18.320 | 0.000 | 750 |
| boosting_sentinel | CISO | mape | 12.281 | 0.000 | 737 |
| boosting_sentinel | DUK | mape | 17.140 | 0.000 | 750 |
| boosting_sentinel | ERCO | mape | 14.111 | 0.000 | 746 |
| boosting_sentinel | ISNE | mape | 26.831 | 0.000 | 752 |
| boosting_sentinel | MISO | mape | 8.003 | 0.000 | 746 |
| boosting_sentinel | NYIS | mape | 10.762 | 0.000 | 752 |
| boosting_sentinel | PJM | mape | 5.172 | 0.000 | 744 |
| boosting_sentinel | SWPP | mape | -1.100 | 0.271 | 741 |
| boosting_sentinel | TVA | mape | 21.819 | 0.000 | 739 |
| last_known_day | BPAT | mape | 27.400 | 0.000 | 750 |
| last_known_day | CISO | mape | 24.697 | 0.000 | 737 |
| last_known_day | DUK | mape | 30.340 | 0.000 | 750 |
| last_known_day | ERCO | mape | 23.926 | 0.000 | 746 |
| last_known_day | ISNE | mape | 28.449 | 0.000 | 752 |
| last_known_day | MISO | mape | 22.842 | 0.000 | 746 |
| last_known_day | NYIS | mape | 23.578 | 0.000 | 752 |
| last_known_day | PJM | mape | 20.318 | 0.000 | 744 |
| last_known_day | SWPP | mape | 14.596 | 0.000 | 741 |
| last_known_day | TVA | mape | 30.622 | 0.000 | 739 |
| profile | BPAT | mape | 23.330 | 0.000 | 750 |
| profile | CISO | mape | 18.131 | 0.000 | 737 |
| profile | DUK | mape | 25.188 | 0.000 | 750 |
| profile | ERCO | mape | 23.400 | 0.000 | 746 |
| profile | ISNE | mape | 27.774 | 0.000 | 752 |
| profile | MISO | mape | 18.272 | 0.000 | 746 |
| profile | NYIS | mape | 19.757 | 0.000 | 752 |
| profile | PJM | mape | 18.241 | 0.000 | 744 |
| profile | SWPP | mape | 14.179 | 0.000 | 741 |
| profile | TVA | mape | 26.870 | 0.000 | 739 |
| recency_regression | BPAT | mape | 21.557 | 0.000 | 750 |
| recency_regression | CISO | mape | 25.972 | 0.000 | 737 |
| recency_regression | DUK | mape | 19.558 | 0.000 | 750 |
| recency_regression | ERCO | mape | 16.367 | 0.000 | 746 |
| recency_regression | ISNE | mape | 31.208 | 0.000 | 752 |
| recency_regression | MISO | mape | 11.555 | 0.000 | 746 |
| recency_regression | NYIS | mape | 12.890 | 0.000 | 752 |
| recency_regression | PJM | mape | 7.753 | 0.000 | 744 |
| recency_regression | SWPP | mape | 0.193 | 0.847 | 741 |
| recency_regression | TVA | mape | 27.354 | 0.000 | 739 |
| recency_regression_sentinel | BPAT | mape | 21.515 | 0.000 | 750 |
| recency_regression_sentinel | CISO | mape | 25.883 | 0.000 | 737 |
| recency_regression_sentinel | DUK | mape | 19.559 | 0.000 | 750 |
| recency_regression_sentinel | ERCO | mape | 16.367 | 0.000 | 746 |
| recency_regression_sentinel | ISNE | mape | 31.202 | 0.000 | 752 |
| recency_regression_sentinel | MISO | mape | 11.555 | 0.000 | 746 |
| recency_regression_sentinel | NYIS | mape | 12.872 | 0.000 | 752 |
| recency_regression_sentinel | PJM | mape | 7.833 | 0.000 | 744 |
| recency_regression_sentinel | SWPP | mape | 0.500 | 0.617 | 741 |
| recency_regression_sentinel | TVA | mape | 27.316 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| additive | 0.986 |
| additive_cluster | 0.986 |
| additive_long | 0.986 |
| additive_sentinel | 0.986 |
| additive_separate | 0.986 |
| additive_special | 0.986 |
| boosting | 0.995 |
| boosting_cluster | 0.995 |
| boosting_long | 0.995 |
| boosting_nospecial | 0.995 |
| boosting_sentinel | 0.995 |
| last_known_day | 0.995 |
| profile | 0.999 |
| recency_regression | 0.995 |
| recency_regression_sentinel | 0.995 |
