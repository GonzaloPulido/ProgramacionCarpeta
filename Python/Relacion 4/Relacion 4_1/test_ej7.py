import pytest
from ej7 import division_con_restas

def test_divison_con_restas():
    assert division_con_restas(20,2) == (10,0)
    assert division_con_restas(30,7) == (4,2)