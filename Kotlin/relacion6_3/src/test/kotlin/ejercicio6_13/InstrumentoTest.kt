package ejercicio6_13

import org.junit.jupiter.api.Test


internal class InstrumentoTest {

    @Test
    fun tocarNota() {
        val guitarra = Guitarra(6)
        val flauta = Flauta(6)
        val notas = arrayListOf<Nota>(Nota.DO,Nota.RE,Nota.MI,Nota.FA,Nota.SOL,Nota.LA,Nota.SI)
        assert(guitarra.tocarNota() in notas)
        assert(flauta.tocarNota() in notas)
    }
}