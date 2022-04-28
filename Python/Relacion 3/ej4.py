def bisiestos(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100:
        return True
    else:
        return False

if __name__=="__main__":
    while True:
        try:
            year = int(input("Introduce un año para saber si es bisiesto o no: "))
            if year < 0 :
                print("El año debe ser 0 o mayor")
            else:
                break
        except ValueError:
            print("Eso no es un numero")
    
    if bisiestos(year):
        print("El año",year,"es bisiesto")
    else:
        print("El año",year,"no es bisiesto")
