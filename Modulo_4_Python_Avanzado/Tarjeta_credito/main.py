from Tarjerta_credito import TarjetaCredito
if __name__ == "__main__":
    tarjeta1 = TarjetaCredito(None,5000, 0.02)
    tarjeta2 = TarjetaCredito(1000, 3000, 0.03)
    tarjeta3 = TarjetaCredito(2000, 10000, 0.04)

    print("--------Tarjeta 1-------")
    tarjeta1.compra(1000).compra(1500).cobrar_interes().mostrar_info_tarjeta()
    print("--------Tarjeta 2-------")
    tarjeta2.compra(700).compra(300).compra(200).pago(300).pago(500).cobrar_interes().mostrar_info_tarjeta()
    print("--------Tarjeta 3-------")
    tarjeta3.compra(700).compra(6000).compra(300).compra(4000).compra(500).mostrar_info_tarjeta()
    tarjeta3.compra(7000)

    print("\nMostrando todas las tarjetas registradas:")
    TarjetaCredito.mostrar_tarjetas()