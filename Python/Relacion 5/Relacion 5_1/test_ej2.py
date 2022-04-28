import pytest
from ej2 import contraseña_aleatoria

def test_contraseña_aleatoria():
    assert len(contraseña_aleatoria()) >= 7 and len(contraseña_aleatoria()) <= 10