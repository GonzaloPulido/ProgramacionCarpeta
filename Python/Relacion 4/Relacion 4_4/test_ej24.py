import pytest
from ej24 import binarios

def test_binarios():
    assert binarios(20) == [1,0,1,0,0]
    assert binarios(0) == [0]