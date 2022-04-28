package ejercicio6_13

class Guitarra(var cuerdas: Int): Instrumento() {

    override fun toString(): String {
        return "Cuerdas = $cuerdas"
    }

}