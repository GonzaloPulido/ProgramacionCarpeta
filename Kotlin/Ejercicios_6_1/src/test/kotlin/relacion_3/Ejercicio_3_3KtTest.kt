package relacion_3

import org.junit.jupiter.api.Test



internal class Ejercicio_3_3KtTest {

    @Test
    fun distanciaPuntos(){
        assert(distanciaPuntos(1,1,1,1) == 0.0)
        assert(distanciaPuntos(1,2,3,4) == 1.4142135623730951)
        assert(distanciaPuntos(-1,3,-2,5) == 8.06225774829855)
    }
}