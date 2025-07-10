# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
print(f"\nLa Matriz es: {matriz}")

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]
print(f"\nLos Cantantes son: {cantantes}")

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
print(f"\nLas Ciudades son: {ciudades}")

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]
print(f"\nLas Coordenadas son: {coordenadas}")

print("\nCambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]")
matriz[1][0] = 6
print(matriz)

print("\nCambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”")
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

print("\nCambia la ciudad de Cancún por Monterrey.")
ciudades["México"][2] = "Monterrey"
print(ciudades)

print("\nCambia la latitud por 9.9355431")
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

"""2. Iterar a través de una lista de diccionarios Crea la función iterarDiccionario(lista) 
que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente."""

def iterar_diccionario(lista):
    for diccionario in lista:
        for Clave, valor in diccionario.items():
            print(f"{Clave} - {valor}", end=", ")
        print()
        
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

print("\nIteracion de la lista de diccionarios")
iterar_diccionario(cantantes)        

"""
3. Obtener valores de una lista de diccionarios Crea la función iterarDiccionario2(llave, lista) 
    que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
    La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, 
    iterarDiccionario2(“nombre”, cantantes) debe de imprimir:
"""
def iterar_diccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])
        
print("\nIteracion de la lista de diccionarios 2 con nombres")        
iterar_diccionario2("nombre", cantantes)
print("\nIteracion de la lista de diccionarios 2 con paises")        
iterar_diccionario2("pais", cantantes)

"""
4. Iterar a través de un diccionario con valores de lista Crea una función imprimirInformacion(diccionario) 
que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave 
junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
"""
def imprimir_diccionario(diccionario):
    for clave in diccionario:
        print(f"\n{clave.upper()} tiene {len(costa_rica[clave])} elementos.")
        for elemento in diccionario[clave]:
            print(f"{elemento}")
            
    
costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}    
print("\nIteracion de un diccionario con valores de listas")
imprimir_diccionario(costa_rica)