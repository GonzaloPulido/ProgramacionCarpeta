class Televisor(precioBase: Double = 100.0, peso: Double = 5.0,
color: String = "Blanco", consumoEnergetico: Char= 'F', var diagonal: Double = 35.0 ,
                var resolucion: ArrayList<Int> = arrayListOf(1280,768)): Electrodomesticos(precioBase, peso, color, consumoEnergetico){


    override fun precioFinal(): Double {
        if (diagonal > 40.0){
            return super.precioFinal()*0.3+super.precioFinal()
        }
        return super.precioFinal()
    }

    override fun toString(): String {
        return "Televisor(diagonal=$diagonal, resolucion=$resolucion)"
    }

}