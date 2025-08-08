import math
class producto :
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def __str__(self):
        return f"Nombre:{self.nombre} - Precio: ${self.precio}, Cantidad: {self.cantidad}"    

class inventario:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, nombre, precio, cantidad):
        for i in self.productos:
            if i.nombre == nombre:
                print(f"El producto '{nombre}' ya existe en el inventario.")
                return
        pro = producto(nombre, precio, cantidad)
        self.productos.append(pro)
        print(f"Producto '{pro.nombre}' agregado al inventario.")
            
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)    
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.") 
    def modificar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.productos:
            if producto.nombre == nombre:
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                print(f"Producto '{nombre}' modificado.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")    

def val_menu(opcion):
    try:
        if int(opcion) <= 0 or int(opcion) > 5 or math.isnan(float(opcion)) or opcion == 1e309:
            print("Por favor, ingrese una opcion valida.")
            return False
        else:
            return True
    except ValueError:
        print("Por favor, ingrese solo numeros.")

def val_num(precio, cantidad):
    try:
        precio = float(precio)
        cantidad = int(cantidad)
        if precio < 0 or cantidad < 0 or math.isnan(precio) or math.isnan(float(cantidad)) or precio == 1e309 or cantidad == 1e309:
            print("Por favor, ingrese valores positivos.")
            return False
        else:
            return True
    except ValueError:
        print("Por favor, ingrese solo numeros.")

def menu():
    inve = inventario()
    while True:
        print("\nopciones")
        print("1. Agregar producto")
        print("2. Mostrar productos")    
        print("3. Modificar producto")
        print("4. Eliminar producto")                
        print("5. Salir")    
        opcion = input("Seleccione una opción: ")
        if val_menu(opcion):
            if opcion == "1":   
                nombre = input("Ingrese el nombre del producto: ")
                while True:
                    precio = input("Ingrese el precio del producto: ")
                    cantidad = input("Ingrese la cantidad del producto: ")
                    if val_num(precio, cantidad):
                        inve.agregar_producto(nombre, precio, cantidad)
                        break
            elif opcion == "2":
                inve.mostrar_productos()
            elif opcion == "3":
                nombre = input("Ingrese el nombre del producto a modificar: ")
                while True:
                    precio = input("Ingrese el nuevo precio del producto: ")
                    cantidad = input("Ingrese la nueva cantidad del producto: ")
                    if val_num(precio, cantidad):
                        inve.modificar_producto(nombre, precio, cantidad)
                        break
            elif opcion == "4": 
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                inve.eliminar_producto(nombre)
            elif opcion == "5":
                print("Saliendo del programa.")
                break

menu()

