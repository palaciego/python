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