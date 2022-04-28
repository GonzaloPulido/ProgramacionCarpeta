package ejercicio6_7

data class Libro(var titulo: String, var numeroPaginas: Int, var listaAutores : ArrayList<Autor>) {
    override fun toString(): String {
        return "Titulo = '$titulo', Numero de paginas = $numeroPaginas, Lista de autores -> [ $listaAutores ]"
    }
}