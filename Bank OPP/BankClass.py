from BankOPP import *

class Bank():
    def __init__(self, hora, direccion, telefono):
        self.accountDict = {}
        self.nextAccountNum = 0
        self.hora = hora
        self.direccion = direccion
        self.telefono = telefono

    def validAccountNum(self):
        accountNum = input("Ingresa el numero de cuenta: ")
        try:
            accountNum = int(accountNum)
        except ValueError:
            raise AbortTransaction('Solo se aceptan numeros')
        if accountNum not in self.accountDict:
            raise AbortTransaction('No existe la cuenta ' + str(accountNum))
        return accountNum
    
    def getUserAccount(self):
        accountNum = self.validAccountNum()
        oAccount = self.accountDict[accountNum]
        return oAccount 

    def createAccount(self, name, balance, password):
        oAccount = Cuenta(name, balance, password)
        keyAccountNum = self.nextAccountNum
        self.accountDict[keyAccountNum] = oAccount
        self.nextAccountNum = self.nextAccountNum + 1
        return keyAccountNum
    
    def newAccount(self):
        print("***Nueva cuenta***")
        nameInput = input("Ingresa el nombre de la cuenta: ")
        balanceInput = input("Ingresa el balance inicial: ")
        balanceInput = int(balanceInput)
        passwordInput = input("Ingresa la contraseña: ")
        numAccount = self.createAccount(nameInput, balanceInput, passwordInput)
        print("El numero de cuenta es: ", numAccount, "\n")

    def deleteAccount(self):
        print("***Eliminar cuenta***")
        oAccount = self.getUserAccount()
        passwordInput = input("¿Cual es tu contraseña: ")
        oAccount.checkPassword(passwordInput)
        data = oAccount.obtenerBalance()
        print("La cuenta tiene", data, "que seran regresados")
        del self.accountDict[self.validAccountNum()]
        print("Cuenta eliminada\n")

    def balanceIntput(self):
        print("***Balance***")
        oAccount = self.getUserAccount()
        passwordInput = input("¿Cual es tu contraseña: ")
        oAccount.checkPassword(passwordInput)
        balance = oAccount.obtenerBalance()
        print("El balance es de:", balance,"\n")

    def depositoInput(self):
        print("***Deposito***")
        oAccount = self.getUserAccount()
        depositAmount = input("ingresa la cantidad a depositar: ")
        passwordInput = input("¿Cual es tu contraseña: ")
        oAccount.checkPassword(passwordInput)
        balance = oAccount.depositar(depositAmount)
        print("Depositado:", depositAmount)
        print("Tu nuevo balance es de:", balance,"\n")

    def retiroInput(self):
        print("***Retiro***")
        oAccount = self.getUserAccount()
        retiroAmount = input("Ingresa la cantidad a retirar: ")
        passwordInput = input("¿Cual es tu contraseña: ")
        oAccount.checkPassword(passwordInput)
        balance = oAccount.retiro(retiroAmount)
        print("Cantidad retirada:", retiroAmount)
        print("Tu balance es de:", balance,"\n")

    def getInfo(self):
        print("Horario:", self.hora)
        print("Direccion:", self.direccion)
        print("Telefono:", self.telefono)
        print("Numero de cuentas:", len(self.accountDict),"\n")

    def show(self):
        for numAccount in self.accountDict:
            oAccount = self.accountDict[numAccount]
            print("Numero de cuenta:", numAccount)
            oAccount.show()
            print()