def numero_central(numero1,numero2,numero3):
    if numero1 > numero2 and numero1 < numero3 or numero1 > numero3 and numero1 < numero2:
        return numero1
    elif numero2 > numero1 and numero2 < numero3 or numero2 > numero3 and numero2 < numero1:
        return numero2
    elif numero3 > numero1 and numero3 < numero2 or numero3 > numero2 and numero3 < numero1:
        return numero3
    elif numero1 == numero2 and numero2 == numero3:
        return numero1
    else:
        return None