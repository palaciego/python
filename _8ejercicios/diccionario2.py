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







