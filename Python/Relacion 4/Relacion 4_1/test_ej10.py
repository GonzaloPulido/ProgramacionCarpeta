import pytest
from ej10 import producto_numeros

def test_producto_numero():
    assert producto_numeros(36) == ['18*2', '12*3', '9*4', '6*6', '4*9', '3*12', '2*18']
    assert producto_numeros(20) == ['10*2', '5*4', '4*5', '2*10']