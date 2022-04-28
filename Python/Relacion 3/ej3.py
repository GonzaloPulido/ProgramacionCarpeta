import math
def distancia_puntos(x1,x2,y1,y2):
    return round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)

if __name__=="__main__":
    while True:
        try:
            x1 = int(input("Introduce la posicion x1: "))
            x2 = int(input("Introduce la posicion x2: "))
            y1 = int(input("Introduce la posicion y1: "))
            y2 = int(input("Introduce la posicion y2: "))
            break
        except ValueError:
            print("Eso no es un numero")
    
    print("La distancia entre los dos puntos es",distancia_puntos(x1,x2,y1,y2))