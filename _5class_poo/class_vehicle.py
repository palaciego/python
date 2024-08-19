class Moto():

    estado="nueva"
    motor=False
    def __init__(self,color,matricula,combustible_litros,ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        self.color="azul"
        self.matricula="1234SSDF"
        self.combustible_litros=0
        self.marca=1
        self.modelo=1
        self.fecha_fabricacion=1
        self.velocidad_punta=1
        self.peso=1
        self.ruedas=4

    def arrancar(self):
        if self.motor:
            print("ya está encendido")
        else: print("Está apagado, arrancamos")
    def detener(self):
        if self.motor:
            print("el motor se detiene")
        else: print("ya está apagado")

    def consultar_precio(self):
        print(f"El precio de la moto es de {self.precio} y tiene {self.ruedas}")

motocicleta_yamaha1= Moto("Roja","ADADSD132",10, 2,"Yamaha",1,1990,200,300)

motocicleta_harley=Moto(
    matricula="DASDASD1234",
    combustible_litros=7,
    color="Morado",
    marca=123,
    peso=44,
    ruedas=3,
    fecha_fabricacion=1991,
    velocidad_punta=190,
    modelo=32
)
motocicleta_harley.detener()
motocicleta_harley.precio= 5000

motocicleta_yamaha1.precio=2440
Moto.consultar_precio(motocicleta_harley)
Moto.consultar_precio(motocicleta_yamaha1)

def construir_perfil(nombre, *apellido, **info):
    perfil = {}
    perfil['nombre'] = nombre
    perfil['apellido'] = ' '.join(apellido)
    for key, value in info.items():
        perfil[key] = value
    return perfil

# Example usage:
perfil = construir_perfil('Juan', 'Perez', 'Gonzalez', edad=30, ciudad='Madrid', profesion='Ingeniero')
print(perfil)