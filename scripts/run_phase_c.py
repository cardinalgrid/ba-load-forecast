"""Phase C: what closes the gap to the BA's forecast? Model families and data options on the same harness.

    python scripts/run_phase_c.py --groups single sentinel long        # no multi-station data needed
    python scripts/run_phase_c.py --groups multi                        # after the extra stations are extracted
    python scripts/run_phase_c.py --report-only

Groups (each is one loader configuration, run on the ten development BAs, December 2020 to 2022):

* ``single``: one station per BA, gross-fault guard; the recency regression (reference from phase B), the
  additive model with and without special-day indicators, with the shape-cluster label, and as a separate
  special-day model; the boosting with and without special-day indicators and with the cluster label.
* ``multi``: the same recency, additive and boosting on the equal-weight mean of several stations per
  BA (the boosting also sees one column per station).
* ``sentinel``: one station, history cleaned by grid-data-sentinel instead of the gross-fault guard.
* ``long``: one station, six years of training instead of two.

One parquet per (group, BA) in ``--out`` (skipped when present); the combined report goes to
``results/phase_c/`` and ``docs/phase_c.md``.
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
from ba_load_forecast.forecasters.special import SeparateSpecialModel, ShapeLabels
from ba_load_forecast.information_set import Loader
from ba_load_forecast.paths import DATA, ISD, TIDY
from ba_load_forecast.report import summarise, write_report

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT")
LONG_TRAIN_DAYS = 2190


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def group_setup(group: str, a) -> tuple[Loader, list]:
    labels = ShapeLabels(ROOT / "results" / "day_clusters")
    common = dict(tidy_dir=a.tidy, isd_dir=a.isd_dir, hrrr_dir=a.hrrr)
    if group == "single":
        loader = Loader(**common, history_days=760)
        models = [
            RecencyRegression(),
            AdditiveModel(), AdditiveModel(special_days=True),
            AdditiveModel(label_column="cluster", labels=labels),
            SeparateSpecialModel(AdditiveModel),
            Boosting(), Boosting(special_days=False),
            Boosting(label_column="cluster", labels=labels),
        ]
    elif group == "multi":
        loader = Loader(**common, history_days=760, stations="multi")
        models = [RecencyRegression(), AdditiveModel(name="additive_multi"), Boosting(name="boosting_multi")]
        models[0].name = "recency_regression_multi"
    elif group == "sentinel":
        loader = Loader(**common, history_days=760, cleaning="sentinel")
        models = [RecencyRegression(), AdditiveModel(name="additive_sentinel"), Boosting(name="boosting_sentinel")]
        models[0].name = "recency_regression_sentinel"
    elif group == "long":
        loader = Loader(**common, history_days=LONG_TRAIN_DAYS + 40)
        models = [AdditiveModel(train_days=LONG_TRAIN_DAYS, name="additive_long"),
                  Boosting(train_days=LONG_TRAIN_DAYS, name="boosting_long")]
    else:
        raise SystemExit(f"unknown group {group}")
    return loader, models


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--groups", nargs="+", default=["single", "sentinel", "long"])
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--tidy", type=Path, default=TIDY)
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--hrrr", type=Path, default=DATA / "hrrr")
    ap.add_argument("--out", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_c")
    ap.add_argument("--phase-b", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_b")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "phase_c")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "phase_c.md")
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
                loader, models = group_setup(group, a)
                t0 = time.time()
                rows = evaluate(loader, models, [ba], a.start, a.end, log=log)
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
    # the phase B floors and profile, for the same days, as references
    for f in sorted(a.phase_b.glob("*.parquet")):
        b = pd.read_parquet(f)
        rows = pd.concat([rows, b[b["model"].isin(["last_known_day", "profile"])]], ignore_index=True)
    rows = rows.drop_duplicates(subset=["ba", "day", "model"])
    a.results.mkdir(parents=True, exist_ok=True)
    rows.to_parquet(a.results / "rows.parquet", index=False)
    tables = summarise(rows)
    for name, t in tables.items():
        t.to_csv(a.results / f"{name}.csv")
    intro = (f"Development BAs ({', '.join(sorted(rows['ba'].unique()))}), {a.start} to {a.end}, 9 a.m. cut-off, HRRR "
             "temperature. Groups: one station with the gross-fault guard (`single`: recency regression, additive with "
             "and without special-day indicators, with the shape-cluster label and as a separate special-day model, "
             "boosting with and without indicators and with the cluster label); several stations per BA (`_multi`); "
             "history cleaned by grid-data-sentinel (`_sentinel`); six years of training (`_long`). Two floors of phase "
             "B are kept as references. Only BA-days on which every model produced a forecast are counted; documented "
             "load-shed days are left out.")
    write_report(tables, a.doc, "Phase C: model families and data options against the BA's forecast", intro)
    log(f"report written: {a.doc}")
    print(tables["overall"].round(2).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
