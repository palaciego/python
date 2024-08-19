'''PALABRAS PROHIBIDAS: 
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna letra prohibida. '''
# --- Lista de 5 palabras aleatorias ---
def limpiador_listas():
    lista_palabras=[]
    print("Bienvenido. ")
    for i in range (5):
        palabra=input(f"Introduzca la {i+1}ª palabra: ")
        lista_palabras.append(palabra.lower())

    print(lista_palabras)

# --- Lista Letras prohibidas ---
    tupla_letras = ()
    while len(tupla_letras) < 5:
        letra = input(f"Introduzca la {len(tupla_letras)+ 1}ª letra: ")
        if len(letra) == 1 and letra.isalpha():
            tupla_letras+=(letra.lower(),)
        else:
            print("Letra no correcta. Introduzca solo una letra.")

    print(tupla_letras)
     
# --- Lista de palabras sin letras prohibidas ---
    
    lista_limpia = []
    for palabra in lista_palabras:
        if not any(letra in palabra for letra in tupla_letras):
            lista_limpia.append(palabra)

    print(lista_limpia)
    
limpiador_listas()
                 
