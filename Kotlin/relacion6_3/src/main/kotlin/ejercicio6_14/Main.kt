package ejercicio6_14

fun main(){

    val cliente = Cliente("Gonzalo","Pulido",21,323123123)
    val cliente2 = Cliente("Gonzalo","Pulido",21,323123123)
    val proveedor = Proveedor("El Perico","S.A.",20,"A275M")

    val grupo = Grupo(arrayListOf(cliente,proveedor))

    println(grupo)
    grupo.registra(cliente2)
    println(grupo)
    grupo.elimina(proveedor)
    println(grupo)

}