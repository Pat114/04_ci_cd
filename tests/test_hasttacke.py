from src.hasttacke import välj_täcke
import pytest


@pytest.mark.unit2
def test_vintertäcke():
    assert välj_täcke(2, False) == "vintertäcke"


@pytest.mark.unit2
def test_regntäcke():
    assert välj_täcke(10, True) == "regntäcke"


@pytest.mark.unit2
def test_inget_täcke():
    assert välj_täcke(15, False) == "inget täcke"
