import pytest
from caddie import comprobar_hoyo,modificar_par,hay_golpes,añadir_modificar_golpes,termino_golf,devolver_listado,resultado

def test_comprobar_hoyo():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":6},{"HOYO":2,"PAR":3}]
    assert comprobar_hoyo(1,lista1) == True
    assert comprobar_hoyo(18,lista1) == False
    
def test_modificar_par():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":6},{"HOYO":2,"PAR":3}]
    assert modificar_par(1,4,lista1) == {"HOYO":1,"PAR":4,"GOLPES":6}

def test_hay_golpes():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":6},{"HOYO":2,"PAR":3}]
    assert hay_golpes(1,lista1) == True
    assert hay_golpes(2,lista1) == False

def test_añadir_modificar_golpes():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":6},{"HOYO":2,"PAR":3}]
    assert añadir_modificar_golpes(1,7,lista1) == {"HOYO":1,"PAR":3,"GOLPES":7}
    assert añadir_modificar_golpes(2,7,lista1) == {"HOYO":2,"PAR":3,"GOLPES":7}

def test_termino_golf():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":3},{"HOYO":2,"PAR":3,"GOLPES":2},
    {"HOYO":3,"PAR":2,"GOLPES":3},{"HOYO":4,"PAR":4,"GOLPES":2},{"HOYO":5,"PAR":2,"GOLPES":4},
    {"HOYO":6,"PAR":3,"GOLPES":9}]
    assert termino_golf(1,lista1) == "PAR"
    assert termino_golf(2,lista1) == "BIRDIE"
    assert termino_golf(3,lista1) == "BOGEY"
    assert termino_golf(4,lista1) == "EAGLE"
    assert termino_golf(5,lista1) == "DOBLE BOGEY"
    assert termino_golf(6,lista1) == "FUERA DE RANGO"

def test_devolver_listado():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":3},{"HOYO":4,"PAR":4,"GOLPES":2},
    {"HOYO":5,"PAR":2,"GOLPES":4},{"HOYO":2,"PAR":3,"GOLPES":2},{"HOYO":3,"PAR":2,"GOLPES":3},
    {"HOYO":6,"PAR":3,"GOLPES":9}]
    assert devolver_listado(lista1) == [{"HOYO":1,"PAR":3,"GOLPES":3},{"HOYO":2,"PAR":3,"GOLPES":2},{"HOYO":3,"PAR":2,"GOLPES":3},{"HOYO":4,"PAR":4,"GOLPES":2},{"HOYO":5,"PAR":2,"GOLPES":4},{"HOYO":6,"PAR":3,"GOLPES":9}]

def test_resultado():
    lista1 = [{"HOYO":1,"PAR":3,"GOLPES":3},{"HOYO":2,"PAR":3,"GOLPES":2},
    {"HOYO":3,"PAR":2,"GOLPES":3},{"HOYO":4,"PAR":4,"GOLPES":2},{"HOYO":5,"PAR":2,"GOLPES":4},
    {"HOYO":6,"PAR":3,"GOLPES":9}]
    assert resultado(lista1) ==  [{"HOYO":1,"DIFERENCIA":0},{"HOYO":2,"DIFERENCIA":1},{"HOYO":3,"DIFERENCIA":1},{"HOYO":4,"DIFERENCIA":2},{"HOYO":5,"DIFERENCIA":2},{"HOYO":6,"DIFERENCIA":6}] 

