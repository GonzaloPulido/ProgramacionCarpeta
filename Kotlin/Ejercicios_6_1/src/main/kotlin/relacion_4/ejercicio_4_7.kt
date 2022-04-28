package relacion_4

fun divisionSucesiva (dividendo: Int, divisor: Int): ArrayList<Int> {
    var contador = 0
    var dividendo2 = dividendo

    while (dividendo2 >= divisor){
        dividendo2 -= divisor
        contador += 1
    }

    return arrayListOf(contador,dividendo2)

}

fun main(){
    println(divisionSucesiva(10,5))
}
