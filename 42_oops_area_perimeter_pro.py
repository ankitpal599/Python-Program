#Python program to create Rectangle class with length and width as attributes and methods to calculate and diplay area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length + self.width)
rect1 = Rectangle(8, 12)
print("Area:",rect1.area())
print("Perimeter:",rect1.perimeter())  
