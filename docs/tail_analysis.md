# Band and tail, apart: `final5` on the scored days of `frozen5`

281245 scored hours at 11 BAs. Relative error `(actual - forecast) / actual`; the band is the 90 % interval (percentiles 5 and 95 of the errors of the 40 known days nearest in forecast minimum temperature, with the adaptive level). Below: the outcome under the lower bound (the forecast band was too high, an over-forecast beyond the band); above: the outcome over the upper bound (an under-forecast beyond the band). Excesses are in percent of the outcome. Regimes by forecast minimum temperature: cold below 32 F, hot 72 F and above.

## The band

Coverage 89.2 % (target 90), width 11.7 % of the outcome; the outcome leaves the band below on 5.8 % of the hours and above on 5.0 % (5 % each side would be exact).

| ba | hours | coverage_pct | width_pct | below_pct | above_pct |
| --- | --- | --- | --- | --- | --- |
| BPAT | 25728 | 89.16 | 9.51 | 5.30 | 5.54 |
| CISO | 25552 | 88.98 | 11.68 | 6.27 | 4.75 |
| DUK | 25584 | 89.38 | 14.34 | 6.17 | 4.44 |
| ERCO | 25656 | 89.27 | 10.74 | 5.47 | 5.26 |
| FPL | 25104 | 89.48 | 16.05 | 7.05 | 3.46 |
| ISNE | 25630 | 89.41 | 15.95 | 5.63 | 4.96 |
| MISO | 25728 | 89.63 | 7.93 | 5.73 | 4.64 |
| NYIS | 25464 | 89.15 | 11.01 | 5.72 | 5.13 |
| PJM | 25440 | 89.44 | 9.25 | 5.46 | 5.10 |
| SWPP | 25655 | 88.10 | 10.87 | 5.84 | 6.06 |
| TVA | 25704 | 89.33 | 11.79 | 5.45 | 5.21 |
| ALL | 281245 | 89.21 | 11.73 | 5.83 | 4.96 |

## The tail

When the band is left below, the outcome is on average 2.02 % of itself under the lower bound (worst 40.5 %); above, 1.68 % over the upper bound (worst 34.2 %). A generalized Pareto distribution fitted to the excesses gives shape 0.19 below and 0.16 above (a positive shape is a heavy tail; the expected shortfall is finite only below 1). `p90_excess` is the 90th percentile of the observed excesses, `gpd_p80_excess` the 80th percentile implied by the fit, both in percent of the outcome.

| regime | side | hours | exceed_rate_pct | mean_excess_pct | worst_pct | n_excess | shape | scale | mean_excess | p90_excess | gpd_p80_excess | gpd_expected_shortfall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALL | below | 281245 | 5.825 | 2.024 | 40.537 | 16383 | 0.194 | 0.016 | 2.024 | 4.579 | 3.068 | 2.015 |
| ALL | above | 281245 | 4.963 | 1.678 | 34.243 | 13957 | 0.157 | 0.014 | 1.678 | 3.790 | 2.584 | 1.674 |
| cold | below | 32040 | 5.506 | 1.929 | 34.448 | 1764 | 0.123 | 0.017 | 1.929 | 4.213 | 3.004 | 1.925 |
| cold | above | 32040 | 7.366 | 1.849 | 14.947 | 2360 | 0.058 | 0.017 | 1.849 | 4.530 | 2.938 | 1.849 |
| mild | below | 214454 | 5.958 | 1.959 | 40.537 | 12778 | 0.208 | 0.015 | 1.959 | 4.402 | 2.947 | 1.946 |
| mild | above | 214454 | 4.762 | 1.639 | 20.601 | 10213 | 0.160 | 0.014 | 1.639 | 3.682 | 2.524 | 1.637 |
| hot | below | 34751 | 5.298 | 2.570 | 23.759 | 1841 | 0.107 | 0.023 | 2.570 | 5.984 | 4.031 | 2.570 |
| hot | above | 34751 | 3.983 | 1.676 | 34.243 | 1384 | 0.233 | 0.013 | 1.676 | 3.400 | 2.446 | 1.633 |

### By BA

| ba | below_rate_pct | below_mean_excess_pct | below_worst_pct | above_rate_pct | above_mean_excess_pct | above_worst_pct |
| --- | --- | --- | --- | --- | --- | --- |
| BPAT | 5.30 | 1.43 | 40.54 | 5.54 | 1.19 | 14.95 |
| CISO | 6.27 | 1.64 | 12.48 | 4.75 | 1.74 | 10.23 |
| DUK | 6.17 | 2.89 | 40.18 | 4.44 | 1.85 | 11.46 |
| ERCO | 5.47 | 2.10 | 23.35 | 5.26 | 1.69 | 12.69 |
| FPL | 7.05 | 2.65 | 34.05 | 3.46 | 1.87 | 34.24 |
| ISNE | 5.63 | 2.18 | 14.17 | 4.96 | 2.08 | 14.85 |
| MISO | 5.73 | 1.21 | 8.91 | 4.64 | 1.00 | 5.04 |
| NYIS | 5.72 | 1.68 | 17.00 | 5.13 | 1.39 | 14.05 |
| PJM | 5.46 | 1.54 | 11.28 | 5.10 | 1.27 | 20.42 |
| SWPP | 5.84 | 2.40 | 29.87 | 6.06 | 2.56 | 27.14 |
| TVA | 5.45 | 2.35 | 16.10 | 5.21 | 1.73 | 19.67 |

## Attribution to member disagreement

Days are split by the daily mean spread of the ensemble members (maximum minus minimum member, relative to the outcome): the top quarter of days per BA against the rest. A tail that concentrates on days of disagreement is one the model itself signals in advance; one that does not is invisible from the members.

| index | hours | coverage_pct | exceed_below_pct | exceed_above_pct | mean_excess_below_pct | mean_excess_above_pct | width_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| members agree (bottom three quarters) | 210808 | 88.59 | 5.70 | 5.71 | 1.89 | 1.69 | 10.69 |
| members disagree (top quarter) | 70437 | 91.07 | 6.21 | 2.72 | 2.40 | 1.63 | 14.83 |

Share of the hours outside the band that fall on days of disagreement: 20.7 % (a quarter would be no signal); share of the total excess beyond the band on those days: 24.1 %.

Tables as CSV in `results/tail_analysis/`.
