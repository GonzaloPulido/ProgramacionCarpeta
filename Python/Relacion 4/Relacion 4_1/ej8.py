def numeros_amigos(numero1,numero2):
    divisoresn1 = 0
    divisoresn2 = 0
    for x in range(1,numero1):
        if numero1 % x == 0:
            divisoresn1 += x

    for y in range(1,numero2):
        if numero2 % y == 0:
            divisoresn2 += y

    if divisoresn1 == numero2 and divisoresn2 == numero1:
        return True
    else:
        return False

if __name__=="__main__":
    while True:
        try:
            numero1 = int(input("Introduce el primer numero: "))
            numero2 = int(input("Introduce el segundo numero: "))
            if numero1 > 0 and numero2 > 0:
                break
            else:
                print("Los numeros tienen que ser mayores que cero")
        except ValueError:
            print("Eso no es un numero")

    if numeros_amigos(numero1,numero2):
        print("Los numeros",numero1,"y",numero2,"son amigos")
    else:
        print("Los numeros",numero1,"y",numero2,"no son amigos")
    
