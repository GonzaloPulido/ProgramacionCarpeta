package ejercicio6_6

data class Cliente(var nombre: String, var dni: String, var edad: Int) {
    override fun toString(): String {
        return "Nombre del cliente ='$nombre', DNI ='$dni', Edad =$edad"
    }

}