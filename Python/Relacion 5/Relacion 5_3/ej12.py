def teclado_movil(cadena):
    resultado = []
    caracteres = {'.':1,',':11,'?':111,'!':1111,':':11111,'A':2,'B':22,'C':222,'D':3,'E':33,'F':333,'G':4,'H':44,'I':444,'J':5,'K':55,'L':555,'M':6,'N':66,'Ñ':666,'O':6666,'P':7,'Q':77,'R':777,'S':7777,'T':8,'V':88,'U':888,'W':9,'X':99,'X':99,'Y':999,'Z':9999,' ':0}
    cadena = cadena.upper()
    for valor in cadena:
        if valor in caracteres.keys():
            resultado.append(caracteres[valor])
    return resultado        

if __name__=="__main__":
    cadena = input('Introduce una cadena: ')

    print('Necesitas pulsar las siguientes teclas:',teclado_movil(cadena))
