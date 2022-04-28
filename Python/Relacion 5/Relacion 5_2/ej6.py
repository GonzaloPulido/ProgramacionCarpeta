def eliminar_extremos(lista):
    lista = sorted(lista)
    del lista[0]
    del lista[-1]
    media = sum(lista)/len(lista)
    return media

if __name__=="__main__":
    puntuaciones = []
    while len(puntuaciones) < 8:
        try:
            entrada = int(input("Introduce la puntuacion entre 1 y 10: "))
            if entrada >= 1 and entrada <= 10:
                puntuaciones.append(entrada)
                print(puntuaciones)
            else:
                print("La puntuacion debe ser entre 1 y 10")

        except ValueError:
            print("Eso no es un numero")
    
    
    print("La media de puntuaciones del jurado es",eliminar_extremos(puntuaciones))
