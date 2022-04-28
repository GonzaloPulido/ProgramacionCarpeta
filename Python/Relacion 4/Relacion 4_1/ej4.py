def lista_numeros(lista):
    positivos = 0
    negativos = 0
    suma = sum(lista)
    for x in lista:
        if x > 0:
            positivos += 1
        elif x < 0:
            negativos += 1
    return suma,positivos,negativos


    