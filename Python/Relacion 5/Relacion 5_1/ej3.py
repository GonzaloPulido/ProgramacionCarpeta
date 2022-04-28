def contraseña_valida(contraseña):
    mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minus = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = ["1","2","3","4","5","6","7","8","9"]
    caracter_mayus = 0
    caracter_minus = 0
    caracter_num = 0

    for caracter in contraseña:
        if caracter in num:
            caracter_num += 1
        elif caracter in mayus:
            caracter_mayus += 1
        elif caracter in minus:
            caracter_minus += 1

    if caracter_num > 0 and caracter_mayus > 0 and caracter_minus > 0 and len(contraseña) >= 8:
        return True

    return False


if __name__=="__main__":
    contraseña = input("Introduce una contraseña: ")

    if contraseña_valida(contraseña):
        print("La contraseña es valida")
    else:
        print("La contraseña no es valida")
