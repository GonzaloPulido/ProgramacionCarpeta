package ejercicio6_14

class Cliente(nombre: String, apellidos:String, edad: Int, var id: Long): Persona(nombre,apellidos,edad) {
    override fun toString(): String {
        return super.toString() + ", Id = $id"
    }
}