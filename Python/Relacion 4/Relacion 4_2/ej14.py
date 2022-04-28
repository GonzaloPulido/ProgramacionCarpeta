def dia_siguiente(day,month,year):
    # Bisiestos
    
    if year % 400 == 0 or year % 4 == 0 and year % 100:
        bisiesto = True
    else:
        bisiesto = False
    # Bisiestos
    #Comprobar fecha
    if year > 0:
        if month > 0 and month < 13:
            if day >= 1 and day <= 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                fecha = True
            elif day >= 1 and day <= 30 and month == 4 or month == 6 or month == 9 or month == 11: 
                fecha = True
            elif day >= 1 and day <= 28 and month == 2 and not bisiesto:
                fecha = True
            elif day >= 1 and day <= 29 and month == 2 and bisiesto:
                fecha = True
            else:
                fecha = False
        else:
            fecha = False     
    else:
        fecha = False
    # Comprobar fecha
    # Dia siguiente
    if fecha:
        if day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            if month < 12:
                day = 1 
                month +=1
                return day,month,year
            elif month == 12:
                day = 1
                month = 1
                year += 1 
                return day,month,year
        elif day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            day = 1
            month += 1
            return day,month,year
        elif month == 2:
            if day == 28 and bisiesto:
                day +=1
                return day,month,year
            elif day == 28 and not bisiesto:
                day = 1
                month += 1
                return day,month,year
            elif day == 29:
                day = 1
                month += 1
                return day,month,year
        else:
            day += 1
            return day,month,year
    else:
        return None
    