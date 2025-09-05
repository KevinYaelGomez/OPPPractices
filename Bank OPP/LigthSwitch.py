class LigthSwicht():
    def __init__(self):
        self.lightOn = False

    def swichtON(self):
        if self.lightOn == True:
            print("El foco ya estaba encendido\n")
        else:
            self.lightOn = True
            print("El foco se encendio\n")

    def swichtOFF(self):
        if self.lightOn == False:
            print("El foco ya estaba apagado\n")
        else:
            self.lightOn = False
            print("El foco se apago\n")    

ligthSwicht = LigthSwicht()

while True:
    print("Presiona 0 para apagar el foco, 1 para encenderlo y 2 para salir")
    respuesta = input("¿Que deseas hacer?: ")
    respuesta = int(respuesta)

    if respuesta == 0:
        ligthSwicht.swichtOFF()

    elif respuesta == 1:
        ligthSwicht.swichtON()

    elif respuesta == 2:
        print("Hasta luego")
        break

    else:
        print("Opcion invalida")
        