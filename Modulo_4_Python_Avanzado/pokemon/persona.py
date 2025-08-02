class Persona:
    def __init__(self, nombre, edad,pokemon):
        self.nombre = nombre
        self.edad = edad
        self.pokemon = []
        if pokemon:
            self.pokemon.append(pokemon)

    def jugar_pokemon(self,nombre_pokemon):
        for p in self.pokemon:
            if p.nombre == nombre_pokemon:
                p.jugar(self.nombre)
                return self
        print(f"\n{self.nombre} no tiene el Pokémon {nombre_pokemon}.")
        return self

    def dar_comida(self,nombre_pokemon):
        for p in self.pokemon:
            if p.nombre == nombre_pokemon:
                p.comer(self.nombre)
                return self
        print(f"\n{self.nombre} no tiene el Pokémon {nombre_pokemon}.")
        return self

    def curar_pokemon(self,nombre_pokemon):
        for p in self.pokemon:
            if p.nombre == nombre_pokemon:
                p.curar(self.nombre)
                return self
        print(f"\n{self.nombre} no tiene el Pokémon {nombre_pokemon}.")
        return self
    
    def tipo_pokemon(self, nombre_pokemon):
        for p in self.pokemon:
            if p.nombre == nombre_pokemon and hasattr(p, 'mostrar_tipo'):
                p.mostrar_tipo()
                return self
            elif p.nombre == nombre_pokemon:
                print(f"\n{self.nombre} no tiene un tipo definido para {nombre_pokemon}.")
                return self
        print(f"\n{self.nombre} no tiene el Pokémon {nombre_pokemon}.")
        return self
    
    def datos_pokemon(self):
        if not self.pokemon:
            print(f"\n{self.nombre} no tiene Pokémon.")
            return self
        print(f"\n{self.nombre} tiene los siguientes Pokémon:")
        for p in self.pokemon:
            p.datos() 
        return self
    
    def agregar_pokemon(self, pokemon):
        self.pokemon.append(pokemon)
        print(f"\n{pokemon.nombre} ha sido añadido a la lista de Pokémon de {self.nombre}.")
        return self