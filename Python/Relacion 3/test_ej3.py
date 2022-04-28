import pytest
from ej3 import distancia_puntos

def test_distancia_puntos():
    assert distancia_puntos(1,1,1,1) == 0
    assert distancia_puntos(1,2,3,4) == 1.41
    assert distancia_puntos (-1,3,-2,5) == 8.06
