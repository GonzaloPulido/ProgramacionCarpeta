def sin_vocales(cadena):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for caracter in cadena:
        if caracter in vocales:
            cadena = cadena.replace(caracter,"")
    return cadena

def sin_consonantes(cadena):
    consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
    for caracter in cadena:
        if caracter in consonantes:
            cadena = cadena.replace(caracter,"")
    return cadena
    

def vocales_mayus(cadena):
    nueva_cadena = ""
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    for caracter in cadena:
        if caracter in vocales:
            nueva_cadena += caracter.upper()
        else:
            nueva_cadena += caracter
    return nueva_cadena

if __name__=="__main__":
    
    cadena = input("Introduce una cadena: ")

    print("Cadena sin vocales:",sin_vocales(cadena))
    print("Cadena sin consonantes:",sin_consonantes(cadena))
    print("Cadena con vocales en mayusculas:",vocales_mayus(cadena))