'''BASE DE DATOS DE UN COLEGIO: 
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los 
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y 
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos. 
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al 
completo. 
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para 
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota 
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la 
clase.  '''

# --- Lista nombres

def cole():
    alumnos = []

    while True:
        nombre = input("\nIntroduzca el nombre del alumno: (Para terminar introduce: parar) ")
        if nombre.lower() != "parar":
            nombre = nombre.capitalize()
            alumnos.append(nombre)
        else:
            break
    print("Alumnos:", alumnos)

    notas = {}
    for alumno in alumnos:
        nota1 = float(input(f"Introduzca nota ejercicios de {alumno}: "))
        nota2 = float(input(f"Introduzca nota examen de {alumno}: "))
        nota3 = float(input(f"Introduzca nota proyecto de {alumno}: "))
        notas[alumno] = (nota1, nota2, nota3)
    print("Notas:", notas)

    # Calcular y mostrar la nota media de cada estudiante
    medias_estudiantes = {}
    for alumno, (nota1, nota2, nota3) in notas.items():
        media = (nota1 + nota2 + nota3) / 3
        medias_estudiantes[alumno] = media
        print(f"Nota media de {alumno}: {media:.2f}")

    # Calcular y mostrar la nota media de la clase
    suma_total = sum(medias_estudiantes.values())
    media_clase = suma_total / len(medias_estudiantes)
    print(f"Nota media de la clase: {media_clase:.2f}")

cole()
