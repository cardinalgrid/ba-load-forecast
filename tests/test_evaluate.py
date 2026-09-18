from datetime import date

import numpy as np
import pandas as pd

from ba_load_forecast.evaluate import BA_MODEL, evaluate
from ba_load_forecast.forecasters.base import Forecaster, ForecastError, blind_copy
from ba_load_forecast.information_set import Loader


class CopyDF:
    name = "copy_df"

    def predict(self, info):
        return info.ba_forecast


class Cheat:
    """Uses the load that occurred: must never be able to."""

    name = "cheat"

    def predict(self, info):
        return info.actual


class Refuses:
    name = "refuses"

    def predict(self, info):
        raise ForecastError("no history")


def test_blind_copy_hides_the_outcome(public_data):
    tidy, isd, hrrr = public_data
    info = Loader(tidy, isd, hrrr, history_days=30).information_set("PJM", date(2024, 1, 16))
    b = blind_copy(info)
    assert np.isnan(b.actual).all()
    assert np.isnan(b.temp_observed_f).all()
    assert not np.isnan(info.actual[0])
    assert b.load_history is info.load_history
    assert b.temp_forecast_f is info.temp_forecast_f
    assert isinstance(CopyDF(), Forecaster)


def test_evaluate_scores_like_the_ba_and_catches_cheats(public_data):
    tidy, isd, hrrr = public_data
    loader = Loader(tidy, isd, hrrr, history_days=30)
    logs = []
    rows = evaluate(loader, [CopyDF(), Cheat(), Refuses()], ["PJM"], date(2024, 1, 15), date(2024, 1, 17), log=logs.append)
    assert len(rows) == 3 * 4
    assert set(rows["model"]) == {"copy_df", "cheat", "refuses", BA_MODEL}
    df = rows[rows["model"] == BA_MODEL].set_index("day")
    cp = rows[rows["model"] == "copy_df"].set_index("day")
    pd.testing.assert_frame_equal(df[["mape", "peak_err_pct", "peak_hour_err"]], cp[["mape", "peak_err_pct", "peak_hour_err"]])
    assert df.loc[date(2024, 1, 16), "skipped"]          # the fixture drops one row: forecast and actual missing
    assert (df.loc[~df["skipped"], "mape"] > 0).all()   # DF is demand + 10 in the fixture
    assert rows[rows["model"] == "cheat"]["skipped"].all()
    ref = rows[rows["model"] == "refuses"]
    assert ref["skipped"].all()
    assert (ref["error"] == "no history").all()
    assert rows.loc[rows["day"] == date(2024, 1, 16), "run_init"].iloc[0] == "2024-01-15T12"
    assert logs == ["PJM: 3 days scored"]
