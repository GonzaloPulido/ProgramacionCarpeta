def raiz_cuadrada_aprox(numero):
    for x in range(1,numero//2+1):
        if x*x <= numero:
            resultado = x
    return resultado
