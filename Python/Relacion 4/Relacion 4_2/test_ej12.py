import pytest
from ej12 import raiz_cuadrada_aprox

def test_raiz_cuadrada_aprox():
    assert raiz_cuadrada_aprox(27) == 5
    assert raiz_cuadrada_aprox(30) == 5