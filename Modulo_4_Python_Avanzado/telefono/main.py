from telefono import Telefono
if __name__ == "__main__":
    Telefono1 = Telefono("Samsung", "Galaxy S21", 799, "Exynos 2100")
    print(Telefono1)
    Telefono2 = Telefono("Apple", "iPhone 13", 999, "A15 Bionic")
    print(Telefono2)

    Telefono1.vender()
    Telefono1.llamar(Telefono2.marca)
    Telefono1.actualizar_precio(749)
 