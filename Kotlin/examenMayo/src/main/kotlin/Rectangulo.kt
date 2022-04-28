class Rectangulo(x: Int, y: Int, var ancho: Int, var alto: Int): Punto(x,y) {

    override fun toString(): String {
        return "Rectangulo(x =$x, y = $y, ancho=$ancho, alto=$alto)"
    }


    override fun mover(x: Int, y: Int): Boolean {
        if(this.x + x > Grafico.maxx || this.y + y > Grafico.maxy ){
            return false
        }
        else if (this.x + ancho > Grafico.maxx || this.y + alto > Grafico.maxy ){
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