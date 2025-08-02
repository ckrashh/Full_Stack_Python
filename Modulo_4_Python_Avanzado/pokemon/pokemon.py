class Pokemon:
    def __init__(self, nombre, color,salud,felicidad,energia):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
        
    def jugar(self, entrenador):
        self.energia -= 10
        self.felicidad += 5
        print(f"\nEl entrenador {entrenador} ha jugado con {self.nombre}. Energía: {self.energia}, Felicidad: {self.felicidad}")
        

    def comer(self,entrenador):
        self.salud += 10
        self.energia += 5
        print(f"\nEl entrenador {entrenador} ha alimentado a {self.nombre}. Salud: {self.salud}, Energía: {self.energia}")
        

    def curar(self,entrenador):
        self.salud+= 20
        self.felicidad -= 5
        print(f"\nEl entrenador {entrenador} ha curado a {self.nombre}. Salud: {self.salud}, Felicidad: {self.felicidad}")
        
    
    def datos(self):
        print (f"\nNombre: {self.nombre}, Color: {self.color}, Salud: {self.salud}, Felicidad: {self.felicidad}, Energía: {self.energia}")

class Charizard(Pokemon):
    def __init__(self):
        super().__init__(nombre="Charizard", color="Naranja", salud=200, felicidad=30, energia=100)
        self.tipo = "Fuego"
    
    def mostrar_tipo(self):
        print(f"\n{self.nombre} es de tipo {self.tipo}.")

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(nombre="Pikachu", color="Amarillo", salud=110, felicidad=90, energia=100)
        self.tipo = "Eléctrico"
    
    def mostrar_tipo(self):
        print(f"\n{self.nombre} es de tipo {self.tipo}.")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(nombre="Squirtle", color="Azul", salud=60, felicidad=85, energia=100)
        self.tipo = "Agua"
        
    def mostrar_tipo(self):
        print(f"\n{self.nombre} es de tipo {self.tipo}.")
        