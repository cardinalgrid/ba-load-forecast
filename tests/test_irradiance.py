"""Forecast irradiance in the sky frame and as a linear PV term of the additive model."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.forecasters.additive import AdditiveModel
from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.sky import IRRADIANCE_COLUMNS, PV_COLUMNS, SKY_COLUMNS, sky_frame
from tests.test_pv_terms import info_with_sky, midday_error
from tests.test_recency import world


def test_sky_frame_carries_the_irradiance_and_the_capacity_times_it():
    hours = pd.date_range("2024-06-21 00:00", periods=24, freq="h")
    off = pd.Series(4.0, index=hours)
    pv = pd.Series([1000.0], index=pd.to_datetime(["2024-06-01"]))
    dswrf = pd.Series(np.where((hours.hour >= 6) & (hours.hour <= 18), 500.0, 0.0), index=hours)
    f = sky_frame(hours, off, 42.36, -71.01, None, pv=pv, dswrf=dswrf)
    assert list(f.columns) == SKY_COLUMNS + PV_COLUMNS + IRRADIANCE_COLUMNS
    np.testing.assert_allclose(f["pv_irr"], 1000.0 * dswrf.to_numpy() / 1000.0)
    g = sky_frame(hours, off, 42.36, -71.01, None, dswrf=dswrf)
    assert "dswrf" in g.columns
    assert "pv_irr" not in g.columns                                      # no capacity, no capacity term


def irradiance_world(days=900):
    """The synthetic world minus a solar dent driven by an irradiance series (clear-sky times a daily factor)."""
    load, temp = world(start="2021-01-01", days=days)
    hours = load.index
    off = pd.Series(5.0, index=hours)
    months = pd.date_range("2021-01-01", hours[-1], freq="MS")
    cap = pd.Series(np.linspace(100.0, 400.0, len(months)), index=months)
    base = sky_frame(hours, off, 42.36, -71.01, None, pv=cap)
    rng = np.random.default_rng(1)
    daily = np.repeat(rng.uniform(0.3, 1.0, days), 24)                      # the day's cloudiness
    dswrf = pd.Series(1000.0 * base["sun"].to_numpy() * daily, index=hours)
    sky = sky_frame(hours, off, 42.36, -71.01, None, pv=cap, dswrf=dswrf)
    net = load - 0.8 * sky["pv_irr"].to_numpy()
    return net, temp, sky


def test_irradiance_term_beats_the_clear_sky_term_when_the_dent_follows_the_irradiance():
    load, temp, sky = irradiance_world()
    first = date(2023, 5, 1)
    clear = midday_error(AdditiveModel(train_days=700, val_days=30, pv=True), load, temp, sky, first, 20)
    irr = midday_error(AdditiveModel(train_days=700, val_days=30, pv=True, irradiance=True), load, temp, sky, first, 20)
    assert abs(irr) < abs(clear) + 0.05                                    # never worse
    # the irradiance term explains the day-to-day variation the clear-sky term cannot: a smaller spread of errors
    def spread(model):
        errs = []
        for k in range(20):
            d = date(2023, 5, 1) + pd.Timedelta(days=k)
            info = info_with_sky(load, temp, sky, d.date() if hasattr(d, "date") else d)
            f = model.predict(info)
            actual = load.reindex(info.timestamps).to_numpy()
            errs.append(np.mean((f - actual)[10:15]) / np.mean(actual[10:15]) * 100)
        return float(np.std(errs))
    assert spread(AdditiveModel(train_days=700, val_days=30, pv=True, irradiance=True)) < spread(AdditiveModel(train_days=700, val_days=30, pv=True))


def test_irradiance_term_needs_the_extraction():
    load, temp, sky = irradiance_world(days=400)
    sky = sky.drop(columns=IRRADIANCE_COLUMNS)
    info = info_with_sky(load, temp, sky, date(2022, 1, 20))
    with pytest.raises(ForecastError, match="irradiance=True"):
        AdditiveModel(train_days=300, val_days=30, pv=True, irradiance=True).predict(info)
