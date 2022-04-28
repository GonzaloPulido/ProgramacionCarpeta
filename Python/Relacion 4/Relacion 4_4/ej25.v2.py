def hexadecimal(numero):
    digitos = "0123456789ABCDEF"
    lista = []
    while numero >= 16:
        resto = numero % 16
        lista.append(digitos[resto])
        numero = numero // 16
    lista.append(digitos[numero])
    lista.reverse()
    return lista

print(hexadecimal(255))