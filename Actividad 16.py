class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    def show_book(self):
        print(f"El libro {self.titulo} ha sido agregado correctamente")

books = []

