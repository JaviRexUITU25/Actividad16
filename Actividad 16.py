class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    def show_book(self):
        print(f"El libro {self.titulo} ha sido agregado correctamente")

books = []
def add_libro():
    try:
        titulo = input("Ingrese el titulo del libro: ").upper()
        autor = input("Agregue el autor del libro: ").upper()
        publi = int(input("Ingrese el año de publicacion del libro: "))
        libro = Libro(titulo,autor,publi)
        books.append(libro)
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido")

def mostrar_lista():
    if not books:
        print("Ningun libro registrado, Registre primero un libro")
    else:
        print("Lista de libros: ")
        i = 1
        for book in books:
            print(f"{i}.", end= "")
            book.show_book()
        print()
