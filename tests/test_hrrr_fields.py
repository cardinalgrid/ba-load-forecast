"""The HRRR field table: conversions and the two-variable wind field."""
import numpy as np

from ba_load_forecast.hrrr import FIELDS, kelvin_to_f, wind_speed_ms


def test_conversions():
    assert kelvin_to_f(273.15) == 32.0
    np.testing.assert_allclose(wind_speed_ms([3.0, 0.0], [4.0, 2.0]), [5.0, 2.0])


def test_field_table_has_the_new_fields_with_their_archive_paths():
    assert FIELDS["dewpoint_f"][0] == "2m_above_ground/DPT"
    assert FIELDS["wind_ms"][0] == ("10m_above_ground/UGRD", "10m_above_ground/VGRD")
    assert FIELDS["wind_ms"][1] is wind_speed_ms
