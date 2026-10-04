# A later cut-off: what more of the day before's load and newer weather runs are worth

The recipe (`final10s`) on the eleven development BAs over 2023-01-01 to 2025-12-31 at four later cut-offs, against the 9 a.m. run of the 43-BA evaluation and each BA's published forecast (`DF`), on the days all six scored. *Load*: the cut-off at 3 p.m. or 9 p.m. of the day before (`BA_LOAD_FORECAST_CUTOFF_HOUR`) with the weather runs of the 9 a.m. cut-off (12 and 06 UTC). *Load and weather*: the same cut-off with the HRRR 18 and 00 UTC runs also available for the temperature (`BA_LOAD_FORECAST_HRRR_INIT_HOURS`, `Loader(aux_init_hours=...)`), the other inputs (NBM, its spread, HRRR dew point and wind) at the latest of their extracted runs; read from a separate data root built by `scripts/merge_late_runs.py`. Mean daily MAPE and mean under-forecast at the hour of the actual peak, in percent.

| BA | days | 9 a.m. | 3 p.m. load | 3 p.m. load and weather | 9 p.m. load | 9 p.m. load and weather | DF | peak 9 a.m. | peak 9 p.m. load and weather | peak DF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PJM | 1085 | 1.93 | 1.90 | 1.90 | 1.85 | 1.84 | 2.40 | -1.15 | -1.07 | -1.18 |
| MISO | 1093 | 1.74 | 1.73 | 1.72 | 1.68 | 1.67 | 2.71 | -0.90 | -0.83 | -0.23 |
| ERCO | 1090 | 2.21 | 2.16 | 2.13 | 2.10 | 2.03 | 2.41 | -1.21 | -1.07 | -0.80 |
| CISO | 1086 | 2.62 | 2.55 | 2.55 | 2.48 | 2.48 | 5.38 | -1.46 | -1.33 | -2.62 |
| SWPP | 1090 | 2.30 | 2.27 | 2.24 | 2.22 | 2.18 | 4.33 | -1.33 | -1.30 | -1.38 |
| NYIS | 1086 | 2.48 | 2.43 | 2.43 | 2.38 | 2.36 | 2.63 | -1.16 | -1.09 | -2.58 |
| ISNE | 1093 | 3.54 | 3.45 | 3.44 | 3.40 | 3.37 | 2.56 | -1.28 | -1.10 | -0.45 |
| TVA | 1092 | 2.40 | 2.36 | 2.32 | 2.30 | 2.20 | 2.28 | -1.38 | -1.33 | -0.88 |
| DUK | 1092 | 2.76 | 2.70 | 2.69 | 2.64 | 2.60 | 2.65 | -1.45 | -1.35 | -1.27 |
| BPAT | 1093 | 2.10 | 2.05 | 2.05 | 1.98 | 1.97 | 2.01 | -1.20 | -1.16 | -1.20 |
| FPL | 1071 | 3.12 | 3.01 | 3.00 | 2.86 | 2.85 | 3.21 | -1.31 | -1.18 | -1.68 |

Weighted by mean demand: MAPE 2.21 at 9 a.m.; 2.16 and 2.15 at 3 p.m. (load; load and weather); 2.11 and 2.08 at 9 p.m.; 2.90 for the published forecasts. BAs ahead of their published forecast: 7, 7, 7, 9 and 10 of 11. Under-forecast at the peak: -1.18 at 9 a.m., -1.17 at 3 p.m. and -1.09 at 9 p.m. (load and weather), -1.10 for the published forecasts.
