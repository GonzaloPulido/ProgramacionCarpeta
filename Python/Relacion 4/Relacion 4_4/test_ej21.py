import pytest
from ej21 import veinte_años

def test_veinte_años():
    assert veinte_años(18,10,2021,18,10,1994) == "Tienes mas de 20 años"
    assert veinte_años(18,10,2021,18,9,2001) == "Tienes mas de 20 años"
    assert veinte_años(18,10,2021,17,10,2001) == "Tienes mas de 20 años"
    assert veinte_años(18,10,2021,18,10,2001) == "¡Felicidades!Hoy es tu 20 cumpleaños"
    assert veinte_años(18,10,2021,20,10,2021) == "Tienes menos de 20 años"
    assert veinte_años(18,10,2021,20,11,2021) == "Tienes menos de 20 años"
    assert veinte_años(18,10,2021,20,11,2018) == "Tienes menos de 20 años"