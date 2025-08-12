from bicicleta import Bicicleta
from datetime import datetime
class Reserva:
    reservas = []
    def __init__(self,rut_cliente,id_reserva,id_bicicleta,fecha_reserva,fecha_devolucion,estado):
        self.rut_cliente = rut_cliente
        # para que no repitan las id de bicicletas
        if self.existe(id_reserva):
            id_reserva = None
        self.id_reserva = id_reserva
        self.bicicleta = id_bicicleta
        self.fecha_reserva = fecha_reserva
        # para poner fecha por defecto en none
        if not fecha_devolucion:
            fecha_devolucion = None
        self.fecha_devolucion = fecha_devolucion
        # para poner estado por defecto en por pagar
        if not estado:
            estado = "Por pagar"
        self.estado = estado
        
        if self.val_reserva(rut_cliente,fecha_reserva,id_bicicleta,id_reserva):
            Reserva.reservas.append(self)
    
    def __str__(self):
        if self.fecha_devolucion:
            # muestra el mensaje de la reserva devuelta
            precio = self.calcular_precio(self.fecha_reserva, self.fecha_devolucion,self.bicicleta)
            return f"Reserva id {self.id_reserva} para el cliente {self.rut_cliente} con id de bicicleta {self.bicicleta} reservada el {self.fecha_reserva} Hasta el {self.fecha_devolucion} con estado {self.estado} por el precio de {precio}."
        # muestra el mensaje de la reserva
        return f"Reserva con id {self.id_reserva} para el cliente {self.rut_cliente} con id de bicicleta {self.bicicleta} reservada el {self.fecha_reserva} con estado {self.estado}."
    
    # Pagar la reservas
    def pagar(self,fecha_devolucion):
        # Validar que lka reserva exista
        if not self.existe(self.id_reserva):
            print(f"La reserva ingresada no existe.")
            self.lineas()
            return self
        # Validar fecha
        if not self.val_fecha(fecha_devolucion):
            return self
        # Validar que la reserva no haya sido pagada
        if self.estado == "Pagada":
            print(f"La reserva {self.id_reserva} ya fue pagada.")
            self.lineas()
            return self
        # calcular el precio
        precio = self.calcular_precio(self.fecha_reserva, fecha_devolucion,self.bicicleta)
        if precio == None:
            return self
        # cambia el estado a pagada
        self.estado = "Pagada"
        self.fecha_devolucion = fecha_devolucion
        # cambia el estado de la bicicleta
        for bicicleta in Bicicleta.bicicletas:
            if bicicleta.id == self.bicicleta:
                bicicleta.estado = "Disponible"
        # muestra el mensaje
        print(f"La reserva del cliente {self.rut_cliente} ha sido pagada con un precio de {precio}.")
        self.lineas()
        return self

    # Mostrar las reservas
    @classmethod
    # muestra todas las reservas
    def mostrar_reservas(cls):
        if len(cls.reservas) == 0:
            print("No hay reservas registradas.")
            cls.lineas()
            return 
        for reserva in cls.reservas:
            print(reserva)

    @classmethod
    def val_reserva(cls,rut_cliente,fecha_reserva,id_bicicleta,id_reserva):
        #valida la reserva que no tenga id repetida
        if not id_reserva:
            print("La reserva ya existe.")
            cls.lineas()
            return False
        #valida la fecha
        if not cls.val_fecha(fecha_reserva):
            return False
        #valida el rut
        if not cls.val_rut(rut_cliente):
            return False
        # Verificar si la bicicleta existe
        if not cls.bicicleta_reservada(id_bicicleta):
            return False
        print("Reserva agregada correctamente.")
        cls.lineas()
        return True
    
    @staticmethod
    def calcular_precio(fecha_reserva, fecha_devolucion,id_bicicleta):
        # Calcular el precio
        try:
            # parsea las fechas
            if type(fecha_reserva) != datetime:
                fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d %H:%M")
            if type(fecha_devolucion) != datetime:
                fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d %H:%M")
            # Verificar que la fecha de devolucion sea posterior a la de reserva
            if fecha_devolucion < fecha_reserva:
                print("La fecha de devolucion debe ser posterior a la fecha de reserva.")
                Bicicleta.lineas()
                return None
        except (ValueError, TypeError):
            print("Las fechas ingresadas son inválidas.")
            Bicicleta.lineas()
            return None
        # Calcular el precio
        diferencia = fecha_devolucion - fecha_reserva
        # obtener el precio
        for bicicleta in Bicicleta.bicicletas:
            if  bicicleta.id == id_bicicleta:
                precio = bicicleta.precio
                break
        # calcular el precio final
        precio_final = precio * int(diferencia.total_seconds() / 3600)
        # si el precio es menor o igual a 0, se le asigna el precio de la bicicleta
        if precio_final <= 0:
            precio_final = precio
        return precio_final
    
    @classmethod
    # verifica si la reserva ya existe
    def existe(cls,id_reserva):
        for reserva in cls.reservas:
            if reserva.id_reserva == id_reserva:
                return True
        return False
    
    @staticmethod
    # imprime una linea separadora
    def lineas():
        print("-" * 50)
    
    @staticmethod
    # valida la fecha
    def val_fecha(fecha_reserva):
        try:
            if type(fecha_reserva) != datetime:
                fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d %H:%M")
            if fecha_reserva < datetime.now():
                raise Exception("La fecha de reserva no puede ser menor a la actual.")
            return True
        except (ValueError, TypeError):
            print("La fecha de reserva o devolución es inválida.")
            Bicicleta.lineas()
            return False
        except Exception as e:
            print(e)
            Bicicleta.lineas()
            return False
        
    @staticmethod
    # valida el rut
    def val_rut(rut):
        # Eliminar puntos y convertir a mayúsculas
        try:
            rut_limpio = rut.replace(".", "").replace("-", "").upper()

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
                print("El RUT es inválido.")
                Reserva.lineas()
                return False
            return True
        except (ValueError,TypeError,AttributeError):
            print("El RUT es inválido.")
            Reserva.lineas()
            return False
     
    @staticmethod
    # verifica si la bicicleta ya fue reservada y disponible
    def bicicleta_reservada(id_bicicleta):
        for bicicleta in Bicicleta.bicicletas:
            if bicicleta.id == id_bicicleta and bicicleta.estado == "Reservada":
                print("La bicicleta ingresada ya fue reservada.")
                Bicicleta.lineas()
                return False
            if bicicleta.id == id_bicicleta and bicicleta.estado == "Disponible":
                bicicleta.estado = "Reservada"
                return True
        print("La bicicleta ingresada no existe.")
        Bicicleta.lineas()
        return False