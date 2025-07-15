#importar fecha y hora
from datetime import datetime

#importar math para validar infinitos y NaN
import math

#Variables de diccionario y listas 
tarea = {}
list_tarea = []

#Funcion para agregar tareas
def agregar_tarea(nombre, descripcion, fecha, estado):
    if tareas_existe(nombre):
        tarea = {}
        tarea["nombre"] = nombre
        tarea["descripcion"] = descripcion
        tarea["fecha"] = fecha
        tarea["estado"] = estado_tarea(estado)

        list_tarea.append(tarea)
        print("Tarea agregada correctamente")
    else:
        print(f"La tarea {nombre} ya existe.")

#funcion para validar si la tarea ya existe
def tareas_existe(nombre):
    for tarea in list_tarea:
        if tarea["nombre"] == nombre:
            return False
    return True

#funcion para ver tareas
def ver_tareas():
    if len(list_tarea) != 0:
        for tarea in list_tarea:
            print(f"\nNombre: {tarea['nombre']}")
            print(f"Descripcion: {tarea['descripcion']}")
            print(f"Fecha de creacion: {tarea['fecha']}")
            print(f"Estado: {tarea['estado']}")   
    else:
        print("\nNo hay tareas en la lista.")

#funcion para eliminar tareas
def eliminar_tarea(nombre):
    if len(list_tarea) != 0:
        for tarea in list_tarea:
            if tarea["nombre"] == nombre:
                list_tarea.remove(tarea)
                print(f"\nLa tarea {tarea['nombre']} ha sido eliminada.")
                return
            
        print(f"\nLa tarea {nombre} no existe.")
    else:
        print("\nNo hay tareas en la lista.")    

#funcion para cambiar el estado de una tarea
def cambiar_estado_tarea(nombre, estado):
    if len(list_tarea) != 0:
        for tarea in list_tarea:
            if tarea["nombre"] == nombre:
                if tarea["estado"] == "Pendiente":
                    tarea["estado"] = estado_tarea(estado)
                    print(f"\nLa tarea {tarea['nombre']} ha sido {tarea['estado']}")
                    return
                else:
                    print(f"\nLa tarea {tarea['nombre']} ya fue completada anteriormente.")    
                    return
        print(f"\nLa tarea {nombre} no existe.")
    else:
        print("\nNo hay tareas en la lista.")            

#funcion para el estado de la tarea
def estado_tarea(estado):
    if estado:
        return "Completada"
    else:
        return "Pendiente"
    
#validar campos vacios
def validar_campos(nombre, descripcion, fecha, estado):

    if nombre == "" or descripcion == "" or fecha == "" or estado == "":
        print("\nPor favor, complete todos los campos.")
        return False
    else:
        return True
    
#validar opciones validas
def val_opcion(opcion):
    try:
        if int(opcion) <= 0 or int(opcion) > 5 or math.isnan(float(opcion)) or opcion == 1e309:
            print("\nPor favor, ingrese una opcion valida.")
            return False
        else:
            return True
    except ValueError:
        print("\nPor favor, ingrese una opcion valida.")    

#menu
while True:

    print("\n--- Gestor de Tareas ---")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar Tarea")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if val_opcion(opcion):
        if opcion == "1":
            while True:
                print("\nAgregar Tarea")
                nombre = input("Nombre tarea: ")
                descripcion = input("Descripcion tarea: ")
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                estado = False 
                if validar_campos(nombre, descripcion, fecha, estado):
                    agregar_tarea(nombre, descripcion, fecha, estado)
                    break

        elif opcion == "2":
            print("\nLista de Tareas")
            ver_tareas()
        elif opcion == "3":
            print("\nMarcar tarea como completada")
            print("Ingrese el nombre de la tarea a marcar como completada:")
            while True:
                nombre = input()
                if nombre == "":
                    print("Por favor, ingrese el nombre de la tarea a marcar como completada.")
                    continue
                else:
                    cambiar_estado_tarea(nombre, True)
                    break
        elif opcion == "4":
            while True:
                print("\nEliminar Tarea")
                print("Ingrese el nombre de la tarea a eliminar:")
                nombre = input()
                if nombre == "":
                    print("Por favor, ingrese el nombre de la tarea a eliminar.")
                    continue
                else:
                    eliminar_tarea(nombre)
                    break
        elif opcion == "5":
            print("\nFin del programa")
            break