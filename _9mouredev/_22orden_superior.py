"""# #22 FUNCIONES DE ORDEN SUPERIOR
> #### Dificultad: Difícil | Publicación: 27/05/24 | Corrección: 03/06/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""


from functools import reduce
from datetime import datetime

"""
Ejercicio
"""

# Función como argumento


def apply_func(func, x):
    return func(x)


print(apply_func(len, "MoureDev"))

# Retorno de función


def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

#  Sistema

numbers = [1, 3, 4, 2, 5]

# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))

# filter()


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def sum_values(x, y):
    return x + y


print(reduce(sum_values, numbers))

"""
Extra
"""

students = [
    {"name": "Brais", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "moure", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "mouredev", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate": "25-01-1980",
        "grades": [10, 9, 9.7, 9.9]}
]


def average(grades):
    return sum(grades) / len(grades)

# Promedio


print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)

# Mejores

print(
    list(
        map(lambda student:
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
    )
)

# Fecha de nacimiento ordenada

print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True))

# Califiación más alta

print(max(map(lambda student: max(student["grades"]), students)))