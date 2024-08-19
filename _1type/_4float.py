
# --- Funciones matemáticas ---
import math

num = -10.75
absoluto = abs(num)             # 10.75
redondeo = round(3.456, 2)      # 3.46
techo = math.ceil(3.1)          # 4
piso = math.floor(3.9)          # 3
num = 3.14159
redondeo = round(num, 2)        # 3.14
truncado = math.trunc(num)      # 3
raiz_cuadrada = math.sqrt(16)   # 4.0
logaritmo = math.log(100, 10)   # 2.0
seno = math.sin(math.pi / 2)    # 1.0
coseno = math.cos(math.pi)      # -1.0
tangente = math.tan(math.pi / 4)# 1.0

3.14159.is_integer() # False

# --- Manejo de excepciones ---
try:
    resultado = 10.0 / 0.0
except ZeroDivisionError:
    print("No se puede dividir por cero")


