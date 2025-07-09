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

print("\nCambiar el valor 3 en matriz por 6.")
matriz[1][0] = 6
print(matriz)

print('\nCambia el nombre del primer cantante por "Enrique Martin Morales".')
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

print("\nCambia la ciudad de Cancún por Monterrey.")
ciudades["México"][2] = "Monterrey"
print(ciudades)

print("\nCambia la latitud por 9.9355431")
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

"""2. Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante.
* BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]"""
print("\n2. Ejercicio bonus")
for i in range(len(cantantes)):
    print(f"Nombre - {cantantes[i]['nombre']}, País - {cantantes[i]['pais']}")

"""3. Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre".
 Luego, imprime todos los valores correspondientes a la clave "pais"."""
print("\n3. Obtener valores específicos desde una lista de diccionarios")
print("Clave Nombre")
for i in range(len(cantantes)):
   print(f"Nombre: {cantantes[i]["nombre"]}")
print("Clave Pais")
for i in range(len(cantantes)):
    print(f"Pais: {cantantes[i]["pais"]}")

"""4. Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario

Realiza un recorrido del diccionario que imprima lo siguiente: 

La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
Cada elemento de la lista correspondiente, en líneas separadas.
"""
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
print("\n4. Recorrer un diccionario con listas como valores")
for clave in costa_rica:
    print(f"\n{clave.upper()} tiene {len(costa_rica[clave])} elementos.")
    for elemento in costa_rica[clave]:
        print(f"{elemento}")
