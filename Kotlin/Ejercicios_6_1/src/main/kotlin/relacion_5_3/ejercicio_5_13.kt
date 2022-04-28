package relacion_5_3

fun codigoMorse(texto: String): String{
    val textoMinus = texto.lowercase()
    val morse: HashMap<Char, String> = hashMapOf('a' to ".-",'b' to "-...",'c' to "-.-.", 'd' to "-..",'e' to ".",
        'f' to "..-.", 'g' to "--.", 'H' to "....",'i' to "..", 'j' to ".---", 'k' to "-.-",'l' to ".-..", 'm' to "--",
        'n' to "-.", 'o' to "---", 'p' to ".--.", 'q' to "--.-", 'r' to ".-.", 's' to "...", 't' to "-", 'u' to "..-",
        'v' to "...-", 'w' to ".--", 'x' to "-..-", 'y' to "-.--", 'z' to "--..", '0' to "-----", '1' to ".----",
        '2' to "..---", '3' to "...--", '4' to "....-", '5' to ".....", '6' to "-....", '7' to "--...",'8' to "---..",
        '9' to "----.")
    var cadenaResultado= ""

    for (caracter in textoMinus){
        cadenaResultado += if (caracter in morse){
            morse[caracter]
        }else{
            " "
        }
    }

    return cadenaResultado

}

fun main(){
    println(codigoMorse("Estoy aprobado"))

}