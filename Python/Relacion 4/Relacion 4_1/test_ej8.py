import pytest
from ej8 import numeros_amigos

def test_numeros_amigos():
    assert numeros_amigos(1,2) == False
    assert numeros_amigos(220,284) == True