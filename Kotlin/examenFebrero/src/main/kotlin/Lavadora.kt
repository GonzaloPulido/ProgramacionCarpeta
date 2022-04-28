class Lavadora(precioBase: Double = 100.0, peso: Double = 5.0,
               color: String = "Blanco", consumoEnergetico: Char= 'F', var carga: Double = 5.0 ): Electrodomesticos(precioBase, peso, color, consumoEnergetico){


    override fun precioFinal(): Double {
        if(carga > 30.0){
            return super.precioFinal()+50.0
        }
        return super.precioFinal()
    }

    override fun toString(): String {
        return "Lavadora(carga=$carga)"
    }


}