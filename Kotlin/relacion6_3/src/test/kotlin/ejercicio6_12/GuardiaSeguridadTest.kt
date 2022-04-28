package ejercicio6_12

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class GuardiaSeguridadTest {

    @Test
    fun cobrar() {
        val empleado = GuardiaSeguridad("Gonzalo", 1000.0, 1, 20.0)
        val empleado1 = GuardiaSeguridad("Gonzalo", 1000.0,0,20.0)
        assert(empleado.cobrar() == 1020.0)
        assert(empleado1.cobrar()== 1000.0)

    }
}