"""Phase E: the full recipe, calibrated prediction intervals, on the development BAs plus FPL.

    python scripts/run_phase_e.py --groups recipe
    python scripts/run_phase_e.py --groups intervals
    python scripts/run_phase_e.py --report-only

Every group uses several stations per BA and six years of training. Groups:

* ``recipe``: the additive model with special-day indicators, the boosting, their ensemble weighted by
  recent error, and the ensemble with the empirical bias correction (which also gives a 90 % interval).
  The two members are fitted once and shared.
* ``intervals``: alternatives for the interval around the corrected ensemble (errors of the same temperature
  regime over a year; adaptive conformal inference).

Per (group, BA) two parquet files go to ``--out``: the daily rows and the hourly forecasts of every model,
of ``DF`` and the outcome. A BA whose station forecasts are not extracted yet is skipped, not marked done.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.evaluate import evaluate
from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import Cached
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.ensemble import Ensemble
from ba_load_forecast.forecasters.quantiles import EmpiricalIntervals
from ba_load_forecast.information_set import Loader
from ba_load_forecast.report import summarise, write_report

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")
TRAIN_DAYS = 2190
HISTORY_DAYS = TRAIN_DAYS + 40


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def loader(a) -> Loader:
    return Loader(a.tidy, a.isd_dir, a.hrrr, history_days=HISTORY_DAYS, stations="multi")


def corrected_ensemble():
    """The members, the ensemble and the corrected ensemble, sharing the fitted members."""
    add = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, name="additive_ml_special"))
    boo = Cached(Boosting(train_days=TRAIN_DAYS, name="boosting_ml"))
    ens = Cached(Ensemble([add, boo], weighting="recent", name="ens_recent"))
    return add, boo, ens


def group_models(group: str) -> list:
    add, boo, ens = corrected_ensemble()
    if group == "recipe":
        return [add, boo, ens, EmpiricalIntervals(ens, name="ens_recent_bc")]
    if group == "intervals":
        from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals

        return [add, boo, ens,
                EmpiricalIntervals(ens, name="ens_bc_simple"),
                EmpiricalIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime"),
                AdaptiveIntervals(ens, name="ens_bc_adaptive")]
    raise SystemExit(f"unknown group {group}")


def stations_ready(ld: Loader, ba: str) -> bool:
    return all(len(ld.hrrr(icao)) for icao in ld.stations_of(ba))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--groups", nargs="+", default=["recipe"])
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--tidy", type=Path, default=ROOT.parent / "ba-forecast-scorecard" / "data" / "tidy")
    ap.add_argument("--isd-dir", type=Path, default=ROOT.parent / "notes" / "03-daily-load-profiles" / "data" / "isd")
    ap.add_argument("--hrrr", type=Path, default=ROOT / "data" / "hrrr")
    ap.add_argument("--out", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "phase_e")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "phase_e.md")
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)

    waiting = []
    if not a.report_only:
        for group in a.groups:
            for ba in a.bas:
                f = a.out / f"{group}_{ba}.parquet"
                if f.exists():
                    log(f"{group} {ba}: done already")
                    continue
                ld = loader(a)
                if not stations_ready(ld, ba):
                    log(f"{group} {ba}: station forecasts not extracted yet, skipped")
                    waiting.append((group, ba))
                    continue
                t0 = time.time()
                rows, hourly = evaluate(ld, group_models(group), [ba], a.start, a.end, log=log, hourly=True)
                hourly.to_parquet(a.out / f"{group}_{ba}_hourly.parquet", index=False)
                tmp = f.with_suffix(".tmp")
                rows.to_parquet(tmp, index=False)
                tmp.replace(f)
                sc = rows[~rows["skipped"].astype(bool)].groupby("model")["mape"].mean().round(2).to_dict()
                log(f"{group} {ba}: {len(rows)} rows in {(time.time() - t0) / 60:.1f} min; mean MAPE {sc}")

    files = sorted(p for p in a.out.glob("*.parquet") if not p.name.endswith("_hourly.parquet"))
    if not files:
        log("no rows to report")
        return 1
    rows = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True).drop_duplicates(subset=["ba", "day", "model"])
    a.results.mkdir(parents=True, exist_ok=True)
    rows.to_parquet(a.results / "rows.parquet", index=False)
    tables = summarise(rows)
    for name, t in tables.items():
        t.to_csv(a.results / f"{name}.csv")
    intro = (f"Development BAs ({', '.join(sorted(rows['ba'].unique()))}), {a.start} to {a.end}, 9 a.m. cut-off, HRRR "
             "temperature at several stations per BA, six years of training. Models: the additive model with "
             "special-day indicators, the boosting, their ensemble weighted by recent error (`ens_recent`), and the "
             "ensemble with the empirical bias correction (`ens_recent_bc` and the `ens_bc_` interval variants: the "
             "point forecast is the corrected median once 20 days of known errors exist). Only BA-days on which every "
             "model produced a forecast are counted; documented load-shed days are left out.")
    write_report(tables, a.doc, "Phase E: the full recipe and calibrated prediction intervals", intro)
    log(f"report written: {a.doc}")
    print(tables["overall"].round(2).to_string())
    if waiting:
        log(f"still waiting for station forecasts: {waiting}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
