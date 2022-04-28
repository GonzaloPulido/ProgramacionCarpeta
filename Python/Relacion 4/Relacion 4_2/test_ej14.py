import pytest
from ej14 import dia_siguiente

def test_dia_siguiente():
    assert dia_siguiente(31,1,2020) == (1,2,2020)
    assert dia_siguiente(31,12,2020) == (1,1,2021)
    assert dia_siguiente(30,4,2020) == (1,5,2020)
    assert dia_siguiente(28,2,2021) == (1,3,2021)
    assert dia_siguiente(29,2,2020) == (1,3,2020)
    assert dia_siguiente(18,10,2021) == (19,10,2021)
    assert dia_siguiente(29,2,2021) == None