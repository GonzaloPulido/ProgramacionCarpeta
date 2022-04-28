class Circulo(x: Int, y: Int, var radio: Int): Punto(x,y) {
    override fun toString(): String {
        return "Circulo( x =$x, y = $y, radio=$radio)"
    }

    override fun mover(x: Int, y: Int): Boolean {
        if(this.x + x > Grafico.maxx || this.y + y > Grafico.maxy ){
            return false
        }
        else if (this.x + radio > Grafico.maxx || this.y + radio > Grafico.maxy ){
            return false
        }
        this.x += x
        this.y += y

        return true
    }

    override fun dibujar() {
        println(this.toString())
    }

}