import numpy as np
import pandas as pd

from ba_load_forecast.cleaning import sentinel_clean


def year_with_faults(seed=0):
    rng = np.random.default_rng(seed)
    hours = pd.date_range("2023-01-01", periods=24 * 400, freq="h")
    h = np.arange(len(hours))
    doy = (hours.normalize() - hours[0].normalize()).days.to_numpy()
    load = (10_000 + 2_500 * np.sin(2 * np.pi * (h - 6) / 24)) * (1 + 0.15 * np.cos(2 * np.pi * doy / 365.25))
    load = load + rng.normal(0, 60, len(hours))
    truth = pd.Series(load, index=hours)
    faulty = truth.copy()
    spike = pd.Timestamp("2023-09-10 14:00")
    faulty[spike] = truth[spike] * 3.0                                  # a lone spike
    stuck = pd.date_range("2023-10-05 02:00", periods=8, freq="h")
    faulty[stuck] = faulty["2023-10-05 01:00"]                          # a frozen run
    temp = pd.Series(50 - 30 * np.cos(2 * np.pi * doy / 365.25), index=hours)
    return truth, faulty, temp, spike, stuck


def test_sentinel_clean_repairs_the_spike_and_the_frozen_run_and_keeps_the_rest():
    truth, faulty, temp, spike, stuck = year_with_faults()
    warm = faulty.loc[: "2023-06-30 23:00"]
    year = faulty.loc["2023-07-01":]
    cleaned, audit = sentinel_clean(year, temp.reindex(year.index), warm=warm, warm_temp=temp.reindex(warm.index))
    assert cleaned.index.equals(year.index)
    assert abs(cleaned[spike] - truth[spike]) / truth[spike] < 0.15
    assert spike in set(audit["timestamp"])
    assert (np.abs(cleaned[stuck[2:]] - truth[stuck[2:]]) / truth[stuck[2:]] < 0.15).all()
    touched = [*stuck, spike]
    assert (cleaned.drop(index=touched) == year.drop(index=touched)).mean() > 0.98
    empty, audit = sentinel_clean(pd.Series(dtype=float))
    assert empty.empty
    assert audit.empty


def test_loader_cleaning_option_cleans_the_history_but_not_the_outcome(public_data, monkeypatch):
    from datetime import date

    from ba_load_forecast import information_set as mod

    calls = []

    def fake_clean(load, temp=None, warm=None, warm_temp=None):
        calls.append((load.index.min().year, None if warm is None else warm.index.min().year))
        return load + 1.0, pd.DataFrame()

    monkeypatch.setattr(mod, "sentinel_clean", fake_clean)
    tidy, isd, hrrr = public_data
    loader = mod.Loader(tidy, isd, hrrr, history_days=30, cleaning="sentinel")
    info = loader.information_set("PJM", date(2024, 1, 16))
    plain = mod.Loader(tidy, isd, hrrr, history_days=30).information_set("PJM", date(2024, 1, 16))
    np.testing.assert_array_equal(info.load_history.to_numpy(), plain.load_history.to_numpy() + 1.0)
    np.testing.assert_array_equal(info.actual, plain.actual)                  # the outcome is never cleaned
    assert len(calls) == 2                                                    # one call per year of history
    assert calls[0][1] is None                                                # 2023: nothing before it in the fixture
    assert calls[1][1] == 2023                                                # 2024 warmed up on 2023
