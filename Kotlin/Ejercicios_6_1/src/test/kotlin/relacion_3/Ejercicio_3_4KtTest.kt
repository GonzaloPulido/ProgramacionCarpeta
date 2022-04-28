package relacion_3

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class Ejercicio_3_4KtTest {

    @Test
    fun anyoBisiesto() {
        assert(anyoBisiesto(2020))
        assert(!anyoBisiesto(2001))

    }
}