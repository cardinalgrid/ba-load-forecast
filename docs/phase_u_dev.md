# Phase U: extra stations, the decision on the development period

Reference `st1h:u_hrrr_1`, candidate `st2h:u_hrrr_x`, days both scored. Rule fixed before the run (section 8u of `docs/methods.md`): per BA, yearly MAPE better by at least 0.03 point and the peak under-forecast not worse by more than 0.10 point on the event days, the 30 coldest mornings and the 30 largest peaks; adopted if the weighted MAPE improves and at least 7 of 12 BAs pass.

**Weighted MAPE 3.526 -> 3.234; 6 of 12 BAs pass; NOT ADOPTED.**

## By stratum

| stratum | bas | days | mape_ref | mape_cand | peak_under_ref | peak_under_cand | coverage_cand | bas_better |
|---|---|---|---|---|---|---|---|---|
| all | 12 | 8734 | 3.53 | 3.23 | -2.06 | -1.79 | 0.88 | 12 |
| winter | 12 | 2425 | 3.50 | 3.15 | -2.12 | -1.84 | 0.88 | 12 |
| summer | 12 | 2837 | 3.85 | 3.52 | -1.82 | -1.47 | 0.87 | 9 |
| shoulder | 12 | 3472 | 3.31 | 3.08 | -2.25 | -2.04 | 0.90 | 12 |
| events | 12 | 124 | 5.14 | 4.42 | -3.58 | -3.09 | 0.79 | 7 |
| cold_mornings | 12 | 360 | 4.15 | 3.74 | -3.06 | -2.59 | 0.85 | 8 |
| top_peaks | 12 | 360 | 3.65 | 3.39 | -2.54 | -2.23 | 0.88 | 8 |

## By BA

| ba | days | demand_mw | mape_ref | mape_cand | mape_gap | peak_gap_events | peak_gap_cold_mornings | peak_gap_top_peaks | pass_mape | pass_peak | pass |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOCO | 752 | 27052 | 3.49 | 3.03 | -0.45 | 1.15 | 1.09 | 0.49 | True | True | True |
| LDWP | 739 | 2941 | 5.73 | 5.17 | -0.57 | 1.18 | 0.28 | 2.62 | True | True | True |
| TPWR | 752 | 567 | 3.27 | 3.05 | -0.22 | -0.50 | 0.74 | 0.96 | True | False | False |
| NWMT | 728 | 1346 | 3.17 | 2.88 | -0.29 | -0.78 | -0.05 | 1.27 | True | False | False |
| PSCO | 752 | 5413 | 3.06 | 3.05 | -0.01 | -0.15 | -0.15 | -0.66 | False | False | False |
| WACM | 575 | 2757 | 4.88 | 4.80 | -0.08 | 0.10 | -0.08 | -0.08 | True | True | True |
| BANC | 721 | 1989 | 3.13 | 3.00 | -0.14 | -0.04 | 0.11 | 0.40 | True | True | True |
| PGE | 754 | 2511 | 2.79 | 2.74 | -0.04 | -0.22 | 0.02 | -0.41 | True | False | False |
| PACE | 750 | 5708 | 3.37 | 3.31 | -0.06 | 0.09 | 0.03 | 0.04 | True | True | True |
| AECI | 753 | 2812 | 3.96 | 3.44 | -0.51 | -1.08 | -0.93 | -0.53 | True | False | False |
| WALC | 705 | 1100 | 4.72 | 4.66 | -0.05 | -0.28 | -0.15 | -0.18 | True | False | False |
| NEVP | 753 | 4445 | 2.41 | 2.37 | -0.04 | 0.03 | -0.06 | 0.21 | True | True | True |

## Each event (weighted)

```
         bas  days  ref_mape  ref_peak_under  ref_worst  u_hrrr_x_mape  u_hrrr_x_peak_under  u_hrrr_x_worst
event                                                                                                      
uri       11    65      4.81           -4.94     -20.68           4.09                -3.61          -20.87
elliott   12    59      5.61           -2.11     -15.63           4.87                -2.59          -16.79
```
