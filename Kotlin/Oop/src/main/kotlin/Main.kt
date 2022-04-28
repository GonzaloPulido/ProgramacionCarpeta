fun main() {
    println("Welcome to Paradise")

    var myCharacter1: Character = Character("Gonzalo",Position(0,0))
    var myCharacter2: Character = Character("Meddy",Position(0,0))


    myCharacter1.walk(Position(x=5,y=5))
    myCharacter2.walk(Position(x=10,y=10))
    println(myCharacter1.toString())
}