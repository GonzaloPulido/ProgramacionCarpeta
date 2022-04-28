while True:
    try:
        entrada = int(input("Introduce un numero: "))
        if entrada <= 0:
            print("La entrada debe ser mayor que 0")
        else:
            break
    except ValueError:
        print("Eso no es un numero")

for x in range(1,entrada+1):
    if x%2 == 0:
        print(-x,end=",")
    else:
        print(x,end=",")