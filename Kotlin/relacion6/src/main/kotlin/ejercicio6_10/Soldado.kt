package ejercicio6_10

 data class Soldado(var nombre : String, var tipo: String, var potencia : Int) {
     override fun toString(): String {
         return "Nombre = '$nombre', Tipo = '$tipo', Potencia = $potencia"
     }
 }