# Second look at 2023 to 2025: the recipe after phase G, under protocol v2

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase G on 2023 to 2025 under protocol v2. This is a second look at these years: the choices of phase G were made on the development period, but the frozen run of `final2` had already been seen; the honest reading compares this table with `docs/frozen_evaluation.md` and treats the difference as an estimate, not a proof.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | 2.46 | 2.12 | 0.01 | -1.35 | 1.24 | 0.56 | 0.29 | -35.37 | 10336 | 11.00 |
| final3_ensemble | 2.79 | 2.46 | -1.10 | -2.07 | 1.24 | 0.50 | 0.24 | -40.43 | 10336 | 11.00 |
| DF | 2.80 | 2.48 | 0.29 | -1.04 | 0.96 | 0.00 | 0.00 | -41.79 | 10336 | 11.00 |
| final3_additive | 2.92 | 2.55 | -1.00 | -2.12 | 1.26 | 0.47 | 0.23 | -40.44 | 10336 | 11.00 |
| final3_boosting | 2.93 | 2.60 | -1.01 | -2.08 | 1.42 | 0.45 | 0.24 | -38.96 | 10336 | 11.00 |
| final3_recency | 3.57 | 3.25 | -1.33 | -2.49 | 1.55 | 0.34 | 0.22 | -42.33 | 10336 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.01 | 1.81 | -0.42 | -1.23 | 1.17 | -15.51 |  |  | 955 | 6750.12 |
| DF | CISO | 5.09 | 4.88 | -0.68 | -1.63 | 0.91 | -24.50 |  |  | 927 | 25354.22 |
| DF | DUK | 2.66 | 2.33 | 0.52 | -1.22 | 1.04 | -12.31 |  |  | 951 | 12350.17 |
| DF | ERCO | 2.40 | 2.01 | 0.74 | -0.84 | 1.05 | -11.36 |  |  | 955 | 53172.06 |
| DF | FPL | 3.24 | 3.09 | -0.48 | -1.64 | 1.11 | -41.79 |  |  | 884 | 16647.36 |
| DF | ISNE | 2.54 | 2.50 | 0.40 | -0.46 | 0.35 | -5.42 |  |  | 944 | 13030.46 |
| DF | MISO | 2.73 | 2.56 | 2.05 | -0.23 | 0.89 | -6.54 |  |  | 958 | 74137.19 |
| DF | NYIS | 2.65 | 2.47 | -2.46 | -2.62 | 0.46 | -10.12 |  |  | 934 | 17188.52 |
| DF | PJM | 2.42 | 2.20 | -0.52 | -1.15 | 0.93 | -7.65 |  |  | 938 | 93269.88 |
| DF | SWPP | 3.41 | 2.18 | 0.36 | -1.49 | 1.39 | -17.10 |  |  | 940 | 33084.94 |
| DF | TVA | 2.29 | 1.98 | 0.47 | -0.94 | 1.01 | -8.44 |  |  | 950 | 18861.11 |
| final3 | BPAT | 2.25 | 2.01 | -0.14 | -1.24 | 1.40 | -16.37 | 0.43 | 0.41 | 955 | 6750.12 |
| final3 | CISO | 2.71 | 2.50 | -0.07 | -1.39 | 0.88 | -15.23 | 0.86 | 0.37 | 927 | 25354.22 |
| final3 | DUK | 3.34 | 2.79 | 0.31 | -1.91 | 1.37 | -15.01 | 0.36 | 0.26 | 951 | 12350.17 |
| final3 | ERCO | 2.51 | 2.13 | -0.07 | -1.52 | 0.97 | -16.43 | 0.45 | 0.21 | 955 | 53172.06 |
| final3 | FPL | 3.46 | 2.98 | 0.66 | -1.63 | 1.05 | -35.37 | 0.51 | 0.39 | 884 | 16647.36 |
| final3 | ISNE | 3.86 | 3.37 | 0.23 | -1.37 | 0.51 | -22.15 | 0.29 | 0.20 | 944 | 13030.46 |
| final3 | MISO | 1.92 | 1.66 | 0.02 | -1.05 | 1.55 | -7.74 | 0.68 | 0.08 | 958 | 74137.19 |
| final3 | NYIS | 2.73 | 2.38 | 0.08 | -1.29 | 0.71 | -11.89 | 0.50 | 0.74 | 934 | 17188.52 |
| final3 | PJM | 2.18 | 1.90 | 0.01 | -1.27 | 1.28 | -10.24 | 0.59 | 0.38 | 938 | 93269.88 |
| final3 | SWPP | 2.41 | 1.91 | -0.19 | -1.42 | 1.64 | -22.68 | 0.56 | 0.38 | 940 | 33084.94 |
| final3 | TVA | 2.91 | 2.53 | -0.16 | -1.79 | 1.42 | -14.29 | 0.33 | 0.23 | 950 | 18861.11 |
| final3_additive | BPAT | 2.45 | 2.13 | -1.32 | -1.99 | 1.49 | -16.50 | 0.38 | 0.29 | 955 | 6750.12 |
| final3_additive | CISO | 3.85 | 3.42 | -2.39 | -3.32 | 0.99 | -20.57 | 0.73 | 0.27 | 927 | 25354.22 |
| final3_additive | DUK | 3.57 | 3.02 | -0.72 | -2.53 | 1.33 | -17.10 | 0.32 | 0.20 | 951 | 12350.17 |
| final3_additive | ERCO | 3.11 | 2.73 | -1.69 | -2.48 | 0.94 | -18.16 | 0.32 | 0.14 | 955 | 53172.06 |
| final3_additive | FPL | 5.07 | 4.71 | -4.91 | -5.44 | 0.97 | -40.44 | 0.27 | 0.10 | 884 | 16647.36 |
| final3_additive | ISNE | 4.24 | 3.71 | -0.82 | -2.30 | 0.62 | -20.50 | 0.24 | 0.16 | 944 | 13030.46 |
| final3_additive | MISO | 2.23 | 1.97 | -0.77 | -1.59 | 1.63 | -9.86 | 0.60 | 0.06 | 958 | 74137.19 |
| final3_additive | NYIS | 2.94 | 2.57 | -0.95 | -2.01 | 0.61 | -15.07 | 0.46 | 0.63 | 934 | 17188.52 |
| final3_additive | PJM | 2.50 | 2.19 | -0.27 | -1.57 | 1.32 | -11.98 | 0.52 | 0.34 | 938 | 93269.88 |
| final3_additive | SWPP | 2.66 | 2.11 | -0.57 | -1.86 | 1.61 | -21.92 | 0.51 | 0.31 | 940 | 33084.94 |
| final3_additive | TVA | 3.28 | 2.83 | 0.69 | -1.57 | 1.30 | -16.52 | 0.27 | 0.26 | 950 | 18861.11 |
| final3_boosting | BPAT | 2.59 | 2.25 | -0.73 | -1.78 | 1.50 | -17.77 | 0.34 | 0.34 | 955 | 6750.12 |
| final3_boosting | CISO | 3.14 | 2.81 | -1.82 | -2.51 | 0.98 | -13.74 | 0.80 | 0.28 | 927 | 25354.22 |
| final3_boosting | DUK | 3.54 | 3.02 | -1.03 | -2.61 | 1.49 | -17.89 | 0.33 | 0.21 | 951 | 12350.17 |
| final3_boosting | ERCO | 2.93 | 2.63 | -1.75 | -2.53 | 1.16 | -17.25 | 0.34 | 0.14 | 955 | 53172.06 |
| final3_boosting | FPL | 5.42 | 5.17 | -5.58 | -5.91 | 1.38 | -38.96 | 0.19 | 0.08 | 884 | 16647.36 |
| final3_boosting | ISNE | 4.11 | 3.55 | -1.04 | -2.13 | 0.58 | -19.19 | 0.24 | 0.16 | 944 | 13030.46 |
| final3_boosting | MISO | 2.19 | 2.01 | -0.60 | -1.45 | 1.63 | -11.49 | 0.63 | 0.06 | 958 | 74137.19 |
| final3_boosting | NYIS | 2.99 | 2.59 | -0.83 | -1.77 | 0.77 | -12.18 | 0.43 | 0.65 | 934 | 17188.52 |
| final3_boosting | PJM | 2.68 | 2.42 | -0.31 | -1.62 | 1.59 | -10.99 | 0.43 | 0.36 | 938 | 93269.88 |
| final3_boosting | SWPP | 3.00 | 2.31 | -0.49 | -1.95 | 1.77 | -21.31 | 0.46 | 0.31 | 940 | 33084.94 |
| final3_boosting | TVA | 3.25 | 2.80 | 0.03 | -1.87 | 1.52 | -14.45 | 0.26 | 0.23 | 950 | 18861.11 |
| final3_ensemble | BPAT | 2.33 | 2.10 | -1.35 | -1.97 | 1.38 | -16.55 | 0.40 | 0.31 | 955 | 6750.12 |
| final3_ensemble | CISO | 3.34 | 2.94 | -2.06 | -2.85 | 1.00 | -16.59 | 0.78 | 0.28 | 927 | 25354.22 |
| final3_ensemble | DUK | 3.42 | 2.86 | -0.89 | -2.55 | 1.30 | -16.39 | 0.35 | 0.21 | 951 | 12350.17 |
| final3_ensemble | ERCO | 2.98 | 2.61 | -1.94 | -2.61 | 0.97 | -17.02 | 0.35 | 0.13 | 955 | 53172.06 |
| final3_ensemble | FPL | 5.21 | 4.90 | -5.44 | -5.78 | 1.05 | -40.43 | 0.23 | 0.07 | 884 | 16647.36 |
| final3_ensemble | ISNE | 4.08 | 3.58 | -1.20 | -2.21 | 0.57 | -20.39 | 0.24 | 0.14 | 944 | 13030.46 |
| final3_ensemble | MISO | 2.12 | 1.94 | -0.76 | -1.48 | 1.50 | -9.67 | 0.64 | 0.06 | 958 | 74137.19 |
| final3_ensemble | NYIS | 2.84 | 2.48 | -1.03 | -1.89 | 0.67 | -13.59 | 0.48 | 0.64 | 934 | 17188.52 |
| final3_ensemble | PJM | 2.38 | 2.12 | -0.28 | -1.44 | 1.35 | -11.68 | 0.54 | 0.37 | 938 | 93269.88 |
| final3_ensemble | SWPP | 2.59 | 2.10 | -0.74 | -1.92 | 1.56 | -22.00 | 0.52 | 0.30 | 940 | 33084.94 |
| final3_ensemble | TVA | 3.16 | 2.68 | 0.36 | -1.64 | 1.26 | -14.86 | 0.30 | 0.25 | 950 | 18861.11 |
| final3_recency | BPAT | 2.88 | 2.60 | -2.09 | -2.58 | 1.65 | -15.57 | 0.26 | 0.24 | 955 | 6750.12 |
| final3_recency | CISO | 4.91 | 4.63 | -2.11 | -3.38 | 1.28 | -17.13 | 0.55 | 0.26 | 927 | 25354.22 |
| final3_recency | DUK | 3.96 | 3.43 | -0.92 | -2.86 | 1.45 | -17.72 | 0.27 | 0.19 | 951 | 12350.17 |
| final3_recency | ERCO | 3.65 | 3.31 | -2.47 | -3.22 | 1.21 | -19.88 | 0.23 | 0.12 | 955 | 53172.06 |
| final3_recency | FPL | 6.36 | 6.03 | -6.02 | -6.54 | 1.18 | -42.33 | 0.13 | 0.09 | 884 | 16647.36 |
| final3_recency | ISNE | 6.28 | 5.84 | -2.01 | -2.95 | 0.77 | -23.61 | 0.04 | 0.13 | 944 | 13030.46 |
| final3_recency | MISO | 2.78 | 2.54 | -0.89 | -1.77 | 1.99 | -11.52 | 0.50 | 0.07 | 958 | 74137.19 |
| final3_recency | NYIS | 4.22 | 3.89 | -1.52 | -2.54 | 0.96 | -13.78 | 0.24 | 0.54 | 934 | 17188.52 |
| final3_recency | PJM | 2.97 | 2.73 | -0.24 | -1.74 | 1.73 | -12.59 | 0.34 | 0.33 | 938 | 93269.88 |
| final3_recency | SWPP | 3.00 | 2.49 | -1.21 | -2.38 | 1.64 | -22.90 | 0.43 | 0.25 | 940 | 33084.94 |
| final3_recency | TVA | 3.68 | 3.11 | 0.42 | -1.83 | 1.55 | -14.70 | 0.21 | 0.24 | 950 | 18861.11 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | gerri_heather | 3.76 | 0.98 | -1.48 | -3.76 | 6 |
| DF | CISO | gerri_heather | 4.87 | 0.22 | -0.77 | -2.41 | 6 |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | ERCO | gerri_heather | 4.26 | 1.90 | -1.57 | -9.43 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | NYIS | gerri_heather | 3.41 | -2.81 | -2.81 | -3.64 | 5 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| DF | TVA | gerri_heather | 3.50 | 2.67 | -0.73 | -4.40 | 6 |
| final3 | BPAT | gerri_heather | 5.18 | -4.75 | -4.75 | -12.13 | 6 |
| final3 | CISO | gerri_heather | 2.69 | 1.08 | -0.40 | -2.27 | 6 |
| final3 | DUK | gerri_heather | 5.81 | -5.87 | -5.87 | -9.23 | 6 |
| final3 | ERCO | gerri_heather | 6.25 | -7.77 | -7.77 | -13.30 | 6 |
| final3 | FPL | gerri_heather | 4.77 | -5.17 | -5.58 | -9.75 | 6 |
| final3 | ISNE | gerri_heather | 3.78 | -0.26 | -1.38 | -5.47 | 6 |
| final3 | MISO | gerri_heather | 2.98 | -2.15 | -2.56 | -4.79 | 6 |
| final3 | NYIS | gerri_heather | 1.79 | 0.04 | -0.76 | -2.10 | 5 |
| final3 | PJM | gerri_heather | 2.85 | -0.24 | -1.17 | -3.81 | 6 |
| final3 | SWPP | gerri_heather | 5.47 | -5.42 | -5.42 | -13.96 | 6 |
| final3 | TVA | gerri_heather | 3.13 | -0.30 | -1.43 | -5.75 | 6 |
| final3_additive | BPAT | gerri_heather | 6.37 | -6.20 | -6.37 | -16.50 | 6 |
| final3_additive | CISO | gerri_heather | 2.97 | 1.78 | -0.23 | -1.14 | 6 |
| final3_additive | DUK | gerri_heather | 5.92 | -7.33 | -7.33 | -15.52 | 6 |
| final3_additive | ERCO | gerri_heather | 7.99 | -9.83 | -9.83 | -16.86 | 6 |
| final3_additive | FPL | gerri_heather | 6.20 | -7.54 | -7.54 | -13.25 | 6 |
| final3_additive | ISNE | gerri_heather | 4.00 | 0.04 | -1.84 | -6.05 | 6 |
| final3_additive | MISO | gerri_heather | 3.01 | -2.49 | -2.67 | -4.06 | 6 |
| final3_additive | NYIS | gerri_heather | 1.80 | -1.05 | -1.48 | -3.10 | 5 |
| final3_additive | PJM | gerri_heather | 2.82 | 1.45 | -0.25 | -1.13 | 6 |
| final3_additive | SWPP | gerri_heather | 7.06 | -7.68 | -7.68 | -18.06 | 6 |
| final3_additive | TVA | gerri_heather | 3.29 | 1.78 | -1.10 | -6.45 | 6 |
| final3_boosting | BPAT | gerri_heather | 6.64 | -7.67 | -7.67 | -13.59 | 6 |
| final3_boosting | CISO | gerri_heather | 2.93 | 1.62 | -0.48 | -2.86 | 6 |
| final3_boosting | DUK | gerri_heather | 5.75 | -6.18 | -6.52 | -12.16 | 6 |
| final3_boosting | ERCO | gerri_heather | 5.81 | -9.80 | -9.80 | -17.25 | 6 |
| final3_boosting | FPL | gerri_heather | 5.68 | -8.78 | -8.78 | -13.39 | 6 |
| final3_boosting | ISNE | gerri_heather | 3.76 | 0.34 | -0.96 | -4.63 | 6 |
| final3_boosting | MISO | gerri_heather | 2.29 | -2.09 | -2.84 | -5.63 | 6 |
| final3_boosting | NYIS | gerri_heather | 2.15 | 1.37 | -0.24 | -1.19 | 5 |
| final3_boosting | PJM | gerri_heather | 2.77 | -0.14 | -1.32 | -3.77 | 6 |
| final3_boosting | SWPP | gerri_heather | 5.51 | -6.72 | -6.72 | -12.29 | 6 |
| final3_boosting | TVA | gerri_heather | 3.67 | -0.80 | -2.76 | -9.70 | 6 |
| final3_ensemble | BPAT | gerri_heather | 5.61 | -5.91 | -5.91 | -13.48 | 6 |
| final3_ensemble | CISO | gerri_heather | 2.71 | 1.78 | -0.45 | -2.73 | 6 |
| final3_ensemble | DUK | gerri_heather | 5.86 | -7.13 | -7.13 | -14.37 | 6 |
| final3_ensemble | ERCO | gerri_heather | 6.15 | -8.50 | -8.50 | -12.11 | 6 |
| final3_ensemble | FPL | gerri_heather | 6.03 | -8.28 | -8.28 | -12.77 | 6 |
| final3_ensemble | ISNE | gerri_heather | 3.93 | 0.02 | -1.42 | -5.74 | 6 |
| final3_ensemble | MISO | gerri_heather | 2.71 | -2.25 | -2.73 | -5.48 | 6 |
| final3_ensemble | NYIS | gerri_heather | 1.86 | -0.04 | -0.47 | -1.61 | 5 |
| final3_ensemble | PJM | gerri_heather | 2.61 | 0.66 | -0.74 | -2.65 | 6 |
| final3_ensemble | SWPP | gerri_heather | 6.77 | -7.69 | -7.69 | -15.92 | 6 |
| final3_ensemble | TVA | gerri_heather | 3.01 | 1.17 | -1.13 | -5.55 | 6 |
| final3_recency | BPAT | gerri_heather | 4.95 | -3.60 | -3.93 | -10.22 | 6 |
| final3_recency | CISO | gerri_heather | 3.52 | 2.00 | -0.72 | -4.31 | 6 |
| final3_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final3_recency | ERCO | gerri_heather | 5.53 | -5.59 | -5.89 | -10.83 | 6 |
| final3_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final3_recency | ISNE | gerri_heather | 5.43 | -0.43 | -1.75 | -6.86 | 6 |
| final3_recency | MISO | gerri_heather | 3.32 | -2.10 | -2.68 | -7.06 | 6 |
| final3_recency | NYIS | gerri_heather | 3.53 | -0.64 | -0.83 | -2.57 | 5 |
| final3_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final3_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| final3_recency | TVA | gerri_heather | 4.68 | 2.89 | -1.21 | -7.25 | 6 |
| DF | BPAT | january_2025 | 2.46 | -0.63 | -1.13 | -5.68 | 6 |
| DF | CISO | january_2025 | 6.30 | -4.14 | -4.14 | -7.74 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | ERCO | january_2025 | 3.99 | 0.33 | -0.83 | -2.52 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | NYIS | january_2025 | 3.90 | -3.63 | -3.63 | -4.31 | 5 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| DF | TVA | january_2025 | 2.96 | 1.69 | -0.29 | -1.52 | 6 |
| final3 | BPAT | january_2025 | 2.55 | -3.13 | -3.55 | -5.02 | 6 |
| final3 | CISO | january_2025 | 1.95 | 0.53 | -0.18 | -0.83 | 6 |
| final3 | DUK | january_2025 | 4.49 | 0.44 | -1.63 | -6.68 | 6 |
| final3 | ERCO | january_2025 | 3.18 | -4.18 | -4.18 | -7.61 | 6 |
| final3 | FPL | january_2025 | 5.52 | -5.99 | -5.99 | -13.07 | 6 |
| final3 | ISNE | january_2025 | 3.85 | -0.54 | -1.28 | -2.96 | 6 |
| final3 | MISO | january_2025 | 2.72 | -2.55 | -2.55 | -4.88 | 6 |
| final3 | NYIS | january_2025 | 2.10 | 1.59 | -0.00 | -0.01 | 5 |
| final3 | PJM | january_2025 | 2.08 | -1.36 | -1.59 | -3.13 | 6 |
| final3 | SWPP | january_2025 | 2.64 | -2.44 | -2.44 | -3.80 | 6 |
| final3 | TVA | january_2025 | 3.03 | -1.72 | -1.97 | -6.80 | 6 |
| final3_additive | BPAT | january_2025 | 3.13 | -3.48 | -3.96 | -5.58 | 6 |
| final3_additive | CISO | january_2025 | 3.47 | 1.90 | 0.00 | 0.00 | 6 |
| final3_additive | DUK | january_2025 | 4.08 | 1.24 | -0.85 | -5.06 | 6 |
| final3_additive | ERCO | january_2025 | 3.27 | -3.81 | -3.81 | -7.91 | 6 |
| final3_additive | FPL | january_2025 | 4.73 | -3.67 | -3.88 | -9.71 | 6 |
| final3_additive | ISNE | january_2025 | 3.42 | 0.02 | -1.08 | -3.26 | 6 |
| final3_additive | MISO | january_2025 | 2.91 | -2.37 | -2.46 | -4.69 | 6 |
| final3_additive | NYIS | january_2025 | 1.70 | -0.49 | -0.97 | -2.47 | 5 |
| final3_additive | PJM | january_2025 | 2.43 | 0.84 | -0.36 | -1.51 | 6 |
| final3_additive | SWPP | january_2025 | 3.55 | -3.63 | -3.63 | -6.13 | 6 |
| final3_additive | TVA | january_2025 | 3.73 | -1.33 | -2.26 | -6.69 | 6 |
| final3_boosting | BPAT | january_2025 | 3.44 | -6.07 | -6.07 | -8.83 | 6 |
| final3_boosting | CISO | january_2025 | 2.49 | 0.30 | -0.70 | -2.26 | 6 |
| final3_boosting | DUK | january_2025 | 4.49 | -2.71 | -3.17 | -8.26 | 6 |
| final3_boosting | ERCO | january_2025 | 3.49 | -6.07 | -6.07 | -8.33 | 6 |
| final3_boosting | FPL | january_2025 | 4.71 | -6.94 | -6.94 | -13.56 | 6 |
| final3_boosting | ISNE | january_2025 | 4.18 | -0.64 | -1.54 | -3.45 | 6 |
| final3_boosting | MISO | january_2025 | 2.45 | -2.78 | -2.78 | -4.42 | 6 |
| final3_boosting | NYIS | january_2025 | 3.10 | 1.05 | -0.37 | -1.07 | 5 |
| final3_boosting | PJM | january_2025 | 2.50 | -3.92 | -3.92 | -7.15 | 6 |
| final3_boosting | SWPP | january_2025 | 4.55 | -8.49 | -8.49 | -9.83 | 6 |
| final3_boosting | TVA | january_2025 | 2.92 | -2.41 | -2.41 | -5.13 | 6 |
| final3_ensemble | BPAT | january_2025 | 3.19 | -5.31 | -5.37 | -7.31 | 6 |
| final3_ensemble | CISO | january_2025 | 3.01 | 0.98 | -0.59 | -1.68 | 6 |
| final3_ensemble | DUK | january_2025 | 4.09 | -0.31 | -1.74 | -7.54 | 6 |
| final3_ensemble | ERCO | january_2025 | 3.19 | -5.42 | -5.42 | -7.47 | 6 |
| final3_ensemble | FPL | january_2025 | 4.30 | -4.86 | -4.86 | -10.98 | 6 |
| final3_ensemble | ISNE | january_2025 | 3.11 | -0.14 | -0.99 | -2.82 | 6 |
| final3_ensemble | MISO | january_2025 | 2.57 | -3.02 | -3.02 | -4.32 | 6 |
| final3_ensemble | NYIS | january_2025 | 1.32 | 0.22 | -0.37 | -0.77 | 5 |
| final3_ensemble | PJM | january_2025 | 2.21 | -1.71 | -1.81 | -3.33 | 6 |
| final3_ensemble | SWPP | january_2025 | 4.05 | -5.64 | -5.64 | -6.19 | 6 |
| final3_ensemble | TVA | january_2025 | 2.68 | -1.89 | -1.97 | -5.23 | 6 |
| final3_recency | BPAT | january_2025 | 3.27 | -6.31 | -6.31 | -8.11 | 6 |
| final3_recency | CISO | january_2025 | 5.72 | 0.91 | -2.66 | -5.17 | 6 |
| final3_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final3_recency | ERCO | january_2025 | 3.97 | -6.77 | -6.77 | -7.58 | 6 |
| final3_recency | FPL | january_2025 | 5.22 | -3.48 | -3.79 | -8.98 | 6 |
| final3_recency | ISNE | january_2025 | 3.79 | 0.28 | -0.90 | -4.07 | 6 |
| final3_recency | MISO | january_2025 | 3.42 | -4.02 | -4.02 | -5.00 | 6 |
| final3_recency | NYIS | january_2025 | 3.12 | -0.05 | -0.87 | -3.05 | 5 |
| final3_recency | PJM | january_2025 | 2.98 | -2.47 | -2.47 | -4.93 | 6 |
| final3_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.85 | 6 |
| final3_recency | TVA | january_2025 | 2.77 | -1.87 | -2.31 | -4.36 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | DF | eve | 2.99 | 0.36 | -1.20 |  | 257 |
| 7 | final3 | eve | 3.05 | 0.81 | -1.40 | 0.49 | 257 |
| 10 | final3_ensemble | eve | 3.16 | -0.34 | -1.91 | 0.45 | 257 |
| 8 | final3_additive | eve | 3.21 | -0.31 | -2.06 | 0.40 | 257 |
| 9 | final3_boosting | eve | 3.42 | -0.24 | -1.88 | 0.39 | 257 |
| 11 | final3_recency | eve | 3.97 | -0.61 | -2.32 | 0.33 | 257 |
| 1 | final3 | special | 3.27 | -0.18 | -1.94 | 0.51 | 271 |
| 0 | DF | special | 3.32 | 0.05 | -1.49 |  | 271 |
| 4 | final3_ensemble | special | 3.54 | -1.22 | -2.63 | 0.47 | 271 |
| 2 | final3_additive | special | 3.55 | -1.39 | -2.83 | 0.47 | 271 |
| 3 | final3_boosting | special | 3.76 | -1.08 | -2.51 | 0.40 | 271 |
| 5 | final3_recency | special | 4.45 | -1.25 | -3.00 | 0.34 | 271 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | all | 0.395 | 1.377 | 0.411 | 0.891 | 12.076 | 0.895 | 10105 |
| final3 | events | 0.437 | 1.804 | 0.659 | 0.817 | 13.081 | 0.785 | 130 |
| final3 | cold_mornings | 0.435 | 1.660 | 0.564 | 0.845 | 13.187 | 0.852 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3 | BPAT | mape | 5.327 | 0.000 | 955 |
| final3 | CISO | mape | -31.679 | 0.000 | 927 |
| final3 | DUK | mape | 11.197 | 0.000 | 951 |
| final3 | ERCO | mape | 2.286 | 0.022 | 955 |
| final3 | FPL | mape | 3.659 | 0.000 | 884 |
| final3 | ISNE | mape | 18.714 | 0.000 | 944 |
| final3 | MISO | mape | -15.192 | 0.000 | 958 |
| final3 | NYIS | mape | 1.343 | 0.179 | 934 |
| final3 | PJM | mape | -5.486 | 0.000 | 938 |
| final3 | SWPP | mape | -10.365 | 0.000 | 940 |
| final3 | TVA | mape | 11.943 | 0.000 | 950 |
| final3_additive | BPAT | mape | 9.173 | 0.000 | 955 |
| final3_additive | CISO | mape | -14.881 | 0.000 | 927 |
| final3_additive | DUK | mape | 13.619 | 0.000 | 951 |
| final3_additive | ERCO | mape | 11.414 | 0.000 | 955 |
| final3_additive | FPL | mape | 21.710 | 0.000 | 884 |
| final3_additive | ISNE | mape | 22.782 | 0.000 | 944 |
| final3_additive | MISO | mape | -8.879 | 0.000 | 958 |
| final3_additive | NYIS | mape | 4.482 | 0.000 | 934 |
| final3_additive | PJM | mape | 1.738 | 0.082 | 938 |
| final3_additive | SWPP | mape | -7.505 | 0.000 | 940 |
| final3_additive | TVA | mape | 17.200 | 0.000 | 950 |
| final3_boosting | BPAT | mape | 12.110 | 0.000 | 955 |
| final3_boosting | CISO | mape | -24.146 | 0.000 | 927 |
| final3_boosting | DUK | mape | 13.754 | 0.000 | 951 |
| final3_boosting | ERCO | mape | 9.335 | 0.000 | 955 |
| final3_boosting | FPL | mape | 26.770 | 0.000 | 884 |
| final3_boosting | ISNE | mape | 21.714 | 0.000 | 944 |
| final3_boosting | MISO | mape | -9.842 | 0.000 | 958 |
| final3_boosting | NYIS | mape | 5.381 | 0.000 | 934 |
| final3_boosting | PJM | mape | 5.618 | 0.000 | 938 |
| final3_boosting | SWPP | mape | -4.364 | 0.000 | 940 |
| final3_boosting | TVA | mape | 16.946 | 0.000 | 950 |
| final3_ensemble | BPAT | mape | 7.129 | 0.000 | 955 |
| final3_ensemble | CISO | mape | -21.396 | 0.000 | 927 |
| final3_ensemble | DUK | mape | 11.930 | 0.000 | 951 |
| final3_ensemble | ERCO | mape | 9.805 | 0.000 | 955 |
| final3_ensemble | FPL | mape | 23.140 | 0.000 | 884 |
| final3_ensemble | ISNE | mape | 22.002 | 0.000 | 944 |
| final3_ensemble | MISO | mape | -10.985 | 0.000 | 958 |
| final3_ensemble | NYIS | mape | 3.167 | 0.002 | 934 |
| final3_ensemble | PJM | mape | -1.071 | 0.284 | 938 |
| final3_ensemble | SWPP | mape | -8.574 | 0.000 | 940 |
| final3_ensemble | TVA | mape | 15.290 | 0.000 | 950 |
| final3_recency | BPAT | mape | 16.996 | 0.000 | 955 |
| final3_recency | CISO | mape | -1.902 | 0.057 | 927 |
| final3_recency | DUK | mape | 18.732 | 0.000 | 951 |
| final3_recency | ERCO | mape | 18.420 | 0.000 | 955 |
| final3_recency | FPL | mape | 31.650 | 0.000 | 884 |
| final3_recency | ISNE | mape | 42.940 | 0.000 | 944 |
| final3_recency | MISO | mape | 0.765 | 0.444 | 958 |
| final3_recency | NYIS | mape | 20.870 | 0.000 | 934 |
| final3_recency | PJM | mape | 11.746 | 0.000 | 938 |
| final3_recency | SWPP | mape | -3.977 | 0.000 | 940 |
| final3_recency | TVA | mape | 21.226 | 0.000 | 950 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.993 |
| final3 | 0.877 |
| final3_additive | 0.857 |
| final3_boosting | 0.991 |
| final3_ensemble | 0.877 |
| final3_recency | 0.877 |
