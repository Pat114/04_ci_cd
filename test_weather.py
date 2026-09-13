from src.weather import vädertyp
import pytest

@pytest.mark.unit2
def test_kallt_väder():
    assert vädertyp(2, False) == "kallt"

@pytest.mark.unit2
def test_regn():
    assert vädertyp(10, True) == "regn"
