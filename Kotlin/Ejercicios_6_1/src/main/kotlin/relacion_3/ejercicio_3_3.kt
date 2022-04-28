package relacion_3

import kotlin.math.pow
import kotlin.math.sqrt

fun main(){
    while(true){
        try{
            println("Introduce la posicion x1: ")
            val x1 :Int = readLine()!!.toInt()
            println("Introduce la posicion x2: ")
            val x2 :Int = readLine()!!.toInt()
            println("Introduce la posicion y1: ")
            val y1 :Int = readLine()!!.toInt()
            println("Introduce la posicion y2: ")
            val y2 :Int = readLine()!!.toInt()

            println(distanciaPuntos(x1,x2,y1,y2))
            break
        }catch (e: NumberFormatException){
            println("Debes introducir los datos con numeros")
        }
    }
}

fun distanciaPuntos(x1 : Int,x2: Int, y1 : Int,y2: Int): Double{

    return sqrt((x2 - x1).toDouble().pow(2.0) + (y2 - y1).toDouble().pow(2.0))
}
