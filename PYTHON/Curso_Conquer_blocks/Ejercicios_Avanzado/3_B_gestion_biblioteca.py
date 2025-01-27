"""
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:

1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.

2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.

3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.
"""
class Libro:
    def __init__(self,titulo,autor,numero_ejemplares):
        self.titulo=titulo
        self.autor=autor
        self.ejemplares=numero_ejemplares

class Usuario:
    def __init__(self, nombre,id):
        self.nombre=nombre
        self.id=id
        self.libros_prestados=[]

class Biblioteca:
    def __init__(self):
        self.lista_inventario=[]

    def agregar_libros(self,libros):
        self.lista_inventario.append(libros)

    def prestar_libros(self,libros,nombre,id):
        for libro in self.lista_inventario:
            if libros== libro.titulo:
                if libro.ejemplares>0:
                    usuario.libros_prestados.append(libros)
                    libro.ejemplares-=1
                elif libro.ejemplares==0:
                    print("se nos acabo ese libro ")
            
            else:
                print("el libro no existe")

    def devolver_libros(self, libros):
        for libro in self.lista_inventario:
            if libro.titulo==libros.titulo:
                libro.ejemplares+=1
            else:
                print("este libro no existe en  nuestros registros ")

    def mostrar_inventario_libros(self):
        for libro in self.lista_inventario:
            print(f"nobre del libro ||{libro.titulo}|| autor del libro ||{libro.autor}|| cantidad de ejemplares ||{libro.ejemplares}||")
        for i in Usuario:
            print(i)

biblioteca=Biblioteca()
usuario=Usuario("eduardo",182184608)
libro1=Libro("juan salvador","jake",5)
libro2=Libro("narnia","judaz",184968835)
biblioteca.agregar_libros(libro1)
biblioteca.mostrar_inventario_libros()
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.mostrar_inventario_libros()
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.prestar_libros("juan salvador","judaz",184968835)
biblioteca.mostrar_inventario_libros()
biblioteca.devolver_libros(libro1)
biblioteca.devolver_libros(libro2)
biblioteca.mostrar_inventario_libros()


