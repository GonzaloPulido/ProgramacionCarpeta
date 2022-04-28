def digito_hexadecimal(numero):
    if numero == 10:
        return 'A'
    elif numero == 11:
        return 'B'
    elif numero == 12:
        return 'C'
    elif numero == 13:
        return 'D'
    elif numero == 14:
        return 'E'
    elif numero == 15:
        return 'F'
    else:
        return str(numero)

def hexadecimal(numero):
    lista = []
    while numero >= 16:
        resto = numero % 16
        lista.append(digito_hexadecimal(resto))
        numero = numero // 16
    lista.append(digito_hexadecimal(numero))
    lista.reverse()
    return lista