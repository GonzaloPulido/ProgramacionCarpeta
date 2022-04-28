def ordenado(numero):
    lista = list()
    numero = str(numero)
    for x in numero:
        lista.append(x)
    lista2 = sorted(lista)
    if lista == lista2:
        return True
    lista2.reverse()
    if lista == lista2:
        return True
    return False
    

def sumados(numero):
    lista = list()
    numero = str(numero)
    for x in numero:
        lista.append(int(x))
    if lista[0] + lista[1] == lista[2]:
        return True
    elif lista[1] + lista[2] == lista[0]:
        return True
    elif lista[0] + lista[2] == lista[1]:   
        return True
    return False

def impar_multiplo(numero):
    if numero % 2 != 0:
        lista = list()
        numero = str(numero)
        for x in numero:
            lista.append(int(x))
        suma = sum(lista)
        if suma % 3 == 0:
            return True
    return False

def matrices(matriz):
    resultado = []

    for x in matriz:
        matriz_secundaria = []
        for y in x:
            if ordenado(y) or sumados(y) or impar_multiplo(y):
                matriz_secundaria.append(True)
            else:
                matriz_secundaria.append(False)
        resultado.append(matriz_secundaria)
    return resultado

matriz = [[123,456,789],[123,422,253],[123,147,138],[512,324,161]]
print(matrices(matriz))