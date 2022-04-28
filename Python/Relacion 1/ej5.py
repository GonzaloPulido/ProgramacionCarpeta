while True:
    try:
        importe_sin_iva = float(input("Introduce el precio sin iva del producto: "))
        iva = float(input("Introduce el iva que vayas a aplicare: "))
        break
    except ValueError:
        print("El dato introducido debe ser con numeros")

iva_aplicar = importe_sin_iva * iva / 100
precio_final = importe_sin_iva + iva_aplicar

print('El precio final del producto es',precio_final,"€")