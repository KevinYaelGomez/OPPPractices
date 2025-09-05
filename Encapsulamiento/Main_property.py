from PropertyDecorator import *

oStudent0 = Student("Armando Casas")
oStudent1 = Student("Rosa Melano")

print(oStudent0.grade)
print(oStudent1.grade)
print()

oStudent1.grade = 85
oStudent0.grade = 92

print(oStudent0.grade)
print(oStudent1.grade)  