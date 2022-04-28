import pytest

from contraseñas1 import comprobar_contraseña

def test_comprobar_contraseña():
    # Contraseña limite primero
    assert comprobar_contraseña(["1-5 a: artzd"]) == 1
    # Contraseña limite segundo
    assert comprobar_contraseña(["1-5 a: aaaaaertzd"]) == 1
    # Contraseña incorrecta
    assert comprobar_contraseña(["1-5 a: aaaaaaaaaertzd"]) == 0