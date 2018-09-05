# PROJECT EULER PROBLEM 23 - Non-abundant Sums


from findFactors import findFactors
from findDivisors import findDivisors
from memoise import Memoise

@Memoise
def findDivisorsII(x):
    return(findDivisors(findFactors(x)))

@Memoise
def isAbundant(x):
    return(x < sum(findDivisorsII(x)[:-1]))

def isSumOfAbundants(X):
    return(any([isAbundant(x) and isAbundant(X-x) for x in range(X//2+1)]))



total = sum([x for x in range(28124) if not isSumOfAbundants(x)])
print(total)


