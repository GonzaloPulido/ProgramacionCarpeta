package ejercicio6_14

class Proveedor (nombre: String, apellidos:String, edad: Int, var codigo: String): Persona(nombre,apellidos,edad) {

    override fun toString(): String {
        return super.toString() + ", Codigo = '$codigo'"
    }
}