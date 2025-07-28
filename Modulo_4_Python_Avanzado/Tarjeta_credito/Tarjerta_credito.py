class TarjetaCredito:

   #Incluye en este método valores por default
    tarjetas = []
    def __init__(self, saldo_pagar, limite_credito, intereses):
        if not saldo_pagar:
            saldo_pagar = 0
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
       
        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        if self.validar_monto(self.saldo_pagar, monto, self.limite_credito):
            self.saldo_pagar += monto
        return self    
 
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        return self
       

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${int(self.saldo_pagar)} pesos, Límite de crédito: ${self.limite_credito} pesos, Intereses: {self.intereses}")
        return self
       
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @staticmethod
    def validar_monto(saldo_pagar, monto, limite_credito):
        if  saldo_pagar + monto > limite_credito:
            print(f"Tarjeta Rechazada.\nTu compra por ${monto} pesos debido a que has alcanzado tu límite de crédito.")
            return False
        return True
    
    @classmethod
    def mostrar_tarjetas(cls):
        if not cls.tarjetas:
            print("No hay tarjetas registradas.")
            return
        for tarjeta in cls.tarjetas:
            tarjeta.mostrar_info_tarjeta()