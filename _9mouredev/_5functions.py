
"""-----------------------------------------------------------------------------------------------"""
doble = lambda x: x * 2
print("El doble de 5 es:", doble(5))

#sumar
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

def suma(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Not all list items are numbers"

#------------------------suma numeros-------------
def sum_of_numbers(n):
    return sum(range(n + 1))

print(sum_of_numbers(5))                # 15 (0 + 1 + 2 + 3 + 4 + 5 = 15)

print(sum([1, 2, 3, 4, 5]))             #15  Esto hace lo mismo que toda la funcion

list=[1, 2, 3, 4, 5]
def sumador(list):
          
    print(sum([1, 2, 3, 4, 5]))                 #15
    print(sum(list))                            #15
    suma=0
    for numero in list:
        suma+=numero

    print(suma)                                 #15

sumador(list)
    
#Global ?????
contador = 0
def incrementa_contador():
    global contador
    contador += 1
incrementa_contador()
print("El valor del contador es:", contador)

#externa????
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

#Asegurar no es negativo???
x = 5
assert x > 0, "x no puede ser negativo"
print("La aserción pasó correctamente.")

#---------------Even nums--------------
def evenum(nunm):
    return nunm%2==0
print(evenum(7))                        #False

#--------------------------------imprimir central.---------------
lista=["champú","colageno","tomillo","cardamomo","Cura"]
numerin=len(lista)
print(numerin)
odd=int(numerin/2)
centro_even1= int(numerin/2-1)
centro_even2= int(numerin/2)

if len(lista)%2==0:
    print(lista[centro_even1:centro_even2])
else:
    print(lista[odd])

print(f" primera  {lista[0]}, última {lista[-1]}, centro {lista[centro_even1]}, {lista[centro_even2]}")

"""Try, except finally raise yield"""
#Gestión de Excepciones:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Finalizando el bloque try-except")


try: 
    x = 1 / 0                                       #Inicia un bloque de código donde se manejan las excepciones.
except ZeroDivisionError:
    print("División por cero")                      #Captura y maneja una excepción específica.
"""raise ValueError("Valor inválido")                   #Genera una excepción específica."""


assert x > 0, "x debe ser mayor que cero"#Verifica si una condición es verdadera y genera una excepción si no lo es.

primernumero=int(input("Introduzca el primer número: "))
segundonumero=int(input("Introduzca el segundo número: "))


def es_primo(numero):
    for n in range (2,numero):
        if numero % n ==0:
            return False
    print(str(numero)+ "es primo.")
    return True

for i in range(primernumero,segundonumero):
    es_primo(i)

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_entre(num1, num2):
    print(f"Números primos entre {num1} y {num2}:")
    for numero in range(num1, num2 + 1):
        if es_primo(numero):
            print(numero, end=" ")

# Pedir al usuario que introduzca dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Asegurarse de que el primer número sea menor o igual que el segundo número
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Imprimir los números primos entre los dos números introducidos
imprimir_primos_entre(numero1, numero2)

lista1=[]
lista2=[]
def comparalistas():

    for i in lista1:
        for j in lista2:
            if i == j :
                cierto=True
            else: cierto=False

    if cierto==False:
        print("diferentes")
    else: print("igualitas uwu")

lista1=["Ana", "Me", "Ama"]
lista2=["Ana", "Me", "ama"]
comparalistas()
