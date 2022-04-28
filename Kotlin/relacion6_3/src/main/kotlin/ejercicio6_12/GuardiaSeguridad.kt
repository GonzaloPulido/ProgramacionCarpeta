package ejercicio6_12

class GuardiaSeguridad(nombre: String,sueldo: Double, var noches: Int = 0, var extraNoche: Double): Empleado(nombre,sueldo) {

    init {
        require(noches >= 0) {"Las noches deben ser mayores o iguales a 0"}
        require(extraNoche >  0.0) {"Las horas extra se deben pagar a mas de 0 €"}
    }

    override fun toString(): String {
        return "Noches = $noches, Extra noche = $extraNoche"
    }

    override fun cobrar(): Double {

        return sueldo + (noches*extraNoche)
    }

}