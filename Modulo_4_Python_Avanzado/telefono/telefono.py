class Telefono:
    def __init__(self, marca, modelo, precio, procesador):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.procesador = procesador

    def __str__(self):        
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}, Procesador: {self.procesador}"    
    
    def vender(self):
        print(f"Vendido {self.modelo} por ${self.precio}.")

    def llamar(self, marca):
        print(f"Llamando la marca {marca} desde {self.marca}.")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"Precio actualizado a ${self.precio}.")    