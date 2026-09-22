# Phase G: parameters

Development BAs: DUK, PJM, SWPP, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). Boosting: `deep` 800 iterations at rate 0.03 with 63 leaves; `shallow` 300 iterations, 15 leaves, 50 samples per leaf; `l2` regularisation 1.0; `refit3` refitted every 3 days; `7y` trained on 2555 days. Additive: 8 and 10 knots; 90 validation days; a penalty grid from 0.001 to 1000; 2555 training days.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 2.79 | 2.55 | 0.18 | -1.09 | 1.09 | 0.00 | 0.00 | -19.98 | 2239 | 3.00 |
| additive_7y | 2.80 | 2.45 | -0.59 | -1.82 | 1.65 | 0.48 | 0.30 | -20.30 | 2239 | 3.00 |
| final_additive | 2.81 | 2.45 | -0.58 | -1.82 | 1.68 | 0.48 | 0.30 | -20.36 | 2239 | 3.00 |
| additive_k8 | 2.81 | 2.45 | -0.60 | -1.83 | 1.69 | 0.47 | 0.30 | -21.08 | 2239 | 3.00 |
| additive_val90 | 2.81 | 2.45 | -0.55 | -1.81 | 1.69 | 0.47 | 0.30 | -20.36 | 2239 | 3.00 |
| boosting_deep | 2.81 | 2.46 | 0.02 | -1.53 | 1.66 | 0.48 | 0.35 | -28.42 | 2239 | 3.00 |
| additive_k10 | 2.81 | 2.45 | -0.63 | -1.86 | 1.69 | 0.47 | 0.30 | -21.53 | 2239 | 3.00 |
| additive_lam | 2.82 | 2.46 | -0.61 | -1.84 | 1.67 | 0.47 | 0.30 | -20.36 | 2239 | 3.00 |
| boosting_refit3 | 2.83 | 2.49 | -0.18 | -1.64 | 1.70 | 0.47 | 0.32 | -21.10 | 2239 | 3.00 |
| boosting_7y | 2.85 | 2.51 | -0.18 | -1.62 | 1.74 | 0.47 | 0.33 | -28.75 | 2239 | 3.00 |
| boosting_l2 | 2.85 | 2.48 | -0.16 | -1.63 | 1.66 | 0.46 | 0.34 | -27.46 | 2239 | 3.00 |
| final_boosting | 2.86 | 2.51 | -0.16 | -1.63 | 1.76 | 0.47 | 0.33 | -28.44 | 2239 | 3.00 |
| boosting_shallow | 2.93 | 2.58 | -0.53 | -1.83 | 1.76 | 0.45 | 0.31 | -27.40 | 2239 | 3.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 750 | 12129.97 |
| DF | PJM | 2.45 | 2.23 | -0.60 | -1.27 | 1.04 | -8.98 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.21 | -19.98 |  |  | 745 | 31350.31 |
| additive_7y | DUK | 3.56 | 3.15 | -0.71 | -2.38 | 1.39 | -14.80 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_7y | PJM | 2.80 | 2.47 | -0.67 | -1.83 | 1.74 | -12.08 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_7y | SWPP | 2.52 | 2.10 | -0.29 | -1.59 | 1.50 | -20.30 | 0.70 | 0.10 | 745 | 31350.31 |
| additive_k10 | DUK | 3.58 | 3.12 | -0.68 | -2.38 | 1.46 | -14.79 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_k10 | PJM | 2.81 | 2.47 | -0.74 | -1.88 | 1.76 | -12.34 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_k10 | SWPP | 2.54 | 2.11 | -0.31 | -1.61 | 1.57 | -21.53 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_k8 | DUK | 3.57 | 3.13 | -0.69 | -2.38 | 1.42 | -14.72 | 0.35 | 0.27 | 750 | 12129.97 |
| additive_k8 | PJM | 2.81 | 2.48 | -0.68 | -1.84 | 1.78 | -12.39 | 0.41 | 0.37 | 744 | 91927.69 |
| additive_k8 | SWPP | 2.52 | 2.10 | -0.32 | -1.61 | 1.55 | -21.08 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_lam | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| additive_lam | PJM | 2.82 | 2.48 | -0.70 | -1.85 | 1.76 | -12.10 | 0.42 | 0.37 | 744 | 91927.69 |
| additive_lam | SWPP | 2.54 | 2.14 | -0.30 | -1.61 | 1.51 | -20.36 | 0.69 | 0.10 | 745 | 31350.31 |
| additive_val90 | DUK | 3.57 | 3.15 | -0.67 | -2.36 | 1.44 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| additive_val90 | PJM | 2.81 | 2.47 | -0.63 | -1.80 | 1.79 | -12.13 | 0.42 | 0.38 | 744 | 91927.69 |
| additive_val90 | SWPP | 2.53 | 2.11 | -0.30 | -1.60 | 1.50 | -20.36 | 0.69 | 0.10 | 745 | 31350.31 |
| boosting_7y | DUK | 3.57 | 3.09 | -0.38 | -2.24 | 1.47 | -15.99 | 0.34 | 0.28 | 750 | 12129.97 |
| boosting_7y | PJM | 2.82 | 2.54 | 0.07 | -1.43 | 1.81 | -11.43 | 0.41 | 0.43 | 744 | 91927.69 |
| boosting_7y | SWPP | 2.65 | 2.19 | -0.85 | -1.94 | 1.64 | -28.75 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_deep | DUK | 3.52 | 3.07 | -0.27 | -2.16 | 1.39 | -18.31 | 0.36 | 0.29 | 750 | 12129.97 |
| boosting_deep | PJM | 2.79 | 2.49 | 0.28 | -1.34 | 1.74 | -12.43 | 0.43 | 0.44 | 744 | 91927.69 |
| boosting_deep | SWPP | 2.60 | 2.11 | -0.64 | -1.84 | 1.51 | -28.42 | 0.68 | 0.09 | 745 | 31350.31 |
| boosting_l2 | DUK | 3.56 | 3.10 | -0.40 | -2.24 | 1.52 | -17.15 | 0.34 | 0.28 | 750 | 12129.97 |
| boosting_l2 | PJM | 2.83 | 2.51 | 0.12 | -1.43 | 1.71 | -11.30 | 0.40 | 0.43 | 744 | 91927.69 |
| boosting_l2 | SWPP | 2.64 | 2.14 | -0.89 | -2.00 | 1.58 | -27.46 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_refit3 | DUK | 3.53 | 3.04 | -0.44 | -2.25 | 1.43 | -16.41 | 0.36 | 0.27 | 750 | 12129.97 |
| boosting_refit3 | PJM | 2.82 | 2.53 | 0.04 | -1.48 | 1.79 | -10.57 | 0.41 | 0.41 | 744 | 91927.69 |
| boosting_refit3 | SWPP | 2.59 | 2.18 | -0.75 | -1.85 | 1.54 | -21.10 | 0.68 | 0.08 | 745 | 31350.31 |
| boosting_shallow | DUK | 3.67 | 3.19 | -0.83 | -2.52 | 1.58 | -15.68 | 0.31 | 0.26 | 750 | 12129.97 |
| boosting_shallow | PJM | 2.89 | 2.60 | -0.30 | -1.62 | 1.76 | -12.08 | 0.40 | 0.39 | 744 | 91927.69 |
| boosting_shallow | SWPP | 2.75 | 2.29 | -1.12 | -2.18 | 1.80 | -27.40 | 0.66 | 0.08 | 745 | 31350.31 |
| final_additive | DUK | 3.57 | 3.15 | -0.71 | -2.38 | 1.42 | -14.75 | 0.34 | 0.27 | 750 | 12129.97 |
| final_additive | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.42 | 0.37 | 744 | 91927.69 |
| final_additive | SWPP | 2.53 | 2.11 | -0.29 | -1.59 | 1.50 | -20.36 | 0.70 | 0.10 | 745 | 31350.31 |
| final_boosting | DUK | 3.58 | 3.12 | -0.42 | -2.27 | 1.50 | -16.82 | 0.33 | 0.27 | 750 | 12129.97 |
| final_boosting | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.41 | 0.42 | 744 | 91927.69 |
| final_boosting | SWPP | 2.67 | 2.18 | -0.92 | -1.99 | 1.65 | -28.44 | 0.68 | 0.08 | 745 | 31350.31 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| additive_7y | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| additive_7y | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_7y | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_k10 | DUK | uri | 3.43 | -2.65 | -2.65 | -8.06 | 6 |
| additive_k10 | PJM | uri | 2.85 | 2.13 | -0.51 | -2.87 | 6 |
| additive_k10 | SWPP | uri | 6.39 | 2.32 | -1.42 | -4.79 | 4 |
| additive_k8 | DUK | uri | 3.44 | -2.69 | -2.69 | -8.13 | 6 |
| additive_k8 | PJM | uri | 2.91 | 2.14 | -0.51 | -2.73 | 6 |
| additive_k8 | SWPP | uri | 6.41 | 2.12 | -1.59 | -4.88 | 4 |
| additive_lam | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| additive_lam | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_lam | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| additive_val90 | DUK | uri | 3.46 | -2.66 | -2.66 | -8.00 | 6 |
| additive_val90 | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| additive_val90 | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| boosting_7y | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_7y | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_7y | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_deep | DUK | uri | 3.37 | -2.88 | -2.88 | -6.14 | 6 |
| boosting_deep | PJM | uri | 2.08 | -0.26 | -0.96 | -3.04 | 6 |
| boosting_deep | SWPP | uri | 5.67 | -2.01 | -3.75 | -9.43 | 4 |
| boosting_l2 | DUK | uri | 3.54 | -2.85 | -2.85 | -4.87 | 6 |
| boosting_l2 | PJM | uri | 1.91 | -1.27 | -1.33 | -3.21 | 6 |
| boosting_l2 | SWPP | uri | 5.60 | -2.32 | -3.99 | -9.71 | 4 |
| boosting_refit3 | DUK | uri | 3.49 | -3.13 | -3.13 | -6.25 | 6 |
| boosting_refit3 | PJM | uri | 2.15 | -1.25 | -1.47 | -3.84 | 6 |
| boosting_refit3 | SWPP | uri | 6.27 | -1.08 | -3.58 | -9.16 | 4 |
| boosting_shallow | DUK | uri | 4.01 | -4.47 | -4.47 | -6.52 | 6 |
| boosting_shallow | PJM | uri | 1.97 | -1.81 | -1.81 | -4.72 | 6 |
| boosting_shallow | SWPP | uri | 6.20 | -4.19 | -5.14 | -11.42 | 4 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| final_boosting | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| additive_7y | DUK | elliott | 4.21 | -2.34 | -2.58 | -5.69 | 4 |
| additive_7y | PJM | elliott | 3.63 | -1.97 | -2.52 | -6.73 | 5 |
| additive_7y | SWPP | elliott | 3.61 | -2.38 | -2.94 | -6.77 | 5 |
| additive_k10 | DUK | elliott | 3.90 | -1.20 | -2.17 | -4.37 | 4 |
| additive_k10 | PJM | elliott | 3.79 | -2.24 | -2.88 | -7.38 | 5 |
| additive_k10 | SWPP | elliott | 3.96 | -2.96 | -3.46 | -6.99 | 5 |
| additive_k8 | DUK | elliott | 3.96 | -2.07 | -2.41 | -5.23 | 4 |
| additive_k8 | PJM | elliott | 3.74 | -2.15 | -2.77 | -7.12 | 5 |
| additive_k8 | SWPP | elliott | 3.78 | -2.73 | -3.18 | -6.73 | 5 |
| additive_lam | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| additive_lam | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| additive_lam | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| additive_val90 | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| additive_val90 | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| additive_val90 | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| boosting_7y | DUK | elliott | 4.13 | -3.57 | -3.57 | -6.38 | 4 |
| boosting_7y | PJM | elliott | 5.02 | -2.24 | -3.07 | -6.54 | 5 |
| boosting_7y | SWPP | elliott | 4.76 | -1.16 | -3.31 | -10.61 | 5 |
| boosting_deep | DUK | elliott | 4.22 | -3.42 | -3.45 | -7.78 | 4 |
| boosting_deep | PJM | elliott | 5.10 | -1.06 | -2.74 | -5.99 | 5 |
| boosting_deep | SWPP | elliott | 5.34 | -0.91 | -3.63 | -11.08 | 5 |
| boosting_l2 | DUK | elliott | 4.43 | -3.90 | -3.90 | -7.25 | 4 |
| boosting_l2 | PJM | elliott | 5.30 | -1.73 | -3.05 | -5.70 | 5 |
| boosting_l2 | SWPP | elliott | 4.88 | -1.91 | -3.82 | -10.98 | 5 |
| boosting_refit3 | DUK | elliott | 4.02 | -2.66 | -2.66 | -7.02 | 4 |
| boosting_refit3 | PJM | elliott | 5.29 | -2.34 | -3.28 | -6.65 | 5 |
| boosting_refit3 | SWPP | elliott | 4.14 | -3.53 | -4.21 | -10.54 | 5 |
| boosting_shallow | DUK | elliott | 4.27 | -5.59 | -5.59 | -9.46 | 4 |
| boosting_shallow | PJM | elliott | 4.92 | -3.07 | -3.66 | -8.09 | 5 |
| boosting_shallow | SWPP | elliott | 4.44 | -2.13 | -3.52 | -10.33 | 5 |
| final_additive | DUK | elliott | 4.00 | -2.64 | -2.64 | -5.19 | 4 |
| final_additive | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| final_additive | SWPP | elliott | 3.62 | -2.55 | -2.95 | -6.74 | 5 |
| final_boosting | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| final_boosting | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| final_boosting | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | additive_k8 | eve | 3.53 | 0.54 | -1.55 | 0.52 | 73 |
| 14 | additive_7y | eve | 3.54 | 0.57 | -1.54 | 0.55 | 73 |
| 17 | additive_lam | eve | 3.54 | 0.53 | -1.57 | 0.53 | 73 |
| 24 | final_additive | eve | 3.54 | 0.56 | -1.55 | 0.53 | 73 |
| 18 | additive_val90 | eve | 3.55 | 0.54 | -1.56 | 0.52 | 73 |
| 15 | additive_k10 | eve | 3.56 | 0.61 | -1.51 | 0.55 | 73 |
| 22 | boosting_refit3 | eve | 3.76 | 0.66 | -1.54 | 0.52 | 73 |
| 13 | DF | eve | 3.89 | 2.15 | -0.75 |  | 73 |
| 23 | boosting_shallow | eve | 3.90 | 0.59 | -1.74 | 0.53 | 73 |
| 19 | boosting_7y | eve | 3.91 | 1.10 | -1.44 | 0.48 | 73 |
| 25 | final_boosting | eve | 3.92 | 0.95 | -1.52 | 0.51 | 73 |
| 20 | boosting_deep | eve | 3.94 | 1.46 | -1.27 | 0.52 | 73 |
| 21 | boosting_l2 | eve | 3.95 | 0.98 | -1.54 | 0.48 | 73 |
| 1 | additive_7y | special | 3.31 | -0.67 | -2.09 | 0.61 | 74 |
| 11 | final_additive | special | 3.33 | -0.63 | -2.06 | 0.61 | 74 |
| 4 | additive_lam | special | 3.34 | -0.66 | -2.06 | 0.61 | 74 |
| 5 | additive_val90 | special | 3.34 | -0.62 | -2.05 | 0.61 | 74 |
| 2 | additive_k10 | special | 3.34 | -0.59 | -2.05 | 0.59 | 74 |
| 3 | additive_k8 | special | 3.34 | -0.60 | -2.06 | 0.58 | 74 |
| 12 | final_boosting | special | 3.90 | -0.12 | -1.98 | 0.54 | 74 |
| 8 | boosting_l2 | special | 3.91 | -0.17 | -2.00 | 0.54 | 74 |
| 6 | boosting_7y | special | 3.92 | -0.15 | -1.90 | 0.53 | 74 |
| 9 | boosting_refit3 | special | 3.94 | -0.42 | -2.07 | 0.54 | 74 |
| 7 | boosting_deep | special | 3.97 | 0.38 | -1.77 | 0.55 | 74 |
| 10 | boosting_shallow | special | 4.05 | -0.65 | -2.34 | 0.50 | 74 |
| 0 | DF | special | 4.47 | 1.66 | -0.98 |  | 74 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 9671 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 9670 | DUK | 2022-12-24 | additive_7y | 7.30 | -12.87 | -12.87 |
| 9667 | DUK | 2022-12-24 | additive_k10 | 7.69 | -13.17 | -13.17 |
| 9666 | DUK | 2022-12-24 | additive_k8 | 7.68 | -13.38 | -13.38 |
| 9669 | DUK | 2022-12-24 | additive_lam | 7.26 | -12.67 | -12.67 |
| 9668 | DUK | 2022-12-24 | additive_val90 | 7.26 | -12.67 | -12.67 |
| 9665 | DUK | 2022-12-24 | boosting_7y | 9.86 | -16.76 | -16.76 |
| 9661 | DUK | 2022-12-24 | boosting_deep | 9.55 | -18.81 | -18.81 |
| 9663 | DUK | 2022-12-24 | boosting_l2 | 9.53 | -16.92 | -16.92 |
| 9664 | DUK | 2022-12-24 | boosting_refit3 | 9.53 | -16.59 | -16.59 |
| 9662 | DUK | 2022-12-24 | boosting_shallow | 11.57 | -20.37 | -20.37 |
| 9659 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 9660 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 20409 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 20408 | SWPP | 2021-02-15 | additive_7y | 2.66 | 1.09 | 0.00 |
| 20405 | SWPP | 2021-02-15 | additive_k10 | 3.99 | 2.82 | 0.00 |
| 20404 | SWPP | 2021-02-15 | additive_k8 | 3.66 | 2.48 | 0.00 |
| 20407 | SWPP | 2021-02-15 | additive_lam | 2.66 | 1.09 | 0.00 |
| 20406 | SWPP | 2021-02-15 | additive_val90 | 2.66 | 1.09 | 0.00 |
| 20403 | SWPP | 2021-02-15 | boosting_7y | 5.58 | -7.79 | -7.79 |
| 20399 | SWPP | 2021-02-15 | boosting_deep | 5.50 | -7.96 | -7.96 |
| 20401 | SWPP | 2021-02-15 | boosting_l2 | 5.02 | -7.10 | -7.10 |
| 20402 | SWPP | 2021-02-15 | boosting_refit3 | 4.26 | -6.83 | -6.83 |
| 20400 | SWPP | 2021-02-15 | boosting_shallow | 5.04 | -7.81 | -7.81 |
| 20397 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 20398 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 20422 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 20421 | SWPP | 2021-02-16 | additive_7y | 8.09 | 3.29 | 0.00 |
| 20418 | SWPP | 2021-02-16 | additive_k10 | 9.53 | 4.85 | 0.00 |
| 20417 | SWPP | 2021-02-16 | additive_k8 | 9.20 | 4.60 | 0.00 |
| 20420 | SWPP | 2021-02-16 | additive_lam | 8.09 | 3.29 | 0.00 |
| 20419 | SWPP | 2021-02-16 | additive_val90 | 8.09 | 3.29 | 0.00 |
| 20416 | SWPP | 2021-02-16 | boosting_7y | 3.72 | -6.44 | -6.44 |
| 20412 | SWPP | 2021-02-16 | boosting_deep | 3.62 | -6.58 | -6.58 |
| 20414 | SWPP | 2021-02-16 | boosting_l2 | 3.61 | -5.96 | -5.96 |
| 20415 | SWPP | 2021-02-16 | boosting_refit3 | 5.59 | -3.82 | -3.82 |
| 20413 | SWPP | 2021-02-16 | boosting_shallow | 3.49 | -6.14 | -6.14 |
| 20410 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 20411 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_7y | DUK | mape | 10.089 | 0.000 | 750 |
| additive_7y | PJM | mape | 5.949 | 0.000 | 744 |
| additive_7y | SWPP | mape | -14.449 | 0.000 | 745 |
| additive_k10 | DUK | mape | 10.383 | 0.000 | 750 |
| additive_k10 | PJM | mape | 6.049 | 0.000 | 744 |
| additive_k10 | SWPP | mape | -14.169 | 0.000 | 745 |
| additive_k8 | DUK | mape | 10.224 | 0.000 | 750 |
| additive_k8 | PJM | mape | 6.075 | 0.000 | 744 |
| additive_k8 | SWPP | mape | -14.390 | 0.000 | 745 |
| additive_lam | DUK | mape | 10.153 | 0.000 | 750 |
| additive_lam | PJM | mape | 6.145 | 0.000 | 744 |
| additive_lam | SWPP | mape | -14.201 | 0.000 | 745 |
| additive_val90 | DUK | mape | 10.191 | 0.000 | 750 |
| additive_val90 | PJM | mape | 6.067 | 0.000 | 744 |
| additive_val90 | SWPP | mape | -14.282 | 0.000 | 745 |
| boosting_7y | DUK | mape | 10.150 | 0.000 | 750 |
| boosting_7y | PJM | mape | 6.187 | 0.000 | 744 |
| boosting_7y | SWPP | mape | -11.927 | 0.000 | 745 |
| boosting_deep | DUK | mape | 9.444 | 0.000 | 750 |
| boosting_deep | PJM | mape | 5.707 | 0.000 | 744 |
| boosting_deep | SWPP | mape | -12.387 | 0.000 | 745 |
| boosting_l2 | DUK | mape | 10.128 | 0.000 | 750 |
| boosting_l2 | PJM | mape | 6.273 | 0.000 | 744 |
| boosting_l2 | SWPP | mape | -11.939 | 0.000 | 745 |
| boosting_refit3 | DUK | mape | 9.418 | 0.000 | 750 |
| boosting_refit3 | PJM | mape | 6.235 | 0.000 | 744 |
| boosting_refit3 | SWPP | mape | -13.442 | 0.000 | 745 |
| boosting_shallow | DUK | mape | 11.676 | 0.000 | 750 |
| boosting_shallow | PJM | mape | 7.309 | 0.000 | 744 |
| boosting_shallow | SWPP | mape | -11.142 | 0.000 | 745 |
| final_additive | DUK | mape | 10.152 | 0.000 | 750 |
| final_additive | PJM | mape | 5.999 | 0.000 | 744 |
| final_additive | SWPP | mape | -14.342 | 0.000 | 745 |
| final_boosting | DUK | mape | 10.290 | 0.000 | 750 |
| final_boosting | PJM | mape | 6.357 | 0.000 | 744 |
| final_boosting | SWPP | mape | -11.466 | 0.000 | 745 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.994 |
| additive_7y | 0.983 |
| additive_k10 | 0.983 |
| additive_k8 | 0.983 |
| additive_lam | 0.983 |
| additive_val90 | 0.983 |
| boosting_7y | 0.991 |
| boosting_deep | 0.991 |
| boosting_l2 | 0.991 |
| boosting_refit3 | 0.991 |
| boosting_shallow | 0.991 |
| final_additive | 0.983 |
| final_boosting | 0.991 |
