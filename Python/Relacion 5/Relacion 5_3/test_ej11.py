import pytest
from ej11 import caracteres_diferentes

def test_caracteres_diferentes():
    assert caracteres_diferentes('programacion') == {'p':1,'r':2,'o':2,'g':1,'a':2,'m':1,'c':1,'i':1,'n':1}
    assert caracteres_diferentes('gonzalo') == {'g':1,'o':2,'n':1,'z':1,'a':1,'l':1}
    assert caracteres_diferentes('javier') == {'j':1,'a':1,'v':1,'i':1,'e':1,'r':1}