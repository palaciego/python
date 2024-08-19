'''ENCRIPTACIÓN ROT13: 
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se 
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma 
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y 
catalán la ”Ç”, en alemán la ”ß”, etc.). 
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos 
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario 
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta 
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el 
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.  
[a,b,c,d,e,f,g,h,i,j,k,l,m] 			
ROT13 
[n,o,p,q,r,s,t,u,v,w,x,y,z]			
[H, O, L, A]
 [U, B, Y, N]
 1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto 
codificado según el cifrado ROT13 
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas 
esta codificación ROT13 de la otra. '''


def rot13():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'e', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palabra=[]
    spliteada=[]
    encriptada=[]

# --- Splitear letras ---

    palabra=input("Introduce la palabra: ")
    for letra in palabra:
        spliteada+=letra.lower()
    print(spliteada)
# --- Transposicionar ---
    for j in range (len(spliteada)):
        for i in range (len(abecedario)):
            if abecedario[i]==spliteada[j]:
                if i+13<26:
                    encriptada.append(abecedario[i+13])
                else: encriptada.append(abecedario[i-26+13])

    print(encriptada)

rot13()
encrip=rot13()

def comprobador():
    test=input("introduzca la palabra a comprobar")
    for i in encrip:
        for j in test:
            if test[i]==j[-13]:
                print("Correcto")
            else: print("Erroroneo")

