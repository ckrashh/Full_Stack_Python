
class Bicicleta:
    bicicletas = []
    def __init__(self,id, marca, modelo,precio,estado):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.estado = estado
        
        # Validar que el id no exista
        if self.val_id(id,self.bicicletas):
            Bicicleta.bicicletas.append(self)

    def __str__(self):
        # muestra la bicicleta
        return f"Bicicleta con id {self.id} de la marca {self.marca} y modelo {self.modelo} con estado {self.estado} y precio por hora {self.precio}." 
    
    @classmethod
    # muestra las bicicletas
    def mostrar_bicicletas(cls):
        for bicicleta in cls.bicicletas:
            print(bicicleta)

    @staticmethod
    # Valida que el id no exista
    def val_id(id,biciletas):
        try:
            id = int(id)
            for bicicleta in biciletas:
                if bicicleta.id == id:
                    print("Ya existe una bicicleta con el id ingresado.")
                    Bicicleta.lineas()
                    return False
            print("Bicicleta agregada correctamente.")
            Bicicleta.lineas()
            return True
        except ValueError:
            print("El id debe ser un entero.")
            Bicicleta.lineas()
            return False
            
    @staticmethod
    # muestra las lineas
    def lineas():
        print("-" * 50)
    
   