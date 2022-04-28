from typing import Container
from datos import passwords

def comprobar_contraseña(lista):
    contraseñas_correctas = 0
    for elemento in lista:
        lista_split = elemento.split()
        contraseña = lista_split[2]
        letra = lista_split[1].replace(":","")
        numeros = lista_split[0].split("-")
        if contraseña[int(numeros[0])-1] == letra:
            if not contraseña[int(numeros[1])-1] == letra:
                contraseñas_correctas += 1
        elif contraseña[int(numeros[1])-1] == letra:
            if not contraseña[int(numeros[0])-1] == letra:
                contraseñas_correctas += 1
        
    return contraseñas_correctas

if __name__=="__main__":
    
    entrada = input("¿Quiere ver cuantas contraseñas son validas? Y/N: ")
    if entrada.upper() == "Y":
        print(comprobar_contraseña(passwords))
    elif entrada.upper() == "N":
        print("Adios, gracias por usar el programa")
    else:
        print("La entrada no es valida, debe ser y ó n")

