# Reproducing the study, step by step

Everything in `results/` and `docs/` was produced by the scripts in `scripts/` from three public data
sources. This page lists the inputs, the commands in order, what each one writes, how long it takes, and
what to expect. The models are deterministic (least squares, seeded k-means and seeded boosting), so a
rerun on the same inputs gives the same rows: on 19 September 2026 phase B for SPP was rerun from scratch
and all 4560 rows matched the stored ones exactly.

## Inputs

| Input | Source | Where the scripts expect it | Notes |
|---|---|---|---|
| Hourly demand `D` and day-ahead forecast `DF` per BA, 2015 to 2026 | EIA-930 (form EIA-930 hourly operating data), tidied by [ba-forecast-scorecard](https://github.com/cardinalgrid/ba-forecast-scorecard) into half-year parquet files (`ba, region, date, hour, local_end, utc_end, forecast, demand, demand_adjusted, demand_imputed`) | `../ba-forecast-scorecard/data/tidy/` | The EIA revises its files; the scorecard repository records the download date of its tidy files. This study used the raw `demand` column, as Note 1 did. |
| Hourly observed temperature, NOAA ISD-Lite, 2015 to 2025 | `https://www.ncei.noaa.gov/pub/data/noaa/isd-lite/<year>/<usaf>-<wban>-<year>.gz` and `isd-history.csv` | `../notes/03-daily-load-profiles/data/isd/` | Fetched on demand by `grid_sentinel.weather.fetch_isd_lite`; `scripts/fetch_isd.py` fetches every station of the multi-station table. NOAA occasionally revises a year's file. |
| Hourly observed temperature after 27 August 2025 (the ISD archive stops there) | NOAA GHCNh, `https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/2025/psv/GHCNh_<GHCN_ID>_2025.psv` and `doc/ghcnh-station-list.csv` | `data/ghcnh/<ICAO>.csv` | `python scripts/fetch_ghcnh.py` (68 stations, about 12 MB downloaded per station, reduced to the METAR temperatures; 25 min). Used only where the ISD series is missing; `python scripts/fetch_asos.py` (Iowa Environmental Mesonet, one request, 1 min) into `data/asos/` fills the hours GHCNh lacks (a 90 h hole at every station from 30 August to 2 September 2025). The runner applies `--supplement-dir data/ghcnh data/asos` in that order by default. |
| HRRR 2 m temperature forecasts, runs 06 and 12 UTC, 2 December 2020 to 31 December 2025 | AWS Open Data `s3://hrrrzarr` (University of Utah's Zarr mirror of NOAA's HRRR), anonymous access | `data/hrrr/` (35 stations) and `data/hrrr_multi/` (28 extra stations) | Immutable archive. About 12 h and 80 GB of downloads per extraction; the result is 91 MB of parquet. |
| HRRR 2 m dew point and 10 m wind speed, same runs, 49 stations of the multi-station table | AWS Open Data `s3://hrrrzarr` (`2m_above_ground/DPT`, `10m_above_ground/UGRD` and `VGRD`) | `data/dewpoint/`, `data/wind/` | `python scripts/extract_hrrr.py --field dewpoint_f --stations docs/stations_grid_multi.csv --out data/dewpoint` (and `--field wind_ms --out data/wind`), one job per initialisation hour, then `--consolidate --out <folder>`; 6 to 12 h each. Observed dew point and wind come from the same ISD-Lite files (columns 6 and 9) and the same supplements. |

Station tables: `docs/stations_grid.csv` (one station per BA, the same assignment as Cardinal Grid
Note 2) and `docs/stations_grid_multi.csv` (four to five per development BA), each with the nearest
HRRR grid cell.

## Environment

**Data folder.** Every script reads its inputs from the locations in the table above by default. Setting the
environment variable `BA_LOAD_FORECAST_DATA` to a folder makes them read everything from there instead, in one
flat layout (`tidy/`, `isd/`, `hrrr/`, `hrrr_multi/`, `hrrr_fpl/`, `cloud/`, `dswrf/`, `dewpoint/`, `wind/`,
`asos/`, `ghcnh/`, `pv/`; see `src/ba_load_forecast/paths.py`). The study moved its inputs to such a folder on a
local disk after a synchronised drive dropped four times during long runs; outputs of long runs go to
`%USERPROFILE%a-load-forecast-runs\` for the same reason.

Python 3.11 on Windows 11; `pip install -e ".[hrrr,dev]"` plus `grid-data-sentinel[pandas]` 0.4.0
installed from its repository (the 0.4 API: `Sentinel`, `Repairer`, `Context`; the 0.3 release does not have
the classes that `cleaning.py` uses). Versions used for the results in this repository: numpy 1.26, pandas 2.2,
scipy 1.17, scikit-learn 1.3, zarr 2.18, s3fs 2026.7, pyarrow 11. k-means and the silhouette are implemented
in numpy (`clusters.py`), so scikit-learn is used only by the boosting.

## Commands, in the order the study ran them

Long jobs run detached through the `.cmd` files (each stage is repeated until it exits cleanly, because
the network drops for minutes at a time); every job is resumable and skips what already exists. Write
long outputs to a local disk, not to a synced folder.

| Step | Command | Writes | Time |
|---|---|---|---|
| 1. HRRR extraction, 35 stations | `scripts\run_extract.cmd` (calls `scripts/extract_hrrr.py` per year, then `--consolidate`) | `data/hrrr/runs/*.parquet`, `data/hrrr/<ICAO>.parquet` | about 12 h |
| 2. HRRR verification | `python scripts/verify_hrrr.py --years 2020 2021 2022 2023 2024 2025` | `results/hrrr_verification/*.csv`, `docs/hrrr_verification.md`, `docs/figures/` | 5 min |
| 3. Phase B (floors, profile, recency regression) | `scripts\run_phase_b.cmd` | rows in `%USERPROFILE%\ba-load-forecast-runs\phase_b\<BA>.parquet`; `results/phase_b/*.csv`, `docs/phase_b.md` | 15 min |
| 4. Daily-shape clusters | `python scripts/day_clusters.py` | `results/day_clusters/*.csv`, `docs/day_clusters.md` | 1 min |
| 5. Load-shed days | hand-made from the FERC/NERC, SPP and MISO reports: `docs/load_shed_days.csv` (quote and page per row) | used by `report.summarise` | |
| 6. Extra stations | `scripts\run_multi.cmd` (ISD-Lite for the extra stations, then the HRRR extraction for them, then `--consolidate --out data\hrrr_multi`) | `data/hrrr_multi/` | about 16 h |
| 7. Phase C, groups without extra stations | `scripts\run_phase_c.cmd single sentinel long` | `%USERPROFILE%\ba-load-forecast-runs\phase_c\<group>_<BA>.parquet` | about 6 h |
| 8. Phase C, extra stations | `scripts\run_phase_c.cmd multi` (after step 6) | same folder; then `results/phase_c/*.csv`, `docs/phase_c.md` | 1 h |
| 9. Report only | `python scripts/run_phase_c.py --report-only` | rebuilds `results/phase_c/` and `docs/phase_c.md` from the rows | 1 min |
| 10. Phase D, base group | `scripts\run_phase_d.cmd base` | `%USERPROFILE%\ba-load-forecast-runs\phase_d\base_<BA>.parquet` | 2.5 h |
| 11. Phase D, other groups | `scripts\run_phase_d_rest.cmd` (extremes, ensemble, special, quantiles; its own log, because Windows locks a log another job is appending to) | same folder; then `results/phase_d/*.csv`, `docs/phase_d.md` | 12 h |
| 12. Report only | `python scripts/run_phase_d.py --report-only` | rebuilds `results/phase_d/` and `docs/phase_d.md` | 1 min |
| 13. FPL stations | `scripts\run_fpl.cmd` (ISD-Lite, HRRR extraction for the FPL stations, consolidation) | `data/hrrr_fpl/` | 2 h |
| 14. Phase E | `scripts\run_phase_e.cmd recipe` and `scripts\run_phase_e.cmd intervals` (one job and one log per group; eleven BAs) | `%USERPROFILE%\ba-load-forecast-runs\phase_e\<group>_<BA>.parquet` and `<group>_<BA>_hourly.parquet`; `results/phase_e/*.csv`, `docs/phase_e.md` | 2.5 h each |
| 15. Diagnostics | `python scripts/diagnose.py --group intervals --model ens_bc_regime` | `results/diagnostics/*.csv`, `docs/diagnostics.md`, `docs/figures/diagnostics_mape_by_hour_month.*` | 1 min |
| 16. Cloud cover, 15 stations | `scripts\run_cloud.cmd` (`extract_hrrr.py --field cloud_pct` per year for the stations of ISO-NE, CAISO and FPL, then consolidation) | `data/cloud/` | about 3 h |
| 17. Phase E, sky group | `scripts\run_phase_e.cmd sky` | `%USERPROFILE%\ba-load-forecast-runs\phase_e\sky_<BA>*.parquet`; `results/phase_e_sky/*.csv`, `docs/phase_e_sky.md` | 1.5 h |
| 18. Diagnostics of the sky group | `python scripts/diagnose.py --group sky --model ens_sky_bc_regime --out results/diagnostics_sky --doc docs/diagnostics_sky.md` | `results/diagnostics_sky/*.csv`, `docs/diagnostics_sky.md`, `docs/figures/diagnostics_sky_mape_by_hour_month.*` | 1 min |
| 19. The BAs' forecast by hour, offsets and time alignment | `python scripts/df_profile.py` (EIA-930 files only; the comparison column reads the stored hourly forecasts of step 14) | `results/df_profile/*.csv`, `docs/df_hourly_bias.md` | 2 min |
| 20. Installed PV capacity | `python scripts/pv_capacity.py` (downloads Forms EIA-861M and EIA-860M into `data/pv/`) | `docs/pv_capacity_monthly.csv` | 3 min |
| 21. Phase E, pv group | `scripts
un_phase_e.cmd pv` (ISO-NE and CAISO; needs steps 16 and 20) | `results/phase_e_pv/*.csv`, `docs/phase_e_pv.md` | 1 h |
| 22. Phase E, intervals2 group | `scripts
un_phase_e.cmd intervals2` (eleven BAs) | `results/phase_e_intervals2/*.csv`, `docs/phase_e_intervals2.md` | 2.5 h |
| 23. Phase E, final recipe | `scripts
un_phase_e.cmd final` (eleven BAs, one run; needs steps 16 and 20 for ISO-NE and CAISO) | `results/phase_e_final/*.csv`, `docs/phase_e_final.md` | 3 h |
| 24. Benchmark profile and diagnostics of the final recipe | `python scripts/df_profile.py --group final --model final` and `python scripts/diagnose.py --group final --model final --out results/diagnostics_final --doc docs/diagnostics_final.md` | `docs/df_hourly_bias.md`, `docs/diagnostics_final.md` | 3 min |
| 25. Phase F, intervals for the coldest days | `scripts\run_phase_e.cmd intervals3` | `results/phase_e_intervals3/*.csv`, `docs/phase_e_intervals3.md` | 2.5 h |
| 26. Phase F, peak | `scripts\run_phase_e.cmd peak` | `results/phase_e_peak/*.csv`, `docs/phase_e_peak.md` | 2.5 h |
| 27. Forecast irradiance, 15 stations | `scripts\run_dswrf.cmd 12` and `scripts\run_dswrf.cmd 6` (two jobs, one per run hour; needs `pip install eccodes`), then `python scripts/extract_dswrf.py --consolidate --out data/dswrf` | `data/dswrf/` | 10 h |
| 28. Phase F, irradiance | `scripts\run_phase_e.cmd irradiance` (ISO-NE and CAISO) | `results/phase_e_irradiance/*.csv`, `docs/phase_e_irradiance.md` | 1 h |
| 29. Phase F, final recipe | `scripts\run_phase_e.cmd final2` (eleven BAs, one run) | `results/phase_f_final/*.csv`, `docs/phase_f_final.md` | 2.5 h |
| 30. Benchmark profile and diagnostics of the phase F recipe | `python scripts/df_profile.py --group final2 --model final2` and `python scripts/diagnose.py --group final2 --model final2 --out results/diagnostics_final2 --doc docs/diagnostics_final2.md` | `docs/df_hourly_bias.md`, `docs/diagnostics_final2.md` | 3 min |
| 31. Frozen evaluation, 2023 to 2025 | three parallel processes of `python scripts/run_phase_e.py --groups frozen --start 2023-01-01 --end 2025-12-31 --bas <group>` (PJM MISO ERCO CISO; SWPP NYIS ISNE TVA; DUK BPAT FPL), then the same command with `--report-only` and all BAs | `%USERPROFILE%\ba-load-forecast-runs\phase_e\frozen_<BA>*.parquet`; `results/frozen_2023_2025/*.csv`, `docs/frozen_evaluation.md` | 1.5 h |
| 32. Benchmark profile, 2023 to 2025 | `python scripts/df_profile.py --group frozen --model final2 --start 2023-01-01 --end 2025-12-31 --out results/df_profile_2023_2025 --doc docs/df_hourly_bias_2023_2025.md` | `docs/df_hourly_bias_2023_2025.md` | 3 min |
| 33. Diagnostics, 2023 to 2025 | `python scripts/diagnose.py --group frozen --model final2 --out results/diagnostics_frozen --doc docs/diagnostics_frozen.md` | `docs/diagnostics_frozen.md` | 1 min |
| 34. Observed temperature for the end of 2025 | `python scripts/fetch_ghcnh.py`, `python scripts/fetch_asos.py`, then `python scripts/check_supplement.py` | `data/ghcnh/<ICAO>.csv`, `data/asos/<ICAO>.csv` (68 stations each; GHCNh has no 2025 file for KCHS), `docs/supplement_check.md` | 25 min, 1 min, 1 min |
| 35. Frozen evaluation of the phase G recipe, protocol v2, 2023 to 2025 | as step 31 with `--groups frozen3` (and `--groups frozen2` for the phase F recipe under the same protocol), after step 34; then `--report-only` | `results/frozen3_2023_2025/`, `docs/frozen_evaluation_v2.md`; `results/frozen2_2023_2025/` | 5 h and 2.5 h |
| 36. Phase H, humidity and wind | `python scripts/run_phase_e.py --groups humid_h` (humidity alone; needs the dew point extraction and the supplements re-fetched with `dewpoint_f, wind_ms`), `--groups humid` (with wind), `--groups humid_l` and `--groups humid_p` (variants of the additive model), each followed by `--report-only`; `python scripts/compare_days.py --candidate humid_h:final3_h humid_h:h_boosting --reference final3:final3 --doc docs/phase_h_humidity_by_season.md` and the same for the other groups | `docs/phase_h_humidity_only.md`, `docs/phase_h_humidity_by_season.md`, `docs/phase_h_humidity.md`, `docs/phase_h_humidity_linear.md`, `docs/phase_h_humidity_boosting.md`, `results/phase_h_*/` | 4 h per group (three processes) |
| 37. Third look at 2023 to 2025 with the phase H recipe | as step 31 with `--groups frozen4` (needs the dew point extraction), then `--report-only` with `--start 2023-01-01 --end 2025-12-31` | `results/frozen4_2023_2025/`, `docs/frozen_evaluation_v3.md` | 5 h |
| 38. Dew point verification | `python scripts/verify_dewpoint.py --years 2021 2022 2023 2024 2025` | `docs/hrrr_dewpoint_verification.md`, `results/hrrr_dewpoint_verification/`, `docs/figures/hrrr_dewpoint_*.png` | 10 min |

Tests: `pytest -q` (104 tests on synthetic data, no network) and `python -m ruff check src tests scripts`.

## What is fixed, and what is not

Fixed by construction: the cut-off (`cutoff.py`), the run chosen per BA-day, the leads, the gross-fault
guard, the seeds (`fit_clusters(seed=0)`, `Boosting(seed=0)`), the training windows (730 or 2190 days),
the refit cadence (7 days), the complete-case rule of the report, and the load-shed list.

Not versioned here: the data files themselves. The HRRR archive is immutable, so steps 1 and 6 give the
same parquet files on any day; the EIA-930 and ISD-Lite files may be revised by their publishers, so a
rerun months later can differ in a few hours of a few BA-years. To reproduce the numbers exactly, use the
same tidy and ISD-Lite snapshots (the scorecard repository and the `isd` cache) or the archived copies
that each tagged release deposits.

## Reading the results

`results/<phase>/rows.parquet` (not committed, rebuilt by the scripts) has one row per BA, day and model
with the metrics of `metrics.py`; `by_model_ba.csv`, `overall.csv`, `events.csv`, `dm_mape.csv`,
`dm_peak.csv`, `coverage.csv` and, when applicable, `shed_days.csv` are the tables of `report.py`. Every
number in the README and in `docs/phase_*.md` comes from these files.
