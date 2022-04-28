package relacion_5_1

import org.junit.jupiter.api.Test



internal class Ejercicio_5_5KtTest {




    @Test
    fun generarTablero() {
        val palabra = "alerones"
        assert(generarTablero(palabra) == arrayListOf<Char>('_','_','_','_','_','_','_','_'))
    }

    @Test
    fun comprobarLetra() {
        val palabra = "alerones"
        assert(comprobarLetra('a', palabra))
        assert(!comprobarLetra('u',palabra))
    }

    @Test
    fun actualizarTablero() {
        val tablero = arrayListOf<Char>('_','_','_','_','_','_','_','_')
        val palabra = "alerones"
        assert(actualizarTablero('a',tablero,palabra) == arrayListOf<Char>('a','_','_','_','_','_','_','_'))
    }

    @Test
    fun comprobarWin() {
        val win = arrayListOf<Char>('a','l','e','r','o','n','e','s')
        assert(comprobarWin(win))

    }
}