"""MATRIZ: 
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en 
ese caso imprima dos listas correspondientes a: 
1. La fila cuyos elementos suman el máximo 
2. La columna cuyos elementos suman el máximo 
Si no se trata de una matriz devolverá dos listas vacías. 
Por ejemplo: 
M1=[[2,5,3],[6,1,8],[7,5,4]]  devolverá: L1 = [7,5,4] y L2 = [2,6,9,7] 
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = [] 
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo 
numero de objetos) """

def es_matriz(M):
    if not M:
        return False
    longitud = len(M[0])
    for fila in M:
        if len(fila) != longitud:
            return False
    return True

def suma_max_fila(M):
    suma_max = -float('inf')
    fila_max = []
    for fila in M:
        suma_fila = sum(fila)
        if suma_fila > suma_max:
            suma_max = suma_fila
            fila_max = fila
    return fila_max

def suma_max_columna(M):
    num_filas = len(M)
    num_columnas = len(M[0])
    suma_max = -float('inf')
    columna_max = []

    for col in range(num_columnas):
        suma_col = sum(M[fila][col] for fila in range(num_filas))
        if suma_col > suma_max:
            suma_max = suma_col
            columna_max = [M[fila][col] for fila in range(num_filas)]
    
    return columna_max

def identificar_matriz(M):
    if es_matriz(M):
        fila_max = suma_max_fila(M)
        columna_max = suma_max_columna(M)
        return fila_max, columna_max
    else:
        return [], []

# Ejemplo de uso
M1 = [[2,5,3],[6,1,8],[7,5,4]]
M2 = [[4,2,3],[4,5],[6,8,2]]

print(identificar_matriz(M1))  # Debería devolver ([7,5,4], [7,5,8])
print(identificar_matriz(M2))  # Debería devolver ([], [])
