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
* ``sky``: on the BAs where behind-the-meter solar matters (ISO-NE, CAISO, FPL), the boosting with the sun's
  elevation and the HRRR cloud cover as seen at the cut-off, against the same boosting without them; its
  report is separate (``results/phase_e_sky/``, ``docs/phase_e_sky.md``).
* ``pv``: on ISO-NE and CAISO, the sky boosting with the installed PV capacity terms (``sky.PV_COLUMNS``) against
  the sky boosting without them; report in ``results/phase_e_pv/``, ``docs/phase_e_pv.md``.

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
SKY_BAS = ("ISNE", "CISO", "FPL")
PV_BAS = ("ISNE", "CISO")
TRAIN_DAYS = 2190
HISTORY_DAYS = TRAIN_DAYS + 40


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def loader(a, sky: bool = False, pv: bool = False) -> Loader:
    return Loader(a.tidy, a.isd_dir, a.hrrr, history_days=HISTORY_DAYS, stations="multi", sky=sky, pv=pv)


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
    if group == "sky":
        boo_sky = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_sky"))
        ens_sky = Cached(Ensemble([add, boo_sky], weighting="recent", name="ens_sky"))
        return [add, boo, boo_sky, ens, ens_sky,
                EmpiricalIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime"),
                EmpiricalIntervals(ens_sky, by_regime=True, window_days=365, name="ens_sky_bc_regime")]
    if group == "pv":
        boo_sky = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_sky"))
        boo_pv = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_pv"))   # same model; the loader adds the PV columns
        ens_sky = Cached(Ensemble([add, boo_sky], weighting="recent", name="ens_sky"))
        ens_pv = Cached(Ensemble([add, boo_pv], weighting="recent", name="ens_pv"))
        return [add, boo_pv, ens_pv, EmpiricalIntervals(ens_pv, by_regime=True, window_days=365, name="ens_pv_bc_regime")]
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
            for ba in (SKY_BAS if group == "sky" else PV_BAS if group == "pv" else a.bas):
                f = a.out / f"{group}_{ba}.parquet"
                if f.exists():
                    log(f"{group} {ba}: done already")
                    continue
                ld = loader(a, sky=group in ("sky", "pv"), pv=group == "pv")
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

    def report(prefixes, results, doc, title, intro):
        files = sorted(p for p in a.out.glob("*.parquet")
                       if not p.name.endswith("_hourly.parquet") and p.name.split("_")[0] in prefixes)
        if not files:
            return None
        rows = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True).drop_duplicates(subset=["ba", "day", "model"])
        results.mkdir(parents=True, exist_ok=True)
        rows.to_parquet(results / "rows.parquet", index=False)
        tables = summarise(rows)
        for name, t in tables.items():
            t.to_csv(results / f"{name}.csv")
        bas = ", ".join(sorted(rows["ba"].unique()))
        write_report(tables, doc, title, intro.format(bas=bas))
        log(f"report written: {doc}")
        print(tables["overall"].round(2).to_string())
        return tables

    common = (f"{{bas}}, {a.start} to {a.end}, 9 a.m. cut-off, HRRR temperature at several stations per BA, six years of "
              "training. Only BA-days on which every model produced a forecast are counted; documented load-shed days "
              "are left out. ")
    main = report({"recipe", "intervals"}, a.results, a.doc, "Phase E: the full recipe and calibrated prediction intervals",
                  "Development BAs: " + common +
                  "Models: the additive model with special-day indicators, the boosting, their ensemble weighted by recent "
                  "error (`ens_recent`), and the ensemble with the empirical bias correction (`ens_recent_bc` and the "
                  "`ens_bc_` interval variants: the point forecast is the corrected median once 20 days of known errors exist).")
    sky = report({"sky"}, a.results.parent / "phase_e_sky", a.doc.parent / "phase_e_sky.md",
                 "Phase E: the sun and the forecast cloud cover as features",
                 "BAs where behind-the-meter solar matters: " + common +
                 "`boosting_ml_sky` is the boosting with the cosine of the solar zenith angle, the HRRR total cloud cover as "
                 "seen at each day's cut-off (available from December 2020) and their product; `ens_sky` and "
                 "`ens_sky_bc_regime` are the ensemble and the corrected ensemble built on it, next to the same models "
                 "without those features.")
    pv = report({"pv"}, a.results.parent / "phase_e_pv", a.doc.parent / "phase_e_pv.md",
                "Phase E: the installed PV capacity as a feature",
                "BAs with large solar behind the load: " + common +
                "`boosting_ml_pv` is the sky boosting with three more columns: the installed PV capacity of the month (MW, from "
                "Forms EIA-861M and EIA-860M), that capacity times the sun's elevation, and the same times one minus the forecast "
                "cloud fraction; `ens_pv` and `ens_pv_bc_regime` are the ensemble and the corrected ensemble built on it. Compare "
                "with `docs/phase_e_sky.md` (same BAs and days, without the capacity terms).")
    if main is None and sky is None and pv is None:
        log("no rows to report")
        return 1
    if waiting:
        log(f"still waiting for station forecasts: {waiting}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
