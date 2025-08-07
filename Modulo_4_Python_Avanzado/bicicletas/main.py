from reserva import Reserva
from bicicleta import Bicicleta
from datetime import datetime
if __name__ == "__main__":
    
    bici1 = Bicicleta("a", "Trek", "Domane", 1000,"Disponible")
    bici2 = Bicicleta(1, "Down", "Hill", 1000,"Disponible")
    bici3 = Bicicleta(2, "Trek", "Hill", 1000,"Disponible")

    Bicicleta.mostrar_bicicletas()

    reserva3 = Reserva(2356456,"2",1,datetime.strptime("2025-10-01 10:00", "%Y-%m-%d %H:%M"),None,"Por pagar")
    reserva2 = Reserva("20222184-k","2",2,"2025-10-01 11:00",None,"Por pagar")
    reserva1 = Reserva("20222184-k","3",3,datetime.strptime("2025-01-01 11:00", "%Y-%m-%d %H:%M"),None,"Por pagar")
    Reserva.mostrar_reservas()