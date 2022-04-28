fun main() {


    val lavadora = Lavadora()
    val lavadora1 = Lavadora(200.0)
    val lavadora2 = Lavadora(200.0,80.0)
    val lavadora3 = Lavadora(200.0,80.0,"Gris")
    val lavadora4 = Lavadora(200.0,80.0,"Gris", 'B', 40.0)
    val televisor = Televisor()
    val televisor1 = Televisor(300.0)
    val televisor2 = Televisor(300.0,100.0)
    val televisor3 = Televisor(300.0,100.0, "Rojo")
    val televisor4 = Televisor(300.0,100.0, "Rojo",'D',40.0)
    val compra= Compra(arrayListOf(lavadora,lavadora1,lavadora2,lavadora3,lavadora4, televisor, televisor1,televisor2,televisor3,televisor4))

    println(compra.precioFinal())
    println("Las lavadoras valen ${compra.desglosar()[0]} \n y los televisores valen ${compra.desglosar()[1]}")
}
