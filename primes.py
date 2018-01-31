from math import sqrt
from collections import Counter

def primes(x0,xf):
    for x in range(x0, xf+1):
        prime = True
        for y in range(2,int(sqrt(x))+1):
            if x%y==0 and x/y!=1:
                prime = False
                break
        if prime:
            yield(x)

def digitList(x, digits=3):
    li = []
    for i in range(digits,-1,-1):
        li.append(int(x%(10**(i+1))/(10**i)))
    return(li)


primeList = list(primes(1000,9999))

for i in range(len(primeList)):
    for j in range(i+1, len(primeList)):
        if Counter(digitList(primeList[i])) == Counter(digitList(primeList[j])):
            for k in range(j+1, len(primeList)):
                if Counter(digitList(primeList[i])) == Counter(digitList(primeList[k])):
                    if (primeList[j] - primeList[i]) == (primeList[k] - primeList[j]):
                        print(str(primeList[i])+str(primeList[j])+str(primeList[k]))
                        print("Difference of: " + str(primeList[k]-primeList[j]))
                    
