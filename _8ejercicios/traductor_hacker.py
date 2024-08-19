"""/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */"""
hacker_dic = {
        "a": "4",
        "b": "I3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "1",
        "m": "||//",
        "n": "^/",
        "o": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2v",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "w": "|/||",  
        "x": "><",
        "y": "j",
        "z": "2",
        " ": " "  
    }
def hacker():
   
    frase=input("escriba aqui su frase: \n").lower()
    transform=""                   #transform = ''.join(hacker_dic.get(letra, letra) for letra in frase)
    for letra in frase:
        for hack in hacker_dic:
            if letra==hack:
                transform+= hacker_dic[hack]

    print(transform)
       
hacker()