class Compra(var listaElectrodomesticos: ArrayList<Electrodomesticos>) {



    init {
        require(listaElectrodomesticos.isNotEmpty()){"Debemos tener almenos un electrodomestico"}
    }


    fun precioFinal(): Double{
        var precioLista = 0.0
        for (x in listaElectrodomesticos){
            precioLista += x.precioFinal()
        }
        return precioLista

    }

    fun desglosar(): ArrayList<Double>{
        val listaLavadoraTele = arrayListOf<Double>()
        var lavadoras = 0.0
        var televisores = 0.0
        for (x in listaElectrodomesticos){
            if (x is Lavadora){
                lavadoras += x.precioFinal()
            }else if (x is Televisor){
                televisores+= x.precioFinal()
            }
        }
        listaLavadoraTele.add(lavadoras)
        listaLavadoraTele.add(televisores)
        return listaLavadoraTele
    }

    override fun toString(): String {
        return "Compra(listaElectrodomesticos=$listaElectrodomesticos)"
    }


}