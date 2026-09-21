# Phase F: the recipe in one run

Development BAs: BPAT, DUK, ERCO, FPL, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. One run of the recipe after phase F: the phase E members (additive model with special days and, at ISO-NE and CAISO, the PV terms; boosting with the sky features there), their ensemble by recent error, the median correction and the 90 % band read from the 40 known days of the same regime nearest in forecast minimum temperature, at an adaptive level per regime, and the point read at the 60th percentile around the forecast peak.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | 2.51 | 2.17 | 0.05 | -1.38 | 1.44 | 0.63 | 0.35 | -48.85 | 6674 | 9.00 |
| final_ensemble | 2.81 | 2.46 | -1.13 | -2.11 | 1.40 | 0.57 | 0.29 | -53.35 | 6674 | 9.00 |
| final_boosting | 2.98 | 2.62 | -0.91 | -2.08 | 1.62 | 0.54 | 0.30 | -52.25 | 6674 | 9.00 |
| final_additive | 3.04 | 2.67 | -1.36 | -2.34 | 1.53 | 0.54 | 0.27 | -54.20 | 6674 | 9.00 |
| DF | 3.09 | 2.79 | 0.07 | -1.33 | 1.17 | 0.00 | 0.00 | -53.60 | 6674 | 9.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | FPL | 3.92 | 3.63 | -3.97 | -4.36 | 1.21 | -53.60 |  |  | 700 | 15274.07 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 3.65 | 3.48 | -1.47 | -1.91 | 1.63 | -10.72 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.85 | 3.49 | 2.60 | -0.43 | 1.25 | -19.98 |  |  | 747 | 31342.11 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| final2 | BPAT | 2.55 | 2.21 | -0.24 | -1.41 | 1.81 | -18.21 | 0.37 | 0.26 | 750 | 6533.15 |
| final2 | DUK | 3.36 | 3.03 | 0.11 | -1.85 | 1.32 | -15.78 | 0.39 | 0.32 | 750 | 12129.97 |
| final2 | ERCO | 2.79 | 2.38 | 0.20 | -1.47 | 1.12 | -13.56 | 0.44 | 0.28 | 746 | 46782.53 |
| final2 | FPL | 3.77 | 3.34 | -0.97 | -2.91 | 1.18 | -48.85 | 0.59 | 0.65 | 700 | 15274.07 |
| final2 | MISO | 2.10 | 1.87 | 0.11 | -1.03 | 1.63 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2 | NYIS | 2.48 | 2.10 | 0.19 | -1.30 | 0.58 | -12.50 | 0.57 | 0.71 | 752 | 17400.75 |
| final2 | PJM | 2.29 | 1.98 | 0.05 | -1.31 | 1.64 | -10.41 | 0.86 | 0.58 | 744 | 91927.69 |
| final2 | SWPP | 2.44 | 1.99 | -0.04 | -1.35 | 1.49 | -20.96 | 0.73 | 0.11 | 747 | 31342.11 |
| final2 | TVA | 3.02 | 2.63 | 0.40 | -1.52 | 1.36 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final_additive | BPAT | 2.81 | 2.45 | -0.89 | -1.81 | 1.85 | -18.41 | 0.29 | 0.22 | 750 | 6533.15 |
| final_additive | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| final_additive | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
| final_additive | FPL | 6.20 | 5.63 | -6.55 | -7.12 | 1.15 | -54.20 | 0.29 | 0.28 | 700 | 15274.07 |
| final_additive | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| final_additive | NYIS | 2.72 | 2.37 | -0.86 | -2.08 | 0.60 | -15.67 | 0.51 | 0.60 | 752 | 17400.75 |
| final_additive | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.75 | 0.51 | 744 | 91927.69 |
| final_additive | SWPP | 2.61 | 2.11 | -0.25 | -1.59 | 1.54 | -20.36 | 0.70 | 0.10 | 747 | 31342.11 |
| final_additive | TVA | 3.35 | 2.97 | -1.05 | -2.35 | 1.42 | -14.12 | 0.25 | 0.26 | 739 | 18562.62 |
| final_boosting | BPAT | 2.73 | 2.43 | -0.43 | -1.57 | 2.00 | -18.16 | 0.27 | 0.24 | 750 | 6533.15 |
| final_boosting | DUK | 3.58 | 3.12 | -0.42 | -2.27 | 1.50 | -16.82 | 0.33 | 0.27 | 750 | 12129.97 |
| final_boosting | ERCO | 3.13 | 2.72 | -2.27 | -2.98 | 1.29 | -15.00 | 0.35 | 0.18 | 746 | 46782.53 |
| final_boosting | FPL | 6.29 | 5.93 | -6.96 | -7.30 | 1.39 | -52.25 | 0.20 | 0.27 | 700 | 15274.07 |
| final_boosting | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| final_boosting | NYIS | 2.70 | 2.40 | -0.48 | -1.61 | 0.74 | -14.02 | 0.51 | 0.66 | 752 | 17400.75 |
| final_boosting | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.75 | 0.57 | 744 | 91927.69 |
| final_boosting | SWPP | 2.73 | 2.19 | -0.89 | -1.99 | 1.69 | -28.44 | 0.68 | 0.08 | 747 | 31342.11 |
| final_boosting | TVA | 3.28 | 2.85 | -0.22 | -1.84 | 1.54 | -15.24 | 0.24 | 0.30 | 739 | 18562.62 |
| final_ensemble | BPAT | 2.59 | 2.27 | -0.66 | -1.61 | 1.83 | -18.29 | 0.32 | 0.23 | 750 | 6533.15 |
| final_ensemble | DUK | 3.43 | 2.97 | -0.56 | -2.26 | 1.33 | -15.64 | 0.37 | 0.27 | 750 | 12129.97 |
| final_ensemble | ERCO | 3.13 | 2.70 | -2.25 | -2.89 | 1.07 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| final_ensemble | FPL | 6.05 | 5.68 | -6.70 | -7.08 | 1.17 | -53.35 | 0.26 | 0.27 | 700 | 15274.07 |
| final_ensemble | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| final_ensemble | NYIS | 2.49 | 2.14 | -0.64 | -1.71 | 0.56 | -13.90 | 0.56 | 0.65 | 752 | 17400.75 |
| final_ensemble | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.79 | 0.55 | 744 | 91927.69 |
| final_ensemble | SWPP | 2.51 | 1.99 | -0.56 | -1.70 | 1.51 | -21.47 | 0.71 | 0.09 | 747 | 31342.11 |
| final_ensemble | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | uri | 2.77 | -0.21 | -1.69 | -6.97 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | FPL | uri | 5.37 | -5.97 | -6.56 | -14.35 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 2.82 | -1.01 | -1.14 | -2.03 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final2 | BPAT | uri | 2.87 | 0.04 | -0.92 | -4.38 | 6 |
| final2 | DUK | uri | 3.51 | -1.08 | -1.67 | -4.03 | 6 |
| final2 | ERCO | uri | 7.11 | -9.52 | -9.52 | -10.27 | 2 |
| final2 | FPL | uri | 7.94 | -7.78 | -7.78 | -11.49 | 6 |
| final2 | MISO | uri | 3.44 | -2.39 | -2.82 | -5.84 | 5 |
| final2 | NYIS | uri | 2.03 | 2.22 | -0.14 | -0.82 | 6 |
| final2 | PJM | uri | 1.86 | 0.07 | -0.65 | -2.07 | 6 |
| final2 | SWPP | uri | 6.41 | 1.17 | -2.28 | -5.30 | 4 |
| final2 | TVA | uri | 3.04 | -1.89 | -2.67 | -5.67 | 6 |
| final_additive | BPAT | uri | 3.18 | -0.34 | -1.38 | -3.11 | 6 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| final_additive | FPL | uri | 10.40 | -14.61 | -14.61 | -18.21 | 6 |
| final_additive | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| final_additive | NYIS | uri | 2.24 | 2.05 | -0.04 | -0.13 | 6 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| final_additive | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| final_boosting | BPAT | uri | 3.51 | 0.87 | -1.00 | -4.84 | 6 |
| final_boosting | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| final_boosting | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| final_boosting | FPL | uri | 9.40 | -11.00 | -11.00 | -15.39 | 6 |
| final_boosting | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| final_boosting | NYIS | uri | 2.22 | 0.80 | -0.76 | -2.94 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| final_boosting | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| final_ensemble | BPAT | uri | 2.95 | 0.23 | -0.68 | -3.44 | 6 |
| final_ensemble | DUK | uri | 3.42 | -2.79 | -2.79 | -6.10 | 6 |
| final_ensemble | ERCO | uri | 6.28 | -9.24 | -9.24 | -9.46 | 2 |
| final_ensemble | FPL | uri | 9.92 | -12.91 | -12.91 | -15.50 | 6 |
| final_ensemble | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| final_ensemble | NYIS | uri | 2.11 | 1.50 | -0.23 | -1.35 | 6 |
| final_ensemble | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| final_ensemble | SWPP | uri | 6.08 | -0.39 | -2.96 | -6.25 | 4 |
| final_ensemble | TVA | uri | 2.71 | -1.06 | -1.72 | -3.36 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | FPL | elliott | 6.78 | -5.10 | -5.10 | -8.18 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 4.02 | -3.14 | -3.14 | -5.88 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final2 | BPAT | elliott | 3.70 | -2.63 | -3.01 | -6.46 | 5 |
| final2 | DUK | elliott | 3.14 | -1.01 | -1.49 | -4.41 | 4 |
| final2 | ERCO | elliott | 6.82 | -1.38 | -3.86 | -9.30 | 5 |
| final2 | FPL | elliott | 7.90 | -9.00 | -9.23 | -14.82 | 5 |
| final2 | MISO | elliott | 3.42 | -1.58 | -2.69 | -4.10 | 5 |
| final2 | NYIS | elliott | 2.78 | -0.62 | -1.45 | -3.18 | 5 |
| final2 | PJM | elliott | 4.26 | -2.70 | -3.11 | -6.29 | 5 |
| final2 | SWPP | elliott | 4.56 | 0.73 | -1.68 | -4.76 | 5 |
| final2 | TVA | elliott | 6.70 | 4.69 | 0.00 | 0.00 | 3 |
| final_additive | BPAT | elliott | 4.28 | -1.49 | -2.47 | -4.95 | 5 |
| final_additive | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| final_additive | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| final_additive | FPL | elliott | 11.83 | -1.71 | -7.55 | -19.18 | 5 |
| final_additive | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| final_additive | NYIS | elliott | 3.27 | -1.91 | -2.37 | -3.71 | 5 |
| final_additive | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| final_additive | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| final_additive | TVA | elliott | 7.91 | 5.47 | 0.00 | 0.00 | 3 |
| final_boosting | BPAT | elliott | 4.33 | -5.23 | -5.23 | -11.93 | 5 |
| final_boosting | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| final_boosting | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| final_boosting | FPL | elliott | 9.68 | -16.11 | -16.11 | -23.65 | 5 |
| final_boosting | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| final_boosting | NYIS | elliott | 2.84 | -0.19 | -1.30 | -3.59 | 5 |
| final_boosting | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| final_boosting | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| final_boosting | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |
| final_ensemble | BPAT | elliott | 4.21 | -3.47 | -3.90 | -8.35 | 5 |
| final_ensemble | DUK | elliott | 3.71 | -3.00 | -3.00 | -3.88 | 4 |
| final_ensemble | ERCO | elliott | 6.73 | -4.28 | -5.36 | -12.60 | 5 |
| final_ensemble | FPL | elliott | 8.81 | -10.29 | -10.53 | -14.82 | 5 |
| final_ensemble | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| final_ensemble | NYIS | elliott | 2.73 | -1.04 | -1.83 | -3.53 | 5 |
| final_ensemble | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| final_ensemble | SWPP | elliott | 4.12 | -2.20 | -3.22 | -7.26 | 5 |
| final_ensemble | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | final2 | eve | 3.52 | 0.67 | -1.61 | 0.47 | 219 |
| 5 | DF | eve | 3.60 | 0.10 | -1.64 |  | 219 |
| 9 | final_ensemble | eve | 3.65 | -0.59 | -2.24 | 0.49 | 219 |
| 8 | final_boosting | eve | 3.85 | -0.51 | -2.34 | 0.45 | 219 |
| 7 | final_additive | eve | 3.87 | -0.66 | -2.41 | 0.44 | 219 |
| 1 | final2 | special | 3.37 | -0.64 | -2.08 | 0.60 | 221 |
| 4 | final_ensemble | special | 3.60 | -1.93 | -2.95 | 0.57 | 221 |
| 2 | final_additive | special | 3.79 | -2.10 | -3.14 | 0.52 | 221 |
| 3 | final_boosting | special | 3.93 | -1.75 | -3.02 | 0.47 | 221 |
| 0 | DF | special | 4.03 | -0.30 | -1.97 |  | 221 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.409 | 1.374 | 0.411 | 0.889 | 12.015 | 0.887 | 6474 |
| final2 | events | 0.529 | 2.058 | 0.621 | 0.765 | 12.674 | 0.800 | 85 |
| final2 | cold_mornings | 0.508 | 1.770 | 0.512 | 0.833 | 13.436 | 0.789 | 270 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 7469 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 7468 | DUK | 2022-12-24 | final2 | 8.29 | -11.33 | -11.33 |
| 7465 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 7466 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 7467 | DUK | 2022-12-24 | final_ensemble | 8.26 | -14.16 | -14.16 |
| 7879 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 7878 | ERCO | 2021-02-15 | final2 | 33.45 | -10.91 | -10.91 |
| 7875 | ERCO | 2021-02-15 | final_additive | 41.72 | -4.24 | -4.24 |
| 7876 | ERCO | 2021-02-15 | final_boosting | 27.39 | -16.57 | -16.57 |
| 7877 | ERCO | 2021-02-15 | final_ensemble | 34.57 | -10.39 | -10.39 |
| 7884 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 7883 | ERCO | 2021-02-16 | final2 | 39.54 | 37.98 | 0.00 |
| 7880 | ERCO | 2021-02-16 | final_additive | 47.08 | 43.33 | 0.00 |
| 7881 | ERCO | 2021-02-16 | final_boosting | 33.46 | 31.10 | 0.00 |
| 7882 | ERCO | 2021-02-16 | final_ensemble | 40.43 | 37.36 | 0.00 |
| 7889 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 7888 | ERCO | 2021-02-17 | final2 | 29.35 | 23.99 | 0.00 |
| 7885 | ERCO | 2021-02-17 | final_additive | 31.74 | 29.84 | 0.00 |
| 7886 | ERCO | 2021-02-17 | final_boosting | 28.91 | 24.01 | 0.00 |
| 7887 | ERCO | 2021-02-17 | final_ensemble | 30.28 | 26.83 | 0.00 |
| 7894 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 7893 | ERCO | 2021-02-18 | final2 | 7.05 | 5.55 | 0.00 |
| 7890 | ERCO | 2021-02-18 | final_additive | 13.46 | 12.91 | 0.00 |
| 7891 | ERCO | 2021-02-18 | final_boosting | 3.58 | -2.96 | -2.96 |
| 7892 | ERCO | 2021-02-18 | final_ensemble | 7.68 | 4.44 | 0.00 |
| 15134 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 15133 | MISO | 2021-02-16 | final2 | 2.57 | 2.89 | 0.00 |
| 15130 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 15131 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 15132 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 26344 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 26343 | SWPP | 2021-02-15 | final2 | 1.83 | -1.71 | -1.71 |
| 26340 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 26341 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 26342 | SWPP | 2021-02-15 | final_ensemble | 2.21 | -3.25 | -3.25 |
| 26349 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 26348 | SWPP | 2021-02-16 | final2 | 6.21 | -0.62 | -0.62 |
| 26345 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 26346 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |
| 26347 | SWPP | 2021-02-16 | final_ensemble | 5.49 | -1.39 | -1.39 |
| 33379 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 33378 | TVA | 2022-12-23 | final2 | 10.26 | -11.56 | -11.56 |
| 33375 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 33376 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 33377 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 33384 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 33383 | TVA | 2022-12-24 | final2 | 4.45 | -11.23 | -11.23 |
| 33380 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 33381 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 33382 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | BPAT | mape | 8.954 | 0.000 | 750 |
| final2 | DUK | mape | 7.740 | 0.000 | 750 |
| final2 | ERCO | mape | 2.537 | 0.011 | 746 |
| final2 | FPL | mape | -1.835 | 0.066 | 700 |
| final2 | MISO | mape | -8.862 | 0.000 | 746 |
| final2 | NYIS | mape | -2.877 | 0.004 | 752 |
| final2 | PJM | mape | -26.312 | 0.000 | 744 |
| final2 | SWPP | mape | -16.252 | 0.000 | 747 |
| final2 | TVA | mape | 13.923 | 0.000 | 739 |
| final_additive | BPAT | mape | 12.541 | 0.000 | 750 |
| final_additive | DUK | mape | 10.152 | 0.000 | 750 |
| final_additive | ERCO | mape | 11.907 | 0.000 | 746 |
| final_additive | FPL | mape | 17.271 | 0.000 | 700 |
| final_additive | MISO | mape | -2.885 | 0.004 | 746 |
| final_additive | NYIS | mape | 0.771 | 0.441 | 752 |
| final_additive | PJM | mape | -14.911 | 0.000 | 744 |
| final_additive | SWPP | mape | -14.397 | 0.000 | 747 |
| final_additive | TVA | mape | 17.307 | 0.000 | 739 |
| final_boosting | BPAT | mape | 12.457 | 0.000 | 750 |
| final_boosting | DUK | mape | 10.290 | 0.000 | 750 |
| final_boosting | ERCO | mape | 6.704 | 0.000 | 746 |
| final_boosting | FPL | mape | 21.017 | 0.000 | 700 |
| final_boosting | MISO | mape | -3.438 | 0.001 | 746 |
| final_boosting | NYIS | mape | 0.532 | 0.595 | 752 |
| final_boosting | PJM | mape | -14.855 | 0.000 | 744 |
| final_boosting | SWPP | mape | -11.406 | 0.000 | 747 |
| final_boosting | TVA | mape | 16.453 | 0.000 | 739 |
| final_ensemble | BPAT | mape | 9.782 | 0.000 | 750 |
| final_ensemble | DUK | mape | 8.508 | 0.000 | 750 |
| final_ensemble | ERCO | mape | 6.848 | 0.000 | 746 |
| final_ensemble | FPL | mape | 18.299 | 0.000 | 700 |
| final_ensemble | MISO | mape | -6.116 | 0.000 | 746 |
| final_ensemble | NYIS | mape | -2.860 | 0.004 | 752 |
| final_ensemble | PJM | mape | -19.327 | 0.000 | 744 |
| final_ensemble | SWPP | mape | -15.215 | 0.000 | 747 |
| final_ensemble | TVA | mape | 14.766 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.992 |
| final2 | 0.991 |
| final_additive | 0.980 |
| final_boosting | 0.991 |
| final_ensemble | 0.991 |
