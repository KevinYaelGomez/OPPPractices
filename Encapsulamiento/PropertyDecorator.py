class Student():
    def __init__(self, name, startingGrade = 0):
        self.__name = name
        self.grade = startingGrade

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('El nuevo grado: ' + str(newGrade) + ', es un caracter invalido')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('El nuevo grado: ' + str(newGrade) + ', debe de ser entre 0 y 100.')
        self.__grade = newGrade

       