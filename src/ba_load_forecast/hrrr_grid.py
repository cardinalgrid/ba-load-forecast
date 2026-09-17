"""The HRRR grid: the nearest grid cell to each station, and the Zarr chunk that holds it.

The public archive (``s3://hrrrzarr``, AWS Open Data) stores every forecast field as a Zarr array of
shape ``(lead, y, x)`` on the 3 km Lambert conformal grid (1059 x 1799 cells), in chunks of
``150 x 150`` cells that hold every lead at once. Reading one station therefore means reading the one
chunk that contains its nearest cell; stations that share a chunk share the read. The latitude and
longitude of every cell come from ``grid/HRRR_chunk_index.zarr`` in the same bucket and are cached
locally as a compressed ``.npz``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

BUCKET = "hrrrzarr"
INDEX_PATH = f"{BUCKET}/grid/HRRR_chunk_index.zarr"
CHUNK = 150
EARTH_RADIUS_KM = 6371.0


@dataclass(frozen=True)
class GridPoint:
    """One HRRR cell: its indices on the full grid, its coordinates and its distance to the target."""

    y: int
    x: int
    grid_lat: float
    grid_lon: float
    distance_km: float

    @property
    def chunk_y(self) -> int:
        return self.y // CHUNK

    @property
    def chunk_x(self) -> int:
        return self.x // CHUNK

    @property
    def in_chunk_y(self) -> int:
        return self.y % CHUNK

    @property
    def in_chunk_x(self) -> int:
        return self.x % CHUNK

    @property
    def chunk_key(self) -> str:
        """The chunk name inside the Zarr array, without the leading lead index (``"4.10"``)."""
        return f"{self.chunk_y}.{self.chunk_x}"


def haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance in kilometres; accepts arrays."""
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = np.sin((p2 - p1) / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2
    return 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(a))


def load_grid(cache: Path, fs=None) -> tuple[np.ndarray, np.ndarray]:
    """Latitude and longitude (degrees, longitude in -180..180) of every cell, both ``(1059, 1799)``.

    Read from the local ``.npz`` cache when it exists, otherwise from the public index and cached.
    """
    cache = Path(cache)
    if cache.exists():
        z = np.load(cache)
        return z["lat"], z["lon"]
    import s3fs
    import zarr

    fs = fs or s3fs.S3FileSystem(anon=True)
    g = zarr.open(s3fs.S3Map(INDEX_PATH, s3=fs), mode="r")
    lat = np.asarray(g["latitude"][:], dtype=float)
    lon = np.asarray(g["longitude"][:], dtype=float)
    lon = np.where(lon > 180.0, lon - 360.0, lon)
    cache.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(cache, lat=lat, lon=lon)
    return lat, lon


def nearest_point(lat: float, lon: float, grid_lat: np.ndarray, grid_lon: np.ndarray, box_deg: float = 0.5) -> GridPoint:
    """The grid cell closest to ``(lat, lon)`` by great-circle distance.

    Only cells within ``box_deg`` degrees in latitude and longitude are compared, which is enough for a
    3 km grid; a target with no cell in that box is outside the HRRR domain.
    """
    box = (np.abs(grid_lat - lat) <= box_deg) & (np.abs(grid_lon - lon) <= box_deg)
    ys, xs = np.nonzero(box)
    if len(ys) == 0:
        raise ValueError(f"({lat}, {lon}) is outside the HRRR domain")
    d = haversine_km(lat, lon, grid_lat[ys, xs], grid_lon[ys, xs])
    k = int(np.argmin(d))
    y, x = int(ys[k]), int(xs[k])
    return GridPoint(y=y, x=x, grid_lat=float(grid_lat[y, x]), grid_lon=float(grid_lon[y, x]), distance_km=float(d[k]))


def station_grid_points(stations, grid_lat: np.ndarray, grid_lon: np.ndarray):
    """One row per station (``icao, lat, lon`` in ``stations``) with its nearest cell and chunk.

    Returns a pandas DataFrame with ``icao, lat, lon, y, x, chunk_y, chunk_x, grid_lat, grid_lon, distance_km``.
    """
    rows = []
    for r in stations.itertuples(index=False):
        p = nearest_point(float(r.lat), float(r.lon), grid_lat, grid_lon)
        rows.append({"icao": r.icao, "lat": float(r.lat), "lon": float(r.lon), "y": p.y, "x": p.x,
                     "chunk_y": p.chunk_y, "chunk_x": p.chunk_x, "grid_lat": p.grid_lat, "grid_lon": p.grid_lon,
                     "distance_km": p.distance_km})
    return pd.DataFrame(rows)


def points_from_table(table) -> dict[str, GridPoint]:
    """``{icao: GridPoint}`` from the DataFrame produced by ``station_grid_points`` (or read back from CSV)."""
    return {r.icao: GridPoint(y=int(r.y), x=int(r.x), grid_lat=float(r.grid_lat), grid_lon=float(r.grid_lon),
                              distance_km=float(r.distance_km)) for r in table.itertuples(index=False)}
