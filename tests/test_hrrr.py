from datetime import date, datetime

import fsspec
import numpy as np
import pytest
import zarr
from numcodecs import Blosc

from ba_load_forecast.hrrr import consolidate, extract, kelvin_to_f, load_station, read_run, run_file, run_root
from ba_load_forecast.hrrr_grid import GridPoint

N_LEAD = 48


def cell_value(lead_index: int, y: int, x: int) -> float:
    """An integer kelvin value, exact in float16, that identifies lead and cell."""
    return 200.0 + lead_index + 3 * (y % 7) + 5 * (x % 5)


def make_run(bucket: str, day: date, init_hour: int, n_lead: int = N_LEAD) -> None:
    root = run_root(day, init_hour, bucket)
    a = zarr.open(root, mode="w", shape=(n_lead, 300, 300), chunks=(n_lead, 150, 150), dtype="<f2",
                  fill_value=-10000.0, compressor=Blosc(cname="lz4", clevel=9, shuffle=1))
    lead = np.arange(n_lead)[:, None, None]
    yy = np.arange(300)[None, :, None]
    xx = np.arange(300)[None, None, :]
    a[:] = (200.0 + lead + 3 * (yy % 7) + 5 * (xx % 5)).astype("<f2")


@pytest.fixture
def bucket(tmp_path):
    b = (tmp_path / "hrrrzarr").as_posix()
    make_run(b, date(2024, 1, 16), 12)
    make_run(b, date(2024, 1, 16), 6)
    make_run(b, date(2024, 1, 17), 12)
    return b


POINTS = {
    "KAAA": GridPoint(y=10, x=20, grid_lat=0, grid_lon=0, distance_km=0),      # chunk 0.0
    "KBBB": GridPoint(y=160, x=170, grid_lat=0, grid_lon=0, distance_km=0),    # chunk 1.1
    "KCCC": GridPoint(y=12, x=22, grid_lat=0, grid_lon=0, distance_km=0),      # chunk 0.0 again
}


def test_read_run_returns_the_right_cell_for_every_station(bucket):
    fs = fsspec.filesystem("file")
    out = read_run(fs, date(2024, 1, 16), 12, POINTS, bucket)
    assert set(out) == set(POINTS)
    for icao, p in POINTS.items():
        expected = kelvin_to_f([cell_value(i, p.y, p.x) for i in range(N_LEAD)])
        np.testing.assert_allclose(out[icao], expected, atol=1e-4)


def test_read_run_absent_run_is_none_and_missing_chunk_is_nan(bucket, tmp_path):
    fs = fsspec.filesystem("file")
    assert read_run(fs, date(2024, 1, 18), 12, POINTS, bucket) is None
    (tmp_path / "hrrrzarr" / "sfc" / "20240116" / "20240116_12z_fcst.zarr" / "2m_above_ground" / "TMP"
     / "2m_above_ground" / "TMP" / "0.1.1").unlink()
    out = read_run(fs, date(2024, 1, 16), 12, POINTS, bucket)
    assert np.isnan(out["KBBB"]).all()
    assert not np.isnan(out["KAAA"]).any()


def test_extract_is_resumable_and_consolidates(bucket, tmp_path):
    fs = fsspec.filesystem("file")
    out = tmp_path / "out"
    logs = []
    n = extract(POINTS, date(2024, 1, 16), date(2024, 1, 17), out, init_hours=(12, 6), fs=fs, log=logs.append, bucket=bucket)
    assert n == 4
    assert run_file(out, date(2024, 1, 17), 6).exists()      # absent run leaves an empty marker
    assert any("not in the archive" in m for m in logs)
    assert extract(POINTS, date(2024, 1, 16), date(2024, 1, 17), out, init_hours=(12, 6), fs=fs, log=logs.append, bucket=bucket) == 0
    counts = consolidate(out, log=logs.append)
    assert counts == {"KAAA": 3 * N_LEAD, "KBBB": 3 * N_LEAD, "KCCC": 3 * N_LEAD}
    s = load_station(out, "KAAA")
    assert list(s.columns) == ["icao", "init_utc", "lead_h", "valid_utc", "temp_f"]
    first = s.iloc[0]
    assert first["init_utc"] == datetime(2024, 1, 16, 6)
    assert first["lead_h"] == 1
    assert first["valid_utc"] == datetime(2024, 1, 16, 7)
    assert first["temp_f"] == pytest.approx(kelvin_to_f(cell_value(0, 10, 20)), abs=1e-3)
    assert load_station(out, "KZZZ").empty
