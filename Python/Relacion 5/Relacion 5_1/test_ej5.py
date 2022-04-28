import pytest
from ej5 import generar_tablero,comprobar_letra,actualizar_tablero,comprobar_win
palabra = "alerones"
tablero = ["_","_","_","_","_","_","_","_"]
win = ["a","l","e","r","o","n","e","s"]

def test_generar_tablero():
    assert generar_tablero(palabra) == ["_","_","_","_","_","_","_","_"]

def test_comprobar_letra():
    assert comprobar_letra("a",palabra) == True
    assert comprobar_letra("u",palabra) == False

def test_actualizar_tablero():
    assert actualizar_tablero("a",tablero,palabra) == ["a","_","_","_","_","_","_","_"]

def test_comprobar_win():
    assert comprobar_win(win) == True

