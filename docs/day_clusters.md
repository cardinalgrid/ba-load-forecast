# Daily load shapes grouped by similarity

For each BA, every complete day from 2018-01-01 to 2022-12-31 (gross faults removed) is a shape: 24 hourly values divided by the day's mean. Days are first split by temperature regime (heating below 59 F, cooling above 72 F, mild between, by the observed daily mean), because across regimes the shape is the season: a heating day peaks in the morning, a cooling day in the afternoon. Within each regime k-means groups the shapes, k being the value between 2 and 5 with the best silhouette (the silhouette shown is the mean over regimes). The groups are crossed with the calendar day type (workday, Saturday, Sunday; holidays as the type they resemble in the Note 2 table). The classifier is the most frequent cluster of each (day type, regime) cell; its accuracy is the share of days whose cluster it names correctly. Distances are to the nearest centroid of the day's regime; the largest ones are the most atypical days.
| ba | k | silhouette | n_days | classifier_accuracy |
| --- | --- | --- | --- | --- |
| PJM | 7 | 0.33 | 1815 | 0.57 |
| MISO | 8 | 0.33 | 1815 | 0.59 |
| ERCO | 6 | 0.38 | 1817 | 0.65 |
| CISO | 7 | 0.34 | 1796 | 0.64 |
| SWPP | 6 | 0.39 | 1719 | 0.61 |
| NYIS | 7 | 0.32 | 1820 | 0.83 |
| ISNE | 6 | 0.28 | 1821 | 0.62 |
| TVA | 7 | 0.41 | 1782 | 0.59 |
| DUK | 6 | 0.37 | 1821 | 0.59 |
| BPAT | 6 | 0.33 | 1821 | 0.61 |


## PJM

k = 7, silhouette 0.329, 1815 days, classifier accuracy 0.575.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 18 | 1.09 | 0.88 | 503 |
| 1 | heating | 7 | 1.08 | 0.94 | 429 |
| 2 | heating | 14 | 3.67 | 0.76 | 1 |
| 3 | mild | 19 | 1.08 | 0.86 | 211 |
| 4 | mild | 17 | 1.16 | 0.82 | 163 |
| 5 | cooling | 17 | 1.23 | 0.77 | 246 |
| 6 | cooling | 16 | 1.18 | 0.81 | 262 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 337 | 0 | 0 | 78 | 0 | 0 | 88 | 0 | 0 |
| 1 | 291 | 0 | 0 | 86 | 0 | 0 | 52 | 0 | 0 |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 163 | 0 | 0 | 32 | 0 | 0 | 16 | 0 |
| 4 | 0 | 113 | 0 | 0 | 24 | 0 | 0 | 26 | 0 |
| 5 | 0 | 0 | 148 | 0 | 0 | 30 | 0 | 0 | 68 |
| 6 | 0 | 0 | 208 | 0 | 0 | 36 | 0 | 0 | 18 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 0 | workday | 0 | 0.21 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 0 | 0.15 |
| 2018-05-28 | Memorial Day | 4 | sunday | 0 | workday | 0 | 0.18 |
| 2018-07-04 | Independence Day | 6 | sunday | 0 | workday | 0 | 0.18 |
| 2018-09-03 | Labor Day | 5 | sunday | 0 | workday | 0 | 0.13 |
| 2018-11-22 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2018-11-23 | Day after Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.08 |
| 2018-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.10 |
| 2018-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.15 |
| 2018-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.21 |
| 2019-01-01 | New Year's Day | 0 | sunday | 0 | workday | 0 | 0.26 |
| 2019-02-03 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 0 | 0.18 |
| 2019-05-27 | Memorial Day | 5 | sunday | 0 | workday | 0 | 0.17 |
| 2019-07-04 | Independence Day | 6 | sunday | 0 | workday | 0 | 0.17 |
| 2019-09-02 | Labor Day | 5 | sunday | 0 | workday | 0 | 0.09 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.16 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.10 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.10 |
| 2019-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.16 |
| 2019-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.08 |
| 2020-01-01 | New Year's Day | 0 | sunday | 0 | workday | 0 | 0.20 |
| 2020-02-02 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 0 | 0.12 |
| 2020-05-25 | Memorial Day | 4 | sunday | 0 | workday | 0 | 0.19 |
| 2020-07-03 | observed holiday | 5 | sunday | 0 | workday | 0 | 0.14 |
| 2020-07-04 | Independence Day | 5 | sunday | 0 | saturday | 1 | 0.15 |
| 2020-09-07 | Labor Day | 5 | sunday | 0 | workday | 0 | 0.11 |
| 2020-11-26 | Thanksgiving | 3 | saturday | 1 | workday | 0 | 0.20 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.11 |
| 2020-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.12 |
| 2020-12-25 | Christmas Day | 0 | saturday | 1 | workday | 0 | 0.27 |
| 2020-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.10 |
| 2021-01-01 | New Year's Day | 0 | sunday | 0 | workday | 0 | 0.16 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 0 | 0.13 |
| 2021-05-31 | Memorial Day | 3 | sunday | 0 | workday | 0 | 0.21 |
| 2021-07-04 | Independence Day | 4 | sunday | 0 | sunday | 0 | 0.36 |
| 2021-07-05 | observed holiday | 5 | sunday | 0 | workday | 0 | 0.27 |
| 2021-09-06 | Labor Day | 5 | sunday | 0 | workday | 0 | 0.14 |
| 2021-11-25 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.19 |
| 2021-11-26 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.17 |
| 2021-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.15 |
| 2021-12-25 | Christmas Day | 1 | saturday | 1 | saturday | 1 | 0.16 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 0 | workday | 0 | 0.12 |
| 2022-01-01 | New Year's Day | 0 | sunday | 0 | saturday | 1 | 0.19 |
| 2022-02-13 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 0 | 0.14 |
| 2022-05-30 | Memorial Day | 5 | sunday | 0 | workday | 0 | 0.25 |
| 2022-07-04 | Independence Day | 5 | sunday | 0 | workday | 0 | 0.13 |
| 2022-09-05 | Labor Day | 6 | sunday | 0 | workday | 0 | 0.13 |
| 2022-11-24 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.21 |
| 2022-11-25 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.10 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 1 | saturday | 1 | 0.15 |
| 2022-12-25 | Christmas Day | 1 | saturday | 1 | sunday | 0 | 0.22 |
| 2022-12-26 | observed holiday | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2022-12-31 | New Year's Eve | 0 | saturday | 1 | saturday | 1 | 0.16 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 824 | 2020-04-09 | 0 | 1.85 | 0 | 0 | 77790 |
| 930 | 2020-07-24 | 6 | 1.26 | 0 | 2 | 114047 |
| 970 | 2020-09-03 | 5 | 1.08 | 0 | 2 | 110780 |
| 919 | 2020-07-13 | 5 | 0.89 | 0 | 2 | 107818 |
| 933 | 2020-07-27 | 5 | 0.78 | 0 | 2 | 123867 |
| 179 | 2018-06-30 | 6 | 0.78 | 1 | 2 | 113902 |
| 934 | 2020-07-28 | 6 | 0.51 | 0 | 2 | 120549 |
| 706 | 2019-12-12 | 0 | 0.51 | 0 | 0 | 104573 |
| 1806 | 2022-12-23 | 0 | 0.46 | 0 | 0 | 112989 |
| 382 | 2019-01-20 | 0 | 0.38 | 2 | 0 | 98348 |
| 1273 | 2021-07-04 | 4 | 0.36 | 2 | 1 | 87732 |
| 1354 | 2021-09-23 | 6 | 0.35 | 0 | 2 | 86626 |
| 949 | 2020-08-13 | 6 | 0.34 | 0 | 2 | 109772 |
| 1564 | 2022-04-24 | 0 | 0.33 | 2 | 0 | 74469 |
| 884 | 2020-06-08 | 4 | 0.30 | 0 | 1 | 88596 |
| 147 | 2018-05-29 | 4 | 0.30 | 0 | 1 | 102526 |
| 1181 | 2021-04-03 | 1 | 0.30 | 1 | 0 | 79078 |
| 847 | 2020-05-02 | 3 | 0.30 | 1 | 1 | 65749 |
| 1167 | 2021-03-20 | 1 | 0.29 | 1 | 0 | 81735 |
| 935 | 2020-07-29 | 5 | 0.29 | 0 | 2 | 117076 |

## MISO

k = 8, silhouette 0.325, 1815 days, classifier accuracy 0.590.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 19 | 1.08 | 0.88 | 581 |
| 1 | heating | 8 | 1.07 | 0.93 | 428 |
| 2 | mild | 16 | 1.16 | 0.82 | 191 |
| 3 | mild | 16 | 1.09 | 0.85 | 145 |
| 4 | cooling | 16 | 1.17 | 0.83 | 80 |
| 5 | cooling | 15 | 1.16 | 0.82 | 126 |
| 6 | cooling | 16 | 1.20 | 0.78 | 192 |
| 7 | cooling | 17 | 1.21 | 0.79 | 72 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 409 | 0 | 0 | 76 | 0 | 0 | 96 | 0 | 0 |
| 1 | 283 | 0 | 0 | 97 | 0 | 0 | 48 | 0 | 0 |
| 2 | 0 | 121 | 0 | 0 | 29 | 0 | 0 | 41 | 0 |
| 3 | 0 | 120 | 0 | 0 | 16 | 0 | 0 | 9 | 0 |
| 4 | 0 | 0 | 7 | 0 | 0 | 40 | 0 | 0 | 33 |
| 5 | 0 | 0 | 120 | 0 | 0 | 6 | 0 | 0 | 0 |
| 6 | 0 | 0 | 190 | 0 | 0 | 1 | 0 | 0 | 1 |
| 7 | 0 | 0 | 7 | 0 | 0 | 17 | 0 | 0 | 48 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 0 | workday | 0 | 0.18 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 0 | 0.19 |
| 2018-05-28 | Memorial Day | 7 | sunday | 0 | workday | 0 | 0.14 |
| 2018-07-04 | Independence Day | 7 | sunday | 0 | workday | 0 | 0.12 |
| 2018-09-03 | Labor Day | 4 | sunday | 0 | workday | 0 | 0.07 |
| 2018-11-22 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.19 |
| 2018-11-23 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.09 |
| 2018-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.07 |
| 2018-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2018-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.09 |
| 2019-01-01 | New Year's Day | 0 | sunday | 0 | workday | 0 | 0.18 |
| 2019-02-03 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 0 | 0.16 |
| 2019-05-27 | Memorial Day | 4 | sunday | 0 | workday | 0 | 0.08 |
| 2019-07-04 | Independence Day | 7 | sunday | 0 | workday | 0 | 0.11 |
| 2019-09-02 | Labor Day | 2 | sunday | 0 | workday | 0 | 0.20 |
| 2019-11-28 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.16 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.07 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.10 |
| 2019-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.10 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 0 | 0.07 |
| 2020-01-01 | New Year's Day | 1 | sunday | 0 | workday | 0 | 0.17 |
| 2020-02-02 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 0 | 0.12 |
| 2020-05-25 | Memorial Day | 7 | sunday | 0 | workday | 0 | 0.04 |
| 2020-07-03 | observed holiday | 6 | sunday | 0 | workday | 0 | 0.11 |
| 2020-07-04 | Independence Day | 7 | sunday | 0 | saturday | 1 | 0.11 |
| 2020-09-07 | Labor Day | 7 | sunday | 0 | workday | 0 | 0.08 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.20 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.12 |
| 2020-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.14 |
| 2020-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.14 |
| 2020-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.08 |
| 2021-01-01 | New Year's Day | 0 | sunday | 0 | workday | 0 | 0.18 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 0 | 0.13 |
| 2021-05-31 | Memorial Day | 2 | sunday | 0 | workday | 0 | 0.14 |
| 2021-07-04 | Independence Day | 7 | sunday | 0 | sunday | 0 | 0.10 |
| 2021-07-05 | observed holiday | 7 | sunday | 0 | workday | 0 | 0.11 |
| 2021-09-06 | Labor Day | 2 | sunday | 0 | workday | 0 | 0.21 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.16 |
| 2021-11-26 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.11 |
| 2021-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.16 |
| 2021-12-25 | Christmas Day | 0 | saturday | 1 | saturday | 1 | 0.16 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 0 | workday | 0 | 0.17 |
| 2022-01-01 | New Year's Day | 0 | sunday | 0 | saturday | 1 | 0.21 |
| 2022-02-13 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 0 | 0.13 |
| 2022-05-30 | Memorial Day | 7 | sunday | 0 | workday | 0 | 0.08 |
| 2022-07-04 | Independence Day | 7 | sunday | 0 | workday | 0 | 0.06 |
| 2022-09-05 | Labor Day | 4 | sunday | 0 | workday | 0 | 0.09 |
| 2022-11-24 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.17 |
| 2022-11-25 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.13 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 1 | saturday | 1 | 0.22 |
| 2022-12-25 | Christmas Day | 1 | saturday | 1 | sunday | 0 | 0.22 |
| 2022-12-26 | observed holiday | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2022-12-31 | New Year's Eve | 0 | saturday | 1 | saturday | 1 | 0.17 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 262 | 2018-09-21 | 5 | 0.29 | 0 | 2 | 79967 |
| 1182 | 2021-04-04 | 3 | 0.29 | 2 | 1 | 57008 |
| 1523 | 2022-03-13 | 1 | 0.29 | 2 | 0 | 69241 |
| 1139 | 2021-02-20 | 1 | 0.28 | 1 | 0 | 77434 |
| 1592 | 2022-05-21 | 5 | 0.28 | 1 | 2 | 68994 |
| 884 | 2020-06-10 | 5 | 0.28 | 0 | 2 | 78080 |
| 1619 | 2022-06-19 | 2 | 0.28 | 2 | 1 | 76077 |
| 1758 | 2022-11-05 | 3 | 0.27 | 1 | 1 | 61282 |
| 1035 | 2020-11-08 | 3 | 0.26 | 2 | 1 | 59399 |
| 526 | 2019-06-13 | 0 | 0.25 | 0 | 0 | 69856 |
| 775 | 2020-02-22 | 1 | 0.24 | 1 | 0 | 70579 |
| 768 | 2020-02-15 | 1 | 0.24 | 1 | 0 | 73543 |
| 1718 | 2022-09-26 | 0 | 0.24 | 0 | 0 | 68203 |
| 618 | 2019-09-15 | 2 | 0.24 | 2 | 1 | 74041 |
| 1453 | 2022-01-02 | 0 | 0.24 | 2 | 0 | 74460 |
| 1460 | 2022-01-09 | 0 | 0.23 | 2 | 0 | 72007 |
| 1427 | 2021-12-06 | 0 | 0.23 | 0 | 0 | 73388 |
| 694 | 2019-12-01 | 0 | 0.23 | 2 | 0 | 65827 |
| 1807 | 2022-12-24 | 1 | 0.22 | 1 | 0 | 88798 |
| 675 | 2019-11-11 | 0 | 0.22 | 0 | 0 | 73906 |

## ERCO

k = 6, silhouette 0.380, 1817 days, classifier accuracy 0.654.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 19 | 1.09 | 0.86 | 339 |
| 1 | heating | 7 | 1.14 | 0.93 | 249 |
| 2 | mild | 18 | 1.10 | 0.84 | 250 |
| 3 | mild | 17 | 1.19 | 0.80 | 172 |
| 4 | cooling | 16 | 1.19 | 0.81 | 241 |
| 5 | cooling | 16 | 1.25 | 0.76 | 566 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 228 | 0 | 0 | 60 | 0 | 0 | 51 | 0 | 0 |
| 1 | 165 | 0 | 0 | 49 | 0 | 0 | 35 | 0 | 0 |
| 2 | 0 | 200 | 0 | 0 | 37 | 0 | 0 | 13 | 0 |
| 3 | 0 | 99 | 0 | 0 | 27 | 0 | 0 | 46 | 0 |
| 4 | 0 | 0 | 192 | 0 | 0 | 27 | 0 | 0 | 22 |
| 5 | 0 | 0 | 380 | 0 | 0 | 84 | 0 | 0 | 102 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 5 | workday | 5 | 0.24 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 5 | sunday | 5 | 0.16 |
| 2018-05-28 | Memorial Day | 5 | sunday | 5 | workday | 5 | 0.14 |
| 2018-07-04 | Independence Day | 4 | sunday | 5 | workday | 5 | 0.21 |
| 2018-09-03 | Labor Day | 4 | sunday | 5 | workday | 5 | 0.17 |
| 2018-11-22 | Thanksgiving | 1 | saturday | 5 | workday | 5 | 0.18 |
| 2018-11-23 | Day after Thanksgiving | 2 | saturday | 5 | workday | 5 | 0.19 |
| 2018-12-24 | Christmas Eve | 1 | saturday | 5 | workday | 5 | 0.14 |
| 2018-12-25 | Christmas Day | 2 | saturday | 5 | workday | 5 | 0.20 |
| 2018-12-31 | New Year's Eve | 1 | saturday | 5 | workday | 5 | 0.13 |
| 2019-01-01 | New Year's Day | 0 | sunday | 5 | workday | 5 | 0.15 |
| 2019-02-03 | Super Bowl Sunday | 2 | saturday | 5 | sunday | 5 | 0.12 |
| 2019-05-27 | Memorial Day | 5 | sunday | 5 | workday | 5 | 0.06 |
| 2019-07-04 | Independence Day | 5 | sunday | 5 | workday | 5 | 0.07 |
| 2019-09-02 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.14 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.19 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.12 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 5 | workday | 5 | 0.10 |
| 2019-12-25 | Christmas Day | 1 | saturday | 5 | workday | 5 | 0.20 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 5 | workday | 5 | 0.08 |
| 2020-01-01 | New Year's Day | 0 | sunday | 5 | workday | 5 | 0.20 |
| 2020-02-02 | Super Bowl Sunday | 2 | saturday | 5 | sunday | 5 | 0.38 |
| 2020-05-25 | Memorial Day | 3 | sunday | 5 | workday | 5 | 0.12 |
| 2020-07-03 | observed holiday | 5 | sunday | 5 | workday | 5 | 0.12 |
| 2020-07-04 | Independence Day | 5 | sunday | 5 | saturday | 5 | 0.19 |
| 2020-09-07 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.11 |
| 2020-11-26 | Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.20 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.16 |
| 2020-12-24 | Christmas Eve | 1 | saturday | 5 | workday | 5 | 0.16 |
| 2020-12-25 | Christmas Day | 1 | saturday | 5 | workday | 5 | 0.25 |
| 2020-12-31 | New Year's Eve | 0 | saturday | 5 | workday | 5 | 0.14 |
| 2021-01-01 | New Year's Day | 1 | sunday | 5 | workday | 5 | 0.22 |
| 2021-02-07 | Super Bowl Sunday | 1 | saturday | 5 | sunday | 5 | 0.14 |
| 2021-05-31 | Memorial Day | 3 | sunday | 5 | workday | 5 | 0.11 |
| 2021-07-04 | Independence Day | 4 | sunday | 5 | sunday | 5 | 0.16 |
| 2021-07-05 | observed holiday | 4 | sunday | 5 | workday | 5 | 0.10 |
| 2021-09-06 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.16 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.27 |
| 2021-11-26 | Day after Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.16 |
| 2021-12-24 | Christmas Eve | 2 | saturday | 5 | workday | 5 | 0.17 |
| 2021-12-25 | Christmas Day | 2 | saturday | 5 | saturday | 5 | 0.21 |
| 2021-12-31 | New Year's Eve | 3 | sunday | 5 | workday | 5 | 0.16 |
| 2022-01-01 | New Year's Day | 0 | sunday | 5 | saturday | 5 | 0.38 |
| 2022-02-13 | Super Bowl Sunday | 1 | saturday | 5 | sunday | 5 | 0.38 |
| 2022-05-30 | Memorial Day | 5 | sunday | 5 | workday | 5 | 0.14 |
| 2022-07-04 | Independence Day | 5 | sunday | 5 | workday | 5 | 0.09 |
| 2022-09-05 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.11 |
| 2022-11-24 | Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.22 |
| 2022-11-25 | Day after Thanksgiving | 0 | saturday | 5 | workday | 5 | 0.11 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 5 | saturday | 5 | 0.32 |
| 2022-12-25 | Christmas Day | 1 | saturday | 5 | sunday | 5 | 0.51 |
| 2022-12-26 | observed holiday | 1 | saturday | 5 | workday | 5 | 0.25 |
| 2022-12-31 | New Year's Eve | 2 | saturday | 5 | saturday | 5 | 0.24 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 1807 | 2022-12-22 | 0 | 0.64 | 0 | 0 | 57903 |
| 1134 | 2021-02-15 | 1 | 0.64 | 0 | 0 | 49236 |
| 673 | 2019-11-11 | 0 | 0.58 | 0 | 0 | 40073 |
| 1139 | 2021-02-20 | 1 | 0.56 | 1 | 0 | 42463 |
| 30 | 2018-01-31 | 2 | 0.55 | 0 | 1 | 36845 |
| 1810 | 2022-12-25 | 1 | 0.51 | 1 | 0 | 51407 |
| 1498 | 2022-02-15 | 2 | 0.45 | 0 | 1 | 40953 |
| 1470 | 2022-01-18 | 2 | 0.45 | 0 | 1 | 41515 |
| 10 | 2018-01-11 | 0 | 0.44 | 0 | 0 | 38811 |
| 1494 | 2022-02-11 | 2 | 0.43 | 0 | 1 | 40441 |
| 1523 | 2022-03-12 | 1 | 0.43 | 1 | 0 | 47192 |
| 44 | 2018-02-14 | 2 | 0.43 | 0 | 1 | 37474 |
| 19 | 2018-01-20 | 2 | 0.43 | 1 | 1 | 35091 |
| 1488 | 2022-02-05 | 1 | 0.42 | 1 | 0 | 53966 |
| 1489 | 2022-02-06 | 1 | 0.41 | 2 | 0 | 48072 |
| 310 | 2018-11-12 | 0 | 0.39 | 0 | 0 | 41350 |
| 1513 | 2022-03-02 | 2 | 0.39 | 0 | 1 | 39812 |
| 1138 | 2021-02-19 | 1 | 0.38 | 0 | 0 | 48962 |
| 1021 | 2020-10-25 | 0 | 0.38 | 2 | 0 | 36330 |
| 756 | 2020-02-02 | 2 | 0.38 | 1 | 1 | 35787 |

## CISO

k = 7, silhouette 0.335, 1796 days, classifier accuracy 0.644.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 18 | 1.16 | 0.86 | 281 |
| 1 | heating | 19 | 1.18 | 0.88 | 164 |
| 2 | mild | 19 | 1.17 | 0.88 | 730 |
| 3 | mild | 18 | 1.24 | 0.80 | 465 |
| 4 | cooling | 17 | 1.19 | 0.82 | 34 |
| 5 | cooling | 17 | 1.27 | 0.76 | 75 |
| 6 | cooling | 18 | 1.26 | 0.80 | 47 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 240 | 0 | 0 | 28 | 0 | 0 | 13 | 0 | 0 |
| 1 | 65 | 0 | 0 | 48 | 0 | 0 | 51 | 0 | 0 |
| 2 | 0 | 487 | 0 | 0 | 131 | 0 | 0 | 112 | 0 |
| 3 | 0 | 344 | 0 | 0 | 54 | 0 | 0 | 67 | 0 |
| 4 | 0 | 0 | 27 | 0 | 0 | 6 | 0 | 0 | 1 |
| 5 | 0 | 0 | 61 | 0 | 0 | 8 | 0 | 0 | 6 |
| 6 | 0 | 0 | 21 | 0 | 0 | 9 | 0 | 0 | 17 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 2 | workday | 2 | 0.22 |
| 2018-02-04 | Super Bowl Sunday | 2 | saturday | 2 | sunday | 2 | 0.13 |
| 2018-05-28 | Memorial Day | 3 | sunday | 2 | workday | 2 | 0.19 |
| 2018-07-04 | Independence Day | 3 | sunday | 2 | workday | 2 | 0.21 |
| 2018-09-03 | Labor Day | 3 | sunday | 2 | workday | 2 | 0.07 |
| 2018-11-22 | Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.21 |
| 2018-11-23 | Day after Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.17 |
| 2018-12-24 | Christmas Eve | 2 | saturday | 2 | workday | 2 | 0.13 |
| 2018-12-25 | Christmas Day | 2 | saturday | 2 | workday | 2 | 0.18 |
| 2018-12-31 | New Year's Eve | 0 | saturday | 2 | workday | 2 | 0.09 |
| 2019-01-01 | New Year's Day | 1 | sunday | 2 | workday | 2 | 0.21 |
| 2019-02-03 | Super Bowl Sunday | 0 | saturday | 2 | sunday | 2 | 0.21 |
| 2019-05-27 | Memorial Day | 1 | sunday | 2 | workday | 2 | 0.23 |
| 2019-09-02 | Labor Day | 5 | sunday | 2 | workday | 2 | 0.16 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 2 | workday | 2 | 0.26 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 2 | workday | 2 | 0.19 |
| 2019-12-24 | Christmas Eve | 0 | saturday | 2 | workday | 2 | 0.13 |
| 2019-12-25 | Christmas Day | 0 | saturday | 2 | workday | 2 | 0.19 |
| 2019-12-31 | New Year's Eve | 2 | saturday | 2 | workday | 2 | 0.15 |
| 2020-01-01 | New Year's Day | 1 | sunday | 2 | workday | 2 | 0.17 |
| 2020-02-02 | Super Bowl Sunday | 2 | saturday | 2 | sunday | 2 | 0.18 |
| 2020-05-25 | Memorial Day | 3 | sunday | 2 | workday | 2 | 0.38 |
| 2020-07-03 | observed holiday | 3 | sunday | 2 | workday | 2 | 0.26 |
| 2020-07-04 | Independence Day | 3 | sunday | 2 | saturday | 2 | 0.28 |
| 2020-09-07 | Labor Day | 5 | sunday | 2 | workday | 2 | 0.20 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 2 | workday | 2 | 0.21 |
| 2020-11-27 | Day after Thanksgiving | 1 | saturday | 2 | workday | 2 | 0.18 |
| 2020-12-24 | Christmas Eve | 2 | saturday | 2 | workday | 2 | 0.19 |
| 2020-12-25 | Christmas Day | 2 | saturday | 2 | workday | 2 | 0.18 |
| 2020-12-31 | New Year's Eve | 1 | saturday | 2 | workday | 2 | 0.16 |
| 2021-01-01 | New Year's Day | 1 | sunday | 2 | workday | 2 | 0.20 |
| 2021-02-07 | Super Bowl Sunday | 1 | saturday | 2 | sunday | 2 | 0.13 |
| 2021-05-31 | Memorial Day | 3 | sunday | 2 | workday | 2 | 0.25 |
| 2021-07-04 | Independence Day | 3 | sunday | 2 | sunday | 2 | 0.28 |
| 2021-07-05 | observed holiday | 3 | sunday | 2 | workday | 2 | 0.19 |
| 2021-09-06 | Labor Day | 5 | sunday | 2 | workday | 2 | 0.23 |
| 2021-11-25 | Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.22 |
| 2021-11-26 | Day after Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.19 |
| 2021-12-24 | Christmas Eve | 0 | saturday | 2 | workday | 2 | 0.22 |
| 2021-12-25 | Christmas Day | 0 | saturday | 2 | saturday | 2 | 0.22 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 2 | workday | 2 | 0.15 |
| 2022-01-01 | New Year's Day | 1 | sunday | 2 | saturday | 2 | 0.14 |
| 2022-02-13 | Super Bowl Sunday | 2 | saturday | 2 | sunday | 2 | 0.25 |
| 2022-05-30 | Memorial Day | 2 | sunday | 2 | workday | 2 | 0.32 |
| 2022-07-04 | Independence Day | 2 | sunday | 2 | workday | 2 | 0.37 |
| 2022-09-05 | Labor Day | 6 | sunday | 2 | workday | 2 | 0.19 |
| 2022-11-24 | Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.34 |
| 2022-11-25 | Day after Thanksgiving | 2 | saturday | 2 | workday | 2 | 0.16 |
| 2022-12-24 | Christmas Eve | 2 | saturday | 2 | saturday | 2 | 0.25 |
| 2022-12-25 | Christmas Day | 2 | saturday | 2 | sunday | 2 | 0.25 |
| 2022-12-26 | observed holiday | 2 | saturday | 2 | workday | 2 | 0.16 |
| 2022-12-31 | New Year's Eve | 0 | saturday | 2 | saturday | 2 | 0.28 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 483 | 2019-05-09 | 2 | 0.96 | 0 | 1 | 21998 |
| 400 | 2019-02-14 | 1 | 0.78 | 0 | 0 | 21801 |
| 460 | 2019-04-16 | 2 | 0.74 | 0 | 1 | 21370 |
| 1539 | 2022-04-17 | 2 | 0.62 | 2 | 1 | 18714 |
| 455 | 2019-04-11 | 2 | 0.61 | 0 | 1 | 21572 |
| 405 | 2019-02-19 | 1 | 0.59 | 0 | 0 | 22434 |
| 1553 | 2022-05-01 | 2 | 0.58 | 2 | 1 | 19521 |
| 399 | 2019-02-13 | 0 | 0.58 | 0 | 0 | 22778 |
| 1545 | 2022-04-23 | 2 | 0.56 | 1 | 1 | 19628 |
| 1560 | 2022-05-08 | 2 | 0.55 | 2 | 1 | 19455 |
| 1511 | 2022-03-20 | 2 | 0.55 | 2 | 1 | 19486 |
| 393 | 2019-02-07 | 0 | 0.54 | 0 | 0 | 22153 |
| 1546 | 2022-04-24 | 2 | 0.54 | 2 | 1 | 19551 |
| 854 | 2020-05-24 | 3 | 0.53 | 2 | 1 | 20711 |
| 1216 | 2021-05-23 | 2 | 0.51 | 2 | 1 | 19922 |
| 868 | 2020-06-07 | 2 | 0.51 | 2 | 1 | 20032 |
| 833 | 2020-05-03 | 2 | 0.50 | 2 | 1 | 19654 |
| 1532 | 2022-04-10 | 2 | 0.50 | 2 | 1 | 19814 |
| 1491 | 2022-02-27 | 2 | 0.50 | 2 | 1 | 20128 |
| 454 | 2019-04-10 | 2 | 0.49 | 0 | 1 | 21022 |

## SWPP

k = 6, silhouette 0.385, 1719 days, classifier accuracy 0.614.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 19 | 1.06 | 0.89 | 434 |
| 1 | heating | 7 | 1.09 | 0.95 | 404 |
| 2 | mild | 17 | 1.16 | 0.82 | 151 |
| 3 | mild | 17 | 1.07 | 0.88 | 198 |
| 4 | cooling | 16 | 1.16 | 0.83 | 149 |
| 5 | cooling | 16 | 1.23 | 0.78 | 383 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 319 | 0 | 0 | 54 | 0 | 0 | 61 | 0 | 0 |
| 1 | 259 | 0 | 0 | 90 | 0 | 0 | 55 | 0 | 0 |
| 2 | 0 | 105 | 0 | 0 | 18 | 0 | 0 | 28 | 0 |
| 3 | 0 | 142 | 0 | 0 | 33 | 0 | 0 | 23 | 0 |
| 4 | 0 | 0 | 97 | 0 | 0 | 28 | 0 | 0 | 24 |
| 5 | 0 | 0 | 271 | 0 | 0 | 48 | 0 | 0 | 64 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 5 | workday | 0 | 0.16 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.20 |
| 2018-05-28 | Memorial Day | 5 | sunday | 5 | workday | 0 | 0.11 |
| 2018-09-03 | Labor Day | 4 | sunday | 5 | workday | 0 | 0.13 |
| 2018-11-22 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.16 |
| 2018-11-23 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.07 |
| 2018-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.09 |
| 2018-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.09 |
| 2018-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.09 |
| 2019-01-01 | New Year's Day | 0 | sunday | 5 | workday | 0 | 0.14 |
| 2019-02-03 | Super Bowl Sunday | 3 | saturday | 1 | sunday | 5 | 0.14 |
| 2019-05-27 | Memorial Day | 5 | sunday | 5 | workday | 0 | 0.13 |
| 2019-07-04 | Independence Day | 5 | sunday | 5 | workday | 0 | 0.14 |
| 2019-09-02 | Labor Day | 5 | sunday | 5 | workday | 0 | 0.21 |
| 2019-11-28 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.21 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.09 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.07 |
| 2019-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.21 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 0 | 0.08 |
| 2020-01-01 | New Year's Day | 1 | sunday | 5 | workday | 0 | 0.14 |
| 2020-02-02 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.08 |
| 2020-05-25 | Memorial Day | 2 | sunday | 5 | workday | 0 | 0.18 |
| 2020-07-03 | observed holiday | 5 | sunday | 5 | workday | 0 | 0.10 |
| 2020-07-04 | Independence Day | 5 | sunday | 5 | saturday | 1 | 0.13 |
| 2020-09-07 | Labor Day | 5 | sunday | 5 | workday | 0 | 0.12 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.11 |
| 2020-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.05 |
| 2020-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.23 |
| 2020-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.10 |
| 2021-01-01 | New Year's Day | 0 | sunday | 5 | workday | 0 | 0.17 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.11 |
| 2021-05-31 | Memorial Day | 2 | sunday | 5 | workday | 0 | 0.20 |
| 2021-07-04 | Independence Day | 5 | sunday | 5 | sunday | 5 | 0.10 |
| 2021-07-05 | observed holiday | 5 | sunday | 5 | workday | 0 | 0.15 |
| 2021-09-06 | Labor Day | 5 | sunday | 5 | workday | 0 | 0.21 |
| 2021-11-25 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.15 |
| 2021-11-26 | Day after Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.06 |
| 2021-12-24 | Christmas Eve | 3 | saturday | 1 | workday | 0 | 0.19 |
| 2021-12-25 | Christmas Day | 3 | saturday | 1 | saturday | 1 | 0.17 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 5 | workday | 0 | 0.10 |
| 2022-01-01 | New Year's Day | 0 | sunday | 5 | saturday | 1 | 0.35 |
| 2022-02-13 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.17 |
| 2022-05-30 | Memorial Day | 4 | sunday | 5 | workday | 0 | 0.14 |
| 2022-07-04 | Independence Day | 5 | sunday | 5 | workday | 0 | 0.12 |
| 2022-09-05 | Labor Day | 5 | sunday | 5 | workday | 0 | 0.11 |
| 2022-11-24 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.16 |
| 2022-11-25 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.11 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 1 | saturday | 1 | 0.21 |
| 2022-12-25 | Christmas Day | 1 | saturday | 1 | sunday | 5 | 0.22 |
| 2022-12-26 | observed holiday | 0 | saturday | 1 | workday | 0 | 0.18 |
| 2022-12-31 | New Year's Eve | 1 | saturday | 1 | saturday | 1 | 0.12 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 1223 | 2021-08-22 | 4 | 0.64 | 2 | 2 | 26683 |
| 419 | 2019-06-08 | 4 | 0.63 | 1 | 2 | 24204 |
| 1224 | 2021-08-23 | 4 | 0.56 | 0 | 2 | 41279 |
| 1225 | 2021-08-24 | 4 | 0.56 | 0 | 2 | 29892 |
| 1219 | 2021-08-18 | 4 | 0.56 | 0 | 2 | 33979 |
| 1220 | 2021-08-19 | 4 | 0.56 | 0 | 2 | 33979 |
| 431 | 2019-06-20 | 5 | 0.45 | 0 | 2 | 34415 |
| 575 | 2019-11-11 | 0 | 0.39 | 0 | 0 | 32123 |
| 526 | 2019-09-23 | 5 | 0.36 | 0 | 2 | 32549 |
| 1218 | 2021-08-17 | 4 | 0.36 | 0 | 2 | 32684 |
| 738 | 2020-04-23 | 3 | 0.35 | 0 | 1 | 21262 |
| 225 | 2018-11-25 | 0 | 0.35 | 2 | 0 | 28549 |
| 1355 | 2022-01-01 | 0 | 0.35 | 2 | 0 | 31711 |
| 348 | 2019-03-29 | 3 | 0.34 | 0 | 1 | 24326 |
| 357 | 2019-04-07 | 3 | 0.34 | 2 | 1 | 27151 |
| 356 | 2019-04-06 | 3 | 0.34 | 1 | 1 | 27151 |
| 777 | 2020-06-01 | 2 | 0.32 | 0 | 1 | 30148 |
| 1709 | 2022-12-22 | 0 | 0.31 | 0 | 0 | 41530 |
| 776 | 2020-05-31 | 2 | 0.30 | 2 | 1 | 26598 |
| 1221 | 2021-08-20 | 5 | 0.29 | 0 | 2 | 39357 |

## NYIS

k = 7, silhouette 0.317, 1820 days, classifier accuracy 0.835.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 19 | 1.12 | 0.88 | 382 |
| 1 | heating | 18 | 1.13 | 0.82 | 638 |
| 2 | mild | 17 | 1.14 | 0.79 | 272 |
| 3 | mild | 18 | 1.14 | 0.84 | 128 |
| 4 | cooling | 17 | 1.20 | 0.79 | 95 |
| 5 | cooling | 17 | 1.20 | 0.76 | 186 |
| 6 | cooling | 17 | 1.14 | 0.82 | 119 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 105 | 0 | 0 | 144 | 0 | 0 | 133 | 0 | 0 |
| 1 | 591 | 0 | 0 | 32 | 0 | 0 | 15 | 0 | 0 |
| 2 | 0 | 270 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 3 | 0 | 14 | 0 | 0 | 57 | 0 | 0 | 57 | 0 |
| 4 | 0 | 0 | 6 | 0 | 0 | 34 | 0 | 0 | 55 |
| 5 | 0 | 0 | 179 | 0 | 0 | 3 | 0 | 0 | 4 |
| 6 | 0 | 0 | 98 | 0 | 0 | 15 | 0 | 0 | 6 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 0 | sunday | 0 | workday | 1 | 0.13 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 0 | sunday | 0 | 0.17 |
| 2018-05-28 | Memorial Day | 1 | sunday | 0 | workday | 1 | 0.30 |
| 2018-07-04 | Independence Day | 5 | sunday | 0 | workday | 1 | 0.18 |
| 2018-09-03 | Labor Day | 5 | sunday | 0 | workday | 1 | 0.19 |
| 2018-11-22 | Thanksgiving | 0 | saturday | 0 | workday | 1 | 0.14 |
| 2018-11-23 | Day after Thanksgiving | 0 | saturday | 0 | workday | 1 | 0.10 |
| 2018-12-24 | Christmas Eve | 1 | saturday | 0 | workday | 1 | 0.11 |
| 2018-12-25 | Christmas Day | 0 | saturday | 0 | workday | 1 | 0.06 |
| 2018-12-31 | New Year's Eve | 1 | saturday | 0 | workday | 1 | 0.10 |
| 2019-01-01 | New Year's Day | 0 | sunday | 0 | workday | 1 | 0.24 |
| 2019-02-03 | Super Bowl Sunday | 0 | saturday | 0 | sunday | 0 | 0.10 |
| 2019-05-27 | Memorial Day | 4 | sunday | 0 | workday | 1 | 0.14 |
| 2019-07-04 | Independence Day | 5 | sunday | 0 | workday | 1 | 0.15 |
| 2019-09-02 | Labor Day | 3 | sunday | 0 | workday | 1 | 0.12 |
| 2019-11-28 | Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.19 |
| 2019-11-29 | Day after Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.11 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 0 | workday | 1 | 0.10 |
| 2019-12-25 | Christmas Day | 0 | saturday | 0 | workday | 1 | 0.09 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 0 | workday | 1 | 0.09 |
| 2020-01-01 | New Year's Day | 0 | sunday | 0 | workday | 1 | 0.18 |
| 2020-02-02 | Super Bowl Sunday | 0 | saturday | 0 | sunday | 0 | 0.16 |
| 2020-05-25 | Memorial Day | 3 | sunday | 0 | workday | 1 | 0.13 |
| 2020-07-03 | observed holiday | 5 | sunday | 0 | workday | 1 | 0.16 |
| 2020-07-04 | Independence Day | 4 | sunday | 0 | saturday | 0 | 0.12 |
| 2020-09-07 | Labor Day | 3 | sunday | 0 | workday | 1 | 0.14 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.23 |
| 2020-11-27 | Day after Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.15 |
| 2020-12-24 | Christmas Eve | 1 | saturday | 0 | workday | 1 | 0.16 |
| 2020-12-25 | Christmas Day | 0 | saturday | 0 | workday | 1 | 0.22 |
| 2020-12-31 | New Year's Eve | 1 | saturday | 0 | workday | 1 | 0.12 |
| 2021-01-01 | New Year's Day | 0 | sunday | 0 | workday | 1 | 0.17 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 0 | sunday | 0 | 0.19 |
| 2021-05-31 | Memorial Day | 0 | sunday | 0 | workday | 1 | 0.12 |
| 2021-07-04 | Independence Day | 3 | sunday | 0 | sunday | 0 | 0.11 |
| 2021-07-05 | observed holiday | 4 | sunday | 0 | workday | 1 | 0.25 |
| 2021-09-06 | Labor Day | 4 | sunday | 0 | workday | 1 | 0.13 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 0 | workday | 1 | 0.24 |
| 2021-11-26 | Day after Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.18 |
| 2021-12-24 | Christmas Eve | 0 | saturday | 0 | workday | 1 | 0.15 |
| 2021-12-25 | Christmas Day | 0 | saturday | 0 | saturday | 0 | 0.14 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 0 | workday | 1 | 0.15 |
| 2022-01-01 | New Year's Day | 0 | sunday | 0 | saturday | 0 | 0.19 |
| 2022-02-13 | Super Bowl Sunday | 0 | saturday | 0 | sunday | 0 | 0.18 |
| 2022-05-30 | Memorial Day | 3 | sunday | 0 | workday | 1 | 0.43 |
| 2022-07-04 | Independence Day | 4 | sunday | 0 | workday | 1 | 0.11 |
| 2022-09-05 | Labor Day | 4 | sunday | 0 | workday | 1 | 0.15 |
| 2022-11-24 | Thanksgiving | 0 | saturday | 0 | workday | 1 | 0.19 |
| 2022-11-25 | Day after Thanksgiving | 1 | saturday | 0 | workday | 1 | 0.11 |
| 2022-12-24 | Christmas Eve | 0 | saturday | 0 | saturday | 0 | 0.08 |
| 2022-12-25 | Christmas Day | 0 | saturday | 0 | sunday | 0 | 0.19 |
| 2022-12-26 | observed holiday | 0 | saturday | 0 | workday | 1 | 0.11 |
| 2022-12-31 | New Year's Eve | 0 | saturday | 0 | saturday | 0 | 0.18 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 1263 | 2021-06-22 | 2 | 0.49 | 0 | 1 | 18622 |
| 1604 | 2022-05-30 | 3 | 0.43 | 2 | 1 | 16965 |
| 1623 | 2022-06-18 | 3 | 0.42 | 1 | 1 | 15421 |
| 886 | 2020-06-09 | 2 | 0.42 | 0 | 1 | 18138 |
| 147 | 2018-05-29 | 2 | 0.42 | 0 | 1 | 19360 |
| 942 | 2020-08-04 | 6 | 0.41 | 0 | 2 | 20429 |
| 257 | 2018-09-16 | 3 | 0.39 | 2 | 1 | 19621 |
| 1595 | 2022-05-21 | 3 | 0.38 | 1 | 1 | 17015 |
| 626 | 2019-09-22 | 3 | 0.38 | 2 | 1 | 17631 |
| 1719 | 2022-09-22 | 2 | 0.36 | 0 | 1 | 17290 |
| 1169 | 2021-03-20 | 0 | 0.35 | 1 | 0 | 15246 |
| 249 | 2018-09-08 | 3 | 0.34 | 1 | 1 | 16951 |
| 1330 | 2021-08-28 | 6 | 0.34 | 1 | 2 | 19640 |
| 185 | 2018-07-06 | 6 | 0.34 | 0 | 2 | 22766 |
| 145 | 2018-05-27 | 3 | 0.33 | 2 | 1 | 16243 |
| 1811 | 2022-12-23 | 1 | 0.33 | 0 | 0 | 18079 |
| 187 | 2018-07-08 | 3 | 0.32 | 2 | 1 | 17740 |
| 887 | 2020-06-10 | 2 | 0.31 | 0 | 1 | 19978 |
| 1546 | 2022-04-02 | 0 | 0.30 | 1 | 0 | 14690 |
| 1574 | 2022-04-30 | 0 | 0.30 | 1 | 0 | 13521 |

## ISNE

k = 6, silhouette 0.277, 1821 days, classifier accuracy 0.618.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 18 | 1.15 | 0.83 | 582 |
| 1 | heating | 19 | 1.16 | 0.89 | 503 |
| 2 | mild | 18 | 1.16 | 0.83 | 229 |
| 3 | mild | 18 | 1.20 | 0.86 | 198 |
| 4 | cooling | 18 | 1.25 | 0.78 | 141 |
| 5 | cooling | 17 | 1.17 | 0.83 | 168 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 443 | 0 | 0 | 74 | 0 | 0 | 65 | 0 | 0 |
| 1 | 312 | 0 | 0 | 103 | 0 | 0 | 88 | 0 | 0 |
| 2 | 0 | 198 | 0 | 0 | 18 | 0 | 0 | 13 | 0 |
| 3 | 0 | 91 | 0 | 0 | 48 | 0 | 0 | 59 | 0 |
| 4 | 0 | 0 | 88 | 0 | 0 | 21 | 0 | 0 | 32 |
| 5 | 0 | 0 | 132 | 0 | 0 | 22 | 0 | 0 | 14 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 0 | sunday | 1 | workday | 0 | 0.21 |
| 2018-02-04 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.22 |
| 2018-05-28 | Memorial Day | 0 | sunday | 1 | workday | 0 | 0.22 |
| 2018-07-04 | Independence Day | 5 | sunday | 1 | workday | 0 | 0.16 |
| 2018-09-03 | Labor Day | 4 | sunday | 1 | workday | 0 | 0.30 |
| 2018-11-22 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.20 |
| 2018-11-23 | Day after Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.15 |
| 2018-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.17 |
| 2018-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.11 |
| 2018-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.13 |
| 2019-01-01 | New Year's Day | 1 | sunday | 1 | workday | 0 | 0.25 |
| 2019-02-03 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.18 |
| 2019-05-27 | Memorial Day | 3 | sunday | 1 | workday | 0 | 0.08 |
| 2019-07-04 | Independence Day | 5 | sunday | 1 | workday | 0 | 0.13 |
| 2019-09-02 | Labor Day | 2 | sunday | 1 | workday | 0 | 0.24 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.26 |
| 2019-11-29 | Day after Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.20 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 0 | 0.20 |
| 2019-12-25 | Christmas Day | 1 | saturday | 1 | workday | 0 | 0.13 |
| 2019-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.15 |
| 2020-01-01 | New Year's Day | 0 | sunday | 1 | workday | 0 | 0.28 |
| 2020-02-02 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.22 |
| 2020-05-25 | Memorial Day | 0 | sunday | 1 | workday | 0 | 0.28 |
| 2020-07-03 | observed holiday | 2 | sunday | 1 | workday | 0 | 0.27 |
| 2020-07-04 | Independence Day | 3 | sunday | 1 | saturday | 1 | 0.15 |
| 2020-09-07 | Labor Day | 3 | sunday | 1 | workday | 0 | 0.15 |
| 2020-11-26 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.38 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.14 |
| 2020-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.16 |
| 2020-12-25 | Christmas Day | 0 | saturday | 1 | workday | 0 | 0.22 |
| 2020-12-31 | New Year's Eve | 0 | saturday | 1 | workday | 0 | 0.12 |
| 2021-01-01 | New Year's Day | 1 | sunday | 1 | workday | 0 | 0.27 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.27 |
| 2021-05-31 | Memorial Day | 0 | sunday | 1 | workday | 0 | 0.22 |
| 2021-07-04 | Independence Day | 3 | sunday | 1 | sunday | 1 | 0.19 |
| 2021-07-05 | observed holiday | 3 | sunday | 1 | workday | 0 | 0.27 |
| 2021-09-06 | Labor Day | 5 | sunday | 1 | workday | 0 | 0.21 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.38 |
| 2021-11-26 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.18 |
| 2021-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 0 | 0.18 |
| 2021-12-25 | Christmas Day | 0 | saturday | 1 | saturday | 1 | 0.20 |
| 2021-12-31 | New Year's Eve | 0 | sunday | 1 | workday | 0 | 0.15 |
| 2022-01-01 | New Year's Day | 0 | sunday | 1 | saturday | 1 | 0.23 |
| 2022-02-13 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.25 |
| 2022-05-30 | Memorial Day | 4 | sunday | 1 | workday | 0 | 0.45 |
| 2022-07-04 | Independence Day | 4 | sunday | 1 | workday | 0 | 0.32 |
| 2022-09-05 | Labor Day | 2 | sunday | 1 | workday | 0 | 0.19 |
| 2022-11-24 | Thanksgiving | 1 | saturday | 1 | workday | 0 | 0.20 |
| 2022-11-25 | Day after Thanksgiving | 0 | saturday | 1 | workday | 0 | 0.14 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 1 | saturday | 1 | 0.23 |
| 2022-12-25 | Christmas Day | 1 | saturday | 1 | sunday | 1 | 0.25 |
| 2022-12-26 | observed holiday | 1 | saturday | 1 | workday | 0 | 0.22 |
| 2022-12-31 | New Year's Eve | 0 | saturday | 1 | saturday | 1 | 0.16 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 943 | 2020-08-04 | 5 | 0.54 | 0 | 2 | 16570 |
| 1331 | 2021-08-28 | 3 | 0.49 | 1 | 1 | 13835 |
| 981 | 2020-09-11 | 2 | 0.48 | 0 | 1 | 13711 |
| 1716 | 2022-09-18 | 3 | 0.47 | 2 | 1 | 11940 |
| 185 | 2018-07-06 | 5 | 0.47 | 0 | 2 | 18123 |
| 1605 | 2022-05-30 | 4 | 0.45 | 2 | 2 | 12512 |
| 1597 | 2022-05-22 | 3 | 0.44 | 2 | 1 | 14088 |
| 1576 | 2022-05-01 | 1 | 0.44 | 2 | 0 | 9606 |
| 1264 | 2021-06-22 | 5 | 0.43 | 0 | 2 | 15451 |
| 1274 | 2021-07-02 | 2 | 0.42 | 0 | 1 | 13781 |
| 873 | 2020-05-26 | 0 | 0.41 | 0 | 0 | 11675 |
| 906 | 2020-06-28 | 2 | 0.41 | 2 | 1 | 13858 |
| 1547 | 2022-04-02 | 1 | 0.41 | 1 | 0 | 10917 |
| 248 | 2018-09-07 | 2 | 0.41 | 0 | 1 | 14998 |
| 147 | 2018-05-29 | 2 | 0.40 | 0 | 1 | 13770 |
| 1793 | 2022-12-04 | 1 | 0.40 | 2 | 0 | 12338 |
| 166 | 2018-06-17 | 3 | 0.39 | 2 | 1 | 13154 |
| 195 | 2018-07-16 | 2 | 0.39 | 0 | 1 | 18183 |
| 1736 | 2022-10-08 | 1 | 0.38 | 1 | 0 | 10134 |
| 1318 | 2021-08-15 | 5 | 0.38 | 2 | 2 | 14123 |

## TVA

k = 7, silhouette 0.405, 1782 days, classifier accuracy 0.587.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 7 | 1.15 | 0.91 | 352 |
| 1 | heating | 19 | 1.09 | 0.86 | 427 |
| 2 | mild | 19 | 1.09 | 0.85 | 232 |
| 3 | mild | 9 | 2.86 | 0.79 | 1 |
| 4 | mild | 16 | 1.18 | 0.79 | 125 |
| 5 | cooling | 16 | 1.28 | 0.72 | 349 |
| 6 | cooling | 15 | 1.21 | 0.78 | 296 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 238 | 0 | 0 | 67 | 0 | 0 | 47 | 0 | 0 |
| 1 | 290 | 0 | 0 | 75 | 0 | 0 | 62 | 0 | 0 |
| 2 | 0 | 183 | 0 | 0 | 34 | 0 | 0 | 15 | 0 |
| 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 0 | 86 | 0 | 0 | 11 | 0 | 0 | 28 | 0 |
| 5 | 0 | 0 | 210 | 0 | 0 | 64 | 0 | 0 | 75 |
| 6 | 0 | 0 | 235 | 0 | 0 | 28 | 0 | 0 | 33 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 0 | sunday | 5 | workday | 1 | 0.26 |
| 2018-02-04 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.17 |
| 2018-05-28 | Memorial Day | 6 | sunday | 5 | workday | 1 | 0.14 |
| 2018-09-03 | Labor Day | 5 | sunday | 5 | workday | 1 | 0.10 |
| 2018-11-22 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.31 |
| 2018-11-23 | Day after Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.24 |
| 2018-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 1 | 0.14 |
| 2018-12-25 | Christmas Day | 0 | saturday | 1 | workday | 1 | 0.16 |
| 2018-12-31 | New Year's Eve | 2 | saturday | 1 | workday | 1 | 0.14 |
| 2019-01-01 | New Year's Day | 1 | sunday | 5 | workday | 1 | 0.25 |
| 2019-02-03 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.15 |
| 2019-05-27 | Memorial Day | 5 | sunday | 5 | workday | 1 | 0.13 |
| 2019-07-04 | Independence Day | 5 | sunday | 5 | workday | 1 | 0.22 |
| 2019-09-02 | Labor Day | 5 | sunday | 5 | workday | 1 | 0.18 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.18 |
| 2019-11-29 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.17 |
| 2019-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 1 | 0.17 |
| 2019-12-25 | Christmas Day | 0 | saturday | 1 | workday | 1 | 0.12 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 1 | 0.17 |
| 2020-01-01 | New Year's Day | 0 | sunday | 5 | workday | 1 | 0.12 |
| 2020-02-02 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.17 |
| 2020-05-25 | Memorial Day | 5 | sunday | 5 | workday | 1 | 0.14 |
| 2020-07-03 | observed holiday | 5 | sunday | 5 | workday | 1 | 0.12 |
| 2020-07-04 | Independence Day | 5 | sunday | 5 | saturday | 1 | 0.18 |
| 2020-09-07 | Labor Day | 5 | sunday | 5 | workday | 1 | 0.25 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.22 |
| 2020-11-27 | Day after Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.22 |
| 2020-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 1 | 0.43 |
| 2020-12-25 | Christmas Day | 1 | saturday | 1 | workday | 1 | 0.23 |
| 2020-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 1 | 0.16 |
| 2021-01-01 | New Year's Day | 1 | sunday | 5 | workday | 1 | 0.27 |
| 2021-02-07 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.14 |
| 2021-05-31 | Memorial Day | 4 | sunday | 5 | workday | 1 | 0.21 |
| 2021-07-04 | Independence Day | 5 | sunday | 5 | sunday | 5 | 0.19 |
| 2021-07-05 | observed holiday | 5 | sunday | 5 | workday | 1 | 0.26 |
| 2021-09-06 | Labor Day | 5 | sunday | 5 | workday | 1 | 0.13 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.23 |
| 2021-11-26 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.28 |
| 2021-12-24 | Christmas Eve | 2 | saturday | 1 | workday | 1 | 0.47 |
| 2021-12-25 | Christmas Day | 2 | saturday | 1 | saturday | 1 | 0.15 |
| 2021-12-31 | New Year's Eve | 2 | sunday | 5 | workday | 1 | 0.14 |
| 2022-01-01 | New Year's Day | 2 | sunday | 5 | saturday | 1 | 0.23 |
| 2022-02-13 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.15 |
| 2022-05-30 | Memorial Day | 5 | sunday | 5 | workday | 1 | 0.16 |
| 2022-07-04 | Independence Day | 5 | sunday | 5 | workday | 1 | 0.15 |
| 2022-09-05 | Labor Day | 6 | sunday | 5 | workday | 1 | 0.16 |
| 2022-11-24 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.26 |
| 2022-11-25 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.11 |
| 2022-12-24 | Christmas Eve | 0 | saturday | 1 | saturday | 1 | 0.33 |
| 2022-12-25 | Christmas Day | 0 | saturday | 1 | sunday | 5 | 0.31 |
| 2022-12-26 | observed holiday | 0 | saturday | 1 | workday | 1 | 0.21 |
| 2022-12-31 | New Year's Eve | 2 | saturday | 1 | saturday | 1 | 0.17 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 359 | 2019-01-29 | 0 | 1.57 | 0 | 0 | 24274 |
| 1420 | 2022-01-02 | 1 | 0.64 | 2 | 0 | 16187 |
| 11 | 2018-01-12 | 1 | 0.62 | 0 | 0 | 20156 |
| 671 | 2019-12-10 | 1 | 0.55 | 0 | 0 | 18867 |
| 1111 | 2021-02-24 | 2 | 0.51 | 0 | 1 | 16446 |
| 1411 | 2021-12-24 | 2 | 0.47 | 1 | 1 | 15809 |
| 236 | 2018-09-26 | 6 | 0.47 | 0 | 2 | 17895 |
| 1478 | 2022-03-02 | 2 | 0.46 | 0 | 1 | 16948 |
| 738 | 2020-02-15 | 0 | 0.45 | 1 | 0 | 20046 |
| 1049 | 2020-12-24 | 1 | 0.43 | 1 | 0 | 18690 |
| 745 | 2020-02-22 | 0 | 0.42 | 1 | 0 | 19693 |
| 1426 | 2022-01-08 | 0 | 0.42 | 1 | 0 | 22000 |
| 1385 | 2021-11-28 | 0 | 0.42 | 2 | 0 | 17871 |
| 1393 | 2021-12-06 | 1 | 0.42 | 0 | 0 | 17154 |
| 678 | 2019-12-17 | 1 | 0.42 | 0 | 0 | 19808 |
| 1398 | 2021-12-11 | 1 | 0.41 | 1 | 0 | 15250 |
| 1464 | 2022-02-16 | 2 | 0.41 | 0 | 1 | 17297 |
| 1116 | 2021-03-01 | 1 | 0.40 | 0 | 0 | 16705 |
| 1750 | 2022-11-30 | 1 | 0.40 | 0 | 0 | 17531 |
| 39 | 2018-02-09 | 0 | 0.40 | 0 | 0 | 18890 |

## DUK

k = 6, silhouette 0.369, 1821 days, classifier accuracy 0.592.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 7 | 1.19 | 0.90 | 354 |
| 1 | heating | 19 | 1.10 | 0.85 | 370 |
| 2 | mild | 17 | 1.20 | 0.77 | 162 |
| 3 | mild | 19 | 1.10 | 0.83 | 272 |
| 4 | cooling | 16 | 1.22 | 0.76 | 234 |
| 5 | cooling | 16 | 1.29 | 0.71 | 429 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 242 | 0 | 0 | 65 | 0 | 0 | 47 | 0 | 0 |
| 1 | 250 | 0 | 0 | 66 | 0 | 0 | 54 | 0 | 0 |
| 2 | 0 | 110 | 0 | 0 | 18 | 0 | 0 | 34 | 0 |
| 3 | 0 | 200 | 0 | 0 | 45 | 0 | 0 | 27 | 0 |
| 4 | 0 | 0 | 189 | 0 | 0 | 28 | 0 | 0 | 17 |
| 5 | 0 | 0 | 273 | 0 | 0 | 64 | 0 | 0 | 92 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 5 | workday | 5 | 0.32 |
| 2018-02-04 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.28 |
| 2018-05-28 | Memorial Day | 4 | sunday | 5 | workday | 5 | 0.25 |
| 2018-07-04 | Independence Day | 4 | sunday | 5 | workday | 5 | 0.23 |
| 2018-09-03 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.17 |
| 2018-11-22 | Thanksgiving | 0 | saturday | 1 | workday | 5 | 0.20 |
| 2018-11-23 | Day after Thanksgiving | 1 | saturday | 1 | workday | 5 | 0.13 |
| 2018-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 5 | 0.30 |
| 2018-12-25 | Christmas Day | 0 | saturday | 1 | workday | 5 | 0.22 |
| 2018-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 5 | 0.25 |
| 2019-01-01 | New Year's Day | 3 | sunday | 5 | workday | 5 | 0.25 |
| 2019-02-03 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.16 |
| 2019-05-27 | Memorial Day | 5 | sunday | 5 | workday | 5 | 0.16 |
| 2019-07-04 | Independence Day | 4 | sunday | 5 | workday | 5 | 0.30 |
| 2019-09-02 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.23 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 1 | workday | 5 | 0.23 |
| 2019-11-29 | Day after Thanksgiving | 1 | saturday | 1 | workday | 5 | 0.18 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 5 | 0.23 |
| 2019-12-25 | Christmas Day | 0 | saturday | 1 | workday | 5 | 0.16 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 5 | 0.17 |
| 2020-01-01 | New Year's Day | 0 | sunday | 5 | workday | 5 | 0.22 |
| 2020-02-02 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.11 |
| 2020-05-25 | Memorial Day | 2 | sunday | 5 | workday | 5 | 0.19 |
| 2020-07-03 | observed holiday | 5 | sunday | 5 | workday | 5 | 0.16 |
| 2020-07-04 | Independence Day | 5 | sunday | 5 | saturday | 1 | 0.20 |
| 2020-09-07 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.20 |
| 2020-11-26 | Thanksgiving | 3 | saturday | 1 | workday | 5 | 0.32 |
| 2020-11-27 | Day after Thanksgiving | 3 | saturday | 1 | workday | 5 | 0.13 |
| 2020-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 5 | 0.21 |
| 2020-12-25 | Christmas Day | 1 | saturday | 1 | workday | 5 | 0.29 |
| 2020-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 5 | 0.32 |
| 2021-01-01 | New Year's Day | 1 | sunday | 5 | workday | 5 | 0.42 |
| 2021-02-07 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 5 | 0.23 |
| 2021-05-31 | Memorial Day | 2 | sunday | 5 | workday | 5 | 0.21 |
| 2021-07-04 | Independence Day | 5 | sunday | 5 | sunday | 5 | 0.23 |
| 2021-07-05 | observed holiday | 5 | sunday | 5 | workday | 5 | 0.29 |
| 2021-09-06 | Labor Day | 5 | sunday | 5 | workday | 5 | 0.16 |
| 2021-11-25 | Thanksgiving | 0 | saturday | 1 | workday | 5 | 0.40 |
| 2021-11-26 | Day after Thanksgiving | 1 | saturday | 1 | workday | 5 | 0.33 |
| 2021-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 5 | 0.22 |
| 2021-12-25 | Christmas Day | 3 | saturday | 1 | saturday | 1 | 0.41 |
| 2021-12-31 | New Year's Eve | 3 | sunday | 5 | workday | 5 | 0.16 |
| 2022-01-01 | New Year's Day | 2 | sunday | 5 | saturday | 1 | 0.23 |
| 2022-02-13 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 5 | 0.37 |
| 2022-05-30 | Memorial Day | 5 | sunday | 5 | workday | 5 | 0.18 |
| 2022-07-04 | Independence Day | 5 | sunday | 5 | workday | 5 | 0.12 |
| 2022-09-05 | Labor Day | 4 | sunday | 5 | workday | 5 | 0.21 |
| 2022-11-24 | Thanksgiving | 0 | saturday | 1 | workday | 5 | 0.28 |
| 2022-11-25 | Day after Thanksgiving | 1 | saturday | 1 | workday | 5 | 0.11 |
| 2022-12-24 | Christmas Eve | 0 | saturday | 1 | saturday | 1 | 0.31 |
| 2022-12-25 | Christmas Day | 0 | saturday | 1 | sunday | 5 | 0.35 |
| 2022-12-26 | observed holiday | 0 | saturday | 1 | workday | 5 | 0.23 |
| 2022-12-31 | New Year's Eve | 1 | saturday | 1 | saturday | 1 | 0.25 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 1812 | 2022-12-23 | 1 | 0.74 | 0 | 0 | 15603 |
| 1527 | 2022-03-12 | 1 | 0.68 | 1 | 0 | 12110 |
| 383 | 2019-01-20 | 1 | 0.65 | 2 | 0 | 11594 |
| 1459 | 2022-01-03 | 1 | 0.61 | 0 | 0 | 11562 |
| 678 | 2019-11-12 | 1 | 0.58 | 0 | 0 | 12178 |
| 282 | 2018-10-11 | 4 | 0.56 | 0 | 2 | 12007 |
| 1646 | 2022-07-10 | 4 | 0.55 | 2 | 2 | 11315 |
| 1517 | 2022-03-02 | 3 | 0.55 | 0 | 1 | 11172 |
| 1622 | 2022-06-16 | 4 | 0.52 | 0 | 2 | 15648 |
| 566 | 2019-07-23 | 4 | 0.50 | 0 | 2 | 12733 |
| 1444 | 2021-12-19 | 1 | 0.49 | 2 | 0 | 10220 |
| 640 | 2019-10-05 | 3 | 0.49 | 1 | 1 | 10086 |
| 780 | 2020-02-22 | 0 | 0.49 | 1 | 0 | 12971 |
| 450 | 2019-03-29 | 3 | 0.47 | 0 | 1 | 10378 |
| 73 | 2018-03-16 | 3 | 0.46 | 0 | 1 | 10478 |
| 1317 | 2021-08-14 | 4 | 0.45 | 1 | 2 | 13945 |
| 12 | 2018-01-13 | 1 | 0.45 | 1 | 0 | 12122 |
| 185 | 2018-07-06 | 4 | 0.43 | 0 | 2 | 13772 |
| 1623 | 2022-06-17 | 5 | 0.43 | 0 | 2 | 14789 |
| 74 | 2018-03-17 | 3 | 0.43 | 1 | 1 | 9883 |

## BPAT

k = 6, silhouette 0.326, 1821 days, classifier accuracy 0.606.

### Clusters

| cluster | regime | peak_hour | peak_to_mean | min_to_mean | n_days |
| --- | --- | --- | --- | --- | --- |
| 0 | heating | 7 | 1.16 | 0.88 | 415 |
| 1 | heating | 18 | 1.09 | 0.85 | 682 |
| 2 | mild | 18 | 1.14 | 0.82 | 318 |
| 3 | mild | 18 | 1.09 | 0.85 | 243 |
| 4 | cooling | 17 | 1.17 | 0.81 | 72 |
| 5 | cooling | 17 | 1.21 | 0.78 | 91 |

### Days per cluster, by day type and regime

| cluster | workday/heating | workday/mild | workday/cooling | saturday/heating | saturday/mild | saturday/cooling | sunday/heating | sunday/mild | sunday/cooling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 323 | 0 | 0 | 58 | 0 | 0 | 34 | 0 | 0 |
| 1 | 431 | 0 | 0 | 131 | 0 | 0 | 120 | 0 | 0 |
| 2 | 0 | 188 | 0 | 0 | 52 | 0 | 0 | 78 | 0 |
| 3 | 0 | 199 | 0 | 0 | 30 | 0 | 0 | 14 | 0 |
| 4 | 0 | 0 | 60 | 0 | 0 | 8 | 0 | 0 | 4 |
| 5 | 0 | 0 | 63 | 0 | 0 | 7 | 0 | 0 | 21 |

### Special days

| day | name | cluster | as_calendar_type | cluster_of_that_type | weekday_type | cluster_of_weekday_type | distance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018-01-01 | New Year's Day | 1 | sunday | 1 | workday | 1 | 0.11 |
| 2018-02-04 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 1 | 0.13 |
| 2018-05-28 | Memorial Day | 2 | sunday | 1 | workday | 1 | 0.08 |
| 2018-07-04 | Independence Day | 4 | sunday | 1 | workday | 1 | 0.21 |
| 2018-09-03 | Labor Day | 2 | sunday | 1 | workday | 1 | 0.10 |
| 2018-11-22 | Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.20 |
| 2018-11-23 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.08 |
| 2018-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 1 | 0.12 |
| 2018-12-25 | Christmas Day | 1 | saturday | 1 | workday | 1 | 0.11 |
| 2018-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 1 | 0.11 |
| 2019-01-01 | New Year's Day | 1 | sunday | 1 | workday | 1 | 0.16 |
| 2019-02-03 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 1 | 0.23 |
| 2019-05-27 | Memorial Day | 2 | sunday | 1 | workday | 1 | 0.12 |
| 2019-07-04 | Independence Day | 2 | sunday | 1 | workday | 1 | 0.13 |
| 2019-09-02 | Labor Day | 2 | sunday | 1 | workday | 1 | 0.23 |
| 2019-11-28 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.17 |
| 2019-11-29 | Day after Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.13 |
| 2019-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 1 | 0.16 |
| 2019-12-25 | Christmas Day | 1 | saturday | 1 | workday | 1 | 0.13 |
| 2019-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 1 | 0.18 |
| 2020-01-01 | New Year's Day | 1 | sunday | 1 | workday | 1 | 0.19 |
| 2020-02-02 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 1 | 0.16 |
| 2020-05-25 | Memorial Day | 2 | sunday | 1 | workday | 1 | 0.09 |
| 2020-07-03 | observed holiday | 2 | sunday | 1 | workday | 1 | 0.14 |
| 2020-07-04 | Independence Day | 2 | sunday | 1 | saturday | 1 | 0.17 |
| 2020-09-07 | Labor Day | 4 | sunday | 1 | workday | 1 | 0.13 |
| 2020-11-26 | Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.20 |
| 2020-11-27 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.11 |
| 2020-12-24 | Christmas Eve | 0 | saturday | 1 | workday | 1 | 0.12 |
| 2020-12-25 | Christmas Day | 1 | saturday | 1 | workday | 1 | 0.13 |
| 2020-12-31 | New Year's Eve | 1 | saturday | 1 | workday | 1 | 0.14 |
| 2021-01-01 | New Year's Day | 1 | sunday | 1 | workday | 1 | 0.20 |
| 2021-02-07 | Super Bowl Sunday | 1 | saturday | 1 | sunday | 1 | 0.10 |
| 2021-05-31 | Memorial Day | 5 | sunday | 1 | workday | 1 | 0.10 |
| 2021-07-04 | Independence Day | 2 | sunday | 1 | sunday | 1 | 0.17 |
| 2021-07-05 | observed holiday | 2 | sunday | 1 | workday | 1 | 0.21 |
| 2021-09-06 | Labor Day | 2 | sunday | 1 | workday | 1 | 0.18 |
| 2021-11-25 | Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.25 |
| 2021-11-26 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.10 |
| 2021-12-24 | Christmas Eve | 1 | saturday | 1 | workday | 1 | 0.10 |
| 2021-12-25 | Christmas Day | 1 | saturday | 1 | saturday | 1 | 0.11 |
| 2021-12-31 | New Year's Eve | 1 | sunday | 1 | workday | 1 | 0.14 |
| 2022-01-01 | New Year's Day | 0 | sunday | 1 | saturday | 1 | 0.21 |
| 2022-02-13 | Super Bowl Sunday | 0 | saturday | 1 | sunday | 1 | 0.17 |
| 2022-05-30 | Memorial Day | 1 | sunday | 1 | workday | 1 | 0.18 |
| 2022-07-04 | Independence Day | 2 | sunday | 1 | workday | 1 | 0.17 |
| 2022-09-05 | Labor Day | 2 | sunday | 1 | workday | 1 | 0.19 |
| 2022-11-24 | Thanksgiving | 0 | saturday | 1 | workday | 1 | 0.20 |
| 2022-11-25 | Day after Thanksgiving | 1 | saturday | 1 | workday | 1 | 0.09 |
| 2022-12-24 | Christmas Eve | 1 | saturday | 1 | saturday | 1 | 0.32 |
| 2022-12-25 | Christmas Day | 1 | saturday | 1 | sunday | 1 | 0.18 |
| 2022-12-26 | observed holiday | 1 | saturday | 1 | workday | 1 | 0.16 |
| 2022-12-31 | New Year's Eve | 1 | saturday | 1 | saturday | 1 | 0.11 |

### The 20 most atypical days

| index | day | cluster | distance | day_type | regime | daily_mean_mw |
| --- | --- | --- | --- | --- | --- | --- |
| 1056 | 2020-11-25 | 1 | 1.00 | 0 | 0 | 7247 |
| 1552 | 2022-04-07 | 3 | 0.45 | 0 | 1 | 6146 |
| 1512 | 2022-02-25 | 0 | 0.36 | 0 | 0 | 8156 |
| 1589 | 2022-05-14 | 3 | 0.36 | 1 | 1 | 5795 |
| 441 | 2019-03-20 | 3 | 0.36 | 0 | 1 | 5717 |
| 877 | 2020-05-30 | 1 | 0.35 | 1 | 0 | 5631 |
| 826 | 2020-04-09 | 3 | 0.35 | 0 | 1 | 5774 |
| 411 | 2019-02-17 | 1 | 0.34 | 2 | 0 | 7178 |
| 1181 | 2021-03-31 | 0 | 0.33 | 0 | 0 | 6418 |
| 1813 | 2022-12-24 | 1 | 0.32 | 1 | 0 | 7974 |
| 1551 | 2022-04-06 | 0 | 0.32 | 0 | 0 | 6590 |
| 1525 | 2022-03-10 | 0 | 0.31 | 0 | 0 | 7391 |
| 1196 | 2021-04-15 | 3 | 0.31 | 0 | 1 | 5785 |
| 1410 | 2021-11-15 | 1 | 0.30 | 0 | 0 | 6056 |
| 1560 | 2022-04-15 | 0 | 0.29 | 0 | 0 | 6726 |
| 1812 | 2022-12-23 | 0 | 0.29 | 0 | 0 | 9457 |
| 779 | 2020-02-21 | 0 | 0.29 | 0 | 0 | 7051 |
| 1011 | 2020-10-11 | 1 | 0.28 | 2 | 0 | 5250 |
| 1167 | 2021-03-17 | 0 | 0.28 | 0 | 0 | 6594 |
| 1036 | 2020-11-05 | 1 | 0.28 | 0 | 0 | 5672 |
