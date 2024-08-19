def scrabble():
    lista = []

    while True:
        entrada = input("Introduzca la letra y su puntuación (por ejemplo, A5): ")
        if len(entrada) > 1 and entrada[:-1].isalpha() and entrada[-1].isdigit():
            lista.append(entrada)
            print("Ficha añadida.")
        else:
            print("Entrada no válida.")

        interruptor = input("¿Introducir otra ficha? y/n: ")
        if interruptor.lower() == "y":
            continue
        else:
            break

    print("Lista de fichas:", lista)

    # Calcular la puntuación total
    puntuacion_total = 0
    for ficha in lista:
        puntuacion_total += int(ficha[1])

    print("La puntuación total de la mano de Scrabble es:", puntuacion_total)

scrabble()


import random

aleatorio=random.randint(1,100)

contador=0

while True:
    try:
        numero=int(input("introduzca un número: "))
        contador +=1

        if numero<aleatorio:
            print("el numero es mayor")

        elif numero>aleatorio:
            print("el numero es menor.")
            
        else:
            print(f"Correcto!, has consumido {contador} intentos.")
            break
    except ValueError:
        print("introduzca un número correcto del 1 al 100")