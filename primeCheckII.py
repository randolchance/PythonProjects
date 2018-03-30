from math import sqrt
from memoise import Memoise

class IsPrime:
    def __init__(self):
        self.prime_dict = {}
        self.prime_list = []
    def __call__(self,x):
        if x not in self.prime_dict:
            self.prime_dict[x] = self.isPrime(x)
        return(self.prime_dict[x])
    def isPrime(self,x):
        if x == 2:
            return(True)
        if x == 1 or x%2 == 0 or x == 0:
            return(False)
        max_x = int(sqrt(x))
        
        def _noList(j=3):
            while j <= max_x:
                if self.isPrime(j):
                    if x%j == 0:
                        return(False)
                j += 2
            return(True)

        start_j = 3
        if self.prime_list:
            if x >= self.prime_list[0]:
                for i in self.prime_list:
                    if x == i or i > max_x:
                        return(True)
                    elif x%i == 0:
                        return(False)
                    else:
                        start_j = i
        else:
            pass
        return(_noList(start_j))


PrimeCheck = IsPrime()
def primes(k=2,f=-1):
    i = 2
    while f == -1 or i < f:
        if PrimeCheck(i):
            if i >= k:
                yield(i)
        i += (i%2!=0 and i!=1) + 1
