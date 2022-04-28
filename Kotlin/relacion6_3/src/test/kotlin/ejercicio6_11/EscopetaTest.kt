package ejercicio6_11

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class EscopetaTest {

    @Test
    fun atacar() {
        val escopeta = Escopeta(true,25.20,200.0)
        val escopeta1 = Escopeta(false,25.20,200.0)

        assert(escopeta.atacar() == 225.20)
        assert(escopeta1.atacar()== 200.0)
    }

}