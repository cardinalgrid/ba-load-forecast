"""Phase O options: the storm member, fitted on the coldest decile of days and answering on such days only."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.features import cold_only_weights, cold_threshold
from ba_load_forecast.forecasters.base import Cached, ForecastError
from ba_load_forecast.forecasters.boosting import Boosting
from ba_load_forecast.forecasters.ensemble import Ensemble
from tests.test_direct_models import perfect_weather_info
from tests.test_recency import world


def test_cold_only_weights_mark_the_cold_decile():
    idx = pd.date_range("2024-01-01", periods=24 * 100, freq="h")
    temp = pd.Series(50.0 + 20.0 * np.sin(np.arange(len(idx)) / (24 * 100) * 2 * np.pi), index=idx)
    temp.iloc[24 * 10: 24 * 11] = 0.0                                          # one day far below every other minimum
    w, threshold = cold_only_weights(idx, temp, 0.10)
    assert w.shape == (len(idx),)
    assert set(np.unique(w)) <= {0.0, 1.0}
    assert (w[24 * 10: 24 * 11] == 1.0).all()
    assert 0.09 < w.mean() < 0.12                                              # about a tenth of the days
    assert threshold == cold_threshold(idx, temp, 0.10)
    assert np.isfinite(threshold)


def test_storm_member_answers_on_cold_days_only_and_the_ensemble_leaves_it_out_elsewhere():
    load, temp = world(days=500)
    storm = Boosting(train_days=360, max_iter=30, cold_only=0.10, min_cold_days=20, name="storm")
    cold = perfect_weather_info(load, temp, date(2023, 1, 10))                 # the coldest part of the synthetic year
    f = storm.predict(cold)
    assert f.shape == (24,)
    assert np.isfinite(f).all()
    assert np.isfinite(storm.cold_threshold_f)
    mild = perfect_weather_info(load, temp, date(2023, 4, 20))
    with pytest.raises(ForecastError):
        storm.predict(mild)
    plain = Cached(Boosting(train_days=360, max_iter=30, name="plain"))
    ens = Ensemble([plain, Cached(storm)], weighting="recent")
    assert np.allclose(ens.predict(mild), plain.predict(mild))                 # the storm member is out on a mild day
    assert set(ens.last_weights) == {"plain"}
    both = ens.predict(cold)
    assert np.isfinite(both).all()
    assert set(ens.last_weights) == {"plain", "storm"}
