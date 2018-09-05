# PROJECT EULER PROBLEM 230 - Fibonacci Words


from memoise import Memoise

def _N(n):
    return((127+19*n)*7**n)

@Memoise
def fib(n):
    if n == 1 or n == 2: return(1)
    else: return(fib(n-2)+fib(n-1))

def findFibDigit(p,fib_n):
    n = fib_n
    F = fib(n)
    if p > F:
        return(None)
    while p > 2:
        F_1 = fib(n-1)
        F_2 = fib(n-2)
        if p > F_2:
            n -= 1
            p -= F_2
        else:
            n -= 2
    return((p+n%2)%2+1)


A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
AorB = (A,B)

l = []
total = 0
for n in range(18):
    N = _N(n)-1
    p = N//100+1
    Y = N%100
    i = 1
    K = 1
    while K < p:
        K = fib(i)
        i += 1
    i -= 1
    k = findFibDigit(p,i)-1
    
    d = int(AorB[k][Y])
    total += 10**n*d


print(total)

