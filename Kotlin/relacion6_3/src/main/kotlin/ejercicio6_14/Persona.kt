package ejercicio6_14

abstract class Persona(var nombre: String, var apellidos:String, var edad: Int) {



    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Persona) return false

        if (nombre != other.nombre) return false
        if (apellidos != other.apellidos) return false
        if (edad != other.edad) return false

        return true
    }

    override fun hashCode(): Int {
        var result = nombre.hashCode()
        result = 31 * result + apellidos.hashCode()
        result = 31 * result + edad
        return result
    }

    override fun toString(): String {
        return "Nombre = '$nombre', Apellidos = '$apellidos', Edad = $edad"
    }
}