class GraficoCompuesto(var listaGraficos: ArrayList<Grafico>):  Grafico{

    override fun mover(x: Int, y: Int): Boolean {
        var seMueve = true
        for (grafico in listaGraficos){
            if (!grafico.mover(x,y)){
                seMueve = false
            }
        }
        return seMueve
    }

    override fun dibujar() {
        for (grafico in listaGraficos){
            println(grafico.toString())
        }
    }

}