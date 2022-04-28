def alturas(lista):
    muy_altos = 0
    altos = 0
    medianos = 0
    bajos = 0
    for x in lista:
        if x > 1.70:
            muy_altos += 1
        elif x > 1.60 and x <= 1.70:
            altos += 1
        elif x > 1.50 and x <= 1.60:
            medianos += 1
        elif x <= 1.50:
            bajos += 1
    return muy_altos,altos,medianos,bajos
