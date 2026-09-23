# Frozen evaluation: the recipe on days the development never saw

Development BAs: BPAT, CISO, DUK, ERCO, FPL, ISNE, MISO, NYIS, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. The recipe settled at the end of phase F (`final2`: additive model with special days and, at ISO-NE and CAISO, the PV terms; boosting with the sky features there; ensemble by recent error; median correction and 90 % band from the 40 known days of the same regime nearest in forecast minimum temperature, adaptive level per regime; point at the 60th percentile around the forecast peak), run once on 2023 to 2025 without any change after seeing these days. The models keep learning day by day from the six years before each day, as in operation.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | 2.52 | 2.18 | 0.06 | -1.37 | 1.28 | 0.62 | 0.36 | -80.50 | 10470 | 11.00 |
| final_ensemble | 2.84 | 2.50 | -1.06 | -2.09 | 1.27 | 0.57 | 0.29 | -81.45 | 10470 | 11.00 |
| final_boosting | 3.01 | 2.68 | -1.00 | -2.12 | 1.45 | 0.53 | 0.29 | -81.17 | 10470 | 11.00 |
| final_additive | 3.04 | 2.66 | -1.14 | -2.25 | 1.34 | 0.53 | 0.29 | -81.79 | 10470 | 11.00 |
| DF | 3.22 | 2.90 | -0.08 | -1.31 | 1.17 | 0.00 | 0.00 | -100 | 10470 | 11.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | 2.01 | 1.81 | -0.41 | -1.23 | 1.16 | -15.51 |  |  | 961 | 6748.98 |
| DF | CISO | 6.73 | 6.57 | -2.18 | -2.67 | 1.53 | -27.07 |  |  | 949 | 25296.41 |
| DF | DUK | 2.66 | 2.33 | 0.52 | -1.22 | 1.03 | -12.31 |  |  | 957 | 12333.89 |
| DF | ERCO | 2.39 | 2.01 | 0.72 | -0.84 | 1.05 | -11.36 |  |  | 961 | 53116.45 |
| DF | FPL | 3.27 | 3.10 | -0.87 | -2.02 | 1.15 | -81.63 |  |  | 918 | 16637.50 |
| DF | ISNE | 2.55 | 2.50 | 0.40 | -0.47 | 0.35 | -5.42 |  |  | 954 | 13025.41 |
| DF | MISO | 2.73 | 2.55 | 2.04 | -0.23 | 0.88 | -6.54 |  |  | 962 | 74208.68 |
| DF | NYIS | 2.94 | 2.48 | -2.76 | -2.92 | 0.50 | -100 |  |  | 949 | 17167.35 |
| DF | PJM | 3.53 | 3.39 | -1.43 | -1.80 | 1.57 | -8.93 |  |  | 949 | 93125.11 |
| DF | SWPP | 3.43 | 2.19 | 0.38 | -1.48 | 1.38 | -17.10 |  |  | 952 | 33085.55 |
| DF | TVA | 2.29 | 1.98 | 0.48 | -0.93 | 1.02 | -8.44 |  |  | 958 | 18844.36 |
| final2 | BPAT | 2.37 | 2.09 | -0.04 | -1.27 | 1.38 | -17.46 | 0.40 | 0.40 | 961 | 6748.98 |
| final2 | CISO | 2.81 | 2.63 | -0.25 | -1.53 | 0.97 | -15.58 | 0.97 | 0.58 | 949 | 25296.41 |
| final2 | DUK | 3.42 | 2.86 | 0.32 | -1.93 | 1.36 | -15.38 | 0.34 | 0.25 | 957 | 12333.89 |
| final2 | ERCO | 2.55 | 2.16 | -0.11 | -1.53 | 1.03 | -16.13 | 0.44 | 0.22 | 961 | 53116.45 |
| final2 | FPL | 3.57 | 3.08 | 0.20 | -2.03 | 1.15 | -80.50 | 0.52 | 0.39 | 918 | 16637.50 |
| final2 | ISNE | 3.85 | 3.35 | 0.46 | -1.28 | 0.53 | -23.75 | 0.29 | 0.21 | 954 | 13025.41 |
| final2 | MISO | 1.91 | 1.71 | 0.10 | -1.01 | 1.51 | -8.60 | 0.68 | 0.08 | 962 | 74208.68 |
| final2 | NYIS | 2.87 | 2.46 | 0.16 | -1.29 | 0.68 | -13.68 | 0.47 | 0.72 | 949 | 17167.35 |
| final2 | PJM | 2.28 | 1.95 | 0.17 | -1.24 | 1.36 | -10.63 | 0.84 | 0.57 | 949 | 93125.11 |
| final2 | SWPP | 2.54 | 2.06 | -0.16 | -1.45 | 1.71 | -24.23 | 0.53 | 0.37 | 952 | 33085.55 |
| final2 | TVA | 2.94 | 2.53 | 0.02 | -1.74 | 1.40 | -14.17 | 0.32 | 0.24 | 958 | 18844.36 |
| final_additive | BPAT | 2.62 | 2.30 | -1.75 | -2.34 | 1.55 | -16.77 | 0.33 | 0.26 | 961 | 6748.98 |
| final_additive | CISO | 4.13 | 3.74 | -2.46 | -3.46 | 1.05 | -23.32 | 0.87 | 0.43 | 949 | 25296.41 |
| final_additive | DUK | 3.65 | 3.06 | -0.80 | -2.64 | 1.38 | -17.49 | 0.32 | 0.20 | 957 | 12333.89 |
| final_additive | ERCO | 3.26 | 2.88 | -1.94 | -2.69 | 1.01 | -18.91 | 0.30 | 0.12 | 961 | 53116.45 |
| final_additive | FPL | 5.06 | 4.68 | -5.03 | -5.63 | 0.99 | -81.79 | 0.28 | 0.10 | 918 | 16637.50 |
| final_additive | ISNE | 4.38 | 3.79 | -0.75 | -2.37 | 0.61 | -22.92 | 0.22 | 0.16 | 954 | 13025.41 |
| final_additive | MISO | 2.35 | 2.09 | -1.01 | -1.76 | 1.74 | -10.32 | 0.57 | 0.05 | 962 | 74208.68 |
| final_additive | NYIS | 3.15 | 2.73 | -0.95 | -2.09 | 0.65 | -17.53 | 0.44 | 0.62 | 949 | 17167.35 |
| final_additive | PJM | 2.61 | 2.27 | -0.32 | -1.63 | 1.44 | -12.48 | 0.76 | 0.52 | 949 | 93125.11 |
| final_additive | SWPP | 2.71 | 2.19 | -0.67 | -1.94 | 1.70 | -23.04 | 0.50 | 0.32 | 952 | 33085.55 |
| final_additive | TVA | 3.30 | 2.80 | 0.52 | -1.68 | 1.30 | -16.29 | 0.27 | 0.25 | 958 | 18844.36 |
| final_boosting | BPAT | 2.64 | 2.33 | -0.79 | -1.83 | 1.50 | -17.90 | 0.34 | 0.33 | 961 | 6748.98 |
| final_boosting | CISO | 3.32 | 2.99 | -2.43 | -2.99 | 1.02 | -14.94 | 0.92 | 0.43 | 949 | 25296.41 |
| final_boosting | DUK | 3.64 | 3.12 | -0.94 | -2.64 | 1.47 | -17.08 | 0.31 | 0.21 | 957 | 12333.89 |
| final_boosting | ERCO | 2.95 | 2.63 | -1.64 | -2.46 | 1.14 | -16.33 | 0.33 | 0.14 | 961 | 53116.45 |
| final_boosting | FPL | 5.65 | 5.36 | -5.99 | -6.31 | 1.46 | -81.17 | 0.17 | 0.08 | 918 | 16637.50 |
| final_boosting | ISNE | 4.13 | 3.58 | -1.08 | -2.15 | 0.64 | -22.84 | 0.24 | 0.15 | 954 | 13025.41 |
| final_boosting | MISO | 2.22 | 2.07 | -0.53 | -1.43 | 1.70 | -8.98 | 0.62 | 0.07 | 962 | 74208.68 |
| final_boosting | NYIS | 3.12 | 2.69 | -0.92 | -1.89 | 0.79 | -14.61 | 0.42 | 0.63 | 949 | 17167.35 |
| final_boosting | PJM | 2.81 | 2.52 | -0.23 | -1.63 | 1.64 | -12.43 | 0.74 | 0.51 | 949 | 93125.11 |
| final_boosting | SWPP | 3.06 | 2.44 | -0.34 | -1.89 | 1.79 | -22.93 | 0.45 | 0.31 | 952 | 33085.55 |
| final_boosting | TVA | 3.34 | 2.89 | 0.21 | -1.82 | 1.50 | -16.13 | 0.24 | 0.23 | 958 | 18844.36 |
| final_ensemble | BPAT | 2.43 | 2.12 | -1.27 | -1.99 | 1.37 | -17.25 | 0.38 | 0.30 | 961 | 6748.98 |
| final_ensemble | CISO | 3.40 | 3.06 | -2.41 | -3.09 | 1.00 | -18.02 | 0.92 | 0.44 | 949 | 25296.41 |
| final_ensemble | DUK | 3.50 | 2.90 | -0.88 | -2.58 | 1.39 | -16.96 | 0.34 | 0.20 | 957 | 12333.89 |
| final_ensemble | ERCO | 2.95 | 2.59 | -1.77 | -2.50 | 0.96 | -16.97 | 0.34 | 0.13 | 961 | 53116.45 |
| final_ensemble | FPL | 5.07 | 4.69 | -5.46 | -5.82 | 1.11 | -81.45 | 0.26 | 0.08 | 918 | 16637.50 |
| final_ensemble | ISNE | 4.01 | 3.48 | -0.91 | -2.14 | 0.59 | -22.88 | 0.26 | 0.16 | 954 | 13025.41 |
| final_ensemble | MISO | 2.14 | 1.95 | -0.77 | -1.51 | 1.55 | -9.14 | 0.63 | 0.06 | 962 | 74208.68 |
| final_ensemble | NYIS | 2.92 | 2.58 | -0.91 | -1.87 | 0.65 | -15.55 | 0.46 | 0.64 | 949 | 17167.35 |
| final_ensemble | PJM | 2.53 | 2.24 | -0.27 | -1.53 | 1.38 | -11.41 | 0.79 | 0.54 | 949 | 93125.11 |
| final_ensemble | SWPP | 2.71 | 2.17 | -0.54 | -1.86 | 1.63 | -22.99 | 0.51 | 0.32 | 952 | 33085.55 |
| final_ensemble | TVA | 3.19 | 2.72 | 0.36 | -1.69 | 1.32 | -15.36 | 0.28 | 0.25 | 958 | 18844.36 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | BPAT | gerri_heather | 3.76 | 0.98 | -1.48 | -3.76 | 6 |
| DF | CISO | gerri_heather | 6.64 | -1.54 | -1.83 | -6.40 | 6 |
| DF | DUK | gerri_heather | 5.00 | -4.45 | -5.21 | -11.31 | 6 |
| DF | ERCO | gerri_heather | 4.26 | 1.90 | -1.57 | -9.43 | 6 |
| DF | FPL | gerri_heather | 2.78 | -1.70 | -1.70 | -3.46 | 6 |
| DF | ISNE | gerri_heather | 2.32 | 0.27 | -0.45 | -1.26 | 6 |
| DF | MISO | gerri_heather | 2.10 | -0.39 | -0.74 | -1.86 | 6 |
| DF | NYIS | gerri_heather | 3.41 | -2.81 | -2.81 | -3.64 | 5 |
| DF | PJM | gerri_heather | 3.73 | -2.95 | -2.95 | -6.72 | 6 |
| DF | SWPP | gerri_heather | 7.29 | -7.49 | -7.49 | -17.10 | 6 |
| DF | TVA | gerri_heather | 3.50 | 2.67 | -0.73 | -4.40 | 6 |
| final2 | BPAT | gerri_heather | 5.31 | -5.27 | -5.27 | -13.30 | 6 |
| final2 | CISO | gerri_heather | 3.29 | 1.71 | -0.11 | -0.33 | 6 |
| final2 | DUK | gerri_heather | 5.77 | -5.90 | -5.90 | -10.44 | 6 |
| final2 | ERCO | gerri_heather | 6.85 | -8.61 | -8.61 | -14.51 | 6 |
| final2 | FPL | gerri_heather | 5.16 | -4.75 | -5.79 | -10.66 | 6 |
| final2 | ISNE | gerri_heather | 4.01 | -0.10 | -1.28 | -4.74 | 6 |
| final2 | MISO | gerri_heather | 2.65 | -1.58 | -1.97 | -4.95 | 6 |
| final2 | NYIS | gerri_heather | 2.08 | 0.58 | -0.42 | -2.10 | 5 |
| final2 | PJM | gerri_heather | 2.71 | -0.64 | -1.45 | -3.63 | 6 |
| final2 | SWPP | gerri_heather | 5.32 | -5.10 | -5.10 | -12.96 | 6 |
| final2 | TVA | gerri_heather | 2.96 | -0.71 | -2.01 | -5.88 | 6 |
| final_additive | BPAT | gerri_heather | 6.00 | -5.74 | -6.16 | -16.77 | 6 |
| final_additive | CISO | gerri_heather | 3.51 | 1.66 | -0.70 | -3.68 | 6 |
| final_additive | DUK | gerri_heather | 6.19 | -7.11 | -7.15 | -15.60 | 6 |
| final_additive | ERCO | gerri_heather | 8.46 | -10.54 | -10.54 | -17.41 | 6 |
| final_additive | FPL | gerri_heather | 6.47 | -8.00 | -8.00 | -14.44 | 6 |
| final_additive | ISNE | gerri_heather | 4.29 | 0.71 | -1.50 | -5.35 | 6 |
| final_additive | MISO | gerri_heather | 2.51 | -1.56 | -1.73 | -3.85 | 6 |
| final_additive | NYIS | gerri_heather | 2.45 | -0.90 | -1.49 | -3.22 | 5 |
| final_additive | PJM | gerri_heather | 2.96 | 1.47 | -0.20 | -0.86 | 6 |
| final_additive | SWPP | gerri_heather | 7.14 | -7.50 | -7.50 | -17.67 | 6 |
| final_additive | TVA | gerri_heather | 3.69 | 1.63 | -1.13 | -6.77 | 6 |
| final_boosting | BPAT | gerri_heather | 5.60 | -6.79 | -6.79 | -12.34 | 6 |
| final_boosting | CISO | gerri_heather | 3.87 | 2.43 | -0.32 | -1.90 | 6 |
| final_boosting | DUK | gerri_heather | 5.75 | -6.31 | -6.46 | -10.78 | 6 |
| final_boosting | ERCO | gerri_heather | 5.53 | -7.55 | -7.55 | -10.72 | 6 |
| final_boosting | FPL | gerri_heather | 5.51 | -7.18 | -7.51 | -13.51 | 6 |
| final_boosting | ISNE | gerri_heather | 4.05 | 0.24 | -0.73 | -3.98 | 6 |
| final_boosting | MISO | gerri_heather | 2.41 | -1.53 | -2.47 | -6.72 | 6 |
| final_boosting | NYIS | gerri_heather | 2.90 | 1.82 | -0.22 | -1.12 | 5 |
| final_boosting | PJM | gerri_heather | 2.44 | 0.19 | -1.03 | -3.13 | 6 |
| final_boosting | SWPP | gerri_heather | 6.01 | -7.00 | -7.00 | -12.41 | 6 |
| final_boosting | TVA | gerri_heather | 3.88 | -0.34 | -2.75 | -9.28 | 6 |
| final_ensemble | BPAT | gerri_heather | 5.54 | -6.31 | -6.31 | -14.38 | 6 |
| final_ensemble | CISO | gerri_heather | 3.56 | 2.06 | -0.50 | -2.76 | 6 |
| final_ensemble | DUK | gerri_heather | 5.82 | -6.72 | -6.81 | -13.22 | 6 |
| final_ensemble | ERCO | gerri_heather | 6.73 | -8.93 | -8.93 | -13.78 | 6 |
| final_ensemble | FPL | gerri_heather | 5.75 | -7.61 | -7.61 | -14.00 | 6 |
| final_ensemble | ISNE | gerri_heather | 4.00 | 0.46 | -1.06 | -4.63 | 6 |
| final_ensemble | MISO | gerri_heather | 2.41 | -1.55 | -2.03 | -5.29 | 6 |
| final_ensemble | NYIS | gerri_heather | 2.04 | 0.57 | -0.41 | -2.07 | 5 |
| final_ensemble | PJM | gerri_heather | 2.55 | 0.86 | -0.49 | -1.92 | 6 |
| final_ensemble | SWPP | gerri_heather | 6.53 | -7.26 | -7.26 | -15.00 | 6 |
| final_ensemble | TVA | gerri_heather | 3.13 | 0.65 | -1.56 | -5.28 | 6 |
| DF | BPAT | january_2025 | 2.46 | -0.63 | -1.13 | -5.68 | 6 |
| DF | CISO | january_2025 | 8.21 | -8.80 | -8.80 | -15.84 | 6 |
| DF | DUK | january_2025 | 2.29 | 0.13 | -1.20 | -6.77 | 6 |
| DF | ERCO | january_2025 | 3.99 | 0.33 | -0.83 | -2.52 | 6 |
| DF | FPL | january_2025 | 4.15 | -4.56 | -4.87 | -9.44 | 6 |
| DF | ISNE | january_2025 | 1.25 | 0.43 | -0.01 | -0.05 | 6 |
| DF | MISO | january_2025 | 2.93 | -1.38 | -2.02 | -4.75 | 6 |
| DF | NYIS | january_2025 | 3.90 | -3.63 | -3.63 | -4.31 | 5 |
| DF | PJM | january_2025 | 3.77 | -3.60 | -3.62 | -7.09 | 6 |
| DF | SWPP | january_2025 | 2.27 | -2.57 | -2.57 | -4.02 | 6 |
| DF | TVA | january_2025 | 2.96 | 1.69 | -0.29 | -1.52 | 6 |
| final2 | BPAT | january_2025 | 2.92 | -3.39 | -3.86 | -5.47 | 6 |
| final2 | CISO | january_2025 | 2.07 | -0.07 | -0.93 | -3.29 | 6 |
| final2 | DUK | january_2025 | 4.67 | -0.64 | -1.99 | -7.14 | 6 |
| final2 | ERCO | january_2025 | 3.23 | -4.73 | -4.73 | -8.11 | 6 |
| final2 | FPL | january_2025 | 5.13 | -5.88 | -5.88 | -11.89 | 6 |
| final2 | ISNE | january_2025 | 3.81 | -0.92 | -1.54 | -3.06 | 6 |
| final2 | MISO | january_2025 | 2.66 | -2.86 | -2.86 | -4.40 | 6 |
| final2 | NYIS | january_2025 | 2.21 | 1.99 | 0.00 | 0.00 | 5 |
| final2 | PJM | january_2025 | 2.11 | -1.09 | -1.42 | -2.98 | 6 |
| final2 | SWPP | january_2025 | 3.13 | -3.11 | -3.11 | -4.93 | 6 |
| final2 | TVA | january_2025 | 3.42 | -2.18 | -2.35 | -7.58 | 6 |
| final_additive | BPAT | january_2025 | 3.22 | -3.47 | -3.99 | -5.58 | 6 |
| final_additive | CISO | january_2025 | 3.96 | 0.14 | -1.37 | -4.08 | 6 |
| final_additive | DUK | january_2025 | 4.08 | 0.49 | -1.19 | -6.25 | 6 |
| final_additive | ERCO | january_2025 | 3.47 | -4.64 | -4.64 | -9.56 | 6 |
| final_additive | FPL | january_2025 | 4.93 | -4.48 | -4.48 | -10.32 | 6 |
| final_additive | ISNE | january_2025 | 3.48 | -0.02 | -1.20 | -4.19 | 6 |
| final_additive | MISO | january_2025 | 2.76 | -2.91 | -2.91 | -4.80 | 6 |
| final_additive | NYIS | january_2025 | 1.85 | -0.43 | -0.95 | -3.22 | 5 |
| final_additive | PJM | january_2025 | 2.30 | 0.77 | -0.24 | -1.22 | 6 |
| final_additive | SWPP | january_2025 | 3.93 | -3.92 | -3.92 | -5.97 | 6 |
| final_additive | TVA | january_2025 | 3.71 | -1.97 | -2.52 | -7.21 | 6 |
| final_boosting | BPAT | january_2025 | 3.76 | -6.56 | -6.56 | -9.44 | 6 |
| final_boosting | CISO | january_2025 | 2.16 | -0.64 | -1.29 | -3.96 | 6 |
| final_boosting | DUK | january_2025 | 4.53 | -2.65 | -2.88 | -8.95 | 6 |
| final_boosting | ERCO | january_2025 | 3.41 | -5.67 | -5.67 | -7.31 | 6 |
| final_boosting | FPL | january_2025 | 4.71 | -6.26 | -6.26 | -11.78 | 6 |
| final_boosting | ISNE | january_2025 | 3.83 | 0.04 | -0.94 | -2.89 | 6 |
| final_boosting | MISO | january_2025 | 2.45 | -2.94 | -2.94 | -4.99 | 6 |
| final_boosting | NYIS | january_2025 | 3.14 | 1.87 | -0.00 | -0.02 | 5 |
| final_boosting | PJM | january_2025 | 2.76 | -3.62 | -3.82 | -8.46 | 6 |
| final_boosting | SWPP | january_2025 | 4.52 | -7.75 | -7.75 | -9.40 | 6 |
| final_boosting | TVA | january_2025 | 2.96 | -2.56 | -2.56 | -5.24 | 6 |
| final_ensemble | BPAT | january_2025 | 3.44 | -5.12 | -5.30 | -7.31 | 6 |
| final_ensemble | CISO | january_2025 | 2.65 | -0.32 | -1.27 | -4.01 | 6 |
| final_ensemble | DUK | january_2025 | 4.20 | -1.10 | -2.00 | -7.62 | 6 |
| final_ensemble | ERCO | january_2025 | 3.16 | -5.17 | -5.17 | -8.43 | 6 |
| final_ensemble | FPL | january_2025 | 4.37 | -5.40 | -5.40 | -10.56 | 6 |
| final_ensemble | ISNE | january_2025 | 3.36 | -0.00 | -0.93 | -2.50 | 6 |
| final_ensemble | MISO | january_2025 | 2.46 | -2.93 | -2.93 | -4.10 | 6 |
| final_ensemble | NYIS | january_2025 | 1.96 | 0.81 | -0.14 | -0.65 | 5 |
| final_ensemble | PJM | january_2025 | 2.05 | -1.30 | -1.55 | -3.07 | 6 |
| final_ensemble | SWPP | january_2025 | 4.16 | -5.72 | -5.72 | -7.60 | 6 |
| final_ensemble | TVA | january_2025 | 2.96 | -2.28 | -2.28 | -6.20 | 6 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | final2 | eve | 3.04 | 0.72 | -1.41 | 0.50 | 260 |
| 9 | final_ensemble | eve | 3.19 | -0.33 | -1.92 | 0.47 | 260 |
| 5 | DF | eve | 3.19 | 0.16 | -1.31 |  | 260 |
| 7 | final_additive | eve | 3.31 | -0.42 | -2.12 | 0.44 | 260 |
| 8 | final_boosting | eve | 3.51 | -0.29 | -1.92 | 0.42 | 260 |
| 1 | final2 | special | 3.22 | -0.34 | -2.02 | 0.52 | 273 |
| 0 | DF | special | 3.45 | -0.09 | -1.57 |  | 273 |
| 4 | final_ensemble | special | 3.47 | -1.34 | -2.63 | 0.50 | 273 |
| 2 | final_additive | special | 3.60 | -1.52 | -2.85 | 0.49 | 273 |
| 3 | final_boosting | special | 3.84 | -1.20 | -2.59 | 0.44 | 273 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final2 | all | 0.410 | 1.415 | 0.422 | 0.891 | 12.364 | 0.894 | 10239 |
| final2 | events | 0.468 | 1.864 | 0.719 | 0.808 | 13.027 | 0.785 | 130 |
| final2 | cold_mornings | 0.453 | 1.675 | 0.576 | 0.845 | 13.339 | 0.836 | 330 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final2 | BPAT | mape | 7.697 | 0.000 | 961 |
| final2 | CISO | mape | -56.610 | 0.000 | 949 |
| final2 | DUK | mape | 12.250 | 0.000 | 957 |
| final2 | ERCO | mape | 3.052 | 0.002 | 961 |
| final2 | FPL | mape | 4.845 | 0.000 | 918 |
| final2 | ISNE | mape | 18.468 | 0.000 | 954 |
| final2 | MISO | mape | -15.528 | 0.000 | 962 |
| final2 | NYIS | mape | -0.434 | 0.664 | 949 |
| final2 | PJM | mape | -27.656 | 0.000 | 949 |
| final2 | SWPP | mape | -9.311 | 0.000 | 952 |
| final2 | TVA | mape | 12.582 | 0.000 | 958 |
| final_additive | BPAT | mape | 12.442 | 0.000 | 961 |
| final_additive | CISO | mape | -33.203 | 0.000 | 949 |
| final_additive | DUK | mape | 14.599 | 0.000 | 957 |
| final_additive | ERCO | mape | 13.648 | 0.000 | 961 |
| final_additive | FPL | mape | 21.483 | 0.000 | 918 |
| final_additive | ISNE | mape | 24.336 | 0.000 | 954 |
| final_additive | MISO | mape | -6.623 | 0.000 | 962 |
| final_additive | NYIS | mape | 1.159 | 0.246 | 949 |
| final_additive | PJM | mape | -19.529 | 0.000 | 949 |
| final_additive | SWPP | mape | -7.251 | 0.000 | 952 |
| final_additive | TVA | mape | 17.219 | 0.000 | 958 |
| final_boosting | BPAT | mape | 12.646 | 0.000 | 961 |
| final_boosting | CISO | mape | -42.962 | 0.000 | 949 |
| final_boosting | DUK | mape | 14.864 | 0.000 | 957 |
| final_boosting | ERCO | mape | 9.722 | 0.000 | 961 |
| final_boosting | FPL | mape | 28.410 | 0.000 | 918 |
| final_boosting | ISNE | mape | 22.180 | 0.000 | 954 |
| final_boosting | MISO | mape | -9.256 | 0.000 | 962 |
| final_boosting | NYIS | mape | 0.981 | 0.327 | 949 |
| final_boosting | PJM | mape | -15.499 | 0.000 | 949 |
| final_boosting | SWPP | mape | -3.831 | 0.000 | 952 |
| final_boosting | TVA | mape | 18.525 | 0.000 | 958 |
| final_ensemble | BPAT | mape | 8.926 | 0.000 | 961 |
| final_ensemble | CISO | mape | -42.564 | 0.000 | 949 |
| final_ensemble | DUK | mape | 12.885 | 0.000 | 957 |
| final_ensemble | ERCO | mape | 9.409 | 0.000 | 961 |
| final_ensemble | FPL | mape | 22.190 | 0.000 | 918 |
| final_ensemble | ISNE | mape | 20.602 | 0.000 | 954 |
| final_ensemble | MISO | mape | -10.775 | 0.000 | 962 |
| final_ensemble | NYIS | mape | -0.150 | 0.881 | 949 |
| final_ensemble | PJM | mape | -22.210 | 0.000 | 949 |
| final_ensemble | SWPP | mape | -7.544 | 0.000 | 952 |
| final_ensemble | TVA | mape | 16.035 | 0.000 | 958 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.994 |
| final2 | 0.996 |
| final_additive | 0.871 |
| final_boosting | 0.996 |
| final_ensemble | 0.996 |
