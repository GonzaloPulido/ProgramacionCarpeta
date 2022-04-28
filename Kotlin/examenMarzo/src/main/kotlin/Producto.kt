abstract class Producto(var titulo: String, var precio: Double, var anyoPublicacion: Int, var descuentoProducto: Int = 0) {



    open fun obtenerDescuento(): Int{
        return descuentoProducto
    }

    override fun toString(): String {
        return "Titulo = '$titulo', Precio = $precio, Año publicacion = $anyoPublicacion, Descuento producto = $descuentoProducto"
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Producto) return false

        if (titulo != other.titulo) return false
        if (precio != other.precio) return false
        if (anyoPublicacion != other.anyoPublicacion) return false
        if (descuentoProducto != other.descuentoProducto) return false

        return true
    }

    override fun hashCode(): Int {
        var result = titulo.hashCode()
        result = 31 * result + precio.hashCode()
        result = 31 * result + anyoPublicacion
        result = 31 * result + descuentoProducto
        return result
    }

}