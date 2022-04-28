package ejercicio6_11

open class ArmaBlanca(var afilada: Boolean, var reduccionSinAfilar: Double, potencia: Double): Arma(potencia) {

    init{
        require(reduccionSinAfilar > 0.0) {"La reduccion al no estar afilada debe ser mayor que 0"}
    }

    override fun toString(): String {
        return "Afilada = $afilada, Reduccion sin afilar = $reduccionSinAfilar"
    }

    open fun afilar(){
        afilada = true
    }

    override fun atacar(): Double{
        return if (afilada){
            potencia
        }else{
            potencia - reduccionSinAfilar
        }

    }

}