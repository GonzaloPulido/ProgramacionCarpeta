import pytest
from ej6 import eliminar_extremos
sorted_lista = [1,2,3,4,5,6,7,8]
unsorted_lista = [8,1,4,3,2,6,5,7]


def test_eliminar_extremos():
    assert eliminar_extremos(sorted_lista) == 4.5
    assert eliminar_extremos(unsorted_lista) == 4.5