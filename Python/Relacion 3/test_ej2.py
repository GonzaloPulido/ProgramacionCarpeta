import pytest
import math
from ej2 import longitud_circunferencia

pi = math.pi
def test_longitud_circunferencia():
    assert longitud_circunferencia(18,pi) == 113.1