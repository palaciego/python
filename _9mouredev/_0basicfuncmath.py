# Sumador de lista
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print(sumar_lista([1, 2, 3, 4, 5]))  # Salida: 15

# Contador de números pares e impares
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

resultado = evens_and_odds(14)
print(resultado)  # Salida: The number of odds are 7. The number of evens are 8.

# Generador de números pares
def pair_generator(limit):
    my_list = []
    for number in range(1, limit):
        my_list.append(number * 2)
    return my_list

print(pair_generator(10))  # Salida: [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Factorial usando math
import math
print(math.factorial(5))  # Salida: 120

# Factorial usando recursión
def factorial(n):
    if isinstance(n, int) and n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        return "Input must be a non-negative integer"

print(factorial(5))  # Salida: 120

# Factorial usando bucle
def factorial_iterativo(n):
    if isinstance(n, int) and n >= 0:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    else:
        return "Input must be a non-negative integer"

print(factorial_iterativo(5))  # Salida: 120

# Potencia usando recursión
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 3))  # Salida: 8

# Suma de elementos en una lista usando recursión
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4, 5]))  # Salida: 15

# Número triangular usando recursión
def numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n - 1)

print(numero_triangular(4))  # Salida: 10

# Imprimir números pares en orden descendente usando recursión
def num_pares(num):
    if num < 2:
        return
    print(num)
    num_pares(num - 2)

num_pares(14)
# Salida: 14 12 10 8 6 4 2

# Imprimir números pares en orden descendente usando bucle
def numeros_pares(num):
    for i in range(num, 0, -2):
        print(i)

numeros_pares(14)
# Salida: 14 12 10 8 6 4 2

# Suma de dígitos de un número usando recursión
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))  # Salida: 10

# Comprobación de número primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(es_primo(11))  # Salida: True
print(es_primo(4))   # Salida: False

# Generador de números primos hasta un límite
def generar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

print(generar_primos(10))  # Salida: [2, 3, 5, 7]

# Función principal para ejecutar todas las funciones de prueba
def main():
    print("Sumador de lista:", sumar_lista([1, 2, 3, 4, 5]))  # Salida: 15
    print("Contador de números pares e impares:", evens_and_odds(14))  # Salida: The number of odds are 7. The number of evens are 8.
    print("Generador de números pares:", pair_generator(10))  # Salida: [2, 4, 6, 8, 10, 12, 14, 16, 18]
    print("Factorial usando math:", math.factorial(5))  # Salida: 120
    print("Factorial usando recursión:", factorial(5))  # Salida: 120
    print("Factorial usando bucle:", factorial_iterativo(5))  # Salida: 120
    print("Potencia usando recursión:", potencia(2, 3))  # Salida: 8
    print("Suma de elementos en una lista usando recursión:", suma_lista([1, 2, 3, 4, 5]))  # Salida: 15
    print("Número triangular usando recursión:", numero_triangular(4))  # Salida: 10
    num_pares(14)  # Salida: 14 12 10 8 6 4 2
    numeros_pares(14)  # Salida: 14 12 10 8 6 4 2
    print("Suma de dígitos de un número usando recursión:", suma_digitos(1234))  # Salida: 10
    print("Comprobación de número primo (11):", es_primo(11))  # Salida: True
    print("Comprobación de número primo (4):", es_primo(4))   # Salida: False
    print("Generador de números primos hasta un límite:", generar_primos(10))  # Salida: [2, 3, 5, 7]

if __name__ == "__main__":
    main()
