package ejercicio_6_4

fun main(){
    println("""
--------- MENU ---------
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
------------------------
    """)
    while(true){
        try{
             println("Introduce la opcion que desees de nuestra calculadora: ")
             val opcion : Int = readLine()!!.toInt()
             if (opcion in 1..4){

                 println("Introduce el primer numero: ")
                 val numero1 : Float = readLine()!!.toFloat()
                 println("Introduce el segundo numero: ")
                 val numero2 : Float = readLine()!!.toFloat()

                 // Error Division entre 0
                 if (opcion == 4 && numero2 <= 0){
                     println("No se puede dividir entre 0")
                 }else{

                     if (opcion == 1){
                         println("La suma de los dos numeros es: ${numero1+numero2}")
                         break
                     }else if (opcion == 2){
                         println("La resta de los dos numeros es: ${numero1 - numero2}")
                         break
                     }else if (opcion == 3){
                         println("El producto de los dos numeros es: ${numero1 * numero2}")
                         break
                     }else{
                         println("El cociente de los dos numeros es: ${numero1 / numero2}")
                         break
                     }
                 }
             }else{
                 println("No existe esa opcion en el menu")
             }
         }catch (e: NumberFormatException){
             println("Debes introducir los datos con numeros")
         }
    }
}