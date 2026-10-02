# Phase O: the severity-scaled move on top of the spread band

Development BAs: DUK, ERCO, MISO, PJM, SWPP, TVA, 2020-12-02 to 2022-12-31, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of training. Only BA-days on which every model produced a forecast are counted; documented load-shed days are left out. Protocol v2 (`docs/phase_g_protocol.md`). The band on the coldest days, where the 90 % interval has covered 77 to 82 % of the hours in the storms. `final10scs` is `final10s` (the NBM spread factor alone, the band of the recipe) with every issued quantile moved up on the cold-decile days by an amount that grows with how far the forecast minimum sits below the cold-decile threshold. Compare with `docs/phase_o_band_s.md` and `docs/phase_o_band_cs.md`.

## All BAs, weighted by mean demand

Mean over BA-days of: hourly MAPE (%), and its median, error at the hour of the actual peak (% of the peak), the negative part of that error (under-forecast), the absolute error in the hour of the peak (h); the worst under-forecast on any day; the fraction of days with a lower MAPE, and with a smaller under-forecast at the peak, than the BA's own forecast (`DF`).

| index | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | win_mape | win_peak_under | worst_peak_under_pct | n_days | n_bas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10scs | 2.17 | 1.85 | -0.02 | -1.17 | 1.25 | 0.62 | 0.25 | -19.15 | 4444 | 6.00 |
| final10scs_ensemble | 2.38 | 2.06 | -1.71 | -2.19 | 1.24 | 0.55 | 0.16 | -20.14 | 4444 | 6.00 |
| final10scs_boosting | 2.43 | 2.14 | -1.42 | -2.08 | 1.45 | 0.54 | 0.18 | -29.38 | 4444 | 6.00 |
| final10scs_additive | 2.68 | 2.36 | -1.95 | -2.50 | 1.34 | 0.49 | 0.16 | -21.65 | 4444 | 6.00 |
| DF | 2.69 | 2.37 | 0.75 | -0.86 | 1.01 | 0.00 | 0.00 | -19.98 | 4444 | 6.00 |
| final10scs_recency | 3.05 | 2.66 | -1.85 | -2.49 | 1.58 | 0.39 | 0.16 | -19.04 | 4444 | 6.00 |

## By BA

| model | ba | mape | mape_median | peak_err_pct | peak_under_pct | abs_peak_hour_err | worst_peak_under_pct | win_mape | win_peak_under | n_days | demand_mw |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | 2.84 | 2.52 | -0.04 | -1.47 | 1.17 | -13.32 |  |  | 747 | 12145.43 |
| DF | ERCO | 2.63 | 2.11 | 0.50 | -1.11 | 0.81 | -14.36 |  |  | 745 | 46853.29 |
| DF | MISO | 2.65 | 2.31 | 2.16 | -0.19 | 0.98 | -6.70 |  |  | 741 | 73714.43 |
| DF | PJM | 2.46 | 2.23 | -0.59 | -1.27 | 1.05 | -8.98 |  |  | 735 | 92099.88 |
| DF | SWPP | 3.76 | 3.48 | 2.57 | -0.43 | 1.20 | -19.98 |  |  | 744 | 31394.87 |
| DF | TVA | 2.23 | 1.92 | -0.13 | -1.24 | 0.98 | -11.24 |  |  | 732 | 18589.75 |
| final10scs | DUK | 2.81 | 2.50 | 0.04 | -1.49 | 1.18 | -12.59 | 0.50 | 0.32 | 747 | 12145.43 |
| final10scs | ERCO | 2.45 | 1.95 | -0.06 | -1.30 | 0.88 | -17.51 | 0.54 | 0.27 | 745 | 46853.29 |
| final10scs | MISO | 1.96 | 1.71 | 0.11 | -0.97 | 1.46 | -7.14 | 0.66 | 0.06 | 741 | 73714.43 |
| final10scs | PJM | 2.00 | 1.76 | -0.18 | -1.17 | 1.29 | -9.31 | 0.65 | 0.43 | 735 | 92099.88 |
| final10scs | SWPP | 2.22 | 1.81 | -0.01 | -1.24 | 1.32 | -19.15 | 0.74 | 0.10 | 744 | 31394.87 |
| final10scs | TVA | 2.59 | 2.25 | 0.31 | -1.31 | 1.14 | -11.14 | 0.38 | 0.32 | 732 | 18589.75 |
| final10scs_additive | DUK | 3.14 | 2.84 | -2.31 | -3.01 | 1.20 | -16.21 | 0.42 | 0.19 | 747 | 12145.43 |
| final10scs_additive | ERCO | 3.29 | 2.87 | -2.65 | -3.23 | 0.97 | -18.25 | 0.34 | 0.11 | 745 | 46853.29 |
| final10scs_additive | MISO | 2.29 | 2.00 | -1.69 | -2.12 | 1.48 | -10.13 | 0.56 | 0.04 | 741 | 73714.43 |
| final10scs_additive | PJM | 2.58 | 2.29 | -1.69 | -2.26 | 1.41 | -12.60 | 0.48 | 0.30 | 735 | 92099.88 |
| final10scs_additive | SWPP | 2.48 | 2.06 | -1.70 | -2.35 | 1.38 | -21.65 | 0.69 | 0.07 | 744 | 31394.87 |
| final10scs_additive | TVA | 3.27 | 3.04 | -2.62 | -3.25 | 1.36 | -14.44 | 0.27 | 0.13 | 732 | 18589.75 |
| final10scs_boosting | DUK | 2.96 | 2.67 | -1.62 | -2.47 | 1.30 | -14.77 | 0.42 | 0.22 | 747 | 12145.43 |
| final10scs_boosting | ERCO | 2.70 | 2.28 | -2.30 | -2.82 | 1.16 | -17.43 | 0.44 | 0.15 | 745 | 46853.29 |
| final10scs_boosting | MISO | 2.16 | 1.87 | -1.07 | -1.67 | 1.58 | -9.57 | 0.60 | 0.04 | 741 | 73714.43 |
| final10scs_boosting | PJM | 2.36 | 2.19 | -1.11 | -1.81 | 1.49 | -12.20 | 0.54 | 0.34 | 735 | 92099.88 |
| final10scs_boosting | SWPP | 2.46 | 2.03 | -1.69 | -2.42 | 1.59 | -29.38 | 0.69 | 0.06 | 744 | 31394.87 |
| final10scs_boosting | TVA | 2.80 | 2.47 | -1.56 | -2.32 | 1.35 | -12.55 | 0.33 | 0.18 | 732 | 18589.75 |
| final10scs_ensemble | DUK | 2.85 | 2.52 | -1.81 | -2.55 | 1.24 | -13.97 | 0.46 | 0.19 | 747 | 12145.43 |
| final10scs_ensemble | ERCO | 2.71 | 2.27 | -2.47 | -2.87 | 0.86 | -17.48 | 0.45 | 0.11 | 745 | 46853.29 |
| final10scs_ensemble | MISO | 2.13 | 1.86 | -1.49 | -1.87 | 1.49 | -9.36 | 0.60 | 0.03 | 741 | 73714.43 |
| final10scs_ensemble | PJM | 2.31 | 2.05 | -1.49 | -1.98 | 1.23 | -11.61 | 0.57 | 0.32 | 735 | 92099.88 |
| final10scs_ensemble | SWPP | 2.20 | 1.81 | -1.42 | -2.04 | 1.27 | -20.14 | 0.72 | 0.06 | 744 | 31394.87 |
| final10scs_ensemble | TVA | 2.84 | 2.53 | -2.11 | -2.71 | 1.18 | -12.60 | 0.31 | 0.11 | 732 | 18589.75 |
| final10scs_recency | DUK | 3.40 | 3.10 | -1.49 | -2.64 | 1.50 | -15.26 | 0.35 | 0.21 | 747 | 12145.43 |
| final10scs_recency | ERCO | 3.29 | 2.74 | -2.58 | -3.16 | 1.09 | -19.04 | 0.32 | 0.14 | 745 | 46853.29 |
| final10scs_recency | MISO | 2.95 | 2.59 | -1.88 | -2.32 | 1.98 | -15.59 | 0.42 | 0.04 | 741 | 73714.43 |
| final10scs_recency | PJM | 2.98 | 2.64 | -1.75 | -2.35 | 1.58 | -16.39 | 0.37 | 0.29 | 735 | 92099.88 |
| final10scs_recency | SWPP | 2.81 | 2.40 | -0.86 | -1.91 | 1.64 | -18.61 | 0.65 | 0.08 | 744 | 31394.87 |
| final10scs_recency | TVA | 3.35 | 2.99 | -2.31 | -3.08 | 1.22 | -15.37 | 0.22 | 0.15 | 732 | 18589.75 |

## The winter events (calendar days of each event)

| model | ba | event | mape | peak_err_pct | peak_under_pct | worst_peak_under_pct | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DF | DUK | uri | 4.88 | -3.81 | -4.48 | -10.25 | 6 |
| DF | ERCO | uri | 3.82 | 0.80 | -0.84 | -1.69 | 2 |
| DF | MISO | uri | 4.05 | 0.76 | -1.69 | -4.70 | 5 |
| DF | PJM | uri | 1.80 | -0.17 | -0.23 | -0.76 | 6 |
| DF | SWPP | uri | 5.65 | 4.83 | 0.00 | 0.00 | 4 |
| DF | TVA | uri | 4.27 | 0.38 | -2.20 | -7.75 | 6 |
| final10scs | DUK | uri | 4.19 | -3.36 | -3.69 | -8.80 | 6 |
| final10scs | ERCO | uri | 6.59 | -8.80 | -8.80 | -9.80 | 2 |
| final10scs | MISO | uri | 3.90 | -3.34 | -3.50 | -7.14 | 5 |
| final10scs | PJM | uri | 1.73 | 0.04 | -0.57 | -2.63 | 6 |
| final10scs | SWPP | uri | 6.14 | 0.40 | -2.66 | -5.96 | 4 |
| final10scs | TVA | uri | 3.87 | -1.52 | -2.59 | -6.68 | 6 |
| final10scs_additive | DUK | uri | 3.91 | -3.97 | -3.97 | -6.69 | 6 |
| final10scs_additive | ERCO | uri | 5.26 | -6.89 | -6.89 | -9.48 | 2 |
| final10scs_additive | MISO | uri | 3.65 | -2.66 | -3.20 | -6.58 | 5 |
| final10scs_additive | PJM | uri | 2.82 | 2.27 | -0.40 | -2.43 | 6 |
| final10scs_additive | SWPP | uri | 6.11 | 2.05 | -1.66 | -4.46 | 4 |
| final10scs_additive | TVA | uri | 3.94 | -0.58 | -1.99 | -5.82 | 6 |
| final10scs_boosting | DUK | uri | 3.88 | -5.03 | -5.03 | -9.61 | 6 |
| final10scs_boosting | ERCO | uri | 8.66 | -13.62 | -13.62 | -15.74 | 2 |
| final10scs_boosting | MISO | uri | 2.65 | -2.90 | -2.95 | -5.31 | 5 |
| final10scs_boosting | PJM | uri | 1.57 | -0.86 | -1.04 | -2.57 | 6 |
| final10scs_boosting | SWPP | uri | 4.88 | -3.23 | -3.99 | -9.76 | 4 |
| final10scs_boosting | TVA | uri | 3.13 | -2.41 | -2.41 | -5.95 | 6 |
| final10scs_ensemble | DUK | uri | 4.11 | -4.86 | -4.86 | -8.07 | 6 |
| final10scs_ensemble | ERCO | uri | 6.37 | -8.91 | -8.91 | -10.45 | 2 |
| final10scs_ensemble | MISO | uri | 3.79 | -3.71 | -3.71 | -7.06 | 5 |
| final10scs_ensemble | PJM | uri | 2.00 | 0.55 | -0.56 | -3.05 | 6 |
| final10scs_ensemble | SWPP | uri | 5.84 | -1.15 | -3.33 | -7.30 | 4 |
| final10scs_ensemble | TVA | uri | 3.56 | -1.63 | -2.30 | -5.75 | 6 |
| final10scs_recency | DUK | uri | 4.82 | -5.61 | -5.61 | -8.14 | 6 |
| final10scs_recency | ERCO | uri | 6.07 | -5.61 | -5.61 | -10.26 | 2 |
| final10scs_recency | MISO | uri | 6.74 | -6.06 | -6.06 | -9.68 | 5 |
| final10scs_recency | PJM | uri | 2.45 | 0.50 | -0.84 | -4.36 | 6 |
| final10scs_recency | SWPP | uri | 6.47 | -2.75 | -4.55 | -10.56 | 4 |
| final10scs_recency | TVA | uri | 4.24 | -1.89 | -2.86 | -6.14 | 6 |
| DF | DUK | elliott | 3.97 | -3.57 | -3.57 | -10.55 | 4 |
| DF | ERCO | elliott | 6.90 | -5.44 | -6.59 | -11.44 | 5 |
| DF | MISO | elliott | 4.82 | 0.77 | -1.22 | -2.84 | 5 |
| DF | PJM | elliott | 3.51 | -3.99 | -3.99 | -7.05 | 5 |
| DF | SWPP | elliott | 4.80 | 0.22 | -1.65 | -4.50 | 5 |
| DF | TVA | elliott | 4.09 | 1.01 | -0.85 | -2.55 | 3 |
| final10scs | DUK | elliott | 3.72 | -0.11 | -1.55 | -3.93 | 4 |
| final10scs | ERCO | elliott | 6.20 | -0.56 | -1.93 | -5.25 | 5 |
| final10scs | MISO | elliott | 3.47 | -1.83 | -2.72 | -5.13 | 5 |
| final10scs | PJM | elliott | 3.91 | -3.02 | -3.03 | -6.93 | 5 |
| final10scs | SWPP | elliott | 4.52 | 0.57 | -1.69 | -5.40 | 5 |
| final10scs | TVA | elliott | 4.88 | 2.01 | -0.19 | -0.58 | 3 |
| final10scs_additive | DUK | elliott | 3.89 | -4.32 | -4.32 | -6.30 | 4 |
| final10scs_additive | ERCO | elliott | 7.53 | -5.95 | -6.29 | -12.74 | 5 |
| final10scs_additive | MISO | elliott | 3.51 | -3.79 | -4.00 | -6.60 | 5 |
| final10scs_additive | PJM | elliott | 3.37 | -2.64 | -2.64 | -7.54 | 5 |
| final10scs_additive | SWPP | elliott | 3.44 | -2.75 | -3.00 | -6.28 | 5 |
| final10scs_additive | TVA | elliott | 4.73 | -0.54 | -0.59 | -1.27 | 3 |
| final10scs_boosting | DUK | elliott | 4.03 | -3.08 | -3.08 | -6.28 | 4 |
| final10scs_boosting | ERCO | elliott | 7.22 | -11.93 | -11.93 | -17.43 | 5 |
| final10scs_boosting | MISO | elliott | 3.52 | -2.09 | -3.12 | -4.27 | 5 |
| final10scs_boosting | PJM | elliott | 3.88 | -4.52 | -4.52 | -7.50 | 5 |
| final10scs_boosting | SWPP | elliott | 4.60 | -3.35 | -4.18 | -12.42 | 5 |
| final10scs_boosting | TVA | elliott | 4.33 | -2.05 | -2.05 | -3.07 | 3 |
| final10scs_ensemble | DUK | elliott | 3.60 | -4.60 | -4.60 | -5.80 | 4 |
| final10scs_ensemble | ERCO | elliott | 6.43 | -7.92 | -7.92 | -12.26 | 5 |
| final10scs_ensemble | MISO | elliott | 3.69 | -4.03 | -4.30 | -7.76 | 5 |
| final10scs_ensemble | PJM | elliott | 4.16 | -4.98 | -4.98 | -9.90 | 5 |
| final10scs_ensemble | SWPP | elliott | 3.99 | -4.19 | -4.46 | -10.42 | 5 |
| final10scs_ensemble | TVA | elliott | 4.07 | -2.07 | -2.07 | -2.63 | 3 |
| final10scs_recency | DUK | elliott | 4.08 | -6.68 | -6.68 | -9.35 | 4 |
| final10scs_recency | ERCO | elliott | 5.48 | -4.79 | -4.79 | -11.25 | 5 |
| final10scs_recency | MISO | elliott | 6.72 | -7.67 | -7.67 | -15.59 | 5 |
| final10scs_recency | PJM | elliott | 5.96 | -8.01 | -8.01 | -16.39 | 5 |
| final10scs_recency | SWPP | elliott | 4.79 | -6.95 | -6.95 | -13.10 | 5 |
| final10scs_recency | TVA | elliott | 3.83 | -3.80 | -3.80 | -4.81 | 3 |

## Special days and their eves

The same metrics on the special days of `calendar_us` (holidays, Super Bowl Sunday) and on the day before each: the days the special-day treatments are about.

| index | model | days | mape | peak_err_pct | peak_under_pct | win_mape | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | final10scs_ensemble | eve | 3.11 | -1.28 | -2.35 | 0.56 | 145 |
| 9 | final10scs_boosting | eve | 3.30 | -0.87 | -2.22 | 0.54 | 145 |
| 7 | final10scs | eve | 3.34 | 0.81 | -1.33 | 0.55 | 145 |
| 8 | final10scs_additive | eve | 3.43 | -1.29 | -2.53 | 0.56 | 145 |
| 11 | final10scs_recency | eve | 3.62 | -1.87 | -2.89 | 0.50 | 145 |
| 6 | DF | eve | 3.77 | 1.46 | -1.04 |  | 145 |
| 4 | final10scs_ensemble | special | 2.99 | -2.01 | -2.63 | 0.63 | 147 |
| 1 | final10scs | special | 3.15 | 0.14 | -1.42 | 0.61 | 147 |
| 2 | final10scs_additive | special | 3.19 | -2.58 | -3.11 | 0.59 | 147 |
| 3 | final10scs_boosting | special | 3.29 | -1.75 | -2.49 | 0.59 | 147 |
| 5 | final10scs_recency | special | 3.61 | -1.79 | -2.84 | 0.58 | 147 |
| 0 | DF | special | 4.07 | 1.14 | -1.13 |  | 147 |

## Quantile forecasts

Pinball loss of the 5th, 50th and 95th percentiles (in percent of the actual), coverage and mean relative width of the 90% band, and the share of days whose actual peak fell inside the band at the hour of the peak; on all days, on the winter-event days and on the 30 coldest days of each BA.

| model | days | pinball_05 | pinball_50 | pinball_95 | coverage_90 | width_90 | peak_in_band | winkler_90 | crps | n_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| final10scs | all | 0.358 | 1.172 | 0.341 | 0.888 | 10.478 | 0.888 | 13.990 | 1.535 | 4317 |
| final10scs | events | 0.558 | 2.107 | 0.647 | 0.773 | 14.055 | 0.821 | 24.104 | 2.995 | 56 |
| final10scs | cold_mornings | 0.517 | 1.726 | 0.544 | 0.848 | 15.093 | 0.844 | 21.206 | 2.471 | 180 |

## Documented load-shed days (left out of every table above)

On these BA-days the load that occurred is the load served under firm load shed, not the demand (`docs/load_shed_days.csv` gives the source of each). No forecast can be scored against it; the metrics are shown for the record.

| index | ba | day | model | mape | peak_err_pct | peak_under_pct |
| --- | --- | --- | --- | --- | --- | --- |
| 4445 | DUK | 2022-12-24 | DF | 7.96 | -10.53 | -10.53 |
| 4444 | DUK | 2022-12-24 | final10scs | 7.00 | -6.74 | -6.74 |
| 4440 | DUK | 2022-12-24 | final10scs_additive | 8.92 | -12.68 | -12.68 |
| 4441 | DUK | 2022-12-24 | final10scs_boosting | 10.90 | -17.09 | -17.09 |
| 4443 | DUK | 2022-12-24 | final10scs_ensemble | 10.08 | -13.84 | -13.84 |
| 4442 | DUK | 2022-12-24 | final10scs_recency | 10.63 | -11.43 | -11.43 |
| 4937 | ERCO | 2021-02-17 | DF | 30.02 | 22.28 | 0.00 |
| 4936 | ERCO | 2021-02-17 | final10scs | 31.81 | 25.11 | 0.00 |
| 4932 | ERCO | 2021-02-17 | final10scs_additive | 29.56 | 25.22 | 0.00 |
| 4933 | ERCO | 2021-02-17 | final10scs_boosting | 28.85 | 23.03 | 0.00 |
| 4935 | ERCO | 2021-02-17 | final10scs_ensemble | 31.76 | 26.20 | 0.00 |
| 4934 | ERCO | 2021-02-17 | final10scs_recency | 38.48 | 31.79 | 0.00 |
| 4943 | ERCO | 2021-02-18 | DF | 18.74 | 16.29 | 0.00 |
| 4942 | ERCO | 2021-02-18 | final10scs | 4.22 | 2.65 | 0.00 |
| 4938 | ERCO | 2021-02-18 | final10scs_additive | 13.29 | 11.84 | 0.00 |
| 4939 | ERCO | 2021-02-18 | final10scs_boosting | 4.23 | -7.71 | -7.71 |
| 4941 | ERCO | 2021-02-18 | final10scs_ensemble | 4.31 | 1.50 | 0.00 |
| 4940 | ERCO | 2021-02-18 | final10scs_recency | 5.36 | 2.19 | 0.00 |
| 9425 | MISO | 2021-02-16 | DF | 7.05 | 10.44 | 0.00 |
| 9424 | MISO | 2021-02-16 | final10scs | 1.65 | 1.40 | 0.00 |
| 9420 | MISO | 2021-02-16 | final10scs_additive | 2.24 | 2.04 | 0.00 |
| 9421 | MISO | 2021-02-16 | final10scs_boosting | 1.52 | 0.96 | 0.00 |
| 9423 | MISO | 2021-02-16 | final10scs_ensemble | 1.56 | 0.51 | 0.00 |
| 9422 | MISO | 2021-02-16 | final10scs_recency | 3.83 | -2.20 | -2.20 |
| 18281 | SWPP | 2021-02-15 | DF | 4.31 | 3.41 | 0.00 |
| 18280 | SWPP | 2021-02-15 | final10scs | 2.48 | -2.09 | -2.09 |
| 18276 | SWPP | 2021-02-15 | final10scs_additive | 2.57 | 1.33 | 0.00 |
| 18277 | SWPP | 2021-02-15 | final10scs_boosting | 6.68 | -8.01 | -8.01 |
| 18279 | SWPP | 2021-02-15 | final10scs_ensemble | 2.87 | -3.68 | -3.68 |
| 18278 | SWPP | 2021-02-15 | final10scs_recency | 4.67 | -4.95 | -4.95 |
| 18287 | SWPP | 2021-02-16 | DF | 10.57 | 6.93 | 0.00 |
| 18286 | SWPP | 2021-02-16 | final10scs | 4.01 | 0.22 | 0.00 |
| 18282 | SWPP | 2021-02-16 | final10scs_additive | 7.69 | 3.65 | 0.00 |
| 18283 | SWPP | 2021-02-16 | final10scs_boosting | 3.28 | -6.32 | -6.32 |
| 18285 | SWPP | 2021-02-16 | final10scs_ensemble | 3.80 | -0.84 | -0.84 |
| 18284 | SWPP | 2021-02-16 | final10scs_recency | 2.38 | -0.44 | -0.44 |
| 26663 | TVA | 2022-12-23 | DF | 3.74 | -6.27 | -6.27 |
| 26662 | TVA | 2022-12-23 | final10scs | 7.05 | -9.76 | -9.76 |
| 26658 | TVA | 2022-12-23 | final10scs_additive | 6.10 | -4.61 | -4.61 |
| 26659 | TVA | 2022-12-23 | final10scs_boosting | 15.03 | -15.47 | -15.47 |
| 26661 | TVA | 2022-12-23 | final10scs_ensemble | 9.72 | -10.91 | -10.91 |
| 26660 | TVA | 2022-12-23 | final10scs_recency | 10.25 | -13.32 | -13.32 |
| 26669 | TVA | 2022-12-24 | DF | 3.88 | -8.57 | -8.57 |
| 26668 | TVA | 2022-12-24 | final10scs | 4.05 | -11.54 | -11.54 |
| 26664 | TVA | 2022-12-24 | final10scs_additive | 4.10 | -10.03 | -10.03 |
| 26665 | TVA | 2022-12-24 | final10scs_boosting | 7.18 | -15.19 | -15.19 |
| 26667 | TVA | 2022-12-24 | final10scs_ensemble | 6.22 | -12.64 | -12.64 |
| 26666 | TVA | 2022-12-24 | final10scs_recency | 7.90 | -12.89 | -12.89 |

## Diebold-Mariano against the BA's forecast (daily MAPE)

Negative statistics favour the model; p-values from the normal approximation.

| model | ba | metric | dm_stat | p_value | n_days |
| --- | --- | --- | --- | --- | --- |
| final10scs | DUK | mape | -0.554 | 0.580 | 747 |
| final10scs | ERCO | mape | -3.211 | 0.001 | 745 |
| final10scs | MISO | mape | -11.803 | 0.000 | 741 |
| final10scs | PJM | mape | -9.361 | 0.000 | 735 |
| final10scs | SWPP | mape | -18.386 | 0.000 | 744 |
| final10scs | TVA | mape | 7.902 | 0.000 | 732 |
| final10scs_additive | DUK | mape | 4.810 | 0.000 | 747 |
| final10scs_additive | ERCO | mape | 9.376 | 0.000 | 745 |
| final10scs_additive | MISO | mape | -4.992 | 0.000 | 741 |
| final10scs_additive | PJM | mape | 2.180 | 0.029 | 735 |
| final10scs_additive | SWPP | mape | -13.905 | 0.000 | 744 |
| final10scs_additive | TVA | mape | 16.869 | 0.000 | 732 |
| final10scs_boosting | DUK | mape | 2.126 | 0.033 | 747 |
| final10scs_boosting | ERCO | mape | 1.164 | 0.245 | 745 |
| final10scs_boosting | MISO | mape | -7.443 | 0.000 | 741 |
| final10scs_boosting | PJM | mape | -2.017 | 0.044 | 735 |
| final10scs_boosting | SWPP | mape | -13.743 | 0.000 | 744 |
| final10scs_boosting | TVA | mape | 11.467 | 0.000 | 732 |
| final10scs_ensemble | DUK | mape | 0.134 | 0.894 | 747 |
| final10scs_ensemble | ERCO | mape | 1.360 | 0.174 | 745 |
| final10scs_ensemble | MISO | mape | -7.559 | 0.000 | 741 |
| final10scs_ensemble | PJM | mape | -3.125 | 0.002 | 735 |
| final10scs_ensemble | SWPP | mape | -17.687 | 0.000 | 744 |
| final10scs_ensemble | TVA | mape | 11.683 | 0.000 | 732 |
| final10scs_recency | DUK | mape | 9.074 | 0.000 | 747 |
| final10scs_recency | ERCO | mape | 8.848 | 0.000 | 745 |
| final10scs_recency | MISO | mape | 3.697 | 0.000 | 741 |
| final10scs_recency | PJM | mape | 9.266 | 0.000 | 735 |
| final10scs_recency | SWPP | mape | -10.439 | 0.000 | 744 |
| final10scs_recency | TVA | mape | 17.916 | 0.000 | 732 |

## Coverage

Fraction of BA-days each model produced a scorable forecast for.

| model | scored_fraction |
| --- | --- |
| DF | 0.995 |
| final10scs | 0.994 |
| final10scs_additive | 0.976 |
| final10scs_boosting | 0.994 |
| final10scs_ensemble | 0.994 |
| final10scs_recency | 0.994 |
