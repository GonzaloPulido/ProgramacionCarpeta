package ejercicio6_14

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class GrupoTest {

    @Test
    fun registra() {
        val cliente = Cliente("Gonzalo","Pulido",21,323123123)
        val cliente2 = Cliente("Gonzalo","Pulido",21,323123123)
        val cliente3 = Cliente("Ale","Cancelo",21,323123123)
        val proveedor = Proveedor("El Perico","S.A.",20,"A275M")
        val grupo = Grupo(arrayListOf(cliente,proveedor))


        assert(!grupo.registra(cliente2))
        assert(grupo.registra(cliente3))

    }

    @Test
    fun elimina() {
        val cliente = Cliente("Gonzalo","Pulido",21,323123123)
        val cliente2 = Cliente("Gonzalo","Pulido",21,323123123)
        val proveedor = Proveedor("El Perico","S.A.",20,"A275M")
        val grupo = Grupo(arrayListOf(cliente,proveedor))

        assert(grupo.elimina(cliente))
        assert(!grupo.elimina(cliente2))
    }
}