from classPadre import ItemBiblioteca


class Libro (ItemBiblioteca) :
    
    def __init__(self, titulo, autor) :
        super().__init__(titulo)
        self.autor = autor
        self.esta_prestado = False


libro_1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez")
libro_2 = Libro("El Quijote", "Miguel de Cervantes")

print(libro_1.titulo)
print(libro_1.autor)    

libro_1.prestar()   

print(libro_2.titulo)
print(libro_2.autor)    