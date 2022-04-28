class ClienteNoRegistrado(var cartera: Double): Cliente {

    override fun aplicaDescuento(producto: Producto): Int {
        return producto.descuentoProducto
    }

    override fun pagar(cantidad: Double): Boolean {
        if (cartera >= cantidad){
            return true
        }
        return false
    }

}