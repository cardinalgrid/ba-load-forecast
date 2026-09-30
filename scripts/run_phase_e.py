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
from ba_load_forecast.paths import DATA, ISD, TIDY
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


def nbm_group_options() -> dict:
    """group -> loader options for the NBM input (folders under the data root: nbm/, nbm_daily/); built at call time
    because the recipe dictionaries are defined further down."""
    return {"nbm_blend": dict(nbm_mode="blend"), "nbm_replace": dict(nbm_mode="replace"), "nbm_cold": dict(nbm_daily=True),
            "frozen6": FINAL6, "blendw": FINAL6W, "blendc": FINAL6C, "blendwc": FINAL6WC, "nbmfld": FINAL6F, "nbmirr": FINAL6I,
            "gfs3": FINAL7, "frozen7": FINAL7, "mw3": FINAL8, "mw2": FINAL8B, "mw3c": FINAL8C, "mw3q": FINAL8Q, "frozen8": FINAL8Q, "storm": FINAL9, "storm2": FINAL9B, "band_a": FINAL10A, "band_a2": FINAL10A2, "band_a2t": FINAL10A2T, "band_b": FINAL10B, "band_s": FINAL10S, "band_as": FINAL10AS, "band_ast": FINAL10AST, "frozen10": FINAL10A2T}


def nbm_options(group: str) -> dict:
    c = nbm_group_options().get(group, {})
    out = {}
    if c.get("nbm_mode"):
        out["nbm_dir"] = DATA / "nbm"
        out["nbm_mode"] = c["nbm_mode"]
    if c.get("nbm_daily"):
        out["nbm_daily_dir"] = DATA / "nbm_daily"
    for k in ("nbm_weight", "nbm_cold_bias_days", "nbm_cold_threshold_f"):
        if k in c:
            out[k] = c[k]
    if c.get("nbm_fields"):
        out["nbm_field_dirs"] = {"dewpoint_f": DATA / "nbm_dewpoint", "wind_ms": DATA / "nbm_wind"}
    if c.get("nbm_dswrf"):
        out["nbm_dswrf_dir"] = DATA / "nbm_dswrf"
    if c.get("gfs"):
        out["gfs_dir"] = DATA / "gfs"
    if c.get("model_weights"):
        out["model_weight_days"] = c["model_weights"]
    if c.get("model_weights_cold"):
        out["model_weight_cold_days"] = c["model_weights_cold"]
    if c.get("gfs_cold_quantile"):
        out["gfs_cold_quantile"] = c["gfs_cold_quantile"]
    if c.get("nbm_spread"):
        out["nbm_spread_dir"] = DATA / "nbm_tempstd"
    return out


def loader(a, sky: bool = False, pv: bool = False, irradiance: bool = False, temp_bias_days: int = 0,
           fields: tuple[str, ...] = (), field_bias_days: int = 0, second_run: bool = False, nbm: dict | None = None) -> Loader:
    return Loader(a.tidy, a.isd_dir, a.hrrr, history_days=HISTORY_DAYS, stations="multi", sky=sky, pv=pv, irradiance=irradiance,
                  temp_bias_days=temp_bias_days, supplement_dir=a.supplement_dir, fields=fields, field_bias_days=field_bias_days,
                  second_run=second_run, **(nbm or {}))


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
HUMID_P = dict(FINAL3, extra_boosting=("load", "temp", "humidity"))                       # phase H: humidity in the boosting only
FINAL4 = HUMID_H                                                                            # the recipe after phase H (= final3_h)
FINAL4B = dict(FINAL4, field_bias_days=30)              # phase H, idea A16: the dew point path corrected by its own recent bias
EXTRA_LEVELS = (0.01, 0.02, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.98, 0.99)
FINAL4Q = dict(FINAL4, intervals=dict(extra_levels=EXTRA_LEVELS))                                      # A17: 23 quantiles in all
FINAL4R = dict(FINAL4Q, boosting=dict(loss="absolute_error"))                                           # A19: robust loss in the boosting
FINAL4W = dict(FINAL4Q, extra_boosting=("load", "temp", "humidity", "wind"), apparent_wind=False)      # wind in the boosting only
FINAL4P = dict(FINAL4Q, intervals=dict(extra_levels=EXTRA_LEVELS, peak_quantile_cold=0.70))            # A8: peak quantile 0.70 on the coldest decile
FINAL5 = dict(FINAL4W, intervals=dict(extra_levels=EXTRA_LEVELS, peak_quantile_cold=0.70))             # the recipe after phase I: wind in the boosting + cold-day peak quantile
FINAL5A = dict(FINAL5, second_run=True)                                                                  # A20: the cut-off run and the run 6 h older averaged (Loader option)
FINAL5B = dict(FINAL5, intervals=dict(extra_levels=EXTRA_LEVELS, peak_quantile_cold=0.70, cold_by_max=True,
                                      peak_quantile_hot=0.70, hot_decile=0.90))                        # A8b: cold by the forecast maximum too, and the hottest decile
FINAL5C = dict(FINAL5, cold_weight=2.0)                                                                  # A22: cold-day training weights in both fitted members
FINAL6N = dict(FINAL5, nbm_mode="blend")                                                                # A21: NBM hourly temperature averaged with the HRRR path
FINAL6R = dict(FINAL5, nbm_mode="replace")                                                              # A21: NBM hourly temperature instead of the HRRR path where it has the hour
FINAL6P = dict(FINAL5, nbm_daily=True, intervals=dict(extra_levels=EXTRA_LEVELS, peak_quantile_cold=0.70, cold_source="mint18p05"))   # A24: cold-day rule on the NBM 5th-percentile minimum
FINAL6 = FINAL6N                                                                                         # the recipe after phase K
FINAL6W = dict(FINAL6, nbm_weight=0.7)                                                                   # A21b: inverse-variance weight on the NBM (MAE 2.05 vs 3.12 F)
FINAL6C = dict(FINAL6, nbm_cold_bias_days=365)                                                           # A21c: the NBM moved by its own cold-hour bias of the last year
FINAL6WC = dict(FINAL6, nbm_weight=0.7, nbm_cold_bias_days=365)                                          # both
FINAL6F = dict(FINAL6, nbm_fields=True)                                                                  # A21d: NBM dew point and wind blended with the HRRR fields
FINAL6I = dict(FINAL6, nbm_dswrf=True, irradiance=True)                                                  # B8: NBM irradiance in the additive PV term (ISO-NE, CAISO)
FINAL7 = dict(FINAL6, gfs=True)                                                                          # phase M: the GFS as a third model in the temperature mean
FINAL8 = dict(FINAL7, model_weights=30)                                                                  # phase N (A27): HRRR, NBM and GFS weighted per station by their 30-day error
FINAL8B = dict(FINAL6, model_weights=30)                                                                 # phase N: HRRR and NBM only, weighted per station
FINAL8C = dict(FINAL8, model_weights_cold=365)                                                           # phase N: on cold days, weights from the cold hours of the last year
FINAL8Q = dict(FINAL8, gfs_cold_quantile=0.10)                                                           # phase N: the GFS leaves the mean on days below the station's cold decile
FINAL9 = dict(FINAL8Q, storm="boosting")                                                                # phase O (A9): a boosting member fitted on the cold decile, used on cold days
FINAL9B = dict(FINAL8Q, storm="both")                                                                   # phase O: a boosting and an additive storm member
FINAL10A = dict(FINAL8Q, intervals=dict(FINAL8Q["intervals"], cold_level="scale", cold_alpha_scale=0.5))     # A1: the nominal level halved on cold days
FINAL10B = dict(FINAL8Q, intervals=dict(FINAL8Q["intervals"], cold_level="adaptive", cold_gamma=0.10))     # A1: a separate adaptive level on cold days
FINAL10S = dict(FINAL8Q, nbm_spread=True, intervals=dict(FINAL8Q["intervals"], spread_beta=1.0))            # A24c: the NBM spread as the width factor
FINAL10AS = dict(FINAL10S, intervals=dict(FINAL10S["intervals"], cold_level="scale", cold_alpha_scale=0.5))  # A1 + A24c
FINAL10AST = dict(FINAL10S, intervals=dict(FINAL10S["intervals"], cold_level="scale", cold_alpha_scale=0.25, cold_tail=True))  # A24c on top of the A1 candidate
FINAL10A2 = dict(FINAL8Q, intervals=dict(FINAL8Q["intervals"], cold_level="scale", cold_alpha_scale=0.25))    # A1: the level quartered on cold days
FINAL10A2T = dict(FINAL10A2, intervals=dict(FINAL10A2["intervals"], cold_tail=True))                        # A1: the quartered level and the exponential tail on cold days


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


def final4_models(ba: str | None) -> list:
    """The recipe after phase H: the phase G recipe with the humidity block in the boosting and the apparent
    temperature in the additive model (no wind); ``frozen4`` runs it on 2023 to 2025."""
    return _final3_models(ba, FINAL4, "final4")


def humid_b_models(ba: str | None) -> list:
    """Phase H, idea A16: ``final4`` with the HRRR dew point path corrected by the median of its own error per local
    hour over the last 30 known days (the temperature correction of phase G applied to the dew point)."""
    return _final3_models(ba, FINAL4B, "final4b")


def events_models(ba: str | None) -> list:
    """Ideas A17, A19, A8 and the wind in the boosting only, side by side: the phase H recipe with 23 quantiles
    (`final4`), the same with a robust loss in the boosting (`final4r`), with the wind block in the boosting and the
    apparent temperature without wind chill (`final4w`), and with the peak read at the 70th percentile on the
    coldest decile of days (`final4p`)."""
    return [*_final3_models(ba, FINAL4Q, "final4"), *_final3_models(ba, FINAL4R, "final4r"),
            *_final3_models(ba, FINAL4W, "final4w"), *_final3_models(ba, FINAL4P, "final4p")]


def humid_p_models(ba: str | None) -> list:
    """Phase H: the humidity block in the boosting only; the additive model as in phase G."""
    return _final3_models(ba, HUMID_P, "final3_hp")


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
                               irradiance=solar and c.get("irradiance", False),
                               apparent=c.get("apparent", False), apparent_wind=c.get("apparent_wind", True), **c["additive"],
                               cold_weight=c.get("cold_weight", 0.0), name=f"{tag}_additive"))
    boo = Cached(Boosting(train_days=c["train_days"], sky=solar or c["sun_everywhere"], extra=c["extra_boosting"],
                          target="ratio" if c["ratio"] else "level", **c["boosting"], cold_weight=c.get("cold_weight", 0.0),
                          name=f"{tag}_boosting"))
    members = [add, boo]
    if c.get("storm"):                                                # A9: members fitted on the coldest decile of days, answering on such days only
        members.append(Cached(Boosting(train_days=c["train_days"], sky=solar or c["sun_everywhere"], extra=c["extra_boosting"],
                                       target="ratio" if c["ratio"] else "level", **c["boosting"], cold_only=0.10,
                                       name=f"{tag}_storm")))
        if c["storm"] == "both":
            members.append(Cached(AdditiveModel(train_days=c["train_days"], special_days=True, pv=solar, extra=c["extra_additive"],
                                                irradiance=solar and c.get("irradiance", False), apparent=c.get("apparent", False),
                                                apparent_wind=c.get("apparent_wind", True), **c["additive"], cold_only=0.10,
                                                name=f"{tag}_storm_additive")))
    if c["third_member"]:
        rec = RecencyRegression(train_days=c["train_days"])
        rec.name = f"{tag}_recency"
        members.append(Cached(rec))
    ens = Cached(Ensemble(members, weighting=c["weighting"], name=f"{tag}_ensemble"))
    return [*members, ens,
            AdaptiveIntervals(ens, **FINAL_INTERVAL, nearest=c["nearest"], peak="quantile", peak_quantile=0.60,
                              **c.get("intervals", {}), name=tag)]


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


def extremes_models(ba: str | None) -> list:
    """Phase J, ideas A8b and A22 next to the phase I recipe: `final5`; `final5b` with the peak quantile 0.70 also
    when the forecast maximum is in the coldest decile or in the hottest decile; `final5c` with cold-day training
    weights (1 plus 2 for every 10 F the day's observed minimum lies below the coldest decile of the training days)
    in the additive and boosting members."""
    return [*_final3_models(ba, FINAL5, "final5"), *_final3_models(ba, FINAL5B, "final5b"), *_final3_models(ba, FINAL5C, "final5c")]


def extremes2_models(ba: str | None) -> list:
    """Phase J, idea A20: the phase I recipe fed with the mean of the cut-off HRRR run and the run 6 h older
    (`Loader(second_run=True)`; its own group because the loader option changes every model's input)."""
    return _final3_models(ba, FINAL5A, "final5a")


def nbm_blend_models(ba: str | None) -> list:
    """Phase K, idea A21: the phase I recipe with the NBM hourly temperature averaged with the HRRR path (loader option)."""
    return _final3_models(ba, FINAL6N, "final6n")


def nbm_replace_models(ba: str | None) -> list:
    """Phase K, idea A21: the phase I recipe with the NBM hourly temperature in place of the HRRR path where the NBM has the hour."""
    return _final3_models(ba, FINAL6R, "final6r")


def nbm_cold_models(ba: str | None) -> list:
    """Phase K, idea A24: the phase I recipe with the cold-day peak rule read from the NBM 5th-percentile 18-h minimum."""
    return _final3_models(ba, FINAL6P, "final6p")


def blendw_models(ba: str | None) -> list:
    """Phase L, idea A21b: the phase K recipe with 0.7 weight on the NBM in the temperature blend."""
    return _final3_models(ba, FINAL6W, "final6w")


def blendc_models(ba: str | None) -> list:
    """Phase L, idea A21c: the phase K recipe with the NBM path corrected by its own cold-hour bias (365 known days)."""
    return _final3_models(ba, FINAL6C, "final6c")


def blendwc_models(ba: str | None) -> list:
    """Phase L: both A21b and A21c."""
    return _final3_models(ba, FINAL6WC, "final6wc")


def nbmfld_models(ba: str | None) -> list:
    """Phase L, idea A21d: the phase K recipe with the NBM dew point and wind blended into the humidity and wind fields."""
    return _final3_models(ba, FINAL6F, "final6f")


def nbmirr_models(ba: str | None) -> list:
    """Phase L, idea B8: the phase K recipe with the NBM irradiance in place of the cloud fraction in the additive PV term."""
    return _final3_models(ba, FINAL6I, "final6i")


def mw3_models(ba: str | None) -> list:
    """Phase N: three weather models weighted per station by the inverse of their recent mean squared error."""
    return _final3_models(ba, FINAL8, "final8")


def mw3c_models(ba: str | None) -> list:
    """Phase N: three models weighted per station, with cold-day weights from the cold hours of the last year."""
    return _final3_models(ba, FINAL8C, "final8c")


def band_a_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10A, "final10a")


def band_a2_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10A2, "final10a2")


def band_a2t_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10A2T, "final10a2t")


def band_b_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10B, "final10b")


def band_s_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10S, "final10s")


def band_as_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10AS, "final10as")


def band_ast_models(ba: str | None) -> list:
    return _final3_models(ba, FINAL10AST, "final10ast")


def storm_models(ba: str | None) -> list:
    """Phase O: the phase N recipe with a boosting storm member (fitted on the cold decile, used on cold days)."""
    return _final3_models(ba, FINAL9, "final9")


def storm2_models(ba: str | None) -> list:
    """Phase O: the phase N recipe with a boosting and an additive storm member."""
    return _final3_models(ba, FINAL9B, "final9b")


def mw3q_models(ba: str | None) -> list:
    """Phase N: three models weighted per station, the GFS left out on days below the station's cold decile."""
    return _final3_models(ba, FINAL8Q, "final8q")


def mw2_models(ba: str | None) -> list:
    """Phase N: the HRRR and the NBM weighted per station (no GFS), to separate the weighting from the third model."""
    return _final3_models(ba, FINAL8B, "final8b")


def gfs3_models(ba: str | None) -> list:
    """Phase M: the phase K recipe with the temperature path as the mean of HRRR, NBM and GFS, hour by hour."""
    return _final3_models(ba, FINAL7, "final7")


def final6_models(ba: str | None) -> list:
    """The recipe after phase K (set FINAL6 to the winner); ``frozen6`` runs it on 2023 to 2025."""
    return _final3_models(ba, FINAL6, "final6")


def final5_models(ba: str | None) -> list:
    """The candidate after phase I: `final4w` (wind block in the boosting, apparent temperature without wind chill)
    with the peak read at the 70th percentile on the coldest decile of days and 23 quantiles; ``frozen5`` runs it
    on 2023 to 2025."""
    return _final3_models(ba, FINAL5, "final5")


PER_BA_GROUPS = {          # groups whose members depend on the BA (solar features at ISO-NE and CAISO)
    "final": final_models, "intervals3": intervals3_models, "peak": peak_models, "irradiance": irradiance_models,
    "final2": final2_models, "frozen": final2_models,      # frozen: the same recipe, on other days
    "frozen2": final2_models,                            # frozen2: the phase F recipe on 2023-2025 under protocol v2
    "protocol": final2_models,                            # protocol: the same recipe, scored under protocol v2
    "feat": feat_models, "hp": hp_models, "ens2": ens2_models,
    "final3": final3_models, "frozen3": final3_models, "final3b": final3b_models, "humid": humid_models,
    "humid_h": humid_h_models, "humid_l": humid_l_models, "humid_p": humid_p_models,
    "final4": final4_models, "frozen4": final4_models, "humid_b": humid_b_models, "events": events_models,
    "final5": final5_models, "frozen5": final5_models, "extremes": extremes_models, "extremes2": extremes2_models,
    "nbm_blend": nbm_blend_models, "nbm_replace": nbm_replace_models, "nbm_cold": nbm_cold_models, "frozen6": final6_models,
    "blendw": blendw_models, "blendc": blendc_models, "blendwc": blendwc_models, "nbmfld": nbmfld_models, "nbmirr": nbmirr_models,
    "gfs3": gfs3_models, "frozen7": gfs3_models, "mw3": mw3_models, "mw2": mw2_models, "mw3c": mw3c_models, "mw3q": mw3q_models, "frozen8": mw3q_models, "storm": storm_models, "storm2": storm2_models, "band_a": band_a_models, "band_a2": band_a2_models, "band_a2t": band_a2t_models, "band_b": band_b_models, "band_s": band_s_models, "band_as": band_as_models, "band_ast": band_ast_models, "frozen10": band_a2t_models,
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
    ap.add_argument("--tidy", type=Path, default=TIDY)
    ap.add_argument("--isd-dir", type=Path, default=ISD)
    ap.add_argument("--hrrr", type=Path, default=DATA / "hrrr")
    ap.add_argument("--supplement-dir", type=Path, nargs="+", default=[DATA / "ghcnh", DATA / "asos"],
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
                            irradiance=group in ("irradiance", "nbmirr") or (group == "final2" and ba in IRR_BAS),
                            temp_bias_days=30 if group == "tbias" else FINAL3B["temp_bias_days"] if group == "final3b"
                            else FINAL3["temp_bias_days"] if group in ("final3", "frozen3") else 0,
                            fields=WEATHER_FIELDS if group in ("humid", "events", "final5", "frozen5", "extremes", "extremes2", "nbm_blend", "nbm_replace", "nbm_cold", "frozen6", "blendw", "blendc", "blendwc", "nbmfld", "nbmirr", "gfs3", "frozen7", "mw3", "mw2", "mw3c", "mw3q", "frozen8", "storm", "storm2", "band_a", "band_a2", "band_a2t", "band_b", "band_s", "band_as", "band_ast", "frozen10") else ("dewpoint_f",) if group in ("humid_h", "humid_l", "humid_p", "final4", "frozen4", "humid_b") else (),
                            field_bias_days=FINAL4B["field_bias_days"] if group == "humid_b" else 0,
                            second_run=group == "extremes2", nbm=nbm_options(group))
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
    events = report({"events"}, a.results.parent / "phase_i_events", a.doc.parent / "phase_i_events.md",
                    "Phase I: robust loss, wind in the boosting, cold-day peak quantile, 23 quantiles", g_common +
                    "`final4` with 23 quantiles (CRPS, Winkler); `final4r` with the boosting fitted by absolute error; `final4w` with "
                    "the wind block in the boosting and the apparent temperature without wind chill in the additive model; `final4p` "
                    "reading the point at the 70th percentile around the peak on the coldest decile of days. Compare on the winter events "
                    "and on the year.")
    final5 = report({"final5"}, a.results.parent / "phase_i_final", a.doc.parent / "phase_i_final.md",
                    "Phase I: the candidate recipe on the development years", g_common +
                    "`final5` is `final4` with the wind block in the boosting (apparent temperature without wind chill in the additive "
                    "model) and the point read at the 70th percentile around the peak on the coldest decile of days, with 23 quantiles. "
                    "Compare with `docs/phase_i_events.md` (same days).")
    extremes = report({"extremes"}, a.results.parent / "phase_j_extremes", a.doc.parent / "phase_j_extremes.md",
                      "Phase J: the hot and cold peak quantile and cold-day training weights", g_common +
                      "`final5` is the phase I recipe; `final5b` reads the point at the 70th percentile around the peak also when the "
                      "forecast maximum is in the coldest decile of known maxima or in the hottest decile; `final5c` fits the additive "
                      "and boosting members with training weights that grow with the distance of the day's observed minimum below the "
                      "coldest decile of the training days. Compare on the winter events, the coldest mornings and the year.")
    extremes2 = report({"extremes2"}, a.results.parent / "phase_j_second_run", a.doc.parent / "phase_j_second_run.md",
                       "Phase J: the cut-off run and the run 6 h older averaged", g_common +
                       "`final5a` is the phase I recipe fed with the mean of the HRRR run available at the cut-off and the run six "
                       "hours older, hour by hour where both cover the hour (in the Eastern zone in daylight time the cut-off run is the "
                       "06 UTC one and no older run is extracted, so the recipe falls back to the single run). Compare with "
                       "`docs/phase_j_extremes.md` (same days).")
    nbm_common = ("`final6n` averages the NBM 2 m temperature at the stations with the HRRR path hour by hour; `final6r` uses the NBM "
                  "where it has the hour and the HRRR elsewhere; `final6p` keeps the HRRR path and reads the cold-day peak rule from the NBM "
                  "5th-percentile 18-hour minimum. NBM files: one GeoTIFF per element and forecast hour in the public archive, hourly to 36 h "
                  "and three-hourly beyond (interpolated). Compare with `docs/phase_i_final.md` (same days).")
    nbm_blend = report({"nbm_blend"}, a.results.parent / "phase_k_nbm_blend", a.doc.parent / "phase_k_nbm_blend.md",
                       "Phase K: the NBM temperature averaged with the HRRR", g_common + nbm_common)
    nbm_replace = report({"nbm_replace"}, a.results.parent / "phase_k_nbm_replace", a.doc.parent / "phase_k_nbm_replace.md",
                         "Phase K: the NBM temperature in place of the HRRR", g_common + nbm_common)
    nbm_cold = report({"nbm_cold"}, a.results.parent / "phase_k_nbm_cold", a.doc.parent / "phase_k_nbm_cold.md",
                      "Phase K: the cold-day peak rule on the NBM minimum", g_common + nbm_common)
    l_common = ("Compare with `docs/phase_k_nbm_blend.md` (`final6n`, the plain mean, same days). ")
    blendw = report({"blendw"}, a.results.parent / "phase_l_weight", a.doc.parent / "phase_l_weight.md",
                    "Phase L: 0.7 weight on the NBM in the temperature blend", g_common + l_common +
                    "`final6w` weights the NBM 0.7 and the HRRR 0.3 (the inverse-variance weights of the two verifications).")
    blendc = report({"blendc"}, a.results.parent / "phase_l_cold_bias", a.doc.parent / "phase_l_cold_bias.md",
                    "Phase L: the NBM corrected by its own cold-hour bias", g_common + l_common +
                    "`final6c` moves the NBM path, on hours forecast below 25 F, by the median of observed minus forecast on such hours "
                    "over the last 365 known days at the station (the NBM is too warm in the cold), before the plain mean with the HRRR.")
    blendwc = report({"blendwc"}, a.results.parent / "phase_l_both", a.doc.parent / "phase_l_both.md",
                     "Phase L: the 0.7 weight and the cold-hour bias together", g_common + l_common + "`final6wc` applies both changes.")
    nbmfld = report({"nbmfld"}, a.results.parent / "phase_l_fields", a.doc.parent / "phase_l_fields.md",
                    "Phase L: the NBM dew point and wind blended into the fields", g_common + l_common +
                    "`final6f` averages the NBM dew point and wind speed with the HRRR paths of those fields, hour by hour, before the "
                    "humidity and wind blocks are built (the temperature is already averaged).")
    nbmirr = report({"nbmirr"}, a.results.parent / "phase_l_irradiance", a.doc.parent / "phase_l_irradiance.md",
                    "Phase L: the NBM irradiance in the PV term", g_common + l_common +
                    "`final6i` feeds the additive model's PV term with the NBM surface short-wave flux as seen at the cut-off, in "
                    "place of the cloud fraction, at the BAs with the PV terms (ISO-NE, CAISO).")
    gfs3 = report({"gfs3"}, a.results.parent / "phase_m_gfs", a.doc.parent / "phase_m_gfs.md",
                  "Phase M: the GFS as a third weather model", g_common +
                  "`final7` is the phase K recipe with the temperature path taken as the mean, hour by hour, of the HRRR, the NBM and the "
                  "GFS 0.25 degree run available at the cut-off (a 5 h availability lag: 06 UTC in most zones), each model where it has "
                  "the hour; before 23 March 2021 the GFS archive is three-hourly and its path is interpolated. Compare with "
                  "`docs/phase_k_nbm_blend.md` (`final6n`, same days).")
    mw3 = report({"mw3"}, a.results.parent / "phase_n_weights3", a.doc.parent / "phase_n_weights3.md",
                 "Phase N: the weather models weighted per station by their recent error", g_common +
                 "`final8` is `final7` (HRRR, NBM and GFS in the temperature mean) with the weights of the three models set per station and "
                 "per day as the inverse of each model's mean squared error at that station's observations over the last 30 days known at "
                 "the cut-off (equal weights with fewer than 240 common hours). Compare with `docs/phase_k_nbm_blend.md` (`final6n`) and "
                 "`docs/phase_m_gfs.md` (`final7`), same days.")
    mw2 = report({"mw2"}, a.results.parent / "phase_n_weights2", a.doc.parent / "phase_n_weights2.md",
                 "Phase N: the HRRR and the NBM weighted per station by their recent error", g_common +
                 "`final8b` is `final6` with the weights of the HRRR and the NBM set per station and per day as the inverse of each "
                 "model's mean squared error over the last 30 days known at the cut-off; no GFS. Compare with `docs/phase_k_nbm_blend.md`.")
    mw3c = report({"mw3c"}, a.results.parent / "phase_n_weights3_cold", a.doc.parent / "phase_n_weights3_cold.md",
                  "Phase N: station weights, with cold-day weights from the cold hours", g_common +
                  "`final8c` is `final8` (HRRR, NBM and GFS weighted per station by their 30-day error) except on days whose temperature "
                  "path dips below 25 F: there the weights come from each model's error on the observed hours below 25 F over the last "
                  "365 days known at the cut-off (at least 48 such hours, else the 30-day weights). Compare with `docs/phase_n_weights3.md`.")
    mw3q = report({"mw3q"}, a.results.parent / "phase_n_weights3_q", a.doc.parent / "phase_n_weights3_q.md",
                  "Phase N: station weights, the GFS left out on cold days", g_common +
                  "`final8q` is `final8` (HRRR, NBM and GFS weighted per station by their 30-day error) except on days whose temperature "
                  "path minimum falls below the tenth percentile of the station's observed daily minima over the last 365 days known at "
                  "the cut-off: there the GFS leaves the mean and the HRRR and the NBM carry it. Compare with `docs/phase_n_weights3.md`.")
    storm = report({"storm"}, a.results.parent / "phase_o_storm", a.doc.parent / "phase_o_storm.md",
                   "Phase O: a storm member", g_common +
                   "`final9` is the phase N recipe with one more ensemble member: a boosting model fitted on the days of the training window "
                   "whose observed minimum is in the coldest decile (at least 40 such days), which answers only on a target day whose forecast "
                   "minimum is at or below that threshold and is left out of the ensemble on every other day; its weight in the ensemble comes "
                   "from its recent error like the others' (the mean of the others' when it has no record). Compare with `docs/phase_n_weights3_q.md`.")
    storm2 = report({"storm2"}, a.results.parent / "phase_o_storm2", a.doc.parent / "phase_o_storm2.md",
                    "Phase O: two storm members", g_common +
                    "`final9b` is `final9` with a second storm member, the additive model fitted on the same cold decile. Compare with `docs/phase_o_storm.md`.")
    band_common = ("The band on the coldest days, where the 90 % interval has covered 77 to 82 % of the hours in the storms. ")
    band_a = report({"band_a"}, a.results.parent / "phase_o_band_a", a.doc.parent / "phase_o_band_a.md",
                    "Phase O: the nominal level halved on cold days", g_common + band_common +
                    "`final10a` reads the band at half the adaptive miscoverage level on the days whose forecast minimum is in the coldest decile "
                    "(a nominal 95 % band on a 90 % target), everything else as the phase N recipe. Compare with `docs/phase_n_weights3_q.md`.")
    band_a2 = report({"band_a2"}, a.results.parent / "phase_o_band_a2", a.doc.parent / "phase_o_band_a2.md",
                     "Phase O: the nominal level quartered on cold days", g_common + band_common +
                     "`final10a2` reads the band at a quarter of the adaptive miscoverage level on the cold-decile days (a nominal 97.5 % band on a "
                     "90 % target). Compare with `docs/phase_o_band_a.md`.")
    band_a2t = report({"band_a2t"}, a.results.parent / "phase_o_band_a2t", a.doc.parent / "phase_o_band_a2t.md",
                      "Phase O: the quartered level and the exponential tail on cold days", g_common + band_common +
                      "`final10a2t` is `final10a2` with the outer quantiles read, on the cold-decile days only, from an exponential fitted to the "
                      "pool errors beyond its 10th and 90th percentiles (as `tail=True` in phase E), so that a level below the smallest error seen "
                      "in the 40 nearest days is still defined. Compare with `docs/phase_o_band_a2.md`.")
    band_b = report({"band_b"}, a.results.parent / "phase_o_band_b", a.doc.parent / "phase_o_band_b.md",
                    "Phase O: a separate adaptive level on cold days", g_common + band_common +
                    "`final10b` tracks one more adaptive level on the cold-decile days alone (step 0.10 instead of 0.02), so that the misses of "
                    "the storms widen the next cold days and not the mild ones. Compare with `docs/phase_n_weights3_q.md`.")
    band_s = report({"band_s"}, a.results.parent / "phase_o_band_s", a.doc.parent / "phase_o_band_s.md",
                    "Phase O: the NBM spread as the width factor", g_common + band_common +
                    "`final10s` multiplies the half-widths of the band by the ratio of the day's NBM temperature spread (the blend's standard "
                    "deviation, mean over the day and the stations) to the median spread of the pool days, clipped to 0.7 to 2. "
                    "Compare with `docs/phase_n_weights3_q.md`.")
    band_as = report({"band_as"}, a.results.parent / "phase_o_band_as", a.doc.parent / "phase_o_band_as.md",
                     "Phase O: the halved level on cold days and the NBM spread factor", g_common + band_common +
                     "`final10as` combines `final10a` and `final10s`. Compare with `docs/phase_o_band_a.md` and `docs/phase_o_band_s.md`.")
    band_ast = report({"band_ast"}, a.results.parent / "phase_o_band_ast", a.doc.parent / "phase_o_band_ast.md",
                      "Phase O: the NBM spread factor on top of the quartered level and the cold tail", g_common + band_common +
                      "`final10ast` combines `final10a2t` (the level quartered and the exponential tail on cold days) with the NBM spread as the "
                      "width factor. Compare with `docs/phase_o_band_a2t.md` and `docs/phase_o_band_s.md`.")
    frozen10 = report({"frozen10"}, a.results.parent / "frozen10_2023_2025", a.doc.parent / "phase_o_frozen_band.md",
                      "The band after phase O on 2023 to 2025, under protocol v2",
                      "Development BAs: " + common +
                      "The phase N recipe with the phase O band (`final10a2t`: the adaptive level quartered and the exponential tail on the "
                      "cold-decile days) on 2023 to 2025 under protocol v2; the point forecast is that of `docs/frozen_evaluation_v6.md`, only "
                      "the band changes. Compare with `docs/frozen_evaluation_v6.md` (same days) and read the difference as an estimate.")
    frozen8 = report({"frozen8"}, a.results.parent / "frozen8_2023_2025", a.doc.parent / "frozen_evaluation_v6.md",
                     "Sixth look at 2023 to 2025: the recipe after phase N, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase N (`final8q`: HRRR, NBM and GFS weighted per station by their recent error, the GFS left out on "
                     "days below the station's cold decile) on 2023 to 2025 under protocol v2. A sixth look at these years: compare with "
                     "`docs/frozen_evaluation_v5.md` (same days, same rules) and read the difference as an estimate.")
    frozen7 = report({"frozen7"}, a.results.parent / "frozen7_2023_2025", a.doc.parent / "frozen_evaluation_v6_equal.md",
                     "Sixth look at 2023 to 2025: the recipe after phase M, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase M (`final7`: three weather models averaged) on 2023 to 2025 under protocol v2. A sixth look at "
                     "these years: compare with `docs/frozen_evaluation_v5.md` (same days, same rules) and read the difference as an estimate.")
    frozen6 = report({"frozen6"}, a.results.parent / "frozen6_2023_2025", a.doc.parent / "frozen_evaluation_v5.md",
                     "Fifth look at 2023 to 2025: the recipe after phase K, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase K (`final6`) on 2023 to 2025 under protocol v2, with the observed-temperature supplement. "
                     "A fifth look at these years: compare with `docs/frozen_evaluation_v4.md` (same days, same rules) and read the "
                     "difference as an estimate.")
    frozen5 = report({"frozen5"}, a.results.parent / "frozen5_2023_2025", a.doc.parent / "frozen_evaluation_v4.md",
                     "Fourth look at 2023 to 2025: the recipe after phase I, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase I (`final5`: the phase H recipe with the wind block in the boosting, the peak read at the "
                     "70th percentile on the coldest decile of days and 23 quantiles) on 2023 to 2025 under protocol v2, with the "
                     "observed-temperature supplement. A fourth look at these years: compare with `docs/frozen_evaluation_v3.md` "
                     "(same days, same rules) and read the difference as an estimate.")
    humid_b = report({"humid_b"}, a.results.parent / "phase_h_dewpoint_bias", a.doc.parent / "phase_h_dewpoint_bias.md",
                     "Phase H: the dew point path corrected by its own recent bias", g_common +
                     "`final4b` is `final4` with the HRRR dew point of every station moved by the median of the forecast's own error at "
                     "that local hour over the last 30 known days (forecast as seen at the cut-off against the airport observation), the "
                     "temperature correction of phase G applied to the dew point. Compare with `docs/phase_h_humidity_only.md` (same days).")
    humid_p = report({"humid_p"}, a.results.parent / "phase_h_humidity_boosting", a.doc.parent / "phase_h_humidity_boosting.md",
                     "Phase H: humidity in the boosting only", g_common +
                     "`final3_hp` is the phase G recipe with the humidity block in the boosting and the additive model unchanged. "
                     "Compare with `docs/phase_h_humidity_only.md`, `docs/phase_h_humidity_linear.md` and `docs/phase_g_final.md` (same days).")
    frozen4 = report({"frozen4"}, a.results.parent / "frozen4_2023_2025", a.doc.parent / "frozen_evaluation_v3.md",
                     "Third look at 2023 to 2025: the recipe after phase H, under protocol v2",
                     "Development BAs: " + common +
                     "The recipe after phase H (`final4`: the phase G recipe with the humidity block in the boosting and the apparent "
                     "temperature in the additive model) on 2023 to 2025 under protocol v2, with the observed-temperature supplement. "
                     "A third look at these years: compare with `docs/frozen_evaluation_v2.md` (same days, same rules) and read the "
                     "difference as an estimate.")
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
    if all(t is None for t in (main, sky, pv, iv2, pv2, final, iv3, peak, irr, final2, frozen, proto, feat, hp, ens2, final3, frozen3, tbias, final3b, frozen2, humid, humid_h, humid_l, humid_p, frozen4, humid_b, events, final5, frozen5, extremes, extremes2, nbm_blend, nbm_replace, nbm_cold, frozen6, blendw, blendc, blendwc, nbmfld, nbmirr, gfs3, frozen7, mw3, mw2, mw3c, mw3q, frozen8, storm, storm2, band_a, band_a2, band_a2t, band_b, band_s, band_as, band_ast, frozen10)):
        log("no rows to report")
        return 1
    if waiting:
        log(f"still waiting for station forecasts: {waiting}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
