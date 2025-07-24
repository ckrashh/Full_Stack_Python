class personaje:
    def __init__(self,tipo, nombre, vida, ataque, defensa):
        self.tipo = tipo
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.estado = False
    def golpear(self,danio, otro_personaje):
        if self.estado:
            self.defensa -=5 
            self.estado = False
        danio = danio - otro_personaje.defensa
        if danio > 0:
            otro_personaje.vida -= danio
            print(f"{self.nombre} golpea a {otro_personaje.nombre} causando {danio} puntos de daño.")
        else:
            print(f"{self.nombre} no logra causar daño a {otro_personaje.nombre}.")       

    def esta_vivo(self):
        self.vida = max(self.vida, 0)
        if self.vida <= 0:
            return True
    
    def defender(self):
        if self.estado:
            print(f"{self.nombre} ya se está defendiendo.")
            return
        print(f"{self.nombre} se defiende.")
        self.defensa += 5
        self.estado = True

    def __str__(self):
        return f"{self.tipo} {self.nombre} - Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}"    