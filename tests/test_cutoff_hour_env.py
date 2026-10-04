"""The cut-off hour set by BA_LOAD_FORECAST_CUTOFF_HOUR (one process, one cut-off)."""

import json
import os
import subprocess
import sys

import pytest

PROBE = (
    "import json; from datetime import date; from ba_load_forecast import cutoff as c; "
    "print(json.dumps([c.CUTOFF_LOCAL_HOUR, c.PATH_HOURS, str(c.last_load_hour(date(2024, 1, 16))), "
    "str(c.path_timestamps(date(2024, 1, 16))[0]), list(c.run_for_day(date(2024, 1, 16), 5.0, init_hours=(18, 12, 6)))[1], "
    "[str(x) for x in c.run_for_day(date(2024, 1, 16), 5.0, init_hours=(0, 18, 12, 6))]]))"
)


def probe(hour: str | None):
    env = dict(os.environ)
    env.pop("BA_LOAD_FORECAST_CUTOFF_HOUR", None)
    if hour is not None:
        env["BA_LOAD_FORECAST_CUTOFF_HOUR"] = hour
    out = subprocess.run([sys.executable, "-c", PROBE], capture_output=True, text=True, env=env, check=False)
    return out


def test_default_is_9am():
    out = probe(None)
    assert json.loads(out.stdout) == [9, 39, "2024-01-15 08:00:00", "2024-01-15 09:00:00", 12, ["2024-01-15", "12"]]


def test_a_later_cutoff_moves_everything_together():
    out = probe("21")
    hour, path_hours, last_load, path_start, run_hour, with_00z = json.loads(out.stdout)
    assert (hour, path_hours, last_load, path_start) == (21, 27, "2024-01-15 20:00:00", "2024-01-15 21:00:00")
    assert run_hour == 18          # 21:00 EST = 02 UTC: the 18 UTC run (+2 h) qualifies when it is among the extracted runs
    assert with_00z == ["2024-01-16", "0"]   # with 00 UTC extracted, the run of day D itself (00 + 2 h = 02 UTC) is the latest


@pytest.mark.parametrize("bad", ["0", "24"])
def test_out_of_range_is_refused(bad):
    out = probe(bad)
    assert out.returncode != 0
    assert "BA_LOAD_FORECAST_CUTOFF_HOUR" in out.stderr
