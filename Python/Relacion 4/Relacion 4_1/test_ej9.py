import pytest
from ej9 import numeros_perfectos

def test_numeros_perfectos():
    assert numeros_perfectos(50) == [6,28]
    assert numeros_perfectos(500) == [6,28,496]