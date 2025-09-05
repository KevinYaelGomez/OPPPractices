#Bank Account OPP Solution

class AbortTransaction (Exception):
    '''raise this exception to abort a bank transaction'''
    pass

class Cuenta():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validAmount(balance)
        self.password = password

    def validAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('La cantidad debe ser con numeros')
        if amount <= 0:
            raise AbortTransaction('La cantidad debe ser positiva')
        return amount
    
    def checkPassword(self, password):
        if password != self.password:
            raise AbortTransaction('La contraseña es incorrecta')

    def depositar(self, numDeposito):
        numDeposito = self.validAmount(numDeposito)
        self.balance = self.balance + numDeposito
        return self.balance
    
    def retiro(self, numRetiro):
        numRetiro = self.validAmount(numRetiro)
        if numRetiro > self.balance:
            raise AbortTransaction('No puedes retirar mas de lo que tienes en tu cuenta')
        self.balance = self.balance - numRetiro
        return self.balance
    
    def obtenerBalance(self):
        return self.balance
    
    def show(self):
        print("Nombre: ", self.name)
        print("Balance: ", self.balance)
        print("Contraseña: ", self.password)
        print()