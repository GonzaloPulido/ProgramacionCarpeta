def binarios(numero):
    lista = []
    if numero == 0:
        lista.append(0)
        return lista
    while numero >= 1:
        resto = numero % 2
        if resto % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)
        numero = numero // 2
    lista.reverse()
    return lista