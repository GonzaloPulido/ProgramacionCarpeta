package relacion_5_3

import org.junit.jupiter.api.Test



internal class Ejercicio_5_13KtTest {

    @Test
    fun codigoMorse() {

        assert(codigoMorse("Gonzalo") == "--.----.--...-.-..---")
        assert(codigoMorse("Estoy aprobado") == "....-----.-- .-.--..-.----....--..---")
    }
}