# The test on January to September 2026: protocol fixed before the test

Written on 15 October 2026. No forecast of this recipe has been produced for any day of 2026 at the time of writing,
and no number of the test is known. The commit that adds this file fixes the recipe, the data, the period, the scoring
and the reports; the test is run once on that commit.

## Why a new test

The years 2023 to 2025 were looked at more than once while the recipe was built (`docs/frozen_evaluation*.md`, six
looks at the eleven development BAs, then the 43 BAs of the station map). Their numbers are honest about what the
recipe does on those years, but the choices of phases G to V were made with them in view. January to September 2026
has never been forecast by any version of the recipe. It is the first period on which the recipe as frozen here has
not been tuned.

## The recipe

`final10s` of section 8n of `docs/methods.md` (the recipe of release 1.0.0) with two changes decided before this test:

1. **The extra stations of phase U** (section 8u) for the temperature of ten BAs: SOCO, LDWP, TPWR, NWMT, WACM, BANC,
   PGE, PACE, AECI and NEVP (`Loader(stations="extra", extra_fields=False)`; humidity and wind stay on the BA's
   station). The HRRR, NBM and GFS are read at the new stations as at the others. The choice was made after looking at
   2023 to 2025, so 2026 is its first clean test too.
2. **The 5th and 95th percentiles at their fixed levels** (section 8v). The band is read at the adaptive level and is
   scored as the 90 % interval it is (coverage, Winkler score, peak in the band). The CRPS and the pinball losses at
   0.05 and 0.95 now score quantiles issued at those fixed levels, with the same spread factor and peak shift as the
   band (`evaluate.py`, `FIXED_EDGES`). The point forecast is unchanged.

Nothing else changes. None of the phase V mechanisms enters (none was adopted, section 8w), and its rule stays as
written. The run is group `t2026` of `scripts/run_phase_e.py`, model `recipe2026`, on the code of the commit that
adds this file.

## Data

- Load and the BA's own day-ahead forecast (`D` and `DF`) from Form EIA-930, as published when downloaded, under
  protocol v2 unchanged (section 8d: fault days of `DF` and spurious peaks of `D` excluded, hour labels as documented).
- Forecast temperature from the HRRR, NBM and GFS archives at the stations of the station map and of phase U, as seen
  at the 9 a.m. cut-off.
- Observed temperature from the ISD-Lite where it exists and from GHCNh and ASOS otherwise (the ISD-Lite files of
  the stations in use end on 27 August 2025; section 2 describes the supplement).
- WACM stopped reporting as a balancing authority on 1 April 2026; it is scored on the days it reported.

## Period and warm-up

The run starts on 2025-01-01 and ends on 2026-09-30. 2025 is a warm-up: several rules of the band compare the day
with the run's own earlier forecasts and stay off until 100 of them exist (section 8w), and the adaptive level needs
its own history. Only 2026-01-01 to 2026-09-30 is scored. The 2025 part of the run is not reported as a result.

## What is reported

`python scripts/test_2026.py --runs <runs>` writes, from the scripts used for 2023 to 2025:

1. `docs/test_2026_scoreboard.md`: per BA, the MAPE of the recipe and of `DF` on the days both scored, the peak
   under-forecast, coverage and Winkler score of the band, and the Diebold-Mariano test of the daily MAPE; aggregates
   on the 38 BAs whose `DF` the EIA lists as comparable with their demand, on the 11 development BAs and on the 27 new
   comparable BAs (the five others are kept in the evaluation of the forecaster only).
2. `docs/test_2026_strata.md`: on the 38 comparable BAs, demand-weighted MAPE, peak under-forecast, peak error, CRPS,
   Winkler score and coverage over the period, by season, on the 30 coldest mornings and on the 30 days of largest
   actual peak of each BA, with the count of BAs better and worse than `DF`.
3. `docs/test_2026_strata_dev.md`: the same on the 11 development BAs.

The headline is the demand-weighted MAPE of the recipe against `DF` on the 38 comparable BAs, with the number of BAs
ahead and behind (and of those with p < 0.05). On 2023 to 2025 these were 2.41 % against 3.16 %, 26 ahead and 12
behind (section 8n). The peak under-forecast on the 30 coldest mornings and the 30 largest peaks is reported next to
it, whatever its sign.

No event list for 2026 is fixed here. The strata of the coldest mornings and the largest peaks carry the extremes of
the period. A cold or heat event named in an official review would be reported only as a descriptive addition,
separate from the test.

## What may not happen after the run

- No setting of the recipe changes and no other variant is reported as the test.
- If a defect is found in the data or the code, it is reported with the result. A rerun after a fix is reported next
  to the first run, never in its place.
- The protocol v2 exclusions are applied by the code as they stand; no BA-day is removed by hand.

## Addendum, 15 October 2026, before the run: version 5.0 of the NBM

Found while gathering the 2026 inputs, before any forecast of 2026 was produced. The NBM archive moved from version 4.3
to version 5.0 in May 2026: the 4.3 tree ends with the runs of 5 May, the 5.0 tree starts that day, and 5 May is the only
day both hold. The 5.0 files keep the grid, the projection and the encoding of 4.3 (same GeoTIFF keys, checked on both
trees), so the stations are read at the same cells. The temperature keeps its name (`temp`); the spread of the 2 m
temperature that sets the width factor of the band is published as `temppstddev` instead of `tempstddev`. On the
two runs of 5 May, over the whole grid and the leads of a 9 a.m. cut-off, the 5.0 spread is about 0.9 times the 4.3
spread (median ratio 0.85 to 0.95 by lead, correlation 0.82 to 0.86).

Decision, taken now and not revisited after the run: the recipe reads the 5.0 tree as it is published, the spread
included, with no rescaling. The width factor compares the day's spread with its median over the 40 nearest known days,
which until May 2027 are mostly days of version 4.3; from May to September 2026 the factor can therefore sit about
10 % lower than the same weather would have given under 4.3, and the band be narrower. This is reported with the result
(coverage and Winkler score by month, May to September against January to April), and is a limitation of the test, not
a reason to change it. `nbm.py` reads the 5.0 tree from commit `c60286b` on.
