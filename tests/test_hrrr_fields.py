from datetime import date

import fsspec
import numpy as np
import zarr
from numcodecs import Blosc

from ba_load_forecast.hrrr import FIELDS, consolidate, extract, load_station, read_run, run_root
from ba_load_forecast.hrrr_grid import GridPoint

POINTS = {"KAAA": GridPoint(y=10, x=20, grid_lat=0, grid_lon=0, distance_km=0)}


def make_cloud_run(bucket: str, day: date, init_hour: int, n_lead: int = 48) -> None:
    root = run_root(day, init_hour, bucket, FIELDS["cloud_pct"][0])
    a = zarr.open(root, mode="w", shape=(n_lead, 300, 300), chunks=(n_lead, 150, 150), dtype="<f2",
                  fill_value=-10000.0, compressor=Blosc(cname="lz4", clevel=9, shuffle=1))
    a[:] = (np.arange(n_lead)[:, None, None] * 2.0 + np.zeros((1, 300, 300))).astype("<f2")     # 0, 2, 4, ... percent


def test_cloud_cover_is_read_without_conversion_and_extracted_under_its_own_name(tmp_path):
    bucket = (tmp_path / "hrrrzarr").as_posix()
    make_cloud_run(bucket, date(2024, 1, 16), 12)
    fs = fsspec.filesystem("file")
    out = read_run(fs, date(2024, 1, 16), 12, POINTS, bucket, field="cloud_pct")
    np.testing.assert_allclose(out["KAAA"], np.arange(48) * 2.0)
    assert read_run(fs, date(2024, 1, 16), 12, POINTS, bucket) is None          # no temperature array in this run
    dest = tmp_path / "cloud"
    assert extract(POINTS, date(2024, 1, 16), date(2024, 1, 16), dest, init_hours=(12,), fs=fs, bucket=bucket,
                   field="cloud_pct", log=lambda m: None) == 1
    consolidate(dest, log=lambda m: None)
    s = load_station(dest, "KAAA")
    assert list(s.columns) == ["icao", "init_utc", "lead_h", "valid_utc", "cloud_pct"]
    assert s["cloud_pct"].iloc[3] == 6.0
