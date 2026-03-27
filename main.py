from classPadre import ItemBiblioteca
from classLibro import Libro
from classDVD import DVD

items = [
    Libro ("LibroA", "Autor A"),
    DVD("Pelicula B", "Director B")
]

for item in items :
    item.prestar()
    print("-"*10)