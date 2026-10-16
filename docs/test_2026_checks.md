# The test on January to September 2026: descriptive checks after the run

Written on 16 October 2026, after the run and the reports of `docs/test_2026_protocol.md`, by
`scripts/test_2026_checks.py`. None of this is the test: the headline of the protocol stands as reported in
`docs/test_2026_scoreboard.md`, and no BA-day was removed from it. These checks describe what the headline compares
against, the BA's own day-ahead forecast (`DF`) as published on Form EIA-930, and the band after the NBM moved to
version 5.0.

## 1. The published DF changed at several BAs

The headline compares the recipe with `DF` as published. At several BAs the published `DF` moved away from the
published demand in 2026 by far more than in earlier years. The table lists the comparable BAs with a level change
(below) or whose `DF` MAPE in 2026 is more than 1.5 times their 2023 to 2025 value. "Months moved" counts the months
of January to September 2026 in which the median hourly ratio `DF / D` moved by more than 5 % (in log) from the same
month of 2024 (raw EIA-930, all hours). A BA is marked as having a level change when that count is six or more; the
rule was written after the run, on these data, and marks 5: FMPP, LDWP, PSCO, SRP, SWPP.

| BA | months moved > 5 % | MAPE DF 2023-2025 | MAPE DF 2026 | MAPE recipe 2026 |
| --- | --- | --- | --- | --- |
| PSCO | 9 | 6.02 | 20.92 | 5.16 |
| SWPP | 8 | 4.33 | 10.42 | 2.69 |
| LDWP | 7 | 8.05 | 9.90 | 5.36 |
| FMPP | 6 | 4.29 | 21.83 | 3.82 |
| SRP | 6 | 3.21 | 8.32 | 6.94 |
| WACM | 3 | 15.41 | 9.87 | 3.35 |
| IPCO | 3 | 3.52 | 5.40 | 2.90 |
| AZPS | 2 | 5.91 | 8.78 | 4.43 |
| CISO | 0 | 5.38 | 10.92 | 2.93 |

Month by month (raw EIA-930, all hours, January to September of each year; hourly MAPE, so larger than the daily MAPE
of the scoreboard):

**FMPP**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.999 | 0.998 | 1.01 | 5 | 4.89 | 7.81 |
| 2 | 1.01 | 1 | 0.71 | 4.3 | 3.72 | 29.2 |
| 3 | 0.999 | 1.01 | 0.696 | 4.37 | 3.35 | 30.4 |
| 4 | 1 | 1 | 0.705 | 4 | 3.58 | 29.2 |
| 5 | 1.01 | 1.01 | 0.709 | 4.5 | 3.58 | 28.9 |
| 6 | 1.01 | 1.02 | 0.721 | 4.43 | 4.17 | 27.9 |
| 7 | 1.01 | 0.993 | 0.712 | 4.39 | 4.13 | 28.8 |
| 8 | 1.01 | 1.02 | 0.983 | 5.06 | 4.12 | 15.2 |
| 9 | 1.01 | 1.01 | 1.02 | 4.25 | 5.26 | 4 |

**LDWP**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.954 | 0.994 | 0.916 | 6.45 | 13.1 | 224 |
| 2 | 0.942 | 0.924 | 0.918 | 9.73 | 8.91 | 9.33 |
| 3 | 0.959 | 0.883 | 0.902 | 6.6 | 11.7 | 10.8 |
| 4 | 0.97 | 0.878 | 0.855 | 7.85 | 12.2 | 63.9 |
| 5 | 0.979 | 0.885 | 0.895 | 6.17 | 11.6 | 12.1 |
| 6 | 0.969 | 0.875 | 0.89 | 10.5 | 12.6 | 11.2 |
| 7 | 1.16 | 0.916 | 0.925 | 18.9 | 11 | 7.91 |
| 8 | 0.995 | 0.912 | 0.93 | 6.23 | 23.4 | 7.47 |
| 9 | 1.05 | 0.945 | 0.949 | 9.92 | 7.47 | 58 |

**PSCO**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.987 | 0.936 | 0.876 | 3.67 | 6.57 | 12.5 |
| 2 | 0.97 | 0.948 | 0.857 | 4.7 | 5.94 | 14.3 |
| 3 | 0.968 | 0.96 | 0.849 | 4.56 | 5.3 | 15.7 |
| 4 | 0.964 | 0.932 | 0.832 | 6.58 | 7.4 | 19.8 |
| 5 | 0.929 | 0.898 | 0.776 | 7.62 | 10 | 23.7 |
| 6 | 0.949 | 0.92 | 0.749 | 5.97 | 8.35 | 25.3 |
| 7 | 0.944 | 0.941 | 0.708 | 5.99 | 6.78 | 28.6 |
| 8 | 0.944 | 0.934 | 0.75 | 6.68 | 7.25 | 25.3 |
| 9 | 0.933 | 0.946 | 0.758 | 7.1 | 6.74 | 24.3 |

**SRP**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.986 | 0.974 | 0.978 | 2.81 | 3.49 | 4.2 |
| 2 | 0.983 | 0.957 | 0.968 | 2.83 | 4.94 | 3.64 |
| 3 | 0.978 | 0.964 | 1.02 | 2.88 | 4.81 | 7.56 |
| 4 | 0.983 | 0.967 | 1.14 | 2.8 | 4.29 | 20.5 |
| 5 | 0.982 | 0.977 | 1.25 | 2.51 | 3.18 | 29.8 |
| 6 | 0.976 | 0.969 | 1.03 | 3.21 | 3.78 | 8.46 |
| 7 | 0.984 | 0.972 | 1.05 | 2.81 | 4.02 | 7.68 |
| 8 | 0.981 | 0.979 | 1.06 | 3.79 | 3.59 | 10.6 |
| 9 | 0.969 | 0.978 | 1.08 | 3.77 | 3.95 | 14.6 |

**SWPP**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.992 | 0.991 | 1.17 | 3.82 | 1.98 | 16.3 |
| 2 | 0.993 | 0.987 | 1.13 | 2.93 | 2.75 | 12.7 |
| 3 | 0.998 | 0.997 | 1.1 | 4.96 | 2.09 | 9.82 |
| 4 | 0.999 | 0.995 | 1.11 | 1.61 | 1.92 | 14.1 |
| 5 | 0.994 | 1.1 | 1.11 | 1.81 | 9.47 | 10.4 |
| 6 | 0.99 | 1.1 | 1.04 | 2.01 | 13.8 | 7.37 |
| 7 | 0.986 | 1.1 | 1.09 | 2.32 | 10.1 | 8.76 |
| 8 | 0.999 | 1.09 | 1.09 | 1.45 | 8.67 | 8.16 |
| 9 | 0.99 | 1.11 | 1.07 | 1.98 | 9.53 | 7.28 |

**CISO**

| month | DF / D 2024 | DF / D 2025 | DF / D 2026 | MAPE DF 2024 | MAPE DF 2025 | MAPE DF 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.963 | 0.959 | 0.966 | 5.95 | 7.9 | 8.27 |
| 2 | 0.957 | 0.958 | 0.972 | 6.6 | 7.77 | 8.75 |
| 3 | 0.957 | 0.955 | 0.975 | 7.43 | 8.55 | 9.48 |
| 4 | 0.955 | 0.947 | 0.961 | 9.24 | 9.98 | 11 |
| 5 | 0.95 | 0.946 | 0.966 | 8.34 | 8.5 | 11 |
| 6 | 0.963 | 0.949 | 0.965 | 6.55 | 8.06 | 10.1 |
| 7 | 0.968 | 0.95 | 0.969 | 6.08 | 8.1 | 8.17 |
| 8 | 0.967 | 0.946 | 0.96 | 6.02 | 7.46 | 8.21 |
| 9 | 0.975 | 0.95 | 0.965 | 6.04 | 7.12 | 8.13 |

SWPP and LDWP had already moved in 2025 (SWPP from May 2025), so part of their change is also in the 2023 to 2025
evaluation. CISO is not marked by the level rule (its ratio stays between 0.95 and 0.98 in the three years), but its
`DF` error rose from 5.38 % over 2023 to 2025 to 10.92 % in
2026. The `DF` as the run saw it (protocol v2 applied), shifted by whole hours, points to a change of hour labels in the
published series: from December 2025 on, a shift of one hour (+1 h) lowers its error in every month:

| month | days | MAPE recipe | MAPE DF | DF shifted -2 h | DF shifted -1 h | DF shifted +1 h | DF shifted +2 h |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-01 | 31 | 2.47 | 5.95 | 8.80 | 7.01 | 7.90 | 10.06 |
| 2025-02 | 28 | 2.63 | 5.81 | 8.75 | 6.96 | 7.77 | 10.05 |
| 2025-03 | 31 | 2.53 | 6.68 | 9.67 | 7.79 | 8.55 | 11.07 |
| 2025-04 | 30 | 3.14 | 8.47 | 11.40 | 9.65 | 9.98 | 12.12 |
| 2025-05 | 31 | 2.43 | 7.52 | 11.12 | 8.96 | 8.51 | 10.35 |
| 2025-06 | 30 | 2.73 | 7.18 | 11.34 | 8.74 | 8.06 | 9.77 |
| 2025-07 | 31 | 2.25 | 7.21 | 11.99 | 9.21 | 8.10 | 9.73 |
| 2025-08 | 31 | 2.27 | 6.64 | 11.96 | 8.77 | 7.46 | 9.10 |
| 2025-09 | 30 | 2.66 | 6.39 | 11.28 | 8.42 | 7.12 | 8.55 |
| 2025-10 | 31 | 2.59 | 8.27 | 11.79 | 9.70 | 9.26 | 10.68 |
| 2025-11 | 30 | 3.10 | 7.45 | 10.33 | 8.50 | 8.35 | 9.68 |
| 2025-12 | 31 | 3.58 | 7.81 | 11.37 | 9.59 | 6.83 | 7.99 |
| 2026-01 | 31 | 2.80 | 9.26 | 12.41 | 10.82 | 8.27 | 9.41 |
| 2026-02 | 28 | 2.84 | 10.04 | 13.54 | 11.84 | 8.74 | 10.02 |
| 2026-03 | 31 | 3.46 | 11.45 | 16.06 | 13.84 | 9.49 | 10.41 |
| 2026-04 | 30 | 2.92 | 12.12 | 15.58 | 13.88 | 11.01 | 12.06 |
| 2026-05 | 31 | 2.84 | 12.62 | 16.77 | 14.77 | 11.04 | 11.81 |
| 2026-06 | 30 | 3.08 | 11.86 | 16.89 | 14.43 | 10.07 | 10.34 |
| 2026-07 | 31 | 2.78 | 10.49 | 16.45 | 13.50 | 8.17 | 8.48 |
| 2026-08 | 31 | 2.63 | 10.28 | 16.48 | 13.35 | 8.21 | 8.37 |
| 2026-09 | 30 | 3.01 | 10.16 | 15.48 | 12.85 | 8.14 | 8.30 |

## 2. The headline without those BAs

The aggregates of the scoreboard recomputed on the comparable BAs left after removing the marked BAs, and CISO as
well. Same per-BA numbers as `docs/test_2026_scoreboard.md`; only the set changes.

| set | BAs | MAPE recipe, weighted | MAPE DF, weighted | MAPE recipe, median | MAPE DF, median | BAs better | BAs worse | better, p < 0.05 | worse, p < 0.05 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 comparable BAs (the headline) | 38 | 2.60 | 4.22 | 3.25 | 3.68 | 24 | 14 | 22 | 11 |
| without the BAs with a level change (FMPP, LDWP, PSCO, SRP, SWPP) | 33 | 2.49 | 3.34 | 3.03 | 3.24 | 19 | 14 | 17 | 11 |
| without those and CISO | 32 | 2.46 | 2.84 | 3.14 | 3.19 | 18 | 14 | 16 | 11 |

Without the published series that changed, the recipe stays ahead on the demand-weighted MAPE, by a much smaller
margin than in the headline, and the medians of the two are close: the gain is concentrated in the largest BAs and in
the BAs whose `DF` is weak. Removing those BAs removes only BAs where the recipe was ahead; the 14
comparable BAs where `DF` is ahead are the same in every row: AECI, SOCO, ISNE, BANC, PACW, PGE, TPWR, NYIS, BPAT, NWMT, ERCO, EPE, FPL, TVA.

## 3. The band by month

Coverage of the 90 % band (mean over BA-days) and Winkler score and width (weighted by mean demand), 43 BAs. The NBM
moved to version 5.0 in May 2026, with a spread about 0.9 times that of version 4.3 on the one day both versions hold
(protocol addendum).

| month | BA-days | coverage 90 | Winkler 90, weighted | width 90, weighted |
| --- | --- | --- | --- | --- |
| January | 1237 | 0.908 | 18.084 | 13.901 |
| February | 1117 | 0.890 | 15.793 | 12.771 |
| March | 1219 | 0.901 | 15.922 | 13.002 |
| April | 1190 | 0.895 | 14.526 | 11.569 |
| May | 1221 | 0.895 | 15.101 | 12.046 |
| June | 1209 | 0.891 | 15.290 | 11.981 |
| July | 1269 | 0.903 | 14.488 | 11.101 |
| August | 1254 | 0.902 | 13.180 | 10.393 |
| September | 1213 | 0.877 | 13.597 | 9.756 |

| NBM | BA-days | coverage 90 | Winkler 90, weighted | width 90, weighted |
| --- | --- | --- | --- | --- |
| January to April (version 4.3) | 4763 | 0.899 | 16.176 | 12.866 |
| May to September (version 5.0) | 6166 | 0.894 | 14.296 | 11.021 |

Coverage is within one point of 90 % in every month except September (0.877). The
width narrows from January to September, and already from January to April under version 4.3, so this table does not
separate the effect of version 5.0 from that of the season.
