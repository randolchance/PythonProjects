# PROJECT EULER PROBLEM 61 - Cyclical Figurate Numbers
from math import sqrt
from math import ceil

def quadSolver(a,b,c):
    in_sqrt = b**2 - 4*a*c
    if in_sqrt < 0:
        return(["Non-real roots!"])
    return([(-b-sqrt(in_sqrt))/2/a,(-b+sqrt(in_sqrt))/2/a])

def TriNum(n):
    return(int(n*(n+1)/2))
def Square(n):
    return(int(n**2))
def PentNum(n):
    return(int(n*(3*n-1)/2))
def HexNum(n):
    return(int(n*(2*n-1)))
def HeptNum(n):
    return(int(n*(5*n-3)/2))
def OctNum(n):
    return(int(n*(3*n-2)))

#Pfn = [A,B] for use in the quadSolver
Pfn = [[] for x in range(9)]
Pfn[3] = [1/2,1/2]
Pfn[4] = [1,0]
Pfn[5] = [3/2,-1/2]
Pfn[6] = [2,-1]
Pfn[7] = [5/2,-3/2]
Pfn[8] = [3,-2]

P = [None for x in range(9)]
P[3] = TriNum
P[4] = Square
P[5] = PentNum
P[6] = HexNum
P[7] = HeptNum
P[8] = OctNum

def numberCheck(aP_,aN,aPmin,aPmax,a,aNumber_list,final):
    while aP_ >= aPmin and aP_ < aPmax:
        if a == 8:
            final_val = aP_ // 100
        else:
            final_val = final
        if not aNumber_list:
            if (aP_ % 100) == final:
                return([[aP_,a,aN]])
            else:
                pass
        else:
            for newA in aNumber_list:
                newPmin = (aP_%100) * 100
                if newPmin >= 1000:
                    newN = ceil(quadSolver(Pfn[newA][0],Pfn[newA][1],-newPmin)[1])
                    newP_ = P[newA](newN)
                    newPmax = newPmin + 100
                    newNumber_list = [x for x in aNumber_list if x != newA]
                    sub_val = numberCheck(newP_,newN,newPmin,newPmax,newA,newNumber_list,final_val)
                    if sub_val:
                        return([[aP_,a,aN]]+sub_val)
                    else:
                        pass
        aN += 1
        aP_ = P[a](aN)
    return(False)

Pmin = 1000
n = ceil(quadSolver(Pfn[8][0],Pfn[8][1],-Pmin)[1])
P_ = P[8](n)
Pmax = 10000
number_list = [3,4,5,6,7]
final_val = 0
result = numberCheck(P_,n,Pmin,Pmax,8,number_list,final_val)
print(result)
total = 0
for r in result:
    total += r[0]
print(total)

#VERIFY 
"""
iP_ = 0
iA = 1
iN = 2
for i in result:
    if P[i[iA]](i[iN]) == i[iP_]:
        print(f"{i} is valid!")
"""
