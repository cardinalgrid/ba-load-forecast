"""Phase B: the floors, the profile and the recency regression against each BA's own forecast.

    python scripts/run_phase_b.py --out <a local folder for the rows>
    python scripts/run_phase_b.py --report-only

One parquet per BA in ``--out`` (skipped when it exists, so the run is resumable); the report goes to
``results/phase_b/`` and ``docs/phase_b.md`` in the repository.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd

from ba_load_forecast.evaluate import evaluate
from ba_load_forecast.forecasters.naive import LastKnownDay, SameTypeMean, SameWeekdayLastWeek
from ba_load_forecast.forecasters.profile import ProfileForecaster
from ba_load_forecast.forecasters.recency import RecencyRegression
from ba_load_forecast.information_set import Loader
from ba_load_forecast.paths import DATA, ISD, TIDY
from ba_load_forecast.report import summarise, write_report

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT")


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def forecasters():
    return [LastKnownDay(), SameWeekdayLastWeek(), SameTypeMean(weeks=2), ProfileForecaster(), RecencyRegression()]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2020, 12, 2))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--tidy", type=Path, default=TIDY)
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--hrrr", type=Path, default=DATA / "hrrr")
    ap.add_argument("--out", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_b")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "phase_b")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "phase_b.md")
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)

    if not a.report_only:
        loader = Loader(a.tidy, a.isd_dir, a.hrrr, history_days=760)
        for ba in a.bas:
            f = a.out / f"{ba}.parquet"
            if f.exists():
                log(f"{ba}: done already")
                continue
            t0 = time.time()
            rows = evaluate(loader, forecasters(), [ba], a.start, a.end, log=log)
            tmp = f.with_suffix(".tmp")
            rows.to_parquet(tmp, index=False)
            tmp.replace(f)
            sc = rows[~rows["skipped"].astype(bool)].groupby("model")["mape"].mean().round(2).to_dict()
            log(f"{ba}: {len(rows)} rows in {(time.time() - t0) / 60:.1f} min; mean MAPE {sc}")
            loader = Loader(a.tidy, a.isd_dir, a.hrrr, history_days=760)   # drop the cache of this BA

    files = [a.out / f"{ba}.parquet" for ba in a.bas if (a.out / f"{ba}.parquet").exists()]
    if not files:
        log("no rows to report")
        return 1
    rows = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
    a.results.mkdir(parents=True, exist_ok=True)
    rows.to_parquet(a.results / "rows.parquet", index=False)
    tables = summarise(rows)
    for name, t in tables.items():
        t.to_csv(a.results / f"{name}.csv")
    bas = ", ".join(sorted(rows["ba"].unique()))
    intro = (f"Day-ahead forecasts issued under the 9 a.m. cut-off for {bas}, {a.start} to {a.end}, scored against "
             "the load that occurred and compared, day by day, with the BA's own day-ahead forecast reported to the "
             "EIA (`DF`). Models: the three floors (last known day, same weekday last week, mean of the same day type "
             "over two weeks), the profile of Cardinal Grid Note 2 with the regime from the HRRR forecast, and the "
             "recency-effect regression fitted on observed temperature and run on the HRRR forecast. Only BA-days on "
             "which every model produced a forecast are counted.")
    write_report(tables, a.doc, "Phase B: floors, profile and recency regression against the BA's forecast", intro)
    log(f"report written: {a.doc}")
    print(tables["overall"].round(2).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
