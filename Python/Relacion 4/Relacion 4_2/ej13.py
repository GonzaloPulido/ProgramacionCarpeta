def precio_viaje(distancia,dias):
    if dias > 7 and distancia * 2 > 800:
        precio = distancia * 2 * 10 * 0.3
    else:
        precio = distancia * 2 * 10
    
    return precio