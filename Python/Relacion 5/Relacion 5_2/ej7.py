def en_orden_ascendente(lista):
    lista2 = sorted(lista)
    if lista == lista2:
        return True
    else:
        return False


def esta_ordenada(lista):
    lista2 = sorted(lista)
    lista2.reverse()
    if lista == lista2:
        return True
    elif en_orden_ascendente(lista):
        return True
    else:
        return False