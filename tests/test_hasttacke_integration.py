import pytest
from src.hasttacke import välj_täcke


@pytest.mark.integration
def test_kallt_väder_ger_vintertäcke():
    assert välj_täcke(2, False) == "vintertäcke"


@pytest.mark.integration
def test_regn_ger_regntäcke():
    assert välj_täcke(10, True) == "regntäcke"


@pytest.mark.integration
def test_varmt_och_torrt_ger_inga_täcken():
    assert välj_täcke(15, False) == "inget täcke"
