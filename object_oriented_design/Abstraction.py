"""
Abstract class for the abstraction of the data
why: Abstraction is important because it allows the user to focus on what the object does instead of how it does it. This makes the code easier to understand and maintain.
"""

from abc import ABC, abstractmethod

class Shape:
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def perimeter(self):
        pass
    
    def draw(self):
        pass
    
    @abstractmethod
    def test(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Circle(Shape):
    def __init__(self, radius=0):
        self.__radius = radius
        
    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def perimeter(self):
        return 2 * 3.14 * self.__radius
    
    def draw(self):
        return "Drawing Circle"
    
    def test(self):
        return "Testing Circle"
    
    
c = Circle(5)
print(c.test())