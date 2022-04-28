package ejercicio6_11

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ArmaBlancaTest {

    @Test
    fun afilar() {
        val cuchillo = Cuchillo(false,10.0,30.0)
        cuchillo.afilar()
        assert(cuchillo.afilada)


    }

    @Test
    fun atacar() {
        val cuchillo = Cuchillo(false,10.0,30.0)
        val cuchillo1 = Cuchillo(true,20.0,30.0)
        assert(cuchillo.atacar() == 20.0)
        assert(cuchillo1.atacar() == 30.0)
    }
}