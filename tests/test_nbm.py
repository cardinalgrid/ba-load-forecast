"""NBM readers: the grid mapping, the hourly path with its three-hourly tail, the daily products and the cold rule."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from ba_load_forecast.forecasters.base import ForecastError
from ba_load_forecast.forecasters.quantiles import AdaptiveIntervals
from ba_load_forecast.nbm import (
    DAILY_ELEMENTS,
    NX,
    NY,
    cell_of,
    daily_at_cutoff,
    daily_valid,
    lead_of,
    nbm_path,
    station_cells,
)
from tests.test_direct_models import perfect_weather_info
from tests.test_ensemble_quantiles import Const, flat_history


def test_grid_mapping_puts_known_stations_in_the_right_region():
    row, col = cell_of([32.897, 25.795, 47.449], [-97.038, -80.290, -122.309])     # KDFW, KMIA, KSEA
    assert (0 <= row).all() and (row < NY).all() and (0 <= col).all() and (col < NX).all()
    assert col[0] < col[1] and col[2] < col[0]                                     # west to east: Seattle, Dallas, Miami
    assert row[1] > row[0] > row[2]                                                # rows grow southward
    cells = station_cells(pd.DataFrame({"icao": ["KDFW", "XXXX"], "lat": [32.897, 0.0], "lon": [-97.038, 0.0]}))
    assert set(cells) == {"KDFW"}                                                  # the equator point is off the grid


def test_lead_and_daily_valid_times():
    assert lead_of("blendv4.0_conus_temp_2020-12-15T12:00_2020-12-16T12:00.tif") == 24
    assert lead_of("blendv4.0_conus_temp_2020-12-15T12:00_2020-12-17T03:00.tif") == 39
    assert lead_of("not_a_file") is None
    assert daily_valid(date(2020, 12, 15), "mint18p50") == pd.Timestamp("2020-12-16 18:00")
    assert daily_valid(date(2020, 12, 15), "probmaxt18gt090") == pd.Timestamp("2020-12-17 06:00")
    assert len(DAILY_ELEMENTS) == 16


def test_hourly_path_interpolates_the_three_hourly_tail():
    init = pd.Timestamp(2024, 1, 9, 12)
    leads = list(range(1, 37)) + [39, 42, 45]
    rows = pd.DataFrame({"icao": "KDFW", "init_utc": init, "lead_h": leads,
                         "valid_utc": [init + pd.Timedelta(hours=k) for k in leads],
                         "nbm_temp_f": [float(k) for k in leads]})
    path = nbm_path(rows, date(2024, 1, 10), 6.0, (date(2024, 1, 9), 12))
    assert path.shape == (39,)
    assert np.isfinite(path).all()                                                 # 09:00 CST D-1 = lead 3 ... 23:00 CST D = lead 41
    assert np.allclose(np.diff(path), 1.0)                                         # leads 37, 38, 40, 41 filled linearly
    path_far = nbm_path(rows, date(2024, 1, 10), 8.0, (date(2024, 1, 9), 12))      # Pacific: last hour is lead 43, inside 42..45
    assert np.isfinite(path_far).all()


def test_daily_products_and_the_nbm_cold_rule():
    init = pd.Timestamp(2024, 1, 9, 12)
    daily = pd.DataFrame({"icao": "KDFW", "init_utc": [init] * 3, "element": ["mint18p05", "mint18p50", "probmint18lt010"],
                          "valid_utc": pd.Timestamp("2024-01-10 18:00"), "lead_h": 30, "value": [5.0, 12.0, 40.0]})
    d = daily_at_cutoff(daily, (date(2024, 1, 9), 12))
    assert d == {"mint18p05": 5.0, "mint18p50": 12.0, "probmint18lt010": 40.0}
    assert daily_at_cutoff(daily, (date(2024, 1, 8), 12)) == {}
    load, temp = flat_history(level=1000.0, days=400)
    ai = AdaptiveIntervals(Const("b", 1000.0), window_days=200, min_days=10, peak="quantile", peak_quantile=0.60,
                           peak_quantile_cold=0.70, cold_source="mint18p05")
    rng = np.random.default_rng(3)
    day0 = date(2024, 3, 1)
    for k in range(250):
        info = perfect_weather_info(load, temp, day0 + timedelta(days=k))
        centre = 50.0 + 30.0 * np.sin(k / 40.0)
        info.temp_forecast_f = centre + 10.0 * np.sin(np.arange(24) / 24.0 * 2 * np.pi)
        info.temp_forecast_path_f[-24:] = info.temp_forecast_f
        info.nbm_daily = {"mint18p05": centre - 15.0}                              # the NBM tail sits 5 F below the path minimum
        info.actual = 1000.0 * (1.0 + rng.normal(0.0, 0.03, 24))
        try:
            ai.predict_quantiles(info)
        except ForecastError:
            pass
    mild = perfect_weather_info(load, temp, day0 + timedelta(days=260))
    mild.temp_forecast_f = 60.0 + 10.0 * np.sin(np.arange(24) / 24.0 * 2 * np.pi)
    mild.temp_forecast_path_f[-24:] = mild.temp_forecast_f
    mild.nbm_daily = {"mint18p05": 0.0}                                             # a cold tail the path does not show
    assert ai.source_min(mild) == 0.0 and ai.is_cold_day(mild) and ai.peak_level(mild) == 0.70
    mild.nbm_daily = None                                                          # no NBM that day: back to the path minimum
    assert ai.source_min(mild) == 50.0 and not ai.is_cold_day(mild)
