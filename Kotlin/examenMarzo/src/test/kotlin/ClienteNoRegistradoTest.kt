import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ClienteNoRegistradoTest {

    @Test
    fun aplicaDescuento() {
        val cliente = ClienteNoRegistrado(200.0)
        val disco = Disco("ACDC",10.25, 2001,2,GeneroMusica.Rock,"ACDC",5)

        assert(cliente.aplicaDescuento(disco) == 2)

    }

    @Test
    fun pagar() {
        val cliente = ClienteNoRegistrado(200.0)
        val cliente2 = ClienteNoRegistrado(100.0)
        assert(!cliente.pagar(400.0))
        assert(cliente2.pagar(100.0))
    }
}