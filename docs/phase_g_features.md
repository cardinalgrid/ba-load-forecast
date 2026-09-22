# Phase G: feature blocks

Development BAs: DUK, PJM, SWPP, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `*_xload` adds the load two and three weeks back and the mean of the same weekday last week; `*_xtemp` adds yesterday's extremes, the heating and cooling degree-hours of the previous 72 hours, the day's range and its temperature at 07:00 and 17:00; `boosting_xsun` gives every BA the sun's elevation; `*_xall` combines them.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| additive_xall | 2.70 | 2.33 | -0.40 | -1.67 | 1.58 | 0.51 | 0.31 | -20.78 | 2221 | 3.00 |
| additive_xtemp | 2.72 | 2.36 | -0.46 | -1.72 | 1.64 | 0.50 | 0.31 | -21.23 | 2221 | 3.00 |
| boosting_xall | 2.78 | 2.46 | -0.22 | -1.60 | 1.70 | 0.47 | 0.33 | -28.20 | 2221 | 3.00 |
| boosting_xtemp | 2.78 | 2.45 | -0.17 | -1.60 | 1.62 | 0.48 | 0.32 | -29.50 | 2221 | 3.00 |
| DF | 2.79 | 2.55 | 0.19 | -1.09 | 1.10 | 0.00 | 0.00 | -19.98 | 2221 | 3.00 |
| additive_xload | 2.80 | 2.41 | -0.52 | -1.78 | 1.67 | 0.49 | 0.30 | -19.71 | 2221 | 3.00 |
| final_additive | 2.81 | 2.45 | -0.59 | -1.83 | 1.68 | 0.48 | 0.30 | -20.36 | 2221 | 3.00 |
| boosting_xload | 2.82 | 2.48 | -0.17 | -1.60 | 1.69 | 0.48 | 0.33 | -27.93 | 2221 | 3.00 |
| boosting_xsun | 2.85 | 2.50 | -0.16 | -1.64 | 1.76 | 0.47 | 0.33 | -28.44 | 2221 | 3.00 |
| final_boosting | 2.85 | 2.50 | -0.16 | -1.64 | 1.76 | 0.47 | 0.33 | -28.44 | 2221 | 3.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.51 | -0.05 | -1.47 | 1.17 | -13.32 |  |  | 746 | 12143.29 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 734 | 92076.14 |
| DF | SWPP | 3.76 | 3.49 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 741 | 31382.01 |
| additive_xall | DUK | 3.52 | 3.15 | -0.58 | -2.30 | 1.39 | -14.98 | 0.35 | 0.26 | 746 | 12143.29 |
| additive_xall | PJM | 2.65 | 2.30 | -0.44 | -1.63 | 1.64 | -12.14 | 0.47 | 0.39 | 734 | 92076.14 |
| additive_xall | SWPP | 2.52 | 2.09 | -0.19 | -1.55 | 1.50 | -20.78 | 0.70 | 0.10 | 741 | 31382.01 |
| additive_xload | DUK | 3.58 | 3.19 | -0.61 | -2.35 | 1.35 | -14.69 | 0.36 | 0.25 | 746 | 12143.29 |
| additive_xload | PJM | 2.78 | 2.40 | -0.61 | -1.77 | 1.73 | -12.68 | 0.44 | 0.37 | 734 | 92076.14 |
| additive_xload | SWPP | 2.55 | 2.13 | -0.22 | -1.57 | 1.60 | -19.71 | 0.69 | 0.10 | 741 | 31382.01 |
| additive_xtemp | DUK | 3.52 | 3.08 | -0.64 | -2.32 | 1.42 | -14.55 | 0.36 | 0.27 | 746 | 12143.29 |
| additive_xtemp | PJM | 2.68 | 2.37 | -0.51 | -1.69 | 1.73 | -11.80 | 0.45 | 0.39 | 734 | 92076.14 |
| additive_xtemp | SWPP | 2.50 | 2.06 | -0.25 | -1.57 | 1.45 | -21.23 | 0.70 | 0.10 | 741 | 31382.01 |
| boosting_xall | DUK | 3.48 | 3.01 | -0.52 | -2.25 | 1.50 | -17.80 | 0.34 | 0.27 | 746 | 12143.29 |
| boosting_xall | PJM | 2.74 | 2.49 | 0.07 | -1.39 | 1.78 | -12.01 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xall | SWPP | 2.61 | 2.15 | -0.93 | -1.97 | 1.55 | -28.20 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xload | DUK | 3.55 | 3.15 | -0.49 | -2.27 | 1.44 | -16.27 | 0.34 | 0.26 | 746 | 12143.29 |
| boosting_xload | PJM | 2.79 | 2.49 | 0.12 | -1.39 | 1.72 | -12.65 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xload | SWPP | 2.60 | 2.20 | -0.87 | -1.94 | 1.69 | -27.93 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xsun | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| boosting_xsun | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| boosting_xsun | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |
| boosting_xtemp | DUK | 3.49 | 3.03 | -0.51 | -2.25 | 1.43 | -17.27 | 0.38 | 0.27 | 746 | 12143.29 |
| boosting_xtemp | PJM | 2.73 | 2.47 | 0.10 | -1.39 | 1.64 | -11.49 | 0.43 | 0.41 | 734 | 92076.14 |
| boosting_xtemp | SWPP | 2.66 | 2.16 | -0.85 | -1.94 | 1.62 | -29.50 | 0.67 | 0.08 | 741 | 31382.01 |
| final_additive | DUK | 3.56 | 3.15 | -0.71 | -2.39 | 1.42 | -14.75 | 0.34 | 0.27 | 746 | 12143.29 |
| final_additive | PJM | 2.81 | 2.47 | -0.68 | -1.84 | 1.77 | -12.10 | 0.42 | 0.37 | 734 | 92076.14 |
| final_additive | SWPP | 2.53 | 2.11 | -0.28 | -1.59 | 1.49 | -20.36 | 0.70 | 0.10 | 741 | 31382.01 |
| final_boosting | DUK | 3.57 | 3.12 | -0.42 | -2.27 | 1.49 | -16.82 | 0.33 | 0.27 | 746 | 12143.29 |
| final_boosting | PJM | 2.82 | 2.52 | 0.12 | -1.44 | 1.84 | -11.75 | 0.42 | 0.42 | 734 | 92076.14 |
| final_boosting | SWPP | 2.67 | 2.19 | -0.90 | -1.98 | 1.62 | -28.44 | 0.68 | 0.08 | 741 | 31382.01 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| additive_xall | DUK | uri | 3.49 | -1.84 | -1.91 | -6.46 | 6 |
| additive_xall | PJM | uri | 3.14 | 3.01 | -0.41 | -2.47 | 6 |
| additive_xall | SWPP | uri | 6.47 | 1.82 | -2.00 | -5.04 | 4 |
| additive_xload | DUK | uri | 3.45 | -2.22 | -2.22 | -6.93 | 6 |
| additive_xload | PJM | uri | 3.11 | 2.58 | -0.37 | -2.24 | 6 |
| additive_xload | SWPP | uri | 6.41 | 1.23 | -2.16 | -5.48 | 4 |
| additive_xtemp | DUK | uri | 3.46 | -2.33 | -2.35 | -7.06 | 6 |
| additive_xtemp | PJM | uri | 3.00 | 2.79 | -0.47 | -2.80 | 6 |
| additive_xtemp | SWPP | uri | 6.59 | 2.33 | -1.74 | -4.71 | 4 |
| boosting_xall | DUK | uri | 3.73 | -2.45 | -2.62 | -5.37 | 6 |
| boosting_xall | PJM | uri | 2.04 | -0.72 | -0.98 | -1.97 | 6 |
| boosting_xall | SWPP | uri | 5.87 | -3.34 | -4.47 | -10.32 | 4 |
| boosting_xload | DUK | uri | 3.57 | -2.86 | -2.93 | -4.81 | 6 |
| boosting_xload | PJM | uri | 2.04 | -1.19 | -1.40 | -3.32 | 6 |
| boosting_xload | SWPP | uri | 5.28 | -3.27 | -4.40 | -10.34 | 4 |
| boosting_xsun | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| boosting_xsun | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| boosting_xsun | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| boosting_xtemp | DUK | uri | 3.60 | -2.52 | -2.58 | -5.65 | 6 |
| boosting_xtemp | PJM | uri | 1.86 | -0.63 | -1.04 | -3.39 | 6 |
| boosting_xtemp | SWPP | uri | 5.79 | -2.74 | -4.18 | -9.79 | 4 |
| final_additive | DUK | uri | 3.45 | -2.72 | -2.72 | -7.63 | 6 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | SWPP | uri | 6.57 | 1.77 | -1.89 | -5.10 | 4 |
| final_boosting | DUK | uri | 3.53 | -2.86 | -2.86 | -4.45 | 6 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | SWPP | uri | 5.52 | -2.69 | -4.08 | -10.21 | 4 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| additive_xall | DUK | elliott | 4.58 | -3.41 | -3.41 | -5.07 | 4 |
| additive_xall | PJM | elliott | 3.53 | -0.16 | -0.93 | -4.57 | 5 |
| additive_xall | SWPP | elliott | 3.00 | -2.57 | -2.84 | -5.40 | 5 |
| additive_xload | DUK | elliott | 4.26 | -3.35 | -3.35 | -4.89 | 4 |
| additive_xload | PJM | elliott | 3.79 | -1.37 | -1.98 | -8.99 | 5 |
| additive_xload | SWPP | elliott | 3.36 | -2.66 | -2.88 | -6.85 | 5 |
| additive_xtemp | DUK | elliott | 4.63 | -2.45 | -2.47 | -5.20 | 4 |
| additive_xtemp | PJM | elliott | 3.60 | -0.12 | -0.90 | -4.52 | 5 |
| additive_xtemp | SWPP | elliott | 3.33 | -2.50 | -2.97 | -6.48 | 5 |
| boosting_xall | DUK | elliott | 4.71 | -2.60 | -2.60 | -5.62 | 4 |
| boosting_xall | PJM | elliott | 5.27 | -2.75 | -3.77 | -7.24 | 5 |
| boosting_xall | SWPP | elliott | 5.50 | -1.75 | -3.68 | -11.27 | 5 |
| boosting_xload | DUK | elliott | 4.64 | -3.33 | -3.33 | -6.47 | 4 |
| boosting_xload | PJM | elliott | 5.09 | -2.53 | -3.43 | -6.72 | 5 |
| boosting_xload | SWPP | elliott | 5.00 | -2.74 | -4.31 | -11.73 | 5 |
| boosting_xsun | DUK | elliott | 4.01 | -3.40 | -3.40 | -7.00 | 4 |
| boosting_xsun | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| boosting_xsun | SWPP | elliott | 5.00 | -1.82 | -3.69 | -11.12 | 5 |
| boosting_xtemp | DUK | elliott | 4.65 | -3.11 | -3.11 | -6.79 | 4 |
| boosting_xtemp | PJM | elliott | 5.38 | -1.56 | -2.95 | -5.92 | 5 |
| boosting_xtemp | SWPP | elliott | 4.59 | -1.33 | -3.29 | -10.96 | 5 |
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
| 11 | additive_xall | eve | 3.50 | 0.84 | -1.38 | 0.55 | 73 |
| 12 | additive_xload | eve | 3.53 | 0.52 | -1.53 | 0.52 | 73 |
| 13 | additive_xtemp | eve | 3.54 | 0.90 | -1.38 | 0.55 | 73 |
| 18 | final_additive | eve | 3.54 | 0.56 | -1.55 | 0.53 | 73 |
| 14 | boosting_xall | eve | 3.76 | 0.73 | -1.44 | 0.52 | 73 |
| 15 | boosting_xload | eve | 3.85 | 0.90 | -1.45 | 0.52 | 73 |
| 17 | boosting_xtemp | eve | 3.86 | 0.85 | -1.51 | 0.49 | 73 |
| 10 | DF | eve | 3.89 | 2.15 | -0.75 |  | 73 |
| 16 | boosting_xsun | eve | 3.92 | 0.95 | -1.52 | 0.51 | 73 |
| 19 | final_boosting | eve | 3.92 | 0.95 | -1.52 | 0.51 | 73 |
| 1 | additive_xall | special | 3.24 | -0.64 | -2.02 | 0.59 | 74 |
| 3 | additive_xtemp | special | 3.27 | -0.54 | -1.97 | 0.58 | 74 |
| 2 | additive_xload | special | 3.32 | -0.81 | -2.14 | 0.58 | 74 |
| 8 | final_additive | special | 3.33 | -0.63 | -2.06 | 0.61 | 74 |
| 5 | boosting_xload | special | 3.79 | -0.07 | -1.82 | 0.57 | 74 |
| 6 | boosting_xsun | special | 3.90 | -0.12 | -1.98 | 0.54 | 74 |
| 9 | final_boosting | special | 3.90 | -0.12 | -1.98 | 0.54 | 74 |
| 4 | boosting_xall | special | 3.92 | -0.09 | -1.90 | 0.54 | 74 |
| 7 | boosting_xtemp | special | 4.05 | -0.11 | -2.05 | 0.53 | 74 |
| 0 | DF | special | 4.47 | 1.66 | -0.98 |  | 74 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 7399 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 7394 | DUK | 2022-12-24 | additive_xall | 6.92 | -12.48 | -12.48 |
| 7392 | DUK | 2022-12-24 | additive_xload | 6.45 | -12.81 | -12.81 |
| 7393 | DUK | 2022-12-24 | additive_xtemp | 7.27 | -12.54 | -12.54 |
| 7398 | DUK | 2022-12-24 | boosting_xall | 9.37 | -16.02 | -16.02 |
| 7395 | DUK | 2022-12-24 | boosting_xload | 10.22 | -17.91 | -17.91 |
| 7397 | DUK | 2022-12-24 | boosting_xsun | 9.36 | -15.80 | -15.80 |
| 7396 | DUK | 2022-12-24 | boosting_xtemp | 9.25 | -15.80 | -15.80 |
| 7390 | DUK | 2022-12-24 | final_additive | 7.26 | -12.67 | -12.67 |
| 7391 | DUK | 2022-12-24 | final_boosting | 9.36 | -15.80 | -15.80 |
| 15559 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 15554 | SWPP | 2021-02-15 | additive_xall | 2.38 | 1.40 | 0.00 |
| 15552 | SWPP | 2021-02-15 | additive_xload | 2.31 | 1.02 | 0.00 |
| 15553 | SWPP | 2021-02-15 | additive_xtemp | 2.77 | 1.43 | 0.00 |
| 15558 | SWPP | 2021-02-15 | boosting_xall | 6.26 | -8.32 | -8.32 |
| 15555 | SWPP | 2021-02-15 | boosting_xload | 6.27 | -8.52 | -8.52 |
| 15557 | SWPP | 2021-02-15 | boosting_xsun | 5.58 | -7.79 | -7.79 |
| 15556 | SWPP | 2021-02-15 | boosting_xtemp | 6.09 | -8.25 | -8.25 |
| 15550 | SWPP | 2021-02-15 | final_additive | 2.66 | 1.09 | 0.00 |
| 15551 | SWPP | 2021-02-15 | final_boosting | 5.58 | -7.79 | -7.79 |
| 15569 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 15564 | SWPP | 2021-02-16 | additive_xall | 7.58 | 3.67 | 0.00 |
| 15562 | SWPP | 2021-02-16 | additive_xload | 7.54 | 3.32 | 0.00 |
| 15563 | SWPP | 2021-02-16 | additive_xtemp | 8.04 | 3.60 | 0.00 |
| 15568 | SWPP | 2021-02-16 | boosting_xall | 3.17 | -5.46 | -5.46 |
| 15565 | SWPP | 2021-02-16 | boosting_xload | 3.36 | -5.76 | -5.76 |
| 15567 | SWPP | 2021-02-16 | boosting_xsun | 3.72 | -6.44 | -6.44 |
| 15566 | SWPP | 2021-02-16 | boosting_xtemp | 3.40 | -6.73 | -6.73 |
| 15560 | SWPP | 2021-02-16 | final_additive | 8.09 | 3.29 | 0.00 |
| 15561 | SWPP | 2021-02-16 | final_boosting | 3.72 | -6.44 | -6.44 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| additive_xall | DUK | mape | 9.584 | 0.000 | 746 |
| additive_xall | PJM | mape | 3.267 | 0.001 | 734 |
| additive_xall | SWPP | mape | -14.178 | 0.000 | 741 |
| additive_xload | DUK | mape | 10.259 | 0.000 | 746 |
| additive_xload | PJM | mape | 5.370 | 0.000 | 734 |
| additive_xload | SWPP | mape | -13.822 | 0.000 | 741 |
| additive_xtemp | DUK | mape | 9.520 | 0.000 | 746 |
| additive_xtemp | PJM | mape | 3.899 | 0.000 | 734 |
| additive_xtemp | SWPP | mape | -14.616 | 0.000 | 741 |
| boosting_xall | DUK | mape | 9.118 | 0.000 | 746 |
| boosting_xall | PJM | mape | 4.850 | 0.000 | 734 |
| boosting_xall | SWPP | mape | -12.160 | 0.000 | 741 |
| boosting_xload | DUK | mape | 9.985 | 0.000 | 746 |
| boosting_xload | PJM | mape | 5.717 | 0.000 | 734 |
| boosting_xload | SWPP | mape | -12.425 | 0.000 | 741 |
| boosting_xsun | DUK | mape | 10.195 | 0.000 | 746 |
| boosting_xsun | PJM | mape | 6.019 | 0.000 | 734 |
| boosting_xsun | SWPP | mape | -11.363 | 0.000 | 741 |
| boosting_xtemp | DUK | mape | 9.116 | 0.000 | 746 |
| boosting_xtemp | PJM | mape | 4.787 | 0.000 | 734 |
| boosting_xtemp | SWPP | mape | -11.830 | 0.000 | 741 |
| final_additive | DUK | mape | 10.073 | 0.000 | 746 |
| final_additive | PJM | mape | 5.791 | 0.000 | 734 |
| final_additive | SWPP | mape | -14.285 | 0.000 | 741 |
| final_boosting | DUK | mape | 10.195 | 0.000 | 746 |
| final_boosting | PJM | mape | 6.019 | 0.000 | 734 |
| final_boosting | SWPP | mape | -11.363 | 0.000 | 741 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.994 |
| additive_xall | 0.975 |
| additive_xload | 0.975 |
| additive_xtemp | 0.983 |
| boosting_xall | 0.991 |
| boosting_xload | 0.991 |
| boosting_xsun | 0.991 |
| boosting_xtemp | 0.991 |
| final_additive | 0.983 |
| final_boosting | 0.991 |
