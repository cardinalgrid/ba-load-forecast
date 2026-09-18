from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.evaluate import evaluate
from ba_load_forecast.information_set import gross_guard, plausible
from tests.conftest import make_info


class Copy:
    name = "copy"

    def predict(self, info):
        return np.full(24, 1000.0)


def test_gross_guard_removes_only_what_no_load_could_be():
    hours = pd.date_range("2024-01-01", periods=24 * 40, freq="h")
    s = pd.Series(1000.0 + 100 * np.sin(np.arange(len(hours)) / 3), index=hours)
    s.iloc[24 * 30] = 2147480000.0       # an overflow
    s.iloc[24 * 31] = 3.0                # a dropped digit
    s.iloc[24 * 32] = 1700.0             # a 70 % jump: not gross, kept
    g = gross_guard(s)
    assert np.isnan(g.iloc[24 * 30])
    assert np.isnan(g.iloc[24 * 31])
    assert g.iloc[24 * 32] == 1700.0
    assert g.isna().sum() == 2
    assert gross_guard(pd.Series(dtype=float)).empty


def test_plausible():
    a = np.full(24, 1000.0)
    assert plausible(a, 1000.0)
    a[5] = 2147480000.0
    assert not plausible(a, 1000.0)
    a[5] = np.nan
    assert plausible(a, 1000.0)
    assert plausible(a, np.nan)


class OneDayLoader:
    def __init__(self, info):
        self.info = info

    def information_set(self, ba, day):
        return self.info


def test_a_gross_fault_in_the_outcome_scores_nobody():
    hours = pd.date_range("2024-01-01", periods=24 * 20, freq="h")
    load = pd.Series(1000.0, index=hours)
    temp = pd.Series(50.0, index=hours)
    actual = np.full(24, 1000.0)
    actual[7] = 2147480000.0
    info = make_info(date(2024, 1, 19), load, temp, np.full(24, 50.0), ba_forecast=np.full(24, 1010.0), actual=actual)
    info.actual_plausible = plausible(actual, 1000.0)
    rows = evaluate(OneDayLoader(info), [Copy()], ["PJM"], date(2024, 1, 19), date(2024, 1, 19))
    assert rows["skipped"].all()
    assert (rows["error"] == "implausible actual").all()
