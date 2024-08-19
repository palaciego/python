print("MI CALCULADORA")


print("Hola, elija una opción:")
print("1: Suma")
print("2: Resta")
print("3: Multiplicacion")
print("4: Division")
print("5: Modulo")
print("6: Exponente")


operacion=int(input("Por favor, teclee una opción:\n"))
error=True

match operacion:
    case 1:
        print("Ha elegido Suma:")
    case 2:
        print("Ha elegido Resta:")
    case 3: 
        print("Ha elegido Multiplicar:")
    case 4:
        print("Ha elegio Dividir:")
    case 5:
        print("Ha elegido Modulo:")
    case 6:
        print("Ha elegido Exponente")
    case _:
        print("Vuelva a ejecutar la calculadora y elija una operacion")
        error=False
if error:

    num_1=float(input("1º Operador:"))
    num_2=float(input("2º Operador:"))

    Suma=round(num_1 + num_2,2)
    Resta=round(num_1-num_2,2)
    Multi=round(num_1*num_2,2)
    divi=round(num_1/num_2,2)
    modulo=round(num_1%num_2,2)
    expo=round(num_1//num_2,2)

    match operacion:
        case 1:
            resultado= print(f"la Suma de {num_1} y {num_2} es {Suma}")
        case 2:
            resultado= print((f"la Resta de {num_1} y {num_2} es {Resta}"))
        case 3:
            resultado =print((f"la Multiplicación de {num_1} y {num_2} es {Multi}"))
        case 4:
            resultado =print((f"la Division de {num_1} y {num_2} es {divi}"))
        case 5:
            resultado =print((f"el modulo de {num_1} y {num_2} es {modulo}"))
        case 6:
            resultado=print(f"el exponente de {num_1} y {num_2} es {expo}")

else: print("Elija una operación del 1 al 6") 
     
        
    