# Main article: reference forecasts on the 43 BAs, 2023 to 2025

All BAs of the station map, 2023-01-01 to 2025-12-31, protocol v2: the vanilla regression of Hong (2010) on calendar and temperature (`vanilla`, fed the same temperature path as the recipe), the mean of the same day type over the last two weeks (`same_type_mean_2w`), the same weekday a week before (`same_weekday_last_week`) and the last 24 known hours (`last_known_day`). The recipe's own numbers are in `docs/evaluation_43_bas.md` on the same days.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | 3.59 | 3.20 | -0.81 | -2.07 | 1.05 | 0.00 | 0.00 | -49.40 | 45546 | 43.00 |
| vanilla | 3.81 | 3.26 | -1.04 | -2.45 | 1.51 | 0.40 | 0.29 | -44.47 | 45546 | 43.00 |
| last_known_day | 6.63 | 5.62 | -1.11 | -4.24 | 2.37 | 0.21 | 0.29 | -70.01 | 45546 | 43.00 |
| same_type_mean_2w | 7.46 | 5.86 | -1.29 | -4.72 | 2.29 | 0.21 | 0.28 | -54.70 | 45546 | 43.00 |
| same_weekday_last_week | 8.63 | 6.70 | -1.31 | -5.38 | 2.59 | 0.19 | 0.28 | -61.30 | 45546 | 43.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | AECI | 2.90 | 2.36 | -0.81 | -1.88 | 0.99 | -15.49 |  |  | 1087 | 2578.11 |
| DF | AVA | 1.75 | 1.50 | -0.35 | -1.16 | 1.28 | -14.38 |  |  | 1077 | 1484.63 |
| DF | AZPS | 5.92 | 4.49 | -2.63 | -3.33 | 1.35 | -26.51 |  |  | 1078 | 4128.08 |
| DF | BANC | 2.22 | 1.86 | -0.12 | -1.47 | 0.96 | -32.40 |  |  | 1049 | 1999.54 |
| DF | BPAT | 2.00 | 1.80 | -0.38 | -1.20 | 1.24 | -15.51 |  |  | 1087 | 6761.53 |
| DF | CISO | 5.36 | 5.12 | -1.73 | -2.61 | 1.18 | -33.79 |  |  | 1067 | 25391.65 |
| DF | CPLE | 4.10 | 3.39 | 1.03 | -1.47 | 1.21 | -20.38 |  |  | 1082 | 6997.57 |
| DF | CPLW | 4.63 | 3.83 | -1.11 | -3.05 | 1.48 | -33.07 |  |  | 1073 | 548.13 |
| DF | DUK | 2.65 | 2.30 | 0.43 | -1.26 | 1.01 | -13.08 |  |  | 1083 | 12276.58 |
| DF | EPE | 3.20 | 2.87 | -1.43 | -2.57 | 0.78 | -33.46 |  |  | 1088 | 1047.27 |
| DF | ERCO | 2.40 | 1.99 | 0.78 | -0.80 | 1.01 | -11.36 |  |  | 1081 | 53269.08 |
| DF | FMPP | 4.28 | 3.83 | -0.50 | -1.99 | 1.12 | -24.04 |  |  | 1029 | 2184.84 |
| DF | FPC | 23.12 | 23.15 | -24.42 | -24.42 | 0.82 | -37.74 |  |  | 1081 | 6593.53 |
| DF | FPL | 3.21 | 3.06 | -0.59 | -1.70 | 1.12 | -41.79 |  |  | 1038 | 16569.15 |
| DF | GCPD | 2.17 | 1.84 | -1.64 | -1.93 | 1.13 | -12.83 |  |  | 1086 | 749.09 |
| DF | IPCO | 3.53 | 2.87 | -0.71 | -1.98 | 1.95 | -35.63 |  |  | 1086 | 2131.15 |
| DF | ISNE | 2.57 | 2.51 | 0.39 | -0.45 | 0.33 | -5.42 |  |  | 1083 | 12997.26 |
| DF | JEA | 4.75 | 4.24 | 0.08 | -1.75 | 1.09 | -19.07 |  |  | 1065 | 1550.04 |
| DF | LDWP | 8.06 | 7.12 | -8.34 | -9.28 | 2.73 | -34.92 |  |  | 1039 | 2716.30 |
| DF | LGEE | 7.85 | 7.87 | -8.83 | -8.89 | 1.38 | -19.65 |  |  | 1095 | 4278.20 |
| DF | MISO | 2.71 | 2.50 | 2.02 | -0.23 | 0.85 | -6.54 |  |  | 1088 | 74077.99 |
| DF | NEVP | 6.22 | 5.99 | -5.93 | -6.17 | 1.32 | -38.58 |  |  | 1041 | 4544.12 |
| DF | NWMT | 1.95 | 1.62 | -1.15 | -1.68 | 1.75 | -20.72 |  |  | 1049 | 1359.63 |
| DF | NYIS | 2.62 | 2.47 | -2.42 | -2.58 | 0.43 | -10.12 |  |  | 1074 | 17101.47 |
| DF | PACE | 4.33 | 3.68 | 1.21 | -1.16 | 2.19 | -13.22 |  |  | 1083 | 5975.48 |
| DF | PACW | 4.38 | 3.40 | 2.14 | -0.74 | 1.57 | -13.23 |  |  | 1018 | 2409.10 |
| DF | PGE | 1.33 | 1.14 | -0.13 | -0.95 | 1.17 | -9.74 |  |  | 1087 | 2611.80 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1073 | 93074.23 |
| DF | PNM | 6.27 | 6.37 | -5.92 | -6.01 | 1.23 | -23.64 |  |  | 1095 | 1668.76 |
| DF | PSCO | 6.05 | 5.78 | -7.20 | -7.44 | 2.25 | -27.29 |  |  | 1046 | 5110.47 |
| DF | PSEI | 22.60 | 21.39 | -28.54 | -28.56 | 4.67 | -49.40 |  |  | 894 | 2868.75 |
| DF | SC | 3.52 | 3.15 | 0.40 | -1.13 | 1.35 | -17.22 |  |  | 1078 | 3064.92 |
| DF | SCEG | 4.57 | 4.52 | -4.28 | -4.60 | 1.66 | -24.28 |  |  | 1045 | 2791.89 |
| DF | SCL | 3.29 | 3.02 | -2.84 | -3.34 | 1.50 | -23.98 |  |  | 1067 | 1080.31 |
| DF | SOCO | 1.70 | 1.70 | -0.66 | -0.84 | 0.32 | -10.51 |  |  | 1081 | 27033.88 |
| DF | SRP | 3.23 | 2.91 | -2.81 | -3.30 | 1.01 | -29.84 |  |  | 1038 | 4047.71 |
| DF | SWPP | 4.33 | 2.47 | 1.42 | -1.38 | 1.48 | -17.10 |  |  | 1078 | 33075.46 |
| DF | TEC | 4.47 | 3.79 | 0.09 | -1.85 | 1.05 | -21.45 |  |  | 1072 | 2562.38 |
| DF | TEPC | 4.31 | 2.68 | -0.37 | -2.06 | 0.92 | -14.84 |  |  | 1065 | 1647.75 |
| DF | TPWR | 2.41 | 2.00 | 0.25 | -0.98 | 1.26 | -25.00 |  |  | 1087 | 527.80 |
| DF | TVA | 2.28 | 1.96 | 0.58 | -0.89 | 1.01 | -8.44 |  |  | 1084 | 18791.86 |
| DF | WACM | 15.42 | 15.47 | -17.49 | -17.49 | 3.04 | -48.69 |  |  | 960 | 3856.17 |
| DF | WALC | 9.66 | 8.54 | -5.32 | -8.17 | 2.73 | -48.02 |  |  | 889 | 1015.38 |
| last_known_day | AECI | 10.22 | 8.23 | -1.81 | -6.43 | 2.38 | -59.39 | 0.06 | 0.25 | 1087 | 2578.11 |
| last_known_day | AVA | 5.73 | 4.87 | -1.07 | -3.90 | 2.64 | -26.94 | 0.07 | 0.26 | 1077 | 1484.63 |
| last_known_day | AZPS | 6.56 | 5.53 | -0.97 | -3.82 | 1.66 | -27.27 | 0.43 | 0.44 | 1078 | 4128.08 |
| last_known_day | BANC | 7.39 | 6.07 | -0.74 | -4.98 | 2.06 | -43.23 | 0.07 | 0.25 | 1049 | 1999.54 |
| last_known_day | BPAT | 4.79 | 4.19 | -0.80 | -3.20 | 2.25 | -23.24 | 0.12 | 0.30 | 1087 | 6761.53 |
| last_known_day | CISO | 6.73 | 6.15 | -0.68 | -3.70 | 1.77 | -26.69 | 0.42 | 0.36 | 1067 | 25391.65 |
| last_known_day | CPLE | 10.35 | 8.40 | -1.81 | -6.44 | 2.68 | -53.69 | 0.12 | 0.19 | 1082 | 6997.57 |
| last_known_day | CPLW | 9.60 | 7.77 | -2.78 | -6.63 | 2.61 | -46.59 | 0.17 | 0.29 | 1073 | 548.13 |
| last_known_day | DUK | 8.68 | 7.54 | -1.48 | -5.83 | 2.33 | -45.63 | 0.07 | 0.22 | 1083 | 12276.58 |
| last_known_day | EPE | 7.64 | 6.74 | -1.14 | -4.87 | 1.32 | -38.58 | 0.10 | 0.33 | 1088 | 1047.27 |
| last_known_day | ERCO | 5.83 | 4.76 | -1.31 | -4.04 | 1.99 | -39.15 | 0.14 | 0.16 | 1081 | 53269.08 |
| last_known_day | FMPP | 7.25 | 6.26 | -1.86 | -5.16 | 1.73 | -31.26 | 0.24 | 0.25 | 1029 | 2184.84 |
| last_known_day | FPC | 8.13 | 6.69 | -1.99 | -5.55 | 1.80 | -38.99 | 0.97 | 0.98 | 1081 | 6593.53 |
| last_known_day | FPL | 6.36 | 5.29 | -1.13 | -4.35 | 1.53 | -37.57 | 0.19 | 0.25 | 1038 | 16569.15 |
| last_known_day | GCPD | 3.72 | 3.23 | -0.65 | -2.43 | 1.78 | -20.74 | 0.26 | 0.42 | 1086 | 749.09 |
| last_known_day | IPCO | 5.70 | 5.07 | -1.19 | -3.85 | 2.51 | -30.64 | 0.26 | 0.29 | 1086 | 2131.15 |
| last_known_day | ISNE | 8.96 | 7.64 | -0.40 | -4.04 | 0.78 | -39.44 | 0.06 | 0.18 | 1083 | 12997.26 |
| last_known_day | JEA | 8.98 | 7.61 | -2.96 | -6.44 | 2.33 | -44.36 | 0.20 | 0.20 | 1065 | 1550.04 |
| last_known_day | LDWP | 7.93 | 7.10 | -3.65 | -6.59 | 2.76 | -48.23 | 0.54 | 0.62 | 1039 | 2716.30 |
| last_known_day | LGEE | 9.54 | 8.16 | -2.03 | -6.28 | 2.81 | -41.98 | 0.47 | 0.68 | 1095 | 4278.20 |
| last_known_day | MISO | 5.69 | 4.94 | -0.75 | -3.52 | 2.81 | -27.21 | 0.22 | 0.07 | 1088 | 74077.99 |
| last_known_day | NEVP | 4.95 | 4.01 | -1.02 | -3.47 | 1.33 | -32.32 | 0.69 | 0.72 | 1041 | 4544.12 |
| last_known_day | NWMT | 4.62 | 3.78 | -1.64 | -3.49 | 3.34 | -24.53 | 0.10 | 0.33 | 1049 | 1359.63 |
| last_known_day | NYIS | 6.91 | 5.67 | -0.44 | -3.71 | 0.93 | -32.79 | 0.15 | 0.55 | 1074 | 17101.47 |
| last_known_day | PACE | 4.88 | 4.32 | -1.85 | -3.64 | 3.09 | -26.80 | 0.42 | 0.18 | 1083 | 5975.48 |
| last_known_day | PACW | 6.32 | 5.64 | -0.98 | -4.08 | 2.16 | -31.10 | 0.32 | 0.16 | 1018 | 2409.10 |
| last_known_day | PGE | 6.25 | 5.40 | -0.77 | -4.06 | 2.50 | -31.21 | 0.02 | 0.25 | 1087 | 2611.80 |
| last_known_day | PJM | 6.56 | 5.56 | -0.78 | -4.11 | 2.89 | -27.12 | 0.13 | 0.32 | 1073 | 93074.23 |
| last_known_day | PNM | 4.93 | 4.33 | -1.40 | -3.25 | 2.38 | -28.43 | 0.70 | 0.76 | 1095 | 1668.76 |
| last_known_day | PSCO | 7.63 | 6.64 | -2.64 | -5.60 | 2.86 | -70.01 | 0.40 | 0.62 | 1046 | 5110.47 |
| last_known_day | PSEI | 6.00 | 5.20 | -0.76 | -3.88 | 2.22 | -26.34 | 0.97 | 0.98 | 894 | 2868.75 |
| last_known_day | SC | 7.82 | 6.02 | -2.37 | -5.60 | 2.89 | -47.97 | 0.15 | 0.20 | 1078 | 3064.92 |
| last_known_day | SCEG | 8.71 | 7.19 | -2.36 | -6.15 | 2.58 | -52.75 | 0.24 | 0.48 | 1045 | 2791.89 |
| last_known_day | SCL | 6.10 | 5.42 | -1.85 | -4.29 | 3.09 | -25.12 | 0.18 | 0.45 | 1067 | 1080.31 |
| last_known_day | SOCO | 7.59 | 6.22 | -1.34 | -4.96 | 2.22 | -45.55 | 0.04 | 0.40 | 1081 | 27033.88 |
| last_known_day | SRP | 6.29 | 5.09 | -1.06 | -4.20 | 1.39 | -39.13 | 0.20 | 0.49 | 1038 | 4047.71 |
| last_known_day | SWPP | 5.74 | 4.91 | -1.21 | -3.92 | 2.73 | -30.27 | 0.31 | 0.23 | 1078 | 33075.46 |
| last_known_day | TEC | 7.85 | 6.67 | -2.36 | -5.58 | 1.89 | -45.94 | 0.23 | 0.23 | 1072 | 2562.38 |
| last_known_day | TEPC | 6.19 | 5.29 | -1.33 | -3.93 | 1.65 | -44.37 | 0.25 | 0.34 | 1065 | 1647.75 |
| last_known_day | TPWR | 6.60 | 5.74 | -1.54 | -4.45 | 3.13 | -26.46 | 0.10 | 0.19 | 1087 | 527.80 |
| last_known_day | TVA | 8.14 | 6.82 | -1.70 | -5.34 | 2.65 | -33.85 | 0.07 | 0.19 | 1084 | 18791.86 |
| last_known_day | WACM | 5.16 | 4.60 | -2.55 | -4.12 | 3.41 | -34.62 | 0.98 | 0.99 | 960 | 3856.17 |
| last_known_day | WALC | 6.55 | 5.97 | -2.99 | -5.36 | 2.20 | -44.07 | 0.72 | 0.51 | 889 | 1015.38 |
| same_type_mean_2w | AECI | 14.29 | 11.19 | -1.22 | -7.87 | 2.68 | -41.53 | 0.05 | 0.29 | 1087 | 2578.11 |
| same_type_mean_2w | AVA | 6.57 | 5.12 | -1.00 | -4.33 | 2.34 | -32.05 | 0.07 | 0.23 | 1077 | 1484.63 |
| same_type_mean_2w | AZPS | 8.11 | 6.67 | -1.16 | -4.69 | 1.76 | -37.04 | 0.36 | 0.43 | 1078 | 4128.08 |
| same_type_mean_2w | BANC | 7.91 | 6.02 | -0.51 | -5.41 | 1.86 | -45.93 | 0.07 | 0.24 | 1049 | 1999.54 |
| same_type_mean_2w | BPAT | 5.58 | 4.28 | -1.15 | -3.84 | 2.42 | -34.86 | 0.13 | 0.28 | 1087 | 6761.53 |
| same_type_mean_2w | CISO | 5.42 | 4.29 | -0.78 | -3.37 | 1.24 | -32.64 | 0.56 | 0.36 | 1067 | 25391.65 |
| same_type_mean_2w | CPLE | 12.34 | 9.78 | -2.34 | -7.68 | 2.79 | -47.04 | 0.11 | 0.19 | 1082 | 6997.57 |
| same_type_mean_2w | CPLW | 11.89 | 8.54 | -2.99 | -7.96 | 2.92 | -49.52 | 0.16 | 0.22 | 1073 | 548.13 |
| same_type_mean_2w | DUK | 9.82 | 8.04 | -1.90 | -6.55 | 2.73 | -39.60 | 0.07 | 0.22 | 1083 | 12276.58 |
| same_type_mean_2w | EPE | 7.41 | 5.91 | -0.97 | -4.64 | 1.01 | -35.77 | 0.14 | 0.34 | 1088 | 1047.27 |
| same_type_mean_2w | ERCO | 7.49 | 5.83 | -1.69 | -4.89 | 2.25 | -35.44 | 0.11 | 0.18 | 1081 | 53269.08 |
| same_type_mean_2w | FMPP | 8.23 | 6.87 | -2.55 | -5.92 | 1.73 | -43.68 | 0.23 | 0.24 | 1029 | 2184.84 |
| same_type_mean_2w | FPC | 9.85 | 8.34 | -2.82 | -6.70 | 2.10 | -54.70 | 0.95 | 0.95 | 1081 | 6593.53 |
| same_type_mean_2w | FPL | 7.75 | 6.48 | -1.48 | -4.99 | 1.41 | -40.48 | 0.15 | 0.25 | 1038 | 16569.15 |
| same_type_mean_2w | GCPD | 4.45 | 3.74 | -0.86 | -2.96 | 1.58 | -29.08 | 0.23 | 0.41 | 1086 | 749.09 |
| same_type_mean_2w | IPCO | 7.37 | 5.89 | -1.18 | -4.74 | 2.16 | -38.77 | 0.20 | 0.25 | 1086 | 2131.15 |
| same_type_mean_2w | ISNE | 8.83 | 6.99 | -0.32 | -3.84 | 0.59 | -39.91 | 0.07 | 0.18 | 1083 | 12997.26 |
| same_type_mean_2w | JEA | 10.02 | 8.29 | -3.80 | -7.34 | 2.71 | -53.64 | 0.18 | 0.19 | 1065 | 1550.04 |
| same_type_mean_2w | LDWP | 7.74 | 6.19 | -3.32 | -6.22 | 2.35 | -39.50 | 0.62 | 0.65 | 1039 | 2716.30 |
| same_type_mean_2w | LGEE | 10.22 | 7.99 | -2.29 | -6.67 | 3.08 | -32.60 | 0.47 | 0.66 | 1095 | 4278.20 |
| same_type_mean_2w | MISO | 6.14 | 4.60 | -0.71 | -3.80 | 2.39 | -26.54 | 0.23 | 0.07 | 1088 | 74077.99 |
| same_type_mean_2w | NEVP | 6.42 | 4.50 | -0.88 | -4.12 | 1.13 | -35.22 | 0.57 | 0.69 | 1041 | 4544.12 |
| same_type_mean_2w | NWMT | 5.15 | 4.08 | -1.62 | -3.70 | 2.92 | -25.06 | 0.11 | 0.34 | 1049 | 1359.63 |
| same_type_mean_2w | NYIS | 6.92 | 5.31 | -0.25 | -3.49 | 0.61 | -35.80 | 0.16 | 0.56 | 1074 | 17101.47 |
| same_type_mean_2w | PACE | 4.78 | 3.97 | -1.86 | -3.72 | 2.33 | -23.82 | 0.46 | 0.17 | 1083 | 5975.48 |
| same_type_mean_2w | PACW | 6.75 | 5.47 | -1.43 | -4.66 | 2.27 | -32.49 | 0.31 | 0.11 | 1018 | 2409.10 |
| same_type_mean_2w | PGE | 6.33 | 4.85 | -0.88 | -4.22 | 2.06 | -35.86 | 0.03 | 0.24 | 1087 | 2611.80 |
| same_type_mean_2w | PJM | 7.21 | 5.66 | -0.87 | -4.39 | 2.73 | -31.78 | 0.11 | 0.31 | 1073 | 93074.23 |
| same_type_mean_2w | PNM | 5.41 | 4.66 | -1.30 | -3.57 | 2.13 | -23.95 | 0.64 | 0.75 | 1095 | 1668.76 |
| same_type_mean_2w | PSCO | 7.06 | 5.82 | -2.60 | -5.36 | 2.40 | -36.70 | 0.47 | 0.63 | 1046 | 5110.47 |
| same_type_mean_2w | PSEI | 6.78 | 5.23 | -1.06 | -4.39 | 2.02 | -37.03 | 0.97 | 0.98 | 894 | 2868.75 |
| same_type_mean_2w | SC | 9.41 | 7.44 | -2.98 | -6.70 | 3.09 | -44.59 | 0.12 | 0.20 | 1078 | 3064.92 |
| same_type_mean_2w | SCEG | 10.13 | 8.19 | -3.11 | -6.79 | 2.60 | -42.78 | 0.21 | 0.47 | 1045 | 2791.89 |
| same_type_mean_2w | SCL | 6.18 | 4.90 | -1.28 | -3.88 | 2.16 | -32.75 | 0.26 | 0.44 | 1067 | 1080.31 |
| same_type_mean_2w | SOCO | 8.81 | 6.92 | -1.99 | -5.88 | 2.83 | -42.08 | 0.04 | 0.38 | 1081 | 27033.88 |
| same_type_mean_2w | SRP | 7.84 | 6.35 | -1.08 | -4.91 | 1.76 | -45.46 | 0.18 | 0.47 | 1038 | 4047.71 |
| same_type_mean_2w | SWPP | 7.27 | 5.68 | -1.24 | -4.71 | 2.53 | -33.78 | 0.27 | 0.22 | 1078 | 33075.46 |
| same_type_mean_2w | TEC | 8.93 | 7.40 | -2.86 | -6.31 | 1.72 | -50.54 | 0.21 | 0.21 | 1072 | 2562.38 |
| same_type_mean_2w | TEPC | 7.72 | 6.55 | -1.62 | -4.88 | 1.72 | -32.89 | 0.21 | 0.33 | 1065 | 1647.75 |
| same_type_mean_2w | TPWR | 6.92 | 5.49 | -1.76 | -4.52 | 2.66 | -35.94 | 0.12 | 0.17 | 1087 | 527.80 |
| same_type_mean_2w | TVA | 10.02 | 7.84 | -2.13 | -6.55 | 3.26 | -40.48 | 0.05 | 0.20 | 1084 | 18791.86 |
| same_type_mean_2w | WACM | 5.39 | 4.57 | -2.52 | -4.21 | 3.29 | -39.14 | 0.97 | 0.99 | 960 | 3856.17 |
| same_type_mean_2w | WALC | 8.81 | 7.75 | -5.49 | -7.63 | 2.30 | -45.55 | 0.60 | 0.39 | 889 | 1015.38 |
| same_weekday_last_week | AECI | 16.22 | 12.26 | -1.42 | -9.21 | 3.31 | -46.39 | 0.03 | 0.27 | 1087 | 2578.11 |
| same_weekday_last_week | AVA | 7.63 | 6.10 | -1.04 | -5.06 | 2.62 | -36.25 | 0.05 | 0.23 | 1077 | 1484.63 |
| same_weekday_last_week | AZPS | 9.30 | 7.90 | -1.23 | -5.41 | 2.17 | -41.54 | 0.32 | 0.43 | 1078 | 4128.08 |
| same_weekday_last_week | BANC | 9.31 | 6.94 | -0.48 | -6.37 | 2.07 | -49.52 | 0.06 | 0.25 | 1049 | 1999.54 |
| same_weekday_last_week | BPAT | 6.40 | 5.18 | -1.18 | -4.40 | 2.68 | -31.01 | 0.09 | 0.28 | 1087 | 6761.53 |
| same_weekday_last_week | CISO | 6.49 | 4.87 | -0.64 | -3.86 | 1.52 | -32.02 | 0.50 | 0.36 | 1067 | 25391.65 |
| same_weekday_last_week | CPLE | 14.39 | 11.18 | -2.54 | -8.97 | 3.37 | -55.65 | 0.09 | 0.19 | 1082 | 6997.57 |
| same_weekday_last_week | CPLW | 13.83 | 9.95 | -3.33 | -9.30 | 3.63 | -60.24 | 0.14 | 0.21 | 1073 | 548.13 |
| same_weekday_last_week | DUK | 11.50 | 9.29 | -2.07 | -7.65 | 3.37 | -43.35 | 0.05 | 0.22 | 1083 | 12276.58 |
| same_weekday_last_week | EPE | 8.31 | 6.75 | -1.06 | -5.20 | 1.19 | -43.16 | 0.11 | 0.34 | 1088 | 1047.27 |
| same_weekday_last_week | ERCO | 8.36 | 6.58 | -1.59 | -5.36 | 2.37 | -36.72 | 0.07 | 0.18 | 1081 | 53269.08 |
| same_weekday_last_week | FMPP | 9.65 | 8.13 | -2.60 | -6.88 | 2.02 | -48.20 | 0.20 | 0.25 | 1029 | 2184.84 |
| same_weekday_last_week | FPC | 11.56 | 9.76 | -2.86 | -7.77 | 2.38 | -57.04 | 0.92 | 0.91 | 1081 | 6593.53 |
| same_weekday_last_week | FPL | 9.20 | 7.77 | -1.66 | -5.82 | 1.71 | -41.41 | 0.12 | 0.27 | 1038 | 16569.15 |
| same_weekday_last_week | GCPD | 4.90 | 4.08 | -0.86 | -3.32 | 1.99 | -28.57 | 0.18 | 0.41 | 1086 | 749.09 |
| same_weekday_last_week | IPCO | 8.46 | 7.06 | -1.20 | -5.44 | 2.77 | -36.92 | 0.16 | 0.26 | 1086 | 2131.15 |
| same_weekday_last_week | ISNE | 10.63 | 8.44 | -0.42 | -4.48 | 0.89 | -46.81 | 0.05 | 0.17 | 1083 | 12997.26 |
| same_weekday_last_week | JEA | 11.90 | 9.52 | -3.73 | -8.52 | 2.94 | -61.30 | 0.17 | 0.20 | 1065 | 1550.04 |
| same_weekday_last_week | LDWP | 9.51 | 7.31 | -3.41 | -7.32 | 2.58 | -57.56 | 0.48 | 0.60 | 1039 | 2716.30 |
| same_weekday_last_week | LGEE | 12.14 | 9.88 | -2.38 | -7.73 | 3.41 | -41.77 | 0.37 | 0.63 | 1095 | 4278.20 |
| same_weekday_last_week | MISO | 6.99 | 5.20 | -0.69 | -4.26 | 2.70 | -26.85 | 0.21 | 0.06 | 1088 | 74077.99 |
| same_weekday_last_week | NEVP | 7.61 | 5.70 | -0.93 | -4.86 | 1.39 | -39.31 | 0.49 | 0.68 | 1041 | 4544.12 |
| same_weekday_last_week | NWMT | 6.02 | 4.89 | -1.61 | -4.24 | 3.28 | -31.28 | 0.07 | 0.32 | 1049 | 1359.63 |
| same_weekday_last_week | NYIS | 8.18 | 6.13 | -0.27 | -4.01 | 0.87 | -40.27 | 0.14 | 0.56 | 1074 | 17101.47 |
| same_weekday_last_week | PACE | 5.68 | 4.67 | -1.86 | -4.19 | 2.81 | -35.17 | 0.36 | 0.17 | 1083 | 5975.48 |
| same_weekday_last_week | PACW | 7.69 | 6.34 | -1.59 | -5.33 | 2.68 | -36.51 | 0.25 | 0.10 | 1018 | 2409.10 |
| same_weekday_last_week | PGE | 7.38 | 5.76 | -0.87 | -4.83 | 2.41 | -35.25 | 0.03 | 0.25 | 1087 | 2611.80 |
| same_weekday_last_week | PJM | 8.33 | 6.23 | -0.90 | -5.04 | 2.90 | -38.40 | 0.12 | 0.29 | 1073 | 93074.23 |
| same_weekday_last_week | PNM | 6.17 | 5.46 | -1.38 | -4.00 | 2.43 | -30.56 | 0.57 | 0.72 | 1095 | 1668.76 |
| same_weekday_last_week | PSCO | 8.28 | 6.85 | -2.59 | -5.98 | 2.76 | -37.80 | 0.38 | 0.61 | 1046 | 5110.47 |
| same_weekday_last_week | PSEI | 7.74 | 6.18 | -1.06 | -4.84 | 2.32 | -32.38 | 0.95 | 0.98 | 894 | 2868.75 |
| same_weekday_last_week | SC | 11.14 | 8.77 | -3.23 | -7.79 | 3.67 | -46.41 | 0.09 | 0.21 | 1078 | 3064.92 |
| same_weekday_last_week | SCEG | 12.20 | 9.69 | -3.26 | -8.21 | 3.21 | -49.40 | 0.16 | 0.46 | 1045 | 2791.89 |
| same_weekday_last_week | SCL | 6.97 | 5.66 | -1.32 | -4.42 | 2.70 | -27.87 | 0.21 | 0.44 | 1067 | 1080.31 |
| same_weekday_last_week | SOCO | 10.39 | 7.81 | -1.97 | -6.94 | 3.08 | -43.20 | 0.04 | 0.38 | 1081 | 27033.88 |
| same_weekday_last_week | SRP | 8.99 | 7.30 | -1.08 | -5.60 | 1.99 | -43.22 | 0.12 | 0.47 | 1038 | 4047.71 |
| same_weekday_last_week | SWPP | 8.21 | 6.35 | -1.34 | -5.28 | 3.21 | -33.42 | 0.24 | 0.22 | 1078 | 33075.46 |
| same_weekday_last_week | TEC | 10.52 | 8.92 | -2.80 | -7.18 | 2.03 | -50.16 | 0.16 | 0.24 | 1072 | 2562.38 |
| same_weekday_last_week | TEPC | 8.87 | 7.54 | -1.61 | -5.59 | 2.24 | -45.07 | 0.20 | 0.33 | 1065 | 1647.75 |
| same_weekday_last_week | TPWR | 7.94 | 6.41 | -1.76 | -5.15 | 3.10 | -35.29 | 0.10 | 0.17 | 1087 | 527.80 |
| same_weekday_last_week | TVA | 11.64 | 9.23 | -2.26 | -7.59 | 3.44 | -40.39 | 0.05 | 0.19 | 1084 | 18791.86 |
| same_weekday_last_week | WACM | 6.34 | 5.35 | -2.43 | -4.62 | 3.45 | -38.15 | 0.96 | 0.96 | 960 | 3856.17 |
| same_weekday_last_week | WALC | 9.62 | 8.42 | -5.25 | -8.11 | 2.73 | -48.02 | 0.15 | 0.02 | 889 | 1015.38 |
| vanilla | AECI | 6.86 | 5.74 | -0.11 | -3.13 | 1.52 | -22.96 | 0.13 | 0.35 | 1087 | 2578.11 |
| vanilla | AVA | 3.49 | 2.92 | -0.79 | -2.07 | 1.75 | -17.91 | 0.17 | 0.29 | 1077 | 1484.63 |
| vanilla | AZPS | 5.81 | 5.00 | -4.08 | -4.62 | 1.54 | -30.80 | 0.51 | 0.29 | 1078 | 4128.08 |
| vanilla | BANC | 4.31 | 3.71 | -2.48 | -3.57 | 1.66 | -31.67 | 0.12 | 0.19 | 1049 | 1999.54 |
| vanilla | BPAT | 2.86 | 2.42 | -0.95 | -1.79 | 1.39 | -15.29 | 0.32 | 0.32 | 1087 | 6761.53 |
| vanilla | CISO | 4.48 | 4.05 | -1.42 | -2.76 | 1.77 | -23.86 | 0.64 | 0.34 | 1067 | 25391.65 |
| vanilla | CPLE | 5.01 | 4.39 | -2.22 | -3.87 | 1.53 | -20.13 | 0.33 | 0.16 | 1082 | 6997.57 |
| vanilla | CPLW | 5.76 | 4.46 | -1.28 | -3.63 | 1.49 | -31.99 | 0.38 | 0.33 | 1073 | 548.13 |
| vanilla | DUK | 3.68 | 3.07 | -0.77 | -2.50 | 1.37 | -19.46 | 0.31 | 0.21 | 1083 | 12276.58 |
| vanilla | EPE | 4.88 | 4.37 | -3.34 | -4.32 | 0.94 | -32.79 | 0.24 | 0.26 | 1088 | 1047.27 |
| vanilla | ERCO | 2.86 | 2.41 | -0.89 | -2.04 | 1.12 | -19.42 | 0.39 | 0.18 | 1081 | 53269.08 |
| vanilla | FMPP | 4.42 | 3.86 | -1.33 | -3.03 | 1.17 | -21.48 | 0.52 | 0.29 | 1029 | 2184.84 |
| vanilla | FPC | 5.49 | 4.78 | -1.31 | -3.42 | 1.24 | -25.00 | 1.00 | 1.00 | 1081 | 6593.53 |
| vanilla | FPL | 4.60 | 4.05 | -1.67 | -3.08 | 1.14 | -38.05 | 0.31 | 0.25 | 1038 | 16569.15 |
| vanilla | GCPD | 3.35 | 2.66 | 0.36 | -1.34 | 1.25 | -11.75 | 0.31 | 0.53 | 1086 | 749.09 |
| vanilla | IPCO | 4.68 | 3.74 | -1.69 | -2.98 | 1.77 | -18.29 | 0.36 | 0.25 | 1086 | 2131.15 |
| vanilla | ISNE | 6.24 | 5.64 | -2.31 | -3.20 | 0.91 | -25.59 | 0.07 | 0.12 | 1083 | 12997.26 |
| vanilla | JEA | 4.49 | 4.00 | -2.42 | -3.80 | 1.51 | -24.61 | 0.57 | 0.17 | 1065 | 1550.04 |
| vanilla | LDWP | 7.75 | 6.77 | -5.82 | -7.34 | 2.85 | -33.69 | 0.56 | 0.57 | 1039 | 2716.30 |
| vanilla | LGEE | 4.83 | 4.00 | -0.66 | -2.73 | 1.66 | -18.33 | 0.82 | 0.92 | 1095 | 4278.20 |
| vanilla | MISO | 2.88 | 2.44 | -0.47 | -1.63 | 1.65 | -13.05 | 0.50 | 0.07 | 1088 | 74077.99 |
| vanilla | NEVP | 4.05 | 3.70 | -1.80 | -3.01 | 1.49 | -19.01 | 0.78 | 0.79 | 1041 | 4544.12 |
| vanilla | NWMT | 4.15 | 3.47 | -1.14 | -2.59 | 2.30 | -22.67 | 0.13 | 0.34 | 1049 | 1359.63 |
| vanilla | NYIS | 4.64 | 4.04 | -1.17 | -2.76 | 0.94 | -20.67 | 0.23 | 0.54 | 1074 | 17101.47 |
| vanilla | PACE | 3.68 | 3.21 | -2.76 | -3.36 | 2.33 | -18.20 | 0.61 | 0.11 | 1083 | 5975.48 |
| vanilla | PACW | 4.64 | 3.78 | -1.04 | -2.73 | 1.72 | -17.59 | 0.47 | 0.15 | 1018 | 2409.10 |
| vanilla | PGE | 3.78 | 3.36 | -1.35 | -2.47 | 1.92 | -18.60 | 0.06 | 0.24 | 1087 | 2611.80 |
| vanilla | PJM | 3.37 | 2.86 | -0.54 | -2.08 | 1.58 | -15.47 | 0.33 | 0.31 | 1073 | 93074.23 |
| vanilla | PNM | 3.92 | 3.55 | -1.63 | -2.60 | 1.92 | -19.95 | 0.81 | 0.85 | 1095 | 1668.76 |
| vanilla | PSCO | 6.18 | 5.72 | -4.24 | -5.52 | 2.28 | -25.16 | 0.50 | 0.62 | 1046 | 5110.47 |
| vanilla | PSEI | 4.12 | 3.41 | -0.55 | -2.16 | 1.81 | -41.40 | 0.98 | 0.97 | 894 | 2868.75 |
| vanilla | SC | 4.44 | 3.81 | -1.06 | -2.77 | 1.67 | -19.58 | 0.42 | 0.23 | 1078 | 3064.92 |
| vanilla | SCEG | 4.82 | 4.28 | -2.69 | -3.97 | 1.81 | -23.16 | 0.53 | 0.52 | 1045 | 2791.89 |
| vanilla | SCL | 3.66 | 3.07 | -0.53 | -1.95 | 1.99 | -23.74 | 0.47 | 0.62 | 1067 | 1080.31 |
| vanilla | SOCO | 4.28 | 3.48 | -0.13 | -2.32 | 1.43 | -15.17 | 0.09 | 0.44 | 1081 | 27033.88 |
| vanilla | SRP | 4.48 | 3.95 | -3.87 | -4.46 | 1.33 | -38.38 | 0.28 | 0.34 | 1038 | 4047.71 |
| vanilla | SWPP | 2.92 | 2.36 | -0.98 | -2.07 | 1.74 | -21.89 | 0.52 | 0.27 | 1078 | 33075.46 |
| vanilla | TEC | 5.02 | 4.41 | -1.88 | -3.56 | 1.20 | -21.27 | 0.44 | 0.21 | 1072 | 2562.38 |
| vanilla | TEPC | 8.27 | 6.31 | -1.72 | -4.61 | 1.57 | -41.58 | 0.14 | 0.32 | 1065 | 1647.75 |
| vanilla | TPWR | 4.15 | 3.55 | -0.93 | -2.37 | 2.04 | -17.02 | 0.22 | 0.22 | 1087 | 527.80 |
| vanilla | TVA | 3.52 | 2.95 | -0.71 | -2.20 | 1.36 | -12.87 | 0.26 | 0.19 | 1084 | 18791.86 |
| vanilla | WACM | 8.64 | 7.28 | -0.16 | -3.58 | 3.06 | -33.83 | 0.85 | 0.94 | 960 | 3856.17 |
| vanilla | WALC | 10.77 | 9.76 | -12.73 | -13.45 | 2.57 | -44.47 | 0.43 | 0.29 | 889 | 1015.38 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | AECI | gerri_heather | 3.77 | -4.70 | -4.70 | -9.07 | 6 |
| DF | AVA | gerri_heather | 3.83 | -4.81 | -4.81 | -7.37 | 5 |
| DF | AZPS | gerri_heather | 3.46 | -4.25 | -4.25 | -10.69 | 6 |
| DF | BANC | gerri_heather | 2.06 | -1.74 | -1.86 | -3.29 | 6 |
| DF | BPAT | gerri_heather | 3.76 | 0.98 | -1.48 | -3.76 | 6 |
| DF | CISO | gerri_heather | 4.87 | 0.22 | -0.77 | -2.41 | 6 |
| DF | CPLE | gerri_heather | 7.53 | 1.07 | -3.67 | -10.79 | 6 |
| DF | CPLW | gerri_heather | 8.02 | -5.77 | -5.77 | -15.23 | 6 |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | EPE | gerri_heather | 2.42 | -0.95 | -1.63 | -3.86 | 6 |
| DF | ERCO | gerri_heather | 4.26 | 1.90 | -1.57 | -9.43 | 6 |
| DF | FMPP | gerri_heather | 7.66 | -2.86 | -3.50 | -10.37 | 6 |
| DF | FPC | gerri_heather | 27.26 | -29.12 | -29.12 | -37.15 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | GCPD | gerri_heather | 3.03 | -3.06 | -3.10 | -7.12 | 6 |
| DF | IPCO | gerri_heather | 1.93 | 0.24 | -0.82 | -3.66 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | JEA | gerri_heather | 4.64 | -1.35 | -2.52 | -11.25 | 6 |
| DF | LDWP | gerri_heather | 6.40 | -11.16 | -12.91 | -22.52 | 6 |
| DF | LGEE | gerri_heather | 10.19 | -11.87 | -11.87 | -17.80 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | NEVP | gerri_heather | 4.51 | -3.88 | -3.92 | -7.68 | 6 |
| DF | NWMT | gerri_heather | 2.26 | -2.41 | -2.72 | -6.73 | 6 |
| DF | NYIS | gerri_heather | 3.41 | -2.81 | -2.81 | -3.64 | 5 |
| DF | PACE | gerri_heather | 5.07 | 4.72 | 0.00 | 0.00 | 6 |
| DF | PACW | gerri_heather | 3.39 | -1.38 | -3.21 | -13.23 | 6 |
| DF | PGE | gerri_heather | 1.87 | -1.51 | -2.20 | -3.97 | 6 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | PNM | gerri_heather | 5.49 | -4.28 | -4.28 | -6.38 | 6 |
| DF | PSCO | gerri_heather | 3.84 | -4.56 | -4.56 | -9.55 | 6 |
| DF | PSEI | gerri_heather | 38.33 | -46.10 | -46.10 | -49.23 | 5 |
| DF | SC | gerri_heather | 10.47 | 6.70 | 0.00 | 0.00 | 6 |
| DF | SCEG | gerri_heather | 3.07 | -1.91 | -2.21 | -5.10 | 6 |
| DF | SCL | gerri_heather | 7.08 | -7.59 | -7.59 | -9.77 | 6 |
| DF | SOCO | gerri_heather | 1.32 | -0.39 | -0.41 | -0.76 | 6 |
| DF | SRP | gerri_heather | 2.58 | -0.66 | -1.21 | -2.88 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| DF | TEC | gerri_heather | 3.92 | -0.59 | -1.16 | -5.26 | 6 |
| DF | TEPC | gerri_heather | 2.53 | -1.81 | -1.81 | -4.51 | 4 |
| DF | TPWR | gerri_heather | 3.49 | -4.29 | -4.75 | -10.37 | 6 |
| DF | TVA | gerri_heather | 3.50 | 2.67 | -0.73 | -4.40 | 6 |
| DF | WACM | gerri_heather | 17.75 | -17.56 | -17.56 | -18.41 | 5 |
| DF | WALC | gerri_heather | 10.11 | -1.42 | -4.44 | -13.68 | 6 |
| last_known_day | AECI | gerri_heather | 19.67 | -14.29 | -15.70 | -43.03 | 6 |
| last_known_day | AVA | gerri_heather | 7.13 | -2.48 | -4.97 | -18.01 | 5 |
| last_known_day | AZPS | gerri_heather | 6.06 | 1.19 | -3.18 | -9.55 | 6 |
| last_known_day | BANC | gerri_heather | 5.77 | 0.58 | -1.71 | -7.44 | 6 |
| last_known_day | BPAT | gerri_heather | 9.24 | -5.96 | -7.84 | -23.24 | 6 |
| last_known_day | CISO | gerri_heather | 6.24 | 0.42 | -2.66 | -9.97 | 6 |
| last_known_day | CPLE | gerri_heather | 19.62 | -12.29 | -15.58 | -32.68 | 6 |
| last_known_day | CPLW | gerri_heather | 15.62 | -13.02 | -15.45 | -35.00 | 6 |
| last_known_day | DUK | gerri_heather | 13.82 | -12.21 | -13.32 | -28.57 | 6 |
| last_known_day | EPE | gerri_heather | 10.26 | 1.84 | -4.25 | -18.60 | 6 |
| last_known_day | ERCO | gerri_heather | 13.82 | -12.97 | -13.14 | -29.24 | 6 |
| last_known_day | FMPP | gerri_heather | 7.40 | -2.01 | -3.87 | -9.55 | 6 |
| last_known_day | FPC | gerri_heather | 14.81 | -4.61 | -8.05 | -30.79 | 6 |
| last_known_day | FPL | gerri_heather | 7.33 | -8.01 | -8.39 | -15.94 | 6 |
| last_known_day | GCPD | gerri_heather | 8.02 | -1.32 | -3.55 | -17.02 | 6 |
| last_known_day | IPCO | gerri_heather | 6.28 | -4.21 | -6.00 | -11.49 | 6 |
| last_known_day | ISNE | gerri_heather | 8.26 | -3.77 | -6.00 | -17.09 | 6 |
| last_known_day | JEA | gerri_heather | 18.24 | -5.83 | -10.90 | -43.95 | 6 |
| last_known_day | LDWP | gerri_heather | 7.04 | -2.99 | -5.57 | -14.35 | 6 |
| last_known_day | LGEE | gerri_heather | 10.76 | -12.60 | -13.43 | -24.71 | 6 |
| last_known_day | MISO | gerri_heather | 7.51 | -7.94 | -7.94 | -15.52 | 6 |
| last_known_day | NEVP | gerri_heather | 4.73 | 2.14 | -0.76 | -2.68 | 6 |
| last_known_day | NWMT | gerri_heather | 6.96 | -0.59 | -3.48 | -13.51 | 6 |
| last_known_day | NYIS | gerri_heather | 7.00 | -3.59 | -5.52 | -13.71 | 5 |
| last_known_day | PACE | gerri_heather | 4.25 | 0.78 | -1.60 | -5.26 | 6 |
| last_known_day | PACW | gerri_heather | 7.26 | -3.70 | -6.86 | -18.98 | 6 |
| last_known_day | PGE | gerri_heather | 7.70 | -5.13 | -7.03 | -18.85 | 6 |
| last_known_day | PJM | gerri_heather | 8.34 | -8.28 | -8.28 | -15.45 | 6 |
| last_known_day | PNM | gerri_heather | 6.98 | 2.05 | -2.69 | -6.34 | 6 |
| last_known_day | PSCO | gerri_heather | 7.24 | -1.97 | -4.31 | -9.97 | 6 |
| last_known_day | PSEI | gerri_heather | 8.06 | -2.80 | -4.86 | -21.98 | 5 |
| last_known_day | SC | gerri_heather | 15.45 | -8.85 | -10.77 | -31.62 | 6 |
| last_known_day | SCEG | gerri_heather | 14.35 | -9.62 | -10.33 | -30.37 | 6 |
| last_known_day | SCL | gerri_heather | 10.62 | -2.70 | -6.89 | -22.84 | 6 |
| last_known_day | SOCO | gerri_heather | 13.95 | -8.47 | -13.12 | -32.21 | 6 |
| last_known_day | SRP | gerri_heather | 5.39 | 1.01 | -1.83 | -6.62 | 6 |
| last_known_day | SWPP | gerri_heather | 13.09 | -8.79 | -10.61 | -20.84 | 6 |
| last_known_day | TEC | gerri_heather | 9.44 | -1.40 | -4.33 | -9.37 | 6 |
| last_known_day | TEPC | gerri_heather | 4.30 | -4.08 | -4.86 | -12.36 | 4 |
| last_known_day | TPWR | gerri_heather | 10.21 | -5.95 | -7.25 | -20.63 | 6 |
| last_known_day | TVA | gerri_heather | 13.25 | -13.45 | -15.27 | -25.92 | 6 |
| last_known_day | WACM | gerri_heather | 4.79 | -0.87 | -2.24 | -4.94 | 5 |
| last_known_day | WALC | gerri_heather | 6.82 | -0.96 | -4.50 | -10.84 | 6 |
| same_type_mean_2w | AECI | gerri_heather | 31.28 | -35.30 | -35.30 | -41.53 | 6 |
| same_type_mean_2w | AVA | gerri_heather | 23.25 | -22.19 | -22.19 | -32.05 | 5 |
| same_type_mean_2w | AZPS | gerri_heather | 8.00 | -5.24 | -7.07 | -17.45 | 6 |
| same_type_mean_2w | BANC | gerri_heather | 5.34 | -1.96 | -3.34 | -9.90 | 6 |
| same_type_mean_2w | BPAT | gerri_heather | 20.99 | -22.15 | -22.15 | -34.86 | 6 |
| same_type_mean_2w | CISO | gerri_heather | 3.38 | 0.26 | -1.54 | -7.35 | 6 |
| same_type_mean_2w | CPLE | gerri_heather | 16.14 | -8.85 | -11.69 | -21.17 | 6 |
| same_type_mean_2w | CPLW | gerri_heather | 14.51 | -17.31 | -17.45 | -31.91 | 6 |
| same_type_mean_2w | DUK | gerri_heather | 10.84 | -12.95 | -12.95 | -23.26 | 6 |
| same_type_mean_2w | EPE | gerri_heather | 5.52 | 1.39 | -1.72 | -7.77 | 6 |
| same_type_mean_2w | ERCO | gerri_heather | 21.62 | -24.02 | -24.02 | -33.30 | 6 |
| same_type_mean_2w | FMPP | gerri_heather | 5.57 | -4.09 | -5.00 | -10.58 | 6 |
| same_type_mean_2w | FPC | gerri_heather | 9.57 | -5.75 | -6.73 | -21.93 | 6 |
| same_type_mean_2w | FPL | gerri_heather | 7.17 | -10.07 | -10.07 | -15.40 | 6 |
| same_type_mean_2w | GCPD | gerri_heather | 19.54 | -20.89 | -20.89 | -29.08 | 6 |
| same_type_mean_2w | IPCO | gerri_heather | 14.50 | -14.71 | -14.71 | -21.69 | 6 |
| same_type_mean_2w | ISNE | gerri_heather | 7.18 | -1.03 | -3.82 | -9.28 | 6 |
| same_type_mean_2w | JEA | gerri_heather | 14.16 | -7.93 | -9.02 | -28.49 | 6 |
| same_type_mean_2w | LDWP | gerri_heather | 6.44 | -3.74 | -5.82 | -15.96 | 6 |
| same_type_mean_2w | LGEE | gerri_heather | 19.15 | -21.37 | -21.37 | -29.75 | 6 |
| same_type_mean_2w | MISO | gerri_heather | 14.23 | -14.71 | -14.71 | -19.82 | 6 |
| same_type_mean_2w | NEVP | gerri_heather | 4.32 | 1.75 | -1.05 | -4.50 | 6 |
| same_type_mean_2w | NWMT | gerri_heather | 15.39 | -14.79 | -14.79 | -23.91 | 6 |
| same_type_mean_2w | NYIS | gerri_heather | 4.72 | -2.31 | -3.48 | -7.74 | 5 |
| same_type_mean_2w | PACE | gerri_heather | 4.04 | -4.41 | -4.41 | -9.19 | 6 |
| same_type_mean_2w | PACW | gerri_heather | 17.93 | -17.82 | -17.82 | -30.97 | 6 |
| same_type_mean_2w | PGE | gerri_heather | 17.26 | -16.84 | -16.84 | -29.36 | 6 |
| same_type_mean_2w | PJM | gerri_heather | 10.73 | -12.39 | -12.39 | -19.66 | 6 |
| same_type_mean_2w | PNM | gerri_heather | 5.72 | 0.37 | -2.48 | -10.19 | 6 |
| same_type_mean_2w | PSCO | gerri_heather | 11.66 | -13.56 | -13.56 | -17.65 | 6 |
| same_type_mean_2w | PSEI | gerri_heather | 21.74 | -22.62 | -22.62 | -37.03 | 5 |
| same_type_mean_2w | SC | gerri_heather | 12.39 | -6.18 | -7.66 | -14.65 | 6 |
| same_type_mean_2w | SCEG | gerri_heather | 11.97 | -4.57 | -6.49 | -13.60 | 6 |
| same_type_mean_2w | SCL | gerri_heather | 22.56 | -20.36 | -20.36 | -32.75 | 6 |
| same_type_mean_2w | SOCO | gerri_heather | 12.51 | -10.82 | -13.99 | -29.05 | 6 |
| same_type_mean_2w | SRP | gerri_heather | 9.47 | -5.14 | -8.40 | -19.80 | 6 |
| same_type_mean_2w | SWPP | gerri_heather | 20.75 | -22.00 | -22.00 | -33.78 | 6 |
| same_type_mean_2w | TEC | gerri_heather | 6.46 | -4.64 | -5.35 | -13.18 | 6 |
| same_type_mean_2w | TEPC | gerri_heather | 8.62 | -0.67 | -3.29 | -13.15 | 4 |
| same_type_mean_2w | TPWR | gerri_heather | 22.39 | -24.09 | -24.09 | -33.96 | 6 |
| same_type_mean_2w | TVA | gerri_heather | 18.94 | -18.69 | -19.83 | -30.38 | 6 |
| same_type_mean_2w | WACM | gerri_heather | 6.95 | -7.70 | -7.84 | -17.04 | 5 |
| same_type_mean_2w | WALC | gerri_heather | 9.55 | -7.51 | -8.22 | -20.52 | 6 |
| same_weekday_last_week | AECI | gerri_heather | 31.85 | -36.60 | -36.60 | -44.29 | 6 |
| same_weekday_last_week | AVA | gerri_heather | 22.78 | -21.34 | -21.34 | -28.91 | 5 |
| same_weekday_last_week | AZPS | gerri_heather | 10.55 | 1.11 | -5.37 | -15.48 | 6 |
| same_weekday_last_week | BANC | gerri_heather | 5.84 | 0.93 | -2.28 | -9.57 | 6 |
| same_weekday_last_week | BPAT | gerri_heather | 20.33 | -22.10 | -22.10 | -30.97 | 6 |
| same_weekday_last_week | CISO | gerri_heather | 4.90 | 2.20 | -1.50 | -7.92 | 6 |
| same_weekday_last_week | CPLE | gerri_heather | 19.57 | -12.76 | -16.81 | -34.80 | 6 |
| same_weekday_last_week | CPLW | gerri_heather | 15.76 | -15.29 | -19.40 | -36.17 | 6 |
| same_weekday_last_week | DUK | gerri_heather | 12.26 | -11.67 | -13.58 | -29.42 | 6 |
| same_weekday_last_week | EPE | gerri_heather | 7.52 | 5.35 | -0.71 | -2.89 | 6 |
| same_weekday_last_week | ERCO | gerri_heather | 20.88 | -22.29 | -22.29 | -33.06 | 6 |
| same_weekday_last_week | FMPP | gerri_heather | 7.20 | -4.22 | -5.20 | -9.99 | 6 |
| same_weekday_last_week | FPC | gerri_heather | 10.76 | -8.92 | -9.40 | -24.93 | 6 |
| same_weekday_last_week | FPL | gerri_heather | 8.31 | -8.11 | -8.11 | -10.93 | 6 |
| same_weekday_last_week | GCPD | gerri_heather | 19.73 | -20.55 | -20.55 | -28.57 | 6 |
| same_weekday_last_week | IPCO | gerri_heather | 12.77 | -12.05 | -12.05 | -19.38 | 6 |
| same_weekday_last_week | ISNE | gerri_heather | 9.75 | 1.71 | -3.28 | -13.49 | 6 |
| same_weekday_last_week | JEA | gerri_heather | 11.36 | -10.63 | -13.24 | -27.40 | 6 |
| same_weekday_last_week | LDWP | gerri_heather | 7.22 | 1.43 | -2.87 | -9.33 | 6 |
| same_weekday_last_week | LGEE | gerri_heather | 19.76 | -21.41 | -21.41 | -32.00 | 6 |
| same_weekday_last_week | MISO | gerri_heather | 14.09 | -14.01 | -14.01 | -21.58 | 6 |
| same_weekday_last_week | NEVP | gerri_heather | 5.89 | 4.00 | -1.00 | -6.01 | 6 |
| same_weekday_last_week | NWMT | gerri_heather | 15.79 | -15.11 | -15.11 | -24.82 | 6 |
| same_weekday_last_week | NYIS | gerri_heather | 6.81 | 0.44 | -2.50 | -6.03 | 5 |
| same_weekday_last_week | PACE | gerri_heather | 3.27 | -1.70 | -2.11 | -4.41 | 6 |
| same_weekday_last_week | PACW | gerri_heather | 16.81 | -17.03 | -17.03 | -26.16 | 6 |
| same_weekday_last_week | PGE | gerri_heather | 16.52 | -16.34 | -16.34 | -25.52 | 6 |
| same_weekday_last_week | PJM | gerri_heather | 12.23 | -10.24 | -11.41 | -24.88 | 6 |
| same_weekday_last_week | PNM | gerri_heather | 8.46 | 3.29 | -2.44 | -12.15 | 6 |
| same_weekday_last_week | PSCO | gerri_heather | 9.53 | -11.98 | -11.98 | -17.87 | 6 |
| same_weekday_last_week | PSEI | gerri_heather | 21.64 | -22.29 | -22.29 | -32.38 | 5 |
| same_weekday_last_week | SC | gerri_heather | 13.80 | -9.52 | -12.86 | -22.66 | 6 |
| same_weekday_last_week | SCEG | gerri_heather | 13.78 | -5.91 | -10.30 | -19.28 | 6 |
| same_weekday_last_week | SCL | gerri_heather | 21.19 | -19.21 | -19.21 | -27.87 | 6 |
| same_weekday_last_week | SOCO | gerri_heather | 14.56 | -9.86 | -15.42 | -28.36 | 6 |
| same_weekday_last_week | SRP | gerri_heather | 12.67 | 2.42 | -6.43 | -16.93 | 6 |
| same_weekday_last_week | SWPP | gerri_heather | 20.70 | -21.23 | -21.23 | -33.42 | 6 |
| same_weekday_last_week | TEC | gerri_heather | 8.49 | -4.99 | -5.86 | -11.59 | 6 |
| same_weekday_last_week | TEPC | gerri_heather | 12.75 | 6.51 | -3.48 | -13.92 | 4 |
| same_weekday_last_week | TPWR | gerri_heather | 21.89 | -23.71 | -23.71 | -30.58 | 6 |
| same_weekday_last_week | TVA | gerri_heather | 20.92 | -19.64 | -19.93 | -32.09 | 6 |
| same_weekday_last_week | WACM | gerri_heather | 4.18 | -4.11 | -4.35 | -11.88 | 5 |
| same_weekday_last_week | WALC | gerri_heather | 10.11 | -1.42 | -4.44 | -13.68 | 6 |
| vanilla | AECI | gerri_heather | 6.79 | -6.27 | -6.29 | -14.15 | 6 |
| vanilla | AVA | gerri_heather | 5.67 | -5.91 | -5.91 | -10.27 | 5 |
| vanilla | AZPS | gerri_heather | 5.38 | -6.21 | -6.28 | -9.55 | 6 |
| vanilla | BANC | gerri_heather | 4.73 | -2.58 | -2.86 | -6.66 | 6 |
| vanilla | BPAT | gerri_heather | 5.43 | -5.20 | -5.35 | -12.16 | 6 |
| vanilla | CISO | gerri_heather | 3.06 | 1.56 | -0.53 | -2.98 | 6 |
| vanilla | CPLE | gerri_heather | 7.13 | -1.53 | -4.36 | -13.85 | 6 |
| vanilla | CPLW | gerri_heather | 5.83 | -8.28 | -8.28 | -10.69 | 6 |
| vanilla | DUK | gerri_heather | 5.79 | -6.88 | -7.02 | -13.11 | 6 |
| vanilla | EPE | gerri_heather | 3.77 | -2.70 | -3.34 | -8.15 | 6 |
| vanilla | ERCO | gerri_heather | 5.54 | -6.58 | -6.58 | -14.51 | 6 |
| vanilla | FMPP | gerri_heather | 6.70 | 2.39 | -1.46 | -4.57 | 6 |
| vanilla | FPC | gerri_heather | 7.87 | 0.40 | -3.74 | -15.02 | 6 |
| vanilla | FPL | gerri_heather | 4.72 | -4.46 | -5.33 | -12.10 | 6 |
| vanilla | GCPD | gerri_heather | 8.61 | -9.75 | -9.75 | -11.75 | 6 |
| vanilla | IPCO | gerri_heather | 6.71 | -5.35 | -5.35 | -8.80 | 6 |
| vanilla | ISNE | gerri_heather | 4.62 | -1.59 | -1.96 | -6.39 | 6 |
| vanilla | JEA | gerri_heather | 6.15 | -6.31 | -7.09 | -15.78 | 6 |
| vanilla | LDWP | gerri_heather | 6.34 | -10.10 | -10.10 | -17.37 | 6 |
| vanilla | LGEE | gerri_heather | 5.99 | -5.45 | -6.14 | -13.07 | 6 |
| vanilla | MISO | gerri_heather | 3.13 | -2.93 | -3.12 | -7.52 | 6 |
| vanilla | NEVP | gerri_heather | 4.20 | -3.60 | -3.60 | -7.27 | 6 |
| vanilla | NWMT | gerri_heather | 9.70 | -9.67 | -9.67 | -13.19 | 6 |
| vanilla | NYIS | gerri_heather | 2.55 | -0.86 | -0.91 | -1.79 | 5 |
| vanilla | PACE | gerri_heather | 5.04 | -6.66 | -6.66 | -8.70 | 6 |
| vanilla | PACW | gerri_heather | 5.11 | -5.78 | -5.78 | -11.64 | 6 |
| vanilla | PGE | gerri_heather | 5.13 | -5.77 | -6.01 | -10.95 | 6 |
| vanilla | PJM | gerri_heather | 2.95 | 0.16 | -1.02 | -4.83 | 6 |
| vanilla | PNM | gerri_heather | 3.28 | -3.52 | -4.15 | -10.24 | 6 |
| vanilla | PSCO | gerri_heather | 11.71 | -12.95 | -12.95 | -18.03 | 6 |
| vanilla | PSEI | gerri_heather | 7.82 | -7.73 | -7.73 | -9.45 | 5 |
| vanilla | SC | gerri_heather | 6.14 | -0.59 | -3.29 | -14.24 | 6 |
| vanilla | SCEG | gerri_heather | 5.24 | -2.52 | -4.17 | -11.77 | 6 |
| vanilla | SCL | gerri_heather | 8.99 | -8.63 | -8.63 | -11.58 | 6 |
| vanilla | SOCO | gerri_heather | 4.50 | 0.11 | -2.75 | -9.41 | 6 |
| vanilla | SRP | gerri_heather | 3.64 | -1.62 | -2.67 | -8.08 | 6 |
| vanilla | SWPP | gerri_heather | 7.73 | -8.40 | -8.40 | -15.79 | 6 |
| vanilla | TEC | gerri_heather | 9.66 | 3.44 | -1.40 | -6.33 | 6 |
| vanilla | TEPC | gerri_heather | 9.96 | -11.74 | -11.74 | -16.63 | 4 |
| vanilla | TPWR | gerri_heather | 4.61 | -5.55 | -5.55 | -9.39 | 6 |
| vanilla | TVA | gerri_heather | 4.86 | 3.72 | -0.94 | -2.93 | 6 |
| vanilla | WACM | gerri_heather | 3.69 | 0.42 | -0.94 | -2.56 | 5 |
| vanilla | WALC | gerri_heather | 4.26 | -1.71 | -2.95 | -10.19 | 6 |
| DF | AECI | january_2025 | 1.27 | -0.78 | -0.79 | -1.41 | 6 |
| DF | AVA | january_2025 | 2.10 | -1.88 | -2.38 | -9.22 | 6 |
| DF | AZPS | january_2025 | 5.83 | -0.10 | -1.29 | -6.32 | 6 |
| DF | BANC | january_2025 | 2.14 | -2.31 | -3.27 | -6.26 | 6 |
| DF | BPAT | january_2025 | 2.46 | -0.63 | -1.13 | -5.68 | 6 |
| DF | CISO | january_2025 | 6.30 | -4.14 | -4.14 | -7.74 | 6 |
| DF | CPLE | january_2025 | 6.89 | 5.43 | -0.53 | -3.21 | 6 |
| DF | CPLW | january_2025 | 5.11 | -5.64 | -5.68 | -11.40 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | EPE | january_2025 | 2.83 | -2.85 | -3.06 | -7.15 | 6 |
| DF | ERCO | january_2025 | 3.99 | 0.33 | -0.83 | -2.52 | 6 |
| DF | FMPP | january_2025 | 5.76 | -9.06 | -9.06 | -18.25 | 6 |
| DF | FPC | january_2025 | 26.82 | -28.62 | -28.62 | -34.20 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | GCPD | january_2025 | 1.91 | -1.36 | -1.84 | -4.45 | 6 |
| DF | IPCO | january_2025 | 3.91 | -3.48 | -3.66 | -6.22 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | JEA | january_2025 | 6.26 | -3.45 | -3.90 | -14.25 | 6 |
| DF | LDWP | january_2025 | 7.66 | -10.77 | -10.77 | -23.84 | 3 |
| DF | LGEE | january_2025 | 7.82 | -8.18 | -8.18 | -13.68 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | NEVP | january_2025 | 5.78 | -4.66 | -4.70 | -13.17 | 6 |
| DF | NWMT | january_2025 | 1.62 | -1.23 | -1.41 | -3.54 | 6 |
| DF | NYIS | january_2025 | 3.90 | -3.63 | -3.63 | -4.31 | 5 |
| DF | PACE | january_2025 | 3.25 | 0.34 | -0.99 | -2.62 | 6 |
| DF | PACW | january_2025 | 3.94 | -0.67 | -1.72 | -3.40 | 6 |
| DF | PGE | january_2025 | 1.02 | 1.06 | -0.10 | -0.57 | 6 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | PNM | january_2025 | 10.14 | -9.64 | -9.64 | -12.31 | 6 |
| DF | PSCO | january_2025 | 8.21 | -11.71 | -11.71 | -18.67 | 6 |
| DF | PSEI | january_2025 | 37.60 | -41.53 | -41.53 | -47.40 | 4 |
| DF | SC | january_2025 | 5.44 | 1.62 | -0.74 | -3.65 | 6 |
| DF | SCEG | january_2025 | 4.79 | -3.77 | -3.77 | -9.04 | 6 |
| DF | SCL | january_2025 | 2.95 | -2.68 | -2.94 | -6.04 | 6 |
| DF | SOCO | january_2025 | 1.15 | -1.30 | -1.30 | -1.77 | 6 |
| DF | SRP | january_2025 | 2.99 | -2.53 | -2.53 | -4.79 | 5 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| DF | TEC | january_2025 | 6.61 | -5.71 | -5.71 | -14.25 | 6 |
| DF | TEPC | january_2025 | 2.62 | -2.15 | -2.15 | -3.22 | 6 |
| DF | TPWR | january_2025 | 1.50 | -1.27 | -1.80 | -3.11 | 6 |
| DF | TVA | january_2025 | 2.96 | 1.69 | -0.29 | -1.52 | 6 |
| DF | WACM | january_2025 | 17.25 | -17.51 | -17.51 | -19.29 | 6 |
| DF | WALC | january_2025 | 10.22 | 3.30 | -3.02 | -11.67 | 5 |
| last_known_day | AECI | january_2025 | 17.04 | -7.15 | -11.77 | -38.67 | 6 |
| last_known_day | AVA | january_2025 | 4.00 | -1.88 | -3.09 | -13.64 | 6 |
| last_known_day | AZPS | january_2025 | 5.26 | -2.59 | -3.96 | -8.29 | 6 |
| last_known_day | BANC | january_2025 | 3.49 | -1.19 | -2.50 | -7.43 | 6 |
| last_known_day | BPAT | january_2025 | 3.46 | -0.26 | -1.92 | -6.86 | 6 |
| last_known_day | CISO | january_2025 | 4.29 | -1.67 | -2.85 | -8.61 | 6 |
| last_known_day | CPLE | january_2025 | 18.92 | -9.32 | -13.45 | -29.73 | 6 |
| last_known_day | CPLW | january_2025 | 18.90 | -9.83 | -13.33 | -43.30 | 6 |
| last_known_day | DUK | january_2025 | 14.58 | -9.35 | -9.67 | -35.33 | 6 |
| last_known_day | EPE | january_2025 | 7.11 | -6.02 | -6.63 | -18.89 | 6 |
| last_known_day | ERCO | january_2025 | 14.62 | -8.46 | -10.44 | -30.93 | 6 |
| last_known_day | FMPP | january_2025 | 15.24 | -16.50 | -16.50 | -27.26 | 6 |
| last_known_day | FPC | january_2025 | 19.89 | -16.47 | -16.47 | -35.71 | 6 |
| last_known_day | FPL | january_2025 | 10.05 | -12.79 | -12.79 | -18.59 | 6 |
| last_known_day | GCPD | january_2025 | 3.21 | -0.15 | -2.10 | -9.72 | 6 |
| last_known_day | IPCO | january_2025 | 4.93 | -1.53 | -3.10 | -9.66 | 6 |
| last_known_day | ISNE | january_2025 | 10.24 | -3.13 | -6.17 | -17.11 | 6 |
| last_known_day | JEA | january_2025 | 23.13 | -15.98 | -17.87 | -44.36 | 6 |
| last_known_day | LDWP | january_2025 | 22.16 | -25.91 | -26.05 | -48.23 | 3 |
| last_known_day | LGEE | january_2025 | 16.17 | -7.39 | -11.08 | -28.29 | 6 |
| last_known_day | MISO | january_2025 | 9.95 | -7.87 | -8.93 | -18.31 | 6 |
| last_known_day | NEVP | january_2025 | 3.64 | -3.36 | -4.09 | -10.51 | 6 |
| last_known_day | NWMT | january_2025 | 4.64 | -0.61 | -2.90 | -7.98 | 6 |
| last_known_day | NYIS | january_2025 | 7.58 | -3.30 | -5.68 | -15.36 | 5 |
| last_known_day | PACE | january_2025 | 5.07 | -3.84 | -5.07 | -11.96 | 6 |
| last_known_day | PACW | january_2025 | 3.85 | -1.05 | -2.72 | -7.90 | 6 |
| last_known_day | PGE | january_2025 | 4.53 | -0.99 | -2.86 | -8.37 | 6 |
| last_known_day | PJM | january_2025 | 9.94 | -5.23 | -6.92 | -22.39 | 6 |
| last_known_day | PNM | january_2025 | 5.01 | -4.13 | -4.71 | -8.95 | 6 |
| last_known_day | PSCO | january_2025 | 5.64 | -2.32 | -4.27 | -13.74 | 6 |
| last_known_day | PSEI | january_2025 | 4.77 | -0.78 | -3.23 | -6.79 | 4 |
| last_known_day | SC | january_2025 | 14.65 | -12.52 | -14.67 | -34.52 | 6 |
| last_known_day | SCEG | january_2025 | 14.35 | -15.22 | -15.70 | -37.88 | 6 |
| last_known_day | SCL | january_2025 | 3.84 | -0.79 | -2.30 | -6.36 | 6 |
| last_known_day | SOCO | january_2025 | 14.47 | -15.32 | -15.92 | -40.87 | 6 |
| last_known_day | SRP | january_2025 | 4.64 | -2.73 | -3.90 | -11.37 | 5 |
| last_known_day | SWPP | january_2025 | 8.25 | -3.35 | -5.09 | -17.13 | 6 |
| last_known_day | TEC | january_2025 | 15.72 | -17.36 | -17.45 | -30.48 | 6 |
| last_known_day | TEPC | january_2025 | 3.90 | -6.46 | -6.82 | -25.78 | 6 |
| last_known_day | TPWR | january_2025 | 4.28 | 0.27 | -2.46 | -5.15 | 6 |
| last_known_day | TVA | january_2025 | 17.50 | -9.84 | -13.87 | -30.69 | 6 |
| last_known_day | WACM | january_2025 | 4.33 | -0.78 | -1.78 | -3.91 | 6 |
| last_known_day | WALC | january_2025 | 7.58 | -5.22 | -6.09 | -18.69 | 5 |
| same_type_mean_2w | AECI | january_2025 | 14.47 | -14.72 | -15.34 | -25.03 | 6 |
| same_type_mean_2w | AVA | january_2025 | 7.68 | -9.34 | -9.34 | -13.58 | 6 |
| same_type_mean_2w | AZPS | january_2025 | 4.88 | -6.42 | -6.42 | -12.01 | 6 |
| same_type_mean_2w | BANC | january_2025 | 2.44 | -1.07 | -1.94 | -4.95 | 6 |
| same_type_mean_2w | BPAT | january_2025 | 8.34 | -12.17 | -12.17 | -19.32 | 6 |
| same_type_mean_2w | CISO | january_2025 | 1.91 | -1.87 | -1.91 | -3.98 | 6 |
| same_type_mean_2w | CPLE | january_2025 | 17.32 | -6.52 | -10.23 | -18.86 | 6 |
| same_type_mean_2w | CPLW | january_2025 | 16.81 | -14.56 | -14.56 | -24.10 | 6 |
| same_type_mean_2w | DUK | january_2025 | 13.72 | -7.34 | -8.35 | -13.82 | 6 |
| same_type_mean_2w | EPE | january_2025 | 5.12 | -6.64 | -6.64 | -10.88 | 6 |
| same_type_mean_2w | ERCO | january_2025 | 12.95 | -15.14 | -15.14 | -26.03 | 6 |
| same_type_mean_2w | FMPP | january_2025 | 17.96 | -17.81 | -17.81 | -29.98 | 6 |
| same_type_mean_2w | FPC | january_2025 | 22.74 | -18.42 | -19.70 | -33.96 | 6 |
| same_type_mean_2w | FPL | january_2025 | 15.61 | -17.77 | -17.77 | -24.18 | 6 |
| same_type_mean_2w | GCPD | january_2025 | 3.86 | -5.58 | -5.80 | -8.84 | 6 |
| same_type_mean_2w | IPCO | january_2025 | 8.11 | -8.23 | -8.46 | -12.68 | 6 |
| same_type_mean_2w | ISNE | january_2025 | 7.97 | -2.39 | -3.74 | -7.92 | 6 |
| same_type_mean_2w | JEA | january_2025 | 22.51 | -17.39 | -19.27 | -31.00 | 6 |
| same_type_mean_2w | LDWP | january_2025 | 8.85 | -12.02 | -12.02 | -13.56 | 3 |
| same_type_mean_2w | LGEE | january_2025 | 11.76 | -13.37 | -13.86 | -22.98 | 6 |
| same_type_mean_2w | MISO | january_2025 | 8.44 | -9.16 | -9.16 | -13.39 | 6 |
| same_type_mean_2w | NEVP | january_2025 | 2.16 | -1.79 | -2.38 | -5.33 | 6 |
| same_type_mean_2w | NWMT | january_2025 | 7.37 | -7.21 | -7.21 | -13.12 | 6 |
| same_type_mean_2w | NYIS | january_2025 | 3.91 | -1.79 | -2.19 | -5.47 | 5 |
| same_type_mean_2w | PACE | january_2025 | 3.67 | -5.66 | -5.66 | -10.09 | 6 |
| same_type_mean_2w | PACW | january_2025 | 6.96 | -9.62 | -9.87 | -18.02 | 6 |
| same_type_mean_2w | PGE | january_2025 | 5.07 | -6.18 | -6.22 | -10.78 | 6 |
| same_type_mean_2w | PJM | january_2025 | 7.64 | -8.69 | -8.69 | -14.54 | 6 |
| same_type_mean_2w | PNM | january_2025 | 4.81 | -5.94 | -5.94 | -8.57 | 6 |
| same_type_mean_2w | PSCO | january_2025 | 8.82 | -10.84 | -11.17 | -21.14 | 6 |
| same_type_mean_2w | PSEI | january_2025 | 8.55 | -10.80 | -10.80 | -15.79 | 4 |
| same_type_mean_2w | SC | january_2025 | 15.69 | -7.95 | -9.99 | -19.15 | 6 |
| same_type_mean_2w | SCEG | january_2025 | 16.31 | -11.94 | -13.10 | -27.14 | 6 |
| same_type_mean_2w | SCL | january_2025 | 7.45 | -8.74 | -8.74 | -14.54 | 6 |
| same_type_mean_2w | SOCO | january_2025 | 16.28 | -16.04 | -16.04 | -24.98 | 6 |
| same_type_mean_2w | SRP | january_2025 | 4.26 | -5.57 | -5.57 | -8.87 | 5 |
| same_type_mean_2w | SWPP | january_2025 | 7.54 | -7.19 | -7.19 | -13.27 | 6 |
| same_type_mean_2w | TEC | january_2025 | 19.05 | -17.13 | -17.90 | -31.46 | 6 |
| same_type_mean_2w | TEPC | january_2025 | 4.42 | -7.09 | -7.09 | -10.76 | 6 |
| same_type_mean_2w | TPWR | january_2025 | 11.41 | -14.71 | -15.05 | -23.95 | 6 |
| same_type_mean_2w | TVA | january_2025 | 13.33 | -15.29 | -15.94 | -24.06 | 6 |
| same_type_mean_2w | WACM | january_2025 | 6.25 | -6.32 | -6.49 | -11.96 | 6 |
| same_type_mean_2w | WALC | january_2025 | 10.05 | 2.73 | -0.32 | -1.58 | 5 |
| same_weekday_last_week | AECI | january_2025 | 21.79 | -21.37 | -21.37 | -29.46 | 6 |
| same_weekday_last_week | AVA | january_2025 | 7.61 | -8.72 | -8.72 | -12.86 | 6 |
| same_weekday_last_week | AZPS | january_2025 | 6.13 | -4.00 | -5.44 | -17.14 | 6 |
| same_weekday_last_week | BANC | january_2025 | 2.15 | 1.04 | -0.31 | -1.84 | 6 |
| same_weekday_last_week | BPAT | january_2025 | 6.73 | -10.27 | -10.27 | -15.33 | 6 |
| same_weekday_last_week | CISO | january_2025 | 2.15 | 1.54 | -0.22 | -1.32 | 6 |
| same_weekday_last_week | CPLE | january_2025 | 22.33 | -5.55 | -11.32 | -20.45 | 6 |
| same_weekday_last_week | CPLW | january_2025 | 24.71 | -17.77 | -17.77 | -26.32 | 6 |
| same_weekday_last_week | DUK | january_2025 | 18.83 | -8.42 | -10.10 | -18.87 | 6 |
| same_weekday_last_week | EPE | january_2025 | 7.48 | -9.20 | -9.74 | -16.20 | 6 |
| same_weekday_last_week | ERCO | january_2025 | 16.93 | -18.59 | -18.59 | -26.62 | 6 |
| same_weekday_last_week | FMPP | january_2025 | 21.56 | -19.31 | -19.31 | -28.37 | 6 |
| same_weekday_last_week | FPC | january_2025 | 27.29 | -19.72 | -22.08 | -31.16 | 6 |
| same_weekday_last_week | FPL | january_2025 | 18.47 | -18.79 | -18.79 | -28.22 | 6 |
| same_weekday_last_week | GCPD | january_2025 | 2.69 | -4.40 | -4.56 | -7.13 | 6 |
| same_weekday_last_week | IPCO | january_2025 | 7.95 | -7.05 | -7.05 | -9.54 | 6 |
| same_weekday_last_week | ISNE | january_2025 | 9.26 | -4.84 | -5.45 | -9.05 | 6 |
| same_weekday_last_week | JEA | january_2025 | 29.62 | -19.48 | -23.34 | -33.27 | 6 |
| same_weekday_last_week | LDWP | january_2025 | 6.73 | -1.47 | -5.49 | -16.48 | 3 |
| same_weekday_last_week | LGEE | january_2025 | 14.46 | -14.92 | -14.92 | -24.61 | 6 |
| same_weekday_last_week | MISO | january_2025 | 10.94 | -10.88 | -10.88 | -12.31 | 6 |
| same_weekday_last_week | NEVP | january_2025 | 1.77 | -1.13 | -1.87 | -4.21 | 6 |
| same_weekday_last_week | NWMT | january_2025 | 8.65 | -7.93 | -7.97 | -13.37 | 6 |
| same_weekday_last_week | NYIS | january_2025 | 5.91 | -4.72 | -4.72 | -6.33 | 5 |
| same_weekday_last_week | PACE | january_2025 | 3.86 | -5.33 | -5.33 | -7.60 | 6 |
| same_weekday_last_week | PACW | january_2025 | 4.64 | -6.45 | -6.45 | -11.82 | 6 |
| same_weekday_last_week | PGE | january_2025 | 5.09 | -4.23 | -4.23 | -8.78 | 6 |
| same_weekday_last_week | PJM | january_2025 | 9.52 | -10.09 | -10.09 | -13.50 | 6 |
| same_weekday_last_week | PNM | january_2025 | 5.50 | -5.43 | -5.43 | -9.85 | 6 |
| same_weekday_last_week | PSCO | january_2025 | 10.58 | -13.14 | -13.39 | -20.28 | 6 |
| same_weekday_last_week | PSEI | january_2025 | 5.58 | -7.72 | -7.72 | -12.96 | 4 |
| same_weekday_last_week | SC | january_2025 | 21.31 | -7.85 | -12.12 | -24.57 | 6 |
| same_weekday_last_week | SCEG | january_2025 | 22.14 | -13.74 | -16.36 | -29.53 | 6 |
| same_weekday_last_week | SCL | january_2025 | 5.26 | -5.85 | -5.85 | -10.83 | 6 |
| same_weekday_last_week | SOCO | january_2025 | 23.22 | -18.26 | -18.26 | -27.54 | 6 |
| same_weekday_last_week | SRP | january_2025 | 5.71 | -0.42 | -3.59 | -13.26 | 5 |
| same_weekday_last_week | SWPP | january_2025 | 11.03 | -10.35 | -10.35 | -14.29 | 6 |
| same_weekday_last_week | TEC | january_2025 | 23.34 | -21.33 | -22.51 | -33.71 | 6 |
| same_weekday_last_week | TEPC | january_2025 | 6.21 | -3.85 | -5.47 | -14.49 | 6 |
| same_weekday_last_week | TPWR | january_2025 | 8.52 | -12.71 | -12.89 | -19.77 | 6 |
| same_weekday_last_week | TVA | january_2025 | 18.58 | -17.80 | -17.80 | -25.35 | 6 |
| same_weekday_last_week | WACM | january_2025 | 6.09 | -6.36 | -6.36 | -11.48 | 6 |
| same_weekday_last_week | WALC | january_2025 | 10.22 | 3.30 | -3.02 | -11.67 | 5 |
| vanilla | AECI | january_2025 | 6.74 | -7.37 | -7.37 | -13.86 | 6 |
| vanilla | AVA | january_2025 | 2.08 | -2.09 | -2.55 | -6.07 | 6 |
| vanilla | AZPS | january_2025 | 3.00 | 0.57 | -0.72 | -3.11 | 6 |
| vanilla | BANC | january_2025 | 3.88 | -0.27 | -0.94 | -2.99 | 6 |
| vanilla | BPAT | january_2025 | 3.30 | -5.15 | -5.15 | -7.13 | 6 |
| vanilla | CISO | january_2025 | 3.11 | -0.88 | -2.15 | -4.75 | 6 |
| vanilla | CPLE | january_2025 | 8.00 | 2.76 | -1.90 | -7.31 | 6 |
| vanilla | CPLW | january_2025 | 3.90 | 0.20 | -0.93 | -2.57 | 6 |
| vanilla | DUK | january_2025 | 4.38 | 0.69 | -1.85 | -10.20 | 6 |
| vanilla | EPE | january_2025 | 3.60 | -2.32 | -2.45 | -5.16 | 6 |
| vanilla | ERCO | january_2025 | 3.20 | -6.02 | -6.02 | -7.12 | 6 |
| vanilla | FMPP | january_2025 | 9.82 | -7.86 | -9.43 | -19.54 | 6 |
| vanilla | FPC | january_2025 | 10.90 | -8.44 | -10.73 | -20.73 | 6 |
| vanilla | FPL | january_2025 | 8.91 | -10.18 | -10.18 | -13.31 | 6 |
| vanilla | GCPD | january_2025 | 1.82 | 0.07 | -0.55 | -1.72 | 6 |
| vanilla | IPCO | january_2025 | 3.47 | -5.41 | -5.41 | -8.41 | 6 |
| vanilla | ISNE | january_2025 | 3.77 | -1.39 | -1.49 | -3.07 | 6 |
| vanilla | JEA | january_2025 | 8.65 | -9.86 | -10.25 | -24.61 | 6 |
| vanilla | LDWP | january_2025 | 6.37 | -12.51 | -12.51 | -19.46 | 3 |
| vanilla | LGEE | january_2025 | 3.24 | -4.58 | -4.58 | -8.77 | 6 |
| vanilla | MISO | january_2025 | 2.81 | -3.36 | -3.36 | -5.32 | 6 |
| vanilla | NEVP | january_2025 | 3.84 | 0.57 | -1.22 | -5.51 | 6 |
| vanilla | NWMT | january_2025 | 4.80 | -3.93 | -3.93 | -7.23 | 6 |
| vanilla | NYIS | january_2025 | 2.37 | -0.57 | -0.86 | -2.94 | 5 |
| vanilla | PACE | january_2025 | 1.84 | -3.02 | -3.02 | -4.76 | 6 |
| vanilla | PACW | january_2025 | 3.41 | -4.70 | -4.70 | -7.31 | 6 |
| vanilla | PGE | january_2025 | 2.92 | -3.69 | -3.69 | -6.38 | 6 |
| vanilla | PJM | january_2025 | 4.64 | -5.76 | -5.91 | -11.63 | 6 |
| vanilla | PNM | january_2025 | 4.14 | -5.81 | -5.81 | -7.89 | 6 |
| vanilla | PSCO | january_2025 | 9.03 | -11.83 | -11.83 | -21.18 | 6 |
| vanilla | PSEI | january_2025 | 4.05 | -4.66 | -4.66 | -7.66 | 4 |
| vanilla | SC | january_2025 | 6.00 | 1.94 | -1.72 | -7.85 | 6 |
| vanilla | SCEG | january_2025 | 8.07 | -6.77 | -7.70 | -18.46 | 6 |
| vanilla | SCL | january_2025 | 2.44 | -3.28 | -3.28 | -6.12 | 6 |
| vanilla | SOCO | january_2025 | 5.21 | -4.27 | -5.34 | -13.71 | 6 |
| vanilla | SRP | january_2025 | 3.59 | 1.51 | -1.22 | -6.12 | 5 |
| vanilla | SWPP | january_2025 | 4.77 | -5.23 | -5.23 | -9.05 | 6 |
| vanilla | TEC | january_2025 | 9.34 | -5.29 | -6.78 | -21.27 | 6 |
| vanilla | TEPC | january_2025 | 4.47 | -0.74 | -2.54 | -7.72 | 6 |
| vanilla | TPWR | january_2025 | 6.03 | -7.59 | -7.59 | -11.23 | 6 |
| vanilla | TVA | january_2025 | 3.13 | -3.24 | -3.40 | -6.30 | 6 |
| vanilla | WACM | january_2025 | 2.78 | 0.70 | -0.37 | -1.31 | 6 |
| vanilla | WALC | january_2025 | 12.34 | -14.36 | -14.36 | -17.62 | 5 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | DF | eve | 5.19 | -2.31 | -3.85 |  | 1231 |
| 9 | vanilla | eve | 5.39 | 0.30 | -2.28 | 0.37 | 1231 |
| 6 | last_known_day | eve | 7.21 | 0.45 | -3.39 | 0.29 | 1231 |
| 7 | same_type_mean_2w | eve | 8.65 | -0.73 | -4.79 | 0.28 | 1231 |
| 8 | same_weekday_last_week | eve | 10.44 | 0.19 | -5.07 | 0.21 | 1231 |
| 0 | DF | special | 5.37 | -2.71 | -4.11 |  | 1294 |
| 4 | vanilla | special | 7.30 | 2.59 | -1.71 | 0.27 | 1294 |
| 1 | last_known_day | special | 7.35 | 0.14 | -3.69 | 0.31 | 1294 |
| 2 | same_type_mean_2w | special | 9.33 | -1.03 | -5.22 | 0.28 | 1294 |
| 3 | same_weekday_last_week | special | 11.82 | 0.67 | -5.31 | 0.19 | 1294 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| last_known_day | AECI | mape | 34.837 | 0.000 | 1087 |
| last_known_day | AVA | mape | 36.630 | 0.000 | 1077 |
| last_known_day | AZPS | mape | 3.953 | 0.000 | 1078 |
| last_known_day | BANC | mape | 32.233 | 0.000 | 1049 |
| last_known_day | BPAT | mape | 32.830 | 0.000 | 1087 |
| last_known_day | CISO | mape | 10.021 | 0.000 | 1067 |
| last_known_day | CPLE | mape | 30.362 | 0.000 | 1082 |
| last_known_day | CPLW | mape | 24.336 | 0.000 | 1073 |
| last_known_day | DUK | mape | 39.576 | 0.000 | 1083 |
| last_known_day | EPE | mape | 33.797 | 0.000 | 1088 |
| last_known_day | ERCO | mape | 28.169 | 0.000 | 1081 |
| last_known_day | FMPP | mape | 20.214 | 0.000 | 1029 |
| last_known_day | FPC | mape | -79.651 | 0.000 | 1081 |
| last_known_day | FPL | mape | 23.910 | 0.000 | 1038 |
| last_known_day | GCPD | mape | 20.186 | 0.000 | 1086 |
| last_known_day | IPCO | mape | 17.956 | 0.000 | 1086 |
| last_known_day | ISNE | mape | 34.847 | 0.000 | 1083 |
| last_known_day | JEA | mape | 23.546 | 0.000 | 1065 |
| last_known_day | LDWP | mape | -0.705 | 0.481 | 1039 |
| last_known_day | LGEE | mape | 9.121 | 0.000 | 1095 |
| last_known_day | MISO | mape | 26.002 | 0.000 | 1088 |
| last_known_day | NEVP | mape | -9.701 | 0.000 | 1041 |
| last_known_day | NWMT | mape | 30.721 | 0.000 | 1049 |
| last_known_day | NYIS | mape | 27.665 | 0.000 | 1074 |
| last_known_day | PACE | mape | 5.331 | 0.000 | 1083 |
| last_known_day | PACW | mape | 12.729 | 0.000 | 1018 |
| last_known_day | PGE | mape | 39.644 | 0.000 | 1087 |
| last_known_day | PJM | mape | 32.619 | 0.000 | 1073 |
| last_known_day | PNM | mape | -12.751 | 0.000 | 1095 |
| last_known_day | PSCO | mape | 10.312 | 0.000 | 1046 |
| last_known_day | PSEI | mape | -51.315 | 0.000 | 894 |
| last_known_day | SC | mape | 26.124 | 0.000 | 1078 |
| last_known_day | SCEG | mape | 22.477 | 0.000 | 1045 |
| last_known_day | SCL | mape | 28.984 | 0.000 | 1067 |
| last_known_day | SOCO | mape | 36.850 | 0.000 | 1081 |
| last_known_day | SRP | mape | 22.705 | 0.000 | 1038 |
| last_known_day | SWPP | mape | 8.531 | 0.000 | 1078 |
| last_known_day | TEC | mape | 22.428 | 0.000 | 1072 |
| last_known_day | TEPC | mape | 11.330 | 0.000 | 1065 |
| last_known_day | TPWR | mape | 33.586 | 0.000 | 1087 |
| last_known_day | TVA | mape | 35.390 | 0.000 | 1084 |
| last_known_day | WACM | mape | -81.799 | 0.000 | 960 |
| last_known_day | WALC | mape | -16.396 | 0.000 | 889 |
| same_type_mean_2w | AECI | mape | 32.762 | 0.000 | 1087 |
| same_type_mean_2w | AVA | mape | 32.443 | 0.000 | 1077 |
| same_type_mean_2w | AZPS | mape | 10.459 | 0.000 | 1078 |
| same_type_mean_2w | BANC | mape | 30.633 | 0.000 | 1049 |
| same_type_mean_2w | BPAT | mape | 27.111 | 0.000 | 1087 |
| same_type_mean_2w | CISO | mape | 0.416 | 0.677 | 1067 |
| same_type_mean_2w | CPLE | mape | 29.429 | 0.000 | 1082 |
| same_type_mean_2w | CPLW | mape | 21.777 | 0.000 | 1073 |
| same_type_mean_2w | DUK | mape | 32.802 | 0.000 | 1083 |
| same_type_mean_2w | EPE | mape | 27.686 | 0.000 | 1088 |
| same_type_mean_2w | ERCO | mape | 28.990 | 0.000 | 1081 |
| same_type_mean_2w | FMPP | mape | 21.795 | 0.000 | 1029 |
| same_type_mean_2w | FPC | mape | -59.575 | 0.000 | 1081 |
| same_type_mean_2w | FPL | mape | 27.562 | 0.000 | 1038 |
| same_type_mean_2w | GCPD | mape | 23.319 | 0.000 | 1086 |
| same_type_mean_2w | IPCO | mape | 23.948 | 0.000 | 1086 |
| same_type_mean_2w | ISNE | mape | 33.441 | 0.000 | 1083 |
| same_type_mean_2w | JEA | mape | 24.301 | 0.000 | 1065 |
| same_type_mean_2w | LDWP | mape | -1.596 | 0.110 | 1039 |
| same_type_mean_2w | LGEE | mape | 9.756 | 0.000 | 1095 |
| same_type_mean_2w | MISO | mape | 23.894 | 0.000 | 1088 |
| same_type_mean_2w | NEVP | mape | 1.171 | 0.242 | 1041 |
| same_type_mean_2w | NWMT | mape | 27.122 | 0.000 | 1049 |
| same_type_mean_2w | NYIS | mape | 25.700 | 0.000 | 1074 |
| same_type_mean_2w | PACE | mape | 4.478 | 0.000 | 1083 |
| same_type_mean_2w | PACW | mape | 13.411 | 0.000 | 1018 |
| same_type_mean_2w | PGE | mape | 35.578 | 0.000 | 1087 |
| same_type_mean_2w | PJM | mape | 29.750 | 0.000 | 1073 |
| same_type_mean_2w | PNM | mape | -7.188 | 0.000 | 1095 |
| same_type_mean_2w | PSCO | mape | 6.418 | 0.000 | 1046 |
| same_type_mean_2w | PSEI | mape | -48.415 | 0.000 | 894 |
| same_type_mean_2w | SC | mape | 27.908 | 0.000 | 1078 |
| same_type_mean_2w | SCEG | mape | 24.743 | 0.000 | 1045 |
| same_type_mean_2w | SCL | mape | 20.016 | 0.000 | 1067 |
| same_type_mean_2w | SOCO | mape | 33.705 | 0.000 | 1081 |
| same_type_mean_2w | SRP | mape | 26.198 | 0.000 | 1038 |
| same_type_mean_2w | SWPP | mape | 15.052 | 0.000 | 1078 |
| same_type_mean_2w | TEC | mape | 24.300 | 0.000 | 1072 |
| same_type_mean_2w | TEPC | mape | 18.002 | 0.000 | 1065 |
| same_type_mean_2w | TPWR | mape | 27.930 | 0.000 | 1087 |
| same_type_mean_2w | TVA | mape | 32.518 | 0.000 | 1084 |
| same_type_mean_2w | WACM | mape | -69.324 | 0.000 | 960 |
| same_type_mean_2w | WALC | mape | -6.231 | 0.000 | 889 |
| same_weekday_last_week | AECI | mape | 32.938 | 0.000 | 1087 |
| same_weekday_last_week | AVA | mape | 34.130 | 0.000 | 1077 |
| same_weekday_last_week | AZPS | mape | 14.958 | 0.000 | 1078 |
| same_weekday_last_week | BANC | mape | 30.583 | 0.000 | 1049 |
| same_weekday_last_week | BPAT | mape | 29.912 | 0.000 | 1087 |
| same_weekday_last_week | CISO | mape | 6.924 | 0.000 | 1067 |
| same_weekday_last_week | CPLE | mape | 27.591 | 0.000 | 1082 |
| same_weekday_last_week | CPLW | mape | 22.686 | 0.000 | 1073 |
| same_weekday_last_week | DUK | mape | 32.287 | 0.000 | 1083 |
| same_weekday_last_week | EPE | mape | 30.190 | 0.000 | 1088 |
| same_weekday_last_week | ERCO | mape | 28.944 | 0.000 | 1081 |
| same_weekday_last_week | FMPP | mape | 24.238 | 0.000 | 1029 |
| same_weekday_last_week | FPC | mape | -39.675 | 0.000 | 1081 |
| same_weekday_last_week | FPL | mape | 29.557 | 0.000 | 1038 |
| same_weekday_last_week | GCPD | mape | 25.246 | 0.000 | 1086 |
| same_weekday_last_week | IPCO | mape | 28.155 | 0.000 | 1086 |
| same_weekday_last_week | ISNE | mape | 34.455 | 0.000 | 1083 |
| same_weekday_last_week | JEA | mape | 23.318 | 0.000 | 1065 |
| same_weekday_last_week | LDWP | mape | 5.762 | 0.000 | 1039 |
| same_weekday_last_week | LGEE | mape | 14.956 | 0.000 | 1095 |
| same_weekday_last_week | MISO | mape | 24.764 | 0.000 | 1088 |
| same_weekday_last_week | NEVP | mape | 7.462 | 0.000 | 1041 |
| same_weekday_last_week | NWMT | mape | 31.224 | 0.000 | 1049 |
| same_weekday_last_week | NYIS | mape | 27.176 | 0.000 | 1074 |
| same_weekday_last_week | PACE | mape | 11.911 | 0.000 | 1083 |
| same_weekday_last_week | PACW | mape | 17.619 | 0.000 | 1018 |
| same_weekday_last_week | PGE | mape | 34.848 | 0.000 | 1087 |
| same_weekday_last_week | PJM | mape | 29.567 | 0.000 | 1073 |
| same_weekday_last_week | PNM | mape | -0.823 | 0.411 | 1095 |
| same_weekday_last_week | PSCO | mape | 12.367 | 0.000 | 1046 |
| same_weekday_last_week | PSEI | mape | -43.754 | 0.000 | 894 |
| same_weekday_last_week | SC | mape | 27.701 | 0.000 | 1078 |
| same_weekday_last_week | SCEG | mape | 25.838 | 0.000 | 1045 |
| same_weekday_last_week | SCL | mape | 23.666 | 0.000 | 1067 |
| same_weekday_last_week | SOCO | mape | 31.564 | 0.000 | 1081 |
| same_weekday_last_week | SRP | mape | 30.227 | 0.000 | 1038 |
| same_weekday_last_week | SWPP | mape | 17.741 | 0.000 | 1078 |
| same_weekday_last_week | TEC | mape | 26.924 | 0.000 | 1072 |
| same_weekday_last_week | TEPC | mape | 21.106 | 0.000 | 1065 |
| same_weekday_last_week | TPWR | mape | 31.289 | 0.000 | 1087 |
| same_weekday_last_week | TVA | mape | 31.619 | 0.000 | 1084 |
| same_weekday_last_week | WACM | mape | -60.381 | 0.000 | 960 |
| same_weekday_last_week | WALC | mape | -2.264 | 0.024 | 889 |
| vanilla | AECI | mape | 30.373 | 0.000 | 1087 |
| vanilla | AVA | mape | 26.228 | 0.000 | 1077 |
| vanilla | AZPS | mape | -1.087 | 0.277 | 1078 |
| vanilla | BANC | mape | 30.583 | 0.000 | 1049 |
| vanilla | BPAT | mape | 15.451 | 0.000 | 1087 |
| vanilla | CISO | mape | -9.780 | 0.000 | 1067 |
| vanilla | CPLE | mape | 9.817 | 0.000 | 1082 |
| vanilla | CPLW | mape | 5.298 | 0.000 | 1073 |
| vanilla | DUK | mape | 14.129 | 0.000 | 1083 |
| vanilla | EPE | mape | 21.011 | 0.000 | 1088 |
| vanilla | ERCO | mape | 7.936 | 0.000 | 1081 |
| vanilla | FMPP | mape | 1.446 | 0.148 | 1029 |
| vanilla | FPC | mape | -143.241 | 0.000 | 1081 |
| vanilla | FPL | mape | 18.557 | 0.000 | 1038 |
| vanilla | GCPD | mape | 15.947 | 0.000 | 1086 |
| vanilla | IPCO | mape | 11.164 | 0.000 | 1086 |
| vanilla | ISNE | mape | 40.539 | 0.000 | 1083 |
| vanilla | JEA | mape | -3.136 | 0.002 | 1065 |
| vanilla | LDWP | mape | -2.406 | 0.016 | 1039 |
| vanilla | LGEE | mape | -24.246 | 0.000 | 1095 |
| vanilla | MISO | mape | 2.542 | 0.011 | 1088 |
| vanilla | NEVP | mape | -21.254 | 0.000 | 1041 |
| vanilla | NWMT | mape | 29.774 | 0.000 | 1049 |
| vanilla | NYIS | mape | 23.459 | 0.000 | 1074 |
| vanilla | PACE | mape | -7.681 | 0.000 | 1083 |
| vanilla | PACW | mape | 2.364 | 0.018 | 1018 |
| vanilla | PGE | mape | 40.973 | 0.000 | 1087 |
| vanilla | PJM | mape | 15.652 | 0.000 | 1073 |
| vanilla | PNM | mape | -27.109 | 0.000 | 1095 |
| vanilla | PSCO | mape | 1.145 | 0.252 | 1046 |
| vanilla | PSEI | mape | -58.412 | 0.000 | 894 |
| vanilla | SC | mape | 10.856 | 0.000 | 1078 |
| vanilla | SCEG | mape | 2.894 | 0.004 | 1045 |
| vanilla | SCL | mape | 4.866 | 0.000 | 1067 |
| vanilla | SOCO | mape | 30.828 | 0.000 | 1081 |
| vanilla | SRP | mape | 17.438 | 0.000 | 1038 |
| vanilla | SWPP | mape | -11.116 | 0.000 | 1078 |
| vanilla | TEC | mape | 5.590 | 0.000 | 1072 |
| vanilla | TEPC | mape | 26.088 | 0.000 | 1065 |
| vanilla | TPWR | mape | 21.676 | 0.000 | 1087 |
| vanilla | TVA | mape | 17.389 | 0.000 | 1084 |
| vanilla | WACM | mape | -33.848 | 0.000 | 960 |
| vanilla | WALC | mape | 4.549 | 0.000 | 889 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.978 |
| last_known_day | 0.972 |
| same_type_mean_2w | 0.978 |
| same_weekday_last_week | 0.972 |
| vanilla | 0.978 |
