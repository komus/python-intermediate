# Abstract class
# square, rectangle, parallelogram 
# They have some attributes in common
# e.g Area, perimeter
# We can create abstract class for the commonality between our objects

# To create an abstract class, import abc. abc means Abstract Base Class

from abc import ABC, abstractmethod

class FourSidedObjects(ABC):
    @abstractmethod #This is a decorator, and it means that the method is an abstract method
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# class square is extending the functionalities of Abstract class FourSidedObjects
class Square(FourSidedObjects):
    def __init__(self, length):
        self.len = length

    def area(self):
        return self.len * self.len

    def perimeter(self):
        return self.len * 4


sqr = Square(10)
print(sqr.area())
