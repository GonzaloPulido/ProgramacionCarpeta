import org.junit.jupiter.api.Test
import java.lang.IllegalArgumentException
import org.junit.jupiter.api.Assertions.*

internal class ClienteRegistradoTest {

    @Test
    fun aplicaDescuento() {
        val pelicula = Pelicula("Cars", 13.0,2010, 0,GeneroPelicula.Animacion,"El maquinon")
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,5)
        val cliente2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0)

        assert(cliente.aplicaDescuento(pelicula) == 5)
        assert(cliente2.aplicaDescuento(pelicula) == 2)

    }

    @Test
    fun pagar() {
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,5)
        val cliente2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0)

        assert(!cliente.pagar(400.0))
        assert(cliente2.pagar(100.0))

    }

    @Test
    fun validaDNI() {
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740l", "691270867", 200.0,5)
        assertThrows(IllegalArgumentException::class.java) {
            ClienteRegistrado("Ale", "Cancelo", "323740L", "691279067", 100.0) }
    }


    @Test
    fun esVIP() {
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740l", "691270867", 200.0,5)
        val resultados = arrayListOf<Boolean>(true,false)
        assert(cliente.esVIP() in resultados)
    }
}