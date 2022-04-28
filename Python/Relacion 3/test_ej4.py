import pytest
from ej4 import bisiestos

def test_bisiestos():
    assert bisiestos(2001) == False
    assert bisiestos(2020) == True