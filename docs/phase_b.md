# Phase B: floors, profile and recency regression against the BA's forecast

Day-ahead forecasts issued under the 9 a.m. cut-off for BPAT, CISO, DUK, ERCO, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, scored against the load that occurred and compared, day by day, with the BA's own day-ahead forecast reported to the EIA (`DF`). Models: the three floors (last known day, same weekday last week, mean of the same day type over two weeks), the profile of Cardinal Grid Note 2 with the regime from the HRRR forecast, and the recency-effect regression fitted on observed temperature and run on the HRRR forecast. Only BA-days on which every model produced a forecast are counted.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 3.03 | 2.71 | 0.29 | -1.12 | 1.08 | 0.00 | 0.00 | -19.98 | 7473 | 10.00 |
| recency_regression | 4.31 | 3.64 | -0.58 | -2.49 | 1.85 | 0.33 | 0.27 | -26.14 | 7473 | 10.00 |
| profile | 6.88 | 5.30 | -1.50 | -4.35 | 2.14 | 0.22 | 0.23 | -54.16 | 7473 | 10.00 |
| last_known_day | 6.97 | 5.82 | -0.93 | -4.25 | 2.56 | 0.19 | 0.24 | -44.26 | 7473 | 10.00 |
| same_type_mean_2w | 7.13 | 5.43 | -1.18 | -4.42 | 2.46 | 0.20 | 0.24 | -47.85 | 7473 | 10.00 |
| same_weekday_last_week | 8.67 | 6.74 | -1.18 | -5.27 | 2.80 | 0.15 | 0.23 | -50.54 | 7473 | 10.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.07 | 1.80 | 0.19 | -0.96 | 1.46 | -19.35 |  |  | 750 | 6533.15 |
| DF | CISO | 2.80 | 2.38 | 0.11 | -0.83 | 0.41 | -6.84 |  |  | 737 | 25196.91 |
| DF | DUK | 2.84 | 2.52 | -0.07 | -1.49 | 1.17 | -13.32 |  |  | 751 | 12138.74 |
| DF | ERCO | 2.80 | 2.12 | 0.63 | -1.11 | 0.84 | -14.36 |  |  | 750 | 46788.33 |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.17 | -0.19 | 0.97 | -6.70 |  |  | 747 | 73810.76 |
| DF | NYIS | 2.67 | 2.51 | -2.49 | -2.68 | 0.40 | -12.87 |  |  | 752 | 17400.75 |
| DF | PJM | 3.65 | 3.48 | -1.47 | -1.91 | 1.63 | -10.72 |  |  | 744 | 91927.69 |
| DF | SWPP | 3.86 | 3.51 | 2.60 | -0.43 | 1.25 | -19.98 |  |  | 749 | 31365.51 |
| DF | TVA | 2.23 | 1.93 | -0.18 | -1.27 | 0.99 | -16.93 |  |  | 741 | 18592.18 |
| last_known_day | BPAT | 5.26 | 4.53 | -0.78 | -3.31 | 2.51 | -27.64 | 0.11 | 0.22 | 750 | 6533.15 |
| last_known_day | CISO | 6.99 | 6.67 | 0.07 | -3.46 | 0.62 | -33.31 | 0.19 | 0.26 | 737 | 25196.91 |
| last_known_day | DUK | 9.24 | 8.24 | -1.66 | -5.95 | 2.57 | -39.52 | 0.09 | 0.25 | 751 | 12138.74 |
| last_known_day | ERCO | 6.86 | 5.34 | -1.63 | -4.62 | 2.34 | -38.07 | 0.12 | 0.18 | 750 | 46788.33 |
| last_known_day | ISNE | 8.69 | 7.30 | -0.16 | -4.35 | 0.79 | -44.26 | 0.05 | 0.19 | 752 | 13392.81 |
| last_known_day | MISO | 5.94 | 4.98 | -0.84 | -3.64 | 3.08 | -24.61 | 0.22 | 0.07 | 747 | 73810.76 |
| last_known_day | NYIS | 7.19 | 5.86 | -0.29 | -4.13 | 1.16 | -37.87 | 0.14 | 0.51 | 752 | 17400.75 |
| last_known_day | PJM | 7.31 | 6.06 | -0.85 | -4.46 | 3.20 | -33.75 | 0.25 | 0.42 | 744 | 91927.69 |
| last_known_day | SWPP | 6.13 | 4.92 | -1.17 | -4.01 | 2.73 | -40.31 | 0.32 | 0.07 | 749 | 31365.51 |
| last_known_day | TVA | 8.65 | 7.34 | -1.54 | -5.47 | 2.76 | -39.75 | 0.04 | 0.26 | 741 | 18592.18 |
| profile | BPAT | 5.78 | 4.50 | -1.71 | -3.83 | 2.36 | -30.43 | 0.13 | 0.21 | 750 | 6533.15 |
| profile | CISO | 5.54 | 4.37 | -0.44 | -3.01 | 0.54 | -27.55 | 0.20 | 0.24 | 737 | 25196.91 |
| profile | DUK | 8.65 | 6.77 | -2.05 | -5.63 | 2.30 | -45.59 | 0.11 | 0.21 | 751 | 12138.74 |
| profile | ERCO | 7.59 | 5.85 | -2.51 | -5.35 | 2.16 | -41.15 | 0.12 | 0.19 | 750 | 46788.33 |
| profile | ISNE | 7.93 | 6.34 | -1.33 | -4.28 | 0.54 | -36.25 | 0.07 | 0.15 | 752 | 13392.81 |
| profile | MISO | 5.58 | 4.29 | -0.89 | -3.35 | 2.42 | -24.75 | 0.25 | 0.06 | 747 | 73810.76 |
| profile | NYIS | 6.18 | 4.75 | -0.87 | -3.58 | 0.61 | -36.24 | 0.22 | 0.54 | 752 | 17400.75 |
| profile | PJM | 7.30 | 5.65 | -1.77 | -4.79 | 2.70 | -33.55 | 0.27 | 0.38 | 744 | 91927.69 |
| profile | SWPP | 6.73 | 4.77 | -1.12 | -4.05 | 2.12 | -28.84 | 0.35 | 0.07 | 749 | 31365.51 |
| profile | TVA | 9.37 | 7.38 | -2.33 | -6.12 | 2.87 | -54.16 | 0.05 | 0.23 | 741 | 18592.18 |
| recency_regression | BPAT | 3.80 | 3.27 | -0.70 | -2.22 | 2.06 | -18.62 | 0.20 | 0.25 | 750 | 6533.15 |
| recency_regression | CISO | 5.72 | 4.92 | -1.51 | -3.18 | 0.84 | -24.61 | 0.14 | 0.24 | 737 | 25196.91 |
| recency_regression | DUK | 4.59 | 4.16 | -0.05 | -2.44 | 1.72 | -20.27 | 0.21 | 0.29 | 751 | 12138.74 |
| recency_regression | ERCO | 4.36 | 3.48 | -1.27 | -3.05 | 1.49 | -24.41 | 0.24 | 0.23 | 750 | 46788.33 |
| recency_regression | ISNE | 5.24 | 4.72 | -0.81 | -2.55 | 0.72 | -20.97 | 0.09 | 0.17 | 752 | 13392.81 |
| recency_regression | MISO | 3.76 | 3.16 | -0.89 | -2.42 | 2.50 | -24.00 | 0.33 | 0.05 | 747 | 73810.76 |
| recency_regression | NYIS | 3.90 | 3.24 | -0.48 | -2.13 | 0.95 | -26.14 | 0.33 | 0.63 | 752 | 17400.75 |
| recency_regression | PJM | 4.36 | 3.75 | 0.15 | -2.21 | 2.19 | -22.47 | 0.46 | 0.50 | 744 | 91927.69 |
| recency_regression | SWPP | 3.88 | 3.01 | -0.34 | -2.25 | 1.70 | -18.84 | 0.49 | 0.07 | 749 | 31365.51 |
| recency_regression | TVA | 4.67 | 4.18 | -0.57 | -2.72 | 1.81 | -19.34 | 0.14 | 0.26 | 741 | 18592.18 |
| same_type_mean_2w | BPAT | 5.96 | 4.89 | -1.36 | -3.89 | 2.74 | -26.04 | 0.13 | 0.23 | 750 | 6533.15 |
| same_type_mean_2w | CISO | 5.23 | 3.89 | -0.08 | -2.88 | 0.47 | -29.37 | 0.26 | 0.25 | 737 | 25196.91 |
| same_type_mean_2w | DUK | 9.01 | 7.35 | -2.58 | -6.42 | 2.81 | -41.75 | 0.10 | 0.21 | 751 | 12138.74 |
| same_type_mean_2w | ERCO | 8.38 | 6.57 | -2.17 | -5.60 | 2.55 | -41.15 | 0.08 | 0.20 | 750 | 46788.33 |
| same_type_mean_2w | ISNE | 8.19 | 6.11 | -0.08 | -3.77 | 0.57 | -39.84 | 0.07 | 0.19 | 752 | 13392.81 |
| same_type_mean_2w | MISO | 5.90 | 4.43 | -0.78 | -3.60 | 2.71 | -24.94 | 0.23 | 0.06 | 747 | 73810.76 |
| same_type_mean_2w | NYIS | 6.57 | 4.75 | -0.18 | -3.46 | 0.62 | -34.70 | 0.21 | 0.57 | 752 | 17400.75 |
| same_type_mean_2w | PJM | 7.20 | 5.40 | -1.20 | -4.46 | 3.15 | -35.28 | 0.26 | 0.40 | 744 | 91927.69 |
| same_type_mean_2w | SWPP | 7.32 | 5.47 | -1.27 | -4.61 | 2.47 | -30.81 | 0.30 | 0.07 | 749 | 31365.51 |
| same_type_mean_2w | TVA | 9.70 | 7.83 | -2.28 | -6.42 | 3.33 | -47.85 | 0.04 | 0.24 | 741 | 18592.18 |
| same_weekday_last_week | BPAT | 6.92 | 5.42 | -1.27 | -4.45 | 2.94 | -26.24 | 0.09 | 0.20 | 750 | 6533.15 |
| same_weekday_last_week | CISO | 6.41 | 4.47 | -0.00 | -3.53 | 0.58 | -36.14 | 0.19 | 0.26 | 737 | 25196.91 |
| same_weekday_last_week | DUK | 11.20 | 9.51 | -2.54 | -7.74 | 3.38 | -48.59 | 0.07 | 0.22 | 751 | 12138.74 |
| same_weekday_last_week | ERCO | 10.04 | 7.97 | -2.17 | -6.56 | 3.03 | -46.25 | 0.08 | 0.20 | 750 | 46788.33 |
| same_weekday_last_week | ISNE | 10.03 | 7.63 | -0.10 | -4.68 | 0.81 | -48.77 | 0.05 | 0.17 | 752 | 13392.81 |
| same_weekday_last_week | MISO | 7.20 | 5.47 | -0.86 | -4.34 | 3.19 | -32.06 | 0.19 | 0.05 | 747 | 73810.76 |
| same_weekday_last_week | NYIS | 8.02 | 5.84 | -0.19 | -4.22 | 0.89 | -48.88 | 0.14 | 0.54 | 752 | 17400.75 |
| same_weekday_last_week | PJM | 8.87 | 7.05 | -1.18 | -5.40 | 3.29 | -45.11 | 0.18 | 0.38 | 744 | 91927.69 |
| same_weekday_last_week | SWPP | 8.57 | 6.47 | -1.11 | -5.26 | 2.93 | -36.78 | 0.23 | 0.07 | 749 | 31365.51 |
| same_weekday_last_week | TVA | 11.87 | 9.43 | -2.40 | -7.58 | 3.83 | -50.54 | 0.03 | 0.25 | 741 | 18592.18 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | uri | 2.77 | -0.21 | -1.69 | -6.97 | 6 |
| DF | CISO | uri | 1.91 | 0.31 | -0.26 | -0.72 | 6 |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 24.80 | 16.54 | -0.45 | -1.69 | 6 |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.55 | 2.37 | -1.41 | -4.70 | 6 |
| DF | NYIS | uri | 2.78 | -2.59 | -2.59 | -4.66 | 6 |
| DF | PJM | uri | 2.82 | -1.01 | -1.14 | -2.03 | 6 |
| DF | SWPP | uri | 6.25 | 4.94 | 0.00 | 0.00 | 6 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| last_known_day | BPAT | uri | 5.56 | 1.23 | -1.49 | -4.90 | 6 |
| last_known_day | CISO | uri | 6.30 | -0.04 | -2.90 | -8.63 | 6 |
| last_known_day | DUK | uri | 8.80 | -6.01 | -8.05 | -15.89 | 6 |
| last_known_day | ERCO | uri | 14.77 | -8.74 | -10.36 | -20.49 | 6 |
| last_known_day | ISNE | uri | 5.40 | 0.10 | -2.20 | -6.56 | 6 |
| last_known_day | MISO | uri | 3.99 | -1.53 | -2.74 | -8.13 | 6 |
| last_known_day | NYIS | uri | 4.15 | 0.12 | -2.12 | -5.89 | 6 |
| last_known_day | PJM | uri | 4.16 | -3.17 | -4.91 | -11.49 | 6 |
| last_known_day | SWPP | uri | 6.36 | -1.04 | -1.77 | -6.47 | 6 |
| last_known_day | TVA | uri | 8.03 | -1.72 | -4.70 | -9.64 | 6 |
| profile | BPAT | uri | 9.21 | -5.26 | -7.00 | -21.28 | 6 |
| profile | CISO | uri | 2.76 | 0.39 | -0.79 | -2.24 | 6 |
| profile | DUK | uri | 11.34 | -12.81 | -12.81 | -21.53 | 6 |
| profile | ERCO | uri | 18.63 | -16.28 | -19.43 | -41.15 | 6 |
| profile | ISNE | uri | 5.94 | 3.16 | -0.80 | -4.80 | 6 |
| profile | MISO | uri | 11.09 | -9.31 | -9.98 | -21.58 | 6 |
| profile | NYIS | uri | 3.72 | 2.13 | -0.73 | -2.87 | 6 |
| profile | PJM | uri | 3.41 | -2.51 | -2.99 | -6.23 | 6 |
| profile | SWPP | uri | 13.94 | -7.21 | -10.67 | -27.71 | 6 |
| profile | TVA | uri | 16.63 | -17.66 | -17.72 | -27.35 | 6 |
| recency_regression | BPAT | uri | 3.29 | -0.43 | -1.94 | -8.29 | 6 |
| recency_regression | CISO | uri | 3.90 | -1.40 | -1.59 | -2.98 | 6 |
| recency_regression | DUK | uri | 3.90 | -2.84 | -2.84 | -6.00 | 6 |
| recency_regression | ERCO | uri | 34.66 | 17.98 | -3.06 | -15.68 | 6 |
| recency_regression | ISNE | uri | 2.87 | 0.46 | -0.47 | -1.82 | 6 |
| recency_regression | MISO | uri | 9.21 | -8.11 | -8.11 | -12.59 | 6 |
| recency_regression | NYIS | uri | 3.00 | 0.01 | -0.53 | -2.78 | 6 |
| recency_regression | PJM | uri | 5.32 | -3.87 | -3.87 | -4.74 | 6 |
| recency_regression | SWPP | uri | 8.15 | -3.23 | -5.53 | -18.84 | 6 |
| recency_regression | TVA | uri | 5.36 | -1.90 | -3.22 | -6.55 | 6 |
| same_type_mean_2w | BPAT | uri | 8.82 | -8.98 | -8.98 | -22.36 | 6 |
| same_type_mean_2w | CISO | uri | 2.26 | -0.14 | -0.53 | -1.56 | 6 |
| same_type_mean_2w | DUK | uri | 6.27 | -5.33 | -6.48 | -11.36 | 6 |
| same_type_mean_2w | ERCO | uri | 18.14 | -22.25 | -22.48 | -41.15 | 6 |
| same_type_mean_2w | ISNE | uri | 5.05 | 2.45 | -0.36 | -2.08 | 6 |
| same_type_mean_2w | MISO | uri | 11.67 | -10.56 | -10.56 | -19.03 | 6 |
| same_type_mean_2w | NYIS | uri | 3.79 | 1.66 | -0.82 | -3.09 | 6 |
| same_type_mean_2w | PJM | uri | 3.35 | -3.28 | -3.47 | -5.78 | 6 |
| same_type_mean_2w | SWPP | uri | 13.56 | -13.38 | -13.46 | -26.46 | 6 |
| same_type_mean_2w | TVA | uri | 15.85 | -16.65 | -16.65 | -23.25 | 6 |
| same_weekday_last_week | BPAT | uri | 9.04 | -3.45 | -6.38 | -19.27 | 6 |
| same_weekday_last_week | CISO | uri | 2.81 | -0.01 | -0.85 | -3.07 | 6 |
| same_weekday_last_week | DUK | uri | 12.99 | -15.36 | -15.36 | -23.49 | 6 |
| same_weekday_last_week | ERCO | uri | 19.53 | -18.69 | -21.22 | -46.25 | 6 |
| same_weekday_last_week | ISNE | uri | 6.58 | 1.82 | -0.99 | -5.94 | 6 |
| same_weekday_last_week | MISO | uri | 9.16 | -8.68 | -8.90 | -12.38 | 6 |
| same_weekday_last_week | NYIS | uri | 4.44 | 1.34 | -1.02 | -5.42 | 6 |
| same_weekday_last_week | PJM | uri | 4.20 | -3.84 | -3.85 | -9.55 | 6 |
| same_weekday_last_week | SWPP | uri | 11.82 | -9.51 | -10.67 | -19.53 | 6 |
| same_weekday_last_week | TVA | uri | 17.66 | -17.83 | -17.83 | -30.39 | 6 |
| DF | BPAT | elliott | 2.46 | 1.82 | -0.21 | -1.03 | 5 |
| DF | CISO | elliott | 4.61 | 1.17 | -0.98 | -4.88 | 5 |
| DF | DUK | elliott | 4.77 | -4.96 | -4.96 | -10.55 | 5 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | NYIS | elliott | 3.80 | -3.38 | -3.40 | -6.33 | 5 |
| DF | PJM | elliott | 4.02 | -3.14 | -3.14 | -5.88 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 3.98 | -2.36 | -3.48 | -8.57 | 5 |
| last_known_day | BPAT | elliott | 16.65 | 9.54 | -3.69 | -12.35 | 5 |
| last_known_day | CISO | elliott | 7.28 | 5.67 | -0.65 | -3.27 | 5 |
| last_known_day | DUK | elliott | 16.20 | -11.73 | -13.97 | -39.03 | 5 |
| last_known_day | ERCO | elliott | 22.52 | -6.55 | -12.98 | -33.14 | 5 |
| last_known_day | ISNE | elliott | 5.75 | 1.27 | -1.62 | -5.04 | 5 |
| last_known_day | MISO | elliott | 10.19 | -2.25 | -6.65 | -15.11 | 5 |
| last_known_day | NYIS | elliott | 5.81 | 0.58 | -2.12 | -6.27 | 5 |
| last_known_day | PJM | elliott | 11.75 | -3.11 | -7.30 | -19.23 | 5 |
| last_known_day | SWPP | elliott | 15.08 | -1.66 | -5.68 | -20.35 | 5 |
| last_known_day | TVA | elliott | 21.19 | -12.82 | -15.62 | -39.75 | 5 |
| profile | BPAT | elliott | 11.57 | -3.84 | -7.72 | -15.77 | 5 |
| profile | CISO | elliott | 6.73 | 6.86 | -0.06 | -0.30 | 5 |
| profile | DUK | elliott | 24.52 | -28.29 | -28.65 | -45.59 | 5 |
| profile | ERCO | elliott | 22.24 | -32.34 | -32.34 | -40.42 | 5 |
| profile | ISNE | elliott | 8.88 | -3.16 | -6.30 | -15.14 | 5 |
| profile | MISO | elliott | 14.08 | -15.53 | -15.53 | -24.75 | 5 |
| profile | NYIS | elliott | 9.18 | -7.26 | -7.84 | -17.00 | 5 |
| profile | PJM | elliott | 16.64 | -17.72 | -18.05 | -33.55 | 5 |
| profile | SWPP | elliott | 15.89 | -19.05 | -19.05 | -25.25 | 5 |
| profile | TVA | elliott | 29.70 | -37.33 | -37.33 | -54.16 | 5 |
| recency_regression | BPAT | elliott | 4.54 | -0.44 | -2.10 | -6.58 | 5 |
| recency_regression | CISO | elliott | 7.39 | 5.61 | 0.00 | 0.00 | 5 |
| recency_regression | DUK | elliott | 5.44 | -4.14 | -4.43 | -9.81 | 5 |
| recency_regression | ERCO | elliott | 10.81 | 5.82 | -5.94 | -14.70 | 5 |
| recency_regression | ISNE | elliott | 4.23 | 6.39 | -0.23 | -1.17 | 5 |
| recency_regression | MISO | elliott | 6.79 | -7.47 | -7.80 | -24.00 | 5 |
| recency_regression | NYIS | elliott | 3.41 | -0.50 | -2.15 | -4.65 | 5 |
| recency_regression | PJM | elliott | 7.05 | -8.07 | -8.11 | -16.86 | 5 |
| recency_regression | SWPP | elliott | 4.46 | -4.82 | -4.82 | -7.33 | 5 |
| recency_regression | TVA | elliott | 7.73 | -4.02 | -7.34 | -19.05 | 5 |
| same_type_mean_2w | BPAT | elliott | 12.88 | -2.80 | -7.29 | -18.02 | 5 |
| same_type_mean_2w | CISO | elliott | 7.37 | 5.44 | -0.05 | -0.24 | 5 |
| same_type_mean_2w | DUK | elliott | 17.04 | -24.85 | -24.85 | -41.75 | 5 |
| same_type_mean_2w | ERCO | elliott | 21.77 | -27.09 | -27.87 | -37.49 | 5 |
| same_type_mean_2w | ISNE | elliott | 7.18 | -1.55 | -3.63 | -9.96 | 5 |
| same_type_mean_2w | MISO | elliott | 12.87 | -13.75 | -14.09 | -21.43 | 5 |
| same_type_mean_2w | NYIS | elliott | 6.91 | -4.99 | -5.00 | -13.30 | 5 |
| same_type_mean_2w | PJM | elliott | 12.12 | -14.67 | -14.67 | -27.62 | 5 |
| same_type_mean_2w | SWPP | elliott | 15.82 | -17.58 | -17.58 | -27.56 | 5 |
| same_type_mean_2w | TVA | elliott | 22.62 | -30.73 | -30.73 | -47.85 | 5 |
| same_weekday_last_week | BPAT | elliott | 14.30 | 3.45 | -4.32 | -13.83 | 5 |
| same_weekday_last_week | CISO | elliott | 9.46 | 7.81 | 0.00 | 0.00 | 5 |
| same_weekday_last_week | DUK | elliott | 15.65 | -18.93 | -18.93 | -33.71 | 5 |
| same_weekday_last_week | ERCO | elliott | 20.14 | -25.04 | -25.04 | -37.45 | 5 |
| same_weekday_last_week | ISNE | elliott | 7.21 | -0.47 | -2.34 | -11.64 | 5 |
| same_weekday_last_week | MISO | elliott | 11.39 | -10.63 | -11.75 | -20.10 | 5 |
| same_weekday_last_week | NYIS | elliott | 6.89 | -3.48 | -4.13 | -13.00 | 5 |
| same_weekday_last_week | PJM | elliott | 11.06 | -13.89 | -13.91 | -26.00 | 5 |
| same_weekday_last_week | SWPP | elliott | 11.47 | -13.24 | -13.24 | -24.76 | 5 |
| same_weekday_last_week | TVA | elliott | 19.10 | -24.57 | -24.57 | -41.53 | 5 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| last_known_day | BPAT | mape | 27.400 | 0.000 | 750 |
| last_known_day | CISO | mape | 24.697 | 0.000 | 737 |
| last_known_day | DUK | mape | 30.342 | 0.000 | 751 |
| last_known_day | ERCO | mape | 22.335 | 0.000 | 750 |
| last_known_day | ISNE | mape | 28.449 | 0.000 | 752 |
| last_known_day | MISO | mape | 22.723 | 0.000 | 747 |
| last_known_day | NYIS | mape | 23.578 | 0.000 | 752 |
| last_known_day | PJM | mape | 20.318 | 0.000 | 744 |
| last_known_day | SWPP | mape | 13.942 | 0.000 | 749 |
| last_known_day | TVA | mape | 30.386 | 0.000 | 741 |
| profile | BPAT | mape | 23.330 | 0.000 | 750 |
| profile | CISO | mape | 18.131 | 0.000 | 737 |
| profile | DUK | mape | 25.038 | 0.000 | 751 |
| profile | ERCO | mape | 21.043 | 0.000 | 750 |
| profile | ISNE | mape | 27.774 | 0.000 | 752 |
| profile | MISO | mape | 18.285 | 0.000 | 747 |
| profile | NYIS | mape | 19.757 | 0.000 | 752 |
| profile | PJM | mape | 18.241 | 0.000 | 744 |
| profile | SWPP | mape | 13.945 | 0.000 | 749 |
| profile | TVA | mape | 26.672 | 0.000 | 741 |
| recency_regression | BPAT | mape | 21.557 | 0.000 | 750 |
| recency_regression | CISO | mape | 25.972 | 0.000 | 737 |
| recency_regression | DUK | mape | 19.589 | 0.000 | 751 |
| recency_regression | ERCO | mape | 14.559 | 0.000 | 750 |
| recency_regression | ISNE | mape | 31.208 | 0.000 | 752 |
| recency_regression | MISO | mape | 11.559 | 0.000 | 747 |
| recency_regression | NYIS | mape | 12.890 | 0.000 | 752 |
| recency_regression | PJM | mape | 7.753 | 0.000 | 744 |
| recency_regression | SWPP | mape | 0.116 | 0.908 | 749 |
| recency_regression | TVA | mape | 27.181 | 0.000 | 741 |
| same_type_mean_2w | BPAT | mape | 26.086 | 0.000 | 750 |
| same_type_mean_2w | CISO | mape | 14.010 | 0.000 | 737 |
| same_type_mean_2w | DUK | mape | 27.406 | 0.000 | 751 |
| same_type_mean_2w | ERCO | mape | 21.927 | 0.000 | 750 |
| same_type_mean_2w | ISNE | mape | 24.917 | 0.000 | 752 |
| same_type_mean_2w | MISO | mape | 18.915 | 0.000 | 747 |
| same_type_mean_2w | NYIS | mape | 19.591 | 0.000 | 752 |
| same_type_mean_2w | PJM | mape | 18.337 | 0.000 | 744 |
| same_type_mean_2w | SWPP | mape | 16.654 | 0.000 | 749 |
| same_type_mean_2w | TVA | mape | 28.663 | 0.000 | 741 |
| same_weekday_last_week | BPAT | mape | 26.510 | 0.000 | 750 |
| same_weekday_last_week | CISO | mape | 17.509 | 0.000 | 737 |
| same_weekday_last_week | DUK | mape | 29.044 | 0.000 | 751 |
| same_weekday_last_week | ERCO | mape | 23.194 | 0.000 | 750 |
| same_weekday_last_week | ISNE | mape | 26.015 | 0.000 | 752 |
| same_weekday_last_week | MISO | mape | 21.821 | 0.000 | 747 |
| same_weekday_last_week | NYIS | mape | 21.625 | 0.000 | 752 |
| same_weekday_last_week | PJM | mape | 21.248 | 0.000 | 744 |
| same_weekday_last_week | SWPP | mape | 18.930 | 0.000 | 749 |
| same_weekday_last_week | TVA | mape | 27.720 | 0.000 | 741 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.997 |
| last_known_day | 0.995 |
| profile | 0.999 |
| recency_regression | 0.995 |
| same_type_mean_2w | 0.999 |
| same_weekday_last_week | 0.995 |
