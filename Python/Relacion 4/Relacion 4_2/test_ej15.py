import pytest
from ej15 import alturas
lista = [1.71,1.65,1.55,1.49]


def test_alturas():
    assert alturas(lista) == (1,1,1,1)