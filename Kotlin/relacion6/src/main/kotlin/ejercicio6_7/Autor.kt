package ejercicio6_7

data class Autor(var nombre: String, var edad : Int) {
    override fun toString(): String {
        return "Nombre = '$nombre', Edad = $edad"
    }
}