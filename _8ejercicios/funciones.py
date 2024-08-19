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

def fizz_buzz(): 
    count=0
    for numero in range (1,102):
        
        if numero % 3==0 and numero%5==0:
            print ("fizz" + "buzz")
        elif numero %3 ==0:
            print("fizz")
        elif numero %5==0:
            print("buzz")
        else: print(count)
        count+=1

fizz_buzz()


