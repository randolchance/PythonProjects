# We're not getting fancy here. The irrational is considered a sqrt and positive
# If a negative value is given to the irrational part, it will be taken
# to mean the sqrt(ir) value is negative, not imaginary
# WILL NOT accept an IR as an input for anything
from math import sqrt

class IR:
    def ir(self):
        return(self.irrational)
    def wh(self):
        return(self.whole)
    def fa(self):
        return(self.factor)
    
    def reduce(self):
        max_x = int(sqrt(self.irrational))
        for x in range(2,max_x+1):
            y = self.irrational/(x**2)
            if y == 1:
                self.irrational = 0
                self.whole += self.checkInt(self.factor*x)
                break
            elif y%1 == 0:
                self.irrational = int(y)
                self.factor *= x
                break

    def checkInt(self,x):
        if type(x) is float:
            if x%1 == 0:
                return(int(x))
        elif type(x) is int:
            return(x)
        return(float(x))
    
    def __init__(self,ir,wh,irFa=1):
        if type(wh) is IR or type(ir) is IR or type(irFa) is IR:
            raise TypeError("IR given as input")
        if ir < 0:
            self.factor = -irFa
        else:
            self.factor = irFa
        self.irrational = abs(ir)
        self.whole = wh
        
    def __str__(self):
        signWh = self.whole/abs(self.whole)
        if self.irrational == 1:
            str_ir = str(self.factor)
        elif self.irrational == 0:
            str_ir = ""
        else:
            if abs(self.factor) == 1:
                str_ir = "√(" + str(self.irrational) + ")"
            else:
                str_ir = str(self.factor) + "√" + str(self.irrational)
        if self.factor < 0 and not self.irrational == 0:
            signFactor = "-"
        else:
            signFactor = ""
        if self.irrational != 0 and self.factor != 0:
            if signWh == 1:
                signWhole = "+"
            else:
                signWhole = "-"
        else:
            signWhole = ""
        return(f"{signFactor}{str_ir}{signWhole}{abs(self.whole)}")
    
    def __float__(self):
        return(self.factor*sqrt(self.irrational)+self.whole)
    
    def __int__(self):
        return(int(float(self)))
    
    def __neg__(self):
        return(IR(self.irrational,-self.whole,-self.factor))
    
    def __add__(self,x):
        if type(x) is IR:
            if self.irrational == x.irrational:
                return(IR(self.irrational,self.whole+x.whole,self.factor+x.factor))
            else:
                raise TypeError("IR with non-matching irrationals given")
        else:
            return(IR(self.irrational,self.whole+x,self.factor))
        
    def __radd__(self,x):
        return(self + x)
    
    def __sub__(self,x):
        return(self - x)
    
    def __rsub__(self,x):
        return(-self + x)
    
    def __mul__(self,x):
        if type(x) is IR:
            if self.irrational == x.irrational:
                return(IR(self.irrational,self.checkInt(self.factor*x.factor*self.irrational+self.whole*x.whole),self.checkInt(self.factor*x.whole+x.factor*self.whole)))
            else:
                raise TypeError("IR with non-matching irrationals given")
            
    def __rmul__(self,x):
        return(self*x)
    
    def __truediv__(self,x):
        if type(x) is IR:
            if self == x:
                return(1)
            else:
                raise TypeError("IR given as input")
        else:
            return(IR(self.irrational,self.checkInt(self.whole/x),self.checkInt(self.factor/x)))
        
    def __rtruediv__(self,x):
        if type(x) is IR:
            if self == x:
                return(1)
            else:
                raise TypeError("IR given as input")
        else:
            mag = self.factor**2*self.irrational - self.whole**2
            return(IR(self.irrational,self.checkInt(-x*self.whole/mag),self.checkInt(x*self.factor/mag)))
        
    def __eq__(self,x):
        return(self.irrational == x.irrational and self.whole == x.whole and self.factor == x.factor)
    
    def __lt__(self,x):
        return((self.factor*sqrt(self.irrational)+self.whole) < (x.factor*sqrt(x.irrational)+x.whole))
    
    def __gt__(self,x):
        return((self.factor*sqrt(self.irrational)+self.whole) > (x.factor*sqrt(x.irrational)+x.whole))
    
    def __le__(self,x):
        return(self<x or self==x)
    
    def __ge__(self,x):
        return(self>x or self==x)
