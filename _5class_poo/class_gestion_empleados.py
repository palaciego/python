"""SISTEMA DE GESTIÓN DE EMPLEADOS
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
    - Clase base: `Empleado`
        - Atributos: nombre, apellido, salario base
        - Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
        - Atributo adicional: bono anual
        - Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
        - Atributo adicional: horas trabajadas por semana
    Resuelve el problema creando instancias de estas clases y calculando los
    salarios totales para diferentes tipos de empleados."""

class Empleado:
    def __init__(self,nombre,apellido,salario_base=1200):
        self.nombre=nombre
        self.apellido=apellido
        self.salario_base=salario_base
        print(f"Empleado{nombre} {apellido}. Con salario base {salario_base}")

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre,apellido,salario_base,bono_anual):
        super().__init__(nombre,apellido,salario_base)
        self.bono_anual=bono_anual
        print(f"Empleado completo {nombre} {apellido} Con salario base {salario_base} mas bono anual {bono_anual}")
class EmpleadoTiempoParcial(Empleado):
    def __init__(self,nombre,apellido,horas_semana,salario_base):
        super().__init__(self,nombre,apellido,salario_base)
        self.horas_semana=horas_semana
        precio_hora=7.40
        resultado=horas_semana*precio_hora
        print(f"Empleado parcial {nombre} {apellido}. Con salario base {salario_base} con {horas_semana}={resultado}")

Empleado("Paco", "Cucamono",1200)
EmpleadoTiempoParcial("Pepe","MuertoHambre",15,1200)
EmpleadoTiempoCompleto("Jesus", "Bolloleche",1200)

class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base,bono_anual):
        super().__init__(self,nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario(self):
        return super().calcular_salario() + self.bono_anual

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_semana):
        super().__init__(nombre, apellido, salario_base)
        self.horas_semana = horas_semana

    def calcular_salario(self):
        pago_por_hora = 7.40
        salario_semanal = self.horas_semana * pago_por_hora
        return salario_semanal * 4  # Suponiendo 4 semanas en un mes

# Crear instancias y calcular salarios
empleado1 = Empleado("Paco", "Cucamono", 1200)
empleado2 = EmpleadoTiempoCompleto("Pepe", "MuertoHambre", 500)
empleado3 = EmpleadoTiempoParcial("Jesus", "Bolloleche", 0, 15)

print(f"Salario total de {empleado1.nombre} {empleado1.apellido}: ${empleado1.calcular_salario()}")
print(f"Salario total de {empleado2.nombre} {empleado2.apellido}: ${empleado2.calcular_salario()}")
print(f"Salario total de {empleado3.nombre} {empleado3.apellido}: ${empleado3.calcular_salario()}")


