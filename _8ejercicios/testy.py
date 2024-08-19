
def maximo(*args):
    maximo= args[0]
    for numero in args[1:]:
        if numero>maximo:
            maximo=numero
    return maximo


print(maximo(10,60,123,50,1236123.5211231323211))


def printkwargs (**kwargs):
   
   for clave,valor in kwargs.items():
       print(f"{clave} ---> {valor}")
    

printkwargs(Nombre="Fulano", clas="berengano", somelier=123)


def crearpersonaje(nombre, *args, **kwargs):
    descripcion = f"####{nombre.upper()}####\n"
    descripcion += "Habilidades:\n"
    for skill in args:
        descripcion += f"  - {skill}\n"
    for key, value in kwargs.items():
        descripcion += f"{key}: {value}\n"
    return descripcion

print(crearpersonaje("pablo", "salta", "mea", fuerza=123, agilidad=456, inteligencia=789))

numero_a_adivinar = 8

def adivinador(numero_a_adivinar):
    while True:
        try:
            user_num = int(input("Introduzca un número: "))
            if numero_a_adivinar == user_num:
                print("¡Correcto! Has adivinado el número.")
                break
            elif user_num < numero_a_adivinar:
                print("El número es mayor. Intenta de nuevo.")
            else:
                print("El número es menor. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduzca un número válido.")

adivinador(numero_a_adivinar)