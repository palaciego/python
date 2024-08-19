# Definición de la clase base Persona
class Persona:
    # Atributo de clase
    contador_personas = 0

    # Método constructor (__init__) que inicializa los atributos de instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.contador_personas += 1  # Incrementa el contador de personas

    # Método de instancia
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    # Método de clase
    @classmethod
    def obtener_numero_personas(cls):
        return cls.contador_personas

    # Método estático
    @staticmethod
    def descripcion():
        return "La clase Persona representa a un ser humano."

    # Método especial para representación de cadena
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    # Método especial para representación oficial
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

# Definición de la subclase Empleado que hereda de Persona
class Empleado(Persona):
    # Método constructor que inicializa atributos adicionales
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.salario = salario

    # Método de instancia adicional
    def mostrar_informacion(self):
        self.saludar()
        print(f"Mi salario es {self.salario}.")

    # Método especial para representación de cadena
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, salario: {self.salario}"

    # Método especial para representación oficial
    def __repr__(self):
        return f"Empleado(nombre={self.nombre}, edad={self.edad}, salario={self.salario})"


# Definición de la clase Matematica con un método estático
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

# Ejemplos de uso

# Creación de instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# Llamada a métodos de instancia
persona1.saludar()  # Salida: Hola, mi nombre es Juan y tengo 30 años.
persona2.saludar()  # Salida: Hola, mi nombre es Ana y tengo 25 años.

# Llamada a método de clase
print(Persona.obtener_numero_personas())  # Salida: 2

# Llamada a método estático
print(Persona.descripcion())  # Salida: La clase Persona representa a un ser humano.

# Creación de instancia de la subclase Empleado
empleado1 = Empleado("Luis", 28, 50000)

# Llamada a métodos de instancia de Empleado
empleado1.mostrar_informacion()
# Salida:
# Hola, mi nombre es Luis y tengo 28 años.
# Mi salario es 50000.

# Llamada a método estático de Matematica
print(Matematica.sumar(5, 7))  # Salida: 12

# Uso de métodos especiales para representación de cadena
print(persona1)  # Salida: Juan, 30 años
print(repr(persona1))  # Salida: Persona(nombre=Juan, edad=30)
print(empleado1)  # Salida: Luis, 28 años, salario: 50000
print(repr(empleado1))  # Salida: Empleado(nombre=Luis, edad=28, salario=50000)




