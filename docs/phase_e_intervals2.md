# Phase E: regime-conditional errors with an adaptive level

Development BAs: CISO, ERCO, MISO, PJM, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. `ens_bc_regime` reads the 5th and 95th percentiles of the corrected ensemble's errors on the known days of the same temperature regime over the last year; `ens_bc_adaptive` reads them on the last 120 days at a level that adapts to the coverage achieved (adaptive conformal inference); `ens_bc_regime_aci` combines the two (regime pool, one adaptive level); `ens_bc_regime_aci2` tracks one adaptive level per regime.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_bc_regime | 2.39 | 2.10 | -0.73 | -1.70 | 1.37 | 0.65 | 0.28 | -15.23 | 2973 | 4.00 |
| ens_bc_regime_aci | 2.39 | 2.10 | -0.73 | -1.70 | 1.37 | 0.65 | 0.28 | -15.23 | 2973 | 4.00 |
| ens_bc_regime_aci2 | 2.39 | 2.10 | -0.73 | -1.70 | 1.37 | 0.65 | 0.28 | -15.23 | 2973 | 4.00 |
| ens_bc_adaptive | 2.58 | 2.27 | -0.69 | -1.75 | 1.44 | 0.61 | 0.29 | -16.77 | 2973 | 4.00 |
| ens_recent | 2.65 | 2.33 | -1.11 | -2.00 | 1.34 | 0.60 | 0.28 | -18.88 | 2973 | 4.00 |
| boosting_ml | 2.79 | 2.46 | -0.79 | -1.89 | 1.58 | 0.57 | 0.29 | -18.95 | 2973 | 4.00 |
| additive_ml_special | 2.95 | 2.62 | -1.46 | -2.34 | 1.51 | 0.55 | 0.26 | -18.80 | 2973 | 4.00 |
| DF | 3.05 | 2.73 | 0.21 | -1.11 | 1.13 | 0.00 | 0.00 | -14.36 | 2973 | 4.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | ERCO | 2.63 | 2.12 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 746 | 46782.53 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | PJM | 3.65 | 3.48 | -1.47 | -1.91 | 1.63 | -10.72 |  |  | 744 | 91927.69 |
| additive_ml_special | CISO | 3.86 | 3.50 | -3.12 | -3.96 | 0.37 | -18.80 | 0.29 | 0.14 | 737 | 25196.91 |
| additive_ml_special | ERCO | 3.56 | 3.14 | -2.22 | -3.04 | 1.11 | -16.37 | 0.30 | 0.15 | 746 | 46782.53 |
| additive_ml_special | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| additive_ml_special | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.75 | 0.51 | 744 | 91927.69 |
| boosting_ml | CISO | 3.11 | 2.78 | -2.24 | -2.82 | 0.49 | -18.95 | 0.41 | 0.17 | 737 | 25196.91 |
| boosting_ml | ERCO | 3.13 | 2.72 | -2.27 | -2.98 | 1.29 | -15.00 | 0.35 | 0.18 | 746 | 46782.53 |
| boosting_ml | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| boosting_ml | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.75 | 0.57 | 744 | 91927.69 |
| ens_bc_adaptive | CISO | 2.96 | 2.63 | -0.52 | -2.00 | 0.36 | -16.77 | 0.43 | 0.23 | 737 | 25196.91 |
| ens_bc_adaptive | ERCO | 2.93 | 2.50 | -1.05 | -2.14 | 1.16 | -14.76 | 0.40 | 0.22 | 746 | 46782.53 |
| ens_bc_adaptive | MISO | 2.20 | 1.89 | -0.61 | -1.43 | 1.61 | -8.52 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_bc_adaptive | PJM | 2.59 | 2.36 | -0.61 | -1.73 | 1.73 | -12.31 | 0.78 | 0.52 | 744 | 91927.69 |
| ens_bc_regime | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_bc_regime_aci | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime_aci | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime_aci | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime_aci | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_bc_regime_aci2 | CISO | 2.76 | 2.46 | -0.87 | -1.86 | 0.39 | -15.03 | 0.49 | 0.22 | 737 | 25196.91 |
| ens_bc_regime_aci2 | ERCO | 2.79 | 2.39 | -0.74 | -1.94 | 1.11 | -15.23 | 0.44 | 0.23 | 746 | 46782.53 |
| ens_bc_regime_aci2 | MISO | 2.09 | 1.81 | -0.63 | -1.43 | 1.59 | -8.62 | 0.61 | 0.05 | 746 | 73788.38 |
| ens_bc_regime_aci2 | PJM | 2.34 | 2.08 | -0.78 | -1.76 | 1.59 | -11.20 | 0.84 | 0.49 | 744 | 91927.69 |
| ens_recent | CISO | 3.16 | 2.78 | -2.58 | -3.21 | 0.39 | -18.88 | 0.42 | 0.15 | 737 | 25196.91 |
| ens_recent | ERCO | 3.13 | 2.70 | -2.25 | -2.89 | 1.07 | -14.84 | 0.36 | 0.17 | 746 | 46782.53 |
| ens_recent | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_recent | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.79 | 0.55 | 744 | 91927.69 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 2.82 | -1.01 | -1.14 | -2.03 | 6 |
| additive_ml_special | CISO | uri | 2.30 | 1.97 | 0.00 | 0.00 | 6 |
| additive_ml_special | ERCO | uri | 4.97 | -5.56 | -5.56 | -8.11 | 2 |
| additive_ml_special | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| additive_ml_special | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| boosting_ml | CISO | uri | 1.94 | -1.22 | -1.32 | -3.36 | 6 |
| boosting_ml | ERCO | uri | 8.12 | -12.91 | -12.91 | -15.00 | 2 |
| boosting_ml | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| boosting_ml | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| ens_bc_adaptive | CISO | uri | 1.96 | -0.77 | -1.09 | -2.59 | 6 |
| ens_bc_adaptive | ERCO | uri | 6.75 | -9.60 | -9.60 | -9.98 | 2 |
| ens_bc_adaptive | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_adaptive | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime_aci | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime_aci | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime_aci | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime_aci | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_bc_regime_aci2 | CISO | uri | 1.97 | -0.74 | -1.07 | -2.55 | 6 |
| ens_bc_regime_aci2 | ERCO | uri | 6.92 | -9.80 | -9.80 | -10.39 | 2 |
| ens_bc_regime_aci2 | MISO | uri | 3.50 | -3.21 | -3.34 | -6.51 | 5 |
| ens_bc_regime_aci2 | PJM | uri | 1.83 | -0.38 | -0.84 | -2.97 | 6 |
| ens_recent | CISO | uri | 1.78 | 0.44 | -0.28 | -1.40 | 6 |
| ens_recent | ERCO | uri | 6.28 | -9.24 | -9.24 | -9.46 | 2 |
| ens_recent | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| ens_recent | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 4.02 | -3.14 | -3.14 | -5.88 | 5 |
| additive_ml_special | CISO | elliott | 3.89 | 2.67 | -0.55 | -2.75 | 5 |
| additive_ml_special | ERCO | elliott | 7.85 | -5.09 | -6.05 | -12.58 | 5 |
| additive_ml_special | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| additive_ml_special | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| boosting_ml | CISO | elliott | 3.66 | 1.13 | -0.69 | -3.11 | 5 |
| boosting_ml | ERCO | elliott | 6.33 | -3.53 | -5.16 | -12.62 | 5 |
| boosting_ml | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| boosting_ml | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| ens_bc_adaptive | CISO | elliott | 4.09 | 2.82 | -0.44 | -2.20 | 5 |
| ens_bc_adaptive | ERCO | elliott | 6.93 | -2.86 | -4.49 | -11.30 | 5 |
| ens_bc_adaptive | MISO | elliott | 3.58 | -1.17 | -2.16 | -4.06 | 5 |
| ens_bc_adaptive | PJM | elliott | 4.36 | -1.15 | -2.39 | -5.75 | 5 |
| ens_bc_regime | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_bc_regime_aci | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime_aci | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime_aci | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime_aci | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_bc_regime_aci2 | CISO | elliott | 3.06 | 0.99 | -0.83 | -3.77 | 5 |
| ens_bc_regime_aci2 | ERCO | elliott | 6.72 | -3.96 | -5.21 | -12.15 | 5 |
| ens_bc_regime_aci2 | MISO | elliott | 3.38 | -2.05 | -2.94 | -4.54 | 5 |
| ens_bc_regime_aci2 | PJM | elliott | 4.18 | -2.63 | -3.19 | -7.00 | 5 |
| ens_recent | CISO | elliott | 3.27 | 1.77 | -0.59 | -2.96 | 5 |
| ens_recent | ERCO | elliott | 6.73 | -4.28 | -5.36 | -12.60 | 5 |
| ens_recent | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| ens_recent | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | ens_recent | eve | 3.28 | -0.33 | -1.94 | 0.60 | 99 |
| 12 | ens_bc_regime | eve | 3.32 | 0.24 | -1.69 | 0.61 | 99 |
| 13 | ens_bc_regime_aci | eve | 3.32 | 0.24 | -1.69 | 0.61 | 99 |
| 14 | ens_bc_regime_aci2 | eve | 3.32 | 0.24 | -1.69 | 0.61 | 99 |
| 9 | additive_ml_special | eve | 3.48 | -0.49 | -2.18 | 0.59 | 99 |
| 10 | boosting_ml | eve | 3.50 | -0.18 | -1.90 | 0.57 | 99 |
| 11 | ens_bc_adaptive | eve | 3.63 | 0.62 | -1.62 | 0.53 | 99 |
| 8 | DF | eve | 3.80 | 1.29 | -0.94 |  | 99 |
| 4 | ens_bc_regime | special | 2.99 | -0.70 | -1.92 | 0.63 | 99 |
| 5 | ens_bc_regime_aci | special | 2.99 | -0.70 | -1.92 | 0.63 | 99 |
| 6 | ens_bc_regime_aci2 | special | 2.99 | -0.70 | -1.92 | 0.63 | 99 |
| 7 | ens_recent | special | 3.19 | -1.20 | -2.34 | 0.62 | 99 |
| 1 | additive_ml_special | special | 3.29 | -1.59 | -2.73 | 0.59 | 99 |
| 3 | ens_bc_adaptive | special | 3.40 | -0.28 | -1.93 | 0.62 | 99 |
| 2 | boosting_ml | special | 3.58 | -0.82 | -2.14 | 0.53 | 99 |
| 0 | DF | special | 3.94 | 0.99 | -1.12 |  | 99 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ens_bc_adaptive | all | 0.382 | 1.347 | 0.379 | 0.897 | 11.770 | 0.899 | 2889 |
| ens_bc_regime | all | 0.356 | 1.255 | 0.363 | 0.867 | 9.922 | 0.863 | 2888 |
| ens_bc_regime_aci | all | 0.365 | 1.255 | 0.362 | 0.897 | 11.196 | 0.892 | 2888 |
| ens_bc_regime_aci2 | all | 0.360 | 1.255 | 0.364 | 0.894 | 11.008 | 0.891 | 2888 |
| ens_bc_adaptive | events | 0.506 | 1.906 | 0.652 | 0.760 | 11.407 | 0.795 | 39 |
| ens_bc_regime | events | 0.475 | 1.806 | 0.698 | 0.719 | 9.581 | 0.692 | 39 |
| ens_bc_regime_aci | events | 0.470 | 1.806 | 0.677 | 0.762 | 10.800 | 0.718 | 39 |
| ens_bc_regime_aci2 | events | 0.461 | 1.806 | 0.669 | 0.765 | 10.924 | 0.744 | 39 |
| ens_bc_adaptive | cold_mornings | 0.428 | 1.611 | 0.519 | 0.826 | 11.605 | 0.817 | 120 |
| ens_bc_regime | cold_mornings | 0.449 | 1.617 | 0.533 | 0.784 | 10.110 | 0.758 | 120 |
| ens_bc_regime_aci | cold_mornings | 0.411 | 1.617 | 0.530 | 0.815 | 11.079 | 0.775 | 120 |
| ens_bc_regime_aci2 | cold_mornings | 0.408 | 1.617 | 0.526 | 0.817 | 11.134 | 0.783 | 120 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 6495 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 6488 | ERCO | 2021-02-15 | additive_ml_special | 41.72 | -4.24 | -4.24 |
| 6489 | ERCO | 2021-02-15 | boosting_ml | 27.39 | -16.57 | -16.57 |
| 6492 | ERCO | 2021-02-15 | ens_bc_adaptive | 33.89 | -10.66 | -10.66 |
| 6491 | ERCO | 2021-02-15 | ens_bc_regime | 33.61 | -10.86 | -10.86 |
| 6493 | ERCO | 2021-02-15 | ens_bc_regime_aci | 33.61 | -10.86 | -10.86 |
| 6494 | ERCO | 2021-02-15 | ens_bc_regime_aci2 | 33.61 | -10.86 | -10.86 |
| 6490 | ERCO | 2021-02-15 | ens_recent | 34.57 | -10.39 | -10.39 |
| 6503 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 6496 | ERCO | 2021-02-16 | additive_ml_special | 47.08 | 43.33 | 0.00 |
| 6497 | ERCO | 2021-02-16 | boosting_ml | 33.46 | 31.10 | 0.00 |
| 6500 | ERCO | 2021-02-16 | ens_bc_adaptive | 39.79 | 37.44 | 0.00 |
| 6499 | ERCO | 2021-02-16 | ens_bc_regime | 39.49 | 37.58 | 0.00 |
| 6501 | ERCO | 2021-02-16 | ens_bc_regime_aci | 39.49 | 37.58 | 0.00 |
| 6502 | ERCO | 2021-02-16 | ens_bc_regime_aci2 | 39.49 | 37.58 | 0.00 |
| 6498 | ERCO | 2021-02-16 | ens_recent | 40.43 | 37.36 | 0.00 |
| 6511 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 6504 | ERCO | 2021-02-17 | additive_ml_special | 31.74 | 29.84 | 0.00 |
| 6505 | ERCO | 2021-02-17 | boosting_ml | 28.91 | 24.01 | 0.00 |
| 6508 | ERCO | 2021-02-17 | ens_bc_adaptive | 29.65 | 24.44 | 0.00 |
| 6507 | ERCO | 2021-02-17 | ens_bc_regime | 29.39 | 23.92 | 0.00 |
| 6509 | ERCO | 2021-02-17 | ens_bc_regime_aci | 29.39 | 23.92 | 0.00 |
| 6510 | ERCO | 2021-02-17 | ens_bc_regime_aci2 | 29.39 | 23.92 | 0.00 |
| 6506 | ERCO | 2021-02-17 | ens_recent | 30.28 | 26.83 | 0.00 |
| 6519 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 6512 | ERCO | 2021-02-18 | additive_ml_special | 13.46 | 12.91 | 0.00 |
| 6513 | ERCO | 2021-02-18 | boosting_ml | 3.58 | -2.96 | -2.96 |
| 6516 | ERCO | 2021-02-18 | ens_bc_adaptive | 7.10 | 4.76 | 0.00 |
| 6515 | ERCO | 2021-02-18 | ens_bc_regime | 6.89 | 4.76 | 0.00 |
| 6517 | ERCO | 2021-02-18 | ens_bc_regime_aci | 6.89 | 4.76 | 0.00 |
| 6518 | ERCO | 2021-02-18 | ens_bc_regime_aci2 | 6.89 | 4.76 | 0.00 |
| 6514 | ERCO | 2021-02-18 | ens_recent | 7.68 | 4.44 | 0.00 |
| 12503 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 12496 | MISO | 2021-02-16 | additive_ml_special | 2.38 | 1.99 | 0.00 |
| 12497 | MISO | 2021-02-16 | boosting_ml | 2.11 | 0.99 | 0.00 |
| 12500 | MISO | 2021-02-16 | ens_bc_adaptive | 2.07 | 1.67 | 0.00 |
| 12499 | MISO | 2021-02-16 | ens_bc_regime | 2.07 | 1.67 | 0.00 |
| 12501 | MISO | 2021-02-16 | ens_bc_regime_aci | 2.07 | 1.67 | 0.00 |
| 12502 | MISO | 2021-02-16 | ens_bc_regime_aci2 | 2.07 | 1.67 | 0.00 |
| 12498 | MISO | 2021-02-16 | ens_recent | 2.17 | 1.51 | 0.00 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_ml_special | CISO | mape | 13.851 | 0.000 | 737 |
| additive_ml_special | ERCO | mape | 11.907 | 0.000 | 746 |
| additive_ml_special | MISO | mape | -2.885 | 0.004 | 746 |
| additive_ml_special | PJM | mape | -14.911 | 0.000 | 744 |
| boosting_ml | CISO | mape | 4.432 | 0.000 | 737 |
| boosting_ml | ERCO | mape | 6.704 | 0.000 | 746 |
| boosting_ml | MISO | mape | -3.438 | 0.001 | 746 |
| boosting_ml | PJM | mape | -14.855 | 0.000 | 744 |
| ens_bc_adaptive | CISO | mape | 2.411 | 0.016 | 737 |
| ens_bc_adaptive | ERCO | mape | 4.599 | 0.000 | 746 |
| ens_bc_adaptive | MISO | mape | -6.867 | 0.000 | 746 |
| ens_bc_adaptive | PJM | mape | -19.397 | 0.000 | 744 |
| ens_bc_regime | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime | PJM | mape | -25.615 | 0.000 | 744 |
| ens_bc_regime_aci | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime_aci | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime_aci | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime_aci | PJM | mape | -25.615 | 0.000 | 744 |
| ens_bc_regime_aci2 | CISO | mape | -0.572 | 0.567 | 737 |
| ens_bc_regime_aci2 | ERCO | mape | 2.542 | 0.011 | 746 |
| ens_bc_regime_aci2 | MISO | mape | -8.669 | 0.000 | 746 |
| ens_bc_regime_aci2 | PJM | mape | -25.615 | 0.000 | 744 |
| ens_recent | CISO | mape | 4.977 | 0.000 | 737 |
| ens_recent | ERCO | mape | 6.848 | 0.000 | 746 |
| ens_recent | MISO | mape | -6.116 | 0.000 | 746 |
| ens_recent | PJM | mape | -19.327 | 0.000 | 744 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| additive_ml_special | 0.982 |
| boosting_ml | 0.994 |
| ens_bc_adaptive | 0.994 |
| ens_bc_regime | 0.994 |
| ens_bc_regime_aci | 0.994 |
| ens_bc_regime_aci2 | 0.994 |
| ens_recent | 0.994 |
