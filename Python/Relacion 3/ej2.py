import math
def longitud_circunferencia(radio,pi):
    return round(2*pi*radio,2)

if __name__=="__main__":
    while True:
        try:
            radio = float(input("Introduce el radio de la circunferencia: "))
            if radio <= 0:
                print("El radio debe ser mayor que 0")
            else:
                break
        except ValueError:
            print("Eso no es un numero")
    pi = math.pi
    print("La longitud de la circunferencia es",longitud_circunferencia(radio,pi))