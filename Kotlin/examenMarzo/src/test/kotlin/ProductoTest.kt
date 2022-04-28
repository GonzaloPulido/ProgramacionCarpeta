import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class ProductoTest {

    @Test
    fun obtenerDescuento() {
        val disco = Disco("ACDC",10.25, 2001,2,GeneroMusica.Rock,"ACDC",5)
        val pelicula = Pelicula("Cars", 13.0,2010, 0,GeneroPelicula.Animacion,"El maquinon")

        assert(disco.obtenerDescuento() == 2)
        assert(pelicula.descuentoProducto == 0)
    }
}