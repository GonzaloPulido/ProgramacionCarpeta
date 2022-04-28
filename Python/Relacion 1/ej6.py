while True:
    try:
        importe_final = float(input("Introduce el precio final del producto: "))
        break
    except ValueError:
        print("El dato introducido debe ser con numeros")

iva = 10/100+1
precio_sin_iva = importe_final / iva

print("El iva aplicado es de",round(importe_final-precio_sin_iva,2),"€\nEl precio sin iva es de",round(precio_sin_iva,2),"€")