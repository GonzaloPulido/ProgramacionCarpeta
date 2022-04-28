package ejercicio6_11

class Escopeta(var recortada: Boolean, var aumentoRecortada: Double, potencia : Double): ArmaFuego(potencia) {

    init {
        require(aumentoRecortada > 0.0) {"El aumento debe ser mayor que 0"}
    }

    override fun toString(): String {
        return "Recortada = $recortada, Aumento de recortada = $aumentoRecortada"
    }

    override fun atacar(): Double{
        return if (recortada){
            potencia + aumentoRecortada
        }else{
            potencia
        }
    }


}