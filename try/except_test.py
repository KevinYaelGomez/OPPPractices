age = input("Ingresa tu edad: ")
try:
    age = int(age)
except ValueError:
    print("El valor ingresado no es valido")