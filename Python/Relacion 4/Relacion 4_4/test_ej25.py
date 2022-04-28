import pytest
from ej25 import hexadecimal

def test_binarios():
    assert hexadecimal(16) == ['1','0']
    assert hexadecimal(27) == ['1','B']
    assert hexadecimal(255) == ['F','F']