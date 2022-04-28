import pytest
from ej6 import years_diferencia

def test_years_diferencia():
    assert years_diferencia(1,2,1,1,3,1) == 0
    assert years_diferencia(1,1,1,1,2,2) == 0
    assert years_diferencia(1,2,1,1,1,2) == 1
    assert years_diferencia(1,1,2,1,2,1) == 0
    assert years_diferencia(1,2,2,1,1,1) == 1