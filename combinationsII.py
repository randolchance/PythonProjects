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

def nCr(n,r):
    if n < r:
        return("This makes no sense")
    t = n-r
    s = (r >= t)*r + (r < t)*t
    t = n-s
    return(int(reducedFactorial(n,s)/reducedFactorial(t,1)))

def combine(aList,r):
    if r > len(aList):
        raise ValueError("r cannot be bigger than list size")
    elif r == 0:
        yield([])
    elif r == len(aList) or not aList:
        yield(aList)
    else:
        for i in range(len(aList)-(r-1)):
            new_aList = aList[i+1:]
            for a in combine(new_aList,r-1):
                yield([aList[i]]+a)
