import random

def contraseña_aleatoria():
    longitud = random.randint(7,10)
    contraseña = ""
    while len(contraseña) < longitud:
        caracter = random.randint(33,126)
        contraseña += chr(caracter)
    return contraseña

    