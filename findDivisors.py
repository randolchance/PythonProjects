"""
Iterates through the divisors generated by a given set of factors
(which may or may not include a value of 1)
"""
def findDivisors(factors):
    if len(factors) == 0:
        return([])
    else:
        divisors = list(sorted(set(factors)))
        if 1 not in divisors:
            divisors  = [1] + divisors
        else:
            factors.remove(1)
        iList = [[x] for x in range(len(factors))]
        oldList = [x for x in iList]
        for r in range(len(factors)):
            newList = []
            for x in range(len(iList)):
                for y in oldList:
                    if iList[x][0] not in y:
                        a = iList[x]+y
                        A = 1
                        for i in a:
                            A *= factors[i]
                        notDupe = True
                        for z in newList:
                            Z = 1
                            for i in z:
                                Z *= factors[i]
                            if A == Z:
                                notDupe = False
                                break
                        if notDupe:
                            newList.append(a)
                            divisors.append(A)
            oldList = [x for x in newList]
        divisors.sort()
        return(divisors)

def generateDivisors(factors):
    divisors = findDivisors(factors)
    if len(divisors) == 0:
        yield([])
    for d in divisors:
        yield(d)

def countDivisors(factors):
    return(len(findDivisors(factors)))
