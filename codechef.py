import abc


from abc import ABC ,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class squre(shape):
    type = "squre"
    sides = 4

    def __init__(self):
        self.lenth = 4
    
    def printarea(self):
        return self.lenth * self.lenth


print(squre.printarea)