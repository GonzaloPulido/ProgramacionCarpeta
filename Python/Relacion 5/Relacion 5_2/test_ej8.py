import pytest
from ej8 import hay_duplicados

def test_hay_duplicados():
    assert hay_duplicados([79, 62, 51, 46, 77, 58, 52, 45, 39, 74, 31, 99, 29, 17, 69, 75, 59, 23, 16, 92]) == True
    assert hay_duplicados([79, 62, 51, 51, 59, 58, 52, 45, 39, 74, 31, 99, 29, 17, 69, 75, 59, 23, 16, 92]) == False