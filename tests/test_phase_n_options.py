"""Phase N options: the weather models weighted per station by their recent error."""
from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.cutoff import mean_paths, weighted_paths
from ba_load_forecast.information_set import model_weights


def test_weighted_paths_renormalises_over_the_models_that_have_the_hour():
    a = np.array([10.0, 20.0, np.nan, np.nan])
    b = np.array([20.0, np.nan, np.nan, 5.0])
    c = np.array([30.0, 26.0, np.nan, np.nan])
    out = weighted_paths([a, b, c], [0.5, 0.25, 0.25])
    assert np.allclose(out[[0, 1, 3]], [17.5, 22.0, 5.0])                  # hour 1: (0.5*20 + 0.25*26) / 0.75
    assert np.isnan(out[2])
    assert np.allclose(weighted_paths([a, b, c], [1, 1, 1])[[0, 1, 3]], mean_paths([a, b, c])[[0, 1, 3]])


def test_model_weights_are_inverse_mse_on_the_common_known_hours():
    idx = pd.date_range("2024-01-01", periods=24 * 60, freq="h")
    rng = np.random.default_rng(0)
    errors = {
        "hrrr": pd.Series(rng.normal(0.0, 2.0, len(idx)), index=idx),
        "nbm": pd.Series(rng.normal(0.0, 1.0, len(idx)), index=idx),
    }
    w = model_weights(errors, date(2024, 3, 1), 30)
    assert set(w) == {"hrrr", "nbm"}
    assert abs(sum(w.values()) - 1.0) < 1e-9
    assert 0.75 < w["nbm"] < 0.85                                            # MSE 1 against 4: weight about 0.8
    late = {k: v.copy() for k, v in errors.items()}
    late["nbm"].loc[late["nbm"].index >= pd.Timestamp("2024-02-29 09:00")] = 50.0   # after the cut-off (08:00 of D-1 is the last known hour): must not count
    assert abs(model_weights(late, date(2024, 3, 1), 30)["nbm"] - w["nbm"]) < 1e-9
    assert model_weights(errors, date(2024, 1, 5), 30) is None               # fewer than 240 known hours
    assert model_weights({"hrrr": errors["hrrr"]}, date(2024, 3, 1), 30) is None
    partial = {k: v.copy() for k, v in errors.items()}
    partial["nbm"] = partial["nbm"].iloc[::2]                                # only the common hours count
    w2 = model_weights(partial, date(2024, 3, 1), 30)
    assert w2 is not None
    assert 0.7 < w2["nbm"] < 0.9


def test_model_weights_can_be_restricted_to_the_cold_hours():
    idx = pd.date_range("2024-01-01", periods=24 * 60, freq="h")
    cold = pd.Series(np.arange(len(idx)) % 24 < 6, index=idx)                   # six cold hours a night
    hrrr = pd.Series(np.where(cold, 1.0, 3.0), index=idx)                        # good in the cold, poor otherwise
    nbm = pd.Series(np.where(cold, 3.0, 1.0), index=idx)
    errors = {"hrrr": hrrr, "nbm": nbm}
    plain = model_weights(errors, date(2024, 3, 1), 30)
    assert plain["nbm"] > plain["hrrr"]
    cold_only = model_weights(errors, date(2024, 3, 1), 365, min_hours=48, hours=cold)
    assert cold_only["hrrr"] == 0.9                                              # MSE 1 against 9
    assert model_weights(errors, date(2024, 1, 3), 365, min_hours=48, hours=cold) is None
