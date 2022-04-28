import pytest
from ej1 import sin_vocales,sin_consonantes,vocales_mayus

def test_sin_vocales():
    assert sin_vocales("Programaciona") == "Prgrmcn"

def test_sin_consonantes():
    assert sin_consonantes("Programacion") == "oaaio"

def test_vocales_mayus():
    assert vocales_mayus("Programacion") == "PrOgrAmAcIOn"