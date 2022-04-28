while True:
    try: 
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
        opcion = int(input("""
        --------- OPERACIONES ---------
        1. SUMAR
        2. RESTAR
        3. MULTIPLICAR
        4. DIVIDIR

        Elige una de las opciones escribiendo su numero: """))
        if opcion >= 1 and opcion <= 4:
            if opcion == 4 and numero2 == 0:
                print("No se puede dividir un numero entre 0")
            else:
                break
    except ValueError:
        print("El valor a introducir debe ser de tipo numerico")


if opcion == 1:
    print("--------- Has elegido sumar ---------\nLa suma de los dos numeros es:",numero1 + numero2)
elif opcion == 2:
    print("--------- Has elegido restar ---------\nLa resta de los dos numeros es:",numero1 - numero2)
elif opcion == 3:
    print("--------- Has elegido multiplicar ---------\nLa multiplicacion de los dos numeros es:",numero1 * numero2)
elif opcion == 4:
    print("--------- Has elegido dividir ---------\nLa division de los dos numeros es:",numero1 / numero2)

