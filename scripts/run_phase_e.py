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
* ``intervals3``: the final recipe's interval against two refinements for the coldest days: the error pool
  restricted to the 40 or 60 known days nearest in forecast minimum temperature, and an exponential tail
  beyond the pool's outer deciles; report in ``results/phase_e_intervals3/``, ``docs/phase_e_intervals3.md``.
* ``peak``: the final recipe against two corrections of the under-forecast at the daily peak: the hourly median
  correction replaced, around the forecast peak, by the median error measured at the actual peak hour of the pool
  days (``lift``), or the point read at the 55th percentile there (``quantile``); report in
  ``results/phase_e_peak/``, ``docs/phase_e_peak.md``.
* ``irradiance``: on ISO-NE and CAISO, the recipe (nearest-temperature pool) with the forecast surface short-wave flux
  from the HRRR GRIB2 archive, as seen at the cut-off, in the boosting and, times the PV capacity, in the additive
  model, against the same recipe without it; report in ``results/phase_e_irradiance/``, ``docs/phase_e_irradiance.md``.
* ``final2``: the phase F recipe in one run on the eleven BAs: the phase E members (irradiance in place of the cloud
  fraction where ``IRR_BAS`` says so), the nearest-temperature pool and the peak read at the 60th percentile;
  report in ``results/phase_f_final/``, ``docs/phase_f_final.md``.
* ``frozen``: the phase F recipe (``final2``), unchanged, on days the development never saw; run with
  ``--start 2023-01-01 --end 2025-12-31``; report in ``results/frozen_2023_2025/``, ``docs/frozen_evaluation.md``.
* ``protocol``: the phase F recipe (``final2``) scored under protocol v2: reporting faults of the published forecast
  and spikes in the outcome leave the day out for everyone, and the documented hour-label offsets are applied to the
  published series before anything else; report in ``results/phase_g_protocol/``, ``docs/phase_g_protocol.md``.
* ``feat``: the recipe's members with the phase G feature blocks (more load memory, thermal history and day shape,
  the sun's elevation for every BA), each against the plain member; report ``docs/phase_g_features.md``.
* ``hp``: the members with other parameters (boosting depth, rate, leaf size, regularisation, refit period; additive
  knots, validation window, penalty grid; training length); report ``docs/phase_g_parameters.md``.
* ``ens2``: the corrected ensemble with hourly weights, with the recency regression as a third member, with the
  boosting on a ratio target, and with a trimmed-mean correction; report ``docs/phase_g_ensemble.md``.
* ``tbias``: the phase F recipe with the HRRR temperature path corrected by its own recent bias per local hour
  (``Loader(temp_bias_days=30)``); report ``docs/phase_g_tbias.md``.
* ``pv2``: on the same BAs, the additive model with linear PV terms (capacity times the sun, and times the cloud
  fraction) in the ensemble with the sky boosting, against the ensemble without them; report in
  ``results/phase_e_pv2/``, ``docs/phase_e_pv2.md``.

Per (group, BA) two parquet files go to ``--out``: the daily rows and the hourly forecasts of every model,
of ``DF`` and the outcome. A BA whose station forecasts are not extracted yet is skipped, not marked done.
"""

from __future__ import annotations

import argparse
import re
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
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals, EmpiricalIntervals
from ba_load_forecast.information_set import Loader
from ba_load_forecast.report import summarise, write_report
from ba_load_forecast.weather_extra import WEATHER_FIELDS

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL")
SKY_BAS = ("ISNE", "CISO", "FPL")
PV_BAS = ("ISNE", "CISO")
IRR_BAS: tuple[str, ...] = ()          # BAs whose final2 members use the forecast irradiance (set after the irradiance group)
TRAIN_DAYS = 2190
HISTORY_DAYS = TRAIN_DAYS + 40


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def loader(a, sky: bool = False, pv: bool = False, irradiance: bool = False, temp_bias_days: int = 0,
           fields: tuple[str, ...] = ()) -> Loader:
    return Loader(a.tidy, a.isd_dir, a.hrrr, history_days=HISTORY_DAYS, stations="multi", sky=sky, pv=pv, irradiance=irradiance,
                  temp_bias_days=temp_bias_days, supplement_dir=a.supplement_dir, fields=fields)


def fields_ready(ld: Loader, ba: str) -> bool:
    """Every station of the BA has a consolidated extraction of every field the loader was asked for."""
    return all(len(ld.field_rows(f, icao)) for f in ld.fields for icao in ld.stations_of(ba))


def corrected_ensemble():
    """The members, the ensemble and the corrected ensemble, sharing the fitted members."""
    add = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, name="additive_ml_special"))
    boo = Cached(Boosting(train_days=TRAIN_DAYS, name="boosting_ml"))
    ens = Cached(Ensemble([add, boo], weighting="recent", name="ens_recent"))
    return add, boo, ens


def final_members(ba: str | None, irradiance: bool = False, suffix: str = ""):
    """The frozen recipe's members for one BA: PV terms and sky features only where solar behind the load matters."""
    solar = ba in PV_BAS
    add_f = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, irradiance=irradiance, name=f"final_additive{suffix}"))
    boo_f = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, name=f"final_boosting{suffix}"))
    ens_f = Cached(Ensemble([add_f, boo_f], weighting="recent", name=f"final_ensemble{suffix}"))
    return add_f, boo_f, ens_f


def final2_models(ba: str | None) -> list:
    add_f, boo_f, ens_f = final_members(ba, irradiance=ba in IRR_BAS)
    return [add_f, boo_f, ens_f,
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, nearest=40, peak="quantile", peak_quantile=0.60, name="final2")]


def irradiance_models(ba: str | None) -> list:
    add_f, boo_f, ens_f = final_members(ba)
    add_i, boo_i, ens_i = final_members(ba, irradiance=True, suffix="_irr")
    return [add_f, add_i, boo_f, boo_i, ens_f, ens_i,
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, nearest=40, name="final_nn40"),
            AdaptiveIntervals(ens_i, **FINAL_INTERVAL, nearest=40, name="final_nn40_irr")]


FINAL_INTERVAL = dict(by_regime=True, window_days=365, alpha_by_regime=True)


def feat_models(ba: str | None) -> list:
    solar = ba in PV_BAS
    add = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, name="final_additive"))
    boo = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, name="final_boosting"))
    return [add, boo,
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, extra=("load",), name="additive_xload")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, extra=("temp",), name="additive_xtemp")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, extra=("load", "temp"), name="additive_xall")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, extra=("load",), name="boosting_xload")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, extra=("temp",), name="boosting_xtemp")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_xsun")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=True, extra=("load", "temp"), name="boosting_xall"))]


def hp_models(ba: str | None) -> list:
    solar = ba in PV_BAS
    add = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, name="final_additive"))
    boo = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, name="final_boosting"))
    return [add, boo,
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, max_iter=800, learning_rate=0.03, max_leaf_nodes=63, name="boosting_deep")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, max_iter=300, max_leaf_nodes=15, min_samples_leaf=50, name="boosting_shallow")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, l2=1.0, name="boosting_l2")),
            Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, refit_days=3, name="boosting_refit3")),
            Cached(Boosting(train_days=2555, sky=solar, name="boosting_7y")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, n_knots=8, name="additive_k8")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, n_knots=10, name="additive_k10")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, val_days=90, name="additive_val90")),
            Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar,
                                 lambdas=(0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0), name="additive_lam")),
            Cached(AdditiveModel(train_days=2555, special_days=True, pv=solar, name="additive_7y"))]


def ens2_models(ba: str | None) -> list:
    from ba_load_forecast.forecasters.recency import RecencyRegression

    solar = ba in PV_BAS
    add = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=solar, name="final_additive"))
    boo = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, name="final_boosting"))
    boo_ratio = Cached(Boosting(train_days=TRAIN_DAYS, sky=solar, target="ratio", name="boosting_ratio"))
    rec_model = RecencyRegression(train_days=TRAIN_DAYS)
    rec_model.name = "recency_ml"
    rec = Cached(rec_model)
    ens = Cached(Ensemble([add, boo], weighting="recent", name="final_ensemble"))
    ens_h = Cached(Ensemble([add, boo], weighting="hourly", name="ens_hourly"))
    ens_3 = Cached(Ensemble([add, boo, rec], weighting="recent", name="ens_three"))
    ens_r = Cached(Ensemble([add, boo_ratio], weighting="recent", name="ens_ratio"))
    final = dict(FINAL_INTERVAL, nearest=40, peak="quantile", peak_quantile=0.60)
    return [add, boo, boo_ratio, rec, ens, ens_h, ens_3, ens_r,
            AdaptiveIntervals(ens, **final, name="final2"),
            AdaptiveIntervals(ens_h, **final, name="final2_hourly"),
            AdaptiveIntervals(ens_3, **final, name="final2_three"),
            AdaptiveIntervals(ens_r, **final, name="final2_ratio"),
            AdaptiveIntervals(ens, **dict(final, nearest=30), name="final2_nn30"),
            AdaptiveIntervals(ens, **dict(final, nearest=50), name="final2_nn50")]


FINAL3 = dict(                 # what phase G adds to the recipe (set from the feat, hp and ens2 reports; see docs/methods.md)
    extra_additive=("load", "temp"), extra_boosting=("load", "temp"), sun_everywhere=False,
    boosting=dict(), additive=dict(), train_days=TRAIN_DAYS,
    weighting="recent", third_member=True, ratio=False, nearest=40, temp_bias_days=0,
)


FINAL3B = dict(FINAL3, boosting=dict(max_iter=800, learning_rate=0.03, max_leaf_nodes=63), temp_bias_days=30)
HUMID = dict(FINAL3, extra_boosting=("load", "temp", "humidity", "wind"), apparent=True)   # phase H: humidity and wind
HUMID_H = dict(FINAL3, extra_boosting=("load", "temp", "humidity"), apparent=True)          # phase H: humidity alone (no wind field)
HUMID_L = dict(FINAL3, extra_boosting=("load", "temp", "humidity"), extra_additive=("load", "temp", "humidity"))  # phase H: linear terms


def final3b_models(ba: str | None) -> list:
    """``final3`` plus the deeper boosting and the temperature-bias correction (tested as a variant)."""
    return _final3_models(ba, FINAL3B, "final3b")


def final3_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL3, "final3")


def humid_h_models(ba: str | None) -> list:
    """Phase H, humidity alone: the phase G recipe with the humidity block in the boosting and the apparent
    temperature (heat index only, no wind field) in the additive model, plus the boosting with the block."""
    solar = ba in PV_BAS
    one = Cached(Boosting(train_days=FINAL3["train_days"], sky=solar, extra=("load", "temp", "humidity"), name="h_boosting"))
    return [one, *_final3_models(ba, HUMID_H, "final3_h")]


def humid_l_models(ba: str | None) -> list:
    """Phase H, idea A6b: the humidity block in the boosting and, in the additive model, the temperature spline kept
    with linear terms in the heat-index excess and the relative humidity (instead of the apparent temperature)."""
    return _final3_models(ba, HUMID_L, "final3_hl")


def humid_models(ba: str | None) -> list:
    """Phase H: the phase G recipe with the humidity and wind blocks in the boosting and the apparent temperature
    in the additive model (``final3_hw``), plus the boosting with one block at a time to attribute the gain."""
    solar = ba in PV_BAS
    one = [Cached(Boosting(train_days=FINAL3["train_days"], sky=solar, extra=("load", "temp", block), name=f"{short}_boosting"))
           for block, short in (("humidity", "h"), ("wind", "w"))]
    return [*one, *_final3_models(ba, HUMID, "final3_hw")]


def _final3_models(ba: str | None, c: dict, tag: str) -> list:
    """The phase G recipe: the phase F recipe with the options of ``c`` (``FINAL3`` or ``FINAL3B``)."""
    from ba_load_forecast.forecasters.recency import RecencyRegression

    solar = ba in PV_BAS
    add = Cached(AdditiveModel(train_days=c["train_days"], special_days=True, pv=solar, extra=c["extra_additive"],
                               apparent=c.get("apparent", False), **c["additive"], name=f"{tag}_additive"))
    boo = Cached(Boosting(train_days=c["train_days"], sky=solar or c["sun_everywhere"], extra=c["extra_boosting"],
                          target="ratio" if c["ratio"] else "level", **c["boosting"], name=f"{tag}_boosting"))
    members = [add, boo]
    if c["third_member"]:
        rec = RecencyRegression(train_days=c["train_days"])
        rec.name = f"{tag}_recency"
        members.append(Cached(rec))
    ens = Cached(Ensemble(members, weighting=c["weighting"], name=f"{tag}_ensemble"))
    return [*members, ens,
            AdaptiveIntervals(ens, **FINAL_INTERVAL, nearest=c["nearest"], peak="quantile", peak_quantile=0.60, name=tag)]


def final_models(ba: str | None) -> list:
    add_f, boo_f, ens_f = final_members(ba)
    return [add_f, boo_f, ens_f, AdaptiveIntervals(ens_f, **FINAL_INTERVAL, name="final")]


def peak_models(ba: str | None) -> list:
    add_f, boo_f, ens_f = final_members(ba)
    return [add_f, boo_f, ens_f,
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, name="final"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, peak="lift", name="final_peak_lift"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, peak="quantile", name="final_peak_q55"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, peak="quantile", peak_quantile=0.60, name="final_peak_q60")]


def intervals3_models(ba: str | None) -> list:
    add_f, boo_f, ens_f = final_members(ba)
    return [add_f, boo_f, ens_f,
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, name="final"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, nearest=40, name="final_nn40"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, nearest=60, name="final_nn60"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, tail=True, name="final_tail"),
            AdaptiveIntervals(ens_f, **FINAL_INTERVAL, nearest=40, tail=True, name="final_nn40_tail")]


def sky_members(add):
    boo_sky = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_sky"))
    ens_sky = Cached(Ensemble([add, boo_sky], weighting="recent", name="ens_sky"))
    return boo_sky, ens_sky


PER_BA_GROUPS = {          # groups whose members depend on the BA (solar features at ISO-NE and CAISO)
    "final": final_models, "intervals3": intervals3_models, "peak": peak_models, "irradiance": irradiance_models,
    "final2": final2_models, "frozen": final2_models,      # frozen: the same recipe, on other days
    "frozen2": final2_models,                            # frozen2: the phase F recipe on 2023-2025 under protocol v2
    "protocol": final2_models,                            # protocol: the same recipe, scored under protocol v2
    "feat": feat_models, "hp": hp_models, "ens2": ens2_models,
    "final3": final3_models, "frozen3": final3_models, "final3b": final3b_models, "humid": humid_models,
    "humid_h": humid_h_models, "humid_l": humid_l_models,
    "tbias": final2_models,
}


def group_models(group: str, ba: str | None = None) -> list:
    if group in PER_BA_GROUPS:
        return PER_BA_GROUPS[group](ba)
    add, boo, ens = corrected_ensemble()
    regime = dict(by_regime=True, window_days=365)
    groups = {
        "recipe": lambda: [add, boo, ens, EmpiricalIntervals(ens, name="ens_recent_bc")],
        "intervals": lambda: [add, boo, ens,
                              EmpiricalIntervals(ens, name="ens_bc_simple"),
                              EmpiricalIntervals(ens, **regime, name="ens_bc_regime"),
                              AdaptiveIntervals(ens, name="ens_bc_adaptive")],
        "intervals2": lambda: [add, boo, ens,
                               EmpiricalIntervals(ens, **regime, name="ens_bc_regime"),
                               AdaptiveIntervals(ens, name="ens_bc_adaptive"),
                               AdaptiveIntervals(ens, **regime, name="ens_bc_regime_aci"),
                               AdaptiveIntervals(ens, **regime, alpha_by_regime=True, name="ens_bc_regime_aci2")],
        "sky": lambda: sky_models(add, boo, ens, regime),
        "pv": lambda: pv_models(add),
        "pv2": lambda: pv2_models(add),
    }
    if group not in groups:
        raise SystemExit(f"unknown group {group}")
    return groups[group]()


def sky_models(add, boo, ens, regime) -> list:
    boo_sky, ens_sky = sky_members(add)
    return [add, boo, boo_sky, ens, ens_sky,
            EmpiricalIntervals(ens, **regime, name="ens_bc_regime"),
            EmpiricalIntervals(ens_sky, **regime, name="ens_sky_bc_regime")]


def pv_models(add) -> list:
    boo_pv = Cached(Boosting(train_days=TRAIN_DAYS, sky=True, name="boosting_ml_pv"))   # same model; the loader adds the PV columns
    ens_pv = Cached(Ensemble([add, boo_pv], weighting="recent", name="ens_pv"))
    return [add, boo_pv, ens_pv, EmpiricalIntervals(ens_pv, by_regime=True, window_days=365, name="ens_pv_bc_regime")]


def pv2_models(add) -> list:
    add_pv = Cached(AdditiveModel(train_days=TRAIN_DAYS, special_days=True, pv=True, name="additive_ml_pv"))
    boo_sky, ens_sky = sky_members(add)
    ens_pv2 = Cached(Ensemble([add_pv, boo_sky], weighting="recent", name="ens_pv2"))
    return [add, add_pv, boo_sky, ens_sky, ens_pv2,
            EmpiricalIntervals(ens_sky, by_regime=True, window_days=365, name="ens_sky_bc_regime"),
            EmpiricalIntervals(ens_pv2, by_regime=True, window_days=365, name="ens_pv2_bc_regime")]


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
    ap.add_argument("--supplement-dir", type=Path, nargs="+", default=[ROOT / "data" / "ghcnh", ROOT / "data" / "asos"],
                    help="observed temperature for the hours the ISD archive does not cover, applied in order: data/ghcnh "
                         "(scripts/fetch_ghcnh.py, NOAA) then data/asos (scripts/fetch_asos.py, Iowa Environmental Mesonet) for "
                         "the hours GHCNh lacks")
    ap.add_argument("--out", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e")
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "phase_e")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "phase_e.md")
    ap.add_argument("--report-only", action="store_true",
                    help="rebuild the reports of the groups in --groups from the files already in --out (use the group's --start/--end)")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)

    waiting = []
    if not a.report_only:
        for group in a.groups:
            for ba in (SKY_BAS if group == "sky" else PV_BAS if group in ("pv", "pv2", "irradiance") else a.bas):
                f = a.out / f"{group}_{ba}.parquet"
                if f.exists():
                    log(f"{group} {ba}: done already")
                    continue
                solar = group in PER_BA_GROUPS and ba in PV_BAS
                ld = loader(a, sky=group in ("sky", "pv", "pv2") or solar, pv=group in ("pv", "pv2") or solar,
                            irradiance=group == "irradiance" or (group == "final2" and ba in IRR_BAS),
                            temp_bias_days=30 if group == "tbias" else FINAL3B["temp_bias_days"] if group == "final3b"
                            else FINAL3["temp_bias_days"] if group in ("final3", "frozen3") else 0,
                            fields=WEATHER_FIELDS if group == "humid" else ("dewpoint_f",) if group in ("humid_h", "humid_l") else ())
                if not stations_ready(ld, ba) or not fields_ready(ld, ba):
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
        if not set(prefixes) & set(a.groups):          # only the groups asked for: a report carries the period of the command line
            return None
        files = sorted(p for p in a.out.glob("*.parquet")
                       if not p.name.endswith("_hourly.parquet")
                       and any(re.fullmatch(re.escape(pre) + r"_[A-Z0-9]+\.parquet", p.name) for pre in prefixes))
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
    iv3 = report({"intervals3"}, a.results.parent / "phase_e_intervals3", a.doc.parent / "phase_e_intervals3.md",
                 "Phase E: intervals for the coldest days",
                 "Development BAs: " + common +
                 "`final` is the recipe's interval (regime-conditional errors over a year, adaptive level per regime); "
                 "`final_nn40` and `final_nn60` restrict the pool to the 40 or 60 known days nearest to the target day in forecast "
                 "daily minimum temperature; `final_tail` reads the outer quantiles from an exponential fitted beyond the pool's "
                 "10th and 90th percentiles; `final_nn40_tail` does both.")
    peak = report({"peak"}, a.results.parent / "phase_e_peak", a.doc.parent / "phase_e_peak.md",
                  "Phase E: the under-forecast at the daily peak",
                  "Development BAs: " + common +
                  "`final` is the recipe; `final_peak_lift` replaces the hourly median correction, at the hours within 3 % of the "
                  "forecast maximum, by the median of the errors measured at the actual peak hour of the pool days; `final_peak_q55` and "
                  "`final_peak_q60` read the point at the 55th or 60th percentile of the errors at those hours instead of the median. "
                  "The 90 % band moves with the point.")
    irr = report({"irradiance"}, a.results.parent / "phase_e_irradiance", a.doc.parent / "phase_e_irradiance.md",
                 "Phase F: forecast irradiance as a feature",
                 "BAs with large solar behind the load: " + common +
                 "`*_irr` models receive the HRRR forecast surface short-wave flux as seen at each day's cut-off (GRIB2 archive, "
                 "from December 2020): the boosting as a column, the additive model as the installed PV capacity times the flux, in "
                 "place of the capacity times the cloud fraction. `final_nn40` and `final_nn40_irr` are the corrected ensembles with "
                 "the nearest-temperature pool, without and with it.")
    final2 = report({"final2"}, a.results.parent / "phase_f_final", a.doc.parent / "phase_f_final.md",
                    "Phase F: the recipe in one run",
                    "Development BAs: " + common +
                    "One run of the recipe after phase F: the phase E members (additive model with special days and, at ISO-NE and "
                    "CAISO, the PV terms; boosting with the sky features there), their ensemble by recent error, the median correction "
                    "and the 90 % band read from the 40 known days of the same regime nearest in forecast minimum temperature, at an "
                    "adaptive level per regime, and the point read at the 60th percentile around the forecast peak.")
    frozen = report({"frozen"}, a.results.parent / "frozen_2023_2025", a.doc.parent / "frozen_evaluation.md",
                    "Frozen evaluation: the recipe on days the development never saw",
                    "Development BAs: " + common +
                    "The recipe settled at the end of phase F (`final2`: additive model with special days and, at ISO-NE and CAISO, "
                    "the PV terms; boosting with the sky features there; ensemble by recent error; median correction and 90 % band from "
                    "the 40 known days of the same regime nearest in forecast minimum temperature, adaptive level per regime; point at "
                    "the 60th percentile around the forecast peak), run once on 2023 to 2025 without any change after seeing these days. "
                    "The models keep learning day by day from the six years before each day, as in operation.")
    proto = report({"protocol"}, a.results.parent / "phase_g_protocol", a.doc.parent / "phase_g_protocol.md",
                   "Phase G: the recipe under protocol v2",
                   "Development BAs: " + common +
                   "The phase F recipe (`final2`), scored under protocol v2: a day on which the published forecast is missing, "
                   "non-positive or more than 50 % away from the outcome at any hour is left out for every model, as is a day with an "
                   "hour more than 40 % away from the mean of its neighbours; and the documented hour-label offsets "
                   "(`docs/hour_label_offsets.csv`: PJM forecast +1 h from February 2019, CAISO demand -1 h from 14 June 2022) are "
                   "applied to the published series before anything else, for the models and for `DF` alike.")
    g_common = "Development BAs: " + common + "Protocol v2 (`docs/phase_g_protocol.md`). "
    feat = report({"feat"}, a.results.parent / "phase_g_features", a.doc.parent / "phase_g_features.md",
                  "Phase G: feature blocks", g_common +
                  "`*_xload` adds the load two and three weeks back and the mean of the same weekday last week; `*_xtemp` adds "
                  "yesterday's extremes, the heating and cooling degree-hours of the previous 72 hours, the day's range and its "
                  "temperature at 07:00 and 17:00; `boosting_xsun` gives every BA the sun's elevation; `*_xall` combines them.")
    hp = report({"hp"}, a.results.parent / "phase_g_parameters", a.doc.parent / "phase_g_parameters.md",
                "Phase G: parameters", g_common +
                "Boosting: `deep` 800 iterations at rate 0.03 with 63 leaves; `shallow` 300 iterations, 15 leaves, 50 samples per leaf; "
                "`l2` regularisation 1.0; `refit3` refitted every 3 days; `7y` trained on 2555 days. Additive: 8 and 10 knots; 90 "
                "validation days; a penalty grid from 0.001 to 1000; 2555 training days.")
    ens2 = report({"ens2"}, a.results.parent / "phase_g_ensemble", a.doc.parent / "phase_g_ensemble.md",
                  "Phase G: ensemble and correction", g_common +
                  "`ens_hourly` weights the members per hour of the day; `ens_three` adds the recency regression; `ens_ratio` uses "
                  "a boosting trained on the load divided by the last known 24 h mean; `final2_*` are the corrected versions with "
                  "the recipe's correction; `final2_nn30` and `final2_nn50` change the size of the nearest-temperature pool.")
    final3 = report({"final3"}, a.results.parent / "phase_g_final", a.doc.parent / "phase_g_final.md",
                    "Phase G: the recipe after phase G, in one run", g_common +
                    "The phase F recipe with what phase G added (see `docs/methods.md`), run once on the development period.")
    frozen3 = report({"frozen3"}, a.results.parent / "frozen3_2023_2025", a.doc.parent / "frozen_evaluation_v2.md",
                     "Second look at 2023 to 2025: the recipe after phase G, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase G on 2023 to 2025 under protocol v2. This is a second look at these years: the choices of "
                     "phase G were made on the development period, but the frozen run of `final2` had already been seen; the honest "
                     "reading compares this table with `docs/frozen_evaluation.md` and treats the difference as an estimate, not a proof.")
    tbias = report({"tbias"}, a.results.parent / "phase_g_tbias", a.doc.parent / "phase_g_tbias.md",
                   "Phase G: the temperature forecast corrected by its own recent bias", g_common +
                   "The phase F recipe with the HRRR 2 m temperature path of every station moved by the median of the forecast's own "
                   "error at that local hour over the last 30 known days (forecast as seen at the cut-off against the airport observation). "
                   "Compare with `docs/phase_g_protocol.md` (same recipe, no correction).")
    final3b = report({"final3b"}, a.results.parent / "phase_g_final_b", a.doc.parent / "phase_g_final_b.md",
                     "Phase G: the recipe with the deeper boosting and the temperature-bias correction", g_common +
                     "`final3b` is `final3` with the boosting at 800 iterations, rate 0.03 and 63 leaves, and the HRRR temperature path "
                     "corrected by its own recent bias per local hour (30 known days). Compare with `docs/phase_g_final.md`.")
    humid_h = report({"humid_h"}, a.results.parent / "phase_h_humidity_only", a.doc.parent / "phase_h_humidity_only.md",
                     "Phase H: humidity alone", g_common +
                     "`final3_h` is the phase G recipe with the dew point, dew-point depression, relative humidity and heat index as "
                     "features of the boosting and the heat index as the input of the additive model's smooth response (no wind "
                     "field yet); `h_boosting` adds the block to the phase G boosting. Compare with `docs/phase_g_final.md` (same days).")
    humid_l = report({"humid_l"}, a.results.parent / "phase_h_humidity_linear", a.doc.parent / "phase_h_humidity_linear.md",
                     "Phase H: humidity with linear terms in the additive model", g_common +
                     "`final3_hl` is `final3_h` with the additive model keeping its temperature spline and adding linear terms in "
                     "the heat-index excess over the temperature and in the relative humidity, instead of fitting on the apparent "
                     "temperature. Compare with `docs/phase_h_humidity_only.md` and `docs/phase_g_final.md` (same days).")
    humid = report({"humid"}, a.results.parent / "phase_h_humidity", a.doc.parent / "phase_h_humidity.md",
                   "Phase H: humidity and wind", g_common +
                   "`final3_hw` is the phase G recipe with the dew point, dew-point depression, relative humidity, heat index, wind "
                   "speed and wind chill (NWS formulas) as features of the boosting and the apparent temperature as the input of "
                   "the additive model's smooth response; `h_boosting` and `w_boosting` add one block at a time to the phase G "
                   "boosting. Observed dew point and wind from ISD-Lite and the supplements, forecasts from the HRRR archive. "
                   "Compare with `docs/phase_g_final.md` (same days).")
    frozen2 = report({"frozen2"}, a.results.parent / "frozen2_2023_2025", a.doc.parent / "frozen_evaluation_final2_v2.md",
                     "The phase F recipe on 2023 to 2025 under protocol v2",
                     "Development BAs: " + common +
                     "The phase F recipe (`final2`) on 2023 to 2025 scored under protocol v2, the reference for `docs/frozen_evaluation_v2.md` "
                     "(same days, same rules).")
    if all(t is None for t in (main, sky, pv, iv2, pv2, final, iv3, peak, irr, final2, frozen, proto, feat, hp, ens2, final3, frozen3, tbias, final3b, frozen2, humid, humid_h, humid_l)):
        log("no rows to report")
        return 1
    if waiting:
        log(f"still waiting for station forecasts: {waiting}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
