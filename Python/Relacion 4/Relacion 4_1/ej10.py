def producto_numeros(entrada):
    lista = []
    producto = ""
    for x in range(entrada,1,-1):
        for y in range(2,entrada):
            producto = ""
            if x * y == entrada:
                x = str(x)
                y = str(y)
                producto += x+"*"+y
                lista.append(producto)
    return lista

if __name__=="__main__":
    while True:
        try:
            entrada = int(input("Introduce un numero: "))
            if entrada > 2:
                break
            else:
                print("El numero debe ser mayor que 2")
        except ValueError:
            print("Eso no es un numero")
    
    print("Productos de",entrada,":",producto_numeros(entrada))