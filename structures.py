lenguajes = ["Python", "Javascript", "Java", "C++", "Ruby"]

print (lenguajes[-1])

lenguajes.append("Go")

for lenguaje in lenguajes :
    print (f"Me gusta el lenguaje {lenguaje}")

coordenadas = (10, 20)

s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(10)
s.pop()
s.clear()

estudiante = {
    "nombre": "Juan",
    "edad": 25,
    "curso" : "Master en IA",
    "estado" : "Activo"
}

print (f"El estudiante se llama {estudiante['nombre']} y tiene {estudiante['edad']} años")

for clave, valor in estudiante.items() :
    print (f"{clave} : {valor}")
