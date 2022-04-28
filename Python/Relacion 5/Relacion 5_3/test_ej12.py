import pytest
from ej12 import teclado_movil

def test_teclado_movil():
    assert teclado_movil('programacion') == [7, 777, 6666, 4, 777, 2, 6, 2, 222, 444, 6666, 66]
    assert teclado_movil('gonzalo') == [4, 6666, 66, 9999, 2, 555, 6666]
    assert teclado_movil('javier') == [5, 2, 88, 444, 33, 777]