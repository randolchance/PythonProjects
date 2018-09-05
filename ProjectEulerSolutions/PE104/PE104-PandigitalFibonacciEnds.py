# PROJECT EULER PROBLEM 104 - Pandigital Fibonacci Ends


class fib:
    def __init__(self):
        self.fib_dict = {1:1, 2:1}
    def __call__(self,n):
        if n in self.fib_dict:
            return(self.fib_dict[n])
        else:
            return(self.fib(n))
    def fib(self,n):
        if n == 1 or n == 2:
            return(1)
        F = self.fib_dict[n-1] + self.fib_dict[n-2]
        del self.fib_dict[n-2]
        self.fib_dict[n] = F
        return(F)

Fib = fib()


pandigitalset = set([str(i) for i in range(1,10)])

n = 1
RUN = True
while RUN:
    F = Fib(n)
    str_F = str(F)
    if len(str_F) >= 9:
        if set(str_F[-9:]) == pandigitalset and set(str_F[:9]) == pandigitalset:
            print(n)
            break
    n += 1

