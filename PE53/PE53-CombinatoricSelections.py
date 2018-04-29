"""
PROJECT EULER PROBLEM 53 - Combinatoric Selections
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / (r!(n−r)!)

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr,
for 1 ≤ n ≤ 100, are greater than one-million?
"""

def reducedFactorial(n,r):
    if type(r) is not int or type(n) is not int or r < 0 or n < 0:
        return("Program yourself a Gamma function, ass.")
    elif n == 0 and r != 0:
        if r == 1:
            return(1)
        else:
            return(1/(r*reducedFactorial(r-1,1)))
    elif n != 0 and r == 0:
        if n == 1:
            return(1)
        else:
            return(n*reducedFactorial(n-1,1))
    elif r > n:
        return(1/(r*reducedFactorial(r-1,n)))
    elif n == r:
        return(1)
    else: # n > r
        return(n*reducedFactorial(n-1,r))

def combinations(n,r):
    if n < r:
        return("This makes no sense")
    t = n-r
    s = (r >= t)*r + (r < t)*t
    t = n-s
    return(int(reducedFactorial(n,s)/reducedFactorial(t,1)))

threshold = 1000000
count = 0
count_list = []
for n in range(2,101):
    for r in range(1,n):
        nCr = combinations(n,r)
        if nCr > threshold:
            count += 1
            count_list.append([n,r,nCr])
print(count)
            
            
