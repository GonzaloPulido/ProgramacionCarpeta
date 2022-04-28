from ej5 import comprobar_fecha

def years_diferencia(day1,month1,year1,day2,month2,year2):
    if year1 == year2:
        return 0
    elif year1 < year2:
        if month1 < month2 or (month1 == month2 and day1 < day2):
            return year2 - year1 - 1
        else:
            return year2 - year1
    elif year1 > year2:
        if month1 < month2 or (month1 == month2 and day1 < day2):
            return year1 - year2 - 1
        else:
            return year1 - year2
    

if __name__=="__main__":
    while True:
        try:
            day1 = int(input("Introduce el dia de la primera fecha: "))
            month1 = int(input("Introduce el mes de la primera fecha: "))
            year1 = int(input("Introduce el año de la primera fecha: "))
            day2 = int(input("Introduce el dia de la segunda fecha: "))
            month2 = int(input("Introduce el mes de la segunda fecha: "))
            year2 = int(input("Introduce el año de la segunda fecha: "))
            if comprobar_fecha(day1,month1,year1) and comprobar_fecha(day2,month2,year2):
                break
            else:
                print("Parece que las fechas no son correctas")
        except ValueError:
            print("Eso no es un numero")

    print("La diferencia de años entre las dos fechas es",years_diferencia(day1,month1,year1,day2,month2,year2))