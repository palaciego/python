Margarita=13.0
Napolitana=14.0
Cuatro=15.5

Chorizo=1.0
Chedar=1.5
Chipotle=2.75


dinero=float(input("¿Cuanto dinero tienes?"))
resto=0
total=0
pedido=[]

print("---Pizzeria Perales---")

print(f"Tiene: {dinero} $")
while True:
    print("Elija la pizza:")
    print(f"1: Margarita - {Margarita} $")
    print(f"2: Napolitana - {Napolitana} $")
    print(f"3: Cuatro Quesos - {Cuatro} $")
    eleccion=int(input())

    match eleccion:
        case 1:
            print(f"Ha elegido usted la pizza Margarita cuyo precio es {Margarita} $ ")
            dinero-=Margarita
            print(f"Le queda {round(dinero,2)} $")
            total+=Margarita
            pedido.append(f" Mi pedido es Margarita - {Margarita} $")
            break
        case 2:
            print(f"Ha elegido usted la pizza Napolitana cuyo precio es {Napolitana} $")
            dinero-=Napolitana
            print(f"Le queda {dinero} $")
            total+=Napolitana
            pedido.append(f" Mi pedido es Napolitana - {Napolitana} $")
            break
        case 3:
            print((f"Ha elegido usted la pizza Cuatro Quesos cuyo precio es {Cuatro} $"))
            dinero-=Cuatro
            print(f"Le queda {dinero} $")
            total+=Cuatro
            pedido.append(f" Mi pedido es Napolitana - {Cuatro} $")
            break
        case _:
            print("Ha elegido una opcion incorrecta, vuelva a intentarlo.")

 
  
while True:

    print("Elija el extra:")
    print(f"1: Chorizo - {Chorizo} $")
    print(f"2: Chedar - {Chedar} $")
    print(f"3: Chipotle - {Chipotle} $")
    print(f"4: Ninguno más")
    extra=int(input()) 

    match extra:
        case 1:
            print(f"Ha elegido usted el extra Chorizo cuyo precio es {Chorizo} $ ")
            dinero-=Chorizo
            print(f"Le queda {round(dinero,2)} $")
            total+=Chorizo
            pedido.append(f" Mi pedido extra de Chorizo - {Chorizo} $")    
        case 2:
            print(f"Ha elegido usted el extra Chedar cuyo precio es {Chedar} $")
            dinero-=Chedar
            print(f"Le queda {round(dinero,2)} $")
            total+=Chedar
            pedido.append(f" Mi pedido extra de Chedar - {Chedar} $")
            
        case 3:
            print((f"Ha elegido usted el extra Chipotle cuyo precio es {Chipotle} $"))
            dinero-=Chipotle
            print(f"Le queda {round(dinero,2)} $")
            total+=Chipotle
            pedido.append(f" Mi pedido extra de Chipotle - {Chipotle} $")    
        case 4:
            print("De acuerdo. No habrá ningún ingrediente extra más") 
            break   
        case _:
            print("Ha elegido una opcion incorrecta, vuelva a intentarlo.")

           
if total >= dinero: 


    print("---Su pedido---")
    print(f"El Total Pedido es {total} $")
    print(f"Cambio es {dinero} $")
    
    for i in pedido:
        print(f"-{i}-")
    print("Muchisimas gracias por su visita. Vuelva pronto.")

else: print("No tiene suficiente dinero. Vuelva a elaborar su pedido, por favor")