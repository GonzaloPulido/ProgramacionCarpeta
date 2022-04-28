package ejercicio6_8
import kotlin.math.pow
import kotlin.math.sqrt

class Bola(var circulo: Cirulo) {
    override fun toString(): String {
        return "Bola -> Circulo = $circulo)"
    }

    fun colision(bola:Bola, bola1:Bola): Boolean{
        val x1 = bola.circulo.centro.x
        val x2 = bola1.circulo.centro.x
        val y1 = bola.circulo.centro.y
        val y2 = bola1.circulo.centro.y

        val distanciaPuntos = sqrt((x2 - x1).toDouble().pow(2.0) + (y2 - y1).toDouble().pow(2.0))

        return distanciaPuntos < (bola.circulo.radio+bola1.circulo.radio)
    }
}