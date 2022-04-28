import pytest

from contraseñas2 import comprobar_contraseña

def test_comprobar_contraseña():
    # Primera posicion correcta
    assert comprobar_contraseña(["1-5 a: artzd"]) == 1
    # Segunda condicion correcta
    assert comprobar_contraseña(["1-5 a: qweraertzd"]) == 1
    # Dos posiciones incorrecta
    assert comprobar_contraseña(["1-5 a: aaaaaaaaaertzd"]) == 0
    # Dos posiciones no esta
    assert comprobar_contraseña(["1-5 b: aaaaaaaaaertzd"]) == 0