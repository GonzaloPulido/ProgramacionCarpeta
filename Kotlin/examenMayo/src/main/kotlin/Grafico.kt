interface Grafico {

    companion object{
        val maxx = 800
        val maxy = 600
    }

    fun mover(x: Int, y: Int): Boolean
    fun dibujar()

}
