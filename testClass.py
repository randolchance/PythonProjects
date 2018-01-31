class myClass:
    def __init__(self):
        self.myStr = ""
    
    def getString(self):
        self.myStr = input()

    def printString(self):
        print(self.myStr)

testClass = myClass()
testClass.getString()
testClass.printString()
    
