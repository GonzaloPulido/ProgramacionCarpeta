while True:
    try: 
        numero = int(input("Introduce un numero: "))
        break
    except ValueError:
        print("El valor a introducir debe ser de tipo numerico")

if numero % 2 == 0:
    print("El numero",numero,"es par")
else:
    print("El numero",numero,"es impar")