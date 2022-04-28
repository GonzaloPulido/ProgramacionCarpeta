package ejercicio6_11

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ArmaFuegoTest {

    @Test
    fun cargar() {
        val arma1 = ArmaFuego(150.20)
        arma1.cargar()
        assert(arma1.cargada)

    }

    @Test
    fun disparar() {
        val arma1 = ArmaFuego(150.20)
        val arma2 = ArmaFuego(150.20, true)
        assert(!arma1.disparar())
        assert(arma2.disparar())
    }

    @Test
    fun atacar() {
        val arma1 = ArmaFuego(150.20)
        val arma2 = ArmaFuego(150.20, true)
        assert(arma2.atacar() == 150.20)
        assert(arma1.atacar() == 0.0)

    }
}