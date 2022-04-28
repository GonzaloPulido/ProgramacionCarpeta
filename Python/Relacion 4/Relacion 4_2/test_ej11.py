import pytest
from ej11 import numero_central

def test_numero_central():
    assert numero_central(2,1,3) == 2
    assert numero_central(1,2,3) == 2
    assert numero_central(1,3,2) == 2
    assert numero_central(1,1,1) == 1
    assert numero_central(1,1,2) == None
