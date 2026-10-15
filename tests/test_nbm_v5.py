"""NBM version 5.0: the newest tree is tried first and the spread of the temperature is read under its new name."""
from datetime import date

from ba_load_forecast import nbm


def test_version_5_is_tried_first_with_the_renamed_spread(monkeypatch):
    asked = []

    def fake_get(url, timeout=120):
        asked.append(url)
        return b"<Key>x</Key>" if "blendv5.0" in url else b""

    monkeypatch.setattr(nbm, "_get", fake_get)
    assert nbm.list_run(date(2026, 6, 15), 12, "tempstddev")[0] == "5.0"
    assert "blendv5.0/conus/2026/06/15/1200/temppstddev/" in asked[0]
    asked.clear()
    assert nbm.list_run(date(2026, 6, 15), 12, "temp")[0] == "5.0"
    assert "/1200/temp/" in asked[0]


def test_older_trees_keep_their_names():
    assert nbm.element_in("tempstddev", "4.3") == "tempstddev"
    assert nbm.element_in("temp", "5.0") == "temp"
