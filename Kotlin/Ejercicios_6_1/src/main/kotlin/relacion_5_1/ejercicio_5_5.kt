package relacion_5_1

fun elegirPalabras(listaPalabras: ArrayList<String>): String {

    return listaPalabras.random()

}

fun generarTablero(palabra: String) : ArrayList<Char>{

    val tablero : ArrayList<Char> = ArrayList()

    for (x in palabra){
        tablero += '_'
    }

    return  tablero
}

fun comprobarLetra(letra: Char,palabra: String): Boolean{
    return letra in palabra
}

fun actualizarTablero(letra: Char,tablero: ArrayList<Char>,palabra: String): ArrayList<Char> {
    var numero = 0

    for (x in palabra) {
        if (x == letra) {
            tablero[numero] = letra
            numero += 1
        } else {
            numero += 1
        }
    }
    return tablero
}

fun comprobarWin(tablero: ArrayList<Char>): Boolean{
    for (x in tablero) {
        if (x == '_') {
            return false
        }
    }
    return true
}

fun main(){
    val listaPalabras: ArrayList<String> = arrayListOf("cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana")
    val letrasFalladas: ArrayList<Char> = ArrayList()
    val palabra: String = elegirPalabras(listaPalabras)
    val tablero: ArrayList<Char> = generarTablero(palabra)
    var vidas = 5
    println("--------- AHORCADO ---------")
    while (true){
        if (vidas == 0){
            println("Lo sentimos, has pedido todas tus vidas")
            break
        }else if (comprobarWin(tablero)){
            println("¡¡¡HAS GANADO!!!")
            println("La palabra era $palabra")
            break
        }else{
            println("--------- DATOS DEL JUEGO ---------")
            println("Tu tablero: $tablero")
            println("Te quedan $vidas vidas")
            println("Letras falladas: $letrasFalladas")
            try{
                println("Introduce una letra: ")
                var letra: Char = readLine()!![0]
                letra = letra.lowercaseChar()
                if (comprobarLetra(letra,palabra)){
                    actualizarTablero(letra,tablero,palabra)
                }else{
                    letrasFalladas += letra
                    vidas -= 1
                    println("Has fallado")
                }
            }catch (e: NumberFormatException){
                println("Debes introducir una sola letra")
            }
        }
    }
}