"""# #18 CONJUNTOS
> #### Dificultad: Fácil | Publicación: 29/04/24 | Corrección: 06/05/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""


"""
Ejercicio
"""

data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

data.append(6)
print(f"Añadiendo elemento al final: {data}")

data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")

data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posición: {data}")

del data[3]
print(f"Eliminando un elemento concreto: {data}")

data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

print(f"Comprobar si un elemento existe: {-1 in data}")

print(f"Eliminar el contenido: {data.clear()}")

"""
Extra
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {set_1.union(set_2)}")

print(f"Intersección: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")