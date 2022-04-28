package ejercicio6_14

class Grupo(var listaPersonas: ArrayList<Persona>) {

    init{
        require(listaPersonas.isNotEmpty()) {"Se necesita almenos una persona para crear un grupo"}
    }


    fun registra(persona: Persona): Boolean{
        if (persona in listaPersonas){
            return false
        }
        listaPersonas.add(persona)
        return true
    }


    fun elimina(persona: Persona): Boolean{
        if (persona in listaPersonas){
            listaPersonas.remove(persona)
            return true
        }
        return false
    }


    override fun toString(): String {
        return "Grupo = $listaPersonas"
    }


}