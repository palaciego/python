"""Problema de Gestión de Inventario:
Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
sistema de gestión de inventario. El inventario está representado como una lista
de productos ordenados por sus códigos. Cada producto se describe como un
diccionario con las claves 'codigo' y 'cantidad' .
Tu objetivo es implementar una función recursiva que realice una búsqueda
binaria en este inventario y devuelva la cantidad disponible para un producto
específico, dado su código.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada Salida
- Inventario de productos (json,dic,etc)
- Codigo de producto buscado
Cantidad disponible para el producto 307:
80"""
def buscar_producto(inventario, codigo, inicio, fin):
    # Caso base: si el rango de búsqueda es inválido
    if inicio > fin:
        return None

    # Calcular el punto medio
    medio = (inicio + fin) // 2
    producto_medio = inventario[medio]
    
    # Comparar el código del producto medio con el código buscado
    if producto_medio['codigo'] == codigo:
        return producto_medio['cantidad']
    elif producto_medio['codigo'] < codigo:
        # Buscar en la mitad derecha
        return buscar_producto(inventario, codigo, medio + 1, fin)
    else:
        # Buscar en la mitad izquierda
        return buscar_producto(inventario, codigo, inicio, medio - 1)
# Ejemplo de inventario
inventario = [
    {'codigo': 1400, 'cantidad': 8},
    {'codigo': 1600, 'cantidad': 15},
    {'codigo': 1700, 'cantidad': 17},
    {'codigo': 1800, 'cantidad': 4},
    {'codigo': 1900, 'cantidad': 12},
    {'codigo': 2000, 'cantidad': 23},
    {'codigo': 2100, 'cantidad': 2}
]
# Código del producto buscado
codigo_buscado = 1900
# Llamar a la función de búsqueda
cantidad_disponible = buscar_producto(inventario, codigo_buscado, 0, len(inventario) - 1)
# Imprimir el resultado
if cantidad_disponible is not None:
    print(f"Cantidad disponible para el producto {codigo_buscado}: {cantidad_disponible}")
else:
    print(f"Producto con código {codigo_buscado} no encontrado en el inventario.")