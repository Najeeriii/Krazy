from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display(self):
        return f"{self.name}: Area = {self.area()}, Perimeter = {self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


if __name__ == "__main__":
    
    rectangle = Rectangle(10, 5)
    square = Square(7)

    
    print(rectangle.display())
    print(square.display())