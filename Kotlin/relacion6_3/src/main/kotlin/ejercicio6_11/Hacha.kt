package ejercicio6_11

class Hacha(var filos: Int = 1, afilada: Boolean, reduccionSinAfilar: Double, potencia: Double ): ArmaBlanca(afilada,reduccionSinAfilar,potencia) {


    init {
        require(filos > 0) {"El hacha debe tener minimo un filo"}
    }

    override fun toString(): String {
        return "Filos = $filos"
    }

}