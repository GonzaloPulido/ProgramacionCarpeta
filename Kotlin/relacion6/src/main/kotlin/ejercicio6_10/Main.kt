package ejercicio6_10

fun main(){
    val soldado1 = Soldado("Gonzalo", "Tierra", 200)
    val soldado2 = Soldado("Peri", "Mar", 100)
    val soldado3 = Soldado("Ale", "Aire", 50)
    val escuadron: Escuadron = Escuadron(arrayListOf(soldado1,soldado2,soldado3))

    println(escuadron.potenciaFuego())



}