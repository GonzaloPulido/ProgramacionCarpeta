package ejercicio6_12

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class EmpleadoTest {

    @Test
    fun cobrar() {
        val empleado = Empleado("Gonzalo", 1000.0)

        assert(empleado.cobrar() == 1000.0)
    }
}