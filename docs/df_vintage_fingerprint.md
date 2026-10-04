# When is each BA's published forecast made? The error-by-hour fingerprint

Hourly outputs of the `b4` run, 2023-01-01 to 2025-12-31. Fingerprint = (MAE of `DF` / MAE of `final10s`) at hours 00-03 divided by the same ratio at hours 20-23, local reporting clock, `DF` first corrected by its own trailing hourly bias. CAISO, whose `DF` is matched to the day-ahead market forecast of the morning before, gives 1.08; MISO, whose `DF` is matched to a report published at about 00:30 EST of the target day but updated at an unknown hour of the day before, gives 1.19. The scale is not validated: the column is a signal, not a time. A BA with no row has a series the test cannot use (a ratio that is not positive at some hour).

| BA | set | days | fingerprint | slope of log ratio per hour | MAE DF 00-03 | MAE DF 20-23 | signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PGE | new | 1072 | 0.44 | +0.045 | 0.53 | 1.55 | relatively better in the first hours: consistent with a DF made close to the day |
| NWMT | new | 1070 | 0.59 | +0.028 | 1.14 | 2.19 | relatively better in the first hours: consistent with a DF made close to the day |
| WALC | new | 1052 | 0.59 | +0.039 | 19.19 | 29.62 | relatively better in the first hours: consistent with a DF made close to the day |
| EPE | new | 1074 | 0.65 | +0.019 | 1.82 | 3.18 | relatively better in the first hours: consistent with a DF made close to the day |
| BANC | new | 1069 | 0.66 | +0.016 | 1.09 | 2.31 | relatively better in the first hours: consistent with a DF made close to the day |
| SCEG | new | 1045 | 0.66 | +0.021 | 2.20 | 25.09 | relatively better in the first hours: consistent with a DF made close to the day |
| TPWR | new | 1072 | 0.72 | +0.011 | 1.52 | 2.20 | relatively better in the first hours: consistent with a DF made close to the day |
| SRP | new | 1051 | 0.74 | +0.019 | 2.01 | 3.09 | relatively better in the first hours: consistent with a DF made close to the day |
| AVA (a) | new | 1071 | 0.76 | +0.011 | 1.19 | 1.82 | relatively better in the first hours: consistent with a DF made close to the day |
| FPL | development | 1057 | 0.80 | +0.016 | 1.68 | 2.79 | no clear signal |
| AZPS | new | 1073 | 0.82 | +0.006 | 2.53 | 3.12 | no clear signal |
| TEPC (a) | new | 1068 | 0.85 | +0.006 | 3.14 | 4.06 | no clear signal |
| SCL | new | 1067 | 0.89 | +0.005 | 2.68 | 3.35 | no clear signal |
| TEC | new | 1068 | 0.92 | +0.002 | 3.61 | 4.57 | no clear signal |
| JEA | new | 1058 | 0.92 | -0.000 | 3.18 | 3.71 | no clear signal |
| CPLW | new | 1071 | 0.93 | +0.006 | 4.82 | 5.51 | no clear signal |
| CPLE | new | 1071 | 0.94 | +0.003 | 3.53 | 3.71 | no clear signal |
| SC | new | 1069 | 0.97 | +0.001 | 2.42 | 2.66 | no clear signal |
| NYIS | development | 1069 | 0.98 | -0.004 | 1.51 | 1.91 | no clear signal |
| GCPD | new | 1072 | 0.98 | -0.000 | 1.46 | 1.80 | no clear signal |
| IPCO | new | 1072 | 0.99 | -0.003 | 3.13 | 3.48 | no clear signal |
| PSCO | new | 1067 | 1.00 | +0.000 | 11.78 | 11.53 | no clear signal |
| SWPP | development | 1070 | 1.02 | -0.002 | 2.46 | 2.78 | no clear signal |
| PNM | new | 1075 | 1.02 | +0.001 | 1.97 | 2.18 | no clear signal |
| ERCO | development | 1069 | 1.04 | -0.005 | 2.01 | 2.25 | no clear signal |
| DUK | development | 1071 | 1.04 | -0.003 | 2.39 | 2.68 | no clear signal |
| TVA | development | 1072 | 1.04 | -0.003 | 1.92 | 2.06 | no clear signal |
| CISO | development | 1058 | 1.08 | -0.006 | 1.62 | 1.64 | matched: CAISO day-ahead market forecast, morning of D-1 |
| FMPP | new | 1067 | 1.08 | -0.009 | 5.36 | 6.16 | no clear signal |
| BPAT | development | 1072 | 1.10 | -0.007 | 1.81 | 1.95 | no clear signal |
| FPC (a) | new | 1070 | 1.10 | -0.005 | 3.22 | 3.39 | no clear signal |
| LGEE (a) | new | 1075 | 1.11 | -0.004 | 2.84 | 2.84 | no clear signal |
| LDWP | new | 1064 | 1.11 | -0.005 | 7.44 | 12.90 | no clear signal |
| AECI | new | 1072 | 1.12 | -0.009 | 2.75 | 2.73 | no clear signal |
| PACE | new | 1072 | 1.13 | -0.006 | 3.54 | 3.39 | no clear signal |
| NEVP | new | 1063 | 1.17 | -0.010 | 3.19 | 3.18 | no clear signal |
| PACW | new | 1072 | 1.18 | -0.013 | 5.08 | 5.17 | no clear signal |
| PJM | development | 1065 | 1.18 | -0.013 | 1.65 | 1.61 | no clear signal |
| MISO | development | 1072 | 1.19 | -0.010 | 1.59 | 1.55 | matched: forecast in MISO's report published about 00:30 EST of D, updated during D-1 (hour unknown) |
| SOCO | new | 1069 | 1.35 | -0.019 | 1.04 | 0.80 | relatively worse in the first hours: no sign of a late DF |
| PSEI (a) | new | 1072 | 1.38 | -0.022 | 16.58 | 14.72 | relatively worse in the first hours: no sign of a late DF |
| ISNE | development | 1070 | 1.61 | -0.026 | 2.39 | 1.32 | relatively worse in the first hours: no sign of a late DF |

(a) `DF` listed by the EIA as not comparable with demand.
