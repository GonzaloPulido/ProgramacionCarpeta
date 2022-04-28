class Character(var name: String = "",var position: Position = Position(0,0)){
    constructor(name:String): this(){
        this.name = name
    }

    fun walk(distance:Position):Boolean{
        this.position = distance // EL THIS CAMBIA LA POSICION
        return true
    }

    override fun toString(): String {
        return "Character(name='$name', position=$position)"
    }



}