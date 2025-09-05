class Stack():
    def __init__(self, startingStackAsList = None):
        if startingStackAsList is None:
            self.dataList = []
        else:
            self.dataList = startingStackAsList[:] #[:] -> Crea una copia del la lista

    def push(self, item):
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element
    
    def peek(self):
        item = self.dataList[-1] #-1 -> Inicia desde el ultimo elemento guardado en la lista
        return item
    
    def getSize(self):
        nElements = len(self.dataList)
        return nElements
    
    def show(self):
        print('El stack es de:')
        for value in reversed(self.dataList):
            print(' ', value)