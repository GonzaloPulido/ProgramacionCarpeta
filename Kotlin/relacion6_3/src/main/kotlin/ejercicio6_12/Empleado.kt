package ejercicio6_12

open class Empleado(var nombre: String, var sueldo: Double) {

    init {
        require(sueldo > 0.0) {"EL sueldo debe ser mayor que 0"}
    }


    open fun cobrar(): Double{
        return sueldo
    }

    override fun toString(): String {
        return "Nombre = '$nombre', Sueldo = $sueldo"
    }

}