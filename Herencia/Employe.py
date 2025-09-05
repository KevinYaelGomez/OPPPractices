class Employe():
    def __init__(self, name, title, ratePerHour = None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name
    
    def getTitle(self):
        return self.title
    
    def payPerYear(self):
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay
    