package ejercicio_6_3

fun main(){
    println("""
Puntuacion          Calificacion
>= 0.9              Sobresaliente
>= 0.8              Notable
>= 0.7              Bien
>= 0.6              Suficiente
< 0.6               Insuficiente
    """)
    while(true){
        try{
            println("Introduce una puntuacion entre 0.0 y 1.0: ")
            val puntuacion : Double = readLine()!!.toDouble()
            if (puntuacion in 0.0..1.0){
                if (puntuacion >= 0.9) {
                    println("Has obtenido un Sobresaliente")
                    break
                }else if (puntuacion >= 0.8) {
                    println("Has obtenido un Notable")
                    break
                }else if (puntuacion >= 0.7) {
                    println("Has obtenido un Bien")
                    break
                }else if (puntuacion >= 0.6) {
                    println("Has obtenido un Suficiente")
                    break
                }else {
                    println("Has obtenido un Insuficiente")
                    break
                }
            }else{
                println("La puntuacion esta fuera de rango")
            }
        }catch (e:NumberFormatException){
          println("Debes introducir la puntuacion con numeros")
        }
    }
}