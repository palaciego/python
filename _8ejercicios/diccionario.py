pais_ciudad = {}
def añade_pais_ciudad():
    while True:
        pais = input("País (escribe 'Exit' para salir): ")
        if pais == "Exit":
            break
        
        ciudad = input("Ciudad: ")
        
        # Añadir ciudad al diccionario bajo la clave del país
        if pais in pais_ciudad:
            pais_ciudad[pais].append(ciudad)
        else:
            pais_ciudad[pais] = [ciudad]
añade_pais_ciudad()

print(pais_ciudad)

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

def main():
    number = int(input("Introduzca un número: "))
    name = input("¿Cuál es su nombre? ").strip().title()

    print(hola(name) + f". Encantadísimo de conocerte, la solución al cuadrado de {number} es {cuadrado(number)}.", is_even(cuadrado(number)))
def cuadrado(n):
    return n ** 2
def hola(x="World"):
    return f"Saludos, {x}"
def is_even(n):
    if n % 2 == 0:
        return f"{n} es par"
    else:
        return f"{n} es impar"
main()
