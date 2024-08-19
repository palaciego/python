'''. Escribe un programa que pida al usuario un número entero y muestre por pantalla una 
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el 
centro de la estructura. 
'''
# --- input ---
num=int(input("mete el numero: "))
# --- Primera mitad ---
for i in range (num+1):
    print("*"*(i-1)+" "*(num-i))
# --- Segunda mitad ---
for i in range (num-1,-1,-1):
    print("*"*(i-1)+" "*(num-i))

'''
2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
'''
# --- Consultor contraseña ---
def comprobador():
    contraseña = str(123456)
    while True:
        psw_entrada=input(" ")
        if psw_entrada == contraseña:
            print("Contraseña correcta crack")
            break
        else:print("Contraseña incorrecta, intentelo de nuevo")
    
comprobador()

'''
3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última. 
'''
# --- palabra ---
def updown_name():
    name=input("Introduzca su nombre, por favor: ")
    for i in range ((len(name)-1),-1,-1):
        print(name[i])
        
updown_name()
'''
4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
pantalla el número de veces que aparece la letra en la frase. '''
# --- Contador de letras ---
def contador_letra():
    frase=input("Introduzca la frase: ")
    letra=input("Introduzca la letra: ")
    contador=0
    long=len(frase)-1
    
# --- Número de letras en la frase ---
    for i in range (long):
        if frase[i] == letra:
            contador +=1

    print(contador)

contador_letra()