package relacion_4

import org.junit.jupiter.api.Test


internal class Ejercicio_4_7KtTest {

    @Test
    fun divisionSucesiva() {
        assert(divisionSucesiva(20,2) == arrayListOf<Int>(10,0))
        assert(divisionSucesiva(30,7) == arrayListOf<Int>(4,2))
    }
}