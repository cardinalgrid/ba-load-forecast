# The recipe against each BA's own forecast on the 43 BAs, 2023 to 2025

Daily rows of the 43-BA evaluation (`run_phase_e.py --groups b4`, 2023-01-01 to 2025-12-31, 9 a.m. cut-off, protocol v2),
on the days both `final10s` and `DF` scored. MAPE is the mean of the daily MAPE in percent of the actual; peak under-forecast
in percent of the actual peak (negative is under); coverage and Winkler score of the 90 % band of `final10s`. DM is the
Diebold-Mariano statistic of the daily MAPE of `final10s` against `DF` (negative: the recipe's errors are smaller; `*` for
p < 0.05, two-sided, normal approximation). Gap is MAPE of the recipe minus MAPE of `DF`; negative is better.

(a) The EIA lists the day-ahead forecast of these BAs as not comparable with their demand (a different basis or a subset of
the system): AVA, FPC, LGEE, PSEI, TEPC. They stay in the evaluation of the forecaster and are left out of the aggregates
against `DF`.

## Aggregates

Weighted means use each BA's mean demand on the days scored as the weight.

| set | BAs | MAPE recipe, weighted | MAPE DF, weighted | MAPE recipe, median | MAPE DF, median | BAs better | BAs worse | better, p < 0.05 | worse, p < 0.05 | coverage 90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all 43 BAs, forecaster only | 43 | 2.44 | 3.59 | 2.88 | 3.52 | 30 | 13 | 28 | 12 | 0.892 |
| 38 comparable BAs | 38 | 2.41 | 3.16 | 2.86 | 3.40 | 26 | 12 | 24 | 11 | 0.892 |
| 11 development BAs | 11 | 2.21 | 2.90 | 2.40 | 2.63 | 7 | 4 | 6 | 4 | 0.891 |
| 27 new comparable BAs | 27 | 3.18 | 4.14 | 3.07 | 4.29 | 19 | 8 | 18 | 7 | 0.892 |

## By BA, sorted by the gap

| BA | set | mean MW | days | MAPE recipe | MAPE DF | gap | DM | peak under recipe | peak under DF | coverage 90 | Winkler 90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PSEI (a) | new | 2870 | 900 | 2.58 | 22.62 | -20.05 | -67.9* | -1.42 | -28.58 | 0.885 | 15.72 |
| FPC (a) | new | 6584 | 1090 | 3.64 | 23.12 | -19.48 | -159.5* | -1.78 | -24.42 | 0.896 | 22.29 |
| WACM | new | 3857 | 995 | 3.68 | 15.41 | -11.74 | -99.9* | -2.01 | -17.51 | 0.893 | 21.50 |
| LGEE (a) | new | 4278 | 1095 | 3.46 | 7.85 | -4.39 | -46.0* | -1.82 | -8.89 | 0.894 | 19.54 |
| WALC | new | 1012 | 907 | 5.52 | 9.65 | -4.13 | -24.6* | -5.69 | -8.16 | 0.897 | 37.40 |
| NEVP | new | 4556 | 1075 | 2.48 | 6.24 | -3.77 | -45.4* | -1.86 | -6.18 | 0.895 | 15.06 |
| PNM | new | 1669 | 1095 | 2.77 | 6.27 | -3.51 | -46.5* | -1.45 | -6.01 | 0.892 | 15.75 |
| LDWP | new | 2713 | 1062 | 5.27 | 8.05 | -2.78 | -23.6* | -4.73 | -9.33 | 0.894 | 34.34 |
| CISO | development | 25353 | 1086 | 2.62 | 5.38 | -2.76 | -38.4* | -1.46 | -2.62 | 0.892 | 14.94 |
| AZPS | new | 4125 | 1082 | 3.64 | 5.91 | -2.27 | -22.2* | -1.73 | -3.33 | 0.888 | 22.69 |
| PSCO | new | 5104 | 1074 | 3.95 | 6.02 | -2.07 | -24.1* | -3.45 | -7.42 | 0.888 | 23.17 |
| SWPP | development | 33082 | 1090 | 2.30 | 4.33 | -2.02 | -16.8* | -1.33 | -1.38 | 0.881 | 16.56 |
| PACE | new | 5974 | 1091 | 2.77 | 4.33 | -1.57 | -23.1* | -1.88 | -1.17 | 0.890 | 15.23 |
| PACW | new | 2409 | 1024 | 2.91 | 4.38 | -1.47 | -11.7* | -1.83 | -0.75 | 0.894 | 17.78 |
| FMPP | new | 2181 | 1058 | 2.99 | 4.29 | -1.29 | -17.1* | -1.51 | -1.97 | 0.895 | 18.39 |
| JEA | new | 1548 | 1075 | 3.51 | 4.75 | -1.24 | -19.0* | -2.02 | -1.73 | 0.896 | 21.03 |
| MISO | development | 74146 | 1093 | 1.74 | 2.71 | -0.97 | -20.7* | -0.90 | -0.23 | 0.895 | 9.70 |
| SCEG | new | 2790 | 1065 | 3.77 | 4.57 | -0.80 | -11.2* | -2.50 | -4.59 | 0.891 | 22.08 |
| TEC | new | 2556 | 1087 | 3.71 | 4.49 | -0.78 | -10.6* | -1.41 | -1.88 | 0.892 | 23.47 |
| IPCO | new | 2129 | 1092 | 2.85 | 3.52 | -0.68 | -8.8* | -1.58 | -1.97 | 0.894 | 16.28 |
| CPLW | new | 547 | 1085 | 4.05 | 4.64 | -0.59 | -2.9* | -2.34 | -3.07 | 0.891 | 28.34 |
| SCL | new | 1081 | 1083 | 2.76 | 3.29 | -0.53 | -9.5* | -1.54 | -3.35 | 0.890 | 14.89 |
| CPLE | new | 6990 | 1091 | 3.61 | 4.10 | -0.49 | -6.9* | -2.03 | -1.47 | 0.894 | 22.03 |
| PJM | development | 92971 | 1085 | 1.93 | 2.40 | -0.47 | -12.7* | -1.15 | -1.18 | 0.891 | 11.11 |
| TEPC (a) | new | 1646 | 1073 | 3.97 | 4.30 | -0.33 | -2.7* | -1.87 | -2.05 | 0.896 | 24.61 |
| ERCO | development | 53199 | 1090 | 2.21 | 2.41 | -0.20 | -4.5* | -1.21 | -0.80 | 0.892 | 13.07 |
| NYIS | development | 17098 | 1086 | 2.48 | 2.63 | -0.14 | -2.8* | -1.16 | -2.58 | 0.890 | 13.65 |
| SRP | new | 4047 | 1064 | 3.07 | 3.21 | -0.14 | -2.8* | -1.77 | -3.31 | 0.891 | 19.24 |
| FPL | development | 16584 | 1071 | 3.12 | 3.21 | -0.09 | -1.6 | -1.31 | -1.68 | 0.895 | 19.32 |
| GCPD | new | 749 | 1092 | 2.16 | 2.17 | -0.01 | -0.2 | -0.83 | -1.92 | 0.890 | 12.11 |
| EPE | new | 1048 | 1090 | 3.25 | 3.20 | +0.05 | 1.0 | -1.93 | -2.57 | 0.893 | 20.03 |
| BPAT | development | 6761 | 1093 | 2.10 | 2.01 | +0.10 | 2.6* | -1.20 | -1.20 | 0.892 | 11.53 |
| DUK | development | 12266 | 1092 | 2.76 | 2.65 | +0.11 | 2.4* | -1.45 | -1.27 | 0.894 | 17.07 |
| TVA | development | 18783 | 1092 | 2.40 | 2.28 | +0.12 | 3.1* | -1.38 | -0.88 | 0.894 | 14.20 |
| SC | new | 3063 | 1088 | 3.70 | 3.52 | +0.18 | 2.9* | -1.80 | -1.13 | 0.893 | 21.21 |
| TPWR | new | 528 | 1093 | 2.88 | 2.41 | +0.47 | 8.5* | -1.77 | -0.99 | 0.893 | 15.99 |
| BANC | new | 1997 | 1058 | 2.77 | 2.22 | +0.55 | 12.3* | -1.85 | -1.47 | 0.894 | 16.81 |
| AVA (a) | new | 1485 | 1089 | 2.42 | 1.76 | +0.66 | 16.2* | -1.35 | -1.17 | 0.893 | 13.54 |
| NWMT | new | 1359 | 1078 | 2.81 | 1.96 | +0.85 | 19.1* | -1.73 | -1.67 | 0.890 | 16.30 |
| SOCO | new | 27015 | 1087 | 2.67 | 1.70 | +0.97 | 20.1* | -1.57 | -0.84 | 0.893 | 15.99 |
| ISNE | development | 12994 | 1093 | 3.54 | 2.56 | +0.98 | 17.6* | -1.28 | -0.45 | 0.895 | 19.08 |
| PGE | new | 2612 | 1093 | 2.35 | 1.33 | +1.02 | 27.7* | -1.47 | -0.95 | 0.890 | 14.24 |
| AECI | new | 2578 | 1093 | 4.16 | 2.91 | +1.26 | 18.4* | -2.13 | -1.88 | 0.894 | 23.44 |

![The recipe against each BA's forecast](figures/scoreboard_43_bas.png)
