# --- Creación de números complejos ---
complejo1 = 2 + 3j  # Parte real: 2, Parte imaginaria: 3
complejo2 = complex(4, -5)  # Parte real: 4, Parte imaginaria: -5

# --- Aritmética básica ---
suma = complejo1 + complejo2            # (6-2j)
resta = complejo1 - complejo2           # (-2+8j)
multiplicacion = complejo1 * complejo2  # (23+2j)
division = complejo1 / complejo2        # (-0.17073170731707318+0.6097560975609756j)
potencia = complejo1 ** 2               # (-5+12j)

# --- Propiedades ---
real = complejo1.real     # 2.0
imaginario = complejo1.imag  # 3.0
conjugado = complejo1.conjugate()  # (2-3j)

# --- Funciones matemáticas ---
import cmath

num_complejo = 1 + 2j

abs_valor = abs(num_complejo)         # 2.23606797749979 (magnitud)
fase = cmath.phase(num_complejo)      # 1.1071487177940904 (ángulo en radianes)
polar = cmath.polar(num_complejo)     # (2.23606797749979, 1.1071487177940904) (magnitud y fase)
rect = cmath.rect(2.23606797749979, 1.1071487177940904) # (1+2j) convierte de polar a rectangular

# --- Funciones trigonométricas ---
seno = cmath.sin(num_complejo)        # (3.165778513216168+1.959601041421606j)
coseno = cmath.cos(num_complejo)      # (2.0327230070196656-3.0518977991517997j)
tangente = cmath.tan(num_complejo)    # (0.03381282607989669+1.0147936161466335j)

# --- Exponenciales y logaritmos ---
exponencial = cmath.exp(num_complejo) # (-1.1312043837568135+2.4717266720048188j)
logaritmo = cmath.log(num_complejo)   # (0.8047189562170503+1.1071487177940904j)
log_base_10 = cmath.log10(num_complejo) # (0.34948500216800943+0.480828578784234j)
sqrt_complejo = cmath.sqrt(num_complejo) # (1.272019649514069+0.7861513777574233j)

# --- Comparaciones ---
a = 1 + 2j
b = 3 + 4j

igual = (a == b)       # False
diferente = (a != b)   # True

# --- Operaciones adicionales ---
modulo = abs(complejo1)  # 3.605551275463989 (magnitud)
fase = cmath.phase(complejo1)  # 0.982793723247329 (ángulo en radianes)

# --- Ejemplo práctico: suma de una lista de números complejos ---
complejos = [1+2j, 3+4j, -1-1j]  # (3+5j)
suma_complejos = sum(complejos)  

# --- Convertir entre representaciones polar y rectangular ---
magnitude, angle = cmath.polar(num_complejo)  # (2.23606797749979, 1.1071487177940904)
rectangular = cmath.rect(magnitude, angle)    # (1+2j)

# --- Manejo de excepciones ---
try:
    division_compleja = complejo1 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
