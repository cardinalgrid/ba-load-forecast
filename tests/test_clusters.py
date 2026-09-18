import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.clusters import LabelClassifier, crosstab, daily_shapes, fit_clusters

H = np.arange(24)
FAMILIES = [
    1.0 + 0.30 * np.sin(2 * np.pi * (H - 6) / 24),      # afternoon peak
    1.0 + 0.30 * np.cos(2 * np.pi * (H - 7) / 24),      # morning peak
    1.0 + 0.10 * np.sin(2 * np.pi * (H - 9) / 24),      # flat weekend
]


def synthetic_series(days=180, seed=0):
    rng = np.random.default_rng(seed)
    hours = pd.date_range("2024-01-01", periods=24 * days, freq="h")
    family = np.array([k % 3 for k in range(days)])
    v = np.concatenate([FAMILIES[f] * (1000 + 20 * k) + rng.normal(0, 8, 24) for k, f in enumerate(family)])
    return pd.Series(v, index=hours), family


def test_daily_shapes_drops_incomplete_days():
    s, _ = synthetic_series(days=5)
    s = s.drop(s.index[30])                       # day 1 loses an hour
    days, shapes = daily_shapes(s)
    assert len(days) == 4
    assert pd.Timestamp("2024-01-02") not in days
    np.testing.assert_allclose(shapes.mean(axis=1), 1.0)
    assert daily_shapes(pd.Series(dtype=float))[1].shape == (0, 24)


def test_fit_clusters_recovers_three_families_and_flags_a_truncated_day():
    s, family = synthetic_series()
    _, shapes = daily_shapes(s)
    m = fit_clusters(shapes, k_range=range(2, 7))
    assert m.k == 3
    assert m.silhouette > 0.5
    labels = m.label(shapes)
    purity = pd.crosstab(labels, family).max(axis=1).sum() / len(labels)
    assert purity == 1.0
    truncated = FAMILIES[0].copy()
    truncated[16:22] *= 0.6                        # six hours of shed load in the evening peak
    truncated = truncated / truncated.mean()
    assert m.distance(truncated)[0] > m.distance(shapes).max()
    with pytest.raises(ValueError, match="too few"):
        fit_clusters(shapes[:5])


def test_crosstab_and_label_classifier():
    labels = np.array([0, 0, 1, 1, 2, 2, 0])
    day_type = np.array([0, 0, 0, 0, 2, 2, 1])
    regime = np.array([1, 1, 0, 0, 1, 1, 1])
    ct = crosstab(labels, day_type, regime)
    assert ct.loc[0, (0, 1)] == 2
    assert ct.loc[1, (0, 0)] == 2
    clf = LabelClassifier().fit(labels, day_type, regime)
    assert clf.predict(0, 1) == 0
    assert clf.predict(0, 0) == 1
    assert clf.predict(0, 2) == 0            # unseen cell: the day type's mode
    assert clf.predict(1, None) == 0
    assert clf.predict(5, 0) == 0            # unseen type: the overall mode
