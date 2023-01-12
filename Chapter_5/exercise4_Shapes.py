class Shapes:

    def __init__(self, side1, side2, side3):
        self.base = side1
        self.side2 = side2
        self.height = side3

    def inputSides():

        base = int(input("Enter the base length of a side/radius (All Shapes): "))
        side2 = int(input("Enter the second side (Rectangle): "))
        height = int(input("Enter the third side/height (Triangle): "))
        return Shapes(base, side2, height)


class Circle(Shapes):

    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
    def area(self):
        print((self.base * self.base) * 3.14)

class Rectangle(Shapes):

    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
        
    def area(self):
        print(self.base * self.side2)

class Triangle(Shapes):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
    
    def area(self):
        print(round((self.base * self.height) / 2, 1))


side = Shapes.inputSides()

print("Circle area:")
circleArea = Circle.area(side)

print("Rectangle area:")
rectangleArea = Rectangle.area(side)

print("Triangle area:")
triangleArea = Triangle.area(side)