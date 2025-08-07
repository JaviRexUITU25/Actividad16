class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    def show_book(self):
        print(f"Libro: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"Año de publicacion: {self.publicacion}")
books = []
def add_libro():
    try:
        titulo = input("Ingrese el titulo del libro: ").upper()
        autor = input("Agregue el autor del libro: ").upper()
        publi = int(input("Ingrese el año de publicacion del libro: "))
        print(f"El libro: "f"{titulo} " + "ha sido agregado correctamente.")
        libro = Libro(titulo,autor,publi)
        books.append(libro)
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido")

def mostrar_lista():
    try:
        if not books:
            print("Ningun libro registrado, Registre primero un libro")
        else:
            print("Lista de libros: ")
            i = 1
            for mostrar in books:
                print(f"{i}.", end= "")
                mostrar.show_book()
            print()
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido")

def remove_book():
    try:
        eliminado = input("Ingrese el nombre del libro a eliminar: ").upper()
        encontrado = False
        for bookeli in books:
            if bookeli.titulo.lower() == eliminado.lower():
                books.remove(bookeli)
                print("Libro eliminado")
                encontrado = True
                break
        if not encontrado:
            print("Libro no encontrado")
    except ValueError:
        print("Ingrese un valor valido")
    except TypeError:
        print("Ingrese un tipo de valor valido")
    except Exception as e:
        print("Un error inesperado ha ocurrido")
while True:
    print("-"*10 + "Bienvenido al registro de Libros"+ "-"*10 + "\n"
        "1. Registrar Libros.\n"
        "2. Mostrar libros.\n"
        "3. Eliminar libro por nombre.\n"
        "4. Salir del programa")
    user_op = input("Ingrese la opcion que desea ingresar: ")
    match user_op:
        case "1":
            add_libro()
        case "2":
            mostrar_lista()
        case "3":
            remove_book()
        case "4":
            print("¡Gracias por usar el programa!")
            break
        case _:
            print("Ingrese un dato valido")