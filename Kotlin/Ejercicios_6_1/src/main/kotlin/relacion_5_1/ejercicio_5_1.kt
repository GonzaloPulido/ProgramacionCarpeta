package relacion_5_1


fun sinVocales(cadena:String): String {
    val listaVocales = arrayListOf('a','A','e','E','i','I','o','O','u','U')
    var cadenaResultado = ""

    for (letra in cadena) {
        if (letra !in listaVocales) {
            cadenaResultado += letra
        }
    }

    return cadenaResultado
}

fun sinConsonantes(cadena: String): String{
    val listaConsonantes = arrayListOf('b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z')
    var cadenaResultado = ""

    for (letra in cadena) {
        if (letra !in listaConsonantes) {
            cadenaResultado += letra
        }
    }

    return cadenaResultado

}

fun vocalesMayus(cadena: String): String{
    val listaVocales = arrayListOf('a','A','e','E','i','I','o','O','u','U')
    var cadenaResultado = ""

    for (letra in cadena) {
        if (letra in listaVocales) {
            cadenaResultado += letra.uppercase()
        }else{
            cadenaResultado += letra
        }
    }

    return  cadenaResultado



}


fun main(){

    val palabraEjemplo = "Gonzalo"

    println(sinVocales(palabraEjemplo))
    println(sinConsonantes(palabraEjemplo))
    println(vocalesMayus(palabraEjemplo))

}

