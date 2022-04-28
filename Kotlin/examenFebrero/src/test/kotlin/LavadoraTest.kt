import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class LavadoraTest {

    @Test
    fun precioFinal() {
        //Comprobacion Constructores
        val lavadora = Lavadora()
        val lavadora1 = Lavadora(200.0, 80.0)
        val lavadora2 = Lavadora(200.0, 80.0, "negro", 'A', 40.0)
        //Comprobacion Constructores

        //Comprobacion de los datos
        assertThrows(IllegalArgumentException::class.java) {
            val lavadora3 = Lavadora(0.0, 80.0, "negro", 'A', 10.0)
        }
        assertThrows(IllegalArgumentException::class.java) {
            val lavadora4 = Lavadora(100.0, 0.0, "negro", 'A', 10.0)
        }

        assertThrows(IllegalArgumentException::class.java) {
            val lavadora5 = Lavadora(100.0, 8.0, "amarillo", 'A', 10.0)
        }

        assertThrows(IllegalArgumentException::class.java) {
            val lavadora6 = Lavadora(100.0, 8.0, "negro", 'K', 10.0)

        }
        //Comprobacion de los datos

        // Comprobacion del metodo
        assert(lavadora.precioFinal() == 210.0 )
        assert(lavadora1.precioFinal() == 400.0 )
        assert(lavadora2.precioFinal() == 360.0 )









             }
    }