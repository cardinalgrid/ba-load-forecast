# The BAs' own forecast by hour of the day

EIA-930 day-ahead demand forecast (`DF`) against demand (`D`), 2023-01-01 to 2025-12-31, local hours (hour beginning), documented load-shed days left out. Days on which `DF` is off by more than 50% of the demand at any hour are counted apart as reporting faults and left out of the hourly tables.

## Summary

`bias_range` is the distance between the most negative and the most positive mean signed error over the 24 hours. `mape_bias_removed` is the MAPE of `DF` after dividing it by one plus its own median relative error at the same hour over the previous 60 days (the day itself left out), next to `mape_same_days`, the plain MAPE on the days where that correction exists.

| ba | days | fault_hours | fault_days | mape | mape_no_fault_days | bias_min | hour_of_min | bias_max | hour_of_max | bias_range | mape_same_days | mape_bias_removed | model_mape | model_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CISO | 1085 | 1 | 1 | 6.87 | 6.87 | -16.43 | 11 | 5.30 | 17 | 21.73 | 6.90 | 3.22 | 2.86 | 1064 | 25355.37 |
| PJM | 1090 | 1 | 1 | 3.48 | 3.48 | -6.25 | 23 | 2.94 | 5 | 9.19 | 3.48 | 2.10 | 2.31 | 1065 | 92943.47 |
| FPL | 1079 | 14 | 8 | 6.01 | 3.21 | -4.01 | 23 | 4.14 | 8 | 8.15 | 3.22 | 2.23 | 3.66 | 1047 | 16584.29 |
| ISNE | 1091 | 0 | 0 | 2.56 | 2.56 | -5.75 | 3 | 0.79 | 17 | 6.54 | 2.57 | 1.93 | 3.95 | 1067 | 12987.95 |
| ERCO | 1090 | 0 | 0 | 2.41 | 2.41 | -0.55 | 5 | 1.62 | 13 | 2.17 | 2.40 | 2.23 | 2.62 | 1070 | 53198.63 |
| MISO | 1093 | 0 | 0 | 2.71 | 2.71 | 1.55 | 23 | 3.16 | 6 | 1.60 | 2.72 | 1.64 | 1.95 | 1073 | 74145.78 |
| BPAT | 1093 | 0 | 0 | 2.01 | 2.01 | -0.40 | 15 | 0.47 | 4 | 0.88 | 2.00 | 1.99 | 2.40 | 1073 | 6761.19 |
| SWPP | 1091 | 2 | 2 | 4.43 | 4.33 | 1.92 | 0 | 2.77 | 19 | 0.85 | 4.34 | 2.69 | 2.64 | 1069 | 33076.47 |
| TVA | 1093 | 1 | 1 | 2.28 | 2.28 | 0.77 | 3 | 1.46 | 20 | 0.69 | 2.28 | 2.15 | 3.02 | 1072 | 18782.85 |
| DUK | 1092 | 0 | 0 | 2.65 | 2.65 | 0.30 | 2 | 0.89 | 23 | 0.58 | 2.66 | 2.63 | 3.54 | 1067 | 12266.23 |
| NYIS | 1093 | 92 | 4 | 2.97 | 2.63 | -2.44 | 16 | -1.95 | 12 | 0.49 | 2.63 | 1.72 | 2.92 | 1065 | 17100.98 |

`model_mape` is the MAPE of `final2` (stored hourly forecasts of the `frozen` group) on the days it shares with the corrected `DF`; the two `DF` columns are on those same days. Weighted by mean demand over the BAs: `DF` 3.28 %, `DF` with its hourly bias removed 2.16 %, `final2` 2.58 %.

## Mean signed error by hour (%, negative is under-forecast)

| ba | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CISO | -5.2 | -5.5 | -5.3 | -4.2 | -1.8 | 2.1 | 4.4 | 1.6 | -5.1 | -11.8 | -15.3 | -16.4 | -15.4 | -12.4 | -8.2 | -2.8 | 2.1 | 5.3 | 3.4 | 0.9 | -1.1 | -2.5 | -5.5 | -6.5 |
| PJM | -6.0 | -5.5 | -4.7 | -3.0 | -0.1 | 2.9 | 2.5 | 0.7 | -0.2 | -0.1 | -0.1 | -0.0 | -0.1 | -0.4 | -0.1 | 1.0 | 1.8 | 0.4 | -0.8 | -1.5 | -3.0 | -5.0 | -5.9 | -6.3 |
| FPL | -2.8 | -1.9 | -1.3 | -0.6 | 0.7 | 2.8 | 2.3 | 3.2 | 4.1 | 3.7 | 3.2 | 3.0 | 2.6 | 2.1 | 1.6 | 1.0 | 0.5 | 0.4 | -0.8 | -1.5 | -2.0 | -3.0 | -3.8 | -4.0 |
| ISNE | -3.0 | -4.5 | -5.4 | -5.7 | -5.3 | -3.1 | -1.2 | -0.7 | -0.9 | -1.3 | -1.9 | -2.4 | -2.5 | -2.1 | -1.3 | -0.4 | 0.4 | 0.8 | 0.7 | 0.3 | -0.0 | -0.2 | -0.5 | -1.1 |
| ERCO | 0.5 | 0.1 | -0.2 | -0.4 | -0.5 | -0.6 | -0.3 | 0.0 | 0.7 | 1.4 | 1.6 | 1.6 | 1.6 | 1.6 | 1.6 | 1.5 | 1.2 | 1.0 | 0.9 | 0.8 | 0.7 | 0.6 | 0.5 | 0.5 |
| MISO | 1.7 | 1.6 | 2.0 | 2.3 | 2.7 | 3.0 | 3.2 | 3.1 | 2.9 | 2.7 | 2.6 | 2.5 | 2.4 | 2.4 | 2.4 | 2.4 | 2.4 | 2.5 | 2.4 | 2.3 | 2.1 | 2.0 | 1.7 | 1.6 |
| BPAT | -0.3 | 0.0 | 0.4 | 0.4 | 0.5 | 0.4 | 0.3 | 0.2 | 0.2 | 0.1 | -0.1 | -0.2 | -0.3 | -0.3 | -0.4 | -0.4 | -0.3 | -0.2 | -0.0 | -0.0 | -0.1 | 0.0 | 0.1 | 0.3 |
| SWPP | 1.9 | 2.0 | 2.2 | 2.2 | 2.3 | 2.4 | 2.6 | 2.6 | 2.6 | 2.6 | 2.6 | 2.6 | 2.6 | 2.5 | 2.5 | 2.6 | 2.6 | 2.6 | 2.7 | 2.8 | 2.7 | 2.6 | 2.5 | 2.4 |
| TVA | 0.9 | 0.9 | 0.8 | 0.8 | 0.8 | 0.9 | 0.9 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.4 | 1.5 | 1.3 | 1.2 | 1.2 |
| DUK | 0.6 | 0.5 | 0.3 | 0.4 | 0.6 | 0.8 | 0.5 | 0.7 | 0.7 | 0.6 | 0.5 | 0.5 | 0.4 | 0.3 | 0.4 | 0.5 | 0.8 | 0.8 | 0.8 | 0.8 | 0.7 | 0.6 | 0.7 | 0.9 |
| NYIS | -2.2 | -2.2 | -2.2 | -2.2 | -2.2 | -2.2 | -2.4 | -2.4 | -2.3 | -2.2 | -2.1 | -2.0 | -2.0 | -2.0 | -2.2 | -2.4 | -2.4 | -2.4 | -2.2 | -2.1 | -2.1 | -2.1 | -2.0 | -2.0 |

## MAPE by hour (%)

| ba | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CISO | 5.2 | 5.5 | 5.3 | 4.3 | 2.3 | 2.9 | 5.0 | 3.0 | 5.5 | 11.9 | 15.4 | 16.5 | 15.8 | 13.5 | 10.4 | 6.9 | 5.3 | 5.9 | 4.0 | 2.9 | 2.4 | 2.8 | 5.6 | 6.5 |
| PJM | 6.1 | 5.5 | 4.8 | 3.4 | 2.9 | 4.5 | 3.3 | 1.8 | 2.1 | 2.5 | 2.8 | 3.0 | 3.0 | 2.8 | 2.5 | 2.3 | 2.7 | 2.3 | 2.3 | 2.4 | 3.3 | 5.1 | 5.9 | 6.3 |
| FPL | 3.4 | 2.6 | 1.9 | 1.7 | 1.7 | 3.2 | 2.7 | 3.3 | 4.3 | 3.9 | 3.6 | 3.4 | 3.1 | 3.0 | 3.1 | 3.2 | 3.2 | 3.4 | 3.2 | 3.2 | 3.3 | 3.8 | 4.4 | 4.6 |
| ISNE | 3.1 | 4.5 | 5.4 | 5.8 | 5.3 | 3.3 | 1.7 | 1.3 | 1.4 | 1.6 | 2.5 | 3.0 | 3.2 | 3.0 | 2.6 | 2.0 | 1.7 | 1.7 | 1.5 | 1.3 | 1.2 | 1.2 | 1.3 | 1.8 |
| ERCO | 2.0 | 2.0 | 2.2 | 2.2 | 2.1 | 2.1 | 2.2 | 2.3 | 2.5 | 2.8 | 2.7 | 2.6 | 2.7 | 2.8 | 2.8 | 2.8 | 2.7 | 2.6 | 2.4 | 2.3 | 2.3 | 2.3 | 2.2 | 2.2 |
| MISO | 2.2 | 2.2 | 2.4 | 2.7 | 2.9 | 3.2 | 3.3 | 3.2 | 3.0 | 2.9 | 2.8 | 2.8 | 2.8 | 2.8 | 2.9 | 2.9 | 2.9 | 2.9 | 2.8 | 2.6 | 2.4 | 2.3 | 2.2 | 2.2 |
| BPAT | 1.8 | 1.8 | 1.8 | 1.9 | 1.9 | 1.9 | 1.9 | 1.9 | 1.8 | 1.7 | 1.8 | 2.0 | 2.1 | 2.3 | 2.4 | 2.4 | 2.4 | 2.3 | 2.2 | 2.1 | 2.0 | 1.9 | 1.9 | 2.0 |
| SWPP | 3.8 | 4.0 | 4.2 | 4.2 | 4.2 | 4.1 | 4.2 | 4.2 | 4.1 | 4.1 | 4.1 | 4.2 | 4.4 | 4.5 | 4.6 | 4.7 | 4.6 | 4.7 | 4.6 | 4.6 | 4.4 | 4.3 | 4.4 | 4.6 |
| TVA | 2.0 | 2.0 | 2.0 | 2.0 | 2.1 | 2.1 | 2.2 | 2.0 | 1.9 | 1.9 | 2.1 | 2.3 | 2.4 | 2.6 | 2.7 | 2.8 | 2.8 | 2.7 | 2.6 | 2.4 | 2.4 | 2.2 | 2.2 | 2.2 |
| DUK | 2.3 | 2.4 | 2.4 | 2.5 | 2.5 | 2.6 | 2.5 | 2.5 | 2.3 | 2.3 | 2.3 | 2.5 | 2.7 | 2.8 | 2.9 | 3.0 | 3.1 | 3.2 | 3.1 | 3.0 | 2.7 | 2.7 | 2.7 | 2.6 |
| NYIS | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 | 2.5 | 2.6 | 2.6 | 2.7 | 2.8 | 2.9 | 2.9 | 3.0 | 3.0 | 3.1 | 3.1 | 2.9 | 2.7 | 2.6 | 2.5 | 2.4 | 2.4 | 2.4 |

## Time alignment of `DF` and `D`, year by year

MAPE of `DF` as published (`+0h`) and with the value stamped one hour earlier (`-1h`) or later (`+1h`) compared with the same `D`. Only the BA-years in which a moved series beats the published one by 0.3 points or more are listed; the full table is `results/df_profile/alignment_by_year.csv`.

| ba | year | mape_shift_-1h | mape_shift_+0h | mape_shift_+1h | best_shift_h |
| --- | --- | --- | --- | --- | --- |
| PJM | 2019 | 2.34 | 3.64 | 5.90 | -1 |
| PJM | 2020 | 2.49 | 3.89 | 6.04 | -1 |
| PJM | 2021 | 2.36 | 3.62 | 5.80 | -1 |
| PJM | 2022 | 2.49 | 3.64 | 5.68 | -1 |
| PJM | 2023 | 2.29 | 3.45 | 5.50 | -1 |
| PJM | 2024 | 2.43 | 3.56 | 5.56 | -1 |
| PJM | 2025 | 2.47 | 3.44 | 5.26 | -1 |
| CISO | 2016 | 2.62 | 3.28 | 5.79 | -1 |
| CISO | 2023 | 3.57 | 5.50 | 8.19 | -1 |
| CISO | 2024 | 5.49 | 6.97 | 9.20 | -1 |
| CISO | 2025 | 7.11 | 8.14 | 9.91 | -1 |

## Reading

A forecast issued once, a day ahead, by a model without a systematic fault has a signed error near zero at every hour. Where the signed error swings by several points between the night and the morning, and the swing is stable from year to year (`results/df_profile/<BA>_bias_by_year_hour.csv`), the published `DF` and `D` are unlikely to measure the same quantity at those hours, or `DF` is not the forecast the operator used for the night. The EIA-930 instructions ask for "the day-ahead demand forecast generated in the normal course of business" and fix neither the hour of issue nor the treatment of pumping load or of behind-the-meter generation, so the cause cannot be settled from the data alone. Two consequences for a comparison against `DF`: a model that learns the demand series directly gains at those hours for a reason that is not forecasting skill, and the fair reading of a win or a loss looks at the hours as well as at the daily mean.
