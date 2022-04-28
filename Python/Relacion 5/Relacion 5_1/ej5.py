import random

def elegir_palabra(palabras):
    palabra = random.choice(palabras)
    return palabra

def generar_tablero(palabra):
    tablero = []
    for x in palabra:
        tablero.append("_")
    return tablero

def comprobar_letra(letra,palabra):
    if letra in palabra:
        return True
    else:
        return False

def actualizar_tablero(letra,tablero,palabra):
    numero = 0
    for x in palabra:
        if x == letra:
            tablero[numero] = letra
            numero += 1
        else:
            numero += 1
    return tablero
def comprobar_win(tablero):
    for elemento in tablero:
        if elemento == "_":
            return False
    return True
        

if __name__=="__main__":
    palabras = ["cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana"]
    letras_falladas = []
    palabra = elegir_palabra(palabras)
    tablero = generar_tablero(palabra)
    vidas = 5

    print("--------- AHORCADO ---------")
    while True:
        if vidas == 0:
            print("Lo sentimos, te has quedado sin vidas")
            break
        elif comprobar_win(tablero):
            print("¡¡¡¡¡¡  HAS GANADO  !!!!!!")
            print("La palabra era ",*palabra ,sep="")
            break
        else:
            print("--------- DATOS DEL JUEGO ---------")
            print("Tu tablero: ",tablero)
            print("Te quedan",vidas,"vidas")
            print("Letras falladas: ",letras_falladas)
            letra = input("Introduce una letra: ")
            if len(letra) == 1 and letra.isalpha():
                letra = letra.lower()
                if comprobar_letra(letra,palabra):
                    actualizar_tablero(letra,tablero,palabra)
                else:
                    letras_falladas.append(letra)
                    vidas -= 1
                    print("Has fallado")
            else:
                print("Eso no es una letra")