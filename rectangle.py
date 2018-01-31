class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def area(self):
        return(self.length*self.width)
    def isSquare(self):
        isNot = ["","not "]
        print(f"I am {isNot[self.length!=self.width]}a square!")

rect = Rectangle(5,5)
rect.area()
rect.isSquare()

rect2 = Rectangle(5,6)
rect2.area()
rect2.isSquare()
