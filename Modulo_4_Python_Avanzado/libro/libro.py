class Libro:

    def __init__(self,titulo,autor,paginas,leidas):
        self.titulo = titulo
        self.autor = autor  
        self.paginas = paginas
        self.leidas = 0

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}")

    def leer(self,paginas):
        if paginas > self.paginas and self.leidas > self.paginas:
            print("No puedes leer más páginas de las que tiene el libro.")
            return self
        self.leidas += paginas
        return self 
    def leidos(self):
        print(f"Has leído {self.leidas} páginas del libro '{self.titulo}'.")
        return self

    def progreso(self):
        print(f"Has leído {self.leidas} de {self.paginas} páginas del libro '{self.titulo}'.")

    @classmethod
    def desde_string(cls, cadena):
        titulo, autor, paginas = cadena.split(",")
        return cls(titulo, autor, int(paginas),leidas=0)
    
    @staticmethod
    def es_libro_largo(paginas):
        if paginas > 400:
            print("Este es un libro largo.")
        else:
            print("Este es un libro corto.")
    
