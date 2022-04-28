package ejercicio6_11

open class ArmaFuego(potencia: Double, var cargada: Boolean = false): Arma(potencia) {
    override fun toString(): String {
        return "Cargada = $cargada"
    }

    open fun cargar(){
        cargada = true
    }

    open fun disparar(): Boolean{
        if (cargada){
            cargada = false
            return true
        }
        return false
    }

    override fun atacar(): Double{
        if (disparar()){
            return potencia
        }
        return 0.0
    }

}

