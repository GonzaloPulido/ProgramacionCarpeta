def numeros_perfectos(entrada):
    lista = []
    for x in range(1,entrada):
        suma = 0
        for y in range(1,x):
            if x % y == 0:
                suma += y
        if suma == x:
            lista.append(x)
    return lista

if __name__=="__main__":
    while True:
        try:
            entrada = int(input("Introduce un numero: "))
            if entrada > 0:
                break
            else:
                print("El numero tiene que ser mayor que 0")
        except ValueError:
            print("Eso no es un numero")
    
    print("Los numeros perfectos menores que",entrada,"son",numeros_perfectos(entrada))