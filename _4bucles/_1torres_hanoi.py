"""Recursividad:
Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
apilados en orden descendente, desde el disco N en la parte inferior hasta el
disco 1 en la parte superior.
Tu tarea es implementar una solución recursiva para mover todos los discos
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de
Hanoi:
1. Puedes mover un disco a una torre adyacente.
2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si
el disco superior es más grande que el disco que estás colocando.
Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar)
que, dado el número total de discos n y las torres de origen, destino y auxiliar,
imprima los pasos necesarios para lograr el movimiento de todos los discos
desde la torre A hasta la torre C.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada Salida
- N de discos
- N de torres
- Torres : origen, desitno, auxiliar
Mover disco de la torre A a la torre D
Mover disco de la torre A a la torre B
…
"""
# Ejercicio1 :
# Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos apilados en orden descendente, desde el disco N en la parte inferior hasta el disco 1 en la parte superior.

# Tu tarea es implementar una solución ***recursiva*** para mover todos los discos desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de Hanoi:

# 1. Puedes mover un disco a una torre adyacente.
# 2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si el disco superior es más grande que el disco que estás colocando.

# Debes definir una función llamada **`torres_de_hanoi(n, origen, destino, auxiliar)`** que, dado el número total de discos **`n`** y las torres de origen, destino y auxiliar, imprima los pasos necesarios para lograr el movimiento de todos los discos desde la torre A hasta la torre C.

def mover_disco(desde,hacia,disco):
  print(f'Mover disco {disco} de la torre {desde} hacia la torre {hacia}')

def torres_de_hanoi(n,origen,destino,auxiliar):
  #caso base /// recursividad
  if n == 1 :
    mover_disco(origen,destino,n)
    return
  #continuando con la recursividad
  torres_de_hanoi(n-1,origen,auxiliar,destino)
  mover_disco(origen,destino,n)
  torres_de_hanoi(n-1,auxiliar,destino,origen)


torres_de_hanoi(3,'Origen','Destino','Auxiliar')

def torres_de_hanoi(n, origen, destino, auxiliar):
    # Caso base: si solo hay un disco, moverlo directamente al destino
    if n == 1:
        print(f"Mover disco de la torre {origen} a la torre {destino}")
        return
    
    # Mover los n-1 discos desde la torre de origen a la torre auxiliar
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    
    # Mover el disco restante desde la torre de origen a la torre de destino
    print(f"Mover disco de la torre {origen} a la torre {destino}")
    
    # Mover los n-1 discos desde la torre auxiliar a la torre de destino
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso
n = 3  # Número de discos
origen = 'A'  # Torre de origen
destino = 'C'  # Torre de destino
auxiliar = 'B'  # Torre auxiliar

# Llamar a la función torres_de_hanoi
torres_de_hanoi(n, origen, destino, auxiliar)
