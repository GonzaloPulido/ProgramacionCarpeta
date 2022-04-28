package ejercicio6_8

fun main(){
    val punto1 = Punto(3,5)
    val punto2 = Punto(2,9)
    val circulo1 = Cirulo(3, punto1)
    val circulo2 = Cirulo(8,punto2)
    val bola1 = Bola(circulo1)
    val bola2 = Bola(circulo2)

    println(circulo1)
    println(circulo2)
    println(circulo1.calculaDiametro())
    println(circulo1.calculaLongitud())
    println(circulo2.calculaDiametro())
    println(circulo2.calculaLongitud())
    println(bola1.colision(bola1,bola2))


}