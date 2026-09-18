import numpy as np
import pytest

from ba_load_forecast.metrics import day_metrics


def actual_day():
    """Rising through the day (100 to 123) with the peak at hour 18 (130)."""
    a = 100.0 + np.arange(24, dtype=float)
    a[18] = 130.0
    return a


def test_day_metrics_by_hand():
    a = actual_day()
    f = a.copy()
    f[18] = 130.0 * 0.95                         # 5 % under at the actual peak
    f[20] = 131.0                                # the forecast's own peak is at hour 20
    m = day_metrics(f, a)
    assert m["skipped"] is False
    assert m["peak_err_pct"] == pytest.approx(-5.0)
    assert m["peak_under_pct"] == pytest.approx(-5.0)
    assert m["peak_hour_err"] == 2
    assert m["actual_peak"] == 130.0
    assert m["mape"] == pytest.approx((5.0 + (131.0 - 120.0) / 120.0 * 100) / 24)
    over = a * 1.02
    assert day_metrics(over, a)["peak_under_pct"] == 0.0
    assert day_metrics(over, a)["peak_err_pct"] == pytest.approx(2.0)


def test_day_metrics_skips_bad_days():
    a = actual_day()
    a3 = a.copy()
    a3[[1, 2, 3]] = np.nan
    assert day_metrics(a, a3)["skipped"] is True
    assert day_metrics(a, a3)["n_missing"] == 3
    a2 = a.copy()
    a2[[1, 2]] = np.nan
    assert day_metrics(a, a2)["skipped"] is False
    f = a.copy()
    f[5] = np.nan
    assert day_metrics(f, a)["skipped"] is True
    assert day_metrics(a[:23], a)["skipped"] is True
    assert np.isnan(day_metrics(a[:23], a)["mape"])
