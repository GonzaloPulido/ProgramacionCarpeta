import pytest
from ej5 import comprobar_fecha

def test_comprobar_fecha():
    # fechas correctas
    assert comprobar_fecha(31,1,2001) == True
    assert comprobar_fecha(30,4,2001) == True
    assert comprobar_fecha(28,2,2001) == True
    assert comprobar_fecha(29,2,2020) == True
    # fechas incorrectas(dias)
    assert comprobar_fecha(32,1,2001) == False
    assert comprobar_fecha(31,4,2001) == False
    assert comprobar_fecha(29,2,2001) == False
    assert comprobar_fecha(30,2,2020) == False
    # fecha incorrecta mes()
    assert comprobar_fecha(1,0,2001) == False
    assert comprobar_fecha(31,13,2001) == False
    # fecha incorrecta año()
    assert comprobar_fecha(1,1,-1) == False
