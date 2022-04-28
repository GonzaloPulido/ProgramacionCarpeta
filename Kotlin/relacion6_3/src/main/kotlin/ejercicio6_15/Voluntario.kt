package ejercicio6_15

data class Voluntario(var nombre: String, var edad: Int, var dni: String) {

    override fun toString(): String {
        return "Nombre = '$nombre', Edad = $edad DNI = '$dni'"
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Voluntario) return false

        if (dni != other.dni) return false

        return true
    }

    override fun hashCode(): Int {
        return dni.hashCode()
    }


}
