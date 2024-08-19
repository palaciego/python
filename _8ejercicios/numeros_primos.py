''' 
Crea un programa que imprima todos los 
números primos entre el 2 y el 100. Un numero 
primo es un numero positivo y entero mayor que 
uno que no tiene un divisor positivo y entero 
que no sea 1 o sí mismo.
'''

for num in range(2,101):
    primo = True
    i = 2
    while primo == True and i < num:
        if num % i == 0:
            primo = False
        i += 1
        
    if primo:
        print(num)

# --- bucle que recorra los numeros del 2 al 100
for num in range(2,101):
    primo = True
    # --- para dicho numero, hay alguno que sea su divisor
    for i in range(2,num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)