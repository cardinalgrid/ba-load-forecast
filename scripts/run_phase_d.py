"""Phase D: closing the development of the model on the ten development BAs.

    python scripts/run_phase_d.py --groups base
    python scripts/run_phase_d.py --groups extremes ensemble special quantiles
    python scripts/run_phase_d.py --report-only

Every group uses several stations per BA and six years of training (the two levers of phase C, now
combined). Groups:

* ``base``: the additive model, the boosting and the recency regression on that footing.
* ``extremes``: the same additive and boosting with explicit cold and heat extreme terms.
* ``ensemble``: means of the direct models, simple and weighted by recent error.
* ``special``: the best model with the three special-day treatments, to be scored on special days.
* ``quantiles``: the boosting with pinball loss (5, 50, 95 %) and empirical intervals around the additive model.

One parquet per (group, BA) in ``--out`` (skipped when present); the combined report goes to
``results/phase_d/`` and ``docs/phase_d.md``.
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
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.recency import RecencyRegression
from ba_load_forecast.information_set import Loader
from ba_load_forecast.paths import DATA, ISD, TIDY
from ba_load_forecast.report import summarise, write_report

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT")
TRAIN_DAYS = 2190
HISTORY_DAYS = TRAIN_DAYS + 40


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def loader(a) -> Loader:
    return Loader(a.tidy, a.isd_dir, a.hrrr, history_days=HISTORY_DAYS, stations="multi")


def group_models(group: str) -> list:
    if group == "base":
        rec = RecencyRegression()
        rec.name = "recency_ml"
        return [AdditiveModel(train_days=TRAIN_DAYS, name="additive_ml"),
                Boosting(train_days=TRAIN_DAYS, name="boosting_ml"), rec]
    if group == "extremes":
        return [AdditiveModel(train_days=TRAIN_DAYS, extremes=True, name="additive_ml_ext"),
                Boosting(train_days=TRAIN_DAYS, extremes=True, name="boosting_ml_ext")]
    if group == "ensemble":
        from ba_load_forecast.forecasters.ensemble import Ensemble

        def add():
            return AdditiveModel(train_days=TRAIN_DAYS, extremes=True, name="additive_ml_ext")

        def boo():
            return Boosting(train_days=TRAIN_DAYS, extremes=True, name="boosting_ml_ext")

        def rec():
            r = RecencyRegression()
            r.name = "recency_ml"
            return r

        return [Ensemble([add(), boo()], weighting="mean", name="ens_mean"),
                Ensemble([add(), boo()], weighting="recent", name="ens_recent"),
                Ensemble([add(), boo(), rec()], weighting="mean", name="ens_mean3")]
    if group == "special":
        from ba_load_forecast.forecasters.special import SeparateSpecialModel

        def add(**kw):
            return AdditiveModel(train_days=TRAIN_DAYS, extremes=True, **kw)

        sep = SeparateSpecialModel(lambda: add(name="additive_ml_ext"))
        sep.name = "additive_ml_ext_separate"
        return [add(special_days=True, name="additive_ml_ext_special"), sep]
    if group == "quantiles":
        from ba_load_forecast.forecasters.quantiles import EmpiricalIntervals, QuantileBoosting

        return [QuantileBoosting(train_days=TRAIN_DAYS, extremes=True, name="qboost_ml"),
                EmpiricalIntervals(AdditiveModel(train_days=TRAIN_DAYS, extremes=True, name="additive_ml_ext"), name="emp_additive_ml")]
    raise SystemExit(f"unknown group {group}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--groups", nargs="+", default=["base"])
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--tidy", type=Path, default=TIDY)
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--hrrr", type=Path, default=DATA / "hrrr")
    ap.add_argument("--out", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_d")
    ap.add_argument("--phase-c", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_c")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "phase_d")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "phase_d.md")
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)

    if not a.report_only:
        for group in a.groups:
            for ba in a.bas:
                f = a.out / f"{group}_{ba}.parquet"
                if f.exists():
                    log(f"{group} {ba}: done already")
                    continue
                t0 = time.time()
                rows = evaluate(loader(a), group_models(group), [ba], a.start, a.end, log=log)
                tmp = f.with_suffix(".tmp")
                rows.to_parquet(tmp, index=False)
                tmp.replace(f)
                sc = rows[~rows["skipped"].astype(bool)].groupby("model")["mape"].mean().round(2).to_dict()
                log(f"{group} {ba}: {len(rows)} rows in {(time.time() - t0) / 60:.1f} min; mean MAPE {sc}")

    files = sorted(a.out.glob("*.parquet"))
    if not files:
        log("no rows to report")
        return 1
    rows = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
    # phase C references on the same days: the best single-lever variants
    for f in sorted(a.phase_c.glob("*.parquet")):
        c = pd.read_parquet(f)
        rows = pd.concat([rows, c[c["model"].isin(["additive_multi", "boosting_multi", "additive_long"])]], ignore_index=True)
    rows = rows.drop_duplicates(subset=["ba", "day", "model"])
    a.results.mkdir(parents=True, exist_ok=True)
    rows.to_parquet(a.results / "rows.parquet", index=False)
    tables = summarise(rows)
    for name, t in tables.items():
        t.to_csv(a.results / f"{name}.csv")
    intro = (f"Development BAs ({', '.join(sorted(rows['ba'].unique()))}), {a.start} to {a.end}, 9 a.m. cut-off, HRRR "
             "temperature at four to five stations per BA, six years of training (`_ml`). Variants: explicit cold and "
             "heat extreme terms (`_ext`), ensembles of the direct models (`ens_`), the special-day treatments "
             "(`_special`, `_separate`), quantile forecasts (`qboost_`, `emp_`). Three phase C variants are kept as "
             "references (`_multi`: several stations with two years; `additive_long`: one station with six years). Only "
             "BA-days on which every model produced a forecast are counted; documented load-shed days are left out.")
    write_report(tables, a.doc, "Phase D: closing the development of the model", intro)
    log(f"report written: {a.doc}")
    print(tables["overall"].round(2).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
