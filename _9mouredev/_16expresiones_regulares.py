"""# #16 EXPRESIONES REGULARES
> #### Dificultad: Media | Publicación: 15/04/24 | Corrección: 22/04/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""

import re

"""
Ejercicio
"""


def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)


print(find_numbers("Este es el ejercicio 16 publicado 15/04/2024."))


"""
Extra
"""


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))


print(validate_email("mouredev@gmail.com"))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


print(validate_phone("+34 901 65 89 04"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))


print(validate_url("http://www.moure.dev"))