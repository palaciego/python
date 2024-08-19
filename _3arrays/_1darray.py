# Importar modulos
import numpy as np

def crear_array_ones(longitud):
    return np.ones(longitud)

def cambiar_forma_array(array, filas, columnas):
    if filas * columnas == array.size:
        return np.reshape(array, (filas, columnas))
    else:
        raise ValueError("La cantidad de filas y columnas no es compatible con la longitud del array")

def crear_matriz_identidad(tamano):
    return np.eye(tamano)

def concatenar_arrays(array, matriz_identidad):
    concat_horizontal = np.hstack((array, matriz_identidad))
    concat_vertical = np.vstack((array, matriz_identidad))
    return concat_horizontal, concat_vertical

def main():
    try:
        longitud = int(input("Ingrese la longitud del array: "))
        array_ones = crear_array_ones(longitud)
        print("Array de unos:", array_ones)
        
        filas = int(input("Ingrese la cantidad de filas: "))
        columnas = int(input("Ingrese la cantidad de columnas:"))
        
        nuevo_array = cambiar_forma_array(array_ones, filas, columnas)
        print("Array con nueva forma:\n", nuevo_array)
        
        if filas == columnas:
            matriz_identidad = crear_matriz_identidad(filas)
            print("Matriz identidad:\n", matriz_identidad)
            
            concat_horizontal, concat_vertical = concatenar_arrays(nuevo_array, matriz_identidad)
            print("\nConcatenacion horizontal:\n", concat_horizontal)
            print("\nConcatenacion vertical:\n", concat_vertical)
        else:
            print("No se puede crear una matriz identidad con diferente numero de filas que de columnas")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()



# Multiplicar Matrices
matriz=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")

print("¡Listo!")     #1 2 3 4 5 6 7 8 9 ¡Listo!

import numpy as np

#--- Array 0 ---
array_1=np.zeros(8)
print(array_1)
#--- Array lleno ---
array_1[:]=2
print(array_1)
#--- Array 1-9 ---
array_2=np.arange(1,11,2)
print(array_2)
#--- Suma ---
for i in range(len(array_2)):
    array_2[i]+=array_2[i]
print(array_2)

print(array_2.sum())
