package ejercicio6_8

import kotlin.math.PI

class Cirulo(var radio: Int, var centro: Punto) {

    override fun toString(): String {
        return "Radio = $radio, Centro -> [ $centro ])"

    }

    fun calculaDiametro(): Int{
        return radio * 2
    }

    fun calculaLongitud(): Double{
        return 2*Math.PI*radio
    }

}