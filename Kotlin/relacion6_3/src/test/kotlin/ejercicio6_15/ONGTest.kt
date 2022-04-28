package ejercicio6_15

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ONGTest {

    @Test
    fun siguiente() {
        val voluntario = Voluntario("Gonzalo",21,"32906740L")
        val voluntario2 = Voluntario("Jose Antonio",20,"33064540X")
        val voluntario3 = Voluntario("Enzo",7,"32912789H")

        val lista = ONG(arrayListOf(voluntario,voluntario2,voluntario3))
        val lista2 = ONG(arrayListOf())

        assert(lista.siguiente() == voluntario)
        assert(lista.siguiente() == voluntario3)
        assert(lista2.siguiente() == null)

    }

    @Test
    fun registrar() {
        val voluntario = Voluntario("Gonzalo",21,"32906740L")
        val voluntario2 = Voluntario("Jose Antonio",20,"33064540X")
        val voluntario3 = Voluntario("Gonzalo",21,"32906740L")

        val lista = ONG(arrayListOf(voluntario,voluntario2))

        assert(!lista.registrar(voluntario3))
    }
}