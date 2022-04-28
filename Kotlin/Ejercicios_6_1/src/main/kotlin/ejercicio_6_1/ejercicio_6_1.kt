package ejercicio_6_1

import java.lang.NumberFormatException

fun main(){
    while(true) {
        try {
            println("Introduce las horas de trabajo: ")
            val horasTrabajo: Int = readLine()!!.toInt()
            println("Introduce el precio por cada hora trabajada: ")
            val precioHoras: Int = readLine()!!.toInt()
            println("Vas a cobrar ${horasTrabajo * precioHoras}")
            break
        } catch (e: NumberFormatException) {
            println("El dato debe ser un numero")
        }
    }
}