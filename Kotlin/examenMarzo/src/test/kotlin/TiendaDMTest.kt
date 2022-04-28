import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class TiendaDMTest {

    @Test
    fun buscaDisco() {
        val disco = Disco("ACDC",10.25, 2001,2,GeneroMusica.Rock,"ACDC",5)
        val disco1 = Disco("El gonza",10.20, 2021,2,GeneroMusica.Metal,"El gonzalillo",1)
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,)
        val client2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0,)
        val tiendaDM = TiendaDM(arrayListOf(disco), arrayListOf(cliente,client2))
        assert(tiendaDM.buscaDisco(disco))
        assert(!tiendaDM.buscaDisco(disco1))
    }

    @Test
    fun buscaPelicula() {

        val pelicula = Pelicula("Cars", 13.0,2010, 0,GeneroPelicula.Animacion,"El maquinon")
        val pelicula1 = Pelicula("El tio", 15.0,2000, 0,GeneroPelicula.Accion,"Gitano")
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,)
        val client2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0,)
        val tiendaDM = TiendaDM(arrayListOf(pelicula), arrayListOf(cliente,client2))
        assert(tiendaDM.buscaPelicula(pelicula))
        assert(!tiendaDM.buscaPelicula(pelicula1))
    }

    @Test
    fun compraPelicula() {

        val pelicula = Pelicula("Cars", 13.0,2010, 0,GeneroPelicula.Animacion,"El maquinon")
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,)
        val client2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0,)
        val tiendaDM = TiendaDM(arrayListOf(pelicula), arrayListOf(cliente,client2))

        assert(tiendaDM.compraPelicula(3,pelicula) == 39.0)
    }

    @Test
    fun compraDisco() {
        val disco = Disco("ACDC",10.25, 2001,2,GeneroMusica.Rock,"ACDC",5)
        val disco1 = Disco("El gonza",10.20, 2021,2,GeneroMusica.Metal,"El gonzalillo",1)
        val cliente = ClienteRegistrado("Gonzalo", "Pulido", "32906740L", "691270867", 200.0,)
        val client2 = ClienteRegistrado("Ale", "Cancelo", "32923740L", "691279067", 100.0,)
        val tiendaDM = TiendaDM(arrayListOf(disco), arrayListOf(cliente,client2))

        assert(tiendaDM.compraDisco(3,disco) == 30.75)
    }
}