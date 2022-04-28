interface Cliente {

    fun aplicaDescuento(producto:Producto): Int
    fun pagar(cantidad: Double): Boolean
}