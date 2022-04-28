package ejercicio6_10

class Escuadron(var soldados : ArrayList<Soldado>) {
    init {
        require(soldados.isNotEmpty()) {"Necesitamos almenos un soldado"}
    }

    override fun toString(): String {
        if (soldados.isEmpty()){
            throw Exception("Necesitamos almenos un soldado")
        }
        return "Escuadron -> [$soldados])"
    }

    fun potenciaFuego(): Float{
        var fuego = 0
        for (x in soldados){
            fuego += x.potencia
        }

        return fuego.toFloat()

    }
}