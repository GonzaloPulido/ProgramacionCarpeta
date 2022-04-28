package ejercicio6_12

class Comercial(nombre: String, sueldo: Double, var ventas: Double = 0.0, var comision: Double = 0.0): Empleado(nombre,sueldo) {

    init {
        require(ventas >= 0.0) {"No puede haber menos de 0 ventas"}
        require(comision >= 0) {"No puede haber comision menor que 0"}
    }

    override fun toString(): String {
        return "Ventas = $ventas, Comision = $comision"
    }

    override fun cobrar(): Double {
        return sueldo + ventas * comision
    }

    fun vende(importe: Double){
        ventas += importe

    }
}