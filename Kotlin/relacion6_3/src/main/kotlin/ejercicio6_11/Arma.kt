package ejercicio6_11

open class Arma(var potencia: Double){
    init{
        require(potencia > 0.0) {"La potencia debe ser mayor que 0"}
    }

    override fun toString(): String {
        return "Potencia = $potencia"
    }

    open fun atacar(): Double{
        return potencia
    }


}