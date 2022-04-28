package relacion_5_1

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class Ejercicio_5_1KtTest {

    @Test
    fun sinVocales() {
        val palabraEjemplo = "Gonzalo"
        val palabraEjemplo2 = "Programacion"

        assert(sinVocales(palabraEjemplo) == "Gnzl")
        assert(sinVocales(palabraEjemplo2) == "Prgrmcn")

    }

    @Test
    fun sinConsonantes() {
        val palabraEjemplo = "Gonzalo"
        val palabraEjemplo2 = "Programacion"

        assert(sinConsonantes(palabraEjemplo) == "oao")
        assert(sinConsonantes(palabraEjemplo2) == "oaaio")
    }

    @Test
    fun vocalesMayus() {
        val palabraEjemplo = "Gonzalo"
        val palabraEjemplo2 = "Programacion"

        assert(vocalesMayus(palabraEjemplo) == "GOnzAlO")
        assert(vocalesMayus(palabraEjemplo2) == "PrOgrAmAcIOn")
    }
}