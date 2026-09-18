# Phase B: floors, profile and recency regression against the BA's forecast

Day-ahead forecasts issued under the 9 a.m. cut-off for BPAT, CISO, DUK, ERCO, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, scored against the load that occurred and compared, day by day, with the BA's own day-ahead forecast reported to the EIA (`DF`). Models: the three floors (last known day, same weekday last week, mean of the same day type over two weeks), the profile of Cardinal Grid Note 2 with the regime from the HRRR forecast, and the recency-effect regression fitted on observed temperature and run on the HRRR forecast. Only BA-days on which every model produced a forecast are counted.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 3.00 | 2.70 | 0.27 | -1.12 | 1.07 | 0.00 | 0.00 | -19.98 | 7463 | 10.00 |
| recency_regression | 4.28 | 3.64 | -0.60 | -2.49 | 1.84 | 0.33 | 0.27 | -26.14 | 7463 | 10.00 |
| profile | 6.87 | 5.29 | -1.48 | -4.34 | 2.14 | 0.21 | 0.23 | -44.25 | 7463 | 10.00 |
| last_known_day | 6.95 | 5.82 | -0.91 | -4.24 | 2.55 | 0.19 | 0.24 | -44.26 | 7463 | 10.00 |
| same_type_mean_2w | 7.12 | 5.43 | -1.16 | -4.40 | 2.46 | 0.20 | 0.24 | -41.41 | 7463 | 10.00 |
| same_weekday_last_week | 8.66 | 6.73 | -1.16 | -5.26 | 2.79 | 0.15 | 0.23 | -50.54 | 7463 | 10.00 |

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
| DF | SWPP | 3.85 | 3.49 | 2.60 | -0.43 | 1.25 | -19.98 |  |  | 747 | 31342.11 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| last_known_day | BPAT | 5.26 | 4.53 | -0.78 | -3.31 | 2.51 | -27.64 | 0.11 | 0.22 | 750 | 6533.15 |
| last_known_day | CISO | 6.99 | 6.67 | 0.07 | -3.46 | 0.62 | -33.31 | 0.19 | 0.26 | 737 | 25196.91 |
| last_known_day | DUK | 9.21 | 8.24 | -1.61 | -5.91 | 2.57 | -39.52 | 0.09 | 0.25 | 750 | 12129.97 |
| last_known_day | ERCO | 6.79 | 5.34 | -1.59 | -4.58 | 2.30 | -38.07 | 0.11 | 0.18 | 746 | 46782.53 |
| last_known_day | ISNE | 8.69 | 7.30 | -0.16 | -4.35 | 0.79 | -44.26 | 0.05 | 0.19 | 752 | 13392.81 |
| last_known_day | MISO | 5.95 | 4.99 | -0.83 | -3.63 | 3.08 | -24.61 | 0.21 | 0.07 | 746 | 73788.38 |
| last_known_day | NYIS | 7.19 | 5.86 | -0.29 | -4.13 | 1.16 | -37.87 | 0.14 | 0.51 | 752 | 17400.75 |
| last_known_day | PJM | 7.31 | 6.06 | -0.85 | -4.46 | 3.20 | -33.75 | 0.25 | 0.42 | 744 | 91927.69 |
| last_known_day | SWPP | 6.13 | 4.90 | -1.17 | -4.01 | 2.73 | -40.31 | 0.32 | 0.07 | 747 | 31342.11 |
| last_known_day | TVA | 8.60 | 7.33 | -1.46 | -5.40 | 2.74 | -36.52 | 0.04 | 0.27 | 739 | 18562.62 |
| profile | BPAT | 5.78 | 4.50 | -1.71 | -3.83 | 2.36 | -30.43 | 0.13 | 0.21 | 750 | 6533.15 |
| profile | CISO | 5.54 | 4.37 | -0.44 | -3.01 | 0.54 | -27.55 | 0.20 | 0.24 | 737 | 25196.91 |
| profile | DUK | 8.60 | 6.76 | -1.99 | -5.57 | 2.30 | -37.55 | 0.11 | 0.21 | 750 | 12129.97 |
| profile | ERCO | 7.58 | 5.84 | -2.50 | -5.32 | 2.14 | -41.15 | 0.11 | 0.19 | 746 | 46782.53 |
| profile | ISNE | 7.93 | 6.34 | -1.33 | -4.28 | 0.54 | -36.25 | 0.07 | 0.15 | 752 | 13392.81 |
| profile | MISO | 5.57 | 4.29 | -0.88 | -3.35 | 2.41 | -24.75 | 0.25 | 0.06 | 746 | 73788.38 |
| profile | NYIS | 6.18 | 4.75 | -0.87 | -3.58 | 0.61 | -36.24 | 0.22 | 0.54 | 752 | 17400.75 |
| profile | PJM | 7.30 | 5.65 | -1.77 | -4.79 | 2.70 | -33.55 | 0.27 | 0.38 | 744 | 91927.69 |
| profile | SWPP | 6.73 | 4.75 | -1.10 | -4.04 | 2.12 | -28.84 | 0.35 | 0.07 | 747 | 31342.11 |
| profile | TVA | 9.29 | 7.38 | -2.21 | -6.02 | 2.83 | -44.25 | 0.05 | 0.23 | 739 | 18562.62 |
| recency_regression | BPAT | 3.80 | 3.27 | -0.70 | -2.22 | 2.06 | -18.62 | 0.20 | 0.25 | 750 | 6533.15 |
| recency_regression | CISO | 5.72 | 4.92 | -1.51 | -3.18 | 0.84 | -24.61 | 0.14 | 0.24 | 737 | 25196.91 |
| recency_regression | DUK | 4.58 | 4.16 | -0.04 | -2.43 | 1.72 | -20.27 | 0.21 | 0.29 | 750 | 12129.97 |
| recency_regression | ERCO | 4.13 | 3.46 | -1.45 | -3.06 | 1.43 | -24.41 | 0.24 | 0.23 | 746 | 46782.53 |
| recency_regression | ISNE | 5.24 | 4.72 | -0.81 | -2.55 | 0.72 | -20.97 | 0.09 | 0.17 | 752 | 13392.81 |
| recency_regression | MISO | 3.75 | 3.15 | -0.88 | -2.42 | 2.49 | -24.00 | 0.33 | 0.05 | 746 | 73788.38 |
| recency_regression | NYIS | 3.90 | 3.24 | -0.48 | -2.13 | 0.95 | -26.14 | 0.33 | 0.63 | 752 | 17400.75 |
| recency_regression | PJM | 4.36 | 3.75 | 0.15 | -2.21 | 2.19 | -22.47 | 0.46 | 0.50 | 744 | 91927.69 |
| recency_regression | SWPP | 3.86 | 3.00 | -0.34 | -2.25 | 1.68 | -18.84 | 0.49 | 0.07 | 747 | 31342.11 |
| recency_regression | TVA | 4.65 | 4.17 | -0.53 | -2.69 | 1.79 | -19.34 | 0.14 | 0.26 | 739 | 18562.62 |
| same_type_mean_2w | BPAT | 5.96 | 4.89 | -1.36 | -3.89 | 2.74 | -26.04 | 0.13 | 0.23 | 750 | 6533.15 |
| same_type_mean_2w | CISO | 5.23 | 3.89 | -0.08 | -2.88 | 0.47 | -29.37 | 0.26 | 0.25 | 737 | 25196.91 |
| same_type_mean_2w | DUK | 8.98 | 7.34 | -2.53 | -6.37 | 2.81 | -39.67 | 0.10 | 0.21 | 750 | 12129.97 |
| same_type_mean_2w | ERCO | 8.38 | 6.57 | -2.11 | -5.56 | 2.53 | -41.15 | 0.08 | 0.20 | 746 | 46782.53 |
| same_type_mean_2w | ISNE | 8.19 | 6.11 | -0.08 | -3.77 | 0.57 | -39.84 | 0.07 | 0.19 | 752 | 13392.81 |
| same_type_mean_2w | MISO | 5.89 | 4.43 | -0.77 | -3.59 | 2.72 | -24.94 | 0.23 | 0.06 | 746 | 73788.38 |
| same_type_mean_2w | NYIS | 6.57 | 4.75 | -0.18 | -3.46 | 0.62 | -34.70 | 0.21 | 0.57 | 752 | 17400.75 |
| same_type_mean_2w | PJM | 7.20 | 5.40 | -1.20 | -4.46 | 3.15 | -35.28 | 0.26 | 0.40 | 744 | 91927.69 |
| same_type_mean_2w | SWPP | 7.30 | 5.44 | -1.22 | -4.58 | 2.47 | -30.81 | 0.30 | 0.07 | 747 | 31342.11 |
| same_type_mean_2w | TVA | 9.63 | 7.81 | -2.17 | -6.32 | 3.29 | -41.41 | 0.04 | 0.24 | 739 | 18562.62 |
| same_weekday_last_week | BPAT | 6.92 | 5.42 | -1.27 | -4.45 | 2.94 | -26.24 | 0.09 | 0.20 | 750 | 6533.15 |
| same_weekday_last_week | CISO | 6.41 | 4.47 | -0.00 | -3.53 | 0.58 | -36.14 | 0.19 | 0.26 | 737 | 25196.91 |
| same_weekday_last_week | DUK | 11.18 | 9.50 | -2.50 | -7.70 | 3.38 | -48.59 | 0.07 | 0.22 | 750 | 12129.97 |
| same_weekday_last_week | ERCO | 10.03 | 7.94 | -2.13 | -6.53 | 3.00 | -42.88 | 0.08 | 0.21 | 746 | 46782.53 |
| same_weekday_last_week | ISNE | 10.03 | 7.63 | -0.10 | -4.68 | 0.81 | -48.77 | 0.05 | 0.17 | 752 | 13392.81 |
| same_weekday_last_week | MISO | 7.19 | 5.47 | -0.85 | -4.34 | 3.18 | -32.06 | 0.19 | 0.05 | 746 | 73788.38 |
| same_weekday_last_week | NYIS | 8.02 | 5.84 | -0.19 | -4.22 | 0.89 | -48.88 | 0.14 | 0.54 | 752 | 17400.75 |
| same_weekday_last_week | PJM | 8.87 | 7.05 | -1.18 | -5.40 | 3.29 | -45.11 | 0.18 | 0.38 | 744 | 91927.69 |
| same_weekday_last_week | SWPP | 8.57 | 6.47 | -1.08 | -5.24 | 2.92 | -36.78 | 0.23 | 0.07 | 747 | 31342.11 |
| same_weekday_last_week | TVA | 11.82 | 9.40 | -2.30 | -7.49 | 3.82 | -50.54 | 0.03 | 0.25 | 739 | 18562.62 |

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
| same_type_mean_2w | BPAT | uri | 8.82 | -8.98 | -8.98 | -22.36 | 6 |
| same_type_mean_2w | CISO | uri | 2.26 | -0.14 | -0.53 | -1.56 | 6 |
| same_type_mean_2w | DUK | uri | 6.27 | -5.33 | -6.48 | -11.36 | 6 |
| same_type_mean_2w | ERCO | uri | 37.99 | -38.26 | -38.26 | -41.15 | 2 |
| same_type_mean_2w | ISNE | uri | 5.05 | 2.45 | -0.36 | -2.08 | 6 |
| same_type_mean_2w | MISO | uri | 11.78 | -10.84 | -10.84 | -19.03 | 5 |
| same_type_mean_2w | NYIS | uri | 3.79 | 1.66 | -0.82 | -3.09 | 6 |
| same_type_mean_2w | PJM | uri | 3.35 | -3.28 | -3.47 | -5.78 | 6 |
| same_type_mean_2w | SWPP | uri | 12.93 | -11.91 | -12.03 | -26.46 | 4 |
| same_type_mean_2w | TVA | uri | 15.85 | -16.65 | -16.65 | -23.25 | 6 |
| same_weekday_last_week | BPAT | uri | 9.04 | -3.45 | -6.38 | -19.27 | 6 |
| same_weekday_last_week | CISO | uri | 2.81 | -0.01 | -0.85 | -3.07 | 6 |
| same_weekday_last_week | DUK | uri | 12.99 | -15.36 | -15.36 | -23.49 | 6 |
| same_weekday_last_week | ERCO | uri | 35.85 | -38.33 | -38.33 | -42.88 | 2 |
| same_weekday_last_week | ISNE | uri | 6.58 | 1.82 | -0.99 | -5.94 | 6 |
| same_weekday_last_week | MISO | uri | 8.94 | -8.51 | -8.77 | -12.38 | 5 |
| same_weekday_last_week | NYIS | uri | 4.44 | 1.34 | -1.02 | -5.42 | 6 |
| same_weekday_last_week | PJM | uri | 4.20 | -3.84 | -3.85 | -9.55 | 6 |
| same_weekday_last_week | SWPP | uri | 12.91 | -7.92 | -9.67 | -19.53 | 4 |
| same_weekday_last_week | TVA | uri | 17.66 | -17.83 | -17.83 | -30.39 | 6 |
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
| same_type_mean_2w | BPAT | elliott | 12.88 | -2.80 | -7.29 | -18.02 | 5 |
| same_type_mean_2w | CISO | elliott | 7.37 | 5.44 | -0.05 | -0.24 | 5 |
| same_type_mean_2w | DUK | elliott | 12.48 | -20.63 | -20.63 | -34.10 | 4 |
| same_type_mean_2w | ERCO | elliott | 21.77 | -27.09 | -27.87 | -37.49 | 5 |
| same_type_mean_2w | ISNE | elliott | 7.18 | -1.55 | -3.63 | -9.96 | 5 |
| same_type_mean_2w | MISO | elliott | 12.87 | -13.75 | -14.09 | -21.43 | 5 |
| same_type_mean_2w | NYIS | elliott | 6.91 | -4.99 | -5.00 | -13.30 | 5 |
| same_type_mean_2w | PJM | elliott | 12.12 | -14.67 | -14.67 | -27.62 | 5 |
| same_type_mean_2w | SWPP | elliott | 15.82 | -17.58 | -17.58 | -27.56 | 5 |
| same_type_mean_2w | TVA | elliott | 12.44 | -21.79 | -21.79 | -35.73 | 3 |
| same_weekday_last_week | BPAT | elliott | 14.30 | 3.45 | -4.32 | -13.83 | 5 |
| same_weekday_last_week | CISO | elliott | 9.46 | 7.81 | 0.00 | 0.00 | 5 |
| same_weekday_last_week | DUK | elliott | 12.01 | -15.24 | -15.24 | -33.36 | 4 |
| same_weekday_last_week | ERCO | elliott | 20.14 | -25.04 | -25.04 | -37.45 | 5 |
| same_weekday_last_week | ISNE | elliott | 7.21 | -0.47 | -2.34 | -11.64 | 5 |
| same_weekday_last_week | MISO | elliott | 11.39 | -10.63 | -11.75 | -20.10 | 5 |
| same_weekday_last_week | NYIS | elliott | 6.89 | -3.48 | -4.13 | -13.00 | 5 |
| same_weekday_last_week | PJM | elliott | 11.06 | -13.89 | -13.91 | -26.00 | 5 |
| same_weekday_last_week | SWPP | elliott | 11.47 | -13.24 | -13.24 | -24.76 | 5 |
| same_weekday_last_week | TVA | elliott | 10.25 | -14.60 | -14.60 | -21.07 | 3 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 13385 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 13380 | DUK | 2022-12-24 | last_known_day | 29.05 | -39.03 | -39.03 |
| 13383 | DUK | 2022-12-24 | profile | 42.59 | -45.59 | -45.59 |
| 13384 | DUK | 2022-12-24 | recency_regression | 10.06 | -9.81 | -9.81 |
| 13382 | DUK | 2022-12-24 | same_type_mean_2w | 35.26 | -41.75 | -41.75 |
| 13381 | DUK | 2022-12-24 | same_weekday_last_week | 30.21 | -33.71 | -33.71 |
| 13877 | ERCO | 2021-02-15 | DF | 44.43 | -1.04 | -1.04 |
| 13872 | ERCO | 2021-02-15 | last_known_day | 22.77 | -15.91 | -15.91 |
| 13875 | ERCO | 2021-02-15 | profile | 12.39 | -34.83 | -34.83 |
| 13876 | ERCO | 2021-02-15 | recency_regression | 59.63 | 3.38 | 0.00 |
| 13874 | ERCO | 2021-02-15 | same_type_mean_2w | 10.23 | -40.71 | -40.71 |
| 13873 | ERCO | 2021-02-15 | same_weekday_last_week | 19.53 | -46.25 | -46.25 |
| 13883 | ERCO | 2021-02-16 | DF | 47.94 | 60.09 | 0.00 |
| 13878 | ERCO | 2021-02-16 | last_known_day | 37.95 | 9.73 | 0.00 |
| 13881 | ERCO | 2021-02-16 | profile | 10.35 | 12.52 | 0.00 |
| 13882 | ERCO | 2021-02-16 | recency_regression | 81.77 | 86.34 | 0.00 |
| 13880 | ERCO | 2021-02-16 | same_type_mean_2w | 5.99 | 1.37 | 0.00 |
| 13879 | ERCO | 2021-02-16 | same_weekday_last_week | 8.53 | -4.42 | -4.42 |
| 13889 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 13884 | ERCO | 2021-02-17 | last_known_day | 5.67 | -9.74 | -9.74 |
| 13887 | ERCO | 2021-02-17 | profile | 8.92 | 6.34 | 0.00 |
| 13888 | ERCO | 2021-02-17 | recency_regression | 47.01 | 36.53 | 0.00 |
| 13886 | ERCO | 2021-02-17 | same_type_mean_2w | 4.72 | -4.11 | -4.11 |
| 13885 | ERCO | 2021-02-17 | same_weekday_last_week | 9.02 | 7.92 | 0.00 |
| 13895 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 13890 | ERCO | 2021-02-18 | last_known_day | 14.79 | -20.49 | -20.49 |
| 13893 | ERCO | 2021-02-18 | profile | 5.37 | -5.70 | -5.70 |
| 13894 | ERCO | 2021-02-18 | recency_regression | 2.73 | -0.95 | -0.95 |
| 13892 | ERCO | 2021-02-18 | same_type_mean_2w | 11.95 | -13.54 | -13.54 |
| 13891 | ERCO | 2021-02-18 | same_weekday_last_week | 8.42 | 7.27 | 0.00 |
| 22895 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 22890 | MISO | 2021-02-16 | last_known_day | 1.83 | -5.59 | -5.59 |
| 22893 | MISO | 2021-02-16 | profile | 8.70 | -7.19 | -7.19 |
| 22894 | MISO | 2021-02-16 | recency_regression | 7.40 | -6.85 | -6.85 |
| 22892 | MISO | 2021-02-16 | same_type_mean_2w | 11.09 | -9.19 | -9.19 |
| 22891 | MISO | 2021-02-16 | same_weekday_last_week | 10.25 | -9.56 | -9.56 |
| 36347 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 36342 | SWPP | 2021-02-15 | last_known_day | 5.65 | -6.47 | -6.47 |
| 36345 | SWPP | 2021-02-15 | profile | 9.92 | -7.53 | -7.53 |
| 36346 | SWPP | 2021-02-15 | recency_regression | 8.24 | -3.68 | -3.68 |
| 36344 | SWPP | 2021-02-15 | same_type_mean_2w | 17.22 | -15.69 | -15.69 |
| 36343 | SWPP | 2021-02-15 | same_weekday_last_week | 13.48 | -13.59 | -13.59 |
| 36353 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 36348 | SWPP | 2021-02-16 | last_known_day | 6.45 | -0.45 | -0.45 |
| 36351 | SWPP | 2021-02-16 | profile | 5.00 | -8.76 | -8.76 |
| 36352 | SWPP | 2021-02-16 | recency_regression | 7.20 | 7.97 | 0.00 |
| 36350 | SWPP | 2021-02-16 | same_type_mean_2w | 12.40 | -16.91 | -16.91 |
| 36349 | SWPP | 2021-02-16 | same_weekday_last_week | 5.80 | -11.77 | -11.77 |
| 44789 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 44784 | TVA | 2022-12-23 | last_known_day | 38.49 | -39.75 | -39.75 |
| 44787 | TVA | 2022-12-23 | profile | 33.41 | -35.97 | -35.97 |
| 44788 | TVA | 2022-12-23 | recency_regression | 17.85 | -19.05 | -19.05 |
| 44786 | TVA | 2022-12-23 | same_type_mean_2w | 38.73 | -40.43 | -40.43 |
| 44785 | TVA | 2022-12-23 | same_weekday_last_week | 34.53 | -37.50 | -37.50 |
| 44795 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 44790 | TVA | 2022-12-24 | last_known_day | 18.57 | -22.60 | -22.60 |
| 44793 | TVA | 2022-12-24 | profile | 43.83 | -54.16 | -54.16 |
| 44794 | TVA | 2022-12-24 | recency_regression | 6.63 | -13.17 | -13.17 |
| 44792 | TVA | 2022-12-24 | same_type_mean_2w | 37.04 | -47.85 | -47.85 |
| 44791 | TVA | 2022-12-24 | same_weekday_last_week | 30.25 | -41.53 | -41.53 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| last_known_day | BPAT | mape | 27.400 | 0.000 | 750 |
| last_known_day | CISO | mape | 24.697 | 0.000 | 737 |
| last_known_day | DUK | mape | 30.340 | 0.000 | 750 |
| last_known_day | ERCO | mape | 23.926 | 0.000 | 746 |
| last_known_day | ISNE | mape | 28.449 | 0.000 | 752 |
| last_known_day | MISO | mape | 22.842 | 0.000 | 746 |
| last_known_day | NYIS | mape | 23.578 | 0.000 | 752 |
| last_known_day | PJM | mape | 20.318 | 0.000 | 744 |
| last_known_day | SWPP | mape | 13.984 | 0.000 | 747 |
| last_known_day | TVA | mape | 30.622 | 0.000 | 739 |
| profile | BPAT | mape | 23.330 | 0.000 | 750 |
| profile | CISO | mape | 18.131 | 0.000 | 737 |
| profile | DUK | mape | 25.188 | 0.000 | 750 |
| profile | ERCO | mape | 23.400 | 0.000 | 746 |
| profile | ISNE | mape | 27.774 | 0.000 | 752 |
| profile | MISO | mape | 18.272 | 0.000 | 746 |
| profile | NYIS | mape | 19.757 | 0.000 | 752 |
| profile | PJM | mape | 18.241 | 0.000 | 744 |
| profile | SWPP | mape | 13.968 | 0.000 | 747 |
| profile | TVA | mape | 26.870 | 0.000 | 739 |
| recency_regression | BPAT | mape | 21.557 | 0.000 | 750 |
| recency_regression | CISO | mape | 25.972 | 0.000 | 737 |
| recency_regression | DUK | mape | 19.558 | 0.000 | 750 |
| recency_regression | ERCO | mape | 16.367 | 0.000 | 746 |
| recency_regression | ISNE | mape | 31.208 | 0.000 | 752 |
| recency_regression | MISO | mape | 11.555 | 0.000 | 746 |
| recency_regression | NYIS | mape | 12.890 | 0.000 | 752 |
| recency_regression | PJM | mape | 7.753 | 0.000 | 744 |
| recency_regression | SWPP | mape | 0.109 | 0.913 | 747 |
| recency_regression | TVA | mape | 27.354 | 0.000 | 739 |
| same_type_mean_2w | BPAT | mape | 26.086 | 0.000 | 750 |
| same_type_mean_2w | CISO | mape | 14.010 | 0.000 | 737 |
| same_type_mean_2w | DUK | mape | 27.460 | 0.000 | 750 |
| same_type_mean_2w | ERCO | mape | 24.213 | 0.000 | 746 |
| same_type_mean_2w | ISNE | mape | 24.917 | 0.000 | 752 |
| same_type_mean_2w | MISO | mape | 18.884 | 0.000 | 746 |
| same_type_mean_2w | NYIS | mape | 19.591 | 0.000 | 752 |
| same_type_mean_2w | PJM | mape | 18.337 | 0.000 | 744 |
| same_type_mean_2w | SWPP | mape | 16.591 | 0.000 | 747 |
| same_type_mean_2w | TVA | mape | 28.866 | 0.000 | 739 |
| same_weekday_last_week | BPAT | mape | 26.510 | 0.000 | 750 |
| same_weekday_last_week | CISO | mape | 17.509 | 0.000 | 737 |
| same_weekday_last_week | DUK | mape | 29.001 | 0.000 | 750 |
| same_weekday_last_week | ERCO | mape | 24.598 | 0.000 | 746 |
| same_weekday_last_week | ISNE | mape | 26.015 | 0.000 | 752 |
| same_weekday_last_week | MISO | mape | 21.801 | 0.000 | 746 |
| same_weekday_last_week | NYIS | mape | 21.625 | 0.000 | 752 |
| same_weekday_last_week | PJM | mape | 21.248 | 0.000 | 744 |
| same_weekday_last_week | SWPP | mape | 18.936 | 0.000 | 747 |
| same_weekday_last_week | TVA | mape | 27.650 | 0.000 | 739 |

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
