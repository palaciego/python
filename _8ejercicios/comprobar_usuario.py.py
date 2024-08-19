'''ANIDAR ACCESO A UN SITIO WEB: 
Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios 
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos. 
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo…
 nombres_usuario = ["juan123", "ana456", „pedro789"] 
Y otra lista con las contraseñas guardadas para cada usuario… 
contraseñas = ["clave123", "clave456", „clave789"] 
Otra opción puede ser que crees una lista de listas con la forma: 
nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["pedro789“,  
"clave789“] ] 
Despues puedes pedir el usuario y contraseña y comprobar si coinciden. 
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde 
recorras los nombres de usuario y compruebes con un if si el nombre de usuario introducido y la 
contraseña coinciden con los datos de tus listas. '''
# Lista de listas con nombres de usuario y contraseñas
nombres_contraseñas = [
    ["juan123", "clave123"],
    ["ana456", "clave456"],
    ["pedro789", "clave789"]
]
# Función para validar el acceso del usuario
def validar_acceso(usuario, contraseña):
    for registro in nombres_contraseñas:
        if registro[0] == usuario and registro[1] == contraseña:
            return True
    return False
# Solicitar al usuario que ingrese su nombre de usuario y contraseña
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña_usuario = input("Ingrese su contraseña: ")
# Verificar si el acceso es válido
if validar_acceso(nombre_usuario, contraseña_usuario):
    print("Acceso permitido. ¡Bienvenido!")
else:
    print("Acceso denegado. Nombre de usuario o contraseña incorrectos.")
"""Explicación:
Lista de listas: nombres_contraseñas contiene sublistas, cada una con un nombre de usuario y su contraseña correspondiente.
Función validar_acceso: Recorre la lista nombres_contraseñas y verifica si el nombre de usuario y la contraseña ingresados coinciden con algún registro.
Solicitar credenciales: El script pide al usuario que ingrese su nombre de usuario y contraseña.
Validar y mostrar resultado: La función validar_acceso se usa para verificar las credenciales ingresadas y se muestra un mensaje de acceso permitido o denegado según el resultado de la validación.
Este script básico puede ser mejorado agregando características como hashing de contraseñas para mayor seguridad, manejo de intentos fallidos, etc."""