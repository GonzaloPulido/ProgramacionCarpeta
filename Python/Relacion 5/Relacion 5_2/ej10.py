def palindromos(lista):
    lista_palindromos = []
    for palabra in lista:
        if palabra == palabra[::-1]:
            lista_palindromos.append(palabra)
    return lista_palindromos

