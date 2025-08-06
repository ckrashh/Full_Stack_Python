from bicicleta import Bicicleta
from datetime import datetime
class Reserva:
    reservas = []
    def __init__(self,rut_cliente,id_reserva,id_bicicleta,fecha_reserva,fecha_devolucion,estado):
        self.rut_cliente = rut_cliente
        if self.existe(id_reserva):
            id_reserva = None
        self.id_reserva = id_reserva
        self.bicicleta = id_bicicleta
        self.fecha_reserva = fecha_reserva
        if not fecha_devolucion:
            fecha_devolucion = None
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
        
        if self.val_reserva(rut_cliente,fecha_reserva,id_bicicleta,id_reserva) == True:
            Reserva.reservas.append(self)
    
    def __str__(self):
        if self.fecha_devolucion:
            precio = self.calcular_precio(self.fecha_reserva, self.fecha_devolucion,self.bicicleta)
            self.lineas()
            return f"Reserva {self.id_reserva} para el cliente {self.rut_cliente} con bicicleta {self.bicicleta} reservada el {self.fecha_reserva} Hasta el {self.fecha_devolucion} con estado {self.estado} por el precio de {precio}."
        self.lineas()
        return f"Reserva {self.id_reserva} para el cliente {self.rut_cliente} con bicicleta {self.bicicleta} reservada el {self.fecha_reserva} con estado {self.estado}."
    
    # Pagar la reservas
    def pagar(self,fecha_devolucion):
        if not self.existe(self.id_reserva):
            self.lineas()
            print(f"La reserva ingresada no existe.")
            return self
        if self.estado == "Pagada":
            self.lineas()
            print(f"La reserva {self.id_reserva} ya fue pagada.")
            return self
        self.estado = "Pagada"
        self.fecha_devolucion = fecha_devolucion
        for bicicleta in Bicicleta.bicicletas:
            if bicicleta.id == self.bicicleta:
                bicicleta.estado = "Disponible"
        precio = self.calcular_precio(self.fecha_reserva, fecha_devolucion,self.bicicleta)
        self.lineas()
        if precio != None:
            print(f"La reserva del cliente {self.rut_cliente} ha sido pagada con un precio de {precio}.")
        return self

    # Mostrar las reservas
    @classmethod
    def mostrar_reservas(cls):
        if len(cls.reservas) == 0:
            cls.lineas()
            print("No hay reservas registradas.")
            return 
        for reserva in cls.reservas:
            print(reserva)

    @classmethod
    def val_reserva(cls,rut_cliente,fecha_reserva,id_bicicleta,id_reserva,ex=False):
        if not id_reserva:
            cls.lineas()
            print("La reserva ya existe.")
            return False

        if not cls.val_fecha(fecha_reserva):
            return False
        # Eliminar puntos y convertir a mayúsculas
        try:
            rut_limpio = rut_cliente.replace(".", "").replace("-", "").upper()

            # Separar el número del dígito verificador
            numero = rut_limpio[:-1]
            digito_proporcionado = rut_limpio[-1]

            # Calcular el dígito verificador esperado
            reversed_digits = map(int, reversed(str(numero)))
            factores = [2, 3, 4, 5, 6, 7]
            suma = sum(d * f for d, f in zip(reversed_digits, factores * (len(numero) // len(factores) + 1)))
            resto = suma % 11
            digito_esperado = 11 - resto

            if digito_esperado == 11:
                digito_esperado = 0
            elif digito_esperado == 10:
                digito_esperado = 'K'

            # Comparar el dígito proporcionado con el calculado
            if str(digito_esperado) != digito_proporcionado:
                cls.lineas()
                print("El RUT es inválido.")
                return False
        except (ValueError,TypeError,AttributeError):
            cls.lineas()
            print("El RUT es inválido.")
            return False
        
        # Verificar si la bicicleta existe
        for bicicleta in Bicicleta.bicicletas:
            if  bicicleta.id == id_bicicleta and bicicleta.estado == "Disponible":
                bicicleta.estado = "Reservada"
                ex = True
        # Verificar si la reserva ya existe
        if not ex:
            cls.lineas()
            print("La bicicleta ingresada no existe o ya fue reservada.")
            return False
        for reserva in cls.reservas:
            if  reserva.fecha_reserva == fecha_reserva:
                cls.lineas()
                print("Ya existe una reserva para esa fecha.")
                for bicicleta in Bicicleta.bicicletas:
                    if  bicicleta.id == id_bicicleta:
                        bicicleta.estado = "Disponible"
                return False
        cls.lineas()
        print("Reserva agregada correctamente.")
        return True
    
    @staticmethod
    def calcular_precio(fecha_reserva, fecha_devolucion,id_bicicleta):
        # Calcular el precio
        try:
            if type(fecha_reserva) != datetime:
                fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d %H:%M")
            if type(fecha_devolucion) != datetime:
                fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            Bicicleta.lineas()
            print("Las fechas ingresadas son inválidas.")
            return
        diferencia = fecha_devolucion - fecha_reserva
        for bicicleta in Bicicleta.bicicletas:
            if  bicicleta.id == id_bicicleta:
                precio = bicicleta.precio
        precio_final = precio * int(diferencia.total_seconds() / 3600)
        if precio_final <= 0:
            precio_final = precio
        return precio_final
    
    @classmethod
    def existe(cls,id_reserva):
        for reserva in cls.reservas:
            if reserva.id_reserva == id_reserva:
                return True
        return False
    
    @staticmethod
    def lineas():
        print("-" * 50)
    
    @staticmethod
    def val_fecha(fecha_reserva):
        try:
            if type(fecha_reserva) != datetime:
                fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d %H:%M")
                return True
            return True
        except (ValueError, TypeError):
            Bicicleta.lineas()
            print("La fecha de reserva o devolución es inválida.")
            return False