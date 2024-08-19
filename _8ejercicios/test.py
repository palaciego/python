"""Valid Email"""
correcto=False
contador=0
email=input("Introduce su email: ")

for i in email:

    if i=="@":
        correcto=True
    elif i==".":
        contador=contador+1
    else:
        continue
    
    if correcto==True and contador>=1:
        print("Está correcto")
    else:
        print("vuelva a introducir su correo")
        



correcto = False
contador = 0

while not correcto or contador < 1:
    email = input("Introduce su email: ")
    correcto = False
    contador = 0

    for i in email:
        if i == "@":
            correcto = True
        elif i == ".":
            contador += 1

    if correcto and contador >= 1:
        print("Está correcto")
    else:
        print("Por favor, vuelva a introducir su correo electrónico.")

