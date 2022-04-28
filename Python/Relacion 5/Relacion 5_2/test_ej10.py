import pytest
from ej10 import palindromos
lista = ['rallar','eje','reconocer','rajar','salas','javi','apruebame','por','favor']
lista_mal = ['hola','no','tengo','palindromos']

def test_palindromos():
    assert palindromos(lista) == ['rallar','eje','reconocer','rajar','salas']
    assert palindromos(lista_mal) == []
     