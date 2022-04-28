import random
def hay_duplicados(lista):
    # --------- Forma de Javi ---------
    # return len(set(lista)) != len(lista)
    lista2 = lista.copy()
    lista2 = list(set(lista2))
    if sorted(lista) == lista2:
        return True
    return False


if __name__=="__main__":
    intentos = 0
    while True:
        lista = []
        while len(lista) < 20:
            numero = random.randint(1,100)
            lista.append(numero)
        if hay_duplicados(lista):
            intentos += 1
            break
        else:
            intentos += 1
            
    
    print("Lista sin duplicados",lista)
    print("Han sido necesarios",intentos,"intentos")

    