open class Punto(var x: Int, var y: Int): Grafico {

    init{
        require(x<=Grafico.maxx && y<=Grafico.maxy){"Fuera de rango"}
    }

    override fun mover(x: Int, y: Int): Boolean {
        if(this.x + x > Grafico.maxx || this.y + y > Grafico.maxy ){
            return false
        }
        this.x += x
        this.y += y
        return true
    }

    override fun dibujar() {
        println(this.toString())
    }

    override fun toString(): String {
        return "Punto(x=$x, y=$y)"
    }

}