class Auto:
    def __init__(self, marca, modelo,motor, año):
        self.marca = marca
        self.motor = motor
        self.modelo = modelo
        self.año = año
        self.velocidad = 0

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Motor: {self.motor}, Año: {self.año}"    
    
    def acelerar(self):
        self.velocidad += 20
        return f"El auto {self.modelo} está acelerando. Velocidad actual: {self.velocidad} km/h"
    
    def frenar(self):
        self.velocidad -= 20
        if self.velocidad < 0:
            self.velocidad = 0
            return f"El auto {self.modelo} está detenido."
        return f"El auto {self.modelo} esta frenando. Velocidad actual: {self.velocidad} km/h"
    
    def detener(self):
        if self.velocidad == 0:
            return f"El auto {self.modelo} ya está detenido."
        self.velocidad = 0
        return f"El auto {self.modelo} se ha detenido."
    
    def enceder(self):
        return print(f"El auto {self.modelo} se ha encendido.")
    
    def apagar(self):
        return print(f"El auto {self.modelo} se ha apagado.")
    