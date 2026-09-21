# The BAs' own forecast by hour of the day

EIA-930 day-ahead demand forecast (`DF`) against demand (`D`), 2020-12-02 to 2022-12-31, local hours (hour beginning), documented load-shed days left out. Days on which `DF` is off by more than 50% of the demand at any hour are counted apart as reporting faults and left out of the hourly tables.

## Summary

`bias_range` is the distance between the most negative and the most positive mean signed error over the 24 hours. `mape_bias_removed` is the MAPE of `DF` after dividing it by one plus its own median relative error at the same hour over the previous 60 days (the day itself left out), next to `mape_same_days`, the plain MAPE on the days where that correction exists.

| ba | days | fault_hours | fault_days | mape | mape_no_fault_days | bias_min | hour_of_min | bias_max | hour_of_max | bias_range | mape_same_days | mape_bias_removed | model_mape | model_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PJM | 757 | 3 | 2 | 3.66 | 3.65 | -6.67 | 23 | 3.21 | 5 | 9.88 | 3.64 | 2.24 | 2.30 | 734 | 91840.34 |
| FPL | 729 | 6 | 5 | 4.40 | 3.93 | -6.66 | 23 | 1.42 | 8 | 8.07 | 3.91 | 2.45 | 3.76 | 703 | 15202.94 |
| ISNE | 758 | 0 | 0 | 2.36 | 2.36 | -5.83 | 3 | 0.70 | 17 | 6.54 | 2.36 | 1.73 | 3.45 | 737 | 13388.59 |
| CISO | 751 | 0 | 0 | 2.80 | 2.80 | -3.86 | 10 | 1.73 | 17 | 5.59 | 2.83 | 2.10 | 2.66 | 728 | 25198.70 |
| ERCO | 754 | 0 | 0 | 2.63 | 2.63 | -1.00 | 3 | 1.08 | 14 | 2.07 | 2.65 | 2.55 | 2.80 | 731 | 46743.21 |
| MISO | 754 | 0 | 0 | 2.64 | 2.64 | 0.77 | 1 | 2.83 | 9 | 2.06 | 2.64 | 1.74 | 2.12 | 731 | 73854.02 |
| SWPP | 755 | 21 | 2 | 3.85 | 3.76 | 2.09 | 0 | 4.13 | 15 | 2.05 | 3.79 | 2.53 | 2.37 | 730 | 31338.12 |
| DUK | 756 | 0 | 0 | 2.84 | 2.84 | -0.13 | 13 | 1.09 | 17 | 1.21 | 2.84 | 2.84 | 3.37 | 735 | 12125.27 |
| BPAT | 758 | 0 | 0 | 2.08 | 2.08 | 0.10 | 0 | 0.78 | 8 | 0.69 | 2.08 | 2.04 | 2.54 | 735 | 6535.95 |
| TVA | 756 | 1 | 1 | 2.27 | 2.23 | 0.09 | 3 | 0.77 | 20 | 0.68 | 2.22 | 2.21 | 3.01 | 732 | 18578.89 |
| NYIS | 758 | 0 | 0 | 2.67 | 2.67 | -2.58 | 6 | -2.18 | 20 | 0.40 | 2.65 | 1.63 | 2.49 | 737 | 17393.82 |

`model_mape` is the MAPE of `final2` (stored hourly forecasts of the `final2` group) on the days it shares with the corrected `DF`; the two `DF` columns are on those same days. Weighted by mean demand over the BAs: `DF` 3.04 %, `DF` with its hourly bias removed 2.17 %, `final2` 2.55 %.

## Mean signed error by hour (%, negative is under-forecast)

| ba | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PJM | -6.2 | -5.4 | -4.5 | -2.8 | 0.2 | 3.2 | 2.9 | 1.4 | 0.7 | 0.7 | 0.7 | 0.5 | 0.2 | -0.3 | -0.2 | 0.8 | 1.8 | 0.3 | -1.0 | -1.6 | -3.1 | -5.1 | -6.1 | -6.7 |
| FPL | -5.6 | -4.6 | -3.7 | -3.0 | -1.9 | -0.3 | -0.8 | 0.2 | 1.4 | 1.1 | 0.4 | -0.2 | -0.6 | -1.1 | -1.4 | -2.1 | -2.8 | -2.8 | -4.0 | -4.4 | -4.9 | -6.0 | -6.3 | -6.7 |
| ISNE | -2.7 | -4.4 | -5.5 | -5.8 | -5.2 | -3.2 | -1.4 | -0.8 | -0.4 | -0.4 | -0.5 | -0.8 | -1.0 | -1.0 | -0.7 | -0.2 | 0.4 | 0.7 | 0.6 | 0.4 | 0.1 | -0.2 | -0.5 | -1.3 |
| CISO | -2.2 | -2.3 | -2.4 | -2.3 | -1.6 | -0.4 | 0.3 | -0.4 | -1.9 | -3.3 | -3.9 | -3.5 | -2.6 | -1.4 | -0.1 | 0.9 | 1.5 | 1.7 | 0.8 | 0.0 | -0.5 | -1.1 | -2.0 | -2.3 |
| ERCO | -0.1 | -0.5 | -0.9 | -1.0 | -1.0 | -0.8 | -0.5 | -0.3 | -0.3 | -0.1 | 0.3 | 0.6 | 0.9 | 1.0 | 1.1 | 1.0 | 0.9 | 0.8 | 0.8 | 0.7 | 0.7 | 0.5 | 0.3 | 0.2 |
| MISO | 1.0 | 0.8 | 0.9 | 1.2 | 1.7 | 2.3 | 2.7 | 2.8 | 2.8 | 2.8 | 2.8 | 2.8 | 2.7 | 2.6 | 2.5 | 2.5 | 2.5 | 2.7 | 2.6 | 2.4 | 2.2 | 2.0 | 1.7 | 1.3 |
| SWPP | 2.1 | 2.2 | 2.4 | 2.5 | 2.5 | 2.3 | 2.6 | 2.7 | 2.5 | 2.8 | 3.0 | 3.1 | 3.7 | 3.9 | 4.0 | 4.1 | 4.0 | 3.9 | 3.7 | 3.5 | 3.4 | 3.0 | 2.8 | 2.7 |
| DUK | 0.3 | 0.1 | -0.0 | 0.2 | 0.5 | 0.8 | 0.4 | 0.1 | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 | 0.1 | 0.3 | 0.6 | 1.1 | 0.9 | 0.9 | 0.7 | 0.4 | 0.4 | 1.0 |
| BPAT | 0.1 | 0.5 | 0.6 | 0.6 | 0.7 | 0.7 | 0.7 | 0.8 | 0.8 | 0.6 | 0.5 | 0.3 | 0.2 | 0.2 | 0.1 | 0.2 | 0.2 | 0.3 | 0.4 | 0.5 | 0.4 | 0.5 | 0.5 | 0.6 |
| TVA | 0.2 | 0.1 | 0.1 | 0.1 | 0.2 | 0.3 | 0.3 | 0.2 | 0.3 | 0.4 | 0.3 | 0.4 | 0.4 | 0.4 | 0.4 | 0.5 | 0.5 | 0.6 | 0.6 | 0.7 | 0.8 | 0.6 | 0.6 | 0.6 |
| NYIS | -2.4 | -2.4 | -2.4 | -2.5 | -2.5 | -2.5 | -2.6 | -2.6 | -2.4 | -2.3 | -2.3 | -2.3 | -2.3 | -2.3 | -2.2 | -2.3 | -2.4 | -2.4 | -2.3 | -2.2 | -2.2 | -2.2 | -2.2 | -2.2 |

## MAPE by hour (%)

| ba | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PJM | 6.2 | 5.5 | 4.6 | 3.3 | 2.9 | 4.6 | 3.6 | 2.3 | 2.6 | 3.0 | 3.1 | 3.0 | 2.9 | 2.8 | 2.5 | 2.3 | 2.9 | 2.5 | 2.6 | 2.7 | 3.5 | 5.3 | 6.2 | 6.7 |
| FPL | 5.8 | 4.9 | 3.9 | 3.2 | 2.4 | 2.1 | 2.4 | 2.6 | 2.9 | 2.8 | 2.5 | 2.4 | 2.6 | 2.9 | 3.3 | 3.7 | 4.0 | 4.1 | 4.7 | 5.0 | 5.4 | 6.4 | 7.0 | 7.3 |
| ISNE | 2.8 | 4.4 | 5.5 | 5.9 | 5.2 | 3.4 | 1.9 | 1.3 | 1.0 | 0.9 | 1.4 | 1.9 | 2.2 | 2.2 | 2.3 | 2.1 | 1.7 | 1.6 | 1.5 | 1.4 | 1.3 | 1.3 | 1.4 | 1.9 |
| CISO | 2.7 | 2.7 | 2.7 | 2.5 | 1.9 | 1.7 | 2.4 | 2.2 | 2.7 | 3.8 | 4.4 | 4.4 | 4.0 | 3.6 | 3.2 | 3.0 | 3.0 | 2.8 | 2.0 | 1.8 | 1.9 | 2.1 | 2.8 | 3.0 |
| ERCO | 2.2 | 2.4 | 2.6 | 2.6 | 2.6 | 2.5 | 2.6 | 2.6 | 2.4 | 2.3 | 2.4 | 2.6 | 2.7 | 2.8 | 2.9 | 3.0 | 3.0 | 2.9 | 2.8 | 2.7 | 2.6 | 2.6 | 2.6 | 2.7 |
| MISO | 1.7 | 1.7 | 1.8 | 2.0 | 2.3 | 2.8 | 3.0 | 3.1 | 3.1 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 2.9 | 3.0 | 3.0 | 3.0 | 3.0 | 2.7 | 2.6 | 2.4 | 2.3 | 2.1 |
| SWPP | 2.9 | 3.0 | 3.2 | 3.3 | 3.3 | 3.0 | 3.3 | 3.3 | 3.1 | 3.3 | 3.5 | 3.7 | 4.3 | 4.5 | 4.6 | 4.8 | 4.7 | 4.6 | 4.4 | 4.2 | 4.0 | 3.7 | 3.6 | 3.7 |
| DUK | 2.4 | 2.4 | 2.5 | 2.6 | 2.8 | 3.0 | 2.7 | 2.4 | 2.3 | 2.3 | 2.4 | 2.7 | 2.9 | 3.0 | 3.1 | 3.2 | 3.3 | 3.5 | 3.3 | 3.2 | 3.0 | 3.0 | 2.9 | 3.0 |
| BPAT | 1.7 | 1.7 | 1.8 | 1.8 | 1.9 | 1.9 | 2.0 | 1.9 | 1.8 | 1.8 | 1.9 | 2.1 | 2.2 | 2.4 | 2.6 | 2.6 | 2.6 | 2.5 | 2.3 | 2.3 | 2.2 | 2.0 | 2.0 | 2.1 |
| TVA | 1.9 | 2.0 | 2.0 | 2.0 | 2.0 | 2.1 | 2.0 | 1.9 | 1.7 | 1.8 | 2.0 | 2.2 | 2.4 | 2.6 | 2.8 | 2.8 | 2.8 | 2.7 | 2.5 | 2.3 | 2.2 | 2.1 | 2.2 | 2.2 |
| NYIS | 2.5 | 2.5 | 2.6 | 2.6 | 2.6 | 2.6 | 2.7 | 2.7 | 2.6 | 2.5 | 2.6 | 2.7 | 2.8 | 2.8 | 2.9 | 2.9 | 3.0 | 2.9 | 2.8 | 2.7 | 2.6 | 2.5 | 2.5 | 2.5 |

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
