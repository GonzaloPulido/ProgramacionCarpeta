while True:
    try:    
        suma = int(input("Introduce el primer numero: ")) + int(input("Introduce el segundo numero: ")) + int(input("Introduce el tercer numero: "))
        break
    except ValueError:
        print("El numero debe ser introducido con cifras")

print("La suma de los numeros introducidos es",suma)