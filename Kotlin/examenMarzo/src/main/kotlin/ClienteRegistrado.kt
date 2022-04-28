class ClienteRegistrado(var nombre:String, var apellidos: String, var dni: String,var telefono: String,
                        var saldo: Double, var descuento: Int = 2): Cliente{


    init{
        require(validaDNI()) {"DNI incorrecto"}
    }

    override fun aplicaDescuento(producto: Producto): Int {
        return producto.descuentoProducto+descuento
    }

    override fun pagar(cantidad: Double): Boolean {
        if (saldo >= cantidad){
            return true
        }
        return false
    }

    private fun actualizaDescuento(){
        if (descuento < 30){
            if (saldo == 100.0){
                descuento += 5
            }else if (saldo > 100){
                if ((saldo - 100.0) >= 50.0){
                    saldo += 1
                }
            }
        }

    }

    fun validaDNI(): Boolean{
        val numeros = arrayListOf<Char>('0','1','2','3','4','5','6','7','8','9')
        var cont = 0
        for (x in dni){
            cont += 1
            if (cont <= 8){
                if (x !in numeros){
                    return false
                }
            }
            else if(cont == 9){
                if (x.isLetter()){
                    return true
                }
            }

        }
        return false
    }

    fun esVIP(): Boolean{
        val lista = arrayListOf<Boolean>(true,false)
        return  lista.random()
    }

    override fun toString(): String {
        return "ClienteRegistrado(nombre='$nombre', apellidos='$apellidos', dni='$dni', telefono='$telefono', saldo=$saldo, descuento=$descuento)"
    }

}

