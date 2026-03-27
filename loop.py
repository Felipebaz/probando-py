contador = 0

while contador < 3 :
    print (f"El contador es {contador}")
    contador += 1


print ("Inicio del bucle for")
for i in range(3):
    print (f"El contador es {i}")   


for numero in range (1, 6) :
    if numero % 2 == 0 :
        continue 
    print (f"El numero impar es {numero}")

