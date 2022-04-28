package ejercicio6_7

fun main(){
    val autor1 = Autor("Gonzalo", 21)
    val autor2 = Autor("Gonzalo", 21)
    val libro1 = Libro("El gitano jerezano", 250, arrayListOf(autor1,autor2))
    val libro2 = Libro("El programador payo", 180, arrayListOf(autor2))


    println(libro1)
    println(libro2)

}