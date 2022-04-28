from abc import abstractclassmethod
import pytest
from ej15 import dato_en_agenda,dar_nombre,es_nombre,es_numero,filtra_x
agenda = {"Gonzalo":"691270867"}



def test_dato_en_agenda():
    # Nombre
    assert dato_en_agenda("Gonzalo",agenda) == True
    assert dato_en_agenda("Pepe",agenda) == False
    # Numero
    assert dato_en_agenda("691270867", agenda) == True
    assert dato_en_agenda("612 123 123",agenda) == False
    # No valido
    assert dato_en_agenda(".gonza2",agenda) == None

def test_dar_nombre():
    assert dar_nombre("691270867",agenda) == "Gonzalo"
 
def test_es_nombre():
    assert es_nombre("Gonzalo") == True
    assert es_nombre(",Gonzalo") == False

def test_es_numero():
    assert es_numero("+12 123 123 123") == True
    assert es_numero("+12123123123") == None
    assert es_numero("691 27 08 67") == True
    assert es_numero("691 27 08 7") == None
    assert es_numero(".123 123 123") == None
    assert es_numero("Gonzalo") == None

def test_filtra_x():
    assert filtra_x("Gon",agenda) == [{"Gonzalo":"691270867"}]
    assert filtra_x("Pep",agenda) == []

