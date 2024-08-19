"""/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */"""

def tenis():
    count1=0
    count2=0
    resultados={0:"Love",1:"15",2:"30",3:"45"}
    secuencia=["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    
    
    for i in secuencia:
        if i =="P1":
            count1+=1
        elif i =="P2":
            count2+=2
        else: print("input incorrecto")
    print(f"{resultados[count1]} - {resultados[count2]}")

tenis()
    
    
