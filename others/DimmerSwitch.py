class DimmerSwitch():
    def __init__(self, label):
        self.label = label
        self.switch = False
        self.brillo = 0

    def turnON(self):
        self.switch = True

    def turnOFF(self):
        self.switch = False

    def masBrillo(self):
        if self.switch < 10:
            self.brillo = self.brillo + 1

    def menosBrillo(self):
        if self.brillo > 0:
            self.brillo = self.brillo - 1

    def show(self):
        print("Label:", self.label)
        print("Ligth is on?:", self.switch)
        print("Brightness:", self.brillo)
        print()

foco1 = DimmerSwitch("Dimmer1")
foco2 = DimmerSwitch("Dimmer2")
foco3 = DimmerSwitch("Dimmer3")

foco1.turnON()
foco1.masBrillo()

foco2.turnON()
foco2.masBrillo()
foco2.masBrillo()

foco3.menosBrillo()

foco1.show()
foco2.show()
foco3.show()

print(type(foco1))
print(foco1)
print()
print(type(foco2))
print(foco2)
print()
print(type(foco3))
print(foco3)
print()