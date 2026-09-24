"""Where the data lives.

By default the inputs sit next to the repository (``data/`` inside it, the tidy EIA-930 files in the sibling
``ba-forecast-scorecard`` checkout, the ISD-Lite cache in the sibling ``notes`` checkout). When the environment
variable ``BA_LOAD_FORECAST_DATA`` names a folder, everything is read from there instead, in one flat layout:

    <folder>/tidy/        EIA-930 tidy parquet files (the scorecard's ``data/tidy``)
    <folder>/isd/         ISD-Lite station-year files and ``isd-history.csv``
    <folder>/hrrr/, hrrr_multi/, hrrr_fpl/, cloud/, dswrf/, dewpoint/, wind/, asos/, ghcnh/, pv/   as under ``data/``

A local folder outside a synchronised drive keeps long runs independent of the drive being mounted.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_env = os.environ.get("BA_LOAD_FORECAST_DATA")
DATA = Path(_env) if _env else ROOT / "data"
TIDY = DATA / "tidy" if _env else ROOT.parent / "ba-forecast-scorecard" / "data" / "tidy"
ISD = DATA / "isd" if _env else ROOT.parent / "notes" / "03-daily-load-profiles" / "data" / "isd"

__all__ = ["DATA", "ISD", "ROOT", "TIDY"]
