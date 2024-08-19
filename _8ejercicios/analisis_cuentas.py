'''ANALISIS DE VENTAS: 
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los 
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor 
venta.  
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo… 
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250] 
Y otra lista con los días de la semana: 
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“] 
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle 
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la 
semana.  
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se 
reinicie a cero cuando llegue al séptimo día.  '''


def analitycs():
    contador=0
    array_days= [[],
                 [],
                 [],
                 [],
                 [],
                 [],
                 []]
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"]
    ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
                    140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
    
    for i in range (7):
        for j in range (len(ventas)-1):
            array_days[i].append(ventas[j])

    print(array_days)
analitycs()
                   
    
def analizar_ventas():
    # Listas de ventas y días de la semana
    ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
              140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Inicializar un diccionario para sumar las ventas por día de la semana
    ventas_por_dia = {dia: 0 for dia in dias_semana}
    
    # Variable para llevar la cuenta del día de la semana actual
    dia_actual = 0
    
    # Sumar las ventas correspondientes a cada día de la semana
    for venta in ventas:
        dia = dias_semana[dia_actual]
        ventas_por_dia[dia] += venta
        dia_actual = (dia_actual + 1) % 7
    
    # Imprimir las ventas por día de la semana
    for dia, total_ventas in ventas_por_dia.items():
        print(f"{dia}: {total_ventas}")

# Llamar a la función para analizar las ventas
analizar_ventas()
