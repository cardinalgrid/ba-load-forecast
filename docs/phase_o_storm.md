# Phase O: a storm member

Development BAs: DUK, ERCO, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `final9` is the phase N recipe with one more ensemble member: a boosting model fitted on the days of the training window whose observed minimum is in the coldest decile (at least 40 such days), which answers only on a target day whose forecast minimum is at or below that threshold and is left out of the ensemble on every other day; its weight in the ensemble comes from its recent error like the others' (the mean of the others' when it has no record). Compare with `docs/phase_n_weights3_q.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final9 | 2.61 | 2.15 | -0.49 | -1.46 | 1.48 | 0.51 | 0.31 | -12.63 | 558 | 6.00 |
| final9_ensemble | 2.68 | 2.22 | -1.63 | -2.17 | 1.46 | 0.50 | 0.25 | -13.99 | 558 | 6.00 |
| DF | 2.73 | 2.33 | -0.19 | -1.21 | 1.40 | 0.00 | 0.00 | -14.36 | 558 | 6.00 |
| final9_additive | 2.87 | 2.43 | -1.34 | -2.07 | 1.76 | 0.44 | 0.25 | -16.21 | 558 | 6.00 |
| final9_boosting | 2.90 | 2.56 | -1.66 | -2.31 | 1.67 | 0.44 | 0.24 | -17.43 | 558 | 6.00 |
| final9_storm | 3.04 | 2.55 | -1.60 | -2.38 | 1.93 | 0.42 | 0.23 | -19.16 | 558 | 6.00 |
| final9_recency | 3.27 | 2.74 | -1.95 | -2.61 | 2.27 | 0.37 | 0.26 | -19.04 | 558 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 3.31 | 3.06 | -1.43 | -2.34 | 0.60 | -13.32 |  |  | 86 | 13623.94 |
| DF | ERCO | 3.49 | 2.55 | -0.45 | -1.80 | 0.77 | -14.36 |  |  | 94 | 46909.64 |
| DF | MISO | 2.56 | 2.27 | 0.86 | -0.60 | 1.81 | -6.70 |  |  | 100 | 79049.36 |
| DF | PJM | 2.06 | 1.80 | -0.95 | -1.28 | 1.45 | -8.57 |  |  | 101 | 102268.37 |
| DF | SWPP | 3.82 | 3.32 | 0.52 | -1.13 | 1.45 | -7.54 |  |  | 75 | 34004.86 |
| DF | TVA | 2.81 | 2.56 | -0.24 | -1.28 | 1.41 | -7.75 |  |  | 102 | 21419.70 |
| final9 | DUK | 3.37 | 2.97 | 0.07 | -1.71 | 0.91 | -12.63 | 0.55 | 0.42 | 86 | 13623.94 |
| final9 | ERCO | 3.49 | 2.41 | -1.56 | -2.49 | 0.60 | -12.41 | 0.48 | 0.31 | 94 | 46909.64 |
| final9 | MISO | 2.28 | 1.91 | -0.26 | -1.22 | 1.97 | -6.74 | 0.47 | 0.11 | 100 | 79049.36 |
| final9 | PJM | 2.19 | 1.93 | -0.30 | -1.09 | 1.60 | -10.10 | 0.50 | 0.49 | 101 | 102268.37 |
| final9 | SWPP | 2.71 | 2.06 | -0.60 | -1.58 | 1.48 | -8.14 | 0.72 | 0.21 | 75 | 34004.86 |
| final9 | TVA | 3.27 | 3.05 | -0.15 | -1.57 | 1.42 | -10.73 | 0.38 | 0.31 | 102 | 21419.70 |
| final9_additive | DUK | 3.77 | 3.57 | -2.78 | -3.66 | 0.42 | -16.21 | 0.37 | 0.21 | 86 | 13623.94 |
| final9_additive | ERCO | 3.94 | 2.76 | -2.80 | -3.37 | 1.05 | -12.74 | 0.40 | 0.18 | 94 | 46909.64 |
| final9_additive | MISO | 2.28 | 2.06 | -1.29 | -1.74 | 2.20 | -6.60 | 0.54 | 0.09 | 100 | 79049.36 |
| final9_additive | PJM | 2.51 | 2.19 | -0.14 | -1.17 | 2.04 | -11.07 | 0.38 | 0.46 | 101 | 102268.37 |
| final9_additive | SWPP | 3.11 | 2.74 | -2.02 | -2.66 | 1.61 | -10.11 | 0.57 | 0.13 | 75 | 34004.86 |
| final9_additive | TVA | 3.54 | 3.09 | -2.11 | -2.81 | 1.45 | -10.15 | 0.33 | 0.17 | 102 | 21419.70 |
| final9_boosting | DUK | 3.80 | 3.48 | -2.45 | -3.21 | 0.86 | -12.59 | 0.40 | 0.27 | 86 | 13623.94 |
| final9_boosting | ERCO | 3.99 | 3.11 | -4.58 | -4.83 | 1.13 | -17.43 | 0.44 | 0.20 | 94 | 46909.64 |
| final9_boosting | MISO | 2.44 | 2.21 | -0.67 | -1.49 | 1.94 | -6.87 | 0.45 | 0.08 | 100 | 79049.36 |
| final9_boosting | PJM | 2.44 | 2.28 | -0.48 | -1.27 | 1.91 | -9.10 | 0.40 | 0.45 | 101 | 102268.37 |
| final9_boosting | SWPP | 3.13 | 2.78 | -3.13 | -3.42 | 1.55 | -12.42 | 0.61 | 0.08 | 75 | 34004.86 |
| final9_boosting | TVA | 3.48 | 3.00 | -1.67 | -2.44 | 1.46 | -12.55 | 0.35 | 0.20 | 102 | 21419.70 |
| final9_ensemble | DUK | 3.46 | 3.24 | -2.59 | -3.29 | 0.53 | -13.87 | 0.51 | 0.22 | 86 | 13623.94 |
| final9_ensemble | ERCO | 3.70 | 2.61 | -3.85 | -4.11 | 0.65 | -13.99 | 0.45 | 0.17 | 94 | 46909.64 |
| final9_ensemble | MISO | 2.22 | 1.92 | -1.12 | -1.65 | 1.91 | -7.59 | 0.53 | 0.08 | 100 | 79049.36 |
| final9_ensemble | PJM | 2.22 | 1.85 | -0.46 | -1.14 | 1.60 | -9.31 | 0.48 | 0.49 | 101 | 102268.37 |
| final9_ensemble | SWPP | 3.01 | 2.63 | -2.69 | -3.07 | 1.55 | -10.90 | 0.65 | 0.11 | 75 | 34004.86 |
| final9_ensemble | TVA | 3.27 | 2.98 | -2.01 | -2.65 | 1.38 | -10.73 | 0.39 | 0.16 | 102 | 21419.70 |
| final9_recency | DUK | 3.75 | 3.62 | -3.26 | -3.88 | 1.07 | -15.26 | 0.38 | 0.17 | 86 | 13623.94 |
| final9_recency | ERCO | 4.50 | 3.38 | -4.10 | -4.47 | 1.28 | -19.04 | 0.35 | 0.22 | 94 | 46909.64 |
| final9_recency | MISO | 3.06 | 2.56 | -1.77 | -2.26 | 3.07 | -15.59 | 0.36 | 0.11 | 100 | 79049.36 |
| final9_recency | PJM | 2.72 | 2.44 | -0.53 | -1.49 | 2.44 | -16.39 | 0.32 | 0.47 | 101 | 102268.37 |
| final9_recency | SWPP | 3.35 | 2.62 | -2.76 | -3.26 | 2.48 | -13.10 | 0.60 | 0.16 | 75 | 34004.86 |
| final9_recency | TVA | 3.50 | 3.07 | -2.51 | -3.28 | 1.16 | -10.81 | 0.32 | 0.16 | 102 | 21419.70 |
| final9_storm | DUK | 3.51 | 3.15 | -1.94 | -2.73 | 0.78 | -13.59 | 0.48 | 0.33 | 86 | 13623.94 |
| final9_storm | ERCO | 3.94 | 2.74 | -3.91 | -4.33 | 0.81 | -19.16 | 0.38 | 0.20 | 94 | 46909.64 |
| final9_storm | MISO | 2.66 | 2.16 | -0.83 | -1.71 | 2.56 | -9.23 | 0.42 | 0.10 | 100 | 79049.36 |
| final9_storm | PJM | 2.66 | 2.43 | -0.65 | -1.56 | 2.19 | -9.12 | 0.39 | 0.41 | 101 | 102268.37 |
| final9_storm | SWPP | 3.32 | 2.87 | -2.86 | -3.41 | 1.61 | -12.35 | 0.60 | 0.08 | 75 | 34004.86 |
| final9_storm | TVA | 3.59 | 3.21 | -1.71 | -2.58 | 2.07 | -12.40 | 0.29 | 0.18 | 102 | 21419.70 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 8.88 | -10.25 | -10.25 | -10.25 | 1 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final9 | DUK | uri | 2.50 | 0.66 | 0.00 | 0.00 | 1 |
| final9 | ERCO | uri | 6.88 | -9.23 | -9.23 | -9.37 | 2 |
| final9 | MISO | uri | 3.76 | -2.97 | -3.20 | -6.21 | 5 |
| final9 | PJM | uri | 1.67 | -0.65 | -0.79 | -2.55 | 6 |
| final9 | SWPP | uri | 5.79 | 0.50 | -2.41 | -5.79 | 4 |
| final9 | TVA | uri | 3.97 | -1.94 | -2.86 | -7.87 | 6 |
| final9_additive | DUK | uri | 3.77 | -3.13 | -3.13 | -3.13 | 1 |
| final9_additive | ERCO | uri | 5.26 | -6.89 | -6.89 | -9.48 | 2 |
| final9_additive | MISO | uri | 3.65 | -2.66 | -3.20 | -6.58 | 5 |
| final9_additive | PJM | uri | 2.82 | 2.27 | -0.40 | -2.43 | 6 |
| final9_additive | SWPP | uri | 6.11 | 2.05 | -1.66 | -4.46 | 4 |
| final9_additive | TVA | uri | 3.94 | -0.58 | -1.99 | -5.82 | 6 |
| final9_boosting | DUK | uri | 3.98 | -1.88 | -1.88 | -1.88 | 1 |
| final9_boosting | ERCO | uri | 8.66 | -13.62 | -13.62 | -15.74 | 2 |
| final9_boosting | MISO | uri | 2.65 | -2.90 | -2.95 | -5.31 | 5 |
| final9_boosting | PJM | uri | 1.57 | -0.86 | -1.04 | -2.57 | 6 |
| final9_boosting | SWPP | uri | 4.88 | -3.23 | -3.99 | -9.76 | 4 |
| final9_boosting | TVA | uri | 3.13 | -2.41 | -2.41 | -5.95 | 6 |
| final9_ensemble | DUK | uri | 3.63 | -2.26 | -2.26 | -2.26 | 1 |
| final9_ensemble | ERCO | uri | 6.78 | -9.64 | -9.64 | -10.43 | 2 |
| final9_ensemble | MISO | uri | 3.62 | -3.53 | -3.53 | -6.50 | 5 |
| final9_ensemble | PJM | uri | 1.85 | -0.20 | -0.75 | -3.18 | 6 |
| final9_ensemble | SWPP | uri | 5.54 | -1.14 | -3.16 | -7.25 | 4 |
| final9_ensemble | TVA | uri | 3.77 | -2.14 | -2.80 | -7.32 | 6 |
| final9_recency | DUK | uri | 4.51 | -3.90 | -3.90 | -3.90 | 1 |
| final9_recency | ERCO | uri | 6.07 | -5.61 | -5.61 | -10.26 | 2 |
| final9_recency | MISO | uri | 6.74 | -6.06 | -6.06 | -9.68 | 5 |
| final9_recency | PJM | uri | 2.45 | 0.50 | -0.84 | -4.36 | 6 |
| final9_recency | SWPP | uri | 6.47 | -2.75 | -4.55 | -10.56 | 4 |
| final9_recency | TVA | uri | 4.24 | -1.89 | -2.86 | -6.14 | 6 |
| final9_storm | DUK | uri | 2.57 | -0.34 | -0.34 | -0.34 | 1 |
| final9_storm | ERCO | uri | 8.03 | -11.97 | -11.97 | -13.58 | 2 |
| final9_storm | MISO | uri | 3.25 | -2.93 | -2.99 | -5.67 | 5 |
| final9_storm | PJM | uri | 1.98 | -2.31 | -2.31 | -4.15 | 6 |
| final9_storm | SWPP | uri | 4.32 | -1.08 | -2.47 | -7.05 | 4 |
| final9_storm | TVA | uri | 4.52 | -3.67 | -4.28 | -12.40 | 6 |
| DF | DUK | elliott | 4.27 | -4.58 | -4.58 | -10.55 | 3 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.84 | -4.57 | -4.57 | -7.05 | 4 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final9 | DUK | elliott | 3.77 | -1.53 | -2.06 | -6.01 | 3 |
| final9 | ERCO | elliott | 5.97 | -4.39 | -5.16 | -10.89 | 5 |
| final9 | MISO | elliott | 3.65 | -2.53 | -3.41 | -6.74 | 5 |
| final9 | PJM | elliott | 4.65 | -4.52 | -4.52 | -7.83 | 4 |
| final9 | SWPP | elliott | 4.37 | -0.52 | -2.40 | -8.14 | 5 |
| final9 | TVA | elliott | 4.09 | 0.59 | -0.21 | -0.62 | 3 |
| final9_additive | DUK | elliott | 4.38 | -5.47 | -5.47 | -6.30 | 3 |
| final9_additive | ERCO | elliott | 7.53 | -5.95 | -6.29 | -12.74 | 5 |
| final9_additive | MISO | elliott | 3.51 | -3.79 | -4.00 | -6.60 | 5 |
| final9_additive | PJM | elliott | 3.72 | -3.16 | -3.16 | -7.54 | 4 |
| final9_additive | SWPP | elliott | 3.44 | -2.75 | -3.00 | -6.28 | 5 |
| final9_additive | TVA | elliott | 4.73 | -0.54 | -0.59 | -1.27 | 3 |
| final9_boosting | DUK | elliott | 4.70 | -3.32 | -3.32 | -6.28 | 3 |
| final9_boosting | ERCO | elliott | 7.22 | -11.93 | -11.93 | -17.43 | 5 |
| final9_boosting | MISO | elliott | 3.52 | -2.09 | -3.12 | -4.27 | 5 |
| final9_boosting | PJM | elliott | 4.32 | -5.07 | -5.07 | -7.50 | 4 |
| final9_boosting | SWPP | elliott | 4.60 | -3.35 | -4.18 | -12.42 | 5 |
| final9_boosting | TVA | elliott | 4.33 | -2.05 | -2.05 | -3.07 | 3 |
| final9_ensemble | DUK | elliott | 4.23 | -5.01 | -5.01 | -6.63 | 3 |
| final9_ensemble | ERCO | elliott | 6.59 | -8.97 | -8.97 | -13.99 | 5 |
| final9_ensemble | MISO | elliott | 3.60 | -3.72 | -4.18 | -7.59 | 5 |
| final9_ensemble | PJM | elliott | 4.58 | -5.12 | -5.12 | -8.88 | 4 |
| final9_ensemble | SWPP | elliott | 4.15 | -4.01 | -4.39 | -10.90 | 5 |
| final9_ensemble | TVA | elliott | 4.08 | -1.59 | -1.59 | -2.50 | 3 |
| final9_recency | DUK | elliott | 4.58 | -7.43 | -7.43 | -9.35 | 3 |
| final9_recency | ERCO | elliott | 5.48 | -4.79 | -4.79 | -11.25 | 5 |
| final9_recency | MISO | elliott | 6.72 | -7.67 | -7.67 | -15.59 | 5 |
| final9_recency | PJM | elliott | 6.93 | -9.39 | -9.39 | -16.39 | 4 |
| final9_recency | SWPP | elliott | 4.79 | -6.95 | -6.95 | -13.10 | 5 |
| final9_recency | TVA | elliott | 3.83 | -3.80 | -3.80 | -4.81 | 3 |
| final9_storm | DUK | elliott | 4.66 | -3.46 | -3.63 | -8.48 | 3 |
| final9_storm | ERCO | elliott | 8.02 | -12.91 | -12.91 | -19.16 | 5 |
| final9_storm | MISO | elliott | 4.38 | -2.59 | -3.75 | -7.10 | 5 |
| final9_storm | PJM | elliott | 4.77 | -2.91 | -3.51 | -7.86 | 4 |
| final9_storm | SWPP | elliott | 4.92 | -2.89 | -4.06 | -12.35 | 5 |
| final9_storm | TVA | elliott | 4.55 | -0.19 | -0.74 | -2.06 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | final9 | eve | 4.14 | -1.67 | -2.52 | 0.57 | 28 |
| 11 | final9_ensemble | eve | 4.16 | -3.46 | -3.87 | 0.54 | 28 |
| 7 | DF | eve | 4.22 | -1.28 | -2.42 |  | 28 |
| 10 | final9_boosting | eve | 4.35 | -3.35 | -4.00 | 0.54 | 28 |
| 9 | final9_additive | eve | 4.46 | -2.94 | -3.50 | 0.50 | 28 |
| 12 | final9_recency | eve | 4.82 | -4.63 | -5.07 | 0.54 | 28 |
| 13 | final9_storm | eve | 4.94 | -3.17 | -4.05 | 0.43 | 28 |
| 4 | final9_ensemble | special | 3.23 | -2.00 | -2.53 | 0.62 | 40 |
| 1 | final9 | special | 3.38 | -0.23 | -1.37 | 0.65 | 40 |
| 3 | final9_boosting | special | 3.56 | -1.99 | -2.62 | 0.60 | 40 |
| 2 | final9_additive | special | 3.58 | -2.74 | -3.15 | 0.50 | 40 |
| 5 | final9_recency | special | 3.77 | -2.06 | -3.01 | 0.62 | 40 |
| 6 | final9_storm | special | 3.84 | -1.20 | -2.30 | 0.55 | 40 |
| 0 | DF | special | 4.45 | -0.55 | -1.72 |  | 40 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final9 | all | 0.431 | 1.458 | 0.451 | 0.859 | 11.985 | 0.866 | 17.641 | 1.915 | 522 |
| final9 | events | 0.494 | 2.083 | 0.715 | 0.719 | 11.967 | 0.714 | 24.166 | 2.781 | 49 |
| final9 | cold_mornings | 0.482 | 1.706 | 0.586 | 0.811 | 12.922 | 0.783 | 21.373 | 2.283 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 573 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 572 | DUK | 2022-12-24 | final9 | 9.52 | -12.40 | -12.40 |
| 567 | DUK | 2022-12-24 | final9_additive | 8.92 | -12.68 | -12.68 |
| 568 | DUK | 2022-12-24 | final9_boosting | 10.90 | -17.09 | -17.09 |
| 571 | DUK | 2022-12-24 | final9_ensemble | 9.93 | -14.65 | -14.65 |
| 570 | DUK | 2022-12-24 | final9_recency | 10.63 | -11.43 | -11.43 |
| 569 | DUK | 2022-12-24 | final9_storm | 9.49 | -17.11 | -17.11 |
| 867 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 866 | ERCO | 2021-02-17 | final9 | 30.93 | 24.23 | 0.00 |
| 861 | ERCO | 2021-02-17 | final9_additive | 29.56 | 25.22 | 0.00 |
| 862 | ERCO | 2021-02-17 | final9_boosting | 28.85 | 23.03 | 0.00 |
| 865 | ERCO | 2021-02-17 | final9_ensemble | 30.73 | 25.06 | 0.00 |
| 864 | ERCO | 2021-02-17 | final9_recency | 38.48 | 31.79 | 0.00 |
| 863 | ERCO | 2021-02-17 | final9_storm | 26.68 | 20.60 | 0.00 |
| 874 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 873 | ERCO | 2021-02-18 | final9 | 4.87 | 2.84 | 0.00 |
| 868 | ERCO | 2021-02-18 | final9_additive | 13.29 | 11.84 | 0.00 |
| 869 | ERCO | 2021-02-18 | final9_boosting | 4.23 | -7.71 | -7.71 |
| 872 | ERCO | 2021-02-18 | final9_ensemble | 4.75 | 1.33 | 0.00 |
| 871 | ERCO | 2021-02-18 | final9_recency | 5.36 | 2.19 | 0.00 |
| 870 | ERCO | 2021-02-18 | final9_storm | 6.62 | 0.59 | 0.00 |
| 1539 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 1538 | MISO | 2021-02-16 | final9 | 1.70 | 1.38 | 0.00 |
| 1533 | MISO | 2021-02-16 | final9_additive | 2.24 | 2.04 | 0.00 |
| 1534 | MISO | 2021-02-16 | final9_boosting | 1.52 | 0.96 | 0.00 |
| 1537 | MISO | 2021-02-16 | final9_ensemble | 1.54 | 0.18 | 0.00 |
| 1536 | MISO | 2021-02-16 | final9_recency | 3.83 | -2.20 | -2.20 |
| 1535 | MISO | 2021-02-16 | final9_storm | 1.71 | -0.90 | -0.90 |
| 2848 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 2847 | SWPP | 2021-02-15 | final9 | 2.48 | -2.74 | -2.74 |
| 2842 | SWPP | 2021-02-15 | final9_additive | 2.57 | 1.33 | 0.00 |
| 2843 | SWPP | 2021-02-15 | final9_boosting | 6.68 | -8.01 | -8.01 |
| 2846 | SWPP | 2021-02-15 | final9_ensemble | 3.07 | -4.32 | -4.32 |
| 2845 | SWPP | 2021-02-15 | final9_recency | 4.67 | -4.95 | -4.95 |
| 2844 | SWPP | 2021-02-15 | final9_storm | 4.42 | -6.93 | -6.93 |
| 2855 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 2854 | SWPP | 2021-02-16 | final9 | 4.18 | -0.56 | -0.56 |
| 2849 | SWPP | 2021-02-16 | final9_additive | 7.69 | 3.65 | 0.00 |
| 2850 | SWPP | 2021-02-16 | final9_boosting | 3.28 | -6.32 | -6.32 |
| 2853 | SWPP | 2021-02-16 | final9_ensemble | 3.86 | -1.64 | -1.64 |
| 2852 | SWPP | 2021-02-16 | final9_recency | 2.38 | -0.44 | -0.44 |
| 2851 | SWPP | 2021-02-16 | final9_storm | 4.08 | -4.74 | -4.74 |
| 3926 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 3925 | TVA | 2022-12-23 | final9 | 10.07 | -11.78 | -11.78 |
| 3920 | TVA | 2022-12-23 | final9_additive | 6.10 | -4.61 | -4.61 |
| 3921 | TVA | 2022-12-23 | final9_boosting | 15.03 | -15.47 | -15.47 |
| 3924 | TVA | 2022-12-23 | final9_ensemble | 10.16 | -11.85 | -11.85 |
| 3923 | TVA | 2022-12-23 | final9_recency | 10.25 | -13.32 | -13.32 |
| 3922 | TVA | 2022-12-23 | final9_storm | 11.16 | -13.92 | -13.92 |
| 3933 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 3932 | TVA | 2022-12-24 | final9 | 5.41 | -13.07 | -13.07 |
| 3927 | TVA | 2022-12-24 | final9_additive | 4.10 | -10.03 | -10.03 |
| 3928 | TVA | 2022-12-24 | final9_boosting | 7.18 | -15.19 | -15.19 |
| 3931 | TVA | 2022-12-24 | final9_ensemble | 5.70 | -12.50 | -12.50 |
| 3930 | TVA | 2022-12-24 | final9_recency | 7.90 | -12.89 | -12.89 |
| 3929 | TVA | 2022-12-24 | final9_storm | 4.93 | -12.18 | -12.18 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final9 | DUK | mape | 0.314 | 0.753 | 86 |
| final9 | ERCO | mape | -0.004 | 0.997 | 94 |
| final9 | MISO | mape | -1.565 | 0.118 | 100 |
| final9 | PJM | mape | 0.945 | 0.345 | 101 |
| final9 | SWPP | mape | -4.624 | 0.000 | 75 |
| final9 | TVA | mape | 3.131 | 0.002 | 102 |
| final9_additive | DUK | mape | 2.078 | 0.038 | 86 |
| final9_additive | ERCO | mape | 1.861 | 0.063 | 94 |
| final9_additive | MISO | mape | -1.459 | 0.145 | 100 |
| final9_additive | PJM | mape | 2.914 | 0.004 | 101 |
| final9_additive | SWPP | mape | -2.667 | 0.008 | 75 |
| final9_additive | TVA | mape | 4.360 | 0.000 | 102 |
| final9_boosting | DUK | mape | 2.214 | 0.027 | 86 |
| final9_boosting | ERCO | mape | 1.932 | 0.053 | 94 |
| final9_boosting | MISO | mape | -0.735 | 0.462 | 100 |
| final9_boosting | PJM | mape | 2.369 | 0.018 | 101 |
| final9_boosting | SWPP | mape | -2.145 | 0.032 | 75 |
| final9_boosting | TVA | mape | 4.106 | 0.000 | 102 |
| final9_ensemble | DUK | mape | 0.723 | 0.470 | 86 |
| final9_ensemble | ERCO | mape | 0.828 | 0.408 | 94 |
| final9_ensemble | MISO | mape | -1.798 | 0.072 | 100 |
| final9_ensemble | PJM | mape | 1.068 | 0.285 | 101 |
| final9_ensemble | SWPP | mape | -2.702 | 0.007 | 75 |
| final9_ensemble | TVA | mape | 3.051 | 0.002 | 102 |
| final9_recency | DUK | mape | 2.143 | 0.032 | 86 |
| final9_recency | ERCO | mape | 3.350 | 0.001 | 94 |
| final9_recency | MISO | mape | 2.002 | 0.045 | 100 |
| final9_recency | PJM | mape | 3.755 | 0.000 | 101 |
| final9_recency | SWPP | mape | -1.475 | 0.140 | 75 |
| final9_recency | TVA | mape | 4.124 | 0.000 | 102 |
| final9_storm | DUK | mape | 0.851 | 0.395 | 86 |
| final9_storm | ERCO | mape | 1.736 | 0.083 | 94 |
| final9_storm | MISO | mape | 0.554 | 0.580 | 100 |
| final9_storm | PJM | mape | 3.458 | 0.001 | 101 |
| final9_storm | SWPP | mape | -1.625 | 0.104 | 75 |
| final9_storm | TVA | mape | 4.755 | 0.000 | 102 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.995 |
| final9 | 0.994 |
| final9_additive | 0.976 |
| final9_boosting | 0.994 |
| final9_ensemble | 0.994 |
| final9_recency | 0.994 |
| final9_storm | 0.126 |
