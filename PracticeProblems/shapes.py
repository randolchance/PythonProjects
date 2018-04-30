class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width= w
    def area(self):
        return(self.length*self.width)
    def isSquare(self):
        isNot = ["","not "]
        print(f"I am {isNot[self.length!=self.width]}a square!")

sha = Shape()
print(sha.area())

rect = Rectangle(5,5)
print(rect.area())
rect.isSquare()

rect2 = Rectangle(5,6)
print(rect2.area())
rect2.isSquare()
