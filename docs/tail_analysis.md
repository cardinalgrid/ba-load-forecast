# Band and tail, apart: `final6` on the scored days of `frozen6`

281197 scored hours at 11 BAs. Relative error `(actual - forecast) / actual`; the band is the 90 % interval (percentiles 5 and 95 of the errors of the 40 known days nearest in forecast minimum temperature, with the adaptive level). Below: the outcome under the lower bound (the forecast band was too high, an over-forecast beyond the band); above: the outcome over the upper bound (an under-forecast beyond the band). Excesses are in percent of the outcome. Regimes by forecast minimum temperature: cold below 32 F, hot 72 F and above.

## The band

Coverage 89.2 % (target 90), width 10.8 % of the outcome; the outcome leaves the band below on 5.9 % of the hours and above on 4.9 % (5 % each side would be exact).

| ba | hours | coverage_pct | width_pct | below_pct | above_pct |
| --- | --- | --- | --- | --- | --- |
| BPAT | 25728 | 89.19 | 8.91 | 5.24 | 5.57 |
| CISO | 25552 | 88.90 | 11.09 | 6.50 | 4.59 |
| DUK | 25584 | 89.46 | 12.65 | 5.89 | 4.64 |
| ERCO | 25656 | 89.32 | 9.99 | 5.68 | 5.00 |
| FPL | 25056 | 89.55 | 14.10 | 7.04 | 3.42 |
| ISNE | 25630 | 89.47 | 15.27 | 5.66 | 4.87 |
| MISO | 25728 | 89.60 | 7.43 | 5.73 | 4.67 |
| NYIS | 25464 | 89.15 | 10.59 | 5.77 | 5.09 |
| PJM | 25440 | 89.41 | 8.36 | 5.47 | 5.13 |
| SWPP | 25655 | 87.98 | 10.33 | 6.12 | 5.89 |
| TVA | 25704 | 89.32 | 10.56 | 5.51 | 5.17 |
| ALL | 281197 | 89.21 | 10.84 | 5.87 | 4.92 |

## The tail

When the band is left below, the outcome is on average 1.93 % of itself under the lower bound (worst 40.2 %); above, 1.58 % over the upper bound (worst 35.4 %). A generalized Pareto distribution fitted to the excesses gives shape 0.20 below and 0.17 above (a positive shape is a heavy tail; the expected shortfall is finite only below 1). `p90_excess` is the 90th percentile of the observed excesses, `gpd_p80_excess` the 80th percentile implied by the fit, both in percent of the outcome.

| regime | side | hours | exceed_rate_pct | mean_excess_pct | worst_pct | n_excess | shape | scale | mean_excess | p90_excess | gpd_p80_excess | gpd_expected_shortfall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALL | below | 281197 | 5.871 | 1.925 | 40.231 | 16508 | 0.204 | 0.015 | 1.925 | 4.374 | 2.901 | 1.913 |
| ALL | above | 281197 | 4.916 | 1.585 | 35.383 | 13823 | 0.168 | 0.013 | 1.585 | 3.523 | 2.429 | 1.579 |
| cold | below | 32040 | 5.543 | 1.750 | 32.774 | 1776 | 0.126 | 0.015 | 1.750 | 3.947 | 2.723 | 1.746 |
| cold | above | 32040 | 7.154 | 1.836 | 13.699 | 2292 | 0.056 | 0.017 | 1.836 | 4.443 | 2.920 | 1.836 |
| mild | below | 214406 | 6.018 | 1.871 | 40.231 | 12902 | 0.217 | 0.015 | 1.871 | 4.190 | 2.796 | 1.854 |
| mild | above | 214406 | 4.686 | 1.551 | 20.651 | 10048 | 0.163 | 0.013 | 1.551 | 3.440 | 2.384 | 1.547 |
| hot | below | 34751 | 5.266 | 2.478 | 27.158 | 1830 | 0.105 | 0.022 | 2.478 | 5.859 | 3.891 | 2.479 |
| hot | above | 34751 | 4.268 | 1.428 | 35.383 | 1483 | 0.254 | 0.010 | 1.428 | 2.711 | 2.031 | 1.369 |

### By BA

| ba | below_rate_pct | below_mean_excess_pct | below_worst_pct | above_rate_pct | above_mean_excess_pct | above_worst_pct |
| --- | --- | --- | --- | --- | --- | --- |
| BPAT | 5.24 | 1.45 | 40.23 | 5.57 | 1.13 | 13.33 |
| CISO | 6.50 | 1.52 | 11.83 | 4.59 | 1.60 | 9.04 |
| DUK | 5.89 | 2.77 | 36.71 | 4.64 | 1.63 | 8.77 |
| ERCO | 5.68 | 1.87 | 20.74 | 5.00 | 1.75 | 13.19 |
| FPL | 7.04 | 2.75 | 37.47 | 3.42 | 1.83 | 35.38 |
| ISNE | 5.66 | 1.99 | 14.97 | 4.87 | 2.02 | 12.27 |
| MISO | 5.73 | 1.11 | 8.12 | 4.67 | 0.92 | 4.66 |
| NYIS | 5.77 | 1.51 | 11.98 | 5.09 | 1.39 | 14.52 |
| PJM | 5.47 | 1.39 | 10.64 | 5.13 | 1.18 | 20.41 |
| SWPP | 6.12 | 2.46 | 28.55 | 5.89 | 2.63 | 27.05 |
| TVA | 5.51 | 2.15 | 17.11 | 5.17 | 1.31 | 20.65 |

## Attribution to member disagreement

Days are split by the daily mean spread of the ensemble members (maximum minus minimum member, relative to the outcome): the top quarter of days per BA against the rest. A tail that concentrates on days of disagreement is one the model itself signals in advance; one that does not is invisible from the members.

| index | hours | coverage_pct | exceed_below_pct | exceed_above_pct | mean_excess_below_pct | mean_excess_above_pct | width_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| members agree (bottom three quarters) | 210784 | 88.71 | 5.64 | 5.66 | 1.73 | 1.61 | 9.96 |
| members disagree (top quarter) | 70413 | 90.73 | 6.57 | 2.70 | 2.43 | 1.46 | 13.45 |

Share of the hours outside the band that fall on days of disagreement: 21.5 % (a quarter would be no signal); share of the total excess beyond the band on those days: 26.1 %.

Tables as CSV in `results/tail_analysis/`.
