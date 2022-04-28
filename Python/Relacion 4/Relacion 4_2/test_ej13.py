import pytest
from ej13 import precio_viaje

def test_precio_viaje():
    assert precio_viaje(500,8) == 3000.0
    assert precio_viaje(300,4) == 6000