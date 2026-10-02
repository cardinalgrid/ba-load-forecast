# The recipe on the 43 BAs of the station map, 2023 to 2025, under protocol v2

All BAs of the station map with data on 2023 to 2025 (the eleven development BAs and 32 others, one station each), 2023-01-01 to 2025-12-31, 9 a.m. cut-off, protocol v2. The recipe is `final10s` (point `final8`, band with the NBM spread factor), unchanged from the development BAs. For the 32 new BAs this is the first evaluation; for the eleven it repeats `docs/phase_o_frozen_band_spread_alone.md`. Five BAs (AVA, FPC, LGEE, PSEI, TEPC) have a published forecast that the EIA lists as not comparable with their demand; their rows against `DF` carry that caveat.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10s | 2.11 | 1.84 | -0.13 | -1.20 | 1.14 | 0.67 | 0.28 | -31.78 | 14647 | 14.00 |
| final10s_ensemble | 2.29 | 2.05 | -1.70 | -2.17 | 1.14 | 0.63 | 0.17 | -32.23 | 14647 | 14.00 |
| final10s_boosting | 2.35 | 2.07 | -1.63 | -2.16 | 1.27 | 0.61 | 0.19 | -32.08 | 14647 | 14.00 |
| final10s_additive | 2.53 | 2.28 | -1.70 | -2.33 | 1.23 | 0.58 | 0.18 | -33.54 | 14647 | 14.00 |
| final10s_recency | 3.09 | 2.78 | -1.83 | -2.52 | 1.55 | 0.45 | 0.17 | -40.49 | 14647 | 14.00 |
| DF | 3.10 | 2.79 | 0.00 | -1.37 | 1.04 | 0.00 | 0.00 | -49.40 | 14647 | 14.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | AVA | 1.75 | 1.50 | -0.33 | -1.15 | 1.29 | -14.38 |  |  | 1065 | 1484.88 |
| DF | BANC | 2.23 | 1.88 | -0.12 | -1.48 | 0.96 | -32.40 |  |  | 1038 | 2002.87 |
| DF | CISO | 5.36 | 5.12 | -1.74 | -2.63 | 1.20 | -33.79 |  |  | 1044 | 25453.81 |
| DF | CPLE | 4.10 | 3.39 | 1.04 | -1.46 | 1.22 | -20.38 |  |  | 1074 | 7009.52 |
| DF | ERCO | 2.40 | 1.99 | 0.79 | -0.80 | 1.01 | -11.36 |  |  | 1071 | 53336.07 |
| DF | IPCO | 3.53 | 2.87 | -0.72 | -1.99 | 1.95 | -35.63 |  |  | 1080 | 2133.48 |
| DF | LDWP | 8.07 | 7.12 | -8.29 | -9.24 | 2.71 | -34.92 |  |  | 1015 | 2721.75 |
| DF | MISO | 2.72 | 2.51 | 2.03 | -0.22 | 0.85 | -6.54 |  |  | 1084 | 74014.33 |
| DF | PACW | 4.38 | 3.42 | 2.16 | -0.74 | 1.57 | -13.23 |  |  | 1012 | 2410.19 |
| DF | PGE | 1.33 | 1.14 | -0.12 | -0.94 | 1.15 | -9.74 |  |  | 1081 | 2612.74 |
| DF | PJM | 2.40 | 2.17 | -0.55 | -1.17 | 0.95 | -7.65 |  |  | 1061 | 93218.11 |
| DF | PSEI | 22.60 | 21.39 | -28.53 | -28.56 | 4.65 | -49.40 |  |  | 890 | 2868.94 |
| DF | SCL | 3.28 | 3.01 | -2.86 | -3.36 | 1.51 | -23.98 |  |  | 1051 | 1080.52 |
| DF | TPWR | 2.42 | 2.00 | 0.25 | -0.98 | 1.27 | -25.00 |  |  | 1081 | 527.75 |
| final10s | AVA | 2.42 | 2.04 | -0.05 | -1.33 | 1.45 | -14.60 | 0.27 | 0.32 | 1065 | 1484.88 |
| final10s | BANC | 2.78 | 2.40 | -0.45 | -1.85 | 1.12 | -31.78 | 0.30 | 0.29 | 1038 | 2002.87 |
| final10s | CISO | 2.62 | 2.41 | -0.35 | -1.46 | 1.05 | -15.45 | 0.90 | 0.39 | 1044 | 25453.81 |
| final10s | CPLE | 3.61 | 3.14 | -0.19 | -2.03 | 1.29 | -15.97 | 0.54 | 0.23 | 1074 | 7009.52 |
| final10s | ERCO | 2.21 | 1.87 | 0.05 | -1.20 | 0.87 | -16.19 | 0.54 | 0.23 | 1071 | 53336.07 |
| final10s | IPCO | 2.85 | 2.44 | -0.38 | -1.57 | 1.43 | -15.45 | 0.61 | 0.34 | 1080 | 2133.48 |
| final10s | LDWP | 5.27 | 4.59 | -3.32 | -4.58 | 2.27 | -31.47 | 0.80 | 0.71 | 1015 | 2721.75 |
| final10s | MISO | 1.74 | 1.52 | -0.01 | -0.90 | 1.29 | -6.79 | 0.73 | 0.08 | 1084 | 74014.33 |
| final10s | PACW | 2.90 | 2.41 | -0.60 | -1.82 | 1.49 | -28.36 | 0.69 | 0.14 | 1012 | 2410.19 |
| final10s | PGE | 2.35 | 2.02 | -0.28 | -1.47 | 1.46 | -13.02 | 0.18 | 0.30 | 1081 | 2612.74 |
| final10s | PJM | 1.93 | 1.66 | -0.15 | -1.13 | 1.12 | -10.32 | 0.67 | 0.41 | 1061 | 93218.11 |
| final10s | PSEI | 2.58 | 2.17 | 0.07 | -1.42 | 1.23 | -11.90 | 1.00 | 0.99 | 890 | 2868.94 |
| final10s | SCL | 2.75 | 2.41 | -0.30 | -1.53 | 1.61 | -20.58 | 0.62 | 0.69 | 1051 | 1080.52 |
| final10s | TPWR | 2.88 | 2.53 | -0.54 | -1.76 | 1.73 | -12.27 | 0.32 | 0.22 | 1081 | 527.75 |
| final10s_additive | AVA | 2.61 | 2.29 | -1.38 | -2.18 | 1.48 | -20.01 | 0.21 | 0.21 | 1065 | 1484.88 |
| final10s_additive | BANC | 3.18 | 2.83 | -3.07 | -3.64 | 1.24 | -33.54 | 0.24 | 0.15 | 1038 | 2002.87 |
| final10s_additive | CISO | 2.98 | 2.74 | -1.64 | -2.37 | 1.14 | -20.80 | 0.87 | 0.31 | 1044 | 25453.81 |
| final10s_additive | CPLE | 4.07 | 3.69 | -3.26 | -4.13 | 1.25 | -20.44 | 0.47 | 0.12 | 1074 | 7009.52 |
| final10s_additive | ERCO | 2.95 | 2.68 | -2.31 | -2.89 | 0.93 | -18.78 | 0.38 | 0.10 | 1071 | 53336.07 |
| final10s_additive | IPCO | 3.23 | 2.90 | -1.70 | -2.56 | 1.56 | -17.84 | 0.50 | 0.27 | 1080 | 2133.48 |
| final10s_additive | LDWP | 5.46 | 4.91 | -4.08 | -5.27 | 2.53 | -29.10 | 0.78 | 0.69 | 1015 | 2721.75 |
| final10s_additive | MISO | 2.03 | 1.84 | -1.37 | -1.87 | 1.43 | -9.30 | 0.65 | 0.05 | 1084 | 74014.33 |
| final10s_additive | PACW | 3.30 | 2.79 | -0.50 | -1.98 | 1.29 | -22.28 | 0.62 | 0.16 | 1012 | 2410.19 |
| final10s_additive | PGE | 2.66 | 2.28 | -1.90 | -2.61 | 1.58 | -14.96 | 0.15 | 0.21 | 1081 | 2612.74 |
| final10s_additive | PJM | 2.28 | 2.03 | -1.45 | -2.11 | 1.18 | -11.98 | 0.57 | 0.26 | 1061 | 93218.11 |
| final10s_additive | PSEI | 3.22 | 2.74 | -1.77 | -2.81 | 1.33 | -18.32 | 1.00 | 0.98 | 890 | 2868.94 |
| final10s_additive | SCL | 2.98 | 2.64 | -1.50 | -2.40 | 1.70 | -19.64 | 0.57 | 0.57 | 1051 | 1080.52 |
| final10s_additive | TPWR | 3.31 | 2.89 | -0.68 | -2.01 | 1.75 | -13.77 | 0.29 | 0.21 | 1081 | 527.75 |
| final10s_boosting | AVA | 2.62 | 2.32 | -1.84 | -2.52 | 1.64 | -15.21 | 0.21 | 0.18 | 1065 | 1484.88 |
| final10s_boosting | BANC | 3.14 | 2.80 | -2.00 | -2.88 | 1.22 | -32.08 | 0.23 | 0.21 | 1038 | 2002.87 |
| final10s_boosting | CISO | 2.72 | 2.46 | -1.12 | -1.88 | 1.07 | -15.29 | 0.88 | 0.35 | 1044 | 25453.81 |
| final10s_boosting | CPLE | 4.06 | 3.51 | -2.89 | -3.82 | 1.39 | -21.00 | 0.47 | 0.12 | 1074 | 7009.52 |
| final10s_boosting | ERCO | 2.50 | 2.17 | -2.14 | -2.60 | 1.04 | -16.04 | 0.45 | 0.10 | 1071 | 53336.07 |
| final10s_boosting | IPCO | 2.94 | 2.65 | -2.15 | -2.82 | 1.72 | -19.78 | 0.56 | 0.25 | 1080 | 2133.48 |
| final10s_boosting | LDWP | 5.44 | 4.73 | -4.79 | -5.60 | 2.18 | -31.12 | 0.79 | 0.67 | 1015 | 2721.75 |
| final10s_boosting | MISO | 1.88 | 1.68 | -1.36 | -1.75 | 1.38 | -10.32 | 0.69 | 0.04 | 1084 | 74014.33 |
| final10s_boosting | PACW | 3.22 | 2.75 | -1.64 | -2.60 | 1.62 | -28.36 | 0.64 | 0.12 | 1012 | 2410.19 |
| final10s_boosting | PGE | 2.61 | 2.29 | -1.99 | -2.60 | 1.59 | -13.25 | 0.13 | 0.20 | 1081 | 2612.74 |
| final10s_boosting | PJM | 2.22 | 1.95 | -1.51 | -2.03 | 1.29 | -12.58 | 0.58 | 0.27 | 1061 | 93218.11 |
| final10s_boosting | PSEI | 2.71 | 2.34 | -1.02 | -2.04 | 1.39 | -16.87 | 1.00 | 0.99 | 890 | 2868.94 |
| final10s_boosting | SCL | 2.84 | 2.53 | -1.28 | -2.13 | 1.65 | -19.09 | 0.61 | 0.60 | 1051 | 1080.52 |
| final10s_boosting | TPWR | 3.07 | 2.70 | -1.24 | -2.23 | 1.80 | -13.61 | 0.29 | 0.18 | 1081 | 527.75 |
| final10s_ensemble | AVA | 2.43 | 2.18 | -1.59 | -2.24 | 1.49 | -16.94 | 0.26 | 0.19 | 1065 | 1484.88 |
| final10s_ensemble | BANC | 2.95 | 2.64 | -2.55 | -3.19 | 1.21 | -32.23 | 0.25 | 0.15 | 1038 | 2002.87 |
| final10s_ensemble | CISO | 2.76 | 2.56 | -1.40 | -2.09 | 1.27 | -17.15 | 0.89 | 0.33 | 1044 | 25453.81 |
| final10s_ensemble | CPLE | 3.69 | 3.27 | -2.98 | -3.72 | 1.25 | -19.00 | 0.53 | 0.11 | 1074 | 7009.52 |
| final10s_ensemble | ERCO | 2.54 | 2.24 | -2.29 | -2.68 | 0.80 | -17.49 | 0.45 | 0.08 | 1071 | 53336.07 |
| final10s_ensemble | IPCO | 2.89 | 2.51 | -1.85 | -2.52 | 1.49 | -15.78 | 0.56 | 0.26 | 1080 | 2133.48 |
| final10s_ensemble | LDWP | 5.29 | 4.64 | -4.41 | -5.30 | 2.28 | -30.35 | 0.81 | 0.70 | 1015 | 2721.75 |
| final10s_ensemble | MISO | 1.88 | 1.72 | -1.43 | -1.78 | 1.26 | -9.25 | 0.69 | 0.04 | 1084 | 74014.33 |
| final10s_ensemble | PACW | 3.00 | 2.54 | -0.77 | -1.93 | 1.34 | -24.52 | 0.68 | 0.15 | 1012 | 2410.19 |
| final10s_ensemble | PGE | 2.49 | 2.20 | -1.84 | -2.43 | 1.49 | -14.02 | 0.16 | 0.20 | 1081 | 2612.74 |
| final10s_ensemble | PJM | 2.08 | 1.84 | -1.48 | -1.95 | 1.13 | -10.76 | 0.64 | 0.24 | 1061 | 93218.11 |
| final10s_ensemble | PSEI | 2.76 | 2.35 | -2.12 | -2.73 | 1.30 | -15.67 | 1.00 | 0.99 | 890 | 2868.94 |
| final10s_ensemble | SCL | 2.76 | 2.48 | -1.31 | -2.12 | 1.52 | -19.47 | 0.63 | 0.62 | 1051 | 1080.52 |
| final10s_ensemble | TPWR | 3.10 | 2.81 | -0.73 | -1.87 | 1.62 | -13.18 | 0.30 | 0.21 | 1081 | 527.75 |
| final10s_recency | AVA | 2.98 | 2.69 | -1.52 | -2.34 | 1.87 | -17.75 | 0.17 | 0.23 | 1065 | 1484.88 |
| final10s_recency | BANC | 4.26 | 3.86 | -2.78 | -3.83 | 1.78 | -30.65 | 0.12 | 0.15 | 1038 | 2002.87 |
| final10s_recency | CISO | 4.47 | 4.23 | -1.55 | -2.73 | 1.66 | -20.64 | 0.66 | 0.33 | 1044 | 25453.81 |
| final10s_recency | CPLE | 4.36 | 3.93 | -2.76 | -3.90 | 1.51 | -19.23 | 0.41 | 0.13 | 1074 | 7009.52 |
| final10s_recency | ERCO | 3.10 | 2.71 | -2.57 | -3.07 | 1.02 | -19.91 | 0.35 | 0.08 | 1071 | 53336.07 |
| final10s_recency | IPCO | 4.18 | 3.34 | -1.49 | -2.66 | 1.83 | -16.33 | 0.41 | 0.27 | 1080 | 2133.48 |
| final10s_recency | LDWP | 7.69 | 6.62 | -4.18 | -6.19 | 2.78 | -31.07 | 0.58 | 0.66 | 1015 | 2721.75 |
| final10s_recency | MISO | 2.55 | 2.29 | -1.59 | -2.05 | 1.74 | -11.32 | 0.54 | 0.05 | 1084 | 74014.33 |
| final10s_recency | PACW | 4.44 | 3.63 | 0.26 | -1.80 | 1.71 | -19.21 | 0.48 | 0.18 | 1012 | 2410.19 |
| final10s_recency | PGE | 3.39 | 3.23 | -1.62 | -2.41 | 1.92 | -16.00 | 0.07 | 0.21 | 1081 | 2612.74 |
| final10s_recency | PJM | 2.72 | 2.48 | -1.50 | -2.22 | 1.60 | -10.56 | 0.40 | 0.24 | 1061 | 93218.11 |
| final10s_recency | PSEI | 5.94 | 5.21 | -5.60 | -5.85 | 1.66 | -40.49 | 0.96 | 0.96 | 890 | 2868.94 |
| final10s_recency | SCL | 3.44 | 3.10 | -1.15 | -2.22 | 1.84 | -19.65 | 0.48 | 0.60 | 1051 | 1080.52 |
| final10s_recency | TPWR | 4.29 | 3.75 | 0.17 | -1.68 | 2.04 | -14.13 | 0.18 | 0.27 | 1081 | 527.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | AVA | gerri_heather | 3.83 | -4.81 | -4.81 | -7.37 | 5 |
| DF | BANC | gerri_heather | 2.06 | -1.74 | -1.86 | -3.29 | 6 |
| DF | CISO | gerri_heather | 4.87 | 0.22 | -0.77 | -2.41 | 6 |
| DF | CPLE | gerri_heather | 7.53 | 1.07 | -3.67 | -10.79 | 6 |
| DF | ERCO | gerri_heather | 4.26 | 1.90 | -1.57 | -9.43 | 6 |
| DF | IPCO | gerri_heather | 1.93 | 0.24 | -0.82 | -3.66 | 6 |
| DF | LDWP | gerri_heather | 6.40 | -11.16 | -12.91 | -22.52 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | PACW | gerri_heather | 3.39 | -1.38 | -3.21 | -13.23 | 6 |
| DF | PGE | gerri_heather | 1.87 | -1.51 | -2.20 | -3.97 | 6 |
| DF | PJM | gerri_heather | 2.94 | -2.00 | -2.14 | -5.86 | 6 |
| DF | PSEI | gerri_heather | 38.33 | -46.10 | -46.10 | -49.23 | 5 |
| DF | SCL | gerri_heather | 7.08 | -7.59 | -7.59 | -9.77 | 6 |
| DF | TPWR | gerri_heather | 3.49 | -4.29 | -4.75 | -10.37 | 6 |
| final10s | AVA | gerri_heather | 4.08 | -4.06 | -4.40 | -11.65 | 5 |
| final10s | BANC | gerri_heather | 2.50 | -0.55 | -1.02 | -4.19 | 6 |
| final10s | CISO | gerri_heather | 2.62 | 0.78 | -0.47 | -2.20 | 6 |
| final10s | CPLE | gerri_heather | 7.64 | 2.85 | -0.98 | -2.68 | 6 |
| final10s | ERCO | gerri_heather | 6.17 | -6.31 | -6.31 | -11.37 | 6 |
| final10s | IPCO | gerri_heather | 3.04 | -1.17 | -1.56 | -4.13 | 6 |
| final10s | LDWP | gerri_heather | 3.96 | -3.25 | -3.46 | -8.12 | 6 |
| final10s | MISO | gerri_heather | 2.71 | -1.94 | -2.12 | -4.62 | 6 |
| final10s | PACW | gerri_heather | 4.52 | -5.68 | -5.69 | -11.76 | 6 |
| final10s | PGE | gerri_heather | 4.84 | -4.45 | -5.06 | -8.91 | 6 |
| final10s | PJM | gerri_heather | 2.70 | -0.51 | -1.14 | -3.61 | 6 |
| final10s | PSEI | gerri_heather | 4.64 | -5.59 | -5.59 | -10.03 | 5 |
| final10s | SCL | gerri_heather | 5.94 | -6.14 | -6.14 | -9.94 | 6 |
| final10s | TPWR | gerri_heather | 5.07 | -6.61 | -6.61 | -11.40 | 6 |
| final10s_additive | AVA | gerri_heather | 6.23 | -6.42 | -6.72 | -20.01 | 5 |
| final10s_additive | BANC | gerri_heather | 3.11 | -3.21 | -3.21 | -8.33 | 6 |
| final10s_additive | CISO | gerri_heather | 2.68 | 1.00 | -0.56 | -1.91 | 6 |
| final10s_additive | CPLE | gerri_heather | 7.70 | -4.47 | -6.53 | -10.86 | 6 |
| final10s_additive | ERCO | gerri_heather | 8.10 | -10.35 | -10.35 | -15.06 | 6 |
| final10s_additive | IPCO | gerri_heather | 3.29 | -1.90 | -2.32 | -5.66 | 6 |
| final10s_additive | LDWP | gerri_heather | 4.23 | -5.08 | -5.45 | -9.67 | 6 |
| final10s_additive | MISO | gerri_heather | 3.00 | -3.19 | -3.19 | -5.21 | 6 |
| final10s_additive | PACW | gerri_heather | 6.94 | -7.48 | -8.11 | -20.12 | 6 |
| final10s_additive | PGE | gerri_heather | 8.46 | -3.37 | -5.59 | -12.31 | 6 |
| final10s_additive | PJM | gerri_heather | 2.45 | -0.48 | -0.97 | -2.97 | 6 |
| final10s_additive | PSEI | gerri_heather | 4.26 | -5.66 | -5.83 | -10.10 | 5 |
| final10s_additive | SCL | gerri_heather | 7.08 | -7.64 | -7.64 | -12.89 | 6 |
| final10s_additive | TPWR | gerri_heather | 4.07 | -7.00 | -7.00 | -11.30 | 6 |
| final10s_boosting | AVA | gerri_heather | 5.16 | -7.90 | -7.90 | -10.49 | 5 |
| final10s_boosting | BANC | gerri_heather | 2.32 | -0.87 | -1.47 | -3.27 | 6 |
| final10s_boosting | CISO | gerri_heather | 2.60 | 0.77 | -0.75 | -4.09 | 6 |
| final10s_boosting | CPLE | gerri_heather | 8.50 | -1.58 | -4.90 | -11.88 | 6 |
| final10s_boosting | ERCO | gerri_heather | 7.44 | -10.20 | -10.20 | -16.04 | 6 |
| final10s_boosting | IPCO | gerri_heather | 3.47 | -4.63 | -4.63 | -7.54 | 6 |
| final10s_boosting | LDWP | gerri_heather | 4.84 | -3.31 | -3.89 | -6.58 | 6 |
| final10s_boosting | MISO | gerri_heather | 2.99 | -3.66 | -3.73 | -7.14 | 6 |
| final10s_boosting | PACW | gerri_heather | 6.33 | -9.06 | -9.06 | -14.55 | 6 |
| final10s_boosting | PGE | gerri_heather | 6.59 | -9.37 | -9.37 | -12.78 | 6 |
| final10s_boosting | PJM | gerri_heather | 2.93 | -1.94 | -2.48 | -4.24 | 6 |
| final10s_boosting | PSEI | gerri_heather | 5.86 | -8.78 | -8.78 | -16.87 | 5 |
| final10s_boosting | SCL | gerri_heather | 8.45 | -9.60 | -9.60 | -13.79 | 6 |
| final10s_boosting | TPWR | gerri_heather | 6.16 | -8.80 | -8.80 | -12.15 | 6 |
| final10s_ensemble | AVA | gerri_heather | 5.19 | -6.92 | -6.92 | -14.17 | 5 |
| final10s_ensemble | BANC | gerri_heather | 2.74 | -2.50 | -2.70 | -6.20 | 6 |
| final10s_ensemble | CISO | gerri_heather | 2.47 | 0.71 | -0.62 | -3.62 | 6 |
| final10s_ensemble | CPLE | gerri_heather | 7.65 | -3.46 | -5.68 | -11.81 | 6 |
| final10s_ensemble | ERCO | gerri_heather | 7.42 | -9.41 | -9.41 | -13.58 | 6 |
| final10s_ensemble | IPCO | gerri_heather | 3.23 | -3.00 | -3.00 | -6.01 | 6 |
| final10s_ensemble | LDWP | gerri_heather | 4.38 | -4.64 | -5.34 | -9.31 | 6 |
| final10s_ensemble | MISO | gerri_heather | 2.97 | -3.39 | -3.39 | -5.71 | 6 |
| final10s_ensemble | PACW | gerri_heather | 4.45 | -6.28 | -6.28 | -10.96 | 6 |
| final10s_ensemble | PGE | gerri_heather | 5.52 | -6.17 | -6.50 | -10.64 | 6 |
| final10s_ensemble | PJM | gerri_heather | 2.44 | -1.14 | -1.68 | -4.09 | 6 |
| final10s_ensemble | PSEI | gerri_heather | 5.58 | -7.59 | -7.59 | -12.02 | 5 |
| final10s_ensemble | SCL | gerri_heather | 7.11 | -8.03 | -8.03 | -11.42 | 6 |
| final10s_ensemble | TPWR | gerri_heather | 4.43 | -7.25 | -7.25 | -10.95 | 6 |
| final10s_recency | AVA | gerri_heather | 6.79 | -6.22 | -6.22 | -12.05 | 5 |
| final10s_recency | BANC | gerri_heather | 4.69 | -3.93 | -3.93 | -8.03 | 6 |
| final10s_recency | CISO | gerri_heather | 3.45 | 0.34 | -0.92 | -4.80 | 6 |
| final10s_recency | CPLE | gerri_heather | 7.35 | -4.30 | -5.99 | -13.95 | 6 |
| final10s_recency | ERCO | gerri_heather | 7.19 | -7.44 | -7.44 | -15.08 | 6 |
| final10s_recency | IPCO | gerri_heather | 3.95 | -2.42 | -2.63 | -5.52 | 6 |
| final10s_recency | LDWP | gerri_heather | 5.08 | -5.93 | -7.22 | -12.75 | 6 |
| final10s_recency | MISO | gerri_heather | 3.74 | -3.24 | -3.26 | -7.06 | 6 |
| final10s_recency | PACW | gerri_heather | 3.80 | -0.09 | -1.59 | -6.19 | 6 |
| final10s_recency | PGE | gerri_heather | 4.96 | -6.13 | -6.29 | -11.43 | 6 |
| final10s_recency | PJM | gerri_heather | 3.15 | -0.86 | -1.96 | -5.34 | 6 |
| final10s_recency | PSEI | gerri_heather | 9.49 | -8.83 | -8.83 | -12.39 | 5 |
| final10s_recency | SCL | gerri_heather | 6.05 | -6.64 | -6.64 | -8.78 | 6 |
| final10s_recency | TPWR | gerri_heather | 3.56 | -4.74 | -4.74 | -8.33 | 6 |
| DF | AVA | january_2025 | 2.10 | -1.88 | -2.38 | -9.22 | 6 |
| DF | BANC | january_2025 | 2.14 | -2.31 | -3.27 | -6.26 | 6 |
| DF | CISO | january_2025 | 6.30 | -4.14 | -4.14 | -7.74 | 6 |
| DF | CPLE | january_2025 | 6.89 | 5.43 | -0.53 | -3.21 | 6 |
| DF | ERCO | january_2025 | 3.99 | 0.33 | -0.83 | -2.52 | 6 |
| DF | IPCO | january_2025 | 3.91 | -3.48 | -3.66 | -6.22 | 6 |
| DF | LDWP | january_2025 | 7.66 | -10.77 | -10.77 | -23.84 | 3 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | PACW | january_2025 | 3.94 | -0.67 | -1.72 | -3.40 | 6 |
| DF | PGE | january_2025 | 1.02 | 1.06 | -0.10 | -0.57 | 6 |
| DF | PJM | january_2025 | 3.35 | -2.31 | -2.32 | -4.28 | 6 |
| DF | PSEI | january_2025 | 37.60 | -41.53 | -41.53 | -47.40 | 4 |
| DF | SCL | january_2025 | 2.95 | -2.68 | -2.94 | -6.04 | 6 |
| DF | TPWR | january_2025 | 1.50 | -1.27 | -1.80 | -3.11 | 6 |
| final10s | AVA | january_2025 | 1.49 | -1.28 | -1.71 | -5.92 | 6 |
| final10s | BANC | january_2025 | 2.36 | 1.45 | -0.34 | -1.21 | 6 |
| final10s | CISO | january_2025 | 2.05 | 1.79 | 0.00 | 0.00 | 6 |
| final10s | CPLE | january_2025 | 5.65 | 4.58 | -0.81 | -4.89 | 6 |
| final10s | ERCO | january_2025 | 2.56 | -2.29 | -2.37 | -6.12 | 6 |
| final10s | IPCO | january_2025 | 2.29 | -0.28 | -1.13 | -2.18 | 6 |
| final10s | LDWP | january_2025 | 8.00 | -11.35 | -11.35 | -13.74 | 3 |
| final10s | MISO | january_2025 | 2.45 | -2.00 | -2.00 | -3.26 | 6 |
| final10s | PACW | january_2025 | 2.99 | -1.61 | -2.23 | -4.22 | 6 |
| final10s | PGE | january_2025 | 2.69 | 0.07 | -1.20 | -3.69 | 6 |
| final10s | PJM | january_2025 | 1.75 | -0.99 | -1.41 | -3.65 | 6 |
| final10s | PSEI | january_2025 | 2.72 | -0.25 | -1.46 | -3.19 | 4 |
| final10s | SCL | january_2025 | 1.96 | 0.48 | -0.80 | -2.93 | 6 |
| final10s | TPWR | january_2025 | 4.06 | -3.91 | -4.86 | -6.96 | 6 |
| final10s_additive | AVA | january_2025 | 1.99 | -2.17 | -2.17 | -5.49 | 6 |
| final10s_additive | BANC | january_2025 | 1.99 | -1.86 | -2.07 | -5.16 | 6 |
| final10s_additive | CISO | january_2025 | 2.73 | 0.81 | -0.24 | -1.11 | 6 |
| final10s_additive | CPLE | january_2025 | 5.10 | 2.50 | -0.71 | -3.66 | 6 |
| final10s_additive | ERCO | january_2025 | 3.52 | -3.89 | -3.93 | -6.84 | 6 |
| final10s_additive | IPCO | january_2025 | 3.21 | -2.26 | -2.75 | -5.43 | 6 |
| final10s_additive | LDWP | january_2025 | 12.58 | -16.88 | -16.88 | -22.95 | 3 |
| final10s_additive | MISO | january_2025 | 2.89 | -2.86 | -2.86 | -4.83 | 6 |
| final10s_additive | PACW | january_2025 | 2.96 | -2.71 | -3.22 | -5.19 | 6 |
| final10s_additive | PGE | january_2025 | 2.29 | -2.80 | -2.82 | -5.41 | 6 |
| final10s_additive | PJM | january_2025 | 2.27 | -0.75 | -1.25 | -2.22 | 6 |
| final10s_additive | PSEI | january_2025 | 3.71 | -3.19 | -3.82 | -6.04 | 4 |
| final10s_additive | SCL | january_2025 | 1.95 | -2.38 | -2.61 | -6.01 | 6 |
| final10s_additive | TPWR | january_2025 | 3.55 | -4.72 | -5.60 | -7.95 | 6 |
| final10s_boosting | AVA | january_2025 | 2.42 | -4.46 | -4.65 | -9.83 | 6 |
| final10s_boosting | BANC | january_2025 | 3.01 | -1.14 | -1.63 | -4.08 | 6 |
| final10s_boosting | CISO | january_2025 | 2.00 | -0.39 | -0.85 | -2.58 | 6 |
| final10s_boosting | CPLE | january_2025 | 6.26 | -2.21 | -4.50 | -10.12 | 6 |
| final10s_boosting | ERCO | january_2025 | 3.26 | -5.84 | -5.84 | -8.22 | 6 |
| final10s_boosting | IPCO | january_2025 | 2.59 | -3.75 | -3.75 | -7.12 | 6 |
| final10s_boosting | LDWP | january_2025 | 7.02 | -7.80 | -7.80 | -10.75 | 3 |
| final10s_boosting | MISO | january_2025 | 2.88 | -4.10 | -4.10 | -5.87 | 6 |
| final10s_boosting | PACW | january_2025 | 2.87 | -3.76 | -3.91 | -7.12 | 6 |
| final10s_boosting | PGE | january_2025 | 2.68 | -3.22 | -3.37 | -6.63 | 6 |
| final10s_boosting | PJM | january_2025 | 2.69 | -5.15 | -5.15 | -9.27 | 6 |
| final10s_boosting | PSEI | january_2025 | 2.72 | -1.91 | -2.66 | -5.54 | 4 |
| final10s_boosting | SCL | january_2025 | 2.39 | 0.01 | -1.14 | -3.45 | 6 |
| final10s_boosting | TPWR | january_2025 | 3.87 | -5.09 | -5.89 | -8.80 | 6 |
| final10s_ensemble | AVA | january_2025 | 2.23 | -3.49 | -3.57 | -7.99 | 6 |
| final10s_ensemble | BANC | january_2025 | 2.06 | -2.06 | -2.19 | -4.61 | 6 |
| final10s_ensemble | CISO | january_2025 | 2.47 | -0.01 | -0.89 | -2.29 | 6 |
| final10s_ensemble | CPLE | january_2025 | 5.49 | -0.12 | -2.29 | -7.70 | 6 |
| final10s_ensemble | ERCO | january_2025 | 3.20 | -5.47 | -5.47 | -7.26 | 6 |
| final10s_ensemble | IPCO | january_2025 | 2.58 | -3.54 | -3.54 | -5.69 | 6 |
| final10s_ensemble | LDWP | january_2025 | 7.80 | -11.72 | -11.72 | -11.88 | 3 |
| final10s_ensemble | MISO | january_2025 | 2.88 | -3.78 | -3.78 | -5.12 | 6 |
| final10s_ensemble | PACW | january_2025 | 3.01 | -3.66 | -3.88 | -6.40 | 6 |
| final10s_ensemble | PGE | january_2025 | 2.37 | -3.05 | -3.05 | -6.19 | 6 |
| final10s_ensemble | PJM | january_2025 | 2.36 | -3.20 | -3.20 | -5.34 | 6 |
| final10s_ensemble | PSEI | january_2025 | 3.35 | -3.76 | -4.00 | -6.74 | 4 |
| final10s_ensemble | SCL | january_2025 | 1.95 | -1.28 | -1.74 | -4.84 | 6 |
| final10s_ensemble | TPWR | january_2025 | 3.53 | -4.79 | -5.56 | -8.24 | 6 |
| final10s_recency | AVA | january_2025 | 3.02 | -3.84 | -3.92 | -8.61 | 6 |
| final10s_recency | BANC | january_2025 | 2.78 | -3.37 | -3.67 | -6.57 | 6 |
| final10s_recency | CISO | january_2025 | 4.80 | -0.70 | -3.08 | -5.66 | 6 |
| final10s_recency | CPLE | january_2025 | 6.52 | -0.92 | -2.72 | -9.78 | 6 |
| final10s_recency | ERCO | january_2025 | 4.09 | -6.92 | -6.92 | -8.05 | 6 |
| final10s_recency | IPCO | january_2025 | 2.78 | -4.54 | -4.54 | -7.21 | 6 |
| final10s_recency | LDWP | january_2025 | 5.93 | -10.02 | -10.02 | -17.52 | 3 |
| final10s_recency | MISO | january_2025 | 3.72 | -4.44 | -4.44 | -5.98 | 6 |
| final10s_recency | PACW | january_2025 | 3.32 | -4.59 | -4.59 | -6.99 | 6 |
| final10s_recency | PGE | january_2025 | 2.91 | -3.16 | -3.18 | -6.63 | 6 |
| final10s_recency | PJM | january_2025 | 3.25 | -3.51 | -3.51 | -6.30 | 6 |
| final10s_recency | PSEI | january_2025 | 7.42 | -8.08 | -8.08 | -10.68 | 4 |
| final10s_recency | SCL | january_2025 | 1.99 | -1.42 | -1.81 | -5.01 | 6 |
| final10s_recency | TPWR | january_2025 | 3.07 | -4.47 | -5.03 | -7.91 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final10s_ensemble | eve | 2.93 | -0.95 | -2.03 | 0.62 | 406 |
| 7 | final10s | eve | 3.04 | 0.30 | -1.53 | 0.60 | 406 |
| 8 | final10s_additive | eve | 3.12 | -1.15 | -2.38 | 0.57 | 406 |
| 9 | final10s_boosting | eve | 3.17 | -0.97 | -2.13 | 0.57 | 406 |
| 11 | final10s_recency | eve | 3.88 | -0.81 | -2.20 | 0.49 | 406 |
| 6 | DF | eve | 4.92 | -1.52 | -3.46 |  | 406 |
| 1 | final10s | special | 3.38 | -1.42 | -2.63 | 0.59 | 424 |
| 4 | final10s_ensemble | special | 3.39 | -2.62 | -3.36 | 0.59 | 424 |
| 2 | final10s_additive | special | 3.54 | -3.23 | -3.89 | 0.55 | 424 |
| 3 | final10s_boosting | special | 3.68 | -2.66 | -3.48 | 0.50 | 424 |
| 5 | final10s_recency | special | 4.30 | -1.94 | -3.25 | 0.48 | 424 |
| 0 | DF | special | 5.27 | -2.32 | -4.02 |  | 424 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10s | all | 0.418 | 1.385 | 0.400 | 0.892 | 12.619 | 0.898 | 16.360 | 1.797 | 14355 |
| final10s | events | 0.508 | 1.809 | 0.491 | 0.906 | 16.576 | 0.894 | 19.985 | 2.304 | 161 |
| final10s | cold_mornings | 0.498 | 1.512 | 0.469 | 0.913 | 15.632 | 0.900 | 19.328 | 1.988 | 420 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final10s | AVA | mape | 16.215 | 0.000 | 1065 |
| final10s | BANC | mape | 12.126 | 0.000 | 1038 |
| final10s | CISO | mape | -37.524 | 0.000 | 1044 |
| final10s | CPLE | mape | -6.966 | 0.000 | 1074 |
| final10s | ERCO | mape | -4.371 | 0.000 | 1071 |
| final10s | IPCO | mape | -8.778 | 0.000 | 1080 |
| final10s | LDWP | mape | -23.297 | 0.000 | 1015 |
| final10s | MISO | mape | -20.775 | 0.000 | 1084 |
| final10s | PACW | mape | -11.670 | 0.000 | 1012 |
| final10s | PGE | mape | 27.632 | 0.000 | 1081 |
| final10s | PJM | mape | -12.801 | 0.000 | 1061 |
| final10s | PSEI | mape | -67.483 | 0.000 | 890 |
| final10s | SCL | mape | -9.451 | 0.000 | 1051 |
| final10s | TPWR | mape | 8.410 | 0.000 | 1081 |
| final10s_additive | AVA | mape | 20.742 | 0.000 | 1065 |
| final10s_additive | BANC | mape | 18.161 | 0.000 | 1038 |
| final10s_additive | CISO | mape | -33.876 | 0.000 | 1044 |
| final10s_additive | CPLE | mape | -0.484 | 0.628 | 1074 |
| final10s_additive | ERCO | mape | 9.289 | 0.000 | 1071 |
| final10s_additive | IPCO | mape | -3.590 | 0.000 | 1080 |
| final10s_additive | LDWP | mape | -20.462 | 0.000 | 1015 |
| final10s_additive | MISO | mape | -13.105 | 0.000 | 1084 |
| final10s_additive | PACW | mape | -8.734 | 0.000 | 1012 |
| final10s_additive | PGE | mape | 29.945 | 0.000 | 1081 |
| final10s_additive | PJM | mape | -3.325 | 0.001 | 1061 |
| final10s_additive | PSEI | mape | -64.403 | 0.000 | 890 |
| final10s_additive | SCL | mape | -5.589 | 0.000 | 1051 |
| final10s_additive | TPWR | mape | 14.130 | 0.000 | 1081 |
| final10s_boosting | AVA | mape | 21.660 | 0.000 | 1065 |
| final10s_boosting | BANC | mape | 17.095 | 0.000 | 1038 |
| final10s_boosting | CISO | mape | -36.172 | 0.000 | 1044 |
| final10s_boosting | CPLE | mape | -0.594 | 0.552 | 1074 |
| final10s_boosting | ERCO | mape | 1.779 | 0.075 | 1071 |
| final10s_boosting | IPCO | mape | -7.481 | 0.000 | 1080 |
| final10s_boosting | LDWP | mape | -20.790 | 0.000 | 1015 |
| final10s_boosting | MISO | mape | -16.651 | 0.000 | 1084 |
| final10s_boosting | PACW | mape | -8.981 | 0.000 | 1012 |
| final10s_boosting | PGE | mape | 32.335 | 0.000 | 1081 |
| final10s_boosting | PJM | mape | -5.042 | 0.000 | 1061 |
| final10s_boosting | PSEI | mape | -67.514 | 0.000 | 890 |
| final10s_boosting | SCL | mape | -7.885 | 0.000 | 1051 |
| final10s_boosting | TPWR | mape | 11.515 | 0.000 | 1081 |
| final10s_ensemble | AVA | mape | 17.611 | 0.000 | 1065 |
| final10s_ensemble | BANC | mape | 15.466 | 0.000 | 1038 |
| final10s_ensemble | CISO | mape | -37.145 | 0.000 | 1044 |
| final10s_ensemble | CPLE | mape | -5.500 | 0.000 | 1074 |
| final10s_ensemble | ERCO | mape | 2.512 | 0.012 | 1071 |
| final10s_ensemble | IPCO | mape | -8.385 | 0.000 | 1080 |
| final10s_ensemble | LDWP | mape | -24.890 | 0.000 | 1015 |
| final10s_ensemble | MISO | mape | -16.434 | 0.000 | 1084 |
| final10s_ensemble | PACW | mape | -11.437 | 0.000 | 1012 |
| final10s_ensemble | PGE | mape | 29.954 | 0.000 | 1081 |
| final10s_ensemble | PJM | mape | -10.030 | 0.000 | 1061 |
| final10s_ensemble | PSEI | mape | -66.801 | 0.000 | 890 |
| final10s_ensemble | SCL | mape | -9.838 | 0.000 | 1051 |
| final10s_ensemble | TPWR | mape | 11.910 | 0.000 | 1081 |
| final10s_recency | AVA | mape | 25.928 | 0.000 | 1065 |
| final10s_recency | BANC | mape | 32.899 | 0.000 | 1038 |
| final10s_recency | CISO | mape | -10.920 | 0.000 | 1044 |
| final10s_recency | CPLE | mape | 3.091 | 0.002 | 1074 |
| final10s_recency | ERCO | mape | 11.174 | 0.000 | 1071 |
| final10s_recency | IPCO | mape | 6.628 | 0.000 | 1080 |
| final10s_recency | LDWP | mape | -3.377 | 0.001 | 1015 |
| final10s_recency | MISO | mape | -2.961 | 0.003 | 1084 |
| final10s_recency | PACW | mape | 0.616 | 0.538 | 1012 |
| final10s_recency | PGE | mape | 44.453 | 0.000 | 1081 |
| final10s_recency | PJM | mape | 7.941 | 0.000 | 1061 |
| final10s_recency | PSEI | mape | -51.088 | 0.000 | 890 |
| final10s_recency | SCL | mape | 2.466 | 0.014 | 1051 |
| final10s_recency | TPWR | mape | 23.447 | 0.000 | 1081 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.974 |
| final10s | 0.974 |
| final10s_additive | 0.955 |
| final10s_boosting | 0.974 |
| final10s_ensemble | 0.974 |
| final10s_recency | 0.974 |
