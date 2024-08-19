# Se define una lista de tuplas con información sobre los usuarios y sus amigos en una red social
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Se crea una nueva lista sin duplicados, eliminando las cuentas repetidas de amigos
#for i in range(len(red_social)):
    #usuario = red_social[i][0]
    #amigos = red_social[i][1]
#for tupla in red_social:
red_social_sin_duplicados = []
for usuario, amigos in red_social:
    # Se crea una lista de amigos sin duplicados
    amigos_sin_duplicados = list(set(amigos))
    # Se agrega una nueva tupla a la lista red_social_sin_duplicados con el usuario y la lista de amigos sin duplicados
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados))

# Se crea una nueva lista que almacena el número de amigos de cada usuario
amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    # Se agrega el número de amigos de cada usuario a la lista amigos_por_usuario
    amigos_por_usuario.append((usuario, len(amigos)))

# Se convierte la lista amigos_por_usuario a una tupla para hacerla inmutable
amigos_por_usuario = tuple(amigos_por_usuario)

# Se imprime la lista completa de usuarios y su número de amigos correspondiente
print("Usuarios con número de amistades:", amigos_por_usuario)

# Se obtiene el usuario con más amigos, extrayendo el índice del máximo en la lista numero_amigos
lista_usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]

indice_con_mas_amigos = numero_amigos.index(max(numero_amigos))
usuario_con_mas_amigos = lista_usuarios[indice_con_mas_amigos]

# Se imprime el usuario con más amigos
print("Usuario con mayor conexión:", usuario_con_mas_amigos)

# Output: tuplas de tuplas -- usuario, número de amigos
# Output: Usuario con más amigos


"""set Clientes"""

# Se definen dos bases de datos como listas de tuplas con información sobre clientes
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

# Se crean dos conjuntos de nombres de clientes en ambas bases de datos, utilizando una comprensión de listas
nombres1 = set([cliente[0] for cliente in base_datos1])
nombres2 = set([cliente[0] for cliente in base_datos2])

# Se encuentra la intersección de ambos conjuntos, es decir, los clientes que aparecen en ambas bases de datos
nombres_comunes = nombres1.intersection(nombres2)

# Se imprime la lista de nombres de clientes comunes
print(nombres_comunes)

# Se crea una lista de tuplas de clientes comunes, recorriendo las dos bases de datos mediante un bucle for anidado
# y comprobando si el nombre del cliente aparece en la lista de clientes comunes.
clientes_comunes = []
for cliente1 in base_datos1:
    if cliente1[0] in nombres_comunes:
        for cliente2 in base_datos2:
            if cliente2[0] == cliente1[0]:
                # Si el cliente coincide en ambas bases de datos, se agrega una nueva tupla a la lista clientes_comunes
                # con la información del cliente de ambas bases de datos
                clientes_comunes.append((cliente1[0], cliente1[1],cliente1[2], cliente2[1], cliente2[2]))
                break

# Se imprime la lista completa de clientes comunes
print(clientes_comunes)




"""Lista de tuplas"""
# Se define una lista de tuplas con información sobre los libros y sus autores
lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]

# Se crea una lista vacía para almacenar los títulos de los libros y los apellidos de los autores
titulos_y_apellidos = []

# Se recorre la lista de libros con un bucle for, desempaquetando cada tupla en título y autor
for tupla in lista_libros:
    titulo, autor = tupla
    
    # Se utiliza el método split() para dividir el nombre completo del autor en una lista de palabras,
    # y se selecciona el último elemento de la lista (que debería ser el apellido)
    apellido = autor.split()[-1]

    # Se agrega una nueva tupla a la lista titulos_y_apellidos, que contiene el título del libro
    # y el apellido del autor
    titulos_y_apellidos.append((titulo, apellido))

# Se imprime la lista completa de títulos de libros y apellidos de autores
print(titulos_y_apellidos)



for num in range (2,101):
    primo=True
    for i in range (2,num):      # while primo == True and i < num:
        if num%i == 0:
            primo=False
            break                # i+=1
    if primo:
        print(num)


