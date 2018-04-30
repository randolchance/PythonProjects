from collections import Counter

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

# Takes a list of a range of indices and creates a generator of lists of all
# possible combinations
def combine(aList):
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
                        a = iList[x]+y
                        notDupe = True
                        for z in newList:
                            if Counter(a) == Counter(z):
                                notDupe = False
                                break
                        if notDupe:
                            newList.append(a)
            yield(newList)
            oldList = [x for x in newList]


# Takes a list of indices and a value R, 0<=R<=len(aList), where R
# is r in nCr, and returns a list of all the possible combinations of R
# items out of n = len(aList) items
def combination(aList,R):
    aList_size = len(aList)
    if R > aList_size:
        R = aList_size
    if aList_size == 0 or R == 0:
        return([])
    elif aList_size == 1 or R == 1:
        return([[x] for x in aList])
    else:
        iList = [[x] for x in aList]
        oldList = [x for x in iList]
        newList = []
        for r in range(R-1):
            newList = []
            for x in range(len(iList)):
                for y in oldList:
                    if iList[x][0] not in y:
                        a = iList[x]+y
                        notDupe = True
                        for z in newList:
                            if Counter(a) == Counter(z):
                                notDupe = False
                                break
                        if notDupe:
                            newList.append(a)
            oldList = [x for x in newList]
        return(newList)
