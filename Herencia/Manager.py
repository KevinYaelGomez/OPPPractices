from Employe import *

class Manager(Employe):
    def __init__(self, name, title, salary, reportsList = None):
        self.salary = salary
        if reportsList is not None:
            reportsList = []
        self.reportList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportList
    
    def payPerYear(self, giveBonus = False):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary)
            print(self.name, 'get a bonus for good work')
        return pay


oEmploye1 = Employe('Jose Sanchez', 'Cocinero', 16)
oEmploye2 = Employe('Rosa Melano', 'Cajera', 14)
oManager = Manager('Pica Lucas', 'Manager de Pizzeria', 5500, [oEmploye1, oEmploye2])

print('Employee name:', oEmploye1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmploye1.payPerYear()))
print('Employee name:', oEmploye2.getName())
print('Employee salary:', '{:,.2f}'.format(oEmploye2.payPerYear()))
print()

managerName = oManager.getName()
print('Manager name:', managerName)
print('Manager salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')
reportsList = oManager.getReports()
for oEmplpyee in reportsList:
    print(' ', oEmplpyee.getName(), '(' + oEmplpyee.getTitle() + ')')

