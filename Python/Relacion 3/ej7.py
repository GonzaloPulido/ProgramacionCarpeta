def caracteres_binario(numero):
    contador = 0
    binario = bin(numero)[2:]
    longitud = len(binario)
    return longitud
        
if __name__=="__main__":
    while True:
        try:
            numero = int(input("Introduce un numero entero: "))
            if numero >= 0:
                break
            else:
                print("El numero debe ser positivo")
        except ValueError:
            print("Eso no es un numero")
    
    print("El numero",numero,"en binario ocupa",caracteres_binario(numero),"caracteres")
