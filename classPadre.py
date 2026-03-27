class ItemBiblioteca :
    def __init__(self, titulo):
         self.titulo = titulo
         self.esta_prestado = False

    def prestar(self) :
            if self.esta_prestado :
                print(f"Error: El libro '{self.titulo}' ya está prestado.")
            else :
                self.esta_prestado = True
                print(f"Has prestado '{self.titulo}'")

    def devolver(self) :
        if not self.esta_prestado :
             print(f"Error: el libro '{self.titulo}' no está prestado.")
        else :
            self.esta_prestado = False
            print(f"Has devuelto '{self.titulo}'")