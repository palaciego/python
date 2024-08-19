class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Creando un nuevo animal llamado {nombre}")

    def sonido(self):
        return "Hago algún ruido"

class Perro(Animal):
    def sonido(self):
        return "Guau Guau"

gato = Animal("Whiskers")
perro = Perro("Fido")

def imprime_sonido(animal):
    print(f"El sonido del animal es: {animal.sonido()}")

if isinstance(gato, Animal):
    print(f"{gato.nombre} es un animal.")

for i in range(3):
    print("Iteración", i)

for i in range(5):
    print("Valor de i en el segundo bucle:", i)
    if i == 2:
        break

for i in range(5):
    if i == 2:
        continue
    print("Valor de i en el tercer bucle:", i)

def funcion_vacia():
    pass

x = 5
assert x > 0, "x no puede ser negativo"
print("La aserción pasó correctamente.")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Finalizando el bloque try-except")

del gato
print("La variable 'gato' ha sido eliminada.")

doble = lambda x: x * 2
print("El doble de 5 es:", doble(5))

contador = 0
def incrementa_contador():
    global contador
    contador += 1
incrementa_contador()
print("El valor del contador es:", contador)

def externa():
    x = 10
    def interna():
        nonlocal x
        x += 1
        print("Valor de x dentro de la función interna:", x)
    interna()
    print("Valor de x fuera de la función interna:", x)
print("Llamando a la función externa...")
externa()

def suma(a, b):
    return a + b
print("La suma de 3 y 4 es:", suma(3, 4))

#Recursividad para factorizar (multiplicar todos los nº por si mismo hasta alcanzar el nº)
#Forma 1
def factorial(n):
    if n == 1:
        return 1
    else: n* factorial(n-1)
#Forma 2
import math
# Ejemplo: Factorial de 5
print(math.factorial(5))  # Salida: 120
#Forma 3
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo: Factorial de 5
print(factorial(5))  # Salida: 120

def sumar (a,b):
    """
    Calcula la suma de dos argumentos.
    
    Args:
        a(parametro)
        b(parametro)

    Returna:
        int: La suma de a y b.
    
    """
    return(a+b)

print(sumar(5,7))


#Gestión de Excepciones:
"""try: x = 1 / 0                                   
 #Inicia un bloque de código donde se manejan las excepciones.
except ZeroDivisionError: print("División por cero") 
#Captura y maneja una excepción específica.
raise ValueError("Valor inválido")                   
#Genera una excepción específica.
assert x > 0, "x debe ser mayor que cero"#Verifica si una condición es verdadera y genera una excepción si no lo es.
finally: print("Operación finalizada")  #Define un bloque de código que siempre se ejecuta, 
independientemente de si se genera una excepción o no."""

class Perro:
    especie="Canis Spaniel"
    def ladrar(self):
        print("GUAU")
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

mi_perro= Perro("Trufa",14)
print(mi_perro.nombre)
print(mi_perro.edad)

class Torra:
    pass

try:
    numero=int(input("Ingrese un numero"))
    division = 10/numero
    print(division)
except:
    print("elemento no apropiado")


def verificar_tipos(valor):
    if isinstance(valor, (int, float, complex)):
        return "Es un número"
    elif isinstance(valor, str):
        return "Es una cadena"
    elif isinstance(valor, list):
        return "Es una lista"
    else:
        return "Tipo desconocido"