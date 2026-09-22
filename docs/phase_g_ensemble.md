# Phase G: ensemble and correction

Development BAs: ISNE, MISO, PJM, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). `ens_hourly` weights the members per hour of the day; `ens_three` adds the recency regression; `ens_ratio` uses a boosting trained on the load divided by the last known 24 h mean; `final2_*` are the corrected versions with the recipe's correction; `final2_nn30` and `final2_nn50` change the size of the nearest-temperature pool.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2_three | 2.34 | 2.03 | 0.08 | -1.23 | 1.45 | 0.55 | 0.26 | -16.85 | 2981 | 4.00 |
| final2_hourly | 2.36 | 2.07 | 0.16 | -1.22 | 1.49 | 0.53 | 0.26 | -17.45 | 2981 | 4.00 |
| final2_nn50 | 2.36 | 2.07 | 0.12 | -1.24 | 1.50 | 0.53 | 0.26 | -17.99 | 2981 | 4.00 |
| final2 | 2.36 | 2.07 | 0.15 | -1.23 | 1.54 | 0.53 | 0.26 | -17.43 | 2981 | 4.00 |
| final2_nn30 | 2.37 | 2.06 | 0.18 | -1.22 | 1.52 | 0.53 | 0.27 | -17.99 | 2981 | 4.00 |
| final2_ratio | 2.40 | 2.10 | 0.18 | -1.23 | 1.49 | 0.52 | 0.26 | -15.86 | 2981 | 4.00 |
| DF | 2.50 | 2.23 | 0.55 | -0.81 | 0.96 | 0.00 | 0.00 | -16.93 | 2981 | 4.00 |
| ens_hourly | 2.57 | 2.27 | -0.61 | -1.65 | 1.47 | 0.48 | 0.24 | -19.51 | 2981 | 4.00 |
| ens_three | 2.58 | 2.26 | -0.72 | -1.68 | 1.52 | 0.48 | 0.24 | -18.19 | 2981 | 4.00 |
| final_ensemble | 2.58 | 2.28 | -0.60 | -1.65 | 1.48 | 0.47 | 0.24 | -19.48 | 2981 | 4.00 |
| ens_ratio | 2.60 | 2.27 | -0.60 | -1.65 | 1.55 | 0.47 | 0.24 | -18.19 | 2981 | 4.00 |
| final_boosting | 2.77 | 2.45 | -0.20 | -1.52 | 1.71 | 0.43 | 0.26 | -21.43 | 2981 | 4.00 |
| final_additive | 2.79 | 2.48 | -1.01 | -1.98 | 1.68 | 0.43 | 0.23 | -20.55 | 2981 | 4.00 |
| boosting_ratio | 2.81 | 2.46 | -0.21 | -1.54 | 1.69 | 0.44 | 0.26 | -17.56 | 2981 | 4.00 |
| recency_ml | 3.22 | 2.89 | -1.00 | -2.07 | 1.89 | 0.33 | 0.22 | -20.32 | 2981 | 4.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ISNE | 2.36 | 2.31 | 0.49 | -0.48 | 0.34 | -6.96 |  |  | 752 | 13392.81 |
| DF | MISO | 2.65 | 2.30 | 2.16 | -0.19 | 0.97 | -6.70 |  |  | 746 | 73788.38 |
| DF | PJM | 2.45 | 2.23 | -0.60 | -1.27 | 1.04 | -8.98 |  |  | 744 | 91927.69 |
| DF | TVA | 2.23 | 1.92 | -0.16 | -1.25 | 0.98 | -16.93 |  |  | 739 | 18562.62 |
| boosting_ratio | ISNE | 3.69 | 3.33 | -0.72 | -2.05 | 0.61 | -17.56 | 0.26 | 0.16 | 752 | 13392.81 |
| boosting_ratio | MISO | 2.39 | 2.08 | -0.56 | -1.50 | 1.58 | -10.19 | 0.55 | 0.06 | 746 | 73788.38 |
| boosting_ratio | PJM | 2.92 | 2.56 | 0.14 | -1.42 | 1.95 | -11.43 | 0.42 | 0.42 | 744 | 91927.69 |
| boosting_ratio | TVA | 3.34 | 2.91 | -0.20 | -1.93 | 1.56 | -13.73 | 0.24 | 0.29 | 739 | 18562.62 |
| ens_hourly | ISNE | 3.52 | 3.13 | -0.96 | -2.19 | 0.51 | -19.51 | 0.27 | 0.17 | 752 | 13392.81 |
| ens_hourly | MISO | 2.22 | 1.91 | -0.94 | -1.60 | 1.52 | -8.21 | 0.57 | 0.05 | 746 | 73788.38 |
| ens_hourly | PJM | 2.60 | 2.34 | -0.29 | -1.54 | 1.56 | -10.97 | 0.47 | 0.39 | 744 | 91927.69 |
| ens_hourly | TVA | 3.13 | 2.73 | -0.63 | -2.02 | 1.49 | -14.26 | 0.28 | 0.28 | 739 | 18562.62 |
| ens_ratio | ISNE | 3.53 | 3.12 | -0.92 | -2.16 | 0.53 | -18.19 | 0.28 | 0.16 | 752 | 13392.81 |
| ens_ratio | MISO | 2.23 | 1.94 | -0.96 | -1.63 | 1.63 | -8.57 | 0.58 | 0.05 | 746 | 73788.38 |
| ens_ratio | PJM | 2.65 | 2.32 | -0.26 | -1.50 | 1.65 | -11.00 | 0.46 | 0.40 | 744 | 91927.69 |
| ens_ratio | TVA | 3.16 | 2.73 | -0.62 | -2.06 | 1.46 | -12.80 | 0.28 | 0.27 | 739 | 18562.62 |
| ens_three | ISNE | 3.65 | 3.27 | -1.42 | -2.40 | 0.52 | -18.19 | 0.25 | 0.14 | 752 | 13392.81 |
| ens_three | MISO | 2.25 | 1.92 | -1.02 | -1.63 | 1.70 | -8.77 | 0.57 | 0.05 | 746 | 73788.38 |
| ens_three | PJM | 2.58 | 2.29 | -0.37 | -1.53 | 1.54 | -11.08 | 0.48 | 0.41 | 744 | 91927.69 |
| ens_three | TVA | 3.10 | 2.71 | -0.77 | -2.11 | 1.38 | -14.95 | 0.29 | 0.26 | 739 | 18562.62 |
| final2 | ISNE | 3.43 | 2.98 | 0.64 | -1.35 | 0.51 | -17.43 | 0.30 | 0.22 | 752 | 13392.81 |
| final2 | MISO | 2.10 | 1.87 | 0.11 | -1.03 | 1.63 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2 | PJM | 2.29 | 1.98 | 0.05 | -1.31 | 1.64 | -10.41 | 0.56 | 0.42 | 744 | 91927.69 |
| final2 | TVA | 3.02 | 2.63 | 0.40 | -1.52 | 1.36 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final2_hourly | ISNE | 3.43 | 2.97 | 0.64 | -1.34 | 0.52 | -17.45 | 0.30 | 0.22 | 752 | 13392.81 |
| final2_hourly | MISO | 2.10 | 1.87 | 0.11 | -1.02 | 1.59 | -7.97 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_hourly | PJM | 2.28 | 1.99 | 0.07 | -1.30 | 1.59 | -10.48 | 0.56 | 0.42 | 744 | 91927.69 |
| final2_hourly | TVA | 3.02 | 2.64 | 0.39 | -1.52 | 1.36 | -15.98 | 0.29 | 0.33 | 739 | 18562.62 |
| final2_nn30 | ISNE | 3.46 | 3.03 | 0.73 | -1.32 | 0.53 | -17.99 | 0.30 | 0.22 | 752 | 13392.81 |
| final2_nn30 | MISO | 2.10 | 1.84 | 0.13 | -1.03 | 1.61 | -7.96 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_nn30 | PJM | 2.29 | 1.98 | 0.09 | -1.31 | 1.63 | -9.94 | 0.55 | 0.42 | 744 | 91927.69 |
| final2_nn30 | TVA | 3.03 | 2.64 | 0.41 | -1.51 | 1.34 | -15.87 | 0.29 | 0.32 | 739 | 18562.62 |
| final2_nn50 | ISNE | 3.43 | 2.99 | 0.61 | -1.36 | 0.50 | -17.99 | 0.31 | 0.22 | 752 | 13392.81 |
| final2_nn50 | MISO | 2.09 | 1.85 | 0.07 | -1.04 | 1.58 | -7.44 | 0.61 | 0.06 | 746 | 73788.38 |
| final2_nn50 | PJM | 2.29 | 1.99 | 0.03 | -1.32 | 1.60 | -10.78 | 0.55 | 0.42 | 744 | 91927.69 |
| final2_nn50 | TVA | 3.02 | 2.65 | 0.37 | -1.53 | 1.37 | -15.18 | 0.28 | 0.32 | 739 | 18562.62 |
| final2_ratio | ISNE | 3.46 | 3.00 | 0.72 | -1.33 | 0.53 | -15.86 | 0.31 | 0.21 | 752 | 13392.81 |
| final2_ratio | MISO | 2.11 | 1.83 | 0.13 | -1.04 | 1.58 | -8.54 | 0.61 | 0.07 | 746 | 73788.38 |
| final2_ratio | PJM | 2.34 | 2.07 | 0.08 | -1.31 | 1.56 | -10.24 | 0.53 | 0.41 | 744 | 91927.69 |
| final2_ratio | TVA | 3.05 | 2.64 | 0.50 | -1.51 | 1.45 | -14.28 | 0.28 | 0.32 | 739 | 18562.62 |
| final2_three | ISNE | 3.45 | 3.03 | 0.42 | -1.40 | 0.51 | -16.85 | 0.30 | 0.21 | 752 | 13392.81 |
| final2_three | MISO | 2.07 | 1.83 | 0.02 | -1.06 | 1.68 | -8.33 | 0.60 | 0.07 | 746 | 73788.38 |
| final2_three | PJM | 2.26 | 1.93 | 0.01 | -1.29 | 1.42 | -11.39 | 0.59 | 0.42 | 744 | 91927.69 |
| final2_three | TVA | 2.99 | 2.59 | 0.37 | -1.55 | 1.37 | -16.38 | 0.30 | 0.32 | 739 | 18562.62 |
| final_additive | ISNE | 3.86 | 3.46 | -1.13 | -2.51 | 0.55 | -20.55 | 0.20 | 0.16 | 752 | 13392.81 |
| final_additive | MISO | 2.44 | 2.18 | -1.41 | -1.98 | 1.81 | -9.48 | 0.53 | 0.05 | 746 | 73788.38 |
| final_additive | PJM | 2.81 | 2.47 | -0.66 | -1.83 | 1.78 | -12.10 | 0.42 | 0.37 | 744 | 91927.69 |
| final_additive | TVA | 3.35 | 2.97 | -1.05 | -2.35 | 1.42 | -14.12 | 0.25 | 0.26 | 739 | 18562.62 |
| final_boosting | ISNE | 3.67 | 3.34 | -0.81 | -2.06 | 0.60 | -21.43 | 0.25 | 0.16 | 752 | 13392.81 |
| final_boosting | MISO | 2.41 | 2.08 | -0.51 | -1.45 | 1.81 | -11.84 | 0.54 | 0.06 | 746 | 73788.38 |
| final_boosting | PJM | 2.83 | 2.54 | 0.14 | -1.43 | 1.83 | -11.75 | 0.41 | 0.42 | 744 | 91927.69 |
| final_boosting | TVA | 3.28 | 2.85 | -0.22 | -1.84 | 1.54 | -15.24 | 0.24 | 0.30 | 739 | 18562.62 |
| final_ensemble | ISNE | 3.53 | 3.16 | -0.96 | -2.20 | 0.53 | -19.48 | 0.26 | 0.16 | 752 | 13392.81 |
| final_ensemble | MISO | 2.23 | 1.94 | -0.95 | -1.61 | 1.56 | -8.41 | 0.58 | 0.05 | 746 | 73788.38 |
| final_ensemble | PJM | 2.61 | 2.34 | -0.27 | -1.53 | 1.56 | -10.89 | 0.46 | 0.39 | 744 | 91927.69 |
| final_ensemble | TVA | 3.14 | 2.72 | -0.63 | -2.02 | 1.47 | -14.12 | 0.29 | 0.28 | 739 | 18562.62 |
| recency_ml | ISNE | 5.23 | 4.91 | -2.67 | -3.43 | 0.68 | -20.32 | 0.06 | 0.11 | 752 | 13392.81 |
| recency_ml | MISO | 2.92 | 2.60 | -1.20 | -1.97 | 2.15 | -14.05 | 0.42 | 0.05 | 746 | 73788.38 |
| recency_ml | PJM | 3.09 | 2.76 | -0.58 | -1.85 | 1.94 | -19.85 | 0.32 | 0.37 | 744 | 91927.69 |
| recency_ml | TVA | 3.58 | 3.27 | -1.05 | -2.58 | 1.52 | -16.84 | 0.20 | 0.24 | 739 | 18562.62 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | ISNE | uri | 1.48 | -0.30 | -0.58 | -1.97 | 6 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| boosting_ratio | ISNE | uri | 3.19 | 1.36 | -0.40 | -2.37 | 6 |
| boosting_ratio | MISO | uri | 2.93 | -2.56 | -2.82 | -6.40 | 5 |
| boosting_ratio | PJM | uri | 2.05 | -1.41 | -2.04 | -4.03 | 6 |
| boosting_ratio | TVA | uri | 4.70 | -3.36 | -4.53 | -9.47 | 6 |
| ens_hourly | ISNE | uri | 2.79 | 1.29 | -0.41 | -2.28 | 6 |
| ens_hourly | MISO | uri | 3.35 | -3.08 | -3.19 | -6.26 | 5 |
| ens_hourly | PJM | uri | 2.22 | 0.41 | -0.71 | -3.29 | 6 |
| ens_hourly | TVA | uri | 2.70 | -1.12 | -1.74 | -3.38 | 6 |
| ens_ratio | ISNE | uri | 2.71 | 1.45 | -0.19 | -0.59 | 6 |
| ens_ratio | MISO | uri | 3.18 | -2.43 | -2.73 | -5.84 | 5 |
| ens_ratio | PJM | uri | 2.20 | 0.36 | -0.86 | -3.13 | 6 |
| ens_ratio | TVA | uri | 3.67 | -1.72 | -2.86 | -5.58 | 6 |
| ens_three | ISNE | uri | 2.50 | 0.38 | -0.56 | -2.72 | 6 |
| ens_three | MISO | uri | 3.98 | -3.94 | -3.94 | -7.27 | 5 |
| ens_three | PJM | uri | 2.32 | 0.71 | -0.71 | -3.60 | 6 |
| ens_three | TVA | uri | 2.97 | -0.93 | -1.77 | -3.40 | 6 |
| final2 | ISNE | uri | 2.76 | 2.18 | -0.15 | -0.87 | 6 |
| final2 | MISO | uri | 3.44 | -2.39 | -2.82 | -5.84 | 5 |
| final2 | PJM | uri | 1.86 | 0.07 | -0.65 | -2.07 | 6 |
| final2 | TVA | uri | 3.04 | -1.89 | -2.67 | -5.67 | 6 |
| final2_hourly | ISNE | uri | 2.73 | 2.13 | -0.18 | -1.07 | 6 |
| final2_hourly | MISO | uri | 3.43 | -2.34 | -2.83 | -5.82 | 5 |
| final2_hourly | PJM | uri | 1.85 | 0.01 | -0.62 | -2.08 | 6 |
| final2_hourly | TVA | uri | 3.03 | -1.91 | -2.70 | -5.69 | 6 |
| final2_nn30 | ISNE | uri | 2.74 | 2.20 | -0.14 | -0.84 | 6 |
| final2_nn30 | MISO | uri | 3.48 | -2.47 | -2.80 | -5.84 | 5 |
| final2_nn30 | PJM | uri | 1.88 | -0.07 | -0.70 | -2.27 | 6 |
| final2_nn30 | TVA | uri | 3.02 | -1.78 | -2.59 | -5.32 | 6 |
| final2_nn50 | ISNE | uri | 2.83 | 2.34 | -0.15 | -0.88 | 6 |
| final2_nn50 | MISO | uri | 3.44 | -2.52 | -2.86 | -5.93 | 5 |
| final2_nn50 | PJM | uri | 1.86 | 0.08 | -0.63 | -2.27 | 6 |
| final2_nn50 | TVA | uri | 3.08 | -2.02 | -2.80 | -5.47 | 6 |
| final2_ratio | ISNE | uri | 2.62 | 2.02 | -0.03 | -0.21 | 6 |
| final2_ratio | MISO | uri | 3.10 | -1.16 | -2.07 | -4.87 | 5 |
| final2_ratio | PJM | uri | 1.87 | -0.06 | -0.77 | -2.67 | 6 |
| final2_ratio | TVA | uri | 4.23 | -2.24 | -3.65 | -7.49 | 6 |
| final2_three | ISNE | uri | 2.61 | 1.78 | -0.13 | -0.76 | 6 |
| final2_three | MISO | uri | 4.05 | -3.32 | -3.55 | -7.08 | 5 |
| final2_three | PJM | uri | 1.99 | -0.05 | -0.78 | -2.89 | 6 |
| final2_three | TVA | uri | 3.44 | -2.08 | -3.01 | -5.89 | 6 |
| final_additive | ISNE | uri | 2.56 | 1.52 | -0.29 | -1.49 | 6 |
| final_additive | MISO | uri | 3.53 | -2.28 | -2.76 | -5.27 | 5 |
| final_additive | PJM | uri | 2.94 | 2.28 | -0.43 | -2.57 | 6 |
| final_additive | TVA | uri | 3.33 | 0.03 | -1.21 | -3.04 | 6 |
| final_boosting | ISNE | uri | 3.32 | 1.07 | -0.73 | -3.06 | 6 |
| final_boosting | MISO | uri | 3.37 | -4.08 | -4.08 | -7.61 | 5 |
| final_boosting | PJM | uri | 1.98 | -1.08 | -1.17 | -3.87 | 6 |
| final_boosting | TVA | uri | 2.71 | -2.16 | -2.67 | -5.05 | 6 |
| final_ensemble | ISNE | uri | 2.81 | 1.32 | -0.38 | -2.20 | 6 |
| final_ensemble | MISO | uri | 3.36 | -3.15 | -3.24 | -6.36 | 5 |
| final_ensemble | PJM | uri | 2.22 | 0.48 | -0.69 | -3.28 | 6 |
| final_ensemble | TVA | uri | 2.71 | -1.06 | -1.72 | -3.36 | 6 |
| recency_ml | ISNE | uri | 3.52 | -1.97 | -1.97 | -4.02 | 6 |
| recency_ml | MISO | uri | 6.72 | -5.90 | -5.90 | -9.40 | 5 |
| recency_ml | PJM | uri | 2.77 | 1.24 | -0.74 | -4.36 | 6 |
| recency_ml | TVA | uri | 3.79 | -0.67 | -1.87 | -3.87 | 6 |
| DF | ISNE | elliott | 3.18 | 3.19 | 0.00 | 0.00 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| boosting_ratio | ISNE | elliott | 3.50 | 2.91 | -0.27 | -1.35 | 5 |
| boosting_ratio | MISO | elliott | 4.18 | -1.29 | -2.55 | -5.39 | 5 |
| boosting_ratio | PJM | elliott | 5.89 | -2.68 | -4.19 | -11.43 | 5 |
| boosting_ratio | TVA | elliott | 11.08 | 10.45 | 0.00 | 0.00 | 3 |
| ens_hourly | ISNE | elliott | 3.40 | 2.15 | -0.43 | -1.24 | 5 |
| ens_hourly | MISO | elliott | 3.45 | -2.05 | -2.83 | -4.91 | 5 |
| ens_hourly | PJM | elliott | 4.24 | -1.95 | -2.88 | -6.29 | 5 |
| ens_hourly | TVA | elliott | 6.81 | 2.92 | -0.40 | -0.76 | 3 |
| ens_ratio | ISNE | elliott | 3.40 | 2.36 | -0.43 | -1.13 | 5 |
| ens_ratio | MISO | elliott | 3.60 | -2.11 | -2.98 | -4.76 | 5 |
| ens_ratio | PJM | elliott | 4.52 | -2.32 | -3.34 | -8.72 | 5 |
| ens_ratio | TVA | elliott | 9.40 | 7.91 | 0.00 | 0.00 | 3 |
| ens_three | ISNE | elliott | 3.42 | 2.55 | -0.56 | -1.72 | 5 |
| ens_three | MISO | elliott | 3.51 | -2.89 | -3.45 | -6.43 | 5 |
| ens_three | PJM | elliott | 4.59 | -4.24 | -4.63 | -10.18 | 5 |
| ens_three | TVA | elliott | 6.02 | 2.93 | -1.03 | -1.64 | 3 |
| final2 | ISNE | elliott | 3.51 | 1.63 | -0.72 | -2.23 | 5 |
| final2 | MISO | elliott | 3.42 | -1.58 | -2.69 | -4.10 | 5 |
| final2 | PJM | elliott | 4.26 | -2.70 | -3.11 | -6.29 | 5 |
| final2 | TVA | elliott | 6.70 | 4.69 | 0.00 | 0.00 | 3 |
| final2_hourly | ISNE | elliott | 3.49 | 1.77 | -0.69 | -2.23 | 5 |
| final2_hourly | MISO | elliott | 3.44 | -1.75 | -2.72 | -4.03 | 5 |
| final2_hourly | PJM | elliott | 4.22 | -2.91 | -3.25 | -6.23 | 5 |
| final2_hourly | TVA | elliott | 6.66 | 4.67 | 0.00 | 0.00 | 3 |
| final2_nn30 | ISNE | elliott | 3.55 | 1.77 | -0.63 | -1.87 | 5 |
| final2_nn30 | MISO | elliott | 3.43 | -1.58 | -2.73 | -4.20 | 5 |
| final2_nn30 | PJM | elliott | 4.32 | -2.87 | -3.16 | -6.39 | 5 |
| final2_nn30 | TVA | elliott | 6.79 | 4.59 | 0.00 | 0.00 | 3 |
| final2_nn50 | ISNE | elliott | 3.56 | 1.72 | -0.67 | -2.16 | 5 |
| final2_nn50 | MISO | elliott | 3.44 | -1.45 | -2.57 | -4.04 | 5 |
| final2_nn50 | PJM | elliott | 4.25 | -2.61 | -3.12 | -6.29 | 5 |
| final2_nn50 | TVA | elliott | 6.69 | 4.72 | 0.00 | 0.00 | 3 |
| final2_ratio | ISNE | elliott | 3.53 | 1.94 | -0.70 | -1.84 | 5 |
| final2_ratio | MISO | elliott | 3.64 | -1.86 | -2.90 | -4.83 | 5 |
| final2_ratio | PJM | elliott | 4.63 | -2.84 | -3.63 | -8.43 | 5 |
| final2_ratio | TVA | elliott | 9.63 | 9.71 | 0.00 | 0.00 | 3 |
| final2_three | ISNE | elliott | 3.41 | 2.41 | -0.68 | -2.24 | 5 |
| final2_three | MISO | elliott | 3.63 | -2.61 | -3.39 | -6.72 | 5 |
| final2_three | PJM | elliott | 4.85 | -5.06 | -5.21 | -11.39 | 5 |
| final2_three | TVA | elliott | 5.82 | 4.86 | 0.00 | 0.00 | 3 |
| final_additive | ISNE | elliott | 3.99 | 1.75 | -0.62 | -2.38 | 5 |
| final_additive | MISO | elliott | 3.43 | -3.19 | -3.55 | -6.50 | 5 |
| final_additive | PJM | elliott | 3.70 | -2.01 | -2.64 | -6.50 | 5 |
| final_additive | TVA | elliott | 7.91 | 5.47 | 0.00 | 0.00 | 3 |
| final_boosting | ISNE | elliott | 3.32 | 2.41 | -0.31 | -1.57 | 5 |
| final_boosting | MISO | elliott | 3.89 | -0.76 | -2.13 | -3.77 | 5 |
| final_boosting | PJM | elliott | 5.20 | -1.79 | -3.00 | -5.99 | 5 |
| final_boosting | TVA | elliott | 6.08 | 0.38 | -1.37 | -3.14 | 3 |
| final_ensemble | ISNE | elliott | 3.39 | 2.09 | -0.44 | -1.16 | 5 |
| final_ensemble | MISO | elliott | 3.44 | -1.88 | -2.79 | -4.45 | 5 |
| final_ensemble | PJM | elliott | 4.29 | -1.90 | -2.80 | -6.26 | 5 |
| final_ensemble | TVA | elliott | 6.82 | 2.96 | -0.31 | -0.54 | 3 |
| recency_ml | ISNE | elliott | 4.47 | 3.82 | -0.89 | -3.30 | 5 |
| recency_ml | MISO | elliott | 5.29 | -5.58 | -5.72 | -14.05 | 5 |
| recency_ml | PJM | elliott | 6.47 | -8.60 | -8.71 | -19.85 | 5 |
| recency_ml | TVA | elliott | 4.94 | 2.83 | -2.44 | -4.15 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | DF | eve | 3.33 | 1.59 | -0.74 |  | 98 |
| 19 | ens_three | eve | 3.45 | 0.60 | -1.56 | 0.43 | 98 |
| 17 | ens_hourly | eve | 3.50 | 1.14 | -1.32 | 0.42 | 98 |
| 28 | final_ensemble | eve | 3.51 | 1.15 | -1.33 | 0.41 | 98 |
| 25 | final2_three | eve | 3.56 | 1.50 | -1.35 | 0.45 | 98 |
| 21 | final2_hourly | eve | 3.57 | 1.92 | -1.15 | 0.43 | 98 |
| 20 | final2 | eve | 3.57 | 1.93 | -1.16 | 0.43 | 98 |
| 23 | final2_nn50 | eve | 3.57 | 1.95 | -1.15 | 0.42 | 98 |
| 18 | ens_ratio | eve | 3.58 | 1.26 | -1.26 | 0.48 | 98 |
| 22 | final2_nn30 | eve | 3.59 | 1.92 | -1.15 | 0.45 | 98 |
| 26 | final_additive | eve | 3.59 | 0.85 | -1.53 | 0.43 | 98 |
| 24 | final2_ratio | eve | 3.64 | 2.12 | -1.09 | 0.45 | 98 |
| 27 | final_boosting | eve | 3.90 | 1.47 | -1.26 | 0.39 | 98 |
| 16 | boosting_ratio | eve | 4.08 | 1.66 | -1.21 | 0.38 | 98 |
| 29 | recency_ml | eve | 4.18 | -0.67 | -2.44 | 0.33 | 98 |
| 0 | DF | special | 3.24 | 0.75 | -0.99 |  | 99 |
| 7 | final2_nn30 | special | 3.39 | -0.30 | -1.96 | 0.44 | 99 |
| 6 | final2_hourly | special | 3.39 | -0.32 | -1.99 | 0.43 | 99 |
| 5 | final2 | special | 3.40 | -0.32 | -1.99 | 0.42 | 99 |
| 2 | ens_hourly | special | 3.40 | -1.11 | -2.34 | 0.43 | 99 |
| 8 | final2_nn50 | special | 3.41 | -0.29 | -1.99 | 0.42 | 99 |
| 13 | final_ensemble | special | 3.41 | -1.10 | -2.34 | 0.44 | 99 |
| 9 | final2_ratio | special | 3.42 | -0.29 | -1.98 | 0.42 | 99 |
| 11 | final_additive | special | 3.44 | -1.45 | -2.58 | 0.48 | 99 |
| 4 | ens_three | special | 3.45 | -1.27 | -2.53 | 0.44 | 99 |
| 10 | final2_three | special | 3.46 | -0.39 | -2.07 | 0.43 | 99 |
| 3 | ens_ratio | special | 3.51 | -1.14 | -2.40 | 0.46 | 99 |
| 12 | final_boosting | special | 3.92 | -0.74 | -2.28 | 0.32 | 99 |
| 1 | boosting_ratio | special | 4.10 | -0.88 | -2.46 | 0.35 | 99 |
| 14 | recency_ml | special | 4.29 | -1.70 | -3.22 | 0.30 | 99 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.382 | 1.361 | 0.391 | 0.890 | 11.667 | 0.892 | 2896 |
| final2_hourly | all | 0.382 | 1.358 | 0.391 | 0.890 | 11.654 | 0.893 | 2896 |
| final2_nn30 | all | 0.387 | 1.367 | 0.394 | 0.886 | 11.646 | 0.889 | 2896 |
| final2_nn50 | all | 0.380 | 1.360 | 0.391 | 0.892 | 11.710 | 0.894 | 2896 |
| final2_ratio | all | 0.388 | 1.376 | 0.389 | 0.890 | 11.716 | 0.895 | 2896 |
| final2_three | all | 0.377 | 1.351 | 0.391 | 0.889 | 11.521 | 0.895 | 2896 |
| final2 | events | 0.487 | 1.697 | 0.538 | 0.801 | 12.329 | 0.805 | 41 |
| final2_hourly | events | 0.489 | 1.690 | 0.534 | 0.808 | 12.293 | 0.780 | 41 |
| final2_nn30 | events | 0.482 | 1.708 | 0.533 | 0.814 | 12.755 | 0.829 | 41 |
| final2_nn50 | events | 0.481 | 1.709 | 0.567 | 0.795 | 12.167 | 0.805 | 41 |
| final2_ratio | events | 0.619 | 1.899 | 0.527 | 0.782 | 11.957 | 0.756 | 41 |
| final2_three | events | 0.444 | 1.772 | 0.736 | 0.780 | 12.261 | 0.756 | 41 |
| final2 | cold_mornings | 0.453 | 1.485 | 0.475 | 0.852 | 11.996 | 0.833 | 120 |
| final2_hourly | cold_mornings | 0.452 | 1.483 | 0.471 | 0.856 | 11.975 | 0.833 | 120 |
| final2_nn30 | cold_mornings | 0.460 | 1.486 | 0.485 | 0.853 | 12.241 | 0.833 | 120 |
| final2_nn50 | cold_mornings | 0.443 | 1.476 | 0.479 | 0.848 | 11.837 | 0.817 | 120 |
| final2_ratio | cold_mornings | 0.505 | 1.544 | 0.464 | 0.849 | 11.950 | 0.800 | 120 |
| final2_three | cold_mornings | 0.434 | 1.494 | 0.542 | 0.848 | 11.963 | 0.808 | 120 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 12419 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 12407 | MISO | 2021-02-16 | boosting_ratio | 1.35 | -1.49 | -1.49 |
| 12410 | MISO | 2021-02-16 | ens_hourly | 2.19 | 1.54 | 0.00 |
| 12412 | MISO | 2021-02-16 | ens_ratio | 1.73 | 0.20 | 0.00 |
| 12411 | MISO | 2021-02-16 | ens_three | 1.67 | 0.50 | 0.00 |
| 12413 | MISO | 2021-02-16 | final2 | 2.57 | 2.89 | 0.00 |
| 12414 | MISO | 2021-02-16 | final2_hourly | 2.55 | 3.00 | 0.00 |
| 12417 | MISO | 2021-02-16 | final2_nn30 | 2.42 | 2.69 | 0.00 |
| 12418 | MISO | 2021-02-16 | final2_nn50 | 2.40 | 2.77 | 0.00 |
| 12416 | MISO | 2021-02-16 | final2_ratio | 2.46 | 2.13 | 0.00 |
| 12415 | MISO | 2021-02-16 | final2_three | 1.88 | 2.37 | 0.00 |
| 12405 | MISO | 2021-02-16 | final_additive | 2.38 | 1.99 | 0.00 |
| 12406 | MISO | 2021-02-16 | final_boosting | 2.11 | 0.99 | 0.00 |
| 12409 | MISO | 2021-02-16 | final_ensemble | 2.17 | 1.51 | 0.00 |
| 12408 | MISO | 2021-02-16 | recency_ml | 3.61 | -2.07 | -2.07 |
| 44639 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 44627 | TVA | 2022-12-23 | boosting_ratio | 13.51 | -16.88 | -16.88 |
| 44630 | TVA | 2022-12-23 | ens_hourly | 9.59 | -10.09 | -10.09 |
| 44632 | TVA | 2022-12-23 | ens_ratio | 9.54 | -11.02 | -11.02 |
| 44631 | TVA | 2022-12-23 | ens_three | 8.36 | -10.13 | -10.13 |
| 44633 | TVA | 2022-12-23 | final2 | 10.26 | -11.56 | -11.56 |
| 44634 | TVA | 2022-12-23 | final2_hourly | 10.30 | -11.56 | -11.56 |
| 44637 | TVA | 2022-12-23 | final2_nn30 | 9.94 | -11.25 | -11.25 |
| 44638 | TVA | 2022-12-23 | final2_nn50 | 10.29 | -11.61 | -11.61 |
| 44636 | TVA | 2022-12-23 | final2_ratio | 9.90 | -12.17 | -12.17 |
| 44635 | TVA | 2022-12-23 | final2_three | 8.86 | -11.81 | -11.81 |
| 44625 | TVA | 2022-12-23 | final_additive | 6.61 | -5.25 | -5.25 |
| 44626 | TVA | 2022-12-23 | final_boosting | 13.98 | -15.00 | -15.00 |
| 44629 | TVA | 2022-12-23 | final_ensemble | 9.54 | -10.08 | -10.08 |
| 44628 | TVA | 2022-12-23 | recency_ml | 11.83 | -10.22 | -10.22 |
| 44654 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 44642 | TVA | 2022-12-24 | boosting_ratio | 5.92 | -15.66 | -15.66 |
| 44645 | TVA | 2022-12-24 | ens_hourly | 4.68 | -10.60 | -10.60 |
| 44647 | TVA | 2022-12-24 | ens_ratio | 4.53 | -12.13 | -12.13 |
| 44646 | TVA | 2022-12-24 | ens_three | 5.34 | -10.90 | -10.90 |
| 44648 | TVA | 2022-12-24 | final2 | 4.45 | -11.23 | -11.23 |
| 44649 | TVA | 2022-12-24 | final2_hourly | 4.45 | -11.15 | -11.15 |
| 44652 | TVA | 2022-12-24 | final2_nn30 | 4.25 | -11.23 | -11.23 |
| 44653 | TVA | 2022-12-24 | final2_nn50 | 4.54 | -11.29 | -11.29 |
| 44651 | TVA | 2022-12-24 | final2_ratio | 4.18 | -13.29 | -13.29 |
| 44650 | TVA | 2022-12-24 | final2_three | 5.12 | -10.46 | -10.46 |
| 44640 | TVA | 2022-12-24 | final_additive | 3.65 | -8.48 | -8.48 |
| 44641 | TVA | 2022-12-24 | final_boosting | 6.04 | -12.78 | -12.78 |
| 44644 | TVA | 2022-12-24 | final_ensemble | 4.68 | -10.66 | -10.66 |
| 44643 | TVA | 2022-12-24 | recency_ml | 7.21 | -11.36 | -11.36 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| boosting_ratio | ISNE | mape | 19.017 | 0.000 | 752 |
| boosting_ratio | MISO | mape | -3.785 | 0.000 | 746 |
| boosting_ratio | PJM | mape | 7.508 | 0.000 | 744 |
| boosting_ratio | TVA | mape | 16.651 | 0.000 | 739 |
| ens_hourly | ISNE | mape | 17.242 | 0.000 | 752 |
| ens_hourly | MISO | mape | -6.211 | 0.000 | 746 |
| ens_hourly | PJM | mape | 2.510 | 0.012 | 744 |
| ens_hourly | TVA | mape | 14.640 | 0.000 | 739 |
| ens_ratio | ISNE | mape | 17.362 | 0.000 | 752 |
| ens_ratio | MISO | mape | -6.126 | 0.000 | 746 |
| ens_ratio | PJM | mape | 3.382 | 0.001 | 744 |
| ens_ratio | TVA | mape | 14.950 | 0.000 | 739 |
| ens_three | ISNE | mape | 19.301 | 0.000 | 752 |
| ens_three | MISO | mape | -5.746 | 0.000 | 746 |
| ens_three | PJM | mape | 2.281 | 0.023 | 744 |
| ens_three | TVA | mape | 14.569 | 0.000 | 739 |
| final2 | ISNE | mape | 15.636 | 0.000 | 752 |
| final2 | MISO | mape | -8.862 | 0.000 | 746 |
| final2 | PJM | mape | -3.041 | 0.002 | 744 |
| final2 | TVA | mape | 13.923 | 0.000 | 739 |
| final2_hourly | ISNE | mape | 15.515 | 0.000 | 752 |
| final2_hourly | MISO | mape | -8.923 | 0.000 | 746 |
| final2_hourly | PJM | mape | -3.118 | 0.002 | 744 |
| final2_hourly | TVA | mape | 13.858 | 0.000 | 739 |
| final2_nn30 | ISNE | mape | 15.768 | 0.000 | 752 |
| final2_nn30 | MISO | mape | -8.862 | 0.000 | 746 |
| final2_nn30 | PJM | mape | -2.925 | 0.003 | 744 |
| final2_nn30 | TVA | mape | 14.117 | 0.000 | 739 |
| final2_nn50 | ISNE | mape | 15.710 | 0.000 | 752 |
| final2_nn50 | MISO | mape | -9.041 | 0.000 | 746 |
| final2_nn50 | PJM | mape | -2.918 | 0.004 | 744 |
| final2_nn50 | TVA | mape | 13.943 | 0.000 | 739 |
| final2_ratio | ISNE | mape | 15.794 | 0.000 | 752 |
| final2_ratio | MISO | mape | -8.700 | 0.000 | 746 |
| final2_ratio | PJM | mape | -2.046 | 0.041 | 744 |
| final2_ratio | TVA | mape | 14.024 | 0.000 | 739 |
| final2_three | ISNE | mape | 15.645 | 0.000 | 752 |
| final2_three | MISO | mape | -9.285 | 0.000 | 746 |
| final2_three | PJM | mape | -3.577 | 0.000 | 744 |
| final2_three | TVA | mape | 13.397 | 0.000 | 739 |
| final_additive | ISNE | mape | 21.098 | 0.000 | 752 |
| final_additive | MISO | mape | -2.885 | 0.004 | 746 |
| final_additive | PJM | mape | 5.999 | 0.000 | 744 |
| final_additive | TVA | mape | 17.307 | 0.000 | 739 |
| final_boosting | ISNE | mape | 19.009 | 0.000 | 752 |
| final_boosting | MISO | mape | -3.438 | 0.001 | 746 |
| final_boosting | PJM | mape | 6.357 | 0.000 | 744 |
| final_boosting | TVA | mape | 16.453 | 0.000 | 739 |
| final_ensemble | ISNE | mape | 17.396 | 0.000 | 752 |
| final_ensemble | MISO | mape | -6.116 | 0.000 | 746 |
| final_ensemble | PJM | mape | 2.785 | 0.005 | 744 |
| final_ensemble | TVA | mape | 14.766 | 0.000 | 739 |
| recency_ml | ISNE | mape | 36.416 | 0.000 | 752 |
| recency_ml | MISO | mape | 3.503 | 0.000 | 746 |
| recency_ml | PJM | mape | 10.791 | 0.000 | 744 |
| recency_ml | TVA | mape | 20.636 | 0.000 | 739 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.996 |
| boosting_ratio | 0.991 |
| ens_hourly | 0.992 |
| ens_ratio | 0.991 |
| ens_three | 0.992 |
| final2 | 0.992 |
| final2_hourly | 0.992 |
| final2_nn30 | 0.992 |
| final2_nn50 | 0.992 |
| final2_ratio | 0.991 |
| final2_three | 0.992 |
| final_additive | 0.982 |
| final_boosting | 0.992 |
| final_ensemble | 0.992 |
| recency_ml | 0.992 |
