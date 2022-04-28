fun main() {
    println("Hello World!")
    var numero: Int
    while (true){
        try {
            print("Dame un numero: ")
            numero = readLine()!!.toInt()
            break
        } catch (e: Exception){
            println("Eso no es un numero")
        }
    }
    // Convertir a valor numerico
    numero += 7
    println("Has introducido $numero")
}