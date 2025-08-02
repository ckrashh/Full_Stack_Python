class Persona():
    def __init__(self, nombre, apellido, tomatgochi):
        self.nombre = nombre
        self.apellido = apellido
        if not tomatgochi:
            self.tomatgochi = None
        self.tomatgochi = tomatgochi

    def __str__(self):
        if not self.tomatgochi: 
            return f"\nLos datos de la Persona son nombre= {self.nombre}, apellido= {self.apellido}, tomatgochi= No tiene"
        else:
            return f"\nLos datos de la Persona son nombre= {self.nombre}, apellido= {self.apellido}, tomatgochi= {self.tomatgochi.nombre}"

    # Metodo para jugar con el Tomatgochi
    def jugar_con_tomatgochi(self):
        if not self.val_tomatgochi(self.tomatgochi,contexto="jugar"):
            return self
        nombre = self.nombre + " " + self.apellido
        self.tomatgochi.jugar(nombre)
        return self

    # Metodo para dar comida al Tomatgochi
    def darle_comida(self):
        if not self.val_tomatgochi(self.tomatgochi,contexto="comer"):
            return self
        nombre = self.nombre + " " + self.apellido
        self.tomatgochi.comer(nombre)
        return self

    # Metodo para curar el Tomatgochi
    def curarlo(self):
        if not self.val_tomatgochi(self.tomatgochi,contexto="curar"):
            return self
        nombre = self.nombre + " " + self.apellido
        self.tomatgochi.curar(nombre)
        return self
    
    @staticmethod
    def val_tomatgochi(tomatgochi,contexto):
        if not tomatgochi:
            if contexto == "jugar":
                print("No tienes un Tomatgochi para jugar.")
            elif contexto == "comer":
                print("No tienes un Tomatgochi para alimentarlo.")
            elif contexto == "curar":
                print("No tienes un Tomatgochi para curarlo.")
            return False
        return True