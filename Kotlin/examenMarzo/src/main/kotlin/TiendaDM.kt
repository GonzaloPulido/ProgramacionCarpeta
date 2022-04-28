class TiendaDM(var listaProducto: ArrayList<Producto>, var listaClientes: ArrayList<Cliente>) {

    init {
        require(listaProducto.isEmpty()) {"Es necesario almenos un producto"}
        require(listaClientes.isEmpty()) {"Es necesario almenos un cliente"}
    }

    fun buscaDisco(disco: Disco): Boolean{
        for (x in listaProducto){
            if (x == disco){
                return true
            }
        }
        return false
    }

    fun buscaPelicula(pelicula:Pelicula): Boolean{
        for (x in listaProducto){
            if (x == pelicula){
                return true
            }
        }
        return false
    }

    fun compraPelicula(numEjemplares: Int, pelicula: Pelicula): Double{
        return pelicula.precio * numEjemplares
    }

    fun compraDisco(numEjemplares: Int,disco: Disco):Double{
        return disco.precio*numEjemplares
    }


    override fun toString(): String {
        return "Lista de productos = $listaProducto"
    }


}