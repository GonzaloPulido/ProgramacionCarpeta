from ej2 import contraseña_aleatoria
from ej3 import contraseña_valida

def contraseña_correcta():
    intentos = 0
    while True:
        contraseña = contraseña_aleatoria()
        validar = contraseña_valida(contraseña)
        if validar == True:
            intentos += 1
            return contraseña,intentos
        else:
            intentos +=1