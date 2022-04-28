package ejercicio6_11

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ArmaTest {

    @Test
    fun atacar() {
        val arma1 = Arma(100.10)

        assert(arma1.atacar() == 100.10)
    }
}