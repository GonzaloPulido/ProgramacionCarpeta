package relacion_4

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class Ejercicio_4_4KtTest {

    @Test
    fun listaNumeros() {
        val listaEjemplo : ArrayList<Int> = arrayListOf(1,3,-5,7,2,4,-6,8)
        val listaEjemplo2 : ArrayList<Int> = arrayListOf(7,-2,4,-6,8)
        assert(listaNumeros(listaEjemplo) == arrayListOf(14,6,2))
        assert(listaNumeros(listaEjemplo2) == arrayListOf(11,3,2))

    }
}