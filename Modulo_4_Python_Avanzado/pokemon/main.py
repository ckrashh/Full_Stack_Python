from pokemon import Pikachu, Squirtle, Charizard,Pokemon
from persona import Persona

if __name__ == "__main__":
    squirtle = Squirtle()
    pikachu = Pikachu()
    charizard = Charizard()
    piplu = Pokemon(nombre="Piplup", color="Azul", salud=50, felicidad=80, energia=100)

    ash = Persona(nombre="Ash Ketchum", edad=10, pokemon = pikachu)
    ash.agregar_pokemon(squirtle).agregar_pokemon(charizard).agregar_pokemon(piplu)
    
    ash.jugar_pokemon("Pikachu").dar_comida("Charizard").curar_pokemon("Squirtle").jugar_pokemon("Piplup")

    ash.datos_pokemon()
    ash.tipo_pokemon("Pikachu").tipo_pokemon("Squirtle").tipo_pokemon("Charizard").tipo_pokemon("Piplup")