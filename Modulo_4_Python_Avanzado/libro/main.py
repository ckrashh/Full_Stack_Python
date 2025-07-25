from libro import Libro
if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, 0)
    libro1.mostrar_info()
    libro1.leer(100)
    libro1.leidos()
    libro1.progreso()

    libro2 = Libro.desde_string("El amor en los tiempos del cólera,Gabriel García Márquez,368")
    libro2.mostrar_info()
    libro2.leer(200).leer(50).leidos().progreso()

    Libro.es_libro_largo(libro1.paginas)
    Libro.es_libro_largo(libro2.paginas)
