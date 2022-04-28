import pytest
from ej9 import elimina_duplicados

def test_elimina_duplicados():
    assert elimina_duplicados([9,2,4,3,5,1,3,4,7,5]) == [3,4,5]
    assert elimina_duplicados([1,2,3,4,5,6]) == []
    assert elimina_duplicados([1,1,2,2,3,3,4,4]) == [1,2,3,4]