# HRRR 2 m temperature against ISD-Lite observations

Forecast minus observed at the grid cell of each station (the NBM 2 m temperature, whole degrees Fahrenheit, from the public archive; leads beyond 36 h interpolated from the three-hourly files), 2021, 2022, 2023, 2024, 2025, leads 17 to 45 h of the 12 and 06 UTC runs (the leads a day-ahead forecast issued at 9 a.m. local time uses). 2511356 forecast-observation pairs at 35 stations. Observations are hourly ISD-Lite readings; a station reports to the nearest tenth of a degree Celsius.

Overall: bias -0.21 °F, MAE 2.05 °F, RMSE 2.75 °F.

On the 30 coldest mornings of each station (lowest observed minimum between 04:00 and 09:00 local time), hours 04:00 to 09:00: bias +1.24 °F, MAE 2.40 °F, 12521 pairs. A positive bias means the forecast was warmer than what occurred.

![MAE by lead](figures/hrrr_mae_by_lead.png)

![Bias on cold mornings by station](figures/hrrr_cold_morning_bias.png)

## By observed temperature

| bin | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| below 20 F | 31454 | 2.14 | 3.09 | 4.15 |
| 20 to 32 F | 133933 | 0.70 | 2.24 | 2.99 |
| 32 to 59 F | 954630 | -0.10 | 2.15 | 2.84 |
| 59 to 72 F | 634978 | -0.27 | 2.02 | 2.72 |
| above 72 F | 756361 | -0.53 | 1.86 | 2.54 |

## By month

| month | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| 1 | 222311 | -0.40 | 2.21 | 2.89 |
| 2 | 219749 | -0.23 | 2.35 | 3.21 |
| 3 | 243793 | -0.39 | 2.18 | 2.88 |
| 4 | 232088 | -0.21 | 2 | 2.68 |
| 5 | 244649 | 0 | 1.91 | 2.61 |
| 6 | 234941 | 0.03 | 1.90 | 2.63 |
| 7 | 193932 | 0.08 | 1.92 | 2.68 |
| 8 | 189047 | -0.04 | 1.92 | 2.64 |
| 9 | 179828 | -0.36 | 1.87 | 2.46 |
| 10 | 176806 | -0.32 | 1.91 | 2.49 |
| 11 | 184066 | -0.43 | 2.10 | 2.74 |
| 12 | 190146 | -0.24 | 2.24 | 2.95 |

## By station

| icao | n | bias_f | mae_f | rmse_f |
| --- | --- | --- | --- | --- |
| KABQ | 71868 | -0.06 | 2.09 | 2.79 |
| KATL | 71812 | -0.65 | 2.06 | 2.72 |
| KAVL | 71643 | -0.43 | 2.31 | 2.97 |
| KBIL | 71858 | -0.19 | 2.55 | 3.32 |
| KBNA | 71891 | -0.13 | 2.10 | 2.80 |
| KBOI | 71804 | -0.04 | 1.98 | 2.64 |
| KBOS | 71871 | -0.37 | 2.11 | 2.82 |
| KCAE | 71693 | 0.01 | 2.30 | 3.01 |
| KCHS | 71864 | 0.06 | 1.94 | 2.60 |
| KCLT | 71765 | -0.11 | 2.01 | 2.69 |
| KDEN | 71882 | 0.08 | 2.97 | 3.96 |
| KDFW | 71868 | -0.01 | 2.04 | 2.90 |
| KELP | 71889 | -0.18 | 2.31 | 3.13 |
| KGEG | 70486 | -0.12 | 1.80 | 2.39 |
| KIND | 71884 | -0.03 | 1.88 | 2.51 |
| KJAX | 71862 | 0.54 | 2.17 | 2.88 |
| KJFK | 71849 | 0.07 | 1.85 | 2.43 |
| KLAS | 71817 | -0.06 | 1.65 | 2.24 |
| KLAX | 71873 | -0.05 | 1.53 | 2.09 |
| KMCO | 71768 | -0.44 | 1.80 | 2.44 |
| KMGM | 71407 | -0.52 | 2.15 | 2.82 |
| KMIA | 71856 | -0.36 | 1.58 | 2.14 |
| KMWH | 71554 | -0.43 | 2.46 | 3.15 |
| KOKC | 71836 | 0.41 | 2.32 | 3.16 |
| KPDX | 71847 | -0.10 | 1.90 | 2.50 |
| KPHL | 71829 | -0.81 | 2.10 | 2.73 |
| KPHX | 71794 | -0.18 | 1.64 | 2.27 |
| KRDU | 71820 | -0.40 | 2.14 | 2.79 |
| KSDF | 71822 | -0.57 | 2.18 | 2.88 |
| KSEA | 71825 | -0.03 | 1.61 | 2.15 |
| KSGF | 71630 | -0.10 | 2.13 | 2.86 |
| KSLC | 71769 | -0.50 | 2.20 | 2.90 |
| KSMF | 71658 | -0.69 | 2.08 | 2.65 |
| KTPA | 71658 | -0.11 | 1.51 | 2.07 |
| KTUS | 71804 | -0.69 | 2.17 | 2.95 |

## Cold mornings by station

| icao | n | bias_f | mae_f | rmse_f | min_observed_f |
| --- | --- | --- | --- | --- | --- |
| KABQ | 360 | 3.28 | 3.68 | 5.35 | 6.10 |
| KATL | 348 | 0.08 | 1.48 | 1.82 | 8.10 |
| KAVL | 334 | 0.58 | 2.68 | 4.14 | 0 |
| KBIL | 354 | 1.21 | 2.88 | 3.70 | -26 |
| KBNA | 354 | 1.50 | 1.91 | 2.38 | -0.90 |
| KBOI | 342 | 1.27 | 2.84 | 3.68 | 0 |
| KBOS | 377 | 1.06 | 2.17 | 2.64 | -9 |
| KCAE | 375 | 2.11 | 2.59 | 3.09 | 12.90 |
| KCHS | 382 | 1.29 | 2.31 | 2.89 | 18 |
| KCLT | 377 | 0.73 | 1.67 | 2.07 | 9 |
| KDEN | 354 | 5.46 | 5.77 | 6.54 | -22 |
| KDFW | 354 | 1.74 | 2.74 | 3.38 | -0.90 |
| KELP | 360 | 4.26 | 4.56 | 5.82 | 14 |
| KGEG | 316 | 0.66 | 3.22 | 4.07 | -9.90 |
| KIND | 354 | 2.02 | 2.37 | 2.95 | -9 |
| KJAX | 371 | 2.17 | 2.90 | 3.43 | 19.90 |
| KJFK | 378 | 1.45 | 1.95 | 2.42 | 5 |
| KLAS | 348 | 1.54 | 1.76 | 2.09 | 28 |
| KLAX | 342 | 0.99 | 1.48 | 1.89 | 39.90 |
| KMCO | 383 | -0.08 | 1.86 | 2.20 | 30 |
| KMGM | 340 | 0.58 | 1.68 | 2.11 | 15.10 |
| KMIA | 382 | -0.47 | 2.16 | 2.63 | 42.10 |
| KMWH | 346 | 2.77 | 3.88 | 4.96 | -9 |
| KOKC | 354 | 1.62 | 2.39 | 2.95 | -11 |
| KPDX | 354 | 1.21 | 3.10 | 3.78 | 18 |
| KPHL | 377 | -0.76 | 1.63 | 2.02 | 8.10 |
| KPHX | 354 | -0.18 | 1.18 | 1.56 | 36 |
| KRDU | 371 | 0.44 | 1.44 | 1.88 | 10 |
| KSDF | 354 | 0.13 | 2.08 | 2.57 | -5.10 |
| KSEA | 360 | 0.17 | 1.53 | 1.89 | 15.10 |
| KSGF | 354 | 1.93 | 2.42 | 3.05 | -14.10 |
| KSLC | 348 | 0.56 | 1.80 | 2.46 | 9 |
| KSMF | 356 | 1.01 | 2.26 | 2.76 | 27 |
| KTPA | 348 | 0.48 | 1.39 | 1.76 | 32 |
| KTUS | 360 | 0.78 | 2.40 | 3.10 | 25 |

## The four winter events

All hours of the local calendar days of each event (the dates of `grid_sentinel.events`), every lead from 17 to 45 h; the last row of each event pools every station.

| icao | event | n | bias_f | mae_f | rmse_f | min_observed_f |
| --- | --- | --- | --- | --- | --- | --- |
| KABQ | uri | 254 | 2.80 | 4.21 | 6.12 | 7 |
| KATL | uri | 255 | 0.49 | 2.15 | 2.74 | 23 |
| KAVL | uri | 255 | 0.30 | 2.07 | 2.61 | 19.90 |
| KBIL | uri | 254 | 0.92 | 2.46 | 3.02 | -20 |
| KBNA | uri | 255 | 3.33 | 3.37 | 3.91 | 10.90 |
| KBOI | uri | 254 | 1.19 | 2.52 | 3.30 | 17.10 |
| KBOS | uri | 255 | 1.28 | 2.07 | 2.79 | 17.10 |
| KCAE | uri | 255 | 1.54 | 2.27 | 2.96 | 28 |
| KCHS | uri | 255 | 2.43 | 4.29 | 5.38 | 34 |
| KCLT | uri | 255 | 1.57 | 2.48 | 3.29 | 30 |
| KDEN | uri | 254 | 3.92 | 4.74 | 6.10 | -16.10 |
| KDFW | uri | 255 | 1.37 | 2.21 | 2.90 | -0.90 |
| KELP | uri | 254 | 4.79 | 5.57 | 7.68 | 14 |
| KGEG | uri | 226 | 1.46 | 2.93 | 3.43 | 12 |
| KIND | uri | 255 | 0.38 | 1.94 | 2.28 | 1.90 |
| KJAX | uri | 255 | 2.37 | 4.34 | 5.13 | 42.10 |
| KJFK | uri | 255 | -0.33 | 1.50 | 1.92 | 24.10 |
| KLAS | uri | 254 | -1.14 | 1.85 | 2.66 | 42.10 |
| KLAX | uri | 254 | -1.09 | 1.96 | 2.58 | 48 |
| KMCO | uri | 255 | -0.92 | 2.55 | 3.44 | 60.10 |
| KMGM | uri | 162 | 1.06 | 2.54 | 3.09 | 19 |
| KMIA | uri | 255 | -1.83 | 1.96 | 2.16 | 72 |
| KMWH | uri | 252 | 1.58 | 2.80 | 4.08 | 10 |
| KOKC | uri | 254 | 1.28 | 2.10 | 2.49 | -11 |
| KPDX | uri | 254 | 2.08 | 3.04 | 3.90 | 25 |
| KPHL | uri | 255 | -0.13 | 1.84 | 2.26 | 24.10 |
| KPHX | uri | 254 | -0.66 | 1.27 | 1.72 | 44.10 |
| KRDU | uri | 255 | 0.62 | 2.36 | 3.16 | 28.90 |
| KSDF | uri | 255 | 0.18 | 2.05 | 2.67 | 10.90 |
| KSEA | uri | 254 | 0.40 | 1.80 | 2.18 | 25 |
| KSGF | uri | 255 | 1.70 | 2.35 | 2.96 | -14.10 |
| KSLC | uri | 254 | 0.14 | 2.07 | 2.63 | 21.90 |
| KSMF | uri | 254 | -1.70 | 2.16 | 2.71 | 34 |
| KTPA | uri | 255 | -0.25 | 1.77 | 2.24 | 55.90 |
| KTUS | uri | 254 | -2.54 | 2.75 | 3.35 | 37.90 |
| ALL | uri | 8786 | 0.81 | 2.58 | 3.56 | -20 |
| KABQ | elliott | 230 | 0.69 | 3.66 | 4.55 | 19 |
| KATL | elliott | 230 | -0.83 | 1.91 | 2.57 | 8.10 |
| KAVL | elliott | 230 | -0.64 | 2.01 | 2.71 | 0 |
| KBIL | elliott | 230 | -2.65 | 3.68 | 4.21 | -22 |
| KBNA | elliott | 230 | 1.15 | 2.45 | 3.31 | -0.90 |
| KBOI | elliott | 230 | 3.11 | 4.65 | 5.15 | 7 |
| KBOS | elliott | 230 | 1.03 | 1.76 | 2.27 | 10.90 |
| KCAE | elliott | 230 | 0.81 | 2.09 | 2.79 | 12.90 |
| KCHS | elliott | 230 | 0.12 | 2.71 | 3.54 | 18 |
| KCLT | elliott | 230 | 0.03 | 1.63 | 2.41 | 9 |
| KDEN | elliott | 230 | 0.94 | 4.22 | 4.95 | -22 |
| KDFW | elliott | 230 | -0.19 | 2.54 | 3.32 | 10.90 |
| KELP | elliott | 230 | 1.36 | 5.04 | 5.92 | 18 |
| KGEG | elliott | 204 | 3.56 | 4.41 | 5.42 | -9.90 |
| KIND | elliott | 230 | 0.67 | 2.66 | 3.83 | -9 |
| KJAX | elliott | 230 | 0.56 | 2.65 | 3.40 | 19.90 |
| KJFK | elliott | 230 | 1.79 | 2.34 | 2.86 | 7 |
| KLAS | elliott | 230 | 0.55 | 1.30 | 1.59 | 39.90 |
| KLAX | elliott | 230 | 0.21 | 1.54 | 2 | 48 |
| KMCO | elliott | 230 | -0.28 | 2.20 | 2.89 | 30 |
| KMGM | elliott | 230 | -1.83 | 2.27 | 2.96 | 16 |
| KMIA | elliott | 230 | 0.55 | 2.44 | 3.03 | 46 |
| KMWH | elliott | 229 | 2.71 | 3.47 | 4.10 | -5.10 |
| KOKC | elliott | 230 | -0.15 | 2.56 | 3.50 | 3 |
| KPDX | elliott | 230 | 7.57 | 7.96 | 9.11 | 19.90 |
| KPHL | elliott | 230 | -0.19 | 1.71 | 2.13 | 8.10 |
| KPHX | elliott | 230 | -0.07 | 1.24 | 1.55 | 41 |
| KRDU | elliott | 230 | -1.48 | 2.31 | 2.86 | 10 |
| KSDF | elliott | 230 | -0.90 | 2.72 | 3.13 | -5.10 |
| KSEA | elliott | 230 | 0.14 | 1.79 | 2.30 | 18 |
| KSGF | elliott | 230 | -0.40 | 2.71 | 3.27 | -8 |
| KSLC | elliott | 230 | 1.54 | 2.35 | 2.77 | 19 |
| KSMF | elliott | 230 | 0.66 | 2.23 | 2.82 | 37 |
| KTPA | elliott | 230 | 1.17 | 1.95 | 2.58 | 32 |
| KTUS | elliott | 230 | 0.68 | 1.99 | 2.46 | 36 |
| ALL | elliott | 8023 | 0.62 | 2.71 | 3.66 | -22 |
| KABQ | gerri_heather | 244 | -1.12 | 3.84 | 4.78 | 14 |
| KATL | gerri_heather | 247 | -0.81 | 3.29 | 4.03 | 14 |
| KAVL | gerri_heather | 247 | 0.34 | 3.45 | 4.21 | 10 |
| KBIL | gerri_heather | 244 | 1.53 | 2.73 | 3.56 | -26 |
| KBNA | gerri_heather | 247 | 0.63 | 2.75 | 3.56 | 0 |
| KBOI | gerri_heather | 242 | 1.90 | 4.10 | 5.14 | 3.90 |
| KBOS | gerri_heather | 249 | 0.43 | 2.26 | 2.89 | 19 |
| KCAE | gerri_heather | 249 | -0.61 | 2.91 | 3.43 | 25 |
| KCHS | gerri_heather | 249 | -1.73 | 3.10 | 3.68 | 30.90 |
| KCLT | gerri_heather | 249 | -0.04 | 3.29 | 4.12 | 18 |
| KDEN | gerri_heather | 244 | 2.57 | 4.76 | 5.51 | -16.10 |
| KDFW | gerri_heather | 247 | 2.79 | 3.74 | 4.79 | 10.90 |
| KELP | gerri_heather | 244 | -1.68 | 4.80 | 5.63 | 21 |
| KGEG | gerri_heather | 239 | 0.55 | 2.46 | 3.23 | -9.90 |
| KIND | gerri_heather | 247 | 2.56 | 3.17 | 3.75 | -5.10 |
| KJAX | gerri_heather | 249 | -1.37 | 3.22 | 4.28 | 30 |
| KJFK | gerri_heather | 249 | 0.19 | 2.02 | 2.46 | 18 |
| KLAS | gerri_heather | 242 | 1.67 | 1.82 | 2.22 | 32 |
| KLAX | gerri_heather | 242 | 0.86 | 1.17 | 1.53 | 42.10 |
| KMCO | gerri_heather | 249 | -0.81 | 2 | 2.69 | 45 |
| KMGM | gerri_heather | 247 | -0.62 | 2.90 | 3.76 | 15.10 |
| KMIA | gerri_heather | 249 | -0.47 | 1.61 | 2.19 | 64.90 |
| KMWH | gerri_heather | 242 | 2.41 | 2.60 | 3.10 | -5.10 |
| KOKC | gerri_heather | 244 | 2.46 | 2.69 | 3.32 | 1 |
| KPDX | gerri_heather | 242 | 0.92 | 2.82 | 3.82 | 15.10 |
| KPHL | gerri_heather | 249 | -0.28 | 2.14 | 2.62 | 14 |
| KPHX | gerri_heather | 244 | 0.26 | 1.06 | 1.40 | 36 |
| KRDU | gerri_heather | 249 | -0.65 | 2.66 | 3.35 | 19 |
| KSDF | gerri_heather | 247 | 1.66 | 2.44 | 3.05 | 6.10 |
| KSEA | gerri_heather | 241 | 0.31 | 1.49 | 1.88 | 15.10 |
| KSGF | gerri_heather | 247 | 2.44 | 2.73 | 3.19 | -5.10 |
| KSLC | gerri_heather | 244 | -1.63 | 2.78 | 3.35 | 12.20 |
| KSMF | gerri_heather | 242 | -0.92 | 1.95 | 2.42 | 37.90 |
| KTPA | gerri_heather | 247 | 0.42 | 1.45 | 1.91 | 43 |
| KTUS | gerri_heather | 244 | 0.73 | 1.70 | 2.07 | 28.90 |
| ALL | gerri_heather | 8597 | 0.42 | 2.68 | 3.50 | -26 |
| KABQ | january_2025 | 271 | 1.13 | 2.14 | 2.72 | 6.10 |
| KATL | january_2025 | 269 | 0.36 | 1.87 | 2.53 | 14 |
| KAVL | january_2025 | 276 | 0.07 | 2.06 | 2.67 | 10 |
| KBIL | january_2025 | 276 | 0.03 | 1.90 | 2.38 | -8 |
| KBNA | january_2025 | 276 | -0.27 | 1.52 | 2.01 | 8.10 |
| KBOI | january_2025 | 276 | 0.27 | 1.96 | 2.54 | 12.90 |
| KBOS | january_2025 | 275 | -0.48 | 1.09 | 1.49 | 10 |
| KCAE | january_2025 | 275 | -0.04 | 2.18 | 2.91 | 16 |
| KCHS | january_2025 | 272 | -0.93 | 2.18 | 2.68 | 23 |
| KCLT | january_2025 | 276 | 0.06 | 1.74 | 2.38 | 19 |
| KDEN | january_2025 | 276 | -0.44 | 4.10 | 5.08 | -11.90 |
| KDFW | january_2025 | 276 | 1 | 1.80 | 2.17 | 21 |
| KELP | january_2025 | 269 | 3.01 | 3.24 | 3.95 | 17.10 |
| KGEG | january_2025 | 271 | -0.51 | 2.06 | 2.58 | 12.90 |
| KIND | january_2025 | 276 | 0.24 | 1.83 | 2.18 | -2.90 |
| KJAX | january_2025 | 272 | -1.03 | 2.75 | 3.33 | 30 |
| KJFK | january_2025 | 268 | -0.14 | 1.18 | 1.47 | 14 |
| KLAS | january_2025 | 276 | 0.90 | 1.50 | 1.84 | 28.90 |
| KLAX | january_2025 | 276 | -2.52 | 2.95 | 3.61 | 43 |
| KMCO | january_2025 | 276 | 0.84 | 2.60 | 3.22 | 39 |
| KMGM | january_2025 | 276 | -0.64 | 2.35 | 2.96 | 15.10 |
| KMIA | january_2025 | 274 | 2.42 | 3.80 | 4.57 | 48.90 |
| KMWH | january_2025 | 271 | 0.49 | 2.82 | 3.36 | 15.10 |
| KOKC | january_2025 | 276 | 1.31 | 2.22 | 2.68 | 1.90 |
| KPDX | january_2025 | 276 | -0.18 | 3.04 | 3.55 | 26.10 |
| KPHL | january_2025 | 274 | -0.32 | 1.52 | 1.98 | 10 |
| KPHX | january_2025 | 276 | -0.41 | 1.85 | 2.46 | 37.90 |
| KRDU | january_2025 | 268 | -0.76 | 2.09 | 2.57 | 17.10 |
| KSDF | january_2025 | 276 | -0.24 | 1.88 | 2.32 | 3.90 |
| KSEA | january_2025 | 271 | -0.48 | 1.74 | 2.16 | 27 |
| KSGF | january_2025 | 276 | 0.97 | 2.19 | 2.69 | 1 |
| KSLC | january_2025 | 276 | -0.56 | 1.71 | 2.08 | 15.10 |
| KSMF | january_2025 | 276 | 0.80 | 1.94 | 2.41 | 30.90 |
| KTPA | january_2025 | 275 | 0.59 | 2.45 | 2.94 | 37.90 |
| KTUS | january_2025 | 276 | -0.35 | 2.77 | 3.52 | 25 |
| ALL | january_2025 | 9595 | 0.12 | 2.20 | 2.85 | -11.90 |

Tables as CSV, including the error by lead and by local hour, are in `results/hrrr_verification/`.
