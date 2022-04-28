while True:
    try: 
        horas_trabajo = int(input("Introduce las horas que has trabajado: "))
        precio_hora  = int(input("Introduce cuanto cobras por hora: "))
        break
    except ValueError:
        print("Parece que el dato introducido no es valido")

importe_total = horas_trabajo * precio_hora

print('Has cobrado',importe_total,'€')