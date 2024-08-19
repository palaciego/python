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
paises={}

def add_country():
    pais=input("Pais: ")

    while pais!= "Salir":
        ciudad=input("Ciudad: ")

        lista_ciudades=paises.setdefault(pais,[ciudad])

        if lista_ciudades != [ciudad]:
            paises[pais].append(ciudad)
        pais=input("Pais: (Salir para salir)")
    print(paises)

add_country()
'''Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con 
los números primos de la lista original. Además, el script debe devolver el número total de 
números primos encontrados y la suma de los números primos encontrados  '''      

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def saca_primos():
    lista_numeros = []
    while True:
        numero = int(input("Introduzca el número: "))
        lista_numeros.append(numero)
        interruptor = input("¿Continuar introduciendo? (y/n): ")
        if interruptor.lower() == "n":
            break
    print("Lista de números introducidos:", lista_numeros)
    
    # --- Primos ---
    lista_primos = []
    for numero in lista_numeros:
        if es_primo(numero):
            lista_primos.append(numero)
    print("Lista de números primos:", lista_primos)
    # --- Cantidad primos y suma ---
    suma = sum(lista_primos)
    print(f"La cantidad de números primos es igual a {len(lista_primos)}")
    print(f"La suma de los números primos es igual a {suma}")
saca_primos()