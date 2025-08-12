from reserva import Reserva
from bicicleta import Bicicleta
from datetime import datetime
if __name__ == "__main__":
    print("-"*50)
    print("--Caso 1 id bicicleta no valor numerico--")
    bici1 = Bicicleta("a", "Trek", "Domane", 1000,"Disponible")

    print("\n--Caso 2 bicicleta bien instanciada --")
    bici2 = Bicicleta(1, "Down", "Hill", 1000,"Disponible")

    print("\n--Caso 3 bicicleta id repetida --")
    bici3 = Bicicleta(1, "Trek", "Hill", 1000,"Disponible")

    print("\n--Caso 4 bicicleta bien instanciada --")
    bici4 = Bicicleta(2, "Trek", "Hill", 1000,"Disponible")

    print("\n-- Bicicletas --")
    Bicicleta.mostrar_bicicletas()
    print("-"*50)

    print("\n--Caso 5 reserva con rut invalido--")
    reserva3 = Reserva(2356456,"2",1,datetime.strptime("2025-10-01 10:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n--Caso 6 reserva bien instanciada--")
    reserva2 = Reserva("20222184-k","2",2,"2025-10-01 11:00",None,"Por pagar")

    print("\n--Caso 7 reserva con id bicicleta inexistente--")
    reserva1 = Reserva("20222184-k","3",3,datetime.strptime("2025-10-01 11:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n--Caso 8 reserva bien instanciada--")
    reserva5 = Reserva("20222184-k","1",1,datetime.strptime("2025-10-01 11:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n--Caso 9 reserva con id repetido--")
    reserva4 = Reserva("20222184-k","1",1,datetime.strptime("2025-10-01 11:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n--Caso 10 reserva con fecha anterior a la actual--")
    reserva6 = Reserva("20222184-k","3",1,datetime.strptime("2025-01-01 1:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n--Caso 11 reserva con fecha invalida--")
    reserva7 = Reserva("20222184-k","3",1,"dgsadgasdgas",None,None)

    print("\n-- Caso 12 Bicicleta ya rentada --")
    reserva8 = Reserva("20222184-k","4",1,datetime.strptime("2025-10-01 11:00", "%Y-%m-%d %H:%M"),None,None)

    print("\n-- Caso 13 pagar reserva inexistente--")
    reserva7.pagar("2025-10-01 12:00")

    print("\n-- Caso 14 pagar reserva existente--")
    reserva5.pagar("2025-10-01 12:00")

    print("\n-- Caso 15 pagar reserva ya pagada--")
    reserva5.pagar("2025-10-01 12:00")

    print("\n-- Caso 16 pagar reserva con fecha invalida--")
    reserva2.pagar("asdgasdgas")

    print("\n-- Caso 17 pagar reserva con fecha anterior a la reserva--")
    reserva2.pagar("2025-01-01 12:00")

    print("\n-- RESERVAS")
    Reserva.mostrar_reservas()
    print("-"*50)
    # Guardar los datos en archivos
    try:
        archivo_reservas = open(f"reservas{datetime.now().strftime('%Y%m%d')}.txt","w")
        for reserva in Reserva.reservas:        
            archivo_reservas.write(f"{reserva}\n")
        archivo_bicicletas = open("bicicletas.txt","w")
        for bicicleta in Bicicleta.bicicletas:            
            archivo_bicicletas.write(f"{bicicleta}\n")
    finally:
        archivo_reservas.close()
        archivo_bicicletas.close()