import numpy as np
import pandas as pd
import pytest

from ba_load_forecast.hrrr_grid import CHUNK, GridPoint, nearest_point, points_from_table, station_grid_points


@pytest.fixture
def small_grid():
    """A 10 x 10 regular grid, 0.03 degrees apart, around (40 N, -75 E)."""
    lat = 40.0 + 0.03 * np.arange(10)[:, None] + np.zeros((1, 10))
    lon = -75.0 + 0.03 * np.arange(10)[None, :] + np.zeros((10, 1))
    return lat, lon


def test_nearest_point_finds_the_closest_cell(small_grid):
    lat, lon = small_grid
    p = nearest_point(40.061, -74.881, lat, lon)
    assert (p.y, p.x) == (2, 4)
    assert p.grid_lat == pytest.approx(40.06)
    assert p.grid_lon == pytest.approx(-74.88)
    assert p.distance_km < 0.2


def test_nearest_point_outside_the_domain_raises(small_grid):
    lat, lon = small_grid
    with pytest.raises(ValueError, match="outside"):
        nearest_point(20.0, -100.0, lat, lon)


def test_chunk_indices():
    p = GridPoint(y=656, x=1527, grid_lat=39.86, grid_lon=-75.22, distance_km=1.1)
    assert (p.chunk_y, p.chunk_x) == (656 // CHUNK, 1527 // CHUNK) == (4, 10)
    assert (p.in_chunk_y, p.in_chunk_x) == (56, 27)
    assert p.chunk_key == "4.10"


def test_station_table_round_trip(small_grid):
    lat, lon = small_grid
    st = pd.DataFrame({"icao": ["KAAA", "KBBB"], "lat": [40.0, 40.27], "lon": [-75.0, -74.73]})
    t = station_grid_points(st, lat, lon)
    assert list(t["icao"]) == ["KAAA", "KBBB"]
    assert list(t["y"]) == [0, 9]
    assert list(t["x"]) == [0, 9]
    pts = points_from_table(t)
    assert pts["KBBB"] == GridPoint(y=9, x=9, grid_lat=40.27, grid_lon=-74.73, distance_km=pts["KBBB"].distance_km)
