while True:
    try: 
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
        numero3 = int(input("Introduce el tercer numero: "))
        break
    except ValueError:
        print("El valor a introducir debe ser de tipo numerico")

if numero1 > numero2 and numero1 > numero3:
    print("El numero",numero1,"es el mayor de los tres")
elif numero2 > numero1 and numero2 > numero3:
    print("El numero",numero2,"es el mayor de los tres")
elif numero3 > numero1 and numero3 > numero2:
    print("El numero",numero3,"es el mayor de los tres")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Hay dos numeros que son iguales")
else:
    print("Los tres numeros son iguales")