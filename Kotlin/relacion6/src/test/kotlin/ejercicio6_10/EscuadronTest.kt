package ejercicio6_10

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class EscuadronTest {

    @Test
    fun potenciaFuego() {
        val soldado1 = Soldado("Gonzalo", "Tierra", 200)
        val soldado2 = Soldado("Peri", "Mar", 100)
        val soldado3 = Soldado("Ale", "Aire", 50)
        val soldado4 = Soldado("Meddy", "Tierra", 80)
        val soldado5 = Soldado("Nando", "Mar", 20)
        val soldado6 = Soldado("Aser", "Aire", 60)
        val escuadron: Escuadron = Escuadron(arrayListOf(soldado1,soldado2,soldado3,soldado4,soldado5,soldado6))


        assert(escuadron.potenciaFuego() == 510.0.toFloat())
    }
}