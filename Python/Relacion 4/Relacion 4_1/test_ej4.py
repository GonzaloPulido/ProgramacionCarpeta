import pytest
from ej4 import lista_numeros
lista = [1,2,3,4,5,-6,-7,-8,-9]

def test_lista_numeros():
    assert lista_numeros(lista) == (-15,5,4)