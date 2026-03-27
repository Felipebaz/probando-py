edad_str = input ("Introduce tu edad: ")
try :
    edad_int = int(edad_str)
    print (f"Tu edad es {edad_int}")
except ValueError :
    print ("Por favor, ingresa un numero valido para la edad")

print ("El programa continúa ejecutándose después del bloque try-except")