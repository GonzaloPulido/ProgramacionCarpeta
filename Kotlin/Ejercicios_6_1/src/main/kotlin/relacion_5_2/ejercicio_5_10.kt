package relacion_5_2

fun palindromos(lista: ArrayList<String>): ArrayList<String>{
    val listaPalindromos: ArrayList<String> = ArrayList()

    for (palabra in lista){
        if (palabra == palabra.reversed()){
            listaPalindromos += palabra
        }
    }
    return listaPalindromos
}

fun main(){
    val lista: ArrayList<String> = arrayListOf("reconocer","sometemos","luis","gonzalo")
    println(palindromos(lista))
}