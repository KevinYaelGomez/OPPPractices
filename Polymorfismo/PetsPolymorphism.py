class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "dice wauw, wauw, wauw!")

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "dice miaw, miaw, miaw!")

class Chicken():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "dice pio, pio, pio!")

dog0 = Dog("Manchas")
dog1 = Dog("Sr. salchicha")
cat0 = Cat("Bigotes")
cat1 = Cat("Quesadilla")
chiken0 = Chicken("Vicente")
chiken1 = Chicken("Calderon")

petList = [dog0, dog1, cat0, cat1, chiken0, chiken1]

for nPet in petList:
    nPet.speak()