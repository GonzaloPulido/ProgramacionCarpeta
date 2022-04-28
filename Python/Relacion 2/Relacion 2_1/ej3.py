while True:
    try: 
        puntuacion = float(input("Introduce una puntuacion entre 0.0 y 1.0: "))
        if puntuacion >= 0.0 and puntuacion <=1.0:
            break
        else:
            print("La puntuacion esta fuera de rango")
    except ValueError:
        print("Parece que el dato introducido no es valido")

print("""
--------- Tabla De Notas ---------
Puntuación      Calificación
>= 0.9          Sobresaliente
>= 0.8          Notable
>= 0.7          Bien
>= 0.6          Suficiente
< 0.6           Insuficiente
----------------------------------
""")

if puntuacion >= 0.9:
    print("Tienes un Sobresaliente")
elif puntuacion >= 0.8:
    print("Tienes un Notable")
elif puntuacion >= 0.7:
    print("Tienes un Bien")
elif puntuacion >= 0.6:
    print("Tienes un Suficiente")
else:
    print("Tienes un insuficiente")