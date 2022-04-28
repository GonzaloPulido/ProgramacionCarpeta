abstract class Electrodomesticos(var precioBase: Double = 100.0, var peso: Double = 5.0,
                                var color: String = "Blanco", var consumoEnergetico: Char= 'F' ) {


    init {
        val listaColores = arrayListOf<String>("blanco", "negro", "rojo", "azul", "gris")
        val listaConsumo = arrayListOf<Char>('A', 'B', 'C', 'D', 'E','F')
        require(precioBase > 0.0) {"El precio debe ser mayor que 0"}
        require(peso > 0.0) {"El peso debe ser mayor que 0"}
        require(color.lowercase() in listaColores) {"No es posible tener ese color"}
        require(consumoEnergetico in listaConsumo){"Ese consumo no es valido"}

    }

    open fun precioFinal(): Double{
        var precioFinal = 0.0
        precioFinal += precioBase
        when (consumoEnergetico) {
            'A' -> {
                precioFinal += 10.0
            }
            'B' -> {
                precioFinal += 30.0
            }
            'C' -> {
                precioFinal += 50.0
            }
            'D' -> {
                precioFinal += 60.0
            }
            'E' -> {
                precioFinal += 80.0
            }
            'F' -> {
                precioFinal += 100.0
            }
        }
        if(peso > 0.0 && peso <= 19.0){
            precioFinal += 10.0
        }else if(peso in 20.0..49.0){
            precioFinal += 50.0
        }else if(peso in 50.0..79.0){
            precioFinal += 80.0
        }else if(peso >= 80.0){
            precioFinal += 100.0
            }
        return precioFinal
        }

    override fun toString(): String {
        return "Electrodomesticos(precioBase=$precioBase, peso=$peso, color='$color', consumoEnergetico=$consumoEnergetico)"
    }


}