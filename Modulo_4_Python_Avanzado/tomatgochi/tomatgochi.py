class Tomatgochi:
    def __init__(self, nombre, color, salud, felicidad, energia):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        if not felicidad : self.felicidad = 100
        self.felicidad = felicidad
        self.energia = energia

    def __str__(self):
        return f"\nLos datos del Tomatgochi son nombre= {self.nombre}, tipo= {self.color}, salud= {self.salud}, felicidad= {self.felicidad}, energia= {self.energia}"
    
    # Metodo con cual juega el Tomatgochi
    def jugar(self,entrenador=None):
        self.energia -= 10
        self.felicidad += 5
        if not entrenador:
            print(f"\nEl tomatgochi {self.nombre} ha jugado. Energía: {self.energia}, Felicidad: {self.felicidad}")
            return self
        print(f"\nEl entrenador {entrenador} ha jugado con {self.nombre}. Energía: {self.energia}, Felicidad: {self.felicidad}")
        return self

    # Metodo con cual come el Tomatgochi
    def comer(self,entrenador=None):
        self.salud += 10
        self.felicidad += 5
        if not entrenador:
            print(f"\nEl tomatgochi {self.nombre} ha comido. Salud: {self.salud}, Felicidad: {self.felicidad}")
            return self
        print(f"\nEl entrenador {entrenador} ha alimentado a {self.nombre}. Salud: {self.salud}, Felicidad: {self.felicidad}")
        return self
    
    # Metodo con cual cura el Tomatgochi
    def curar(self,entrenador=None):
        self.salud += 20
        if not entrenador:
            print(f"\nEl tomatgochi {self.nombre} se curo. Salud: {self.salud}")    
            return self
        print(f"\nEl entrenador {entrenador} ha curado a {self.nombre}. Salud: {self.salud}") 
        return self      