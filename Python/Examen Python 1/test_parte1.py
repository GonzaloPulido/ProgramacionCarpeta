import pytest
from parte1 import filtra_ejercicios,duracion_ejercicios,entrenamiento,ejercicios
lista1 = [{'denominacion': 'Balón-azúcar', 'descripcion': '4x1. Quien la para sólo puede pillar al jugador que no está en posesión de balón.\nAcotar el terreno de juego.', 'estrategia': ['Anticipar.', 'Fintar', 'Apoyar la línea de pase.', 'Crear exigencias antes de poder pasar y delimitar espacios.'], 'duracion': 10}, {'denominacion': 'Entrar con llave', 'descripcion': 'Pasar al recién cambiado que llega al centro con balón.\nNecesitamos 1 balón y los aros.', 'estrategia': ['Siempre en movimiento.', 'Acción para el otro.', 'Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.', 'Enriquecer con cortes y su defensa. Chocar los cortes.'], 'duracion': 10}, {'denominacion': 'Sin parar', 'descripcion': '4x4, 5x5\nPase al jugador interior e intercambio de posiciones.', 'estrategia': ['Interior / Exterior.', 'Reemplazar.', 'Ganar la entrada del balón en el juego interior.', 'Pasar y seguir.'], 'duracion': 10}, {'denominacion': 'Las alianzas', 'descripcion': '4 x 2 + 2.\n4 atacantes intentan tocar con el balón adaptado a 2.\nDos defensores se lo impiden.', 'estrategia': ['Intercepciones de pases.', 'Buscarse apoyos'], 'duracion': 10}, {'denominacion': 'Vuelvete loco', 'descripcion': 'Dos parejas se pasan y mueven defendidas por uno en cancha.\nDos balones a la vez.', 'estrategia': ['Amplitud visual.', 'Variedad de pases', 'Exigencias.'], 'duracion': 10}, {'denominacion': 'Enjaulados', 'descripcion': '2 x 1. Los defensores no pueden sacar los dos pies de los círculos.\nFacilitar el ataque acotando los movimientos de los defensores.\nApoyar la defensa creando exigencias nuevas en los pases.', 'estrategia': ['Negar las líneas de pase.', 'Analizar los pases y las recepciones en carrera.', 'Fintas de pase y puertas atrás'], 'duracion': 10}, {'denominacion': 'No al vecino', 'descripcion': '6 x 1 con dos balones\n7 x 3 y un balón\nNo podemos pasar el balón al compañero vecino.', 'estrategia': ['Visión periférica.', 'Elección de pase.', 'Selección de pases.', 'Fintas defensivas y engaños de pase.'], 'duracion': 10}, {'denominacion': 'Los intocables', 'descripcion': '4 x 5. El quinteto defensor intercepta: ni tocan ni desposeen.\nBuscamos los 2 x 1 y un sentido de presión.', 'estrategia': ['Dos al balón.', 'No telegrafiamos los pases.'], 'duracion': 10}, {'denominacion': 'Más dificil', 'descripcion': '4 x 3 buscan canasta. Cobran punto cada vez que logran su propósito en un número corto de acciones.\nSuperado el número, cambio de posesión.\nToda la cancha', 'estrategia': ['Ver huecos.', 'Cambios de ritmo.', 'Cambios de dirección.'], 'duracion': 10}, {'denominacion': 'Laberinto', 'descripcion': 'A persigue a B favorecido por los brazos que cambian de agarre creando diversos pasillos botando estáticos (en aro, en neumático,...)', 'estrategia': ['Discriminar la ayuda y la protección.', 'Atender los cambios.'], 'duracion': 10}, {'denominacion': 'Dos en apuros', 'descripcion': 'Dos botando quieren juntarse y el defensor no les deja.\nUsar claves de números, colores,... buscando el retener, el centrarse.', 'estrategia': ['Defensa activa y toma de decisiones.', 'Pelea por el balón.', 'Fintas en bote.', 'Memoria y atención.'], 'duracion': 10}, {'denominacion': 'Ayuda', 'descripcion': 'Aguantando el balón en 1 x 1 pasamos a un tercer jugador y saltamos a iniciar el nuevo 1 x 1.', 'estrategia': ['Protección del balón.', 'Flexibilidad de acciones.', 'Sentir la defensa y sellar su paso.'], 'duracion': 10}, {'denominacion': 'Persecución', 'descripcion': 'Las parejas evolucionan por la cancha pasándose el balón. A la señal quien esté en posesión del balón buscará meter canasta. El otro defenderá.', 'estrategia': ['Repaso de pases.', 'Calidad y distancia.', 'Espacio restringido/abierto/colisión'], 'duracion': 10}, {'denominacion': 'Waterloo', 'descripcion': 'Dos equipos cambian de lado botando sus componentes cada uno su balón y venciendo la oposición de un tercer equipo que se mueve por el espacio entre lado y lado.\n1 punto por equipo que primero se reúne.\nLogrados x puntos el vencedor cambia al medio.', 'estrategia': ['Visión en el bote.', 'Atacar botando contra todos.', 'Pelea y dificulta el logro de los demás.', 'Intensidad al fijar al atacante'], 'duracion': 10}, {'denominacion': 'Pasar y seguir', 'descripcion': '1 x 1 desde media cancha y con dos postes repetidores.', 'estrategia': ['Pasar y seguir.', 'Negar el pase de vuelta'], 'duracion': 10}, {'denominacion': 'Seis conquistas', 'descripcion': 'Dividida la zona en sub-espacios buscamos con la colaboración de un pasador el recibir en cada una de ellas.', 'estrategia': ['Memoria.', 'Lucha por recibir.'], 'duracion': 10}, {'denominacion': 'Balón suicida', 'descripcion': 'En media cancha 5 x 1. El que pilla busca tocar al jugador con balón que aguantará al bote o le exigiremos acciones antes de pasar.', 'estrategia': ['Recibir en movimiento.', 'Anticipar.'], 'duracion': 10}, {'denominacion': 'El zorro, la gallina y los polluelos', 'descripcion': 'El zorro, la gallina y el polluelo último llevan balón al bote.\nEl zorro trata de tocar al último polluelo.', 'estrategia': ['Dominios del bote.', 'Extrema colaboración.', 'Estrategias de ruptura del grupo familiar.'], 'duracion': 10}, {'denominacion': 'Sardana atrapo', 'descripcion': '4 cogidos de la mano protegen al ratón de ser pillado por el gato que juegan botando cada uno su balón.', 'estrategia': ['Buscamos el trabajo de pies en la defensa.', 'Todos pelean todo.', 'Cambios bien continuados y organizados.'], 'duracion': 10}, {'denominacion': 'Ring', 'descripcion': 'El jugador en posesión del balón debe evitar ser tocado por el defensor. Lo evita al dejar el balón en el suelo y salir a tocar la línea de banda. El defensor copiará sus movimientos.', 'estrategia': ['Visión.', 'Anticipación', 'Engaños.', 'Cambios de ritmo.'], 'duracion': 10}]


def test_filtra_ejercicios():
    assert len(filtra_ejercicios(ejercicios,10)) == 20
    assert len(filtra_ejercicios(ejercicios,20)) == 30
    assert len(filtra_ejercicios(ejercicios,30)) == 33

def test_duracion_ejercicios():
    assert duracion_ejercicios(ejercicios) == 490
    assert duracion_ejercicios(lista1) == 200


# --------- JAVI NO SE HACER EL TEST DE ESTA FUNCION ---------

# def test_ejercicios():
#     lista_ejercicios = ejercicios(ejercicios,90)
#     contador = 0
#     for x in lista_ejercicios:
#         contador += x["duracion"] 

#     assert sum(ejercicios(ejercicios,90)["duracion"]) == contador

# --------- JAVI NO SE HACER EL TEST DE ESTA FUNCION ---------





    

    
