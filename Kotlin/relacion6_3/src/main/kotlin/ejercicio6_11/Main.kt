package ejercicio6_11

fun main(){
    val rifle1 = Rifle(100.0,80.0)
    val pistola1 = Pistola(22, 70.0)
    val escopeta1 = Escopeta(true, 20.0, 150.0)
    val cuchillo1 = Cuchillo(true,25.0,20.0)
    val hacha1 = Hacha(1,true,20.0, 50.0)

    rifle1.cargar()
    println(rifle1.atacar())

    escopeta1.cargar()
    println(rifle1.atacar())

    pistola1.cargar()
    println(pistola1.atacar())

    cuchillo1.afilar()
    println(cuchillo1.atacar())

    println(hacha1.atacar())


}