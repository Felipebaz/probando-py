class Libro :
    
    def __init__(self, titulo, autor) :
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self) :
        if self.prestado :
            print(f"Error: El libro '{self.titulo}' ya está prestado.")
        else :
            self.prestado = True
            print(f"Has prestado '{self.titulo}'")

    def devolver(self) :
        if not self.prestado :
            print(f"Error: el libro '{self.titulo}' no está prestado.")
        else :
            self.prestado = False
            print(f"Has devuelto '{self.titulo}'")

libro_1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez")
libro_2 = Libro("El Quijote", "Miguel de Cervantes")

print(libro_1.titulo)
print(libro_1.autor)    

libro_1.prestar()   

print(libro_2.titulo)
print(libro_2.autor)    