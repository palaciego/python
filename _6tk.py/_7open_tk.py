
archivo = open("archivo.txt", "w")  # modo escritura  
archivo = open("archivo.txt", "r")  # modo lectura
archivo = open("archivo.txt", "a")  # modo añadir
archivo = open("archivo.txt", "w+") # modo leer y escribir. Crea archivo si no existe pero borra si existe.
archivo = open("archivo.txt", "r+") # modo leer y escribir. No crea si no existe el archivo.

archivo.write("Hola, mundo!")       # Escribir datos en el archivo

for line in archivo:
    print(line)                     #lee las lineas del archivo
contenido=archivo.read()
print(contenido)                      #Guarda y lee.
linea=contenido.readline()            #lee primera linea
linea=contenido.readline()            #lee segunda linea
contenido.seek(0)                     #mueve el cursor al 0 por si nos quedamos sin texto para leer
contenido.seek(len(archivo.read()/2)) #Situa el cursor en mitad del texto
contenido.read(11)                    #lee hasta la posicion dada
archivaco= open("archivaco.txt", "a")
lineas= ["\nLinea 1\n", "Linea 2\n", "Linea 3\n"]

archivaco.writelines(lineas)
archivaco[2] = "modifico la linea 3"

with open("n1_archivo.txt","r+") as archivador:
    contenido=archivador.read()
    print(contenido)
    archivador.write("Ester esta muy buena\n")

archivo.close()                     # Cerrar el archivo

#----------------------------------------------------- TK

from tkinter import*
root= Tk()

root.title("De quererte y no quererte")

root.geometry("500x500+750+100")

mensaje1=Label(root, text="Ole los caracoles")
mensaje2=Label(root, text="Como yo la queria")

"""mensaje2.pack()               incompatible con .grid"""
mensaje1.grid(row=0, column=1)
mensaje2.grid(row=1, column=0)
mensaje3=Label(root, text="Reja me quita la vida").grid(row=2, column=2)


root.mainloop()           #Bucle de ejecución