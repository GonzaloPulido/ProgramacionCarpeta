while True:
    try: 
        horas_trabajo = int(input("Introduce las horas que has trabajado: "))
        precio_hora  = int(input("Introduce cuanto cobras por hora: "))
        if horas_trabajo <= 0 or precio_hora <= 0:
            print("Los valores no pueden ser menores que uno")
        else:
            break
    except ValueError:
        print("Parece que el dato introducido no es valido")

if horas_trabajo > 40:
    plus = (horas_trabajo - 40) * precio_hora * 1.5
    importe_total = 40 * precio_hora + plus
else:
    importe_total = horas_trabajo * precio_hora

print('Has cobrado',importe_total,'€')