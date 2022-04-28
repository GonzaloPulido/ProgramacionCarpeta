package relacion_5_3

import org.junit.jupiter.api.Test


internal class Ejercicio_5_11KtTest {

    @Test
    fun numeroLetras() {
        assert(numeroLetras("Gonzalo") == hashMapOf('a' to 1, 'g' to 1, 'z' to 1, 'l' to 1, 'n' to 1, 'o' to 2))
        assert(numeroLetras("ElPeri") == hashMapOf('p' to 1, 'r' to 1, 'e' to 2, 'i' to 1, 'l' to 1))
    }
}