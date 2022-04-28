package relacion_5_2

import org.junit.jupiter.api.Test



internal class Ejercicio_5_10KtTest {

    @Test
    fun palindromos() {
        val lista: ArrayList<String> = arrayListOf("reconocer","sometemos","luis","gonzalo")
        val lista2: ArrayList<String> = arrayListOf("ama","aerea","radar","gonzalo")
        assert(palindromos(lista)== arrayListOf("reconocer","sometemos"))
        assert(palindromos(lista2)== arrayListOf("ama","aerea","radar"))

    }
}