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

def nPr(n,r):
    if n < r:
        return("This makes no sense")
    return(int(reducedFactorial(n,n-r)))

# Takes a list of a range of indices and creates a generator of lists of all
# possible permutations
def permute(aList):
    if len(aList) == 0:
        yield([])
    else:
        iList = [[x] for x in aList]
        yield(iList)
        oldList = [x for x in iList]
        for r in range(len(aList)-1):
            newList = []
            for x in range(len(iList)):
                for y in oldList:
                    if iList[x][0] not in y:
                        newList.append(iList[x]+y)
            yield(newList)
            oldList = [x for x in newList]


# Takes a list of indices and a value R, 0<=R<=len(aList), where R
# is r in nCr, and returns a list of all the possible permutations of R
# items out of n = len(aList) items
def permutation(aList,R):
    aList_size = len(aList)
    if R > aList_size:
        R = aList_size
    if aList_size == 0 or R == 0:
        yield([])
    elif aList_size == 1 or R == 1:
        for x in aList:
            yield([x])
    else:
        iList = [[x] for x in aList]
        oldList = [x for x in iList]
        newList = []
        for r in range(R-1):
            newList = []
            for x in range(len(iList)):
                for y in oldList:
                    if iList[x][0] not in y:
                        newList.append(iList[x]+y)
            oldList = [x for x in newList]
        for n in newList:
            yield(n)
