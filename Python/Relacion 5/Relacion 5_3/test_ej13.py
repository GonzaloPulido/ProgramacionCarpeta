import pytest
from ej13 import codigo_morse

def test_codigo_morse():
    assert codigo_morse('programacion') == ['.--.', '.-.', '---', '--.', '.-.', '.-', '--', '.-', '-.-.', '..', '---', '-.']
    assert codigo_morse('gonzalo123') == ['--.', '---', '-.', '--..', '.-', '.-..', '---', '.----', '..---', '...--']
    assert codigo_morse('javier456') == ['.---', '.-', '...-', '..', '.', '.-.', '....-', '.....', '-....']
    assert codigo_morse('789') == ['--...', '---..', '----.']