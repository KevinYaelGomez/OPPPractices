from BankOPP import *

accountDict = {}
nextAccountNumber = 0

oAccount = Cuenta("Jose", 300, "papas") 
joseAccountNum = nextAccountNumber 
accountDict[joseAccountNum] = oAccount 
nextAccountNumber = nextAccountNumber + 1
#Primero se crea un objeto, despues se crea una variable que toma el valor de nextAccountNumber con el objetivo de funcionar como key del diccionario, despues se guarda el objeto dentro del la key asignada y se aumenta el valor de la variable nextAccountNumb para la usar el nuevo valor como otra key

oAccount = Cuenta("Martha", 400, "lapiz")
marthaAccountNum = nextAccountNumber
accountDict[marthaAccountNum] = oAccount
nextAccountNumber = nextAccountNumber + 1

accountDict[joseAccountNum].show()
accountDict[marthaAccountNum].show()
print()

def obtenerNumDic():
    respuesta = input("Ingrese su numero de cuenta: ")
    respuesta = int(respuesta)
    return respuesta

while True:
    print("***Banco***")
    print("presiona los caracteres para realizar las siguentes operaciones\n 'N' para crear una nueva cuenta\n 'B' para mostrar el balance de su cuenta\n 'D' para depositar en tu cuenta\n 'R' para retirar de tu cuenta\n 'M' para mostrar los datos de la cuenta\n 'S' para salir\n")
    respuesta = input("¿Que deseas hacer?: ")
    respuesta = respuesta.lower()
    respuesta = respuesta[0]

    if respuesta == 'n':
        print("***Crear nueva cuenta***\n")
        newName = input("¿Cual es el nombre de la cuanta?: ")
        newBalance = input("¿Cual es el balance inicial?: ")
        newBalance = int(newBalance)
        newPassword = input("¿Cual es la contraseña?: ")
        oAccount = Cuenta(newName, newBalance, newPassword)
        newCuenta = nextAccountNumber
        accountDict[newCuenta] = oAccount
        nextAccountNumber = nextAccountNumber + 1
    
    elif respuesta == 'b':
        print("***Balance***")
        accountNum = obtenerNumDic()
        accountPassword = input("Ingrese su contraseña: ")
        oAccount = accountDict[accountNum]
        balance = oAccount.obtenerBalance(accountPassword)
        if balance is not None:
            print("Tu balance es de:", balance,"\n")

    elif respuesta == 'd':
        print("***Deposito***")
        accountNum = obtenerNumDic()
        accountPassword = input("Ingrese la contraseña: ")
        accountDepo = input("Ingrese la cantida a depositar: ")
        accountDepo = int(accountDepo)
        oAccount = accountDict[accountNum]
        balance = oAccount.depositar(accountDepo, accountPassword)
        if balance is not None:
            print("Su nuevo balance es de:", balance, "\n")

    elif respuesta == 'r':
        print("***Retiro***")
        accountNum = obtenerNumDic()
        accountPassword = input("Ingresa la contraseña: ")
        accountRet = input("Ingresa la cantidad a retirar: ")
        oAccount = accountDict[accountNum]
        balance = oAccount.retiro(accountRet, accountPassword)
        if balance is not None:
            print("Tu nuevo balance es de:", balance, "\n")

    elif respuesta == 'm':
        print("***Mostrar datos***")
        for accountNum in accountDict:
            oAccount = accountDict[accountNum]
            print("Numero de cuenta:", accountNum)
            oAccount.show()
    
    elif respuesta == 's':
        print("Hasta luego")
        break

    else:
        print("Opcion invalida\n")