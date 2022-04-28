package ejercicio6_11

class Rifle(var alcance: Double,potencia: Double): ArmaFuego(potencia) {

    init{
        require(alcance > 0.0) {"El alcance de tu rifle debe ser mayor que 0"}
    }

    override fun toString(): String {
        return "Alcance = $alcance"
    }
}

