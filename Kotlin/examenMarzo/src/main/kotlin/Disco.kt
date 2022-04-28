class Disco(titulo: String, precio: Double, anyoPublicacion: Int, descuentoProducto: Int = 0, var genero : GeneroMusica,
            var grupo: String, var stock: Int) : Producto(titulo,precio,anyoPublicacion,descuentoProducto) {

    override fun toString(): String {
        return "Genero = $genero, Grupo = '$grupo', Stock = $stock"
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Disco) return false
        if (!super.equals(other)) return false

        if (genero != other.genero) return false
        if (grupo != other.grupo) return false
        if (stock != other.stock) return false

        return true
    }

    override fun hashCode(): Int {
        var result = super.hashCode()
        result = 31 * result + genero.hashCode()
        result = 31 * result + grupo.hashCode()
        result = 31 * result + stock
        return result
    }


}