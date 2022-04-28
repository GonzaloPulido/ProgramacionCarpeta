import pytest
from ej14 import puntuaciones

def test_puntuaciones():
    assert puntuaciones('programacion') == 19
    assert puntuaciones('gonzalo') == 17
    assert puntuaciones('javier') == 16
    assert puntuaciones('zapato') == 17