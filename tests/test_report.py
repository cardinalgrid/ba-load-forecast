from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.evaluate import BA_MODEL, COLUMNS
from ba_load_forecast.report import complete_cases, dm_test, summarise, write_report


def rows_fixture():
    """Two BAs, 6 days, models A (always better than DF) and B (worse, and missing one day)."""
    rows = []
    for ba, demand in (("PJM", 90000.0), ("TVA", 20000.0)):
        for k in range(6):
            day = date(2021, 2, 13) + timedelta(days=k)      # the first days are inside Uri
            for model, mape, peak in ((BA_MODEL, 3.0, -4.0), ("A", 2.0, -1.0), ("B", 5.0, -8.0)):
                skipped = model == "B" and k == 5
                rows.append({"ba": ba, "day": day, "model": model, "mape": np.nan if skipped else mape + 0.1 * k,
                             "peak_err_pct": np.nan if skipped else peak, "peak_under_pct": np.nan if skipped else min(0.0, peak),
                             "peak_hour_err": 0 if model == "A" else 2, "actual_peak": demand * 1.3, "actual_mean": demand,
                             "n_missing": 0, "skipped": skipped, "day_type": 0, "special_day": None, "run_init": "x", "error": None})
    return pd.DataFrame(rows, columns=COLUMNS)


def test_complete_cases_and_tables():
    rows = rows_fixture()
    cc = complete_cases(rows)
    assert cc.groupby("ba").size().to_dict() == {"PJM": 15, "TVA": 15}      # 5 days x 3 models
    t = summarise(rows)
    by = t["by_model_ba"]
    assert by.loc[("A", "PJM"), "win_mape"] == 1.0
    assert by.loc[("A", "PJM"), "win_peak_under"] == 1.0
    assert by.loc[("B", "TVA"), "win_mape"] == 0.0
    assert np.isnan(by.loc[(BA_MODEL, "PJM"), "win_mape"])
    ov = t["overall"]
    assert list(ov.index) == ["A", BA_MODEL, "B"]
    assert ov.loc["A", "mape"] == pytest.approx(2.2)                          # weights do not matter: same per BA
    assert ov.loc["B", "worst_peak_under_pct"] == -8.0
    assert ov.loc["A", "n_days"] == 10
    ev = t["events"]
    assert set(ev["event"]) == {"uri"}
    assert ev[(ev["model"] == "A") & (ev["ba"] == "PJM")]["n_days"].iloc[0] == 5
    assert t["coverage"].loc["B", "scored_fraction"] == pytest.approx(10 / 12)


def test_dm_test():
    rng = np.random.default_rng(0)
    e = rng.normal(0, 1, 500)
    assert dm_test(e, e) == (0.0, 1.0)
    stat, p = dm_test(e, e * 1.5)
    assert stat < 0
    assert p < 0.01
    assert np.isnan(dm_test([1.0], [2.0])[0])


def test_write_report(tmp_path):
    t = summarise(rows_fixture())
    out = tmp_path / "r.md"
    write_report(t, out, "Phase B", "intro")
    text = out.read_text(encoding="utf-8")
    assert text.startswith("# Phase B")
    assert "| A |" in text
    assert "uri" in text
