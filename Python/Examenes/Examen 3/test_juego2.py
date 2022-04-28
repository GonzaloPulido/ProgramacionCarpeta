import pytest
from juego2 import crear_diccionario,crear_ataque,crear_cura,comprobar_nombre
lista = [{"NOMBRE":"Gonzalo","PV":100},{"NOMBRE":"Cancelo","PV":50},{"NOMBRE":"Juan","PV":80}]

def test_crear_diccionario():
    assert crear_diccionario("Gonzalo",100) == {"NOMBRE":"Gonzalo","PV":100}
    assert crear_diccionario("Cancelo",50) == {"NOMBRE":"Cancelo","PV":50}

def test_crear_ataque():
    assert crear_ataque("Gonzalo","Cancelo",40,80) == {"JUGADOR":"Gonzalo","OBJETIVO":"Cancelo","PV":40,"POSIBILIDAD":80,"TIPO":"Atacar"}
    assert crear_ataque("Juan","Antonio",20,30) == {"JUGADOR":"Juan","OBJETIVO":"Antonio","PV":20,"POSIBILIDAD":30,"TIPO":"Atacar"}

def test_crear_cura():
    assert crear_cura("Gonzalo",20) == {"JUGADOR":"Gonzalo","PV":20,"TIPO":"Curar"}
    assert crear_cura("Juan",30) == {"JUGADOR":"Juan","PV":30,"TIPO":"Curar"}

def test_comprobar_nombre():
    assert comprobar_nombre("Gonzalo",lista) == {"NOMBRE":"Gonzalo","PV":100}
    assert comprobar_nombre("Cancelo",lista) == {"NOMBRE":"Cancelo","PV":50}
    assert comprobar_nombre("Juan",lista) == {"NOMBRE":"Juan","PV":80}
    assert comprobar_nombre("Pepe",lista) == False
    

