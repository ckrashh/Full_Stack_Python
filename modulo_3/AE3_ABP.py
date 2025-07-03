import random
#creamos las variables necesarias
descuento = 0
def validar_numero(precio,n_productos,n_compras_echas):
    try:
        precio = float(precio)
        n_productos = int(n_productos)
        n_compras_echas = int(n_compras_echas)
        if precio < 0 or n_productos < 0 or n_compras_echas < 0:
            print("Por favor, ingrese valores positivos.")
            return False
        else:
            return True
    except ValueError:
        print("Por favor, ingrese solo numeros.")

while True:
        Precio = input("Ingrese el precio del producto: ")
        N_productos = input("Ingrese el número de productos a comprar: ")
        N_compras_echas = input("Ingrese el número de compras hechas: ")
    
        if validar_numero(Precio, N_productos, N_compras_echas):
            break

Precio = float(Precio)
N_productos = int(N_productos)
N_compras_echas = int(N_compras_echas)
# Generar un número aleatorio del 1 al 7 para el día de la semana
dia = random.randint(1, 7)
if dia == 1:
    dia = "domingo"
elif dia == 2:
    dia = "lunes"
elif dia == 3:
    dia = "martes"
elif dia == 4:
    dia = "miércoles"
elif dia == 5:
    dia = "jueves"
elif dia == 6:
    dia = "viernes"
elif dia == 7:
    dia = "sabado"

#mostramos todos los descuentos aplicados
if N_productos > 10:
    print("¡Felicidades! Has comprado más de 10 productos, tienes un descuento del 10% adicional.")
    descuento += 10
if N_compras_echas > 5:
    print("¡Felicidades! Has hecho más de 5 compras, tienes un descuento del 5% adicional.")
    descuento += 5
if Precio > 500:
    print("La compra es mayor a 500, tienes un descuento del 7%  adiconal.")
    descuento += 7
if dia == "domingo" or dia == "sabado" or dia == "viernes":
    descuento += 15
    print(f"¡Felicidades! Has comprado en el dia {dia}, tienes un descuento del 15% adicional.")
# Verificamos si el descuento total supera el 30%
if descuento > 30: 
    descuento = 30

# Calculamos el precio total con descuento
precio_total = Precio * N_productos

#aplicamos todos los descuentos
if N_productos > 10 and N_compras_echas > 5 and Precio > 500 and (dia == "domingo" or dia == "sabado" or dia == "viernes"):
    precio_total_descuento = precio_total* 0.70  # 30% de descuento
    print("¡Felicidades! tu descuento total es del 30%. (No se puede superar el 30% de descuento)")
    print(f"El precio final de la compra es: $ {float(precio_total_descuento)} pesos")

#Aplica el total de los descuentos que se agreagon  
elif N_productos > 10 or N_compras_echas > 5 or Precio > 500 or (dia == "domingo" or dia == "sabado" or dia == "viernes"):
        precio_total_descuento = precio_total * (1 - descuento / 100)
        print(f"¡Felicidades! tu descuento total es del {(descuento)}%. (No se puede superar el 30% de descuento)")
        print(f"El precio final de la compra es: ${float(precio_total_descuento)} pesos")

#Si no se aplica descuento, mostramos el precio total sin descuento        
else: 
    print(f"No tienes descuento, el precio final de la compra es: $ {float(precio_total)} pesos")

# Mensaje final    
print("Gracias por tu compra, que tengas un buen día.")    
