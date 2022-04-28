package ejercicio6_13

abstract class Instrumento {

    open fun tocarNota(): Nota{
        return Nota.values().random()
    }

}