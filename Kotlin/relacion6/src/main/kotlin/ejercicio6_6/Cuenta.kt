package ejercicio6_6

class Cuenta(var numeroCuenta: String, var saldo: Double, var titular: Cliente) {

    fun retirar (cantidad: Double){
        saldo -= cantidad
    }

    fun ingresar (cantidad: Double){
        if (cantidad > 0){
            saldo += cantidad
        }
    }

    override fun toString(): String {
        return "Tu numero de cuenta = '$numeroCuenta', Tu saldo = $saldo, Datos del titular -> [$titular]"
    }

}

