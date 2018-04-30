# We're not getting fancy here. The irrational is considered a sqrt and positive
# If a negative value is given to the irrational part, it will be taken
# to mean the sqrt(ir) value is negative, not imaginary
# WILL NOT accept an IR as an input for anything
from math import sqrt

# Returns the number of nested IR types in the irrational part of an IR type
def len_IR(ir):
    if type(ir) is IR:
        if type(ir.Ir()) is IR:
            return(1 + len_IR(ir.Ir()))
        else:
            return(1)
    else:
        return(0)

# Reduces (if possible) a given IR type
def reduce(ir):
    if type(ir) is IR:
        irrational = ir.Ir()
        factor = ir.Fa()
        whole = ir.Wh()
        
        if type(irrational) is IR:
            irrational = reduce(irrational)

        # Check to see if the reduced irrational part is a perfect square
        if type(irrational) is not IR:
            max_x = int(sqrt(irrational))
            x = 2
            while x <= max_x:
                y = irrational/(x**2)
                if y == 1:
                    whole = whole + factor*x
                    irrational = 0
                    break
                elif y%1 == 0:
                    irrational = int(y)
                    factor = factor*x
                    max_x = int(sqrt(irrational))
                    x = 2
                else:
                    x += 1
        
        # This should never have to happen
        #if type(factor) is IR:
        #    factor = reduce(factor)

        if type(whole) is IR:
            whole = reduce(whole)

        if irrational == 0:
            return(whole)
        
        # Check to see if the irrational part can be merged with a term in the whole part
        node = whole
        while type(node) is IR:
            if irrational == node.Ir():
                node.setFa(node.Fa() + factor)
                irrational = 0
                break
            else:
                node = node.Wh()
        if irrational == 0:
            return(whole)
        else:
            return(IR(irrational,whole,factor))
        
    else:
        return(ir)

class IR:
    def Ir(self):
        return(self.irrational)
    def Wh(self):
        return(self.whole)
    def Fa(self):
        return(self.factor)
    def setIr(self,x):
        self.irrational = x
        return(x)
    def setWh(self,x):
        self.whole = x
        return(x)
    def setFa(self,x):
        self.factor = x
        return(x)

    def checkInt(self,x):
        if type(x) is float:
            if x%1 == 0:
                return(int(x))
            else:
                return(float(x))
        elif type(x) is int:
            return(x)
        elif type(x) is IR:
            x.setIr(self.checkInt(x.Ir()))
            x.setWh(self.checkInt(x.Wh()))
            x.setFa(self.checkInt(x.Fa()))
            return(x)
        else:
            raise ValueError
    
    def __init__(self,ir,wh=0,irFa=1):
        if type(irFa) is IR:
            whole = IR(ir*irFa.Ir(),wh,irFa.Fa())
            whole = reduce(whole)
            wh = whole
            irFa = irFa.Wh()
        
        if type(ir) is IR:
            if (ir.Fa() < 0 and ir.Wh() < 0) or float(ir) < 0:
                self.factor = -irFa
                ir.setFa(-ir.Fa())
                ir.setWh(-ir.Wh())
            else:
                self.factor = irFa
            self.irrational = ir
        else:
            if ir < 0:
                self.factor = -irFa
            else:
                self.factor = irFa
            self.irrational = abs(ir)
        self.whole = wh
        
    def __str__(self):
        if self.factor > 0:
            if self.factor == 1:
                str_fa = ""
            else:
                str_fa = str(self.factor)
        elif self.factor < 0:
            if self.factor == -1:
                str_fa = "-"
            else:
                str_fa = str(self.factor)
        else:
            str_fa = ""

        if self.factor == 0 or self.irrational == 0:
            str_ir = ""
        else:
            str_ir = "√(" + str(self.irrational) + ")"

        if type(self.whole) is not IR:
            if self.whole > 0:
                if self.factor == 0 or self.irrational == 0:
                    str_wh = str(self.whole)
                else:
                    str_wh = "+" + str(self.whole)
            elif self.whole < 0:
                str_wh = str(self.whole)
            else:
                str_wh = ""
        else:
            if self.whole.Fa() > 0:
                str_wh = "+" + str(self.whole)
            else:
                str_wh = str(self.whole)
        
        return(str_fa + str_ir + str_wh)
    
    def __float__(self):
        return(float(self.factor)*sqrt(float(self.irrational))+float(self.whole))
    
    def __int__(self):
        return(int(float(self)))
    
    def __neg__(self):
        return(IR(self.irrational,-self.whole,-self.factor))
    
    def __add__(self,x):
        if type(x) is IR:
            if self.irrational == x.Ir():
                factor = self.factor+x.Fa()
                if factor == 0:
                    return(self.whole+x.Wh())
                else:
                    return(IR(self.irrational,self.whole+x.Wh(),self.factor+x.Fa()))
            elif self.irrational < x.Ir():
                return(IR(self.irrational,IR(x.Ir(),self.whole+x.Wh(),x.Fa()),self.factor))
            else:
                return(IR(x.Ir(),IR(self.irrational,self.whole+x.Wh(),self.factor),x.Fa()))
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
            if self.irrational == x.Ir():
                irrational = self.irrational
                whole = self.checkInt(self.factor*x.Fa()*self.irrational+self.whole*x.Wh())
                factor = self.checkInt(self.factor*x.Wh()+x.Fa()*self.whole)
                return(reduce(IR(irrational,whole,factor)))
            else:
                irrational = self.checkInt(self.irrational*x.Ir())
                whole = IR(self.irrational,self.checkInt(self.whole*x.Wh()),self.checkInt(self.factor*x.Wh()))
                whole = IR(x.Ir(),whole,self.checkInt(self.whole*x.Fa()))
                factor = self.checkInt(self.factor*x.Fa())
                return(reduce(IR(irrational,whole,factor)))
        else:
            return(IR(self.irrational,self.whole*x,self.factor*x))
            
    def __rmul__(self,x):
        return(self*x)
    
    def __truediv__(self,x):
        if type(x) is IR:
            if self == x:
                return(1)
            else:
                mag = reduce(x)
                fac = 1
                mag_len = len(mag)
                while type(mag) is IR:
                    inv = IR(mag.Ir(),-mag.Wh(),mag.Fa())
                    mag = reduce(mag*inv)
                    if len(mag) >= mag_len:
                        return(float(self)/float(x))
                    fac = reduce(fac*inv)
                return(self.checkInt(self*reduce(fac)/mag))
        else:
            return(IR(self.irrational,self.checkInt(self.whole/x),self.checkInt(self.factor/x)))
        
    def __rtruediv__(self,x):
        if type(x) is IR:
            return(x/self)
        else:
            mag = reduce(self)
            fac = 1
            mag_len = len(mag)
            while type(mag) is IR:
                inv = IR(mag.Ir(),-mag.Wh(),mag.Fa())
                mag = reduce(mag*inv)
                if len(mag) >= mag_len:
                    return(x/float(self))
                fac = reduce(fac*inv)
            return(self.checkInt(self*reduce(fac)/mag))
        
    def __eq__(self,x):
        if type(x) is IR:
            return(self.irrational == x.Ir() and self.whole == x.Wh() and self.factor == x.Fa())
        else:
            return(float(self) == x)
    
    def __lt__(self,x):
        if type(x) is IR:
            return((self.factor*sqrt(float(self.irrational))+float(self.whole)) < (x.Fa()*sqrt(float(x.Ir()))+float(x.Wh())))
        else:
            return(float(self) < x)
    
    def __gt__(self,x):
        if type(x) is IR:
            return((self.factor*sqrt(float(self.irrational))+float(self.whole)) > (x.Fa()*sqrt(float(x.Ir()))+float(x.Wh())))
        else:
            return(float(self) > x)
    
    def __le__(self,x):
        return(self<x or self==x)
    
    def __ge__(self,x):
        return(self>x or self==x)

    def __len__(self):
        if type(self.whole) is IR:
            return(1+len(self.whole))
        else:
            if self.whole != 0:
                return(2)
            else:
                return(1)

a = IR(IR(IR(5,3),3),IR(3,IR(IR(IR(5,3),3),3)))
print(a, len_IR(a))
b = reduce(a)
print(b, len_IR(b))
c = 5
print(c, len_IR(c))
