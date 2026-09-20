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
* ``intervals2``: the regime-conditional error pool (365 days) with the adaptive level, one level in all or one
  per regime, against the regime-conditional and the adaptive intervals of ``intervals``; report in
  ``results/phase_e_intervals2/``, ``docs/phase_e_intervals2.md``.
* ``pv``: on ISO-NE and CAISO, the sky boosting with the installed PV capacity terms (``sky.PV_COLUMNS``) against
  the sky boosting without them; report in ``results/phase_e_pv/``, ``docs/phase_e_pv.md``.
* ``final``: the frozen recipe on the eleven BAs, one run: the additive model with special-day indicators (with the
  linear PV terms at ISO-NE and CAISO), the boosting (with the sky features at ISO-NE and CAISO), their ensemble weighted
  by recent error, and the regime-conditional bias correction read at an adaptive level per regime (``final``); report in
  ``results/phase_e_final/``, ``docs/phase_e_final.md``.
* ``pv2``: on the same BAs, the additive model with linear PV terms (capacity times the sun, and times the cloud
  fraction) in the ensemble with the sky boosting, against the ensemble without them; report in
  ``results/phase_e_pv2/``, ``docs/phase_e_pv2.md``.

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


def group_models(group: str, ba: str | None = None) -> list:
    add, boo, ens = corrected_ensemble()
    if group == "final":
        from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals

        solar = ba in PV_BAS
        add_f = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, name="final_additive"))
        boo_f = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, name="final_boosting"))
        ens_f = Cached(Ensemble([add_f, boo_f], weighting="recent", name="final_ensemble"))
        return [add_f, boo_f, ens_f,
                AdaptiveIntervals(ens_f, by_regime=True, window_days=365, alpha_by_regime=True, name="final")]
    if group == "recipe":
        return [add, boo, ens, EmpiricalIntervals(ens, name="ens_recent_bc")]
    if group == "intervals":
        from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals

        return [add, boo, ens,
                EmpiricalIntervals(ens, name="ens_bc_simple"),
                EmpiricalIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime"),
                AdaptiveIntervals(ens, name="ens_bc_adaptive")]
    if group == "intervals2":
        from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals

        return [add, boo, ens,
                EmpiricalIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime"),
                AdaptiveIntervals(ens, name="ens_bc_adaptive"),
                AdaptiveIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime_aci"),
                AdaptiveIntervals(ens, by_regime=True, window_days=365, alpha_by_regime=True, name="ens_bc_regime_aci2")]
    if group == "sky":
        boo_sky = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_sky"))
        ens_sky = Cached(Ensemble([add, boo_sky], weighting="recent", name="ens_sky"))
        return [add, boo, boo_sky, ens, ens_sky,
                EmpiricalIntervals(ens, by_regime=True, window_days=365, name="ens_bc_regime"),
                EmpiricalIntervals(ens_sky, by_regime=True, window_days=365, name="ens_sky_bc_regime")]
    if group == "pv2":
        add_pv = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=True, name="additive_ml_pv"))
        boo_sky = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_sky"))
        ens_sky = Cached(Ensemble([add, boo_sky], weighting="recent", name="ens_sky"))
        ens_pv2 = Cached(Ensemble([add_pv, boo_sky], weighting="recent", name="ens_pv2"))
        return [add, add_pv, boo_sky, ens_sky, ens_pv2,
                EmpiricalIntervals(ens_sky, by_regime=True, window_days=365, name="ens_sky_bc_regime"),
                EmpiricalIntervals(ens_pv2, by_regime=True, window_days=365, name="ens_pv2_bc_regime")]
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
            for ba in (SKY_BAS if group == "sky" else PV_BAS if group in ("pv", "pv2") else a.bas):
                f = a.out / f"{group}_{ba}.parquet"
                if f.exists():
                    log(f"{group} {ba}: done already")
                    continue
                solar = group == "final" and ba in PV_BAS
                ld = loader(a, sky=group in ("sky", "pv", "pv2") or solar, pv=group in ("pv", "pv2") or solar)
                if not stations_ready(ld, ba):
                    log(f"{group} {ba}: station forecasts not extracted yet, skipped")
                    waiting.append((group, ba))
                    continue
                t0 = time.time()
                rows, hourly = evaluate(ld, group_models(group, ba), [ba], a.start, a.end, log=log, hourly=True)
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
    iv2 = report({"intervals2"}, a.results.parent / "phase_e_intervals2", a.doc.parent / "phase_e_intervals2.md",
                 "Phase E: regime-conditional errors with an adaptive level",
                 "Development BAs: " + common +
                 "`ens_bc_regime` reads the 5th and 95th percentiles of the corrected ensemble's errors on the known days of the same "
                 "temperature regime over the last year; `ens_bc_adaptive` reads them on the last 120 days at a level that adapts to "
                 "the coverage achieved (adaptive conformal inference); `ens_bc_regime_aci` combines the two (regime pool, one adaptive "
                 "level); `ens_bc_regime_aci2` tracks one adaptive level per regime.")
    pv = report({"pv"}, a.results.parent / "phase_e_pv", a.doc.parent / "phase_e_pv.md",
                "Phase E: the installed PV capacity as a feature",
                "BAs with large solar behind the load: " + common +
                "`boosting_ml_pv` is the sky boosting with three more columns: the installed PV capacity of the month (MW, from "
                "Forms EIA-861M and EIA-860M), that capacity times the sun's elevation, and the same times one minus the forecast "
                "cloud fraction; `ens_pv` and `ens_pv_bc_regime` are the ensemble and the corrected ensemble built on it. Compare "
                "with `docs/phase_e_sky.md` (same BAs and days, without the capacity terms).")
    pv2 = report({"pv2"}, a.results.parent / "phase_e_pv2", a.doc.parent / "phase_e_pv2.md",
                 "Phase E: linear PV terms in the additive model",
                 "BAs with large solar behind the load: " + common +
                 "`additive_ml_pv` is the additive model with two linear terms per hour: the installed PV capacity times the sun's "
                 "elevation, and the same times the forecast cloud fraction (zero before December 2020); `ens_pv2` and "
                 "`ens_pv2_bc_regime` pair it with the sky boosting, next to the same ensemble built on the additive model "
                 "without those terms (`ens_sky`, `ens_sky_bc_regime`).")
    final = report({"final"}, a.results.parent / "phase_e_final", a.doc.parent / "phase_e_final.md",
                   "Phase E: the frozen recipe on the eleven BAs",
                   "Development BAs: " + common +
                   "One run of the recipe that phase E settled on. `final_additive` is the additive model with special-day indicators, "
                   "with the linear PV terms at ISO-NE and CAISO; `final_boosting` is the boosting, with the sky features at ISO-NE and "
                   "CAISO; `final_ensemble` weights the two by their recent error; `final` is that ensemble with the regime-conditional "
                   "bias correction (median of the errors of the same temperature regime over the last year) and a 90 % interval read "
                   "at an adaptive level per regime.")
    if main is None and sky is None and pv is None and iv2 is None and pv2 is None and final is None:
        log("no rows to report")
        return 1
    if waiting:
        log(f"still waiting for station forecasts: {waiting}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
