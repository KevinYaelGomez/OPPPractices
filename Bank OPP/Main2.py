from BankClass import *

oBank = Bank("9:00 am / 6:00pm", "Enrique Segoviano #1269", "3330580209")

while True:
    print("***Banco***")
    print("presiona los caracteres para realizar las siguentes operaciones\n 'N' para crear una nueva cuenta\n 'V' para borrar una cuenta\n 'B' para mostrar el balance de su cuenta\n 'D' para depositar en tu cuenta\n 'R' para retirar de tu cuenta\n 'M' para mostrar los datos de la cuenta\n 'S' para salir\n")
    respuesta = input("¿Que deseas hacer?: ")
    respuesta = respuesta.lower()
    respuesta = respuesta[0]

    try:
        if respuesta == 'n':
            oBank.newAccount()
        elif respuesta == 'v':
            oBank.deleteAccount()
        elif respuesta == 'b':
            oBank.balanceIntput()
        elif respuesta == 'd':
            oBank.depositoInput()
        elif respuesta == 'r':
            oBank.retiroInput()
        elif respuesta == 'm':
            oBank.show()
        elif respuesta == 's':
            print("Hasta luego")
            break
        else:
            print("Opcion invalida")
        
    except AbortTransaction as error:
        print(error)
