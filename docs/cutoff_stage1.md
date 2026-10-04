# A later cut-off, stage 1: more of the day before's load, the same weather runs

The recipe (`final10s`) run on the eleven development BAs over 2023-01-01 to 2025-12-31 with the cut-off at 3 p.m. and 9 p.m. of the day before (`BA_LOAD_FORECAST_CUTOFF_HOUR`, `src/ba_load_forecast/cutoff.py`) instead of 9 a.m.: the load is known until the hour before the cut-off, the temperature path starts at it, and the weather runs are the same extracted 12 and 06 UTC runs, so the gain is what the afternoon and evening load of the day before is worth. Compared with the 9 a.m. run of the 43-BA evaluation (`b4`) and with each BA's published forecast (`DF`) on the days all four scored. Mean daily MAPE and mean under-forecast at the hour of the actual peak, in percent.

| BA | days | MAPE 9 a.m. | MAPE 3 p.m. | MAPE 9 p.m. | MAPE DF | peak 9 a.m. | peak 3 p.m. | peak 9 p.m. | peak DF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PJM | 1085 | 1.93 | 1.90 | 1.85 | 2.40 | -1.15 | -1.14 | -1.09 | -1.18 |
| MISO | 1093 | 1.74 | 1.73 | 1.68 | 2.71 | -0.90 | -0.92 | -0.84 | -0.23 |
| ERCO | 1090 | 2.21 | 2.16 | 2.10 | 2.41 | -1.21 | -1.21 | -1.15 | -0.80 |
| CISO | 1086 | 2.62 | 2.55 | 2.48 | 5.38 | -1.46 | -1.45 | -1.34 | -2.62 |
| SWPP | 1090 | 2.30 | 2.27 | 2.22 | 4.33 | -1.33 | -1.34 | -1.31 | -1.38 |
| NYIS | 1086 | 2.48 | 2.43 | 2.38 | 2.63 | -1.16 | -1.17 | -1.09 | -2.58 |
| ISNE | 1093 | 3.54 | 3.45 | 3.40 | 2.56 | -1.28 | -1.25 | -1.11 | -0.45 |
| TVA | 1092 | 2.40 | 2.36 | 2.30 | 2.28 | -1.38 | -1.38 | -1.36 | -0.88 |
| DUK | 1092 | 2.76 | 2.70 | 2.64 | 2.65 | -1.45 | -1.40 | -1.38 | -1.27 |
| BPAT | 1093 | 2.10 | 2.05 | 1.98 | 2.01 | -1.20 | -1.19 | -1.15 | -1.20 |
| FPL | 1071 | 3.12 | 3.01 | 2.86 | 3.21 | -1.31 | -1.28 | -1.21 | -1.68 |

Weighted by mean demand: MAPE 2.21 at 9 a.m., 2.16 at 3 p.m., 2.11 at 9 p.m., 2.90 for the published forecasts; under-forecast at the peak -1.18, -1.18, -1.12 and -1.10. BAs ahead of their published forecast: 7, 7 and 9 of 11.
