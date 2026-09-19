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
| HRRR 2 m temperature forecasts, runs 06 and 12 UTC, 2 December 2020 to 31 December 2025 | AWS Open Data `s3://hrrrzarr` (University of Utah's Zarr mirror of NOAA's HRRR), anonymous access | `data/hrrr/` (35 stations) and `data/hrrr_multi/` (28 extra stations) | Immutable archive. About 12 h and 80 GB of downloads per extraction; the result is 91 MB of parquet. |

Station tables: `docs/stations_grid.csv` (one station per BA, the same assignment as Cardinal Grid
Note 2) and `docs/stations_grid_multi.csv` (four to five per development BA), each with the nearest
HRRR grid cell.

## Environment

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

Tests: `pytest -q` (57 tests on synthetic data, no network) and `python -m ruff check src tests scripts`.

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
