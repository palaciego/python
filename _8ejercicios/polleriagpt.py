Pollo = 12
Salpicon = 8.30
Patatas = 7
Croquetas = 3
Salmorejo = 2

print("¿Cuánto dinero tiene?")
dinero = float(input())
pedido = []
total = 0

print("---Mi Pollería---")

while True:
    print("1: Para Pollo")
    print("2: Para Salpicón")
    print("3: Para Patatas")
    print("4: No Quiero más")
    eleccion = input("Elija su pedido: ")

    if eleccion.isdigit():
        eleccion = int(eleccion)
        if eleccion == 1:
            print(f"Ha elegido un delicioso Pollo Frito por {Pollo} euros.")
            total += Pollo
            pedido.append("Pollo")
        elif eleccion == 2:
            print(f"Ha elegido un Salpicón por {Salpicon} euros.")
            total += Salpicon
            pedido.append("Salpicón")
        elif eleccion == 3:
            print(f"Ha elegido Patatas por {Patatas} euros.")
            total += Patatas
            pedido.append("Patatas")
        elif eleccion == 4:
            print("No deseo nada más.")
            break
        else:
            print("Por favor, seleccione una opción válida.")
    else:
        print("Por favor, introduzca un número.")

while True:
    print("1: Extra Salmorejo")
    print("2: Extra Croquetas")
    print("3: Nada más")
    extra = input("Extra: ")

    if extra.isdigit():
        extra = int(extra)
        if extra == 1:
            print(f"Ha añadido un extra de Salmorejo por {Salmorejo} euros.")
            total += Salmorejo
            pedido.append("Salmorejo")
        elif extra == 2:
            print(f"Ha añadido un extra de Croquetas por {Croquetas} euros.")
            total += Croquetas
            pedido.append("Croquetas")
        elif extra == 3:
            print("No deseo nada más.")
            break
        else:
            print("Por favor, seleccione una opción válida.")
    else:
        print("Por favor, introduzca un número.")

if total <= dinero:
    print("---Ticket---")
    print("Su pedido es:")
    for item in pedido:
        print("- " + item)
    print(f"Total: {total} euros")
    vuelta = round(dinero - total, 2)
    print(f"Su vuelta: {vuelta} euros")
    print("¡Gracias por su visita!")
else:
    print("No tiene suficiente dinero. Vuelva a elaborar su pedido, por favor.")
