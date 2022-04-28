import pytest
from ej7 import en_orden_ascendente,esta_ordenada

def test_en_rden_ascendente():
    assert en_orden_ascendente([1,2,3,4]) == True
    assert en_orden_ascendente([4,3,2,1]) == False

def test_esta_ordenada():
    assert esta_ordenada([4,3,2,1]) == True
    assert esta_ordenada([1,2,3,4]) == True
    assert esta_ordenada([3,2,1,4]) == False