"""
1-Básico: imprime todos los números enteros del 0 al 100.
2-Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
3-Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
4-Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
5-Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
6-Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
"""

print("Codifica el ejercicio 1. Básico")
for i in range (1,100):
    print (i)

print("Codifica el ejercicio 2. Múltiples de 2")
for i in range(3,500):
    if i%2 == 0:
        print(i)

print("Codifica el ejercicio 3. Contando Vanilla Ice")
for i in range (1,101):
    if i%5 == 0 and i%10 !=0 :
        print("ice ice")
    elif i%10 == 0:
        print("baby") 
    else:
        print(i)

print("Codifica el ejercicio 4. Wow. Número gigante a la vista")
num_git = 0
for i in range (0,500000,2):
    num_git += i 
print(num_git)

print("Codifica el ejercicio 5. Regrésame al 3")
for i in range(2024,0,-3):
    print (i)
 
print("Codifica el ejercicio 6. Contador dinámico")
num_Inicial = 3 
num_Final = 10
multiplo = 2
while num_Inicial <=num_Final:
    if num_Inicial%multiplo==0:
        print(num_Inicial)
    num_Inicial+= 1