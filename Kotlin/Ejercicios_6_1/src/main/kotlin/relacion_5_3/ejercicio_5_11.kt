package relacion_5_3

fun numeroLetras(cadena: String): HashMap<Char,Int>{
     val diccionarioResultado: HashMap<Char,Int> = hashMapOf()
     val cadenaMinus = cadena.lowercase()

    for (letra in cadenaMinus){
        if (letra in diccionarioResultado.keys){
            diccionarioResultado[letra] = diccionarioResultado[letra]!! + 1
        }else{
            diccionarioResultado[letra] = 1
        }

    }
    return diccionarioResultado

}

fun main(){

    println(numeroLetras("ElPeri"))

}

