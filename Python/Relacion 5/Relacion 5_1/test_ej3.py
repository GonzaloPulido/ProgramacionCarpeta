import pytest
from ej3 import contraseña_valida

def test_contraseña_valida():
    assert contraseña_valida("1Abasdfg") == True
    assert contraseña_valida("1aaaaa") == False