package ejercicio6_8

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class BolaTest {

    @Test
    fun colision() {
        val punto1 = Punto(3,5)
        val punto2 = Punto(2,9)
        val punto3 = Punto(-20,3)
        val punto4 = Punto(7,6)
        val circulo1 = Cirulo(3, punto1)
        val circulo2 = Cirulo(8,punto2)
        val circulo3 = Cirulo(7, punto3)
        val circulo4 = Cirulo(4,punto4)
        val bola1 = Bola(circulo1)
        val bola2 = Bola(circulo2)
        val bola3 = Bola(circulo3)
        val bola4 = Bola(circulo4)

        assert(bola1.colision(bola1,bola2))
        assert(!bola3.colision(bola3,bola4))


    }
}