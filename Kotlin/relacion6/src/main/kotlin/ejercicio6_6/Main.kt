package ejercicio6_6

fun main(){
    val cliente = Cliente("Gonzalo", "32906740L", 21)
    val cuenta = Cuenta("1111", 220.50, cliente)

    cuenta.retirar(200.0)
    println(cuenta)
    cuenta.ingresar(500.0)
    println(cuenta)

}