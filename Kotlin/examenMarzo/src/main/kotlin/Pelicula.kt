class Pelicula(titulo: String, precio: Double, anyoPublicacion: Int, descuentoProducto: Int = 0,
               var genero: GeneroPelicula, var director: String): Producto(titulo,precio,anyoPublicacion,descuentoProducto) {



    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Pelicula) return false
        if (!super.equals(other)) return false

        if (genero != other.genero) return false
        if (director != other.director) return false

        return true
    }

    override fun hashCode(): Int {
        var result = super.hashCode()
        result = 31 * result + genero.hashCode()
        result = 31 * result + director.hashCode()
        return result
    }

    override fun toString(): String {
        return "Pelicula(genero=$genero, director='$director')"
    }
}