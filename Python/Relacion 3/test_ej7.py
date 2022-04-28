import pytest
from ej7 import caracteres_binario

def test_caracteres_binario():
    assert caracteres_binario(20) == 5
    assert caracteres_binario(1) == 1
    assert caracteres_binario(0) == 1