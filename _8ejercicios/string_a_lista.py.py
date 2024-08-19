'''STRING A LISTA: 
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información: 
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo: 
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos, 
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e 
imprimir la nota media de los alumnos junto con el DNI.  
Supón ahora que tu input es un string como este:  
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n 
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’ 
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI 
de todos los alumnos en ese string.'''

def procesar_alumnos(data):
    # Separar la cadena en líneas individuales
    lineas = data.strip().split('\n')

    # Crear una lista para almacenar la información de todos los alumnos
    lista_alumnos = []

    for linea in lineas:
        # Separar cada línea en sus componentes
        partes = linea.split()
        nombre = partes[0]
        apellido = partes[1]
        dni = partes[2]
        codigo_asignatura = partes[3]
        convocatoria = partes[4]
        notas = list(map(float, partes[5:]))
        
        # Calcular la nota media
        nota_media = sum(notas) / len(notas)

        # Crear una lista con los datos del alumno y añadirla a la lista de alumnos
        alumno = [nombre, apellido, dni, codigo_asignatura, convocatoria] + notas
        lista_alumnos.append(alumno)

        # Imprimir la nota media junto con el DNI del alumno
        print(f'DNI: {dni}, Nota Media: {nota_media:.2f}')

    return lista_alumnos

# Ejemplo de uso
input_data = '''David Fernandez 12311267A 43527 2 9.1 7.6 2.4
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4
Juan Perez 647829236A 43527 2 8.1 8.5 8.4'''

lista_alumnos = procesar_alumnos(input_data)

#Compara Lista
lista1=[]
lista2=[]
def comparalistas():

    for i in lista1:
        for j in lista2:
            if i == j :
                cierto=True
            else: cierto=False

    if cierto==False:
        print("diferentes")
    else: print("igualitas uwu")

lista1=["Ana", "Me", "Ama"]
lista2=["Ana", "Me", "ama"]
comparalistas()
