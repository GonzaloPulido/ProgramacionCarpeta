package ejercicio6_12

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ComercialTest {

    @Test
    fun cobrar() {
        val comercial = Comercial("GOnzalo", 1000.0, 25.0, 2.0)
        val comercial1 = Comercial("GOnzalo", 1000.0, 0.0, 2.0)
        assert(comercial.cobrar() == 1050.0)
        assert(comercial1.cobrar() == 1000.0)


    }

    @Test
    fun vende() {
        val comercial = Comercial("GOnzalo", 1000.0, 0.0, 2.0)
        comercial.vende(25.0)
        assert(comercial.ventas == 25.0)
    }
}