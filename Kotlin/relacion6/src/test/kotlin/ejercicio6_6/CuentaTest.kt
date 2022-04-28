package ejercicio6_6

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class CuentaTest {

    @Test
    fun retirar(){
        val cliente = Cliente("Gonzalo", "32906740L", 21)
        val cuenta = Cuenta("111", 550.0, cliente)
        cuenta.retirar(50.0)
        println(cuenta.saldo)
        assert(cuenta.saldo == 500.0)
    }

    @Test
    fun ingresar() {
        val cliente = Cliente("David", "32906740L", 21)
        val cuenta = Cuenta("1111", 550.20, cliente)
        cuenta.ingresar(50.0)
        assert(cuenta.saldo == 600.20)

    }
}