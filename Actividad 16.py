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

def remove_book():
    try:
        eliminado = input("Ingrese el nombre del libro a eliminar: ").upper()
        eliminado = False
        if eliminado not in books:
            print("Libro no encontrado")
        else:
            for book in books:
                if book.show_book.lower() == eliminado:
                    books.remove(book)
                    print("Libro eliminado")
                    eliminado = True
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
while True:
    print("-"*10 + "Bienvenido al registro de Libros"+ "-"*10 + "\n"
        "1. Registrar Libros."
        "2. Mostrar libros."
        "3.Eliminar libro por nombre."
        "4. Salir del programa")
    user_op = input("Ingrese la opcion que desea ingresar: ")
    match user_op:
        case "1":
            add_libro()
        case "2":
            mostrar_lista()
        case "3":
            credits()
        case "4":
            break
        case _:
            print("Ingrese un dato valido")