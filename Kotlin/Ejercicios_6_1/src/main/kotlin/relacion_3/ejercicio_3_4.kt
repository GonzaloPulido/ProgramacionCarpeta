package relacion_3

fun main(){
    println("Introduce el año que desees saber si es bisiesto: ")
    val anyo = readLine()!!.toInt()

    if (anyo > 0){
        if (anyoBisiesto(anyo)){
            println("$anyo es bisiesto")
        }else
            println("$anyo no es bisiesto")
    }else
        println("Ese año no existe")
}

fun anyoBisiesto(anyo: Int): Boolean{
    return anyo % 400 == 0 || anyo % 4 == 0 && anyo % 100 != 0
}
