
# Bucle for: Imprime números pares del 2 al 10
for i in range(2, 11, 2):
    print(i)  # Salida: 2, 4, 6, 8, 10

# Bucle for: Cuenta regresiva del 10 al 2
for i in range(10, 1, -1):
    print(i)  # Salida: 10, 9, 8, 7, 6, 5, 4, 3, 2

# Bucle for con break
for i in range(5):
    print("Valor de i en el segundo bucle:", i)
    if i == 2:
        break  # Termina el bucle cuando i es 2

# Bucle for con continue
for i in range(5):
    if i == 2:
        continue  # Salta el valor 2
    print("Valor de i en el tercer bucle:", i)  # Salida: 0, 1, 3, 4

# Bucle while con manejo de excepciones
contador = 0
while contador <= 10000000:
    contador += 1
    if contador == 6:
        print("Eureka")
        continue
    if contador > 10:
        break
    print(contador)  # Salida: 1, 2, 3, 4, 5, Eureka, 7, 8, 9, 10

# Bucle while para verificación de contraseña
password = "chocolateillo"
password_entrada = ""
while password_entrada != password:
    password_entrada = input("Introduzca la contraseña: ")
    if password_entrada != password:
        print("Contraseña incorrecta, intentalo de nuevo.")
print("Contraseña correcta.")

# Bucle for sobre listas o colecciones
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)  # Salida: manzana, banana, cereza

# Bucle while infinito (con condición de salida interna)
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        break

# Bucle for con la función enumerate
palabras = ["hola", "mundo", "python"]
for i, palabra in enumerate(palabras):
    print(f"Índice: {i}, Palabra: {palabra}")  # Salida: Índice: 0, Palabra: hola, etc.

# Bucle for con comprensión de listas
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


