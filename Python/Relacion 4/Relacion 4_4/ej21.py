from datetime import datetime
def comprobar_fecha(day,month,year):
    bisiesto = bool
    if year > 0:
        if year % 400 == 0 or year % 4 == 0 and year % 100:
            bisiesto = True
        else:
            bisiesto = False
        if month > 0 and month < 13:
            if day >= 1 and day <= 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                return True
            elif day >= 1 and day <= 30 and month == 4 or month == 6 or month == 9 or month == 11: 
                return True
            elif day >= 1 and day <= 28 and month == 2 and not bisiesto:
                return True
            elif day >= 1 and day <= 29 and month == 2 and bisiesto:
                return True
            else:
                return False
        else:
            return False      
    else:
        return False
    
def veinte_años(day_hoy,month_hoy,year_hoy,day_birth,month_birth,year_birth):
    diferenciaYear = year_hoy - year_birth
    if diferenciaYear > 20:
        return "Tienes mas de 20 años"
    elif diferenciaYear == 20:
        if month_hoy > month_birth:
            return "Tienes mas de 20 años"
        elif month_hoy == month_birth:
            if day_hoy > day_birth:
                return "Tienes mas de 20 años"
            elif day_hoy == day_birth:
                return "¡Felicidades!Hoy es tu 20 cumpleaños"
            else:
                return "Tienes menos de 20 años"
        else:
            return "Tienes menos de 20 años"
    else:
        return "Tienes menos de 20 años"

if __name__=="__main__":
    now = datetime.now()
    while True:
        try:
            day_hoy = int(input("Introduce el dia de la fecha de hoy: "))
            month_hoy = int(input("Introduce el mes de la fecha de hoy: "))
            year_hoy = int(input("Introduce el año de la fecha de hoy: "))
            day_birth = int(input("Introduce el dia de tu fecha de nacimiento: "))
            month_birth = int(input("Introduce el mes de tu fecha de nacimiento: "))
            year_birth = int(input("Introduce el año de tu fecha de nacimiento: "))
            if day_hoy == now.day and month_hoy == now.month and year_hoy == now.year:
                if comprobar_fecha(day_birth,month_birth,year_birth):
                    if year_birth > year_hoy:
                        print("La fecha introducida tiene que ser menor que la fecha de hoy")
                    else:
                        break
                else:
                    print("Ups, parece que la fecha de tu cumpleaños no es correcta")
            else:
                print("Esa no es la fecha de hoy")

        except ValueError:
            print("La fecha debe ser introducida con numeros")

    
