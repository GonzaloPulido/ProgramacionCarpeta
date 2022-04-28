def caracteres_diferentes(cadena):
    caracteres = dict()
    cadena = cadena.lower()
    for valor in cadena:
        if valor in caracteres.keys():
            caracteres[valor] += 1
        else:
            caracteres[valor] = 1
    
    return caracteres

if __name__=="__main__":
    while True:
        cadena = input("Introduce una cadena: ")
        if cadena.isalpha():
            break
        else:
            print("La cadena debe contener unicamente letras")
    
    print("El recuento de letras de tu cadena es",caracteres_diferentes(cadena))
