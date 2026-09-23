# Second look at 2023 to 2025: the recipe after phase G, under protocol v2

Development BAs: BPAT, DUK, FPL, MISO, NYIS, PJM, SWPP, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe after phase G on 2023 to 2025 under protocol v2. This is a second look at these years: the choices of phase G were made on the development period, but the frozen run of `final2` had already been seen; the honest reading compares this table with `docs/frozen_evaluation.md` and treats the difference as an estimate, not a proof.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | 2.30 | 1.96 | 0.08 | -1.26 | 1.36 | 0.59 | 0.31 | -35.37 | 7419 | 7.00 |
| final3_ensemble | 2.57 | 2.26 | -0.91 | -1.87 | 1.34 | 0.54 | 0.26 | -40.43 | 7419 | 7.00 |
| final3_additive | 2.66 | 2.31 | -0.83 | -1.92 | 1.36 | 0.52 | 0.25 | -40.44 | 7419 | 7.00 |
| final3_boosting | 2.80 | 2.49 | -0.86 | -1.95 | 1.56 | 0.48 | 0.26 | -38.96 | 7419 | 7.00 |
| DF | 2.82 | 2.38 | 0.39 | -1.06 | 0.98 | 0.00 | 0.00 | -41.79 | 7419 | 7.00 |
| final3_recency | 3.23 | 2.91 | -1.06 | -2.24 | 1.69 | 0.39 | 0.24 | -42.33 | 7419 | 7.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.00 | 1.80 | -0.38 | -1.20 | 1.24 | -15.51 |  |  | 1081 | 6762.61 |
| DF | DUK | 2.65 | 2.31 | 0.43 | -1.26 | 1.02 | -13.08 |  |  | 1070 | 12295.77 |
| DF | FPL | 3.21 | 3.06 | -0.60 | -1.71 | 1.12 | -41.79 |  |  | 1003 | 16583.18 |
| DF | MISO | 2.72 | 2.51 | 2.03 | -0.22 | 0.85 | -6.54 |  |  | 1084 | 74014.33 |
| DF | NYIS | 2.62 | 2.46 | -2.44 | -2.59 | 0.43 | -10.12 |  |  | 1058 | 17111.01 |
| DF | PJM | 2.40 | 2.17 | -0.54 | -1.17 | 0.95 | -7.65 |  |  | 1057 | 93208.59 |
| DF | SWPP | 4.33 | 2.46 | 1.42 | -1.38 | 1.49 | -17.10 |  |  | 1066 | 33074.81 |
| final3 | BPAT | 2.25 | 1.98 | -0.08 | -1.24 | 1.46 | -16.37 | 0.43 | 0.40 | 1081 | 6762.61 |
| final3 | DUK | 3.33 | 2.78 | 0.47 | -1.84 | 1.34 | -15.01 | 0.36 | 0.27 | 1070 | 12295.77 |
| final3 | FPL | 3.43 | 2.96 | 0.58 | -1.66 | 1.06 | -35.37 | 0.51 | 0.39 | 1003 | 16583.18 |
| final3 | MISO | 1.90 | 1.65 | 0.09 | -1.00 | 1.54 | -7.74 | 0.69 | 0.08 | 1084 | 74014.33 |
| final3 | NYIS | 2.72 | 2.39 | 0.07 | -1.27 | 0.66 | -17.67 | 0.49 | 0.74 | 1058 | 17111.01 |
| final3 | PJM | 2.16 | 1.87 | 0.06 | -1.23 | 1.26 | -10.24 | 0.59 | 0.40 | 1057 | 93208.59 |
| final3 | SWPP | 2.44 | 1.89 | -0.27 | -1.48 | 1.73 | -22.68 | 0.60 | 0.34 | 1066 | 33074.81 |
| final3_additive | BPAT | 2.45 | 2.12 | -1.28 | -1.98 | 1.52 | -16.50 | 0.38 | 0.29 | 1081 | 6762.61 |
| final3_additive | DUK | 3.54 | 2.94 | -0.60 | -2.44 | 1.34 | -17.10 | 0.32 | 0.21 | 1070 | 12295.77 |
| final3_additive | FPL | 4.96 | 4.59 | -4.68 | -5.28 | 0.99 | -40.44 | 0.27 | 0.11 | 1003 | 16583.18 |
| final3_additive | MISO | 2.19 | 1.93 | -0.70 | -1.53 | 1.57 | -9.86 | 0.62 | 0.06 | 1084 | 74014.33 |
| final3_additive | NYIS | 2.91 | 2.54 | -1.01 | -2.02 | 0.59 | -18.39 | 0.46 | 0.64 | 1058 | 17111.01 |
| final3_additive | PJM | 2.47 | 2.16 | -0.28 | -1.55 | 1.28 | -11.99 | 0.52 | 0.36 | 1057 | 93208.59 |
| final3_additive | SWPP | 2.69 | 2.13 | -0.65 | -1.92 | 1.65 | -21.92 | 0.55 | 0.28 | 1066 | 33074.81 |
| final3_boosting | BPAT | 2.56 | 2.23 | -0.68 | -1.75 | 1.54 | -17.77 | 0.34 | 0.34 | 1081 | 6762.61 |
| final3_boosting | DUK | 3.50 | 2.96 | -0.92 | -2.54 | 1.50 | -17.89 | 0.34 | 0.22 | 1070 | 12295.77 |
| final3_boosting | FPL | 5.42 | 5.19 | -5.50 | -5.83 | 1.34 | -38.96 | 0.19 | 0.08 | 1003 | 16583.18 |
| final3_boosting | MISO | 2.15 | 1.98 | -0.64 | -1.46 | 1.61 | -11.49 | 0.64 | 0.06 | 1084 | 74014.33 |
| final3_boosting | NYIS | 2.98 | 2.59 | -0.78 | -1.72 | 0.75 | -16.02 | 0.42 | 0.66 | 1058 | 17111.01 |
| final3_boosting | PJM | 2.67 | 2.40 | -0.29 | -1.59 | 1.62 | -11.62 | 0.43 | 0.37 | 1057 | 93208.59 |
| final3_boosting | SWPP | 3.02 | 2.31 | -0.64 | -2.05 | 1.85 | -21.31 | 0.51 | 0.27 | 1066 | 33074.81 |
| final3_ensemble | BPAT | 2.31 | 2.07 | -1.32 | -1.95 | 1.43 | -16.55 | 0.40 | 0.30 | 1081 | 6762.61 |
| final3_ensemble | DUK | 3.39 | 2.80 | -0.76 | -2.45 | 1.32 | -16.39 | 0.35 | 0.22 | 1070 | 12295.77 |
| final3_ensemble | FPL | 5.09 | 4.83 | -5.24 | -5.61 | 1.02 | -40.43 | 0.24 | 0.09 | 1003 | 16583.18 |
| final3_ensemble | MISO | 2.09 | 1.88 | -0.73 | -1.45 | 1.47 | -9.67 | 0.65 | 0.06 | 1084 | 74014.33 |
| final3_ensemble | NYIS | 2.81 | 2.47 | -1.01 | -1.84 | 0.65 | -15.75 | 0.48 | 0.65 | 1058 | 17111.01 |
| final3_ensemble | PJM | 2.35 | 2.07 | -0.28 | -1.42 | 1.31 | -11.68 | 0.54 | 0.38 | 1057 | 93208.59 |
| final3_ensemble | SWPP | 2.62 | 2.08 | -0.87 | -2.01 | 1.64 | -22.00 | 0.56 | 0.27 | 1066 | 33074.81 |
| final3_recency | BPAT | 2.88 | 2.60 | -2.09 | -2.58 | 1.69 | -15.57 | 0.26 | 0.23 | 1081 | 6762.61 |
| final3_recency | DUK | 3.97 | 3.44 | -0.74 | -2.75 | 1.47 | -17.72 | 0.26 | 0.21 | 1070 | 12295.77 |
| final3_recency | FPL | 6.17 | 5.75 | -5.73 | -6.30 | 1.17 | -42.33 | 0.13 | 0.10 | 1003 | 16583.18 |
| final3_recency | MISO | 2.74 | 2.50 | -0.84 | -1.74 | 1.98 | -11.52 | 0.51 | 0.07 | 1084 | 74014.33 |
| final3_recency | NYIS | 4.16 | 3.84 | -1.39 | -2.43 | 0.94 | -13.78 | 0.24 | 0.55 | 1058 | 17111.01 |
| final3_recency | PJM | 2.91 | 2.68 | -0.21 | -1.70 | 1.71 | -12.59 | 0.36 | 0.35 | 1057 | 93208.59 |
| final3_recency | SWPP | 3.03 | 2.46 | -1.36 | -2.49 | 1.76 | -22.90 | 0.49 | 0.23 | 1066 | 33074.81 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | gerri_heather | 3.76 | 0.98 | -1.48 | -3.76 | 6 |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | NYIS | gerri_heather | 3.41 | -2.81 | -2.81 | -3.64 | 5 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| final3 | BPAT | gerri_heather | 5.18 | -4.75 | -4.75 | -12.13 | 6 |
| final3 | DUK | gerri_heather | 5.81 | -5.87 | -5.87 | -9.23 | 6 |
| final3 | FPL | gerri_heather | 4.77 | -5.17 | -5.58 | -9.75 | 6 |
| final3 | MISO | gerri_heather | 2.98 | -2.15 | -2.56 | -4.79 | 6 |
| final3 | NYIS | gerri_heather | 1.79 | 0.04 | -0.76 | -2.10 | 5 |
| final3 | PJM | gerri_heather | 2.85 | -0.24 | -1.17 | -3.81 | 6 |
| final3 | SWPP | gerri_heather | 5.47 | -5.42 | -5.42 | -13.96 | 6 |
| final3_additive | BPAT | gerri_heather | 6.37 | -6.20 | -6.37 | -16.50 | 6 |
| final3_additive | DUK | gerri_heather | 5.92 | -7.33 | -7.33 | -15.52 | 6 |
| final3_additive | FPL | gerri_heather | 6.20 | -7.54 | -7.54 | -13.25 | 6 |
| final3_additive | MISO | gerri_heather | 3.01 | -2.49 | -2.67 | -4.06 | 6 |
| final3_additive | NYIS | gerri_heather | 1.80 | -1.05 | -1.48 | -3.10 | 5 |
| final3_additive | PJM | gerri_heather | 2.82 | 1.45 | -0.25 | -1.13 | 6 |
| final3_additive | SWPP | gerri_heather | 7.06 | -7.68 | -7.68 | -18.06 | 6 |
| final3_boosting | BPAT | gerri_heather | 6.64 | -7.67 | -7.67 | -13.59 | 6 |
| final3_boosting | DUK | gerri_heather | 5.75 | -6.18 | -6.52 | -12.16 | 6 |
| final3_boosting | FPL | gerri_heather | 5.68 | -8.78 | -8.78 | -13.39 | 6 |
| final3_boosting | MISO | gerri_heather | 2.29 | -2.09 | -2.84 | -5.63 | 6 |
| final3_boosting | NYIS | gerri_heather | 2.15 | 1.37 | -0.24 | -1.19 | 5 |
| final3_boosting | PJM | gerri_heather | 2.77 | -0.14 | -1.32 | -3.77 | 6 |
| final3_boosting | SWPP | gerri_heather | 5.51 | -6.72 | -6.72 | -12.29 | 6 |
| final3_ensemble | BPAT | gerri_heather | 5.61 | -5.91 | -5.91 | -13.48 | 6 |
| final3_ensemble | DUK | gerri_heather | 5.86 | -7.13 | -7.13 | -14.37 | 6 |
| final3_ensemble | FPL | gerri_heather | 6.03 | -8.28 | -8.28 | -12.77 | 6 |
| final3_ensemble | MISO | gerri_heather | 2.71 | -2.25 | -2.73 | -5.48 | 6 |
| final3_ensemble | NYIS | gerri_heather | 1.86 | -0.04 | -0.47 | -1.61 | 5 |
| final3_ensemble | PJM | gerri_heather | 2.61 | 0.66 | -0.74 | -2.65 | 6 |
| final3_ensemble | SWPP | gerri_heather | 6.77 | -7.69 | -7.69 | -15.92 | 6 |
| final3_recency | BPAT | gerri_heather | 4.95 | -3.60 | -3.93 | -10.22 | 6 |
| final3_recency | DUK | gerri_heather | 6.46 | -8.02 | -8.02 | -15.68 | 6 |
| final3_recency | FPL | gerri_heather | 6.74 | -8.66 | -8.66 | -13.98 | 6 |
| final3_recency | MISO | gerri_heather | 3.32 | -2.10 | -2.68 | -7.06 | 6 |
| final3_recency | NYIS | gerri_heather | 3.53 | -0.64 | -0.83 | -2.57 | 5 |
| final3_recency | PJM | gerri_heather | 3.48 | 0.55 | -1.42 | -4.10 | 6 |
| final3_recency | SWPP | gerri_heather | 8.18 | -8.79 | -8.79 | -17.66 | 6 |
| DF | BPAT | january_2025 | 2.46 | -0.63 | -1.13 | -5.68 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | NYIS | january_2025 | 3.90 | -3.63 | -3.63 | -4.31 | 5 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| final3 | BPAT | january_2025 | 2.55 | -3.13 | -3.55 | -5.02 | 6 |
| final3 | DUK | january_2025 | 4.49 | 0.44 | -1.63 | -6.68 | 6 |
| final3 | FPL | january_2025 | 5.52 | -5.99 | -5.99 | -13.07 | 6 |
| final3 | MISO | january_2025 | 2.72 | -2.55 | -2.55 | -4.88 | 6 |
| final3 | NYIS | january_2025 | 2.10 | 1.59 | -0.00 | -0.01 | 5 |
| final3 | PJM | january_2025 | 2.08 | -1.36 | -1.59 | -3.13 | 6 |
| final3 | SWPP | january_2025 | 2.64 | -2.44 | -2.44 | -3.80 | 6 |
| final3_additive | BPAT | january_2025 | 3.13 | -3.48 | -3.96 | -5.58 | 6 |
| final3_additive | DUK | january_2025 | 4.08 | 1.24 | -0.85 | -5.06 | 6 |
| final3_additive | FPL | january_2025 | 4.73 | -3.67 | -3.88 | -9.71 | 6 |
| final3_additive | MISO | january_2025 | 2.91 | -2.37 | -2.46 | -4.69 | 6 |
| final3_additive | NYIS | january_2025 | 1.70 | -0.49 | -0.97 | -2.47 | 5 |
| final3_additive | PJM | january_2025 | 2.43 | 0.84 | -0.36 | -1.51 | 6 |
| final3_additive | SWPP | january_2025 | 3.55 | -3.63 | -3.63 | -6.13 | 6 |
| final3_boosting | BPAT | january_2025 | 3.44 | -6.07 | -6.07 | -8.83 | 6 |
| final3_boosting | DUK | january_2025 | 4.49 | -2.71 | -3.17 | -8.26 | 6 |
| final3_boosting | FPL | january_2025 | 4.71 | -6.94 | -6.94 | -13.56 | 6 |
| final3_boosting | MISO | january_2025 | 2.45 | -2.78 | -2.78 | -4.42 | 6 |
| final3_boosting | NYIS | january_2025 | 3.10 | 1.05 | -0.37 | -1.07 | 5 |
| final3_boosting | PJM | january_2025 | 2.50 | -3.92 | -3.92 | -7.15 | 6 |
| final3_boosting | SWPP | january_2025 | 4.55 | -8.49 | -8.49 | -9.83 | 6 |
| final3_ensemble | BPAT | january_2025 | 3.19 | -5.31 | -5.37 | -7.31 | 6 |
| final3_ensemble | DUK | january_2025 | 4.09 | -0.31 | -1.74 | -7.54 | 6 |
| final3_ensemble | FPL | january_2025 | 4.30 | -4.86 | -4.86 | -10.98 | 6 |
| final3_ensemble | MISO | january_2025 | 2.57 | -3.02 | -3.02 | -4.32 | 6 |
| final3_ensemble | NYIS | january_2025 | 1.32 | 0.22 | -0.37 | -0.77 | 5 |
| final3_ensemble | PJM | january_2025 | 2.21 | -1.71 | -1.81 | -3.33 | 6 |
| final3_ensemble | SWPP | january_2025 | 4.05 | -5.64 | -5.64 | -6.19 | 6 |
| final3_recency | BPAT | january_2025 | 3.27 | -6.31 | -6.31 | -8.11 | 6 |
| final3_recency | DUK | january_2025 | 4.53 | 0.53 | -1.84 | -9.33 | 6 |
| final3_recency | FPL | january_2025 | 5.22 | -3.48 | -3.79 | -8.98 | 6 |
| final3_recency | MISO | january_2025 | 3.42 | -4.02 | -4.02 | -5.00 | 6 |
| final3_recency | NYIS | january_2025 | 3.12 | -0.05 | -0.87 | -3.05 | 5 |
| final3_recency | PJM | january_2025 | 2.98 | -2.47 | -2.47 | -4.93 | 6 |
| final3_recency | SWPP | january_2025 | 4.51 | -5.15 | -5.15 | -8.85 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | final3 | eve | 3.02 | 0.80 | -1.38 | 0.48 | 205 |
| 10 | final3_ensemble | eve | 3.10 | -0.47 | -1.94 | 0.48 | 205 |
| 8 | final3_additive | eve | 3.17 | -0.34 | -2.01 | 0.43 | 205 |
| 6 | DF | eve | 3.33 | 0.77 | -1.20 |  | 205 |
| 9 | final3_boosting | eve | 3.39 | -0.43 | -2.01 | 0.39 | 205 |
| 11 | final3_recency | eve | 3.83 | -0.73 | -2.33 | 0.34 | 205 |
| 1 | final3 | special | 3.12 | 0.03 | -1.73 | 0.50 | 215 |
| 4 | final3_ensemble | special | 3.33 | -1.24 | -2.51 | 0.48 | 215 |
| 2 | final3_additive | special | 3.34 | -1.35 | -2.68 | 0.47 | 215 |
| 0 | DF | special | 3.54 | 0.58 | -1.39 |  | 215 |
| 3 | final3_boosting | special | 3.61 | -1.12 | -2.46 | 0.37 | 215 |
| 5 | final3_recency | special | 4.11 | -1.29 | -2.82 | 0.35 | 215 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final3 | all | 0.380 | 1.301 | 0.395 | 0.892 | 11.569 | 0.897 | 7272 |
| final3 | events | 0.451 | 1.840 | 0.724 | 0.795 | 12.843 | 0.732 | 82 |
| final3 | cold_mornings | 0.427 | 1.655 | 0.557 | 0.838 | 13.137 | 0.843 | 210 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final3 | BPAT | mape | 5.776 | 0.000 | 1081 |
| final3 | DUK | mape | 11.726 | 0.000 | 1070 |
| final3 | FPL | mape | 3.999 | 0.000 | 1003 |
| final3 | MISO | mape | -16.472 | 0.000 | 1084 |
| final3 | NYIS | mape | 1.699 | 0.089 | 1058 |
| final3 | PJM | mape | -5.973 | 0.000 | 1057 |
| final3 | SWPP | mape | -15.306 | 0.000 | 1066 |
| final3_additive | BPAT | mape | 9.917 | 0.000 | 1081 |
| final3_additive | DUK | mape | 14.064 | 0.000 | 1070 |
| final3_additive | FPL | mape | 22.501 | 0.000 | 1003 |
| final3_additive | MISO | mape | -10.118 | 0.000 | 1084 |
| final3_additive | NYIS | mape | 4.771 | 0.000 | 1058 |
| final3_additive | PJM | mape | 1.665 | 0.096 | 1057 |
| final3_additive | SWPP | mape | -12.991 | 0.000 | 1066 |
| final3_boosting | BPAT | mape | 12.447 | 0.000 | 1081 |
| final3_boosting | DUK | mape | 14.098 | 0.000 | 1070 |
| final3_boosting | FPL | mape | 28.932 | 0.000 | 1003 |
| final3_boosting | MISO | mape | -10.980 | 0.000 | 1084 |
| final3_boosting | NYIS | mape | 6.019 | 0.000 | 1058 |
| final3_boosting | PJM | mape | 6.169 | 0.000 | 1057 |
| final3_boosting | SWPP | mape | -10.740 | 0.000 | 1066 |
| final3_ensemble | BPAT | mape | 7.402 | 0.000 | 1081 |
| final3_ensemble | DUK | mape | 12.219 | 0.000 | 1070 |
| final3_ensemble | FPL | mape | 24.183 | 0.000 | 1003 |
| final3_ensemble | MISO | mape | -12.287 | 0.000 | 1084 |
| final3_ensemble | NYIS | mape | 3.286 | 0.001 | 1058 |
| final3_ensemble | PJM | mape | -1.276 | 0.202 | 1057 |
| final3_ensemble | SWPP | mape | -13.833 | 0.000 | 1066 |
| final3_recency | BPAT | mape | 18.156 | 0.000 | 1081 |
| final3_recency | DUK | mape | 19.472 | 0.000 | 1070 |
| final3_recency | FPL | mape | 32.912 | 0.000 | 1003 |
| final3_recency | MISO | mape | 0.349 | 0.727 | 1084 |
| final3_recency | NYIS | mape | 21.580 | 0.000 | 1058 |
| final3_recency | PJM | mape | 11.821 | 0.000 | 1057 |
| final3_recency | SWPP | mape | -9.942 | 0.000 | 1066 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.992 |
| final3 | 0.990 |
| final3_additive | 0.967 |
| final3_boosting | 0.990 |
| final3_ensemble | 0.990 |
| final3_recency | 0.990 |
