import pytest
from juego1 import jugador,aplica

jugador1 = {"NOMBRE":"Gonzalo","PV":100}
jugador2 = {"NOMBRE":"Cancelo","PV":100}
accion1 = {"TIPO":"Atacar","JUGADOR":"Gonzalo","PV":20,"OBJETIVO":"Cancelo","POSIBILIDAD":100}
accion2 = {"TIPO":"Curar","JUGADOR":"Gonzalo","PV":20}
lista = [jugador1,jugador2]

def test_jugador():
    assert jugador(lista,"Gonzalo") == {"NOMBRE":"Gonzalo","PV":100}
    assert jugador(lista,"Cancelo") == {"NOMBRE":"Cancelo","PV":100}

def test_aplica():
    assert aplica(jugador1,accion1) == {"NOMBRE":"Gonzalo","PV":80}
    assert aplica(jugador2,accion2) == {"NOMBRE":"Cancelo","PV":120}