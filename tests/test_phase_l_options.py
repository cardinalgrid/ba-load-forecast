"""Phase L options: the weighted blend of two forecast paths and the cold-hour bias of the second weather model."""
from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.cutoff import blend_paths, mean_paths
from ba_load_forecast.information_set import apply_cold_bias, cold_bias_from_table


def test_weighted_blend():
    a = np.array([10.0, 20.0, 30.0])
    b = np.array([20.0, np.nan, 40.0])
    assert np.allclose(blend_paths(a, b, 0.7), [17.0, 20.0, 37.0])
    assert np.allclose(blend_paths(a, b), [15.0, 20.0, 35.0])              # the default is the plain mean
    assert np.allclose(blend_paths(a, b, 1.0), [20.0, 20.0, 40.0])


def test_cold_bias_uses_only_cold_hours_known_at_the_cutoff():
    idx = pd.date_range("2024-01-01", periods=24 * 400, freq="h")
    k = np.arange(len(idx))
    seen = np.where(k % 50 < 5, 10.0, 60.0)                                  # one cold spell of 5 hours every 50 hours
    e = np.where(k % 50 < 5, -2.0, 0.5)                                       # the forecast too warm by 2 F when cold
    t = pd.DataFrame({"seen": seen, "e": e}, index=idx)
    assert cold_bias_from_table(t, date(2025, 2, 1), 365, 25.0) == -2.0
    assert cold_bias_from_table(t, date(2024, 1, 5), 365, 25.0) == 0.0        # fewer than 48 cold hours known yet
    assert cold_bias_from_table(t, date(2025, 2, 1), 365, 5.0) == 0.0         # nothing forecast below 5 F
    assert cold_bias_from_table(pd.DataFrame(columns=["seen", "e"]), date(2025, 2, 1), 365, 25.0) == 0.0
    late = t.copy()
    late.loc[late.index >= pd.Timestamp("2025-01-31"), "e"] = 99.0            # errors after the cut-off must not count
    assert cold_bias_from_table(late, date(2025, 2, 1), 365, 25.0) == -2.0


def test_apply_cold_bias_touches_cold_hours_only():
    out = apply_cold_bias(np.array([10.0, 30.0, np.nan, 24.9]), -2.0, 25.0)
    assert np.allclose(out[[0, 1, 3]], [8.0, 30.0, 22.9])
    assert np.isnan(out[2])


def test_mean_of_the_models_that_have_the_hour():
    a = np.array([10.0, 20.0, np.nan, np.nan])
    b = np.array([20.0, np.nan, np.nan, 5.0])
    c = np.array([30.0, 26.0, np.nan, np.nan])
    out = mean_paths([a, b, c])
    assert np.allclose(out[[0, 1, 3]], [20.0, 23.0, 5.0])
    assert np.isnan(out[2])

