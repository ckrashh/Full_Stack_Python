from auto import Auto
from libro import Libro
if __name__ == "__main__":
    print("---LIBROS---")
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "978-3-16-148410-0")
    libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "978-3-16-148410-1")
    libro3 = Libro("El túnel", "Ernesto Sabato", 1948, "978-3-16-148410-2")
    libro4 = Libro("Rayuela", "Julio Cortázar", 1963, "978-3-16-148410-3")
    libro5 = Libro("El alquimista", "Paulo Coelho", 1988, "978-3-16-148410-4")
    libros = [libro1, libro2, libro3, libro4, libro5]

    for libro in libros:
        print(libro)

    print("\n---AUTOS---")
    auto1 = Auto("Toyota", "Corolla", "1.8L", 2020)
    print(auto1)
    auto1.enceder()
    while True:
        opcion = input("\nElija una opcion:\n1. Acelerar\n2. Frenar\n3. Detener\n4. Apagar\n")
        if opcion == "1":
            print(auto1.acelerar())
        elif opcion == "2":
            print(auto1.frenar())
        elif opcion == "3":
            print(auto1.detener())
        elif opcion == "4":
            auto1.apagar()
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")    

