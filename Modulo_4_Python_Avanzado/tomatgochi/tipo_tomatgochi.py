from tomatgochi import Tomatgochi

class TipoTomatgochi(Tomatgochi):
    def __init__(self,nombre, color, salud, felicidad, energia, tipo, descripcion):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return (f"\nLos datos del Tomatgochi son nombre= {self.nombre}, tipo= {self.tipo}, "
                f"color= {self.color}, salud= {self.salud}, felicidad= {self.felicidad}, "
                f"energia= {self.energia}, \ndescripcion= {self.descripcion}")
    
    # Metodo para mostrar el tipo de Tomatgochi
    def mostrar_tipo(self):
        print(f"\nEl Tomatgochi es de Tipo: {self.tipo} con su Descripción: {self.descripcion}")
        return self