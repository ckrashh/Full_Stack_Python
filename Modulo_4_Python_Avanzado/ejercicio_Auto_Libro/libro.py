class Libro:
    def __init__(self, titulo, autor, anio, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.isbn = isbn
    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Año: {self.anio} - ISBN: {self.isbn}"
