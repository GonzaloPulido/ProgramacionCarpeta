def elimina_duplicados(lista):
    lista.sort()
    lista_de_duplicados = []
    lista_guardar = []
    for valor in lista:
        if valor in lista_guardar:
            lista_de_duplicados.append(valor)
        else:
            lista_guardar.append(valor)

    return lista_de_duplicados