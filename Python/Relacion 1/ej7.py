while True:
    try:    
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
        numero3 = int(input("Introduce el tercer numero: "))
        break
    except ValueError:
        print("El numero debe ser introducido con cifras")

suma = numero1 + numero2 + numero3

print("La suma de los numeros introducidos es",suma)