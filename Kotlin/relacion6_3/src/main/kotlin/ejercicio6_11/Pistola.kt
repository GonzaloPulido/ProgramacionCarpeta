package ejercicio6_11

class Pistola(var calibre: Int, potencia: Double): ArmaFuego(potencia) {

    init {
        require(calibre > 0) {"El calibre de tu pistola debe ser mayor que 0"}
    }

    override fun toString(): String {
        return "Calibre = $calibre"
    }


}