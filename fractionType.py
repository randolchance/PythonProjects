class frac:
    def reduce(self,num,den):
        if type(num) is frac:
            den *= num.denominator
            num = num.numerator
        elif type(num) is float:
            num = int(num)
        if type(den) is frac:
            num *= den.denominator
            den = den.numerator
        elif type(den) is float:
            den = int(den)
        if den < 0:
            num *= -1
            den *= -1
        factors_num = findFactors(num)
        factors_den = findFactors(den)
        tempList = [x for x in factors_den]
        for x in tempList:
            if x in factors_num:
                factors_num.remove(x)
                factors_den.remove(x)
        numerator = 1
        for x in factors_num:
            numerator *= x
        denominator = 1
        for x in factors_den:
            denominator *= x
        self.numerator = numerator
        self.denominator = denominator

    def num(self):
        return(self.numerator)
    def den(self):
        return(self.denominator)
    
    def __init__(self,num,den):
        self.reduce(num,den)
    def __str__(self):
        return(f"{self.numerator}/{self.denominator}")
    def __int__(self):
        return(int(float(self)))
    def __float__(self):
        return(self.numerator/self.denominator)
    def __add__(self,x):
        if type(x) is int or type(x) is float:
            return(frac(int(x)*self.denominator + self.numerator,self.denominator))
        elif type(x) is frac:
            return(frac(self.numerator*x.denominator+self.numerator*self.denominator,self.denominator*x.denominator))
        return(self)
    def __radd__(self,x):
        return(self.__add__(x))
    def __sub__(self,x):
        return(self.__add__(-x))
    def __rsub__(self,x):
        return(self.__add__(-x))
    def __mul__(self,x):
        if type(x) is int or type(x) is float:
            return(frac(int(x)*self.numerator,self.denominator))
        elif type(x) is frac:
            return(frac(x.numerator*self.numerator,x.denominator*self.denominator))
        return(self)
    def __rmul__(self,x):
        return(self.__mul__(x))
    def __truediv__(self,x):
        if type(x) is int or type(x) is float:
            return(self.__mul__(frac(1,int(x))))
        elif type(x) is frac:
            return(self.__mul__(frac(x.denominator,x.numerator)))
        return(self)
    def __rtruediv__(self,x):
        return(frac(x*self.denominator,self.numerator))
    def __pow__(self,x):
        return(frac(self.numerator**x,self.denominator**x))
    def __neg__(self):
        return(frac(-self.numerator,self.denominator))
    def __pos__(self):
        return(self)
    def __abs__(self):
        return(frac(abs(self.numerator),self.denominator))
    def __eq__(self,x):
        return(self.numerator == x.numerator and self.denominator == x.denominator)
    def __ne__(self,x):
        return(not self == x)
    def __lt__(self,x):
        return(self.numerator*x.denominator < x.numerator*self.denominator)
    def __gt__(self,x):
        return(self.numerator*x.denominator > x.numerator*self.denominator)
    def __le__(self,x):
        return(self < x or self == x)
    def __ge__(self,x):
        return(self > x or self == x)
