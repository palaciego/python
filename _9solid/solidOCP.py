"""# #27 SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
> #### Dificultad: Media | Publicación: 01/07/24 | Corrección: 08/07/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""


"""
Ejercicio
"""


from abc import ABC, abstractmethod


class Form:
    def draw(self):
        pass


class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")


class Circle(Form):
    def draw(self):
        print("Dibuja un círculo")


class Triangle(Form):
    def draw(self):
        print("Dibuja un triángulo")


"""
Extra
"""


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Substration(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)


calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("addition", 10, 5))
print(calculator.calculate("substration", 10, 5))
print(calculator.calculate("multiplication", 10, 5))
print(calculator.calculate("division", 10, 5))
print(calculator.calculate("power", 10, 5))