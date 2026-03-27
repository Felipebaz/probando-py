from classPadre import ItemBiblioteca

class DVD (ItemBiblioteca) :
    def __init__(self, titulo, director) :
        super().__init__(titulo)
        self.director = director
        self.esta_prestado = False

    def prestar(self) :
        print(f"Verificando si el DVD '{self.titulo}' esta rayado...")
        super.prestar()



