# HRRR 2 m temperature against ISD-Lite observations

Forecast minus observed at the nearest HRRR grid cell of each station, 2020, 2021, 2022, 2023, 2024, 2025, leads 17 to 45 h of the 12 and 06 UTC runs (the leads a day-ahead forecast issued at 9 a.m. local time uses). 3493344 forecast-observation pairs at 35 stations. Observations are hourly ISD-Lite readings; a station reports to the nearest tenth of a degree Celsius.

Overall: bias -1.23 °F, MAE 3.12 °F, RMSE 4.02 °F.

On the 30 coldest mornings of each station (lowest observed minimum between 04:00 and 09:00 local time), hours 04:00 to 09:00: bias +0.11 °F, MAE 3.48 °F, 12813 pairs. A positive bias means the forecast was warmer than what occurred.

![MAE by lead](figures/hrrr_mae_by_lead.png)

![Bias on cold mornings by station](figures/hrrr_cold_morning_bias.png)

## By observed temperature

| bin | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| below 20 F | 40767 | 1.44 | 3.77 | 5.24 |
| 20 to 32 F | 180362 | 0.51 | 3.01 | 4.01 |
| 32 to 59 F | 1275210 | -1.52 | 3.13 | 3.96 |
| 59 to 72 F | 868328 | -1.52 | 3.11 | 4 |
| above 72 F | 1128677 | -1.05 | 3.12 | 4.05 |

## By month

| month | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| 1 | 311697 | -1.35 | 3.25 | 4.15 |
| 2 | 285331 | -1.42 | 3.42 | 4.42 |
| 3 | 313978 | -1.89 | 3.31 | 4.19 |
| 4 | 303101 | -1.67 | 3.13 | 4 |
| 5 | 314368 | -1.14 | 2.95 | 3.84 |
| 6 | 303299 | -0.57 | 2.95 | 3.88 |
| 7 | 314506 | -0.28 | 3.02 | 3.98 |
| 8 | 302288 | -0.34 | 2.98 | 3.92 |
| 9 | 242138 | -1.11 | 2.85 | 3.66 |
| 10 | 251446 | -1.73 | 3.02 | 3.80 |
| 11 | 243268 | -1.93 | 3.26 | 4.09 |
| 12 | 307924 | -1.56 | 3.27 | 4.15 |

## By station

| icao | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| KABQ | 99971 | -0.34 | 3.06 | 3.87 |
| KATL | 99806 | -1.88 | 3.15 | 4.01 |
| KAVL | 99651 | -0.91 | 3.02 | 3.89 |
| KBIL | 99959 | 0.91 | 3.05 | 4.14 |
| KBNA | 99976 | -1.65 | 3.10 | 4.09 |
| KBOI | 99889 | -0.01 | 2.50 | 3.28 |
| KBOS | 99977 | -2.31 | 3.35 | 4.26 |
| KCAE | 99729 | -0.15 | 2.88 | 3.77 |
| KCHS | 99966 | -1.12 | 2.52 | 3.33 |
| KCLT | 99773 | -1.18 | 2.94 | 3.83 |
| KDEN | 99991 | 0.34 | 3.50 | 4.76 |
| KDFW | 99979 | -1.21 | 2.88 | 3.78 |
| KELP | 100003 | -2.86 | 3.93 | 4.96 |
| KGEG | 97920 | 0.03 | 2.70 | 3.50 |
| KIND | 99966 | -0.61 | 2.54 | 3.34 |
| KJAX | 99969 | -0.06 | 2.44 | 3.29 |
| KJFK | 99954 | -2.24 | 3.20 | 4.06 |
| KLAS | 99907 | -1.62 | 3.71 | 4.48 |
| KLAX | 99974 | -2.44 | 3.18 | 3.98 |
| KMCO | 99849 | -1.84 | 2.75 | 3.54 |
| KMGM | 99402 | -0.36 | 2.76 | 3.66 |
| KMIA | 99965 | -3.23 | 3.65 | 4.36 |
| KMWH | 99549 | 0.85 | 3.30 | 4.28 |
| KOKC | 99942 | 1.29 | 2.90 | 3.87 |
| KPDX | 99957 | -2.06 | 3.42 | 4.12 |
| KPHL | 99931 | -2.36 | 3.40 | 4.25 |
| KPHX | 99856 | -3.12 | 4.39 | 5.34 |
| KRDU | 99892 | -1.45 | 2.98 | 3.85 |
| KSDF | 99898 | -1.85 | 3.20 | 4.13 |
| KSEA | 99927 | -1.06 | 2.54 | 3.21 |
| KSGF | 99672 | 0.39 | 2.80 | 3.67 |
| KSLC | 99854 | -1.67 | 3.41 | 4.26 |
| KSMF | 99714 | -1.92 | 2.94 | 3.65 |
| KTPA | 99706 | -3.44 | 3.85 | 4.54 |
| KTUS | 99870 | -1.88 | 3.29 | 4.23 |

## Cold mornings by station

| icao | n | bias_f | mae_f | rmse_f | min_observed_f |
| --- | --- | --- | --- | --- | --- |
| KABQ | 360 | 1.85 | 3.19 | 4.43 | 6.10 |
| KATL | 360 | -0.12 | 2.44 | 3.09 | 8.10 |
| KAVL | 356 | -0.42 | 4.03 | 6.06 | 0 |
| KBIL | 360 | 0.67 | 2.84 | 3.61 | -26 |
| KBNA | 360 | -0.36 | 3.37 | 4.16 | -0.90 |
| KBOI | 360 | 2.59 | 3.49 | 5 | 0 |
| KBOS | 390 | -2.29 | 3.01 | 4.02 | -9 |
| KCAE | 390 | 5.73 | 5.94 | 6.80 | 12.90 |
| KCHS | 390 | 2.21 | 3.26 | 3.80 | 18 |
| KCLT | 390 | 1.92 | 3.35 | 4.27 | 9 |
| KDEN | 360 | 1.81 | 4.29 | 5.32 | -22 |
| KDFW | 360 | 1.03 | 2.99 | 3.99 | -0.90 |
| KELP | 360 | 0.09 | 2.97 | 4.64 | 14 |
| KGEG | 314 | 2.82 | 4.13 | 5.13 | -9.90 |
| KIND | 360 | 0.28 | 2.82 | 3.50 | -9 |
| KJAX | 390 | 1.33 | 2.18 | 2.71 | 19.90 |
| KJFK | 385 | -2.86 | 3.18 | 3.88 | 5 |
| KLAS | 360 | -0.94 | 2.19 | 2.81 | 28 |
| KLAX | 360 | -3.20 | 3.44 | 4.05 | 39.90 |
| KMCO | 390 | -3.01 | 3.29 | 3.78 | 30 |
| KMGM | 352 | 2.48 | 3.10 | 4.11 | 15.10 |
| KMIA | 390 | -5.10 | 5.20 | 5.94 | 42.10 |
| KMWH | 346 | 3.63 | 4.66 | 6.32 | -9 |
| KOKC | 360 | 2.34 | 3.01 | 4.12 | -11 |
| KPDX | 360 | 2.98 | 4.51 | 5.98 | 18 |
| KPHL | 390 | -3.08 | 3.42 | 4.12 | 8.10 |
| KPHX | 360 | -5.03 | 5.04 | 5.42 | 36 |
| KRDU | 384 | 1.72 | 3.68 | 4.40 | 10 |
| KSDF | 360 | -2.42 | 3.68 | 5.18 | -5.10 |
| KSEA | 360 | 2.04 | 3.35 | 3.92 | 15.10 |
| KSGF | 360 | 1.63 | 2.45 | 3.13 | -14.10 |
| KSLC | 360 | -2.38 | 3.97 | 5.14 | 9 |
| KSMF | 356 | 1.69 | 2.68 | 3.51 | 27 |
| KTPA | 360 | -4.02 | 4.12 | 4.69 | 32 |
| KTUS | 360 | -0.73 | 2.68 | 3.36 | 25 |

## The four winter events

All hours of the local calendar days of each event (the dates of `grid_sentinel.events`), every lead from 17 to 45 h; the last row of each event pools every station.

| icao | event | n | bias_f | mae_f | rmse_f | min_observed_f |
| --- | --- | --- | --- | --- | --- | --- |
| KABQ | uri | 348 | 1.55 | 3.64 | 5.60 | 7 |
| KATL | uri | 348 | -2.54 | 3.54 | 4.29 | 23 |
| KAVL | uri | 348 | -0.93 | 2.42 | 3.11 | 19.90 |
| KBIL | uri | 348 | 1.89 | 3.35 | 4.15 | -20 |
| KBNA | uri | 348 | 1.37 | 2.53 | 2.90 | 10.90 |
| KBOI | uri | 348 | 1.24 | 2.31 | 3.28 | 17.10 |
| KBOS | uri | 348 | -0.16 | 2.43 | 2.98 | 17.10 |
| KCAE | uri | 348 | -1.23 | 2.39 | 3.70 | 28 |
| KCHS | uri | 348 | -0.27 | 4.55 | 6.62 | 34 |
| KCLT | uri | 348 | -1.75 | 2.25 | 3.53 | 30 |
| KDEN | uri | 348 | 4 | 5.32 | 6.93 | -16.10 |
| KDFW | uri | 348 | 0.03 | 2.15 | 2.79 | -0.90 |
| KELP | uri | 348 | 1.41 | 5.17 | 7.66 | 14 |
| KGEG | uri | 306 | 2.08 | 3.05 | 3.73 | 12 |
| KIND | uri | 348 | -0.32 | 2.02 | 2.54 | 1.90 |
| KJAX | uri | 348 | -0.87 | 4.66 | 5.96 | 42.10 |
| KJFK | uri | 348 | -1.08 | 2.18 | 2.79 | 24.10 |
| KLAS | uri | 348 | -2.68 | 4.39 | 5.26 | 42.10 |
| KLAX | uri | 348 | -0.64 | 3.10 | 3.64 | 48 |
| KMCO | uri | 348 | -4.19 | 4.48 | 5.81 | 60.10 |
| KMGM | uri | 231 | -0.63 | 2.89 | 3.90 | 19 |
| KMIA | uri | 348 | -4.41 | 4.41 | 4.71 | 72 |
| KMWH | uri | 346 | 3.01 | 4.31 | 6 | 10 |
| KOKC | uri | 348 | 1.75 | 2.80 | 3.70 | -11 |
| KPDX | uri | 348 | -0.44 | 3.59 | 4.49 | 25 |
| KPHL | uri | 348 | -1.30 | 2.48 | 3.11 | 24.10 |
| KPHX | uri | 348 | -2.98 | 3.90 | 4.71 | 44.10 |
| KRDU | uri | 348 | -0.90 | 2.54 | 3.87 | 28.90 |
| KSDF | uri | 348 | -1.38 | 2.15 | 2.84 | 10.90 |
| KSEA | uri | 348 | -0.75 | 2.85 | 3.45 | 25 |
| KSGF | uri | 348 | 1.34 | 2.83 | 3.69 | -14.10 |
| KSLC | uri | 348 | 0.48 | 2.37 | 3.17 | 21.90 |
| KSMF | uri | 348 | -1.12 | 2.47 | 3.13 | 34 |
| KTPA | uri | 348 | -4.90 | 5.05 | 5.74 | 55.90 |
| KTUS | uri | 348 | -3.16 | 3.50 | 4.24 | 37.90 |
| ALL | uri | 12019 | -0.54 | 3.26 | 4.43 | -20 |
| KABQ | elliott | 290 | 0.65 | 3.96 | 5.22 | 19 |
| KATL | elliott | 290 | -3.24 | 3.41 | 4.60 | 8.10 |
| KAVL | elliott | 290 | -3.34 | 3.75 | 4.71 | 0 |
| KBIL | elliott | 290 | -0.52 | 3.41 | 4.23 | -22 |
| KBNA | elliott | 290 | -4.45 | 4.70 | 6.06 | -0.90 |
| KBOI | elliott | 290 | 2.08 | 2.87 | 3.98 | 7 |
| KBOS | elliott | 290 | -3.08 | 3.24 | 3.91 | 10.90 |
| KCAE | elliott | 290 | 0.45 | 3.27 | 5.01 | 12.90 |
| KCHS | elliott | 290 | -0.39 | 3.43 | 4.49 | 18 |
| KCLT | elliott | 290 | -2.69 | 3.03 | 4.18 | 9 |
| KDEN | elliott | 290 | 1.55 | 5.51 | 6.74 | -22 |
| KDFW | elliott | 290 | -1.02 | 2.56 | 3.34 | 10.90 |
| KELP | elliott | 290 | -1.66 | 4.08 | 5.54 | 18 |
| KGEG | elliott | 254 | 4.90 | 5.66 | 7.18 | -9.90 |
| KIND | elliott | 290 | -2.75 | 3.15 | 3.95 | -9 |
| KJAX | elliott | 290 | -0.23 | 2.71 | 3.80 | 19.90 |
| KJFK | elliott | 290 | -2.12 | 3 | 3.75 | 7 |
| KLAS | elliott | 290 | 0.56 | 2.53 | 3.07 | 39.90 |
| KLAX | elliott | 290 | -2.82 | 4.03 | 4.61 | 48 |
| KMCO | elliott | 290 | -2.86 | 4 | 4.88 | 30 |
| KMGM | elliott | 290 | -1.35 | 3.19 | 4.46 | 16 |
| KMIA | elliott | 290 | -3.87 | 4.83 | 5.58 | 46 |
| KMWH | elliott | 288 | 3.58 | 3.86 | 4.90 | -5.10 |
| KOKC | elliott | 290 | 0.97 | 2.09 | 3.86 | 3 |
| KPDX | elliott | 290 | 7.54 | 7.67 | 8.95 | 19.90 |
| KPHL | elliott | 290 | -3.22 | 4.14 | 4.77 | 8.10 |
| KPHX | elliott | 290 | -2.29 | 4.09 | 4.48 | 41 |
| KRDU | elliott | 290 | -2.97 | 3.86 | 4.90 | 10 |
| KSDF | elliott | 290 | -4.86 | 5.06 | 5.58 | -5.10 |
| KSEA | elliott | 290 | 1.56 | 3.52 | 4.10 | 18 |
| KSGF | elliott | 290 | -3.05 | 3.44 | 4.36 | -8 |
| KSLC | elliott | 290 | -0.34 | 2.57 | 3.31 | 19 |
| KSMF | elliott | 290 | -1.50 | 2.62 | 3.26 | 37 |
| KTPA | elliott | 290 | -2.44 | 2.96 | 3.72 | 32 |
| KTUS | elliott | 290 | 0.36 | 2.37 | 3.19 | 36 |
| ALL | elliott | 10112 | -0.96 | 3.67 | 4.79 | -22 |
| KABQ | gerri_heather | 348 | 0.52 | 3.04 | 3.82 | 14 |
| KATL | gerri_heather | 348 | -3.51 | 4.32 | 5.50 | 14 |
| KAVL | gerri_heather | 348 | -1.39 | 3.89 | 5.11 | 10 |
| KBIL | gerri_heather | 348 | -0.96 | 2.73 | 3.61 | -26 |
| KBNA | gerri_heather | 348 | -2.52 | 3.28 | 4.41 | 0 |
| KBOI | gerri_heather | 348 | 2.69 | 5.64 | 6.83 | 3.90 |
| KBOS | gerri_heather | 348 | -2.05 | 3.20 | 4 | 19 |
| KCAE | gerri_heather | 348 | -1.01 | 3.59 | 4.58 | 25 |
| KCHS | gerri_heather | 348 | -3.48 | 4.09 | 5.24 | 30.90 |
| KCLT | gerri_heather | 348 | -1.21 | 4.80 | 5.87 | 18 |
| KDEN | gerri_heather | 348 | -1.04 | 4.06 | 5.44 | -16.10 |
| KDFW | gerri_heather | 348 | -0.45 | 2.82 | 4.10 | 10.90 |
| KELP | gerri_heather | 348 | -3.89 | 5.18 | 6.33 | 21 |
| KGEG | gerri_heather | 338 | 3.27 | 4.42 | 5.65 | -9.90 |
| KIND | gerri_heather | 348 | -1.93 | 3.70 | 4.60 | -5.10 |
| KJAX | gerri_heather | 348 | -1.33 | 3.32 | 4.63 | 30 |
| KJFK | gerri_heather | 348 | -2.12 | 2.97 | 4.02 | 18 |
| KLAS | gerri_heather | 348 | 0.83 | 2.82 | 3.81 | 32 |
| KLAX | gerri_heather | 348 | -1.66 | 2.58 | 3.16 | 42.10 |
| KMCO | gerri_heather | 348 | -3.34 | 4.01 | 5.01 | 45 |
| KMGM | gerri_heather | 348 | -1.52 | 3.24 | 4.28 | 15.10 |
| KMIA | gerri_heather | 348 | -4.72 | 4.83 | 6.05 | 64.90 |
| KMWH | gerri_heather | 348 | 1.72 | 2.91 | 3.70 | -5.10 |
| KOKC | gerri_heather | 348 | 2.25 | 2.92 | 3.80 | 1 |
| KPDX | gerri_heather | 348 | 3.83 | 4.90 | 6.52 | 15.10 |
| KPHL | gerri_heather | 348 | -2.41 | 3.18 | 4.29 | 14 |
| KPHX | gerri_heather | 348 | -3.38 | 4.46 | 5.06 | 36 |
| KRDU | gerri_heather | 348 | -3.04 | 4.24 | 5.61 | 19 |
| KSDF | gerri_heather | 348 | -2.63 | 3.94 | 5.19 | 6.10 |
| KSEA | gerri_heather | 346 | 2.83 | 3.36 | 4.20 | 15.10 |
| KSGF | gerri_heather | 348 | 0.04 | 2.98 | 3.71 | -5.10 |
| KSLC | gerri_heather | 348 | -3.20 | 4 | 5.53 | 12.20 |
| KSMF | gerri_heather | 348 | -1.86 | 2.47 | 2.90 | 37.90 |
| KTPA | gerri_heather | 348 | -2.71 | 3.50 | 4.36 | 43 |
| KTUS | gerri_heather | 348 | -0.88 | 2.39 | 2.87 | 28.90 |
| ALL | gerri_heather | 12168 | -1.15 | 3.65 | 4.78 | -26 |
| KABQ | january_2025 | 342 | -0.74 | 2.84 | 3.48 | 6.10 |
| KATL | january_2025 | 340 | -1.12 | 2.57 | 3.18 | 14 |
| KAVL | january_2025 | 348 | -2.33 | 3.58 | 4.15 | 10 |
| KBIL | january_2025 | 348 | 0.98 | 3.23 | 4.28 | -8 |
| KBNA | january_2025 | 348 | -3.12 | 3.60 | 4.35 | 8.10 |
| KBOI | january_2025 | 348 | -0.39 | 2.36 | 3.15 | 12.90 |
| KBOS | january_2025 | 346 | -2.82 | 2.91 | 3.51 | 10 |
| KCAE | january_2025 | 345 | 1.41 | 3.59 | 4.69 | 16 |
| KCHS | january_2025 | 343 | -1.12 | 3.07 | 3.82 | 23 |
| KCLT | january_2025 | 348 | -1 | 2.84 | 3.43 | 19 |
| KDEN | january_2025 | 348 | -0.18 | 4.16 | 5.11 | -11.90 |
| KDFW | january_2025 | 348 | -0.24 | 1.74 | 2.29 | 21 |
| KELP | january_2025 | 340 | -1.30 | 2.91 | 3.63 | 17.10 |
| KGEG | january_2025 | 343 | -0.91 | 2.19 | 2.66 | 12.90 |
| KIND | january_2025 | 348 | -1.27 | 2.44 | 3.18 | -2.90 |
| KJAX | january_2025 | 343 | -2.41 | 3.71 | 4.58 | 30 |
| KJFK | january_2025 | 338 | -4.30 | 4.40 | 5.04 | 14 |
| KLAS | january_2025 | 348 | -1.64 | 3.87 | 4.65 | 28.90 |
| KLAX | january_2025 | 348 | -4.97 | 5.38 | 6.52 | 43 |
| KMCO | january_2025 | 348 | -3.22 | 4.04 | 4.74 | 39 |
| KMGM | january_2025 | 348 | 1.38 | 2.75 | 3.65 | 15.10 |
| KMIA | january_2025 | 346 | -4.27 | 4.67 | 5.95 | 48.90 |
| KMWH | january_2025 | 343 | 0.35 | 2.75 | 3.60 | 15.10 |
| KOKC | january_2025 | 348 | 1.79 | 2.72 | 3.37 | 1.90 |
| KPDX | january_2025 | 348 | -0.35 | 3.54 | 4.16 | 26.10 |
| KPHL | january_2025 | 346 | -2.13 | 3.14 | 4.03 | 10 |
| KPHX | january_2025 | 348 | -4.41 | 5.52 | 6.69 | 37.90 |
| KRDU | january_2025 | 338 | -2.41 | 3.20 | 3.91 | 17.10 |
| KSDF | january_2025 | 348 | -3.48 | 3.73 | 4.89 | 3.90 |
| KSEA | january_2025 | 343 | 0.51 | 2.01 | 2.49 | 27 |
| KSGF | january_2025 | 348 | -0.79 | 2.49 | 3.09 | 1 |
| KSLC | january_2025 | 348 | -2.42 | 3.38 | 4.02 | 15.10 |
| KSMF | january_2025 | 348 | -1.78 | 2.39 | 3.03 | 30.90 |
| KTPA | january_2025 | 346 | -3.99 | 4.42 | 5.45 | 37.90 |
| KTUS | january_2025 | 348 | -1.70 | 3.65 | 4.63 | 25 |
| ALL | january_2025 | 12102 | -1.55 | 3.31 | 4.23 | -11.90 |

Tables as CSV, including the error by lead and by local hour, are in `results/hrrr_verification/`.
