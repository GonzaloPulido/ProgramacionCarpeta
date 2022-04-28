import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class TelevisorTest {

    @Test
    fun precioFinal() {
        val televisor = Televisor()
        val televisor1 = Televisor(200.0, 80.0)
        val televisor2 = Televisor(200.0, 80.0, "negro", 'A', 45.0)

        assert(televisor.precioFinal() == 210.0)
        assert(televisor1.precioFinal() == 400.0)
        assert(televisor2.precioFinal() == 403.0)

    }
}