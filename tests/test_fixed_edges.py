"""The 5th and 95th percentiles issued at their fixed levels next to the band (docs/methods.md 8v): when the extra levels
include 0.05 and 0.95, the CRPS and the pinball losses score them, and coverage and Winkler keep the adaptive band."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.evaluate import score_day
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from ba_load_forecast.metrics import crps_from_quantiles, quantile_metrics
from tests.test_direct_models import perfect_weather_info
from tests.test_ensemble_quantiles import Const, flat_history

LEVELS = (0.02, 0.05, 0.10, 0.90, 0.95, 0.98)


def run(extra_levels):
    load, temp = flat_history(level=1000.0, days=160)
    rng = np.random.default_rng(3)
    noise = np.where(load.index < pd.Timestamp("2024-03-15"), 0.03, 0.01)       # calmer days later: the band over-covers
    load = load * (1.0 + rng.normal(0.0, 1.0, len(load)) * noise)                # and the adaptive level drifts above 0.10
    ai = AdaptiveIntervals(Const("b", 1000.0), window_days=60, min_days=10, extra_levels=extra_levels, name="band")
    hourly, rows, info = [], None, None
    for k in range(100):
        d = date(2024, 2, 1) + timedelta(days=k)
        info = perfect_weather_info(load, temp, d)
        info.actual = load.reindex(info.timestamps).to_numpy()
        hourly = []
        rows = score_day(info, [ai], hourly)
    return ai, rows, hourly, info


def test_fixed_edges_are_issued_and_scored_in_place_of_the_band_edges():
    ai, rows, hourly, info = run(LEVELS)
    w = {r["model"]: np.array([r[f"h{h:02d}"] for h in range(24)]) for r in hourly}
    assert {"band_q05", "band_q95", "band_q05f", "band_q95f"} <= set(w)
    assert ai.alphas[None] > 0.12                                                 # the case of the fix: the band is not 5-95
    assert (w["band_q95"] < w["band_q95f"]).mean() > 0.5
    row = next(r for r in rows if r["model"] == "band")
    actual = info.actual
    q05f, q95f, med = w["band_q05f"], w["band_q95f"], w["band"]
    fixed = quantile_metrics(np.vstack([q05f, med, q95f]), actual)
    assert abs(row["pinball_05"] - fixed["pinball_05"]) < 1e-9
    assert abs(row["pinball_95"] - fixed["pinball_95"]) < 1e-9
    band = quantile_metrics(np.vstack([w["band_q05"], med, w["band_q95"]]), actual)
    assert abs(row["coverage_90"] - band["coverage_90"]) < 1e-9                   # coverage and Winkler: the band
    assert abs(row["winkler_90"] - band["winkler_90"]) < 1e-9
    qx = np.vstack([w[f"band_q{round(lv * 100):02d}{'f' if lv in (0.05, 0.95) else ''}"] for lv in LEVELS])
    expected = crps_from_quantiles(np.vstack([qx[:3], med, qx[3:]]), np.array([0.02, 0.05, 0.10, 0.5, 0.90, 0.95, 0.98]), actual)
    assert abs(row["crps"] - expected) < 1e-9
    assert (np.diff(qx, axis=0) >= -1e-9).all()                                   # the fixed edges sit between their neighbours


def test_without_fixed_edges_the_band_edges_stand_in_as_before():
    _, rows, hourly, info = run((0.02, 0.10, 0.90, 0.98))
    w = {r["model"]: np.array([r[f"h{h:02d}"] for h in range(24)]) for r in hourly}
    assert "band_q05f" not in w
    row = next(r for r in rows if r["model"] == "band")
    band = quantile_metrics(np.vstack([w["band_q05"], w["band"], w["band_q95"]]), info.actual)
    assert abs(row["pinball_05"] - band["pinball_05"]) < 1e-9
    qx = np.vstack([w["band_q02"], w["band_q05"], w["band_q10"], w["band"], w["band_q90"], w["band_q95"], w["band_q98"]])
    expected = crps_from_quantiles(qx, np.array([0.02, 0.05, 0.10, 0.5, 0.90, 0.95, 0.98]), info.actual)
    assert abs(row["crps"] - expected) < 1e-9
