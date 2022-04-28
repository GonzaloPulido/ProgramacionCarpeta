from datos import passwords

def comprobar_contraseña(lista):
    contraseñas_validas = 0
    for elemento in lista:
        lista_split = elemento.split()
        longitud_letras = lista_split[0].split("-")
        letra = lista_split[1].replace(":","")
        contraseña = lista_split[2]
        contador = 0
        for x in contraseña:
            if x == letra:
                contador += 1
        if contador >= int(longitud_letras[0]) and contador <= int(longitud_letras[1]):
            contraseñas_validas += 1

    return contraseñas_validas

if __name__=="__main__":
    
    entrada = input("¿Quiere ver cuantas contraseñas son validas? Y/N: ")
    if entrada.upper() == "Y":
        print(comprobar_contraseña(passwords))
    elif entrada.upper() == "N":
        print("Adios, gracias por usar el programa")
    else:
        print("La entrada no es valida, debe ser y ó n")