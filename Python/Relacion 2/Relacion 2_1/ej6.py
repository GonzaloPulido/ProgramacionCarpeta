while True:
    try: 
        entrada = int(input("Introduce el primer numero: "))
        almacen = entrada
        entrada = int(input("Introduce el segundo numero: "))
        if almacen < entrada:
            almacen = entrada
        entrada = int(input("Introduce el primer numero: "))
        if almacen < entrada:
            almacen = entrada
        break
    except ValueError:
        print("El valor a introducir debe ser de tipo numerico")

print("El mayor de los tres numeros es",almacen)