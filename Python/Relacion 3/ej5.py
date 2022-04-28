from ej4 import bisiestos

def comprobar_fecha(day,month,year):
    if year > 0:
        if month > 0 and month < 13:
            if day >= 1 and day <= 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                return True
            elif day >= 1 and day <= 30 and month == 4 or month == 6 or month == 9 or month == 11: 
                return True
            elif day >= 1 and day <= 28 and month == 2 and not bisiestos(year):
                return True
            elif day >= 1 and day <= 29 and month == 2 and bisiestos(year):
                return True
            else:
                return False
        else:
            return False      
    else:
        return False

if __name__=="__main__":
    while True:
        try:
            day = int(input("Introduce el dia de la fecha: "))
            month = int(input("Introduce el mes de la fecha: "))
            year = int(input("Introduce el año de la fecha: "))
            break
        except ValueError:
            print("Eso no es un numero")
    
    if comprobar_fecha(day,month,year):
        print("La fecha es valida")
    else:
        print("La fecha no es valida")