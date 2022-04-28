package ejercicio_6_2

import java.lang.NumberFormatException

fun main(){
    while(true){
        try{
            println("Introduce el precio final del articulo: ")
            val precioFinal : Double = readLine()!!.toDouble()
            val iva = 10.0/100+1
            val precioSinIva = precioFinal/iva
            println("El IVA aplicado al producto es de ${precioFinal - precioSinIva}")
            println("El precio del producto sin iva es de $precioSinIva")
            break
        }catch (e: NumberFormatException){
            println("Debes introducir el precio con numeros")
        }
    }
}