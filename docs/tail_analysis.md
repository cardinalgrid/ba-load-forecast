# Band and tail, apart: `final4` on the scored days of `frozen4`

281245 scored hours at 11 BAs. Relative error `(actual - forecast) / actual`; the band is the 90 % interval (percentiles 5 and 95 of the errors of the 40 known days nearest in forecast minimum temperature, with the adaptive level). Below: the outcome under the lower bound (the forecast band was too high, an over-forecast beyond the band); above: the outcome over the upper bound (an under-forecast beyond the band). Excesses are in percent of the outcome. Regimes by forecast minimum temperature: cold below 32 F, hot 72 F and above.

## The band

Coverage 89.2 % (target 90), width 11.7 % of the outcome; the outcome leaves the band below on 5.8 % of the hours and above on 5.0 % (5 % each side would be exact).

| ba | hours | coverage_pct | width_pct | below_pct | above_pct |
| --- | --- | --- | --- | --- | --- |
| BPAT | 25728 | 89.16 | 9.53 | 5.28 | 5.55 |
| CISO | 25552 | 88.98 | 11.69 | 6.26 | 4.76 |
| DUK | 25584 | 89.44 | 14.20 | 6.07 | 4.49 |
| ERCO | 25656 | 89.19 | 10.70 | 5.46 | 5.35 |
| FPL | 25104 | 89.56 | 15.96 | 6.98 | 3.47 |
| ISNE | 25630 | 89.40 | 15.89 | 5.67 | 4.94 |
| MISO | 25728 | 89.61 | 7.93 | 5.66 | 4.73 |
| NYIS | 25464 | 89.15 | 11.04 | 5.57 | 5.27 |
| PJM | 25440 | 89.42 | 9.25 | 5.34 | 5.24 |
| SWPP | 25655 | 88.16 | 10.85 | 5.84 | 6.00 |
| TVA | 25704 | 89.33 | 11.82 | 5.45 | 5.22 |
| ALL | 281245 | 89.22 | 11.71 | 5.78 | 5.00 |

## The tail

When the band is left below, the outcome is on average 2.04 % of itself under the lower bound (worst 41.2 %); above, 1.70 % over the upper bound (worst 33.3 %). A generalized Pareto distribution fitted to the excesses gives shape 0.19 below and 0.15 above (a positive shape is a heavy tail; the expected shortfall is finite only below 1). `p90_excess` is the 90th percentile of the observed excesses, `gpd_p80_excess` the 80th percentile implied by the fit, both in percent of the outcome.

| regime | side | hours | exceed_rate_pct | mean_excess_pct | worst_pct | n_excess | shape | scale | mean_excess | p90_excess | gpd_p80_excess | gpd_expected_shortfall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALL | below | 281245 | 5.777 | 2.035 | 41.173 | 16248 | 0.189 | 0.016 | 2.035 | 4.585 | 3.090 | 2.025 |
| ALL | above | 281245 | 5.005 | 1.695 | 33.254 | 14075 | 0.154 | 0.014 | 1.695 | 3.797 | 2.613 | 1.691 |
| cold | below | 32040 | 5.209 | 1.948 | 33.458 | 1669 | 0.127 | 0.017 | 1.948 | 4.383 | 3.030 | 1.944 |
| cold | above | 32040 | 7.615 | 1.872 | 15.036 | 2440 | 0.055 | 0.018 | 1.872 | 4.568 | 2.977 | 1.872 |
| mild | below | 214454 | 5.931 | 1.967 | 41.173 | 12720 | 0.202 | 0.016 | 1.967 | 4.405 | 2.965 | 1.954 |
| mild | above | 214454 | 4.784 | 1.653 | 20.768 | 10260 | 0.158 | 0.014 | 1.653 | 3.698 | 2.546 | 1.650 |
| hot | below | 34751 | 5.349 | 2.581 | 23.595 | 1859 | 0.100 | 0.023 | 2.581 | 5.926 | 4.054 | 2.580 |
| hot | above | 34751 | 3.957 | 1.697 | 33.254 | 1375 | 0.220 | 0.013 | 1.697 | 3.459 | 2.494 | 1.655 |

### By BA

| ba | below_rate_pct | below_mean_excess_pct | below_worst_pct | above_rate_pct | above_mean_excess_pct | above_worst_pct |
| --- | --- | --- | --- | --- | --- | --- |
| BPAT | 5.28 | 1.42 | 39.94 | 5.55 | 1.20 | 15.04 |
| CISO | 6.26 | 1.64 | 11.87 | 4.76 | 1.73 | 10.30 |
| DUK | 6.07 | 2.95 | 41.17 | 4.49 | 1.89 | 11.32 |
| ERCO | 5.46 | 2.12 | 23.60 | 5.35 | 1.68 | 13.19 |
| FPL | 6.98 | 2.67 | 32.13 | 3.47 | 1.98 | 33.25 |
| ISNE | 5.67 | 2.18 | 14.65 | 4.94 | 2.12 | 15.08 |
| MISO | 5.66 | 1.21 | 8.75 | 4.73 | 1.00 | 4.93 |
| NYIS | 5.57 | 1.70 | 17.48 | 5.27 | 1.37 | 13.21 |
| PJM | 5.34 | 1.53 | 11.38 | 5.24 | 1.25 | 20.77 |
| SWPP | 5.84 | 2.42 | 30.12 | 6.00 | 2.66 | 27.29 |
| TVA | 5.45 | 2.31 | 16.03 | 5.22 | 1.75 | 19.25 |

## Attribution to member disagreement

Days are split by the daily mean spread of the ensemble members (maximum minus minimum member, relative to the outcome): the top quarter of days per BA against the rest. A tail that concentrates on days of disagreement is one the model itself signals in advance; one that does not is invisible from the members.

| index | hours | coverage_pct | exceed_below_pct | exceed_above_pct | mean_excess_below_pct | mean_excess_above_pct | width_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| members agree (bottom three quarters) | 210832 | 89.78 | 5.26 | 4.96 | 1.94 | 1.62 | 11.50 |
| members disagree (top quarter) | 70413 | 87.53 | 7.34 | 5.13 | 2.24 | 1.92 | 12.32 |

Share of the hours outside the band that fall on days of disagreement: 29.0 % (a quarter would be no signal); share of the total excess beyond the band on those days: 32.6 %.

Tables as CSV in `results/tail_analysis/`.
