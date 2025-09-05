from POO.Herencia.Employe import *
from POO.Herencia.Manager import *

oEmploye1 = Employe('Jose Sanchez', 'Cocinero', 16)
oEmploye2 = Employe('Rosa Melano', 'Cajera', 14)
oManager = Manager('Pica Lucas', 'Manager de Pizzeria', 5500, [oEmploye1, oEmploye2])

print('Employee name:', oEmploye1.getName())
print('Employee salary:', '{:, .2f}'.format(oEmploye1.payPerYear()))
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