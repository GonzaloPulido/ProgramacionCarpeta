package ejercicio6_15

class ONG(var listaVoluntario: ArrayList<Voluntario>) {

    override fun toString(): String {
        return "Voluntarios = $listaVoluntario"
    }

    var mayor : Boolean = true


    fun siguiente(): Voluntario?{
        if (listaVoluntario.isEmpty()){
            return null
        }else if(mayor){
            var edad = 0
            var voluntarioFinal : Voluntario? = null
            for (x in listaVoluntario){
                if (x.edad > edad){
                    edad = x.edad
                    voluntarioFinal = x
                }
            }
            mayor = false
            listaVoluntario.remove(voluntarioFinal)
            return voluntarioFinal

        }else{
            var edad = 200
            var voluntarioFinal2 : Voluntario? = null
            for (x in listaVoluntario){
                if (x.edad < edad){
                    edad = x.edad
                    voluntarioFinal2 = x
                }
            }
            mayor = true
            listaVoluntario.remove(voluntarioFinal2)
            return voluntarioFinal2
        }

    }

    fun registrar(voluntario: Voluntario): Boolean{
        return if (voluntario in listaVoluntario){
            false
        }else{
            listaVoluntario.add(voluntario)
            true
        }
    }

}